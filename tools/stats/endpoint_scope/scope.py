"""Scope out stats.nba.com endpoints by differential probing.

stats.nba.com no longer explains itself: an empty request returns a bare HTTP 500
and invalid values return ``{"Param": ["Invalid parameters"]}`` without the regex
patterns the old ``endpoint_analysis`` tool parsed. So instead of starting from an
empty request, this starts from a request known to work (the library's own
endpoint class, or a URL copied from the browser) and changes one thing at a time:

- baseline:  the known-good request -> datasets / JSON shape, drift vs expected_data
- echo:      parameters the server echoes back that we do not send (new upstream)
- required:  drop parameters; HTTP 500 means one of them is required
- nullable:  blank parameters; anything still 200 accepts ""
- validated: garbage values; HTTP 400 names every parameter the server validates
- values:    (opt-in) every value of the related parameters.py classes, to find
             which enum class actually fits and which offered values are rejected
- cassette:  live JSON key paths vs the recorded VCR cassette, which catches new
             fields in nested endpoints that the parser silently ignores

Groups of parameters are tested together and bisected only when a group fails,
so a 40-parameter endpoint costs ~15 requests rather than ~120. Responses are
cached on disk, so re-running a report is free.
"""

import hashlib
import inspect
import json
import os
import re
import time
from contextlib import contextmanager
from datetime import datetime
from urllib.parse import parse_qsl, urlencode, urlparse

import requests

import nba_api.stats.endpoints as endpoints
from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP, NBAStatsResponse
from tools.stats.endpoint_scope.knowledge import (
    MAX_VALUES_PER_PARAMETER,
    SKIP_VALUE_DISCOVERY,
    library_parameter_classes,
    load_cassette,
    parameter_family,
    shape_diff,
    summarize_values,
    unparsed_fields,
)

GARBAGE = "zz~"
# Statuses that mean "slow down" or "blocked", never a verdict on a parameter.
THROTTLE_STATUSES = {403, 429, 502, 503, 504}
# Extra wait before each retry of a failed or throttled request.
RETRY_DELAYS = (0, 5, 15)
# Required args the integration PARAM_DEFAULTS do not cover.
FALLBACK_ARGS = {"game_date": "2025-01-15"}
CACHE_DIR = os.path.join(os.path.expanduser("~"), ".cache", "nba_api", "endpoint_scope")
PRIORS_PATH = os.path.join(CACHE_DIR, "parameter_priors.json")


_last_request = [0.0]  # monotonic start time of the last live request, any prober


def _wait(seconds):
    """Sleep so live requests start at least ``seconds`` apart.

    The gap is measured from the previous request's start, so time spent
    waiting for a response counts towards it.
    """
    remaining = _last_request[0] + seconds - time.monotonic()
    if remaining > 0:
        time.sleep(remaining)
    _last_request[0] = time.monotonic()


class NetworkError(Exception):
    """Raised instead of returning a status, so a timeout is never read as a 500."""


