"""Scenario/issue-regression integration tests for selected stats endpoints.

These tests cover specific parameter combinations reported by users or captured
as regressions. This module is not the broad smoke sweep; it focuses on
scenario-level expectations.
"""

import time

import pytest

from nba_api.stats import endpoints

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
from .helpers import assert_endpoint_instantiates, run_endpoint_test

# =============================================================================
# PlayerDashPtShotDefend Tests
# =============================================================================


@pytest.mark.parametrize(
    "test_case",
    playerdashptshotdefend.TEST_CASES,
    ids=[case["description"] for case in playerdashptshotdefend.TEST_CASES],
)
def test_playerdashptshotdefend(test_case):
    """Test PlayerDashPtShotDefend with various parameter combinations."""
    time.sleep(0.6)  # Rate limiting
    run_endpoint_test(
        endpoints.PlayerDashPtShotDefend,
        test_case["params"],
        test_case.get("expected", "success"),
    )


# =============================================================================
# ScoreboardV3 Tests
# =============================================================================


@pytest.mark.parametrize(
    "test_case",
    scoreboardv3.TEST_CASES,
    ids=[case["description"] for case in scoreboardv3.TEST_CASES],
)
def test_scoreboardv3(test_case):
    """Test ScoreboardV3 with various parameter combinations."""
    time.sleep(0.6)  # Rate limiting
    run_endpoint_test(
        endpoints.ScoreboardV3,
        test_case["params"],
        test_case.get("expected", "success"),
    )


# =============================================================================
# LeagueDashTeamStats Tests
# =============================================================================


@pytest.mark.parametrize(
    "test_case",
    leaguedashteamstats.TEST_CASES,
    ids=[case["description"] for case in leaguedashteamstats.TEST_CASES],
)
def test_leaguedashteamstats(test_case):
    """Test LeagueDashTeamStats with various parameter combinations."""
    time.sleep(0.6)  # Rate limiting
    run_endpoint_test(
        endpoints.LeagueDashTeamStats,
        test_case["params"],
        test_case.get("expected", "success"),
    )


# =============================================================================
# TeamDashLineups Tests
# =============================================================================


@pytest.mark.parametrize(
    "test_case",
    teamdashlineups.TEST_CASES,
    ids=[case["description"] for case in teamdashlineups.TEST_CASES],
)
def test_teamdashlineups(test_case):
    """Test TeamDashLineups with various parameter combinations."""
    time.sleep(0.6)  # Rate limiting
    run_endpoint_test(
        endpoints.TeamDashLineups,
        test_case["params"],
        test_case.get("expected", "success"),
    )


# =============================================================================
# LeagueGameFinder Tests
# =============================================================================


@pytest.mark.parametrize(
    "test_case",
    leaguegamefinder.TEST_CASES,
    ids=[case["description"] for case in leaguegamefinder.TEST_CASES],
)
def test_leaguegamefinder(test_case):
    """Test LeagueGameFinder with various parameter combinations."""
    time.sleep(0.6)  # Rate limiting
    run_endpoint_test(
        endpoints.LeagueGameFinder,
        test_case["params"],
        test_case.get("expected", "success"),
    )


# =============================================================================
# TeamGameLog Tests
# =============================================================================


@pytest.mark.parametrize(
    "test_case",
    teamgamelog.TEST_CASES,
    ids=[case["description"] for case in teamgamelog.TEST_CASES],
)
def test_teamgamelog(test_case):
    """Test TeamGameLog with various parameter combinations."""
    time.sleep(0.6)  # Rate limiting
    run_endpoint_test(
        endpoints.TeamGameLog, test_case["params"], test_case.get("expected", "success")
    )


# =============================================================================
# TeamGameLogs Tests
# =============================================================================


@pytest.mark.parametrize(
    "test_case",
    teamgamelogs.TEST_CASES,
    ids=[case["description"] for case in teamgamelogs.TEST_CASES],
)
def test_teamgamelogs(test_case):
    """Test TeamGameLogs with various parameter combinations."""
    time.sleep(0.6)  # Rate limiting
    run_endpoint_test(
        endpoints.TeamGameLogs,
        test_case["params"],
        test_case.get("expected", "success"),
    )


# =============================================================================
# Template for Adding More Endpoints
# =============================================================================

# Step 1: Create data file tests/integration/data/leaguegamelog.py:
#   TEST_CASES = [
#       ({"season": "2023-24"}, "has_data", "basic"),
#       ({"season": "2020-21", "season_type": "Playoffs"}, "empty", "issue_123"),
#   ]
#
# Step 2: Import the data module:
#   from .data import leaguegamelog
#
# Step 3: Create test function:
#   @pytest.mark.parametrize(
#       "params,expected,description",
#       leaguegamelog.TEST_CASES,
#       ids=[case[2] for case in leaguegamelog.TEST_CASES],
#   )
#   def test_leaguegamelog(params, expected, description):  # noqa: ARG001
#       """Test LeagueGameLog with reported scenarios."""
#       time.sleep(0.6)
#       run_endpoint_test(endpoints.LeagueGameLog, params, expected)


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
    time.sleep(0.6)
    assert_endpoint_instantiates(endpoint_class, params, description)
