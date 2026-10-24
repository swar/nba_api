"""Snapshot of the datasets every offline-testable stats endpoint produces.

Each endpoint class exported from ``nba_api.stats.endpoints`` has one entry in
``endpoint_datasets.json``. Each endpoint is parsed from exactly one offline
source, picked in this order:

1. its smoke cassette ``tests/integration/smoke/cassettes/test_endpoints[<Class>]``,
   replayed through its ``EndpointSpec`` (when the spec exists and is not
   skipped),
2. otherwise the source listed for it in ``EXTRA_SOURCES``, either

   - a scenario cassette from ``tests/integration/scenarios/cassettes``,
     replayed with that scenario case's ``params`` from
     ``tests/integration/scenarios/data``, or
   - a unit fixture payload from ``tests/unit/stats/endpoints/data``, loaded
     into the endpoint (built with ``get_request=False``) through an
     ``NBAStatsResponse``.

Entries from the second group carry a ``source`` field naming the cassette or
fixture used; smoke cassette entries have none. The parsed output is pinned:

- ``data_sets``: the ``get_data_frames()`` order, each entry naming the
  ``DataSet`` attributes holding equal data (columns and row count are spelled
  out only when no attribute matches),
- ``attributes``: every ``DataSet`` attribute (or dataset attribute left
  ``None``, such as the class-level ``player_stats = None`` placeholders many
  endpoints declare) with its column headers, row count and emptiness,
- ``expected_data_unmatched``: ``expected_data`` keys whose column list matches
  no parsed dataset (omitted when everything matches),
- ``error``: the exception type, for cassettes that no longer parse.

Every other endpoint is listed with a ``gap`` reason (no spec, spec skipped,
or no cassette), so changes to the set of uncovered endpoints also fail here.
``EXTRA_SOURCES`` only reuses cassettes and fixtures other tests already rely
on; it never adds response data of its own.

Record mode is forced to ``none``: a missing or unmatched cassette fails
instead of recording, so this never touches the network.

To regenerate after an intentional change, run::

    NBA_API_UPDATE_SNAPSHOTS=1 NBA_API_PROXY= uv run pytest \\
        tests/integration/snapshots -m vcr

Partial runs (``-k``) only rewrite the endpoints that ran; entries for classes
no longer exported are dropped.
"""

import difflib
import importlib
import inspect
import json
import os
from dataclasses import dataclass, field
from pathlib import Path

import pytest
from vcr.errors import CannotOverwriteExistingCassetteException

import nba_api.stats.endpoints as ep
from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsResponse

from ..helpers.endpoint_specs import endpoint_specs
from ..helpers.seasons import pinned_season_kwargs

pytestmark = [pytest.mark.vcr]

SNAPSHOT_PATH = Path(__file__).with_name("endpoint_datasets.json")
CASSETTE_DIR = Path(__file__).parent.parent / "smoke" / "cassettes"
SCENARIO_CASSETTE_DIR = Path(__file__).parent.parent / "scenarios" / "cassettes"
UPDATE = os.environ.get("NBA_API_UPDATE_SNAPSHOTS") == "1"

# Class-level attributes that are None but are not datasets.
NON_DATASET_ATTRS = {"nba_response", "data_sets", "headers", "proxy"}

ENDPOINT_CLASSES = {
    name: cls
    for name, cls in inspect.getmembers(ep, inspect.isclass)
    if issubclass(cls, Endpoint) and cls is not Endpoint
}
SPECS = {spec.endpoint_class.__name__: spec for spec in endpoint_specs}


def cassette_name(name):
    return f"test_endpoints[{name}]"


def gap_reason(name):
    spec = SPECS.get(name)
    if spec is None:
        return "no EndpointSpec"
    if spec.skip:
        return f"spec skipped: {spec.skip}"
    if not (CASSETTE_DIR / f"{cassette_name(name)}.yaml").exists():
        return "no cassette"
    return None


@dataclass(frozen=True)
class ScenarioSource:
    """A scenario cassette, replayed with its case's params."""

    module: str  # tests/integration/scenarios/data/<module>.py
    case: str  # the TEST_CASES entry "name"

    @property
    def cassette(self):
        return f"test_{self.module}[{self.case}]"

    @property
    def description(self):
        return f"scenario cassette {self.cassette}"

    def build(self, endpoint_class):
        data = importlib.import_module(
            f"tests.integration.scenarios.data.{self.module}"
        )
        (params,) = [c["params"] for c in data.TEST_CASES if c["name"] == self.case]
        params = {**pinned_season_kwargs(endpoint_class, params), **params}
        return endpoint_class(**params)