class Priors:
    """Per-parameter outcomes remembered across endpoints and runs.

    Dashboard endpoints share ~30 parameters that fail the same way everywhere
    (LastNGames, Month, MeasureType, ...). Testing likely failures one at a time
    keeps them from poisoning the group tests for everything else.
    """

    KINDS = ("required", "non_nullable", "crash")

    def __init__(self, path=PRIORS_PATH, enabled=True):
        self.path = path
        self.enabled = enabled
        self.facts = {}
        if enabled and os.path.exists(path):
            with open(path) as f:
                stored = json.load(f)
            # A short-lived format nested the names under "names".
            self.facts = stored.get("names", stored) if "types" in stored else stored

    def suspects(self, kind):
        return {name for name, facts in self.facts.items() if facts.get(kind)}

    @staticmethod
    def _rate(facts, kind):
        # Older entries have no "seen": count them as seen as often as they failed.
        seen = facts.get("seen") or max(facts.get(k, 0) for k in Priors.KINDS) or 1
        return facts.get(kind, 0) / seen

    def likely(self, kind, params, threshold=0.0):
        """Params whose past failure rate for ``kind`` is above ``threshold``."""
        return {
            name
            for name in params
            if name in self.facts and self._rate(self.facts[name], kind) > threshold
        }

    def record(self, report):
        if not self.enabled:
            return
        outcomes = {
            "required": set(report["required_parameters"]),
            "non_nullable": set(report["parameters"])
            - set(report["nullable_parameters"]),
            "crash": set(report["type_checked_parameters"]),
        }
        for name in report["parameters"]:
            facts = self.facts.setdefault(name, dict.fromkeys(self.KINDS, 0))
            if "seen" not in facts:
                facts["seen"] = max(facts.get(k, 0) for k in self.KINDS)
            facts["seen"] += 1
            for kind in self.KINDS:
                facts[kind] = facts.get(kind, 0) + (name in outcomes[kind])

    def overridden_by(self, report):
        """A copy in which ``report``'s outcomes replace these for its params.

        An endpoint's own last run predicts its next one better than how the
        same names behaved elsewhere. Nothing is saved from the copy.
        """
        if not self.enabled or not report or "required_parameters" not in report:
            return self
        copy = Priors(enabled=False)
        copy.enabled = True
        names = set(report["parameters"])
        copy.facts = {k: v for k, v in self.facts.items() if k not in names}
        copy.record(report)
        return copy

    def save(self):
        os.makedirs(os.path.dirname(self.path), exist_ok=True)
        with open(self.path, "w") as f:
            json.dump(self.facts, f, indent=1, sort_keys=True)


def redact(text):
    """Strip credentials from proxy URLs so they never reach the terminal."""
    return re.sub(r"\b[a-z0-9+]+://[^\s'\"/@]+@[^\s'\"]*", "<proxy>", str(text))


class Prober:
    """Sends requests for one endpoint, with caching, pacing, and a request log."""

    def __init__(self, endpoint, pause=0.6, proxy="", cache_ttl=86400, timeout=20):
        self.endpoint = endpoint
        self.pause = pause
        self.proxy = proxy
        self.cache_ttl = cache_ttl
        self.timeout = timeout
        self.requests_sent = 0
        self.cache_hits = 0
        self.phase = "baseline"
        self.phases = {}
        self.seconds = 0.0
        self.log = []  # (phase, parameters, status) for every lookup

    def _count(self, kind):
        counts = self.phases.setdefault(self.phase, {"sent": 0, "cached": 0})
        counts[kind] += 1

    def _cache_path(self, parameters):
        key = f"{self.endpoint}?{urlencode(sorted(parameters.items()))}"
        digest = hashlib.sha1(key.encode()).hexdigest()
        return os.path.join(CACHE_DIR, f"{self.endpoint}-{digest}.json")

    def send(self, parameters, use_cache=True):
        """Return (status_code, NBAStatsResponse or None)."""
        parameters = {k: ("" if v is None else v) for k, v in parameters.items()}
        cache_path = self._cache_path(parameters)
        fresh = (
            use_cache
            and self.cache_ttl
            and os.path.exists(cache_path)
            and time.time() - os.path.getmtime(cache_path) < self.cache_ttl
        )
        if fresh:
            with open(cache_path) as f:
                cached = json.load(f)
            self.cache_hits += 1
            self._count("cached")
            self.log.append((self.phase, parameters, cached["status"]))
            response = NBAStatsResponse(cached["body"], cached["status"], cached["url"])
            return cached["status"], response

        start = time.monotonic()
        for delay in RETRY_DELAYS:
            time.sleep(delay)  # backoff counts from the failure, not the request
            _wait(self.pause)
            self.requests_sent += 1
            self._count("sent")
            try:
                response = NBAStatsHTTP().send_api_request(
                    endpoint=self.endpoint,
                    parameters=parameters,
                    proxy=self.proxy,
                    timeout=self.timeout,
                )
            except requests.exceptions.InvalidSchema as e:
                raise SystemExit(f"Proxy misconfigured: {redact(e)}") from None
            except requests.exceptions.RequestException as e:
                last_error = f"{type(e).__name__}: {redact(e)}"
                continue
            if response._status_code not in THROTTLE_STATUSES:
                break
            last_error = f"HTTP {response._status_code} (throttled or blocked?)"
        else:
            self.seconds += time.monotonic() - start
            raise NetworkError(last_error)
        self.seconds += time.monotonic() - start

        status = response._status_code
        self.log.append((self.phase, parameters, status))
        os.makedirs(CACHE_DIR, exist_ok=True)
        with open(cache_path, "w") as f:
            json.dump(
                {"status": status, "body": response.get_response(), "url": None}, f
            )
        return status, response

    def ok(self, parameters):
        return self.send(parameters)[0] == 200

    def recheck(self, parameters):
        """Like ``ok``, but always asks the server again."""
        return self.send(parameters, use_cache=False)[0] == 200


