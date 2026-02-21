"""Integration scenario cases for LeagueGameFinder.

Issue/regression-style params and coarse expectations for scenario tests.
Prefer stable presence/range assertions over brittle exact values.
"""

ENDPOINT_CLASS = "LeagueGameFinder"

TEST_CASES = [
    {
        "name": "Basic team search for 2023-24 season",
        "params": {
            "player_or_team_abbreviation": "T",
            "season_nullable": "2023-24",
            "season_type_nullable": "Regular Season",
        },
        "expected_status": "has_data",
    },
    {
        "name": "game_id_nullable does NOT filter (API limitation #446)",
        "params": {
            "player_or_team_abbreviation": "T",
            "season_nullable": "2023-24",
            "season_type_nullable": "Regular Season",
            "game_id_nullable": "0022301181",
        },
        "expected_status": "success",
        "min_rows": 1000,
        "notes": "game_id_nullable parameter is ignored by NBA API. "
        "Client-side filtering required: df[df['GAME_ID'] == '0022301181']",
    },
    {
        "name": "Player search - LeBron James",
        "params": {
            "player_or_team_abbreviation": "P",
            "player_id_nullable": "2544",
            "season_nullable": "2023-24",
        },
        "expected_status": "has_data",
    },
    {
        "name": "Team ID filter",
        "params": {
            "player_or_team_abbreviation": "T",
            "team_id_nullable": "1610612747",
            "season_nullable": "2023-24",
        },
        "expected_status": "has_data",
    },
    {
        "name": "Conference filter",
        "params": {
            "player_or_team_abbreviation": "T",
            "season_nullable": "2023-24",
            "conference_nullable": "East",
        },
        "expected_status": "has_data",
    },
    {
        "name": "Date range filter (issue #526) - DateFrom/DateTo work correctly",
        "params": {
            "player_or_team_abbreviation": "T",
            "date_from_nullable": "2021-01-01",
            "date_to_nullable": "2021-01-31",
        },
        "expected_status": "success",
        "min_rows": 400,
        "max_rows": 500,
        "notes": "DateFrom/DateTo parameters correctly filter by date range. "
        "Returns ~444 games for January 2021. DateBegin/DateEnd do NOT work.",
    },
    {
        "name": "Date range with season filter",
        "params": {
            "player_or_team_abbreviation": "T",
            "season_nullable": "2023-24",
            "date_from_nullable": "2024-01-01",
            "date_to_nullable": "2024-01-31",
        },
        "expected_status": "success",
        "min_rows": 400,
        "max_rows": 500,
        "notes": "Combining season and date filters works correctly.",
    },
    {
        "name": "Recent date range",
        "params": {
            "player_or_team_abbreviation": "T",
            "date_from_nullable": "2024-11-01",
            "date_to_nullable": "2024-11-13",
        },
        "expected_status": "success",
        "min_rows": 100,
        "notes": "Testing with recent dates to ensure current season works.",
    },
]
