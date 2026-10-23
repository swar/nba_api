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

    def send(parameters, use_cache=True):
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

    def flaky_send(parameters, use_cache=True):
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


def test_truth_classifies_each_parameter_from_single_key_probes(prober):
    from tools.stats.endpoint_scope import truth

    recorded = truth.record_truth("fake", dict(BASELINE), prober)
    expected = truth.classify(recorded)

    assert [p for p, d in expected.items() if d["required"]] == ["A"]
    assert [p for p, d in expected.items() if d["non_null"]] == ["B"]
    assert [p for p, d in expected.items() if d["validated"]] == ["C", "D", "E"]
    assert [p for p, d in expected.items() if d["type_checked"]] == ["F"]
    # Numeric params get a -1 probe; E and F were empty so are never blanked.
    assert "negative" in recorded["probes"]["D"]
    assert "blank" not in recorded["probes"]["E"]
    assert truth.flaky(recorded) == []


def test_truth_scores_the_scoper_and_simulator_matches_fake_server(prober):
    from tools.stats.endpoint_scope import truth

    recorded = truth.record_truth("fake", dict(BASELINE), prober)
    prober.log = []
    real_send = prober.send

    def logging_send(parameters, use_cache=True):
        status, response = real_send(parameters)
        prober.log.append(("x", parameters, status))
        return status, response

    prober.send = logging_send
    prober.requests_sent = 0
    live = truth.score_one(recorded, scope.Priors(enabled=False), prober)
    assert (live["correct"], live["mistakes"]) == (live["total"], [])

    simulated = truth.score_one(
        recorded, scope.Priors(enabled=False), truth.SimulatedProber(recorded)
    )
    assert simulated["correct"] == simulated["total"]
    assert simulated["requests"] == live["requests"]
    exact, pass_fail, disagreements = truth.check_simulator(
        {"fake": recorded}, {"fake": {"cold": live}}
    )
    assert disagreements == [] and exact == pass_fail == len(live["log"])


def test_check_simulator_flags_group_interactions():
    from tools.stats.endpoint_scope import truth

    ok = {"status": 200, "named": False}
    recorded = {
        "params": {"PlayerID": "1", "TeamID": "2"},
        "probes": {"PlayerID": {"drop": ok}, "TeamID": {"drop": ok}},
    }
    # The server needs PlayerID *or* TeamID: each drop passes alone, both fail.
    log = [("drop", {}, 500)]
    exact, pass_fail, disagreements = truth.check_simulator(
        {"x": recorded}, {"x": {"cold": {"log": log}}}
    )
    assert exact == pass_fail == 0 and disagreements == [("x", {}, 500, 200)]


def _run_cli(monkeypatch, tmp_path, outcomes, argv):
    """Run the CLI with scope_endpoint answering from ``outcomes`` per endpoint."""
    from tools.stats.endpoint_scope import __main__ as cli

    calls, sleeps = [], []

    def fake_scope(endpoint, *args, **kwargs):
        calls.append(endpoint)
        status = outcomes[endpoint].pop(0) if outcomes[endpoint] else "success"
        return {"endpoint": endpoint, "status": status, "error": "HTTP 503"}

    monkeypatch.setattr(cli, "scope_endpoint", fake_scope)
    monkeypatch.setattr(cli, "format_report", lambda r: r["endpoint"])
    monkeypatch.setattr(
        cli,
        "resolve_targets",
        lambda names, classes: [(n, {"P": "1"}, None, None) for n in names],
    )
    out = tmp_path / "out.json"
    try:
        cli.main([*argv, "--json", str(out), "--no-priors"], sleep=sleeps.append)
        code = 0
    except SystemExit as e:
        code = e.code
    return calls, sleeps, json.loads(out.read_text()) if out.exists() else {}, code


