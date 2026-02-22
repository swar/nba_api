"""Integration scenario cases for TeamGameLog.

Issue/regression-style params and coarse expectations for scenario tests.
Prefer stable presence/range assertions over brittle exact values.
"""

TEST_CASES = [
    {
        "name": "Lakers 2023-24 regular season",
        "params": {
            "team_id": "1610612747",
            "season": "2023-24",
            "season_type_all_star": "Regular Season",
        },
        "expected_status": "has_data",
        "validate_structure": True,
    },
    {
        "name": "Lakers 2023-24 playoffs",
        "params": {
            "team_id": "1610612747",
            "season": "2023-24",
            "season_type_all_star": "Playoffs",
        },
        "expected_status": "has_data",
    },
    {
        "name": "Celtics 2023-24 regular season",
        "params": {
            "team_id": "1610612738",
            "season": "2023-24",
            "season_type_all_star": "Regular Season",
        },
        "expected_status": "has_data",
    },
    {
        "name": "Date range filter",
        "params": {
            "team_id": "1610612747",
            "season": "2023-24",
            "date_from_nullable": "01/01/2024",
            "date_to_nullable": "01/31/2024",
        },
        "expected_status": "has_data",
    },
]