@contextmanager
def phase(prober, name):
    """Attribute the requests sent inside the block to ``name``."""
    previous = getattr(prober, "phase", "")
    prober.phase = name
    try:
        yield
    finally:
        prober.phase = previous


def _confirm(prober, parameters):
    """A request that only checks a failure the bisection already inferred."""
    with phase(prober, f"{getattr(prober, 'phase', '')}:confirm"):
        return prober.ok(parameters)


def bisect_failures(params, keys, mutate, prober, interactions=None):
    """Return the keys in ``keys`` that break the request when ``mutate``d alone.

    Tests the whole group first and only splits groups that fail, so the cost is
    roughly (failures * log2(len(keys))) requests instead of len(keys). When the
    left half of a failing group passes, the right half's group test is skipped
    as it must fail -- unless keys only fail in combination. So every reported
    key is confirmed by a request that mutates it alone, and a failing group no
    single key explains is appended to ``interactions`` instead.
    """
    interactions = [] if interactions is None else interactions
    return _bisect(params, keys, mutate, prober, interactions, False)[0]


def _bisect(params, keys, mutate, prober, interactions, inferred):
    """Return (failures, group_passed). ``inferred``: group failure not tested."""
    if not keys:
        return [], True
    if not inferred and prober.ok(mutate(params, keys)):
        return [], True
    if len(keys) == 1:
        if inferred and _confirm(prober, mutate(params, keys)):
            return [], True
        return list(keys), False
    mid = len(keys) // 2
    left, left_passed = _bisect(params, keys[:mid], mutate, prober, interactions, False)
    right, _ = _bisect(params, keys[mid:], mutate, prober, interactions, left_passed)
    if not left and not right:
        if inferred and _confirm(prober, mutate(params, keys)):
            return [], True
        interactions.append(sorted(keys))
    return left + right, False


def find_failures(params, keys, mutate, prober, suspects=(), interactions=None):
    """Like bisect_failures, but tests likely failures one at a time first."""
    likely = [k for k in keys if k in suspects]
    rest = [k for k in keys if k not in suspects]
    with phase(prober, f"{getattr(prober, 'phase', '')}:suspect"):
        failures = [k for k in likely if not prober.ok(mutate(params, [k]))]
    return failures + bisect_failures(params, rest, mutate, prober, interactions)


def drop(params, keys):
    return {k: v for k, v in params.items() if k not in keys}


def blank(params, keys):
    return {k: ("" if k in keys else v) for k, v in params.items()}


def garbage_value(value):
    """An invalid value of the right type.

    Strings sent to integer params make the server 500 without naming the
    param, but an out-of-range integer gets a 400 that names it, so integers
    can be validated in the same request as everything else.
    """
    return "-1" if str(value).isdigit() else GARBAGE


def garbage(params, keys):
    return {k: (garbage_value(v) if k in keys else v) for k, v in params.items()}


