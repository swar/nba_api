"""Shared integration assertion helpers for scenario endpoint tests.

Reusable response/structure validation utilities for integration tests.
Not pytest fixture or hook configuration.
"""

import json
import logging
import re

logger = logging.getLogger(__name__)


def to_snake_case(name):
    """Convert PascalCase or camelCase to snake_case."""
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
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
    """Count rows per dataset and return total and per-dataset counts."""
    total_rows = 0
    dataset_row_counts = {}

    if hasattr(endpoint, "data_sets") and endpoint.data_sets:
        expected_dataset_names = (
            list(endpoint.expected_data.keys())
            if hasattr(endpoint, "expected_data")
            else []
        )

        for i, dataset in enumerate(endpoint.data_sets):
            df = dataset.get_data_frame()
            rows = len(df)
            total_rows += rows
            dataset_name = (
                expected_dataset_names[i]
                if i < len(expected_dataset_names)
                else f"Dataset{i}"
            )
            dataset_row_counts[dataset_name] = rows

    if dataset_row_counts:
        logger.info(f"Dataset row counts: {dataset_row_counts}")

    return total_rows, dataset_row_counts


def _validate_status(expected_status, total_rows, dataset_row_counts):
    """Validate based on expected status (has_data, empty, success)."""
    if expected_status == "has_data":
        if total_rows == 0:
            logger.error(f"Expected data but got {total_rows} rows")
            return False
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
    """Validate row counts against min/max/exact constraints."""
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
    """Validate endpoint response against expected outcome."""
    if isinstance(expected, str):
        expected_status = expected
        expected_dict = {"status": expected_status}
    else:
        expected_dict = expected
        expected_status = expected_dict.get("status", "success")

    validate_structure = expected_dict.get("validate_structure", False)

    if validate_structure and hasattr(endpoint, "expected_data"):
        validation_passed = validate_dataset_structure(endpoint)
        if not validation_passed:
            return 0, False

    total_rows, dataset_row_counts = _count_dataset_rows(endpoint)

    if not _validate_status(expected_status, total_rows, dataset_row_counts):
        return total_rows, False

    if not _validate_row_counts(expected_dict, total_rows):
        return total_rows, False

    return total_rows, True


def validate_dataset_structure(endpoint):
    """Validate that endpoint response matches expected_data structure."""
    if not hasattr(endpoint, "expected_data"):
        logger.warning("Endpoint has no expected_data, skipping structure validation")
        return True

    expected_datasets = endpoint.expected_data
    actual_datasets = {}

    if hasattr(endpoint, "data_sets") and endpoint.data_sets:
        for dataset_name, _expected_columns in expected_datasets.items():
            dataset_attr_name = to_snake_case(dataset_name)
            if hasattr(endpoint, dataset_attr_name):
                dataset = getattr(endpoint, dataset_attr_name)
                df = dataset.get_data_frame()
                actual_datasets[dataset_name] = list(df.columns)

    missing_datasets = set(expected_datasets.keys()) - set(actual_datasets.keys())
    if missing_datasets:
        logger.error(f"Missing expected datasets: {missing_datasets}")
        return False

    for dataset_name, expected_columns in expected_datasets.items():
        if dataset_name not in actual_datasets:
            continue

        actual_columns = actual_datasets[dataset_name]
        missing_columns = set(expected_columns) - set(actual_columns)
        if missing_columns:
            logger.error(f"Dataset '{dataset_name}' missing columns: {missing_columns}")
            return False

        extra_columns = set(actual_columns) - set(expected_columns)
        if extra_columns:
            logger.warning(
                f"Dataset '{dataset_name}' has extra columns: {extra_columns}"
            )

    logger.info("✓ Dataset structure validation passed")
    return True


def run_endpoint_test(endpoint_class, params, expected="success"):
    """Run a scenario endpoint test and raise AssertionError on failure."""
    endpoint_name = endpoint_class.__name__

    logger.info("Parameters:")
    for key, value in params.items():
        logger.info(f"  {key}: {value}")

    if isinstance(expected, str):
        expected_status = expected
    else:
        expected_status = expected.get("status", "success")

    logger.info(f"Expected: {expected_status}")
    logger.info("Calling endpoint...")

    try:
        endpoint = endpoint_class(**params)
    except Exception as exc:
        if expected_status == "error":
            logger.info(f"✓ Got expected error: {type(exc).__name__}")
            return
        logger.error(f"Unexpected error: {type(exc).__name__}: {exc}")
        raise AssertionError(
            f"{endpoint_name} failed unexpectedly: {type(exc).__name__}: {exc}"
        ) from exc

    if expected_status == "error":
        logger.error("Expected error but endpoint succeeded")
        raise AssertionError(
            f"{endpoint_name} expected endpoint to fail but it succeeded"
        )

    url = endpoint.get_request_url()
    logger.info(f"URL: {url}")

    try:
        response_json = endpoint.get_json()
        response_size = len(response_json)
        logger.info(f"Response size: {response_size:,} bytes")

        if logger.isEnabledFor(logging.DEBUG):
            response_dict = json.loads(response_json)
            logger.debug("JSON Response:")
            logger.debug(json.dumps(response_dict, indent=2))
    except Exception as exc:
        logger.error(f"Response error: {exc}")
        raise AssertionError(f"{endpoint_name} response error: {exc}") from exc

    total_rows, validation_passed = validate_response(endpoint, expected)
    logger.info(f"Data rows: {total_rows}")

    if not validation_passed:
        raise AssertionError(
            f"{endpoint_name} response validation failed for expected: {expected}"
        )

    logger.info("✓ SUCCESS")


def assert_endpoint_instantiates(endpoint_class, params, description):
    """Assert an endpoint class instantiates successfully with provided params."""
    try:
        endpoint = endpoint_class(**params)
        assert endpoint is not None
    except Exception as exc:
        raise AssertionError(
            f"{description} failed: {type(exc).__name__}: {exc}"
        ) from exc
