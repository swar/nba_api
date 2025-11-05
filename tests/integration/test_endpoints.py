"""
Integration tests for endpoint validation.

These tests validate specific endpoint behaviors reported in GitHub issues:
- "Season 2020-21 returns empty"
- "Endpoint broken with these params"
- "Does endpoint work at all?"

This is NOT for testing parameter requirements (use API docs).
This IS for validating exact scenarios users report.

Usage:
    # Test specific endpoint
    pytest tests/integration/test_endpoints.py -k playerdashptshotdefend -v

    # Test all endpoints
    pytest tests/integration/test_endpoints.py -v

    # Quick smoke tests
    pytest tests/integration/test_endpoints.py -k smoke -v

Adding test cases from issues:
    1. Create/edit: tests/integration/data/{endpoint}.py
    2. Add TEST_CASES with exact params: (params, expected, test_id)
    3. Import and add test function (see template below)
"""

import time

import pytest

from nba_api.stats import endpoints

# Import test case data (one module per endpoint)
from .data import playerdashptshotdefend


# =============================================================================
# Helper Functions
# =============================================================================


def has_data(endpoint):
    """Check if endpoint returned any data."""
    for dataset in endpoint.data_sets:
        df = dataset.get_data_frame()
        if not df.empty:
            return True
    return False


def run_endpoint_test(endpoint_class, params, expected):
    """
    Common test logic for all endpoint tests.

    Args:
        endpoint_class: The endpoint class to test
        params: Dict of parameters to pass (the exact scenario to test)
        expected: Expected result - "has_data", "empty", "error"

    Raises:
        AssertionError: If actual result doesn't match expected
    """
    # Attempt to call endpoint with exact params
    try:
        endpoint = endpoint_class(**params)
    except Exception as e:
        if expected == "error":
            return  # Expected to fail
        pytest.fail(f"Endpoint failed unexpectedly: {type(e).__name__}: {e}")

    # Check if result matches expectation
    if expected == "has_data":
        assert has_data(endpoint), "Expected data but response is empty"
    elif expected == "empty":
        assert not has_data(endpoint), "Expected empty but response has data"


# =============================================================================
# PlayerDashPtShotDefend Tests
# =============================================================================


@pytest.mark.parametrize(
    "params,expected,description",
    playerdashptshotdefend.TEST_CASES,
    ids=[case[2] for case in playerdashptshotdefend.TEST_CASES],
)
def test_playerdashptshotdefend(params, expected, description):  # noqa: ARG001
    """Test PlayerDashPtShotDefend with various parameter combinations."""
    time.sleep(0.6)  # Rate limiting
    run_endpoint_test(endpoints.PlayerDashPtShotDefend, params, expected)


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
# Smoke Tests - Quick sanity check for critical endpoints
# =============================================================================

SMOKE_TESTS = [
    (endpoints.LeagueDashPlayerStats, {}, "LeagueDashPlayerStats"),
    (endpoints.CommonAllPlayers, {}, "CommonAllPlayers"),
    (endpoints.PlayerCareerStats, {"player_id": "2544"}, "PlayerCareerStats"),
    (endpoints.BoxScoreSummaryV2, {"game_id": "0022300001"}, "BoxScoreSummaryV2"),
    (endpoints.BoxScoreAdvancedV3, {"game_id": "0022300001"}, "BoxScoreAdvancedV3"),
]


@pytest.mark.parametrize(
    "endpoint_class,params,description",
    SMOKE_TESTS,
    ids=[case[2] for case in SMOKE_TESTS],
)
def test_smoke(endpoint_class, params, description):  # noqa: ARG001
    """Smoke test to verify endpoint doesn't crash."""
    time.sleep(0.6)

    try:
        endpoint = endpoint_class(**params)
        assert endpoint is not None
    except Exception as e:
        pytest.fail(f"{description} failed: {type(e).__name__}: {e}")