def test_cli_backs_off_then_moves_past_one_failing_endpoint(monkeypatch, tmp_path):
    outcomes = {"a": ["network-error"] * 3, "b": [], "c": ["network-error"]}
    calls, sleeps, results, code = _run_cli(
        monkeypatch, tmp_path, outcomes, ["a", "b", "c"]
    )
    assert code == 0
    assert calls == ["a", "a", "a", "b", "c", "c"]
    assert sleeps == [60, 180, 60]
    assert {k: v["status"] for k, v in results.items()} == {
        "a": "network-error",
        "b": "success",
        "c": "success",
    }


def test_cli_stops_when_endpoints_keep_failing(monkeypatch, tmp_path):
    outcomes = {n: ["network-error"] * 3 for n in "abc"}
    calls, _, results, code = _run_cli(monkeypatch, tmp_path, outcomes, ["a", "b", "c"])
    assert code == 1
    assert "c" not in calls
    assert list(results) == ["a"]


def test_cli_resume_skips_finished_endpoints(monkeypatch, tmp_path):
    (tmp_path / "out.json").write_text(
        json.dumps({"a": {"status": "drift"}, "b": {"status": "network-error"}})
    )
    calls, _, results, _ = _run_cli(
        monkeypatch, tmp_path, {"a": [], "b": []}, ["a", "b", "--resume"]
    )
    assert calls == ["b"]
    assert results["a"] == {"status": "drift"} and results["b"]["status"] == "success"


def test_previous_report_cuts_requests_without_changing_results(prober, monkeypatch):
    monkeypatch.setattr(scope, "Prober", lambda *a, **k: prober)
    first = scope.scope_endpoint("fake", dict(BASELINE))
    cold_cost = prober.requests_sent

    prober.requests_sent = 0
    priors = scope.Priors(enabled=False)  # in memory: nothing learned yet
    priors.enabled = True
    again = scope.scope_endpoint("fake", dict(BASELINE), priors=priors, previous=first)

    keys = ("required_parameters", "nullable_parameters", "type_checked_parameters")
    assert {k: again[k] for k in keys} == {k: first[k] for k in keys}
    assert set(again["validated_parameters"]) == set(first["validated_parameters"])
    assert prober.requests_sent < cold_cost


def test_overridden_by_prefers_the_endpoints_own_history():
    priors = scope.Priors(enabled=False)
    priors.enabled = True
    priors.facts = {"A": {"seen": 5, "required": 0}, "Z": {"seen": 1, "required": 1}}
    report = {
        "parameters": ["A"],
        "required_parameters": ["A"],
        "nullable_parameters": [],
        "type_checked_parameters": {},
    }
    own = priors.overridden_by(report)
    assert own.likely("required", {"A": "1", "Z": "1"}) == {"A", "Z"}
    assert priors.likely("required", {"A": "1"}) == set()  # original untouched
    assert priors.overridden_by(None) is priors
    assert scope.Priors(enabled=False).overridden_by(report).facts == {}  # --no-priors


def test_rate_threshold_ignores_rare_failures():
    priors = scope.Priors(enabled=False)
    priors.facts = {
        "LeagueID": {"seen": 100, "non_nullable": 10},
        "PerMode": {"seen": 10, "non_nullable": 10},
        "Legacy": {"non_nullable": 2},  # older files have no "seen"
    }
    params = dict.fromkeys(priors.facts, "x")
    assert priors.likely("non_nullable", params, 0.2) == {"PerMode", "Legacy"}
    assert priors.likely("non_nullable", params) == set(priors.facts)


@pytest.mark.parametrize("strategy", ["STRATEGY", "LEGACY_STRATEGY"])
def test_both_strategies_classify_the_fake_server_correctly(prober, strategy):
    report = {}
    scope.probe_parameters(
        report, dict(BASELINE), prober, strategy=getattr(scope, strategy)
    )
    assert report["required_parameters"] == ["A"]
    assert sorted(set(BASELINE) - set(report["nullable_parameters"])) == ["B"]
    assert set(report["validated_parameters"]) == {"C", "D", "E"}
    assert report["type_checked_parameters"] == {"F": 500}


