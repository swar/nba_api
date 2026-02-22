"""pytest configuration and shared fixtures for integration tests.

Provides:
- rate_limit: autouse fixture that sleeps between live API calls to avoid throttling
- vcr_cassette_dir: configures cassette storage location for pytest-recording
"""

import time

import pytest


@pytest.fixture(autouse=True)
def rate_limit(request):
    """Sleep between requests for live tests to avoid NBA Stats API throttling.

    Skipped automatically for vcr-marked tests (cassette replay is instant).
    """
    if request.node.get_closest_marker("live") and not request.node.get_closest_marker(
        "vcr"
    ):
        time.sleep(0.6)


@pytest.fixture(scope="module")
def vcr_cassette_dir(request):
    """Store cassettes next to the test file, in a cassettes/ subdirectory."""
    return str(request.fspath.dirpath("cassettes"))
