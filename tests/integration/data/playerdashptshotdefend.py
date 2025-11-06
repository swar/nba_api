"""
Test data for PlayerDashPtShotDefend endpoint.

GitHub Issues:
- User reports: "team_id requirement needs to be taken off"
- User reports: "returns empty for certain seasons"

Expected response formats:
- String: "success" | "has_data" | "empty" | "error"
- Dict: {"status": "success", "min_rows": 1, "max_rows": 100}
"""

# Endpoint class name
ENDPOINT_CLASS = "PlayerDashPtShotDefend"

# Test cases
TEST_CASES = [
    {
        "description": "Basic test - LeBron 2023-24 Lakers",
        "params": {"player_id": "2544", "team_id": 1610612747, "season": "2023-24"},
        "expected": "success",  # Endpoint should work
    },
    {
        "description": "Team ID zero - all teams",
        "params": {"player_id": "2544", "team_id": 0, "season": "2023-24"},
        "expected": "has_data",  # Returns data for all teams
    },
    {
        "description": "Playoffs 2023-24",
        "params": {
            "player_id": "2544",
            "team_id": 1610612747,
            "season": "2023-24",
            "season_type_all_star": "Playoffs",
        },
        "expected": "success",
    },
]
