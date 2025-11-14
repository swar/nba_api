"""
Test data for TeamGameLogs endpoint.

GitHub Issues:
- Endpoint was retired in v1.11.0 but is now working again (restored in v1.11.3)

Key Differences from TeamGameLog:
- TeamGameLog: Single team, required team_id parameter
- TeamGameLogs: Multiple teams, optional team_id_nullable parameter
- TeamGameLogs: Includes rank fields (_RANK) for all statistics
- TeamGameLogs: More filtering options (conference, division, measure type)

Expected response formats:
- String: "success" | "has_data" | "empty" | "error"
- Dict: {"status": "success", "min_rows": 1, "max_rows": 100}
"""

# Endpoint class name
ENDPOINT_CLASS = "TeamGameLogs"

# Test cases
TEST_CASES = [
    {
        "description": "Lakers 2023-24 regular season",
        "params": {
            "team_id_nullable": "1610612747",
            "season_nullable": "2023-24",
            "season_type_nullable": "Regular Season",
        },
        "expected": {
            "status": "has_data",
            "validate_structure": True,  # Enable strict validation
        },
    },
    {
        "description": "All teams - last game only",
        "params": {
            "season_nullable": "2024-25",
            "season_type_nullable": "Regular Season",
            "last_n_games_nullable": "1",
        },
        "expected": "has_data",  # Should return ~30 games (one per team)
    },
    {
        "description": "Home games only",
        "params": {
            "team_id_nullable": "1610612747",
            "season_nullable": "2023-24",
            "location_nullable": "Home",
        },
        "expected": "has_data",  # Should return ~41 home games
    },
    {
        "description": "Wins only",
        "params": {
            "team_id_nullable": "1610612747",
            "season_nullable": "2023-24",
            "outcome_nullable": "W",
        },
        "expected": "has_data",  # Should return only winning games
    },
    {
        "description": "Eastern Conference opponents",
        "params": {
            "team_id_nullable": "1610612747",  # Lakers (West)
            "season_nullable": "2023-24",
            "vs_conference_nullable": "East",
        },
        "expected": "has_data",  # Games vs Eastern Conference
    },
]
