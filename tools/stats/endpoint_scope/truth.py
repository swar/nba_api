"""Ground truth for endpoint_scope: every parameter tested on its own, uncached.

The scoper tests parameters in groups and infers what it can, so agreement
between two versions of it proves nothing. This checks it against the server
instead. For each parameter of a known-good request it sends, one at a time:
the parameter dropped, blanked (if it had a value), set to the string garbage
value, and set to -1 (if numeric). Every non-200 is sent again to check the
server answers the same way twice.

    python -m tools.stats.endpoint_scope.truth record leaguedashteamstats URL ... --out truth.json
    python -m tools.stats.endpoint_scope.truth score truth.json [--simulate] [--priors FILE]

``score`` runs the scoper uncached against each recorded endpoint, cold (no
priors) and warm, and compares four decisions per parameter: required,
non-null, validated (a typed invalid value gets a 400 naming it), and
type-checked (a typed invalid value fails some other way). ``--simulate``
answers from the truth file instead of the network. That assumes a group of
changes fails exactly when one of its changes fails alone, so it is only good
for screening ideas; ``--check-simulator`` measures how often that assumption
held for the group requests a live ``score`` actually sent.
"""

import argparse
import json
import os
import time

from nba_api.stats.library.http import NBAStatsResponse
from tools.stats.endpoint_scope.scope import (
    GARBAGE,
    LEGACY_STRATEGY,
    PRIORS_PATH,
    STRATEGY,
    Priors,
    Prober,
    list_endpoint_classes,
    probe_parameters,
    resolve_targets,
)

DECISIONS = ("required", "non_null", "validated", "type_checked")


def named_in(response, parameter):
    """Whether a 400 body names ``parameter`` (keys like "DateTo.Date" count)."""
    if response is None or not response.valid_json():
        return False
    body = response.get_dict()
    if not isinstance(body, dict):
        return False
    return any(k.split(".")[0].lower() == parameter.lower() for k in body)


def mutations(params, name):
    """The single-key changes ground truth sends for one parameter."""
    value = params[name]
    yield "drop", {k: v for k, v in params.items() if k != name}
    if value not in ("", None):
        yield "blank", {**params, name: ""}
    yield "garbage", {**params, name: GARBAGE}
    if str(value).isdigit():
        yield "negative", {**params, name: "-1"}


def record_truth(endpoint, params, prober):
    """Send every single-key mutation; repeat non-200s to check determinism."""
    probes = {}
    for name in sorted(params):
        probes[name] = {}
        for kind, mutated in mutations(params, name):
            status, response = prober.send(mutated)
            entry = {"status": status, "named": named_in(response, name)}
            if status == 400 and response is not None and response.valid_json():
                entry["body"] = response.get_dict()
            if status != 200:
                entry["repeat"] = prober.send(mutated)[0]
            probes[name][kind] = entry
    return {
        "endpoint": endpoint,
        "params": params,
        "probes": probes,
        "requests": prober.requests_sent,
        "recorded": time.strftime("%Y-%m-%d %H:%M"),
    }


def classify(truth):
    """Expected decisions per parameter, from single-key probes alone."""
    expected = {}
    for name, probes in truth["probes"].items():
        typed = probes["negative" if "negative" in probes else "garbage"]
        validated = typed["status"] == 400 and typed["named"]
        expected[name] = {
            "required": probes["drop"]["status"] != 200,
            "non_null": "blank" in probes and probes["blank"]["status"] != 200,
            "validated": validated,
            "type_checked": typed["status"] != 200 and not validated,
        }
    return expected


def flaky(truth):
    """Probes whose repeat disagreed with the first answer."""
    return [
        f"{name}:{kind}"
        for name, probes in truth["probes"].items()
        for kind, entry in probes.items()
        if "repeat" in entry and entry["repeat"] != entry["status"]
    ]


def decisions(report):
    """The scoper's report in the same shape as ``classify``."""
    nullable = set(report["nullable_parameters"])
    return {
        name: {
            "required": name in report["required_parameters"],
            "non_null": name not in nullable,
            "validated": name in report["validated_parameters"],
            "type_checked": name in report["type_checked_parameters"],
        }
        for name in report["parameters"]
    }


def compare(expected, actual):
    """Return (correct, total, mistakes)."""
    correct, mistakes = 0, []
    for name, want in expected.items():
        got = actual.get(name, {})
        for decision in DECISIONS:
            if got.get(decision) == want[decision]:
                correct += 1
            else:
                mistakes.append(f"{name}.{decision}: want {want[decision]}")
    return correct, len(expected) * len(DECISIONS), mistakes


