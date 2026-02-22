"""Integration scenario/issue-regression tests for selected stats endpoints.

Covers reported parameter combinations and regression scenarios.
Not the broad live smoke sweep.
"""

import pytest

from nba_api.stats import endpoints

from ..helpers import assert_endpoint_instantiates, run_endpoint_test

# Import test case data (one module per endpoint)
from .data import (
    leaguedashteamstats,
    leaguegamefinder,
    playerdashptshotdefend,
    scoreboardv3,
    teamdashlineups,
    teamgamelog,
    teamgamelogs,
)

pytestmark = [pytest.mark.live]

EXPECTED_OPTION_KEYS = ("min_rows", "max_rows", "exact_rows", "validate_structure")


def case_expected(test_case):
    """Convert standardized scenario case fields into runner expectation payload."""
    expected = {"status": test_case.get("expected_status", "success")}
    for key in EXPECTED_OPTION_KEYS:
        if key in test_case:
            expected[key] = test_case[key]
    return expected


def run_scenario_case(endpoint_class, test_case):
    """Run a single standardized scenario test case."""
    run_endpoint_test(endpoint_class, test_case["params"], case_expected(test_case))


# =============================================================================
# PlayerDashPtShotDefend Tests
# =============================================================================


@pytest.mark.parametrize(
    "test_case",
    playerdashptshotdefend.TEST_CASES,
    ids=[case["name"] for case in playerdashptshotdefend.TEST_CASES],
)
def test_playerdashptshotdefend(test_case):
    """Test PlayerDashPtShotDefend with various parameter combinations."""
    run_scenario_case(endpoints.PlayerDashPtShotDefend, test_case)


# =============================================================================
# ScoreboardV3 Tests
# =============================================================================


@pytest.mark.parametrize(
    "test_case",
    scoreboardv3.TEST_CASES,
    ids=[case["name"] for case in scoreboardv3.TEST_CASES],
)
def test_scoreboardv3(test_case):
    """Test ScoreboardV3 with various parameter combinations."""
    run_scenario_case(endpoints.ScoreboardV3, test_case)


# =============================================================================
# LeagueDashTeamStats Tests
# =============================================================================


@pytest.mark.parametrize(
    "test_case",
    leaguedashteamstats.TEST_CASES,
    ids=[case["name"] for case in leaguedashteamstats.TEST_CASES],
)
def test_leaguedashteamstats(test_case):
    """Test LeagueDashTeamStats with various parameter combinations."""
    run_scenario_case(endpoints.LeagueDashTeamStats, test_case)


# =============================================================================
# TeamDashLineups Tests
# =============================================================================


@pytest.mark.parametrize(
    "test_case",
    teamdashlineups.TEST_CASES,
    ids=[case["name"] for case in teamdashlineups.TEST_CASES],
)
def test_teamdashlineups(test_case):
    """Test TeamDashLineups with various parameter combinations."""
    run_scenario_case(endpoints.TeamDashLineups, test_case)


# =============================================================================
# LeagueGameFinder Tests
# =============================================================================


@pytest.mark.parametrize(
    "test_case",
    leaguegamefinder.TEST_CASES,
    ids=[case["name"] for case in leaguegamefinder.TEST_CASES],
)
def test_leaguegamefinder(test_case):
    """Test LeagueGameFinder with various parameter combinations."""
    run_scenario_case(endpoints.LeagueGameFinder, test_case)


# =============================================================================
# TeamGameLog Tests
# =============================================================================


@pytest.mark.parametrize(
    "test_case",
    teamgamelog.TEST_CASES,
    ids=[case["name"] for case in teamgamelog.TEST_CASES],
)
def test_teamgamelog(test_case):
    """Test TeamGameLog with various parameter combinations."""
    run_scenario_case(endpoints.TeamGameLog, test_case)


# =============================================================================
# TeamGameLogs Tests
# =============================================================================


@pytest.mark.parametrize(
    "test_case",
    teamgamelogs.TEST_CASES,
    ids=[case["name"] for case in teamgamelogs.TEST_CASES],
)
def test_teamgamelogs(test_case):
    """Test TeamGameLogs with various parameter combinations."""
    run_scenario_case(endpoints.TeamGameLogs, test_case)


# =============================================================================
# Template for Adding More Endpoints
# =============================================================================

# Step 1: Create data file tests/integration/scenarios/data/leaguegamelog.py:
#   TEST_CASES = [
#       {
#           "name": "basic",
#           "params": {"season": "2023-24"},
#           "expected_status": "has_data",
#       },
#       {
#           "name": "issue_123",
#           "params": {"season": "2020-21", "season_type": "Playoffs"},
#           "expected_status": "empty",
#       },
#   ]
#
# Step 2: Import the data module:
#   from .data import leaguegamelog
#
# Step 3: Create test function:
#   @pytest.mark.parametrize(
#       "test_case",
#       leaguegamelog.TEST_CASES,
#       ids=[case["name"] for case in leaguegamelog.TEST_CASES],
#   )
#   def test_leaguegamelog(test_case):
#       """Test LeagueGameLog with reported scenarios."""
#       run_scenario_case(endpoints.LeagueGameLog, test_case)


# =============================================================================
# Common Endpoints - Quick sanity check for critical endpoints
# =============================================================================

COMMON_TESTS = [
    (endpoints.LeagueDashPlayerStats, {}, "LeagueDashPlayerStats"),
    (endpoints.CommonAllPlayers, {}, "CommonAllPlayers"),
    (endpoints.PlayerCareerStats, {"player_id": "2544"}, "PlayerCareerStats"),
    (endpoints.BoxScoreSummaryV2, {"game_id": "0022300001"}, "BoxScoreSummaryV2"),
    (endpoints.BoxScoreAdvancedV3, {"game_id": "0022300001"}, "BoxScoreAdvancedV3"),
]


@pytest.mark.parametrize(
    "endpoint_class,params,description",
    COMMON_TESTS,
    ids=[case[2] for case in COMMON_TESTS],
)
def test_common(endpoint_class, params, description):  # noqa: ARG001
    """Verify endpoint doesn't crash."""
    assert_endpoint_instantiates(endpoint_class, params, description)
