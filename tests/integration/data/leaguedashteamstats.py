"""Test data for LeagueDashTeamStats endpoint."""

# Endpoint class name (PascalCase)
ENDPOINT_CLASS = "LeagueDashTeamStats"

# Test cases
TEST_CASES = [
    {
        "description": "Atlanta Hawks 2023-24 regular season (IST bug regression test - should return GP=82)",
        "params": {
            "season": "2023-24",
            "team_id_nullable": "1610612737",
            "season_type_all_star": "Regular Season",
        },
        "expected": {
            "status": "success",
            "min_rows": 1,
        },
    },
    {
        "description": "All teams 2024-25 regular season base stats",
        "params": {
            "season": "2024-25",
            "season_type_all_star": "Regular Season",
            "measure_type_detailed_defense": "Base",
            "per_mode_detailed": "PerGame",
        },
        "expected": {"status": "success", "min_rows": 30},
    },
    {
        "description": "Lakers 2023-24 playoffs",
        "params": {
            "season": "2023-24",
            "team_id_nullable": "1610612747",
            "season_type_all_star": "Playoffs",
        },
        "expected": "success",
    },
    {
        "description": "Warriors 2023-24 advanced stats",
        "params": {
            "season": "2023-24",
            "team_id_nullable": "1610612744",
            "season_type_all_star": "Regular Season",
            "measure_type_detailed_defense": "Advanced",
            "per_mode_detailed": "PerGame",
        },
        "expected": "has_data",
    },
    {
        "description": "Eastern Conference 2023-24",
        "params": {
            "season": "2023-24",
            "season_type_all_star": "Regular Season",
            "conference_nullable": "East",
        },
        "expected": {"status": "success", "min_rows": 15},
    },
]