class SimulatedProber:
    """Answers from a truth file: a group fails iff one of its changes does.

    A group containing any change that fails with something other than a 400
    gets that status; otherwise the 400 bodies of the failing changes merge.
    """

    def __init__(self, truth, pause=0.0):
        self.truth = truth
        self.baseline = truth["params"]
        self.requests_sent = 0
        self.cache_hits = 0
        self.phase = "baseline"
        self.phases = {}
        self.seconds = 0.0
        self.log = []

    def _single(self, name, parameters):
        probes = self.truth["probes"][name]
        if name not in parameters:
            return probes["drop"]
        kind = {"": "blank", GARBAGE: "garbage", "-1": "negative"}.get(
            str(parameters[name])
        )
        if kind is None or kind not in probes:
            raise KeyError(f"truth has no answer for {name}={parameters[name]!r}")
        return probes[kind]

    def send(self, parameters, use_cache=True):
        self.requests_sent += 1
        counts = self.phases.setdefault(self.phase, {"sent": 0, "cached": 0})
        counts["sent"] += 1
        changed = [
            k
            for k in self.baseline
            if k not in parameters or str(parameters[k]) != str(self.baseline[k])
        ]
        answers = [self._single(k, parameters) for k in changed]
        failing = [a for a in answers if a["status"] != 200]
        hard = [a["status"] for a in failing if a["status"] != 400]
        if not failing:
            status, body = 200, json.dumps({"resultSets": []})
        elif hard:
            status, body = hard[0], ""
        else:
            merged = {}
            for answer in failing:
                merged.update(answer.get("body", {}))
            status, body = 400, json.dumps(merged)
        self.log.append((self.phase, parameters, status))
        return status, NBAStatsResponse(body, status, None)

    def ok(self, parameters):
        return self.send(parameters)[0] == 200


def score_one(truth, priors, prober, strategy=None):
    """Run the scoper's parameter probing and grade it against ``truth``."""
    report = {"baseline_parameters": dict(truth["params"])}
    start = time.monotonic()
    probe_parameters(report, dict(truth["params"]), prober, priors, strategy)
    elapsed = time.monotonic() - start
    correct, total, mistakes = compare(classify(truth), decisions(report))
    return {
        "correct": correct,
        "total": total,
        "mistakes": mistakes,
        # +1: the baseline request every real run sends first.
        "requests": prober.requests_sent + prober.cache_hits + 1,
        "seconds": round(elapsed, 1),
        "phases": prober.phases,
        "interactions": report.get("interactions", {}),
        "log": prober.log,
        "report": report,
    }


def score(truths, simulate=False, priors_path=PRIORS_PATH, pause=0.6, strategy=None):
    """Grade the scoper cold and warm on every recorded endpoint."""
    results = {}
    for endpoint, truth in truths.items():
        results[endpoint] = {}
        for mode in ("cold", "warm"):
            # A fresh copy per endpoint, so results don't depend on order.
            priors = Priors(path=priors_path, enabled=mode == "warm")
            if simulate:
                prober = SimulatedProber(truth)
            else:
                prober = Prober(endpoint, pause=pause, proxy="", cache_ttl=0)
            results[endpoint][mode] = score_one(truth, priors, prober, strategy)
    return results


def proxy_truth(report):
    """A truth entry built from a probed report, for costing whole runs.

    Every failure in a report was confirmed by a single-key request, so this is
    a fair model of the server for the requests the scoper sends. It has no
    answers for values the scoper never sent.
    """
    params = report["baseline_parameters"]
    nullable = set(report["nullable_parameters"])
    probes = {}
    for name, value in params.items():
        failed = {"status": 500, "named": False}
        passed = {"status": 200, "named": False}
        entry = {"drop": failed if name in report["required_parameters"] else passed}
        if value not in ("", None):
            entry["blank"] = passed if name in nullable else failed
        typed = "negative" if str(value).isdigit() else "garbage"
        if name in report["validated_parameters"]:
            messages = report["validated_parameters"][name]
            entry[typed] = {"status": 400, "named": True, "body": {name: messages}}
        elif name in report["type_checked_parameters"]:
            status = report["type_checked_parameters"][name]
            entry[typed] = {"status": status, "named": False}
        else:
            entry[typed] = passed
        probes[name] = entry
    return {"endpoint": report["endpoint"], "params": params, "probes": probes}


def simulate_run(reports, priors_facts=None, strategy=None):
    """Replay a full run against proxy truth, priors evolving as they would.

    Returns {endpoint: {"lookups", "correct", "total", "phases"}}.
    """
    priors = Priors(enabled=False)  # in memory only: never read or saved
    priors.enabled = True
    facts = json.loads(json.dumps(priors_facts or {}))
    priors.facts = facts.get("names", facts)
    priors.types = facts.get("types", {})
    results = {}
    for endpoint, report in sorted(reports.items()):
        if "required_parameters" not in report:
            continue
        truth = proxy_truth(report)
        result = score_one(truth, priors, SimulatedProber(truth), strategy)
        priors.record(result["report"])
        results[endpoint] = {
            k: result[k] for k in ("correct", "total", "phases", "mistakes")
        }
        results[endpoint]["lookups"] = result["requests"]
    return results