def test_required_but_nullable_param_is_still_found_blank_first():
    # Like CommonTeamRoster TeamID: dropping it fails, "" is fine. Blank-first
    # tests only non-null params alone, so this one must come out of a group.
    baseline = {"TeamID": "1610612739", "Season": "2025-26", "LeagueID": "00"}

    class Server(CountingProber):
        def send(self, parameters):
            self.requests_sent += 1
            status = 200 if "TeamID" in parameters else 500
            return status, NBAStatsResponse("{}", status, None)

        def ok(self, parameters):
            return self.send(parameters)[0] == 200

    report = {}
    scope.probe_parameters(report, baseline, Server([]))
    assert report["required_parameters"] == ["TeamID"]
    assert report["nullable_parameters"] == sorted(baseline)


def test_transient_500_on_a_drop_is_rechecked_not_reported():
    # CommonTeamRoster in the first full run: one 500 on dropping TeamID, while
    # TeamID="" was fine. Asked again, uncached, the drop passes.
    baseline = {"TeamID": "1610612739", "Season": "2025-26", "LeagueID": "00"}

    class Server(CountingProber):
        transient = True

        def send(self, parameters, use_cache=True):
            self.requests_sent += 1
            status = 200
            if "TeamID" not in parameters and len(parameters) == 2 and use_cache:
                status = 500 if self.transient else 200
            return status, NBAStatsResponse("{}", status, None)

        def ok(self, parameters):
            return self.send(parameters)[0] == 200

        def recheck(self, parameters):
            return self.send(parameters, use_cache=False)[0] == 200

    report = {}
    scope.probe_parameters(report, baseline, Server([]))
    assert report["required_parameters"] == []


def test_surprising_failures_are_rechecked_but_real_ones_kept(prober):
    priors = scope.Priors(enabled=False)
    priors.facts = {"A": {"seen": 5, "required": 0}, "B": {"seen": 5}}
    rechecked = []
    prober.recheck = lambda parameters: (
        rechecked.append(parameters) or prober.ok(parameters)
    )
    report = {}
    scope.probe_parameters(report, dict(BASELINE), prober, priors)
    # A really is required and B really rejects "": both survive the recheck.
    assert report["required_parameters"] == ["A"]
    assert sorted(set(BASELINE) - set(report["nullable_parameters"])) == ["B"]
    assert len(rechecked) == 2  # A: required but nullable (and surprising); B


def test_values_that_leave_the_data_unchanged_are_flagged(prober, monkeypatch):
    real_send = prober.send

    def send(parameters, use_cache=True):
        status, response = real_send(parameters)
        if status == 200:
            # Totals changes the data; every other accepted value is ignored.
            row = [1] if parameters.get("B") == "Totals" else [0]
            body = json.dumps({"resultSets": [{"rowSet": [row]}]})
            response = NBAStatsResponse(body, 200, None)
        return status, response

    monkeypatch.setattr(prober, "send", send)
    monkeypatch.setattr(
        scope, "library_parameter_classes", lambda cls: {"B": "PerModeSimple"}
    )
    report = {"validated_parameters": {"B": ["Invalid"]}, "flags": []}
    results = scope.discover_values(
        report, {**BASELINE, "B": "PerGame"}, None, prober, set()
    )
    verdict = results["B"]
    assert "Totals" in verdict["accepted"] and "Totals" not in verdict["no_effect"]
    assert "PerGame" not in verdict["no_effect"]  # the baseline value itself
    assert set(verdict["no_effect"]) == set(verdict["accepted"]) - {"Totals", "PerGame"}


def test_value_effects_are_not_judged_against_an_empty_baseline(prober, monkeypatch):
    monkeypatch.setattr(
        scope, "library_parameter_classes", lambda cls: {"B": "PerModeSimple"}
    )
    report = {"validated_parameters": {"B": ["Invalid"]}, "flags": []}
    results = scope.discover_values(report, dict(BASELINE), None, prober, set())
    assert results["B"]["no_effect"] is None  # the fake server returns no rows
    assert report["flags"] == ["baseline has no rows: value effects not checked"]