@dataclass(frozen=True)
class FixtureSource:
    """A unit test fixture payload, loaded without a request."""

    module: str  # tests/unit/stats/endpoints/data/<module>.py
    attr: str  # the payload constant in that module
    # Required constructor args, taken from the fixture's own request.
    kwargs: dict = field(default_factory=dict)

    @property
    def description(self):
        return (
            f"unit fixture tests/unit/stats/endpoints/data/{self.module}.py {self.attr}"
        )

    def build(self, endpoint_class):
        data = importlib.import_module(f"tests.unit.stats.endpoints.data.{self.module}")
        payload = getattr(data, self.attr)
        kwargs = {**pinned_season_kwargs(endpoint_class, self.kwargs), **self.kwargs}
        instance = endpoint_class(**kwargs, get_request=False)
        instance.nba_response = NBAStatsResponse(
            json.dumps(payload), 200, "http://fixture.invalid"
        )
        instance.load_response()
        return instance


# Offline sources for endpoints without a usable smoke cassette, one per
# endpoint so each entry is deterministic.
EXTRA_SOURCES = {
    "BoxScoreSummaryV3": FixtureSource(
        "boxscoresummaryv3", "BOXSCORESUMMARYV3_SAMPLE", {"game_id": "0022500142"}
    ),
    "DunkScoreLeaders": FixtureSource("dunkscoreleaders", "DUNKSCORELEADERS_SAMPLE"),
    "GravityLeaders": FixtureSource("gravityleaders", "GRAVITYLEADERS_SAMPLE"),
    "ScheduleLeagueV2": FixtureSource("scheduleleaguev2", "SCHEDULELEAGUEV2_2020_21"),
    # ScheduleLeagueV2Int has no source: the ScheduleLeagueV2 fixture has no
    # leagueSchedule.broadcasterList, so the Int parse raises KeyError on it.
    "ScoreboardV3": ScenarioSource(
        "scoreboardv3", "Regular season game date - November 5, 2025"
    ),
    "TeamGameLog": ScenarioSource("teamgamelog", "Lakers 2023-24 regular season"),
    "TeamGameLogs": ScenarioSource("teamgamelogs", "Lakers 2023-24 regular season"),
}


def source_for(name):
    """Return ``(extra_source, gap_reason)``; both None means the smoke cassette."""
    reason = gap_reason(name)
    if reason is None:
        return None, None
    extra = EXTRA_SOURCES.get(name)
    if extra is None:
        return None, reason
    return extra, None


def describe(data_set):
    data = data_set.data
    rows = len(data.get("data") or [])
    return {
        "columns": data.get("headers"),
        "empty": rows == 0,
        "none": False,
        "rows": rows,
    }


def dataset_attributes(instance):
    names = set(vars(instance))
    for cls in type(instance).__mro__:
        if cls is Endpoint:
            break
        names.update(vars(cls))
    attrs = {}
    for name in sorted(names - NON_DATASET_ATTRS):
        if name.startswith("_"):
            continue
        value = getattr(instance, name)
        if isinstance(value, Endpoint.DataSet):
            attrs[name] = value
        elif value is None:
            attrs[name] = None
    return attrs


def snapshot_instance(instance):
    attrs = dataset_attributes(instance)
    data_sets = []
    for data_set in instance.data_sets or []:
        matches = [
            name
            for name, attr in attrs.items()
            if attr is not None and attr.data == data_set.data
        ]
        data_sets.append({"matches": matches} if matches else describe(data_set))
    entry = {
        "attributes": {
            name: describe(attr)
            if attr is not None
            else {"columns": None, "empty": True, "none": True, "rows": 0}
            for name, attr in attrs.items()
        },
        "data_sets": data_sets,
    }
    # Round-trip through JSON so tuple and list headers compare equal.
    parsed_columns = json.loads(
        json.dumps([ds.data.get("headers") for ds in instance.data_sets or []])
    )
    expected_data = json.loads(json.dumps(getattr(instance, "expected_data", {})))
    unmatched = sorted(
        key for key, columns in expected_data.items() if columns not in parsed_columns
    )
    if unmatched:
        entry["expected_data_unmatched"] = unmatched
    return entry


