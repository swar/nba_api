"""
Test data for ScoreboardV3 endpoint.

GitHub Issues:
- #580: Implement ScoreboardV3 endpoint

Expected response formats:
- String: "success" | "has_data" | "empty" | "error"
- Dict: {"status": "success", "min_rows": 1, "max_rows": 100}
"""

# Endpoint class name
ENDPOINT_CLASS = "ScoreboardV3"

# Test cases
TEST_CASES = [
    {
        "description": "Regular season game date - November 5, 2025",
        "params": {"game_date": "2025-11-05"},
        "expected": "has_data",  # Should have games
    },
    {
        "description": "Offseason date - no games expected",
        "params": {"game_date": "2025-07-15"},
        "expected": "success",  # API returns scoreboard info even with no games
    },
    {
        "description": "Custom league ID",
        "params": {"game_date": "2025-11-05", "league_id": "00"},
        "expected": "has_data",  # Should work with explicit league_id
    },
]