def find_validated(params, keys, prober, validated, crashes):
    """Send garbage; a 400 names validated params, a 500 needs bisecting."""
    if not keys:
        return
    status, response = prober.send(garbage(params, keys))
    if status == 400 and response.valid_json():
        lowered = {k.lower(): k for k in keys}
        for name, messages in response.get_dict().items():
            # Error keys can be "DateTo.Date" or camelCase "seasonType".
            base = name.split(".")[0].lower()
            validated[lowered.get(base, name)] = messages
        # Params that 400 did not name might still crash on their own; recheck.
        rest = [k for k in keys if k.lower() not in {n.lower() for n in validated}]
        if rest and len(rest) < len(keys):
            find_validated(params, rest, prober, validated, crashes)
        return
    if status == 200:
        return
    if len(keys) == 1:
        crashes[keys[0]] = status
        return
    mid = len(keys) // 2
    find_validated(params, keys[:mid], prober, validated, crashes)
    find_validated(params, keys[mid:], prober, validated, crashes)


def json_shape(value, depth=0, max_depth=4):
    """Compact type skeleton of a JSON value (first list element only)."""
    if depth >= max_depth:
        return "..."
    if isinstance(value, dict):
        return {k: json_shape(v, depth + 1, max_depth) for k, v in value.items()}
    if isinstance(value, list):
        return [json_shape(value[0], depth + 1, max_depth)] if value else []
    return type(value).__name__


def list_endpoint_classes():
    classes = {}
    for name in endpoints.__all__:
        module = getattr(endpoints, name, None)
        for _, cls in inspect.getmembers(module, inspect.isclass):
            if issubclass(cls, Endpoint) and getattr(cls, "endpoint", None):
                classes[cls.endpoint.lower()] = cls
    return classes


def baseline_from_class(cls):
    """Known-good parameters for a library endpoint, via the integration specs."""
    from tests.integration.helpers.endpoint_specs import endpoint_specs
    from tests.integration.helpers.models import EndpointSpec

    spec = next((s for s in endpoint_specs if s.endpoint_class is cls), None)
    overrides = dict(spec.overrides) if spec else {}
    note = (spec.skip or spec.deprecated) if spec else "no EndpointSpec"
    try:
        instance = EndpointSpec(cls, get_request=False, **overrides)()
    except ValueError:
        overrides = {**FALLBACK_ARGS, **overrides}
        try:
            instance = EndpointSpec(cls, get_request=False, **overrides)()
        except ValueError as e:
            return {}, f"cannot build a baseline ({e}); pass a full URL instead"
    return dict(instance.parameters), note


def scope_endpoint(
    endpoint,
    params,
    cls=None,
    note=None,
    offline=False,
    values=None,
    priors=None,
    previous=None,
    **prober_kwargs,
):
    """Build a report for one endpoint.

    ``previous`` is this endpoint's report from an earlier run, if any: its
    outcomes are the best guess at what will fail now, though everything is
    still tested.

    ``offline`` reads the baseline from the VCR cassette and skips probing.
    ``values`` is None (skip), an empty set (all validated params), or a set of
    parameter names to run enum discovery on.
    """
    prober = Prober(endpoint, **prober_kwargs)
    priors = priors or Priors(enabled=False)
    report = {
        "endpoint": endpoint,
        "class": cls.__name__ if cls else None,
        "note": note,
        "baseline_parameters": params,
        "last_validated_date": str(datetime.now().date()),
        "flags": [],
    }
    recorded_params, recorded = load_cassette(cls, endpoint) if cls else (None, None)

    if offline:
        if recorded is None:
            report["status"] = "no-cassette"
            return report
        params = report["baseline_parameters"] = recorded_params
        response = NBAStatsResponse(json.dumps(recorded), 200, None)
    else:
        try:
            status, response = prober.send(params)
        except NetworkError as e:
            return _network_failure(report, prober, e)
        report["baseline_status"] = status
        if status != 200 or not response.valid_json():
            report["status"] = "baseline-failed"
            report["baseline_body"] = response.get_response()[:300] if response else ""
            _record_cost(report, prober)
            return report

    raw = response.get_dict()
    describe_response(report, endpoint, cls, response, raw, params)
    if not offline and recorded is not None:
        diff = shape_diff(recorded, raw)
        report["cassette_diff"] = diff
        if diff["added"] or diff["removed"]:
            report["flags"].append("response shape changed since cassette")

    if not offline:
        try:
            probe_parameters(report, params, prober, priors.overridden_by(previous))
            priors.record(report)
            if values is not None:
                with phase(prober, "values"):
                    report["values"] = discover_values(
                        report, params, cls, prober, values
                    )
        except NetworkError as e:
            return _network_failure(report, prober, e)
        for parameter, verdict in report.get("values", {}).items():
            if verdict["library_offers_rejected"]:
                report["flags"].append(f"{parameter}: library offers rejected values")

    report["status"] = "drift" if report["flags"] else "success"
    _record_cost(report, prober)
    return report