def check_simulator(truths, results):
    """How often the simulator agrees with what the live server said.

    Returns (exact, pass_fail, disagreements): requests where the predicted
    status matched exactly, and where it at least matched on 200 vs not --
    which is all the scoper's group tests look at. Mixed groups of non-200
    changes can come back 400 where the simulator guesses 500.
    """
    exact, pass_fail, disagreements = 0, 0, []
    for endpoint, modes in results.items():
        for result in modes.values():
            simulator = SimulatedProber(truths[endpoint])
            for _, parameters, status in result["log"]:
                try:
                    predicted = simulator.send(parameters)[0]
                except KeyError as e:
                    disagreements.append((endpoint, str(e)))
                    continue
                exact += predicted == status
                pass_fail += (predicted == 200) == (status == 200)
                if predicted != status:
                    disagreements.append((endpoint, parameters, status, predicted))
    return exact, pass_fail, disagreements


def summarize(results):
    lines, totals = [], {"cold": [0, 0, 0], "warm": [0, 0, 0]}
    for endpoint, modes in results.items():
        cells = []
        for mode, r in modes.items():
            cells.append(
                f"{mode} {r['correct']}/{r['total']} in {r['requests']} req"
                f" {r['seconds']}s"
            )
            for i, key in enumerate(("correct", "total", "requests")):
                totals[mode][i] += r[key]
            for mistake in r["mistakes"]:
                cells.append(f"\n      MISTAKE ({mode}) {mistake}")
            if r["interactions"]:
                cells.append(f"\n      interactions ({mode}): {r['interactions']}")
        lines.append(f"{endpoint:28s} " + "  |  ".join(cells))
    for mode, (correct, total, requests) in totals.items():
        lines.append(f"TOTAL {mode}: {correct}/{total} correct, {requests} requests")
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="python -m tools.stats.endpoint_scope.truth", description=__doc__
    )
    sub = parser.add_subparsers(dest="command", required=True)
    rec = sub.add_parser("record", help="exhaustive single-key probes (live)")
    rec.add_argument("targets", nargs="+", help="endpoint names or full URLs")
    rec.add_argument("--out", required=True, help="truth JSON (merged if present)")
    rec.add_argument("--pause", type=float, default=0.6)
    sco = sub.add_parser("score", help="grade the scoper against a truth file")
    sco.add_argument("truth")
    sco.add_argument("--simulate", action="store_true", help="no network")
    sco.add_argument("--priors", default=PRIORS_PATH, help="priors for warm runs")
    sco.add_argument("--pause", type=float, default=0.6)
    sco.add_argument("--out", help="write detailed results (with request logs)")
    sco.add_argument(
        "--legacy", action="store_true", help="score the first-run algorithm"
    )
    sco.add_argument(
        "--check-simulator",
        action="store_true",
        help="after a live score, replay its requests through the simulator",
    )
    args = parser.parse_args(argv)

    if args.command == "record":
        truths = {}
        if os.path.exists(args.out):
            with open(args.out) as f:
                truths = json.load(f)
        for endpoint, params, _, note in resolve_targets(
            args.targets, list_endpoint_classes()
        ):
            if not params:
                print(f"{endpoint}: skipped ({note})")
                continue
            prober = Prober(endpoint, pause=args.pause, proxy="", cache_ttl=0)
            truths[endpoint] = record_truth(endpoint, params, prober)
            unstable = flaky(truths[endpoint])
            print(
                f"{endpoint}: {len(params)} params, {prober.requests_sent} requests,"
                f" flaky: {unstable or 'none'}",
                flush=True,
            )
            with open(args.out, "w") as f:
                json.dump(truths, f, indent=1, sort_keys=True)
        return

    with open(args.truth) as f:
        truths = json.load(f)
    strategy = LEGACY_STRATEGY if args.legacy else STRATEGY
    results = score(truths, args.simulate, args.priors, args.pause, strategy)
    print(summarize(results))
    if args.check_simulator and not args.simulate:
        exact, pass_fail, disagreements = check_simulator(truths, results)
        total = sum(len(r["log"]) for modes in results.values() for r in modes.values())
        print(
            f"simulator matched {pass_fail}/{total} requests on pass/fail,"
            f" {exact}/{total} on exact status"
        )
        for d in disagreements[:20]:
            print(f"   {d}")
    if args.out:
        with open(args.out, "w") as f:
            json.dump(results, f, indent=1, default=str)


if __name__ == "__main__":
    main()
