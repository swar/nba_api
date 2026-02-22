"""Integration smoke sweep for stats endpoints.

Broad live check: each deferred endpoint call succeeds and returns valid JSON.
Not a detailed behavior or contract test.
"""

import json

import pytest

from ..catalogs.deferred_endpoints import (
    DeferredEndpoint,
    deferred_endpoints,
)

pytestmark = [pytest.mark.live]


# This method is passed to test_endpoints so console output will be generated with
# the class name rather than path::test_name[deferred_endpoint12]`
def endpoint_id_func(param):
    if isinstance(param, DeferredEndpoint):
        return param.endpoint_class.__name__
    return None


def call_endpoint_and_assert_valid_json(deferred_endpoint):
    endpoint_name = deferred_endpoint.endpoint_class.__name__

    try:
        response = deferred_endpoint()
    except json.decoder.JSONDecodeError:
        pytest.fail(msg=f"Unable to decode response for {endpoint_name}")

    assert response.nba_response.valid_json(), (
        f"Endpoint returned non-valid JSON: {endpoint_name}"
    )


# Run this test on each endpoint in deferred_endpoints.
@pytest.mark.parametrize("deferred_endpoint", deferred_endpoints, ids=endpoint_id_func)
def test_endpoints(deferred_endpoint):
    """Smoke test each endpoint call and JSON validity with pacing."""
    call_endpoint_and_assert_valid_json(deferred_endpoint)