def _record_cost(report, prober):
    report["requests"] = prober.requests_sent
    report["cache_hits"] = prober.cache_hits
    report["phases"] = prober.phases
    report["seconds"] = round(prober.seconds, 1)


def _network_failure(report, prober, error):
    """Partial probe results are untrustworthy; say so instead of guessing."""
    report["status"] = "network-error"
    report["error"] = str(error)[:200]
    _record_cost(report, prober)
    return report


def describe_response(report, endpoint, cls, response, raw, params):
    """Datasets, drift against expected_data, parser coverage, parameter echo."""
    tabular = bool({"resultSets", "resultSet"} & set(raw))
    report["format"] = "tabular" if tabular else "nested"
    if tabular:
        report["data_sets"] = response.get_headers_from_data_sets()
    else:
        report["json_shape"] = json_shape(raw)
        try:
            parsed = response.get_data_sets(endpoint)
            report["data_sets"] = {k: v["headers"] for k, v in parsed.items()}
        except Exception as e:  # no parser registered, or parser broke
            report["data_sets"] = {}
            report["parser_error"] = f"{type(e).__name__}: {e}"[:200]
            report["flags"].append("parser error")
        report["unparsed_fields"] = unparsed_fields(raw, report["data_sets"])

    if cls is not None:
        report["drift"] = dataset_drift(cls.expected_data, report["data_sets"])
        if report["drift"]:
            report["flags"].append("datasets differ from expected_data")

    echoed = response.get_parameters() or raw.get("params") or {}
    sent = {k.lower() for k in params}
    report["server_only_parameters"] = sorted(
        k for k in echoed if k.lower() not in sent
    )
    report["not_echoed_parameters"] = (
        sorted(k for k in params if k.lower() not in {e.lower() for e in echoed})
        if echoed
        else None
    )
    if report["server_only_parameters"]:
        report["flags"].append("server accepts params the library does not send")


# How probe_parameters picks what to test one at a time. LEGACY is the
# algorithm the first full run used; truth.py scores both against ground truth.
STRATEGY = {
    "blank_first": True,
    # Test a param alone when it failed this way on more than this share of the
    # endpoints it was seen on (below that, a group test is cheaper).
    "threshold": {"required": 0.0, "non_nullable": 0.2, "crash": 0.3},
    "priors_beat_hints": True,
    "merge_drop_groups": True,
    "drop_priors": True,
}
LEGACY_STRATEGY = {
    **STRATEGY,
    "blank_first": False,
    "threshold": {},
    "priors_beat_hints": False,
    "merge_drop_groups": False,
    "drop_priors": False,
}


def recheck_surprises(params, prober, priors, required, non_nullable):
    """Ask again, uncached, about failures that contradict what is known.

    A transient 500 looks exactly like a required or non-null parameter; the
    first full run's one wrong decision (CommonTeamRoster TeamID "required")
    was one. Missing and "" both mean "unset" to the server, so a required
    param that accepts "" is suspect, as is a failure for a param that never
    failed that way on two or more other endpoints. That is ~10 requests a run.
    Removes the failures that do not reproduce from ``required`` and
    ``non_nullable`` in place.
    """

    def surprising(name, kind):
        facts = priors.facts.get(name)
        return bool(facts) and facts.get("seen", 0) >= 2 and not facts.get(kind)

    recheck = getattr(prober, "recheck", prober.ok)
    with phase(prober, "recheck"):
        for key in list(required):
            suspect = key not in non_nullable or surprising(key, "required")
            if suspect and recheck(drop(params, [key])):
                required.remove(key)
        for key in list(non_nullable):
            if surprising(key, "non_nullable") and recheck(blank(params, [key])):
                non_nullable.remove(key)


