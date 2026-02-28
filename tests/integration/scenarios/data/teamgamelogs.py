"""Integration scenario cases for TeamGameLogs.

Issue/regression-style params and coarse expectations for scenario tests.
Prefer stable presence/range assertions over brittle exact values.
"""

TEST_CASES = [
    {
        "name": "Lakers 2023-24 regular season",
        "params": {
            "team_id_nullable": "1610612747",
            "season_nullable": "2023-24",
            "season_type_nullable": "Regular Season",
        },
        "expected_status": "has_data",
        "validate_structure": True,
    },
    {
        "name": "All teams - last game only",
        "params": {
            "season_nullable": "2024-25",
            "season_type_nullable": "Regular Season",
            "last_n_games_nullable": "1",
        },
        "expected_status": "has_data",
    },
    {
        "name": "Home games only",
        "params": {
            "team_id_nullable": "1610612747",
            "season_nullable": "2023-24",
            "location_nullable": "Home",
        },
        "expected_status": "has_data",
    },
    {
        "name": "Wins only",
        "params": {
            "team_id_nullable": "1610612747",
            "season_nullable": "2023-24",
            "outcome_nullable": "W",
        },
        "expected_status": "has_data",
    },
    {
        "name": "Eastern Conference opponents",
        "params": {
            "team_id_nullable": "1610612747",
            "season_nullable": "2023-24",
            "vs_conference_nullable": "East",
        },
        "expected_status": "has_data",
    },
]
