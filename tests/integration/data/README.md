# Endpoint Test Data

Test data for validating endpoint behaviors reported in GitHub issues.

## Purpose

**NOT for:** Testing parameter requirements (that's API discovery)
**YES for:** Validating specific scenarios like:
- "Season 2020-21 returns empty"
- "This param combo is broken"
- "Endpoint works with these exact values"

## File Format

Each endpoint has a Python file: `{endpoint_name}.py` (lowercase)

### Required Constants

```python
"""
Test data for EndpointName endpoint.

GitHub Issues:
- #123: User reports "returns empty for playoffs"
"""

# Endpoint class name (PascalCase)
ENDPOINT_CLASS = "EndpointName"

# Test cases
TEST_CASES = [
    {
        "description": "Brief description of what this tests",
        "params": {"param1": "value1", "param2": "value2"},
        "expected": "success"  # or dict for detailed validation
    },
]
```

## Expected Response Formats

### Simple String Format

```python
"expected": "success"      # Endpoint succeeds (any row count)
"expected": "has_data"     # Must return rows > 0
"expected": "empty"        # Must return 0 rows
"expected": "error"        # Known to fail
```

### Detailed Dict Format

```python
"expected": {
    "status": "success",          # "success" | "has_data" | "empty" | "error"
    "min_rows": 1,                # Optional: minimum rows
    "max_rows": 100,              # Optional: maximum rows
    "exact_rows": 5,              # Optional: exact count
    "validate_structure": True,   # Optional: enable strict validation (default: False)
}
```

### Structure Validation (Enhanced Validation)

When `validate_structure: True` is set, the test performs comprehensive validation:

**✅ Validates:**
- Dataset names match `expected_data` keys
- All expected datasets are present
- Column names match `expected_data` field lists for each dataset
- Per-dataset row counts (logged separately)

**Benefits:**
- Catches API response changes early
- Detects `expected_data` definition errors
- Prevents false retirements (like TeamGameLog/TeamGameLogs)
- Provides detailed per-dataset diagnostics

**When to enable:**
- New endpoints (to establish baseline)
- Recently restored endpoints
- Endpoints with frequent API changes
- When debugging unexpected behavior

**Default behavior (False):**
- Validates total row counts only
- Compatible with existing tests
- Less strict, won't break on extra columns

**Example with strict validation:**
```python
{
    "description": "Lakers 2023-24 season",
    "params": {"team_id": "1610612747", "season": "2023-24"},
    "expected": {
        "status": "has_data",
        "validate_structure": True  # Enable strict validation
    }
}
```

## Complete Example

**File:** `tests/integration/data/playerdashptshotdefend.py`

```python
"""
Test data for PlayerDashPtShotDefend endpoint.

GitHub Issues:
- User reports: "team_id requirement needs to be taken off"
"""

ENDPOINT_CLASS = "PlayerDashPtShotDefend"

TEST_CASES = [
    {
        "description": "Basic test - LeBron 2023-24 Lakers",
        "params": {
            "player_id": "2544",
            "team_id": 1610612747,
            "season": "2023-24"
        },
        "expected": "success",
    },
    {
        "description": "Team ID zero - all teams",
        "params": {
            "player_id": "2544",
            "team_id": 0,
            "season": "2023-24"
        },
        "expected": "has_data",  # Verified: returns 6 rows
    },
    {
        "description": "Known broken - old season times out",
        "params": {
            "player_id": "2544",
            "team_id": 1610612747,
            "season": "2015-16"
        },
        "expected": "error",  # NBA API issue
    },
]
```

## Adding Tests for GitHub Issues

### 1. Create test data file

```bash
# Create file for the endpoint
touch tests/integration/data/leaguegamelog.py
```

### 2. Add test cases

```python
"""Test data for LeagueGameLog endpoint."""

ENDPOINT_CLASS = "LeagueGameLog"

TEST_CASES = [
    {
        "description": "Issue #456 - playoffs returns empty",
        "params": {
            "season": "2023-24",
            "season_type_all_star": "Playoffs"
        },
        "expected": "empty",  # Document known behavior
    },
]
```

### 3. Add test function

In `tests/integration/test_endpoints.py`:

```python
from .data import leaguegamelog

@pytest.mark.parametrize(
    "test_case",
    leaguegamelog.TEST_CASES,
    ids=[case["description"] for case in leaguegamelog.TEST_CASES],
)
def test_leaguegamelog(test_case):
    """Test LeagueGameLog with various parameters."""
    time.sleep(0.6)
    run_endpoint_test(
        endpoints.LeagueGameLog,
        test_case["params"],
        test_case.get("expected", "success")
    )
```

### 4. Run tests

```bash
# Test with detailed logging
pytest tests/integration/test_endpoints.py -k leaguegamelog --log-cli-level=INFO

# See actual JSON response
pytest tests/integration/test_endpoints.py -k leaguegamelog --log-cli-level=DEBUG
```

**Logging output shows:**
- Parameters being tested
- Expected outcome
- Full URL called
- Response size
- Number of data rows
- JSON response (with DEBUG level)

## Tips

- Link GitHub issue numbers in file docstrings
- Use descriptive test descriptions (becomes test name in pytest output)
- Document WHY a test expects empty/error (NBA API bug? Seasonal data?)
- Test the actual scenario users report, not general parameter validation