def probe_parameters(report, params, prober, priors=None, strategy=None):
    """Required / nullable / validated parameters by differential probing."""
    priors = priors or Priors(enabled=False)
    s = {**STRATEGY, **(strategy or {})}
    # Only params with a value can be required or non-nullable in practice; check
    # the blank ones as a single group so a surprise still gets caught.
    keys = sorted(params)
    filled = [k for k in keys if params[k] not in ("", None)]
    empty = [k for k in keys if k not in filled]
    numeric = {k for k in keys if str(params[k]).isdigit()}
    # Numbers are a cold-start hint; what earlier endpoints showed wins. LeagueID
    # "00" looks numeric but accepted "" on 86 of 117 endpoints.
    hints = numeric - set(priors.facts) if s["priors_beat_hints"] else numeric

    def likely(kind):
        return priors.likely(kind, params, s["threshold"].get(kind, 0.0))

    interactions = {"drop": [], "blank": []}

    def find_required(suspects):
        with phase(prober, "drop"):
            if s["merge_drop_groups"]:
                return find_failures(
                    params, keys, drop, prober, suspects, interactions["drop"]
                )
            found = find_failures(
                params, filled, drop, prober, suspects, interactions["drop"]
            )
            return found + bisect_failures(
                params, empty, drop, prober, interactions["drop"]
            )

    def find_non_nullable(suspects):
        with phase(prober, "blank"):
            return find_failures(
                params, filled, blank, prober, suspects, interactions["blank"]
            )

    if s["blank_first"]:
        non_nullable = find_non_nullable(likely("non_nullable") | hints)
        # In a full run 83% of non-null params were required and 1 of ~320
        # nullable ones was (CommonTeamRoster TeamID): test the former alone and
        # the latter as a group, which still catches that one. Non-null params
        # that were never required elsewhere (V3 StartRange, ...) join the group.
        suspects = set(non_nullable)
        if s["drop_priors"]:
            suspects -= {k for k in priors.facts if k not in likely("required")}
        required = find_required(suspects)
    else:
        required = find_required(likely("required") | hints)
        # Required params almost always reject "" too: test them one at a time
        # so they don't poison the group tests for everything else.
        non_nullable = find_non_nullable(set(required) | likely("non_nullable") | hints)
    recheck_surprises(params, prober, priors, required, non_nullable)
    report["required_parameters"] = sorted(required)
    # Groups that fail although no single key does: e.g. "PlayerID or TeamID".
    report["interactions"] = {k: v for k, v in interactions.items() if v}
    if report["interactions"]:
        report.setdefault("flags", []).append(
            f"parameters only fail together: {report['interactions']}"
        )
    report["nullable_parameters"] = sorted(k for k in keys if k not in non_nullable)

    # Garbage values: one request usually names every validated param in its
    # 400. Params that 500 instead (dates, mostly) poison that request, so the
    # ones known to do so elsewhere are isolated first.
    validated, crashes = {}, {}
    suspects = [k for k in keys if k in likely("crash") - numeric]
    with phase(prober, "garbage:suspect"):
        for key in suspects:
            find_validated(params, [key], prober, validated, crashes)
    others = [k for k in keys if k not in suspects]
    with phase(prober, "garbage"):
        find_validated(params, others, prober, validated, crashes)
    report["validated_parameters"] = validated
    report["type_checked_parameters"] = crashes
    report["numeric_parameters"] = sorted(numeric)
    report["unvalidated_parameters"] = sorted(
        k for k in keys if k not in validated and k not in crashes
    )

    # analysis.json-compatible keys so the old generators can still consume this.
    report["parameters"] = keys
    report["parameter_patterns"] = dict.fromkeys(keys)


