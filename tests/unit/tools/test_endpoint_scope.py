"""Unit tests for tools.stats.endpoint_scope, against a fake stats.nba.com."""

import json

import pytest

from nba_api.stats.library.http import NBAStatsResponse
from tools.stats.endpoint_scope import knowledge, scope

BASELINE = {"A": "1", "B": "Base", "C": "00", "D": "5", "E": "", "F": ""}


def fake_server(params):
    """A: required. B: rejects "". C, E: validated (400). D: integer, 500 on
    strings but a named 400 when out of range. F: date-like, 500 on garbage."""
    if "A" not in params:
        return 500, ""
    if params.get("B") == "":
        return 500, ""
    if params.get("F") == scope.GARBAGE:
        return 500, ""
    if params.get("D") and not params["D"].lstrip("-").isdigit():
        return 500, ""
    errors = {}
    if params.get("D") == "-1":
        errors["D"] = ["Invalid parameters"]
    if params.get("C", "") not in ("00", ""):
        errors["C"] = ["Invalid parameters"]
    if params.get("E") == scope.GARBAGE:
        errors["e.Value"] = ["Parameter must be valid"]
    if errors:
        return 400, json.dumps(errors)
    body = {
        "resource": "fake",
        "parameters": {**params, "NewParam": None},
        "resultSets": [{"name": "Rows", "headers": ["X", "Y"], "rowSet": []}],
    }
    return 200, json.dumps(body)


@pytest.fixture
def prober(monkeypatch):
    prober = scope.Prober("fake", pause=0, cache_ttl=0)

    def send(parameters):
        prober.requests_sent += 1
        status, body = fake_server(parameters)
        return status, NBAStatsResponse(body, status, None)

    monkeypatch.setattr(prober, "send", send)
    return prober


def test_bisect_failures_finds_only_breaking_keys(prober):
    keys = sorted(BASELINE)
    assert scope.bisect_failures(BASELINE, keys, scope.drop, prober) == ["A"]
    assert scope.bisect_failures(BASELINE, ["C", "D", "E"], scope.drop, prober) == []


def test_probe_parameters_classifies_each_parameter(prober):
    report = {}
    scope.probe_parameters(report, dict(BASELINE), prober)

    assert report["required_parameters"] == ["A"]
    assert sorted(set(BASELINE) - set(report["nullable_parameters"])) == ["B"]
    assert set(report["validated_parameters"]) == {"C", "D", "E"}
    assert report["type_checked_parameters"] == {"F": 500}
    assert report["numeric_parameters"] == ["A", "C", "D"]
    assert report["parameter_patterns"] == dict.fromkeys(sorted(BASELINE))


def test_scope_endpoint_reports_echo_and_drift(prober, monkeypatch):
    monkeypatch.setattr(scope, "Prober", lambda *a, **k: prober)

    class FakeEndpoint:
        __name__ = "FakeEndpoint"
        expected_data = {"Rows": ["X", "Z"]}

    report = scope.scope_endpoint("fake", dict(BASELINE), FakeEndpoint)

    assert report["status"] == "drift"
    assert report["drift"] == {"Rows": {"added": ["Y"], "removed": ["Z"]}}
    assert report["server_only_parameters"] == ["NewParam"]


def test_baseline_failure_stops_early(prober, monkeypatch):
    monkeypatch.setattr(scope, "Prober", lambda *a, **k: prober)
    report = scope.scope_endpoint("fake", {"B": "x"})
    assert report["status"] == "baseline-failed"
    assert prober.requests_sent == 1


def test_dataset_drift_spots_renamed_dataset_and_flattens_headers():
    multi_level = [
        {"name": "SHOT_CATEGORY", "columnNames": ["Mid-Range", "Corner 3"]},
        {"name": "columns", "columnNames": ["PLAYER_ID"]},
    ]
    drift = scope.dataset_drift(
        {"dunks": ["a", "b"], "Shots": multi_level[:1]},
        {"DunkScoreLeaders": ["a", "b"], "Shots": multi_level},
    )
    assert drift["dunks"] == "expected_data key; response calls it DunkScoreLeaders"
    assert drift["Shots"] == {"added": ["columns:PLAYER_ID"], "removed": []}


def test_shape_diff_and_unparsed_fields():
    recorded = {"meta": {"time": 1}, "game": {"players": [{"personId": 1}]}}
    live = {
        "meta": {"time": 1},
        "game": {"players": [{"personId": 1, "speed": 2}], "homeTeamId": 3},
    }
    assert knowledge.shape_diff(recorded, live) == {
        "added": ["game.homeTeamId", "game.players[].speed"],
        "removed": [],
    }
    unparsed = knowledge.unparsed_fields(live, {"P": ["personIdOff", "speed"]})
    assert unparsed == {"homeTeamId": "game.homeTeamId"}


def test_parameter_family_and_value_verdict():
    family = knowledge.parameter_family("PerMode", "PerModeSimple")
    assert {"PerModeSimple", "PerMode36", "PerModeDetailed"} <= set(family)

    verdict = knowledge.summarize_values(
        "PerMode",
        family,
        "PerModeSimple",
        accepted={"Totals", "PerGame", "Per36"},
        rejected={"Per48"},
    )
    assert verdict["best_fit_classes"] == ["PerMode36"]
    assert verdict["accepted_but_missing_from_library"] == ["Per36"]
    assert verdict["library_offers_rejected"] == []


