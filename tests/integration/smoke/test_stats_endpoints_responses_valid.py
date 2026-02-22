"""Integration smoke sweep for stats endpoints.

Broad live check: each endpoint spec call succeeds and returns valid JSON.
Not a detailed behavior or contract test.
"""

import json

import pytest

from ..catalogs.endpoint_specs import endpoint_specs
from ..catalogs.models import EndpointSpec

pytestmark = [pytest.mark.live]


# This method is passed to test_endpoints so console output will be generated with
# the class name rather than path::test_name[endpoint_spec12]`
def endpoint_id_func(param):
    if isinstance(param, EndpointSpec):
        return param.endpoint_class.__name__
    return None


def call_endpoint_and_assert_valid_json(endpoint_spec):
    endpoint_name = endpoint_spec.endpoint_class.__name__

    try:
        response = endpoint_spec()
    except json.decoder.JSONDecodeError:
        pytest.fail(msg=f"Unable to decode response for {endpoint_name}")

    assert response.nba_response.valid_json(), (
        f"Endpoint returned non-valid JSON: {endpoint_name}"
    )


def _to_pytest_param(spec):
    if spec.deprecated:
        return pytest.param(
            spec,
            marks=pytest.mark.deprecated_endpoint(spec.deprecated),
        )
    return spec


# Run this test on each endpoint in endpoint_specs.
@pytest.mark.parametrize(
    "endpoint_spec",
    [_to_pytest_param(spec) for spec in endpoint_specs],
    ids=endpoint_id_func,
)
def test_endpoints(endpoint_spec):
    """Smoke test each endpoint call and JSON validity with pacing."""
    call_endpoint_and_assert_valid_json(endpoint_spec)
