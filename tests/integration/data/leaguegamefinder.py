"""
Test data for LeagueGameFinder endpoint.

GitHub Issues:
- #446: game_id_nullable parameter does not filter results (API limitation)
- #526: date_from_nullable and date_to_nullable work correctly (DateFrom/DateTo)
        DateBegin/DateEnd parameters do NOT work (they are ignored by the API)

Known Limitations:
- The NBA Stats API ignores the game_id_nullable parameter
- Workaround: Filter results client-side using pandas after fetching data
- Using season_nullable helps reduce the result set size before filtering

Date Parameter Behavior:
- DateFrom/DateTo (date_from_nullable/date_to_nullable): ✓ Works correctly
- DateBegin/DateEnd: ✗ Ignored by API (returns unfiltered results)
- The current implementation using DateFrom/DateTo is correct

Expected response formats:
- String: "success" | "has_data" | "empty" | "error"
- Dict: {"status": "success", "min_rows": 1, "max_rows": 100}
"""

# Endpoint class name
ENDPOINT_CLASS = "LeagueGameFinder"

# Test cases
TEST_CASES = [
    {
        "description": "Basic team search for 2023-24 season",
        "params": {
            "player_or_team_abbreviation": "T",
            "season_nullable": "2023-24",
            "season_type_nullable": "Regular Season",
        },
        "expected": "has_data",  # Should return 2023-24 regular season games
    },
    {
        "description": "game_id_nullable does NOT filter (API limitation #446)",
        "params": {
            "player_or_team_abbreviation": "T",
            "season_nullable": "2023-24",
            "season_type_nullable": "Regular Season",
            "game_id_nullable": "0022301181",  # This is ignored by API
        },
        # Despite specifying game_id, API returns all 2023-24 regular season games
        "expected": {"status": "success", "min_rows": 1000},
        "notes": "game_id_nullable parameter is ignored by NBA API. "
        "Client-side filtering required: df[df['GAME_ID'] == '0022301181']",
    },
    {
        "description": "Player search - LeBron James",
        "params": {
            "player_or_team_abbreviation": "P",
            "player_id_nullable": "2544",
            "season_nullable": "2023-24",
        },
        "expected": "has_data",  # Should return LeBron's 2023-24 games
    },
    {
        "description": "Team ID filter",
        "params": {
            "player_or_team_abbreviation": "T",
            "team_id_nullable": "1610612747",  # Lakers
            "season_nullable": "2023-24",
        },
        "expected": "has_data",  # Should return Lakers games
    },
    {
        "description": "Conference filter",
        "params": {
            "player_or_team_abbreviation": "T",
            "season_nullable": "2023-24",
            "conference_nullable": "East",
        },
        "expected": "has_data",  # Should return Eastern Conference games
    },
    {
        "description": "Date range filter (issue #526) - DateFrom/DateTo work correctly",
        "params": {
            "player_or_team_abbreviation": "T",
            "date_from_nullable": "2021-01-01",
            "date_to_nullable": "2021-01-31",
        },
        "expected": {"status": "success", "min_rows": 400, "max_rows": 500},
        "notes": "DateFrom/DateTo parameters correctly filter by date range. "
        "Returns ~444 games for January 2021. DateBegin/DateEnd do NOT work.",
    },
    {
        "description": "Date range with season filter",
        "params": {
            "player_or_team_abbreviation": "T",
            "season_nullable": "2023-24",
            "date_from_nullable": "2024-01-01",
            "date_to_nullable": "2024-01-31",
        },
        "expected": {"status": "success", "min_rows": 400, "max_rows": 500},
        "notes": "Combining season and date filters works correctly.",
    },
    {
        "description": "Recent date range",
        "params": {
            "player_or_team_abbreviation": "T",
            "date_from_nullable": "2024-11-01",
            "date_to_nullable": "2024-11-13",
        },
        "expected": {"status": "success", "min_rows": 100},
        "notes": "Testing with recent dates to ensure current season works.",
    },
]