def test_library_parameter_classes_reads_endpoint_source():
    from nba_api.stats.endpoints import LeagueDashPlayerStats

    mapping = knowledge.library_parameter_classes(LeagueDashPlayerStats)
    assert mapping["PerMode"] == "PerModeDetailed"
    assert mapping["SeasonType"] == "SeasonTypeAllStar"


def test_resolve_targets_parses_urls():
    url = "https://stats.nba.com/stats/NewThing?LeagueID=00&Season="
    [(endpoint, params, cls, note)] = scope.resolve_targets([url], {})
    assert (endpoint, params, cls) == (
        "newthing",
        {"LeagueID": "00", "Season": ""},
        None,
    )


def test_redact_hides_proxy_credentials():
    text = "Cannot connect to socks5://user:secret@10.0.0.1:1080 now"
    assert "secret" not in scope.redact(text)


class CountingProber:
    """Fails whenever any key in ``failing`` is mutated away from the baseline."""

    def __init__(self, failing):
        self.failing = set(failing)
        self.requests_sent = 0

    def ok(self, parameters):
        self.requests_sent += 1
        return all(parameters.get(k) == BIG_BASELINE.get(k) for k in self.failing)


BIG_BASELINE = {f"P{i:02d}": str(i) for i in range(32)}


def test_bisect_skips_right_half_when_left_passes():
    keys = sorted(BIG_BASELINE)
    prober = CountingProber(["P31"])
    assert scope.bisect_failures(BIG_BASELINE, keys, scope.drop, prober) == ["P31"]
    # Whole group + one test per level on the left (the right is inferred),
    # + one request confirming P31 on its own.
    assert prober.requests_sent == 7


def test_find_failures_uses_suspects_to_avoid_bisecting():
    keys = sorted(BIG_BASELINE)
    failing = ["P03", "P11", "P19", "P27"]
    cold = CountingProber(failing)
    warm = CountingProber(failing)
    assert scope.find_failures(BIG_BASELINE, keys, scope.drop, cold) == failing
    assert (
        scope.find_failures(BIG_BASELINE, keys, scope.drop, warm, set(failing))
        == failing
    )
    assert warm.requests_sent == len(failing) + 1 < cold.requests_sent


def test_priors_round_trip(tmp_path):
    priors = scope.Priors(path=str(tmp_path / "priors.json"))
    priors.record(
        {
            "parameters": ["A", "B", "C"],
            "required_parameters": ["A"],
            "nullable_parameters": ["C"],
            "type_checked_parameters": {"B": 500},
        }
    )
    priors.save()
    reloaded = scope.Priors(path=str(tmp_path / "priors.json"))
    assert reloaded.suspects("required") == {"A"}
    assert reloaded.suspects("non_nullable") == {"A", "B"}
    assert reloaded.suspects("crash") == {"B"}
    assert scope.Priors(path=str(tmp_path / "priors.json"), enabled=False).facts == {}


def test_network_error_aborts_instead_of_marking_required(prober, monkeypatch):
    real_send = prober.send
    calls = []

    def flaky_send(parameters):
        calls.append(parameters)
        if len(calls) == 3:
            raise scope.NetworkError("ReadTimeout")
        return real_send(parameters)

    monkeypatch.setattr(prober, "send", flaky_send)
    monkeypatch.setattr(scope, "Prober", lambda *a, **k: prober)
    report = scope.scope_endpoint("fake", dict(BASELINE))
    assert report["status"] == "network-error"
    assert "required_parameters" not in report


class EitherOrProber(CountingProber):
    """Fails only when every key in ``together`` is mutated (e.g. PlayerID or TeamID)."""

    def __init__(self, together, failing=()):
        super().__init__(failing)
        self.together = set(together)

    def ok(self, parameters):
        if not super().ok(parameters):
            return False
        return any(parameters.get(k) == BIG_BASELINE[k] for k in self.together)


@pytest.mark.parametrize("together", [["P00", "P31"], ["P15", "P16"], ["P30", "P31"]])
def test_keys_failing_only_together_are_reported_not_blamed(together):
    keys = sorted(BIG_BASELINE)
    interactions = []
    prober = EitherOrProber(together)
    failures = scope.bisect_failures(
        BIG_BASELINE, keys, scope.drop, prober, interactions
    )
    assert failures == []
    assert interactions and all(set(together) <= set(g) for g in interactions)


@pytest.mark.parametrize("together", [["P00", "P31"], ["P15", "P16"], ["P30", "P31"]])
def test_interaction_masked_by_real_failure_is_never_blamed(together):
    # A genuine failure in the same group explains the group's failure, so the
    # pair can go unnoticed -- but neither half of it may be reported.
    prober = EitherOrProber(together, failing=["P07"])
    failures = scope.bisect_failures(
        BIG_BASELINE, sorted(BIG_BASELINE), scope.drop, prober
    )
    assert failures == ["P07"]


def test_every_reported_failure_was_tested_alone():
    keys = sorted(BIG_BASELINE)
    tested = []

    class Recording(CountingProber):
        def ok(self, parameters):
            changed = [k for k in keys if parameters.get(k) != BIG_BASELINE[k]]
            if len(changed) == 1:
                tested.append(changed[0])
            return super().ok(parameters)

    failing = ["P01", "P02", "P20", "P31"]
    assert (
        scope.bisect_failures(BIG_BASELINE, keys, scope.drop, Recording(failing))
        == failing
    )
    assert set(failing) <= set(tested)
