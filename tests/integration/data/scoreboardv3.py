"""Integration scenario cases for ScoreboardV3.

Issue/regression-style params and coarse expectations for scenario tests.
Prefer stable presence/range assertions over brittle exact values.
"""

ENDPOINT_CLASS = "ScoreboardV3"

TEST_CASES = [
    {
        "name": "Regular season game date - November 5, 2025",
        "params": {"game_date": "2025-11-05"},
        "expected_status": "has_data",
    },
    {
        "name": "Offseason date - no games expected",
        "params": {"game_date": "2025-07-15"},
        "expected_status": "success",
    },
    {
        "name": "Custom league ID",
        "params": {"game_date": "2025-11-05", "league_id": "00"},
        "expected_status": "has_data",
    },
]
