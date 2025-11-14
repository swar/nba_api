"""
Test data for TeamGameLog endpoint.

GitHub Issues:
- Endpoint was retired in v1.11.0 but is now working again (restored in v1.11.3)

Expected response formats:
- String: "success" | "has_data" | "empty" | "error"
- Dict: {"status": "success", "min_rows": 1, "max_rows": 100}
"""

# Endpoint class name
ENDPOINT_CLASS = "TeamGameLog"

# Test cases
TEST_CASES = [
    {
        "description": "Lakers 2023-24 regular season",
        "params": {
            "team_id": "1610612747",
            "season": "2023-24",
            "season_type_all_star": "Regular Season",
        },
        "expected": {
            "status": "has_data",
            "validate_structure": True,  # Enable strict validation
        },
    },
    {
        "description": "Lakers 2023-24 playoffs",
        "params": {
            "team_id": "1610612747",
            "season": "2023-24",
            "season_type_all_star": "Playoffs",
        },
        "expected": "has_data",  # Lakers made playoffs in 2023-24
    },
    {
        "description": "Celtics 2023-24 regular season",
        "params": {
            "team_id": "1610612738",
            "season": "2023-24",
            "season_type_all_star": "Regular Season",
        },
        "expected": "has_data",
    },
    {
        "description": "Date range filter",
        "params": {
            "team_id": "1610612747",
            "season": "2023-24",
            "date_from_nullable": "01/01/2024",
            "date_to_nullable": "01/31/2024",
        },
        "expected": "has_data",  # Should return games in January 2024
    },
]
