# Endpoint Test Data

This directory contains test cases for validating specific endpoint behaviors reported in GitHub issues.

## Purpose

**NOT for:** Testing parameter requirements (that's API discovery)
**YES for:** Validating specific scenarios like:
- "Season 2020-21 returns empty"
- "This param combo is broken"
- "Endpoint works with these exact values"

## Adding Test Cases from GitHub Issues

When you get a report like "LeagueGameLog returns empty for playoffs":

### 1. Create/edit test data file

**File:** `{endpoint_name}.py` (lowercase, matching endpoint name)

```python
"""
Test cases for EndpointName endpoint.

GitHub Issues:
- #123: User reports "returns empty for playoffs"
- #456: "Works in 2015 but not 2021"

Test case format: (params_dict, expected_result, test_id)
"""

TEST_CASES = [
    # Basic test
    (
        {"required_param": "value"},
        "has_data",
        "basic",
    ),
    # From issue #123
    (
        {"required_param": "value", "season_type": "Playoffs"},
        "empty",  # We expect no data for this combo
        "issue_123_playoffs",
    ),
    # From issue #456
    (
        {"required_param": "value", "season": "2015-16"},
        "has_data",
        "issue_456_season_2015-16",
    ),
]
```

**Expected results:**
- `"has_data"` - Endpoint returns data (normal success)
- `"empty"` - Endpoint succeeds but returns no data (document known behavior)
- `"error"` - Endpoint raises exception (known broken scenario)

### 2. Add test function

In `test_endpoints.py`:

```python
# Import the data
from .data import endpointname

# Add test function
@pytest.mark.parametrize(
    "params,expected,description",
    endpointname.TEST_CASES,
    ids=[case[2] for case in endpointname.TEST_CASES],
)
def test_endpointname(params, expected, description):  # noqa: ARG001
    """Test EndpointName with various parameters."""
    time.sleep(0.6)
    run_endpoint_test(endpoints.EndpointName, params, expected)
```

### 3. Run the tests

```bash
# Test your new endpoint
pytest tests/integration/test_endpoints.py -k endpointname -v

# Or run all tests
pytest tests/integration/test_endpoints.py -v
```

## Examples

See `playerdashptshotdefend.py` for a complete example.