def build_entry(name):
    extra, reason = source_for(name)
    if reason:
        return {"gap": reason}
    try:
        instance = extra.build(ENDPOINT_CLASSES[name]) if extra else SPECS[name]()
    except CannotOverwriteExistingCassetteException:
        raise  # request no longer matches the cassette: fail, never record
    except Exception as exc:  # noqa: BLE001 - pin how broken cassettes fail
        entry = {"error": type(exc).__name__}
    else:
        entry = snapshot_instance(instance)
    if extra:
        entry["source"] = extra.description
    return entry


def dump(data):
    return json.dumps(data, indent=2, sort_keys=True) + "\n"


def changed_paths(expected, actual, path=""):
    """Yield dotted paths where two snapshot entries differ."""
    if isinstance(expected, dict) and isinstance(actual, dict):
        for key in sorted(set(expected) | set(actual)):
            yield from changed_paths(
                expected.get(key), actual.get(key), f"{path}.{key}" if path else key
            )
    elif isinstance(expected, list) and isinstance(actual, list):
        if len(expected) != len(actual):
            yield f"{path} (length {len(expected)} -> {len(actual)})"
        else:
            for i, (old, new) in enumerate(zip(expected, actual, strict=True)):
                yield from changed_paths(old, new, f"{path}[{i}]")
    elif expected != actual:
        yield path or "<entry>"


@pytest.fixture(scope="module")
def snapshot():
    stored = json.loads(SNAPSHOT_PATH.read_text()) if SNAPSHOT_PATH.exists() else {}
    updates = {}
    yield stored, updates
    if UPDATE and updates:
        merged = {**stored, **updates}
        merged = {k: v for k, v in merged.items() if k in ENDPOINT_CLASSES}
        SNAPSHOT_PATH.write_text(dump(merged))


@pytest.fixture
def vcr_config():
    return {"record_mode": "none"}


def scenario_source(request):
    """Return the ScenarioSource behind this test's endpoint, if it has one."""
    callspec = getattr(request.node, "callspec", None)
    if callspec is None:
        return None
    extra, _ = source_for(callspec.params["name"])
    return extra if isinstance(extra, ScenarioSource) else None


@pytest.fixture
def vcr_cassette_dir(request):
    if scenario_source(request):
        return str(SCENARIO_CASSETTE_DIR)
    return str(CASSETTE_DIR)


@pytest.fixture
def default_cassette_name(request):
    callspec = getattr(request.node, "callspec", None)
    if callspec is None:
        return request.node.name
    scenario = scenario_source(request)
    if scenario:
        return scenario.cassette
    return cassette_name(callspec.params["name"])


@pytest.mark.parametrize("name", sorted(ENDPOINT_CLASSES))
def test_endpoint_datasets_match_snapshot(name, snapshot):
    stored, updates = snapshot
    actual = json.loads(json.dumps(build_entry(name)))
    if UPDATE:
        updates[name] = actual
        return
    expected = stored.get(name)
    if actual != expected:
        paths = "\n".join(f"  {p}" for p in changed_paths(expected, actual))
        diff = "\n".join(
            difflib.unified_diff(
                dump(expected).splitlines(),
                dump(actual).splitlines(),
                "snapshot",
                "actual",
                lineterm="",
            )
        )
        pytest.fail(
            f"{name} datasets differ from {SNAPSHOT_PATH.name} at:\n{paths}\n\n"
            f"{diff}\n\n"
            "If this change is intentional, regenerate with:\n"
            "NBA_API_UPDATE_SNAPSHOTS=1 NBA_API_PROXY= uv run pytest "
            f"tests/integration/snapshots -m vcr -k {name}",
            pytrace=False,
        )


def test_snapshot_lists_exactly_the_exported_endpoints():
    if UPDATE:
        pytest.skip("snapshot is being regenerated")
    stored = json.loads(SNAPSHOT_PATH.read_text())
    stale = sorted(set(stored) - set(ENDPOINT_CLASSES))
    assert not stale, (
        f"{SNAPSHOT_PATH.name} lists endpoints that are no longer exported: {stale}. "
        "Regenerate it with NBA_API_UPDATE_SNAPSHOTS=1 (see module docstring)."
    )
