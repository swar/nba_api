import json
import time

import pytest

from tests.integration.deferred_endpoints import DeferredEndpoint, deferred_endpoints

# Once we run the test to call the endpoints, we'll cache the responses here.
cached_eps = []


# This method is passed to test_endpoints so console output will be generated with
# the class name rather than path::test_name[deferred_endpoint12]`
def endpoint_id_func(param):
    if isinstance(param, DeferredEndpoint):
        return param.endpoint_class.__name__
    return None


# Run this test on each endpoint in deferred_endpoints.
@pytest.mark.parametrize("deferred_endpoint", deferred_endpoints, ids=endpoint_id_func)
def test_endpoints(deferred_endpoint):
    """Test that each endpoint is callable.

    This takes a very, very long time in total (10-20 minutes) because we don't
    want to barrage the NBA site with requests."""
    # Delay briefly
    time.sleep(0.600)
    # Call the API.
    try:
        response = deferred_endpoint()
    except json.decoder.JSONDecodeError:
        endpoint_class = deferred_endpoint.endpoint_class
        msg = f"Unable to decode response for {endpoint_class}"
        pytest.fail(msg=msg)
    # We want to hang onto all the responses so we don't need to re-retrieve
    # them later.
    cached_eps.append(response)


def test_valid_json():
    # Check that every called endpoint is valid json.
    valid = [ep.nba_response.valid_json() for ep in cached_eps]
    assert len(valid) == len(deferred_endpoints)
    assert all(valid)
