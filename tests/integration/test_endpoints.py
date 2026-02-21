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
from .data import (
    leaguedashteamstats,
    leaguegamefinder,
    playerdashptshotdefend,
    scoreboardv3,
    teamdashlineups,
    teamgamelog,
    teamgamelogs,
)

logger = logging.getLogger(__name__)


# =============================================================================
# Helper Functions
# =============================================================================


def to_snake_case(name):
    """
    Convert PascalCase or camelCase to snake_case.

    Args:
        name: String in PascalCase or camelCase

    Returns:
        String in snake_case

    Examples:
        TeamGameLog -> team_game_log
        LineScore -> line_score
        PlayerStats -> player_stats
    """
    import re

    # Insert underscore before uppercase letters (except at start)
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    # Insert underscore before uppercase letters followed by lowercase
    s2 = re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1)
    return s2.lower()


def has_data(endpoint):
    """Check if endpoint returned any data."""
    for dataset in endpoint.data_sets:
        df = dataset.get_data_frame()
        if not df.empty:
            return True
    return False


def _count_dataset_rows(endpoint):
    """
    Count rows per dataset and return total and per-dataset counts.

    Args:
        endpoint: The endpoint instance

    Returns:
        tuple: (total_rows, dataset_row_counts dict)
    """
    total_rows = 0
    dataset_row_counts = {}

    if hasattr(endpoint, "data_sets") and endpoint.data_sets:
        # Try to get dataset names from expected_data
        expected_dataset_names = (
            list(endpoint.expected_data.keys())
            if hasattr(endpoint, "expected_data")
            else []
        )

        for i, dataset in enumerate(endpoint.data_sets):
            df = dataset.get_data_frame()
            rows = len(df)
            total_rows += rows

            # Try to get dataset name
            dataset_name = (
                expected_dataset_names[i]
                if i < len(expected_dataset_names)
                else f"Dataset{i}"
            )
            dataset_row_counts[dataset_name] = rows

    # Log per-dataset row counts
    if dataset_row_counts:
        logger.info(f"Dataset row counts: {dataset_row_counts}")

    return total_rows, dataset_row_counts


def _validate_status(expected_status, total_rows, dataset_row_counts):
    """
    Validate based on expected status (has_data, empty, success).

    Args:
        expected_status: Expected status string
        total_rows: Total row count across all datasets
        dataset_row_counts: Dict of per-dataset row counts

    Returns:
        bool: True if validation passed, False otherwise
    """
    if expected_status == "has_data":
        if total_rows == 0:
            logger.error(f"Expected data but got {total_rows} rows")
            return False

        # Enhanced validation: check that at least one dataset has data
        # (Some endpoints may have legitimately empty datasets)
        if all(count == 0 for count in dataset_row_counts.values()):
            logger.error("All datasets are empty")
            return False

    elif expected_status == "empty":
        if total_rows != 0:
            logger.error(f"Expected empty but got {total_rows} rows")
            return False

    # "success" status just needs to not error
    return True


def _validate_row_counts(expected_dict, total_rows):
    """
    Validate row counts against min/max/exact constraints.

    Args:
        expected_dict: Dict with optional min_rows, max_rows, exact_rows
        total_rows: Total row count to validate

    Returns:
        bool: True if validation passed, False otherwise
    """
    if "min_rows" in expected_dict and total_rows < expected_dict["min_rows"]:
        logger.error(f"Expected min {expected_dict['min_rows']} rows, got {total_rows}")
        return False

    if "max_rows" in expected_dict and total_rows > expected_dict["max_rows"]:
        logger.error(f"Expected max {expected_dict['max_rows']} rows, got {total_rows}")
        return False

    if "exact_rows" in expected_dict and total_rows != expected_dict["exact_rows"]:
        logger.error(
            f"Expected exactly {expected_dict['exact_rows']} rows, got {total_rows}"
        )
        return False

    return True


def validate_response(endpoint, expected):
    """
    Validate endpoint response against expected outcome.

    Performs comprehensive validation including:
    - Dataset name verification against expected_data
    - Per-dataset row count validation
    - Column structure validation
    - Total row count validation

    Args:
        endpoint: The endpoint instance
        expected: Expected outcome - string or dict
            String: "success" | "has_data" | "empty" | "error"
            Dict: {
                "status": "success",
                "min_rows": 1,
                "max_rows": 100,
                "validate_structure": True  # Check datasets & columns
            }

    Returns:
        tuple: (total_rows, validation_passed)
    """
    # Parse expected format
    if isinstance(expected, str):
        expected_status = expected
        expected_dict = {"status": expected_status}
    else:
        expected_dict = expected
        expected_status = expected_dict.get("status", "success")

    # Get validation options (default False to avoid breaking existing tests)
    # Set to True in test cases that want strict validation
    validate_structure = expected_dict.get("validate_structure", False)

    # Validate dataset structure if enabled and expected_data exists
    if validate_structure and hasattr(endpoint, "expected_data"):
        validation_passed = validate_dataset_structure(endpoint)
        if not validation_passed:
            return 0, False

    # Count total rows and per-dataset rows
    total_rows, dataset_row_counts = _count_dataset_rows(endpoint)

    # Validate based on status
    if not _validate_status(expected_status, total_rows, dataset_row_counts):
        return total_rows, False

    # Validate row counts if specified
    if not _validate_row_counts(expected_dict, total_rows):
        return total_rows, False

    return total_rows, True


def validate_dataset_structure(endpoint):
    """
    Validate that endpoint response matches expected_data structure.

    Checks:
    - Dataset names match expected_data keys
    - Columns match expected_data field lists
    - All expected datasets are present

    Args:
        endpoint: The endpoint instance with expected_data attribute

    Returns:
        bool: True if structure is valid, False otherwise
    """
    if not hasattr(endpoint, "expected_data"):
        logger.warning("Endpoint has no expected_data, skipping structure validation")
        return True

    expected_datasets = endpoint.expected_data
    actual_datasets = {}

    # Gather actual dataset names and columns
    if hasattr(endpoint, "data_sets") and endpoint.data_sets:
        for dataset_name, _expected_columns in expected_datasets.items():
            # Try to get the dataset by name (as an attribute)
            # Convert PascalCase/camelCase to snake_case
            dataset_attr_name = to_snake_case(dataset_name)
            if hasattr(endpoint, dataset_attr_name):
                dataset = getattr(endpoint, dataset_attr_name)
                df = dataset.get_data_frame()
                actual_datasets[dataset_name] = list(df.columns)

    # Validate dataset presence
    missing_datasets = set(expected_datasets.keys()) - set(actual_datasets.keys())
    if missing_datasets:
        logger.error(f"Missing expected datasets: {missing_datasets}")
        return False

    # Validate column structure for each dataset
    for dataset_name, expected_columns in expected_datasets.items():
        if dataset_name not in actual_datasets:
            continue  # Already logged as missing

        actual_columns = actual_datasets[dataset_name]

        # Check for missing columns
        missing_columns = set(expected_columns) - set(actual_columns)
        if missing_columns:
            logger.error(f"Dataset '{dataset_name}' missing columns: {missing_columns}")
            return False

        # Check for extra columns (warning only, not a failure)
        extra_columns = set(actual_columns) - set(expected_columns)
        if extra_columns:
            logger.warning(
                f"Dataset '{dataset_name}' has extra columns: {extra_columns}"
            )

    logger.info("✓ Dataset structure validation passed")
    return True


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

    try:
        endpoint = endpoint_class(**params)
        assert endpoint is not None
    except Exception as e:
        pytest.fail(f"{description} failed: {type(e).__name__}: {e}")
