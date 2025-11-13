"""
Endpoint validation tests.

These tests validate specific endpoint behaviors reported in GitHub issues:
- "Season 2020-21 returns empty"
- "Endpoint broken with these params"
- "Does endpoint work at all?"

This is NOT for testing parameter requirements (use API docs).
This IS for validating exact scenarios users report.

Usage:
    # Test specific endpoint with detailed logging
    pytest tests/integration/test_endpoints.py -k playerdashptshotdefend -v --log-cli-level=INFO

    # Show JSON response
    pytest tests/integration/test_endpoints.py -k playerdashptshotdefend -v --log-cli-level=DEBUG

    # Test all endpoints
    pytest tests/integration/test_endpoints.py -v --log-cli-level=INFO

Adding test cases from issues:
    1. Create/edit: tests/integration/data/{endpoint}.py with ENDPOINT_CLASS and TEST_CASES
    2. Import and add test function (see template below)
"""

import json
import logging
import time

import pytest

from nba_api.stats import endpoints

# Import test case data (one module per endpoint)
from .data import leaguedashteamstats, playerdashptshotdefend, scoreboardv3, teamdashlineups

logger = logging.getLogger(__name__)


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


def validate_response(endpoint, expected):
    """
    Validate endpoint response against expected outcome.

    Args:
        endpoint: The endpoint instance
        expected: Expected outcome - string or dict
            String: "success" | "has_data" | "empty" | "error"
            Dict: {"status": "success", "min_rows": 1, "max_rows": 100}

    Returns:
        tuple: (total_rows, validation_passed)
    """
    # Count total rows
    total_rows = 0
    if hasattr(endpoint, "data_sets") and endpoint.data_sets:
        for dataset in endpoint.data_sets:
            df = dataset.get_data_frame()
            total_rows += len(df)

    # Parse expected format
    if isinstance(expected, str):
        expected_status = expected
        expected_dict = {"status": expected_status}
    else:
        expected_dict = expected
        expected_status = expected_dict.get("status", "success")

    # Validate based on status
    if expected_status == "has_data":
        if total_rows == 0:
            logger.error(f"Expected data but got {total_rows} rows")
            return total_rows, False
    elif expected_status == "empty":
        if total_rows != 0:
            logger.error(f"Expected empty but got {total_rows} rows")
            return total_rows, False
    elif expected_status == "success":
        # Just needs to not error
        pass

    # Validate row counts if specified
    if "min_rows" in expected_dict:
        if total_rows < expected_dict["min_rows"]:
            logger.error(
                f"Expected min {expected_dict['min_rows']} rows, got {total_rows}"
            )
            return total_rows, False

    if "max_rows" in expected_dict:
        if total_rows > expected_dict["max_rows"]:
            logger.error(
                f"Expected max {expected_dict['max_rows']} rows, got {total_rows}"
            )
            return total_rows, False

    if "exact_rows" in expected_dict:
        if total_rows != expected_dict["exact_rows"]:
            logger.error(
                f"Expected exactly {expected_dict['exact_rows']} rows, got {total_rows}"
            )
            return total_rows, False

    return total_rows, True


def run_endpoint_test(endpoint_class, params, expected="success"):
    """
    Common test logic for all endpoint tests.

    Args:
        endpoint_class: The endpoint class to test
        params: Dict of parameters to pass (the exact scenario to test)
        expected: Expected outcome (string or dict)

    Raises:
        AssertionError: If test fails
    """
    logger.info("Parameters:")
    for key, value in params.items():
        logger.info(f"  {key}: {value}")

    # Parse expected format
    if isinstance(expected, str):
        expected_status = expected
    else:
        expected_status = expected.get("status", "success")

    logger.info(f"Expected: {expected_status}")

    # Call endpoint
    logger.info("Calling endpoint...")
    try:
        endpoint = endpoint_class(**params)
    except Exception as e:
        # Check if error was expected
        if expected_status == "error":
            logger.info(f"✓ Got expected error: {type(e).__name__}")
            return  # Test passed - error was expected
        else:
            logger.error(f"Unexpected error: {type(e).__name__}: {e}")
            pytest.fail(f"Endpoint failed unexpectedly: {type(e).__name__}: {e}")

    # If we expected an error but didn't get one
    if expected_status == "error":
        logger.error("Expected error but endpoint succeeded")
        pytest.fail("Expected endpoint to fail but it succeeded")

    # Log URL
    url = endpoint.get_request_url()
    logger.info(f"URL: {url}")

    # Log response details
    try:
        response_json = endpoint.get_json()
        response_size = len(response_json)
        logger.info(f"Response size: {response_size:,} bytes")

        # Show JSON at DEBUG level
        if logger.isEnabledFor(logging.DEBUG):
            response_dict = json.loads(response_json)
            logger.debug("JSON Response:")
            logger.debug(json.dumps(response_dict, indent=2))
    except Exception as e:
        logger.error(f"Response error: {e}")
        pytest.fail(f"Response error: {e}")

    # Validate response
    total_rows, validation_passed = validate_response(endpoint, expected)
    logger.info(f"Data rows: {total_rows}")

    if not validation_passed:
        pytest.fail(f"Response validation failed for expected: {expected}")

    logger.info("✓ SUCCESS")


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
        test_case.get("expected", "success")
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
        test_case.get("expected", "success")
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
        test_case.get("expected", "success")
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
        test_case.get("expected", "success")
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

    try:
        endpoint = endpoint_class(**params)
        assert endpoint is not None
    except Exception as e:
        pytest.fail(f"{description} failed: {type(e).__name__}: {e}")