def response_data(response):
    """The data in a response, without the parameter echo and metadata."""
    if response is None or not response.valid_json():
        return None
    body = response.get_dict()
    if not isinstance(body, dict):
        return body
    return {k: v for k, v in body.items() if k not in ("parameters", "params", "meta")}


def row_count(data):
    """Rows across a tabular response's datasets; None if not tabular."""
    if not isinstance(data, dict):
        return None
    sets = data.get("resultSets") or data.get("resultSet")
    if isinstance(sets, dict):
        sets = [sets]
    if not isinstance(sets, list):
        return None
    return sum(len(s.get("rowSet", [])) for s in sets if isinstance(s, dict))


def discover_values(report, params, cls, prober, only):
    """Try every value of the related parameters.py classes, one request each.

    A 200 only says the server did not reject a value; it may still ignore it.
    Values whose data is identical to the baseline's are listed separately as
    ``no_effect`` (free: the baseline response is cached). When the baseline has
    no rows that comparison means nothing, so ``no_effect`` is None.
    """
    library = library_parameter_classes(cls)
    baseline = response_data(prober.send(params)[1])
    comparable = row_count(baseline) != 0
    if not comparable:
        report["flags"].append("baseline has no rows: value effects not checked")
    results = {}
    for parameter in sorted(report["validated_parameters"]):
        if parameter in SKIP_VALUE_DISCOVERY or parameter not in params:
            continue
        if only and parameter not in only:
            continue
        family = parameter_family(parameter, library.get(parameter))
        candidates = sorted(set().union(*family.values())) if family else []
        if not candidates or len(candidates) > MAX_VALUES_PER_PARAMETER:
            continue
        accepted, rejected, no_effect = set(), set(), set()
        for value in candidates:
            status, response = prober.send({**params, parameter: value})
            (accepted if status == 200 else rejected).add(value)
            same = status == 200 and response_data(response) == baseline
            if same and value != str(params[parameter]):
                no_effect.add(value)
        results[parameter] = summarize_values(
            parameter, family, library.get(parameter), accepted, rejected
        )
        results[parameter]["no_effect"] = sorted(no_effect) if comparable else None
    return results


def flat_headers(headers):
    """Multi-level headers (shot locations) as "LEVEL:column" strings."""
    flat = []
    for header in headers:
        if isinstance(header, dict):
            flat += [f"{header.get('name')}:{c}" for c in header.get("columnNames", [])]
        else:
            flat.append(header)
    return flat


def dataset_drift(expected, actual):
    drift = {}
    expected = {k: flat_headers(v) for k, v in expected.items()}
    actual = {k: flat_headers(v) for k, v in actual.items()}
    # Same columns under a different name: expected_data is keyed differently
    # from the parser's dataset name, which is a naming bug rather than drift.
    for exp_name in [n for n in expected if n not in actual]:
        for act_name in [n for n in actual if n not in expected]:
            if list(expected[exp_name]) == list(actual[act_name]):
                drift[exp_name] = f"expected_data key; response calls it {act_name}"
                expected = {k: v for k, v in expected.items() if k != exp_name}
                actual = {k: v for k, v in actual.items() if k != act_name}
                break
    for name in sorted(set(expected) | set(actual)):
        if name not in actual:
            drift[name] = "dataset missing from response"
        elif name not in expected:
            drift[name] = {"new dataset": actual[name]}
        else:
            added = list(
                dict.fromkeys(c for c in actual[name] if c not in expected[name])
            )
            removed = list(
                dict.fromkeys(c for c in expected[name] if c not in actual[name])
            )
            if added or removed:
                drift[name] = {"added": added, "removed": removed}
    return drift


