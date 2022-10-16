import time
import json
import random
import pytest

from deferred_endpoints import deferred_endpoints

# Once we run the test to call the endpoints, we'll cache the responses here.
cached_eps = []


# Run this test on each endpoint in deferred_endpoints.
@pytest.mark.parametrize('deferred_endpoint', deferred_endpoints)
def test_endpoints_run(deferred_endpoint):
    '''Test that each endpoint is callable.

    This takes a very, very long time in total (10-20 minutes) because we don't
    want to barrage the NBA site with requests.'''
    # Delay briefly
    wait = random.gammavariate(alpha=9, beta=0.4)
    time.sleep(wait)
    # Call the API.
    try:
        response = deferred_endpoint()
    except json.decoder.JSONDecodeError:
        endpoint_class = deferred_endpoint.endpoint_class
        msg = 'Unable to decode response for {}'.format(endpoint_class)
        pytest.fail(msg=msg)
    # We want to hang onto all the responses so we don't need to re-retrieve
    # them later.
    cached_eps.append(response)


def test_valid_json():
    # Check that every called endpoint is valid json.
    valid = [ep.nba_response.valid_json() for ep in cached_eps]
    assert len(valid) == len(deferred_endpoints)
    assert all(valid)