def resolve_targets(names, classes):
    """Yield (endpoint, params, cls, note) for names, class names, or URLs."""
    for name in names:
        if "://" in name or "?" in name:
            parsed = urlparse(name if "://" in name else f"https://x/{name}")
            endpoint = parsed.path.rstrip("/").split("/")[-1].lower()
            params = dict(parse_qsl(parsed.query, keep_blank_values=True))
            yield endpoint, params, classes.get(endpoint), "from URL"
            continue
        cls = classes.get(name.lower())
        if cls is None:
            yield name.lower(), {}, None, "unknown endpoint; pass a full URL instead"
            continue
        params, note = baseline_from_class(cls)
        yield cls.endpoint, params, cls, note


def format_report(r):
    lines = [f"\n== {r['endpoint']}  [{r['status']}]"]
    if r.get("note"):
        lines.append(f"   note: {r['note']}")
    if r["status"] == "no-cassette":
        return "\n".join(lines)
    if r["status"] == "network-error":
        lines.append(
            f"   {r['error']}  (after {r['requests']} requests; results discarded)"
        )
        return "\n".join(lines)
    if r["status"] == "baseline-failed":
        lines.append(f"   baseline HTTP {r['baseline_status']}: {r['baseline_body']!r}")
        lines.append(f"   sent: {r['baseline_parameters']}")
        return "\n".join(lines)
    lines.append(
        f"   format: {r['format']}   requests: {r['requests']}"
        f" (+{r['cache_hits']} cached)  {r.get('seconds', 0)}s"
    )
    if r.get("phases"):
        lines.append(f"   by phase: {format_phases(r['phases'])}")
    for flag in r["flags"]:
        lines.append(f"   ! {flag}")
    for name, headers in r["data_sets"].items():
        lines.append(f"   dataset {name}: {len(headers)} cols")
    if r.get("parser_error"):
        lines.append(f"   parser error: {r['parser_error']}")
    for name, change in (r.get("drift") or {}).items():
        lines.append(f"   DRIFT {name}: {change}")
    diff = r.get("cassette_diff") or {}
    for kind in ("added", "removed"):
        if diff.get(kind):
            lines.append(f"   CASSETTE {kind}: {_clip(diff[kind])}")
    if r.get("unparsed_fields"):
        lines.append(f"   unparsed fields: {_clip(list(r['unparsed_fields']))}")
    if r["server_only_parameters"]:
        lines.append(f"   NEW upstream params: {r['server_only_parameters']}")
    if r["not_echoed_parameters"]:
        lines.append(f"   sent but not echoed: {r['not_echoed_parameters']}")
    if "required_parameters" not in r:  # offline: no probing
        return "\n".join(lines)
    lines.append(f"   required:   {r['required_parameters']}")
    non_nullable = [p for p in r["parameters"] if p not in r["nullable_parameters"]]
    lines.append(f"   non-null:   {non_nullable}")
    validated = {k: v[0] if v else "" for k, v in r["validated_parameters"].items()}
    lines.append(f"   validated:  {validated}")
    if r["type_checked_parameters"]:
        lines.append(f"   500 on bad type: {sorted(r['type_checked_parameters'])}")
    lines.append(f"   free-form:  {r['unvalidated_parameters']}")
    for parameter, v in (r.get("values") or {}).items():
        line = f"   values {parameter}: fits {v['best_fit_classes']}"
        if v["library_class"] and v["library_class"] not in v["best_fit_classes"]:
            line += f" (library uses {v['library_class']})"
        if v["library_offers_rejected"]:
            line += f"; REJECTED but offered: {v['library_offers_rejected']}"
        if v["accepted_but_missing_from_library"]:
            line += f"; also accepts: {v['accepted_but_missing_from_library']}"
        lines.append(line)
    return "\n".join(lines)


def format_phases(phases):
    """{"drop": {"sent": 3, "cached": 1}} -> "drop 4" (sent + cached lookups)."""
    return ", ".join(
        f"{name} {counts['sent'] + counts['cached']}"
        for name, counts in sorted(phases.items())
    )


def _clip(items, limit=12):
    items = list(items)
    more = f" ... +{len(items) - limit} more" if len(items) > limit else ""
    return ", ".join(items[:limit]) + more
