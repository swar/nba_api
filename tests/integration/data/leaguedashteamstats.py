"""Scenario/issue-regression cases for LeagueDashTeamStats integration tests.

These scenarios represent reported behaviors and regression checks. Prefer
stable presence/range assertions over brittle exact-value assertions unless
values are reliably stable.
"""

ENDPOINT_CLASS = "LeagueDashTeamStats"

TEST_CASES = [
    {
        "name": "Atlanta Hawks 2023-24 regular season (IST bug regression test - should return GP=82)",
        "params": {
            "season": "2023-24",
            "team_id_nullable": "1610612737",
            "season_type_all_star": "Regular Season",
        },
        "expected_status": "success",
        "min_rows": 1,
    },
    {
        "name": "All teams 2024-25 regular season base stats",
        "params": {
            "season": "2024-25",
            "season_type_all_star": "Regular Season",
            "measure_type_detailed_defense": "Base",
            "per_mode_detailed": "PerGame",
        },
        "expected_status": "success",
        "min_rows": 30,
    },
    {
        "name": "Lakers 2023-24 playoffs",
        "params": {
            "season": "2023-24",
            "team_id_nullable": "1610612747",
            "season_type_all_star": "Playoffs",
        },
        "expected_status": "success",
    },
    {
        "name": "Warriors 2023-24 advanced stats",
        "params": {
            "season": "2023-24",
            "team_id_nullable": "1610612744",
            "season_type_all_star": "Regular Season",
            "measure_type_detailed_defense": "Advanced",
            "per_mode_detailed": "PerGame",
        },
        "expected_status": "has_data",
    },
    {
        "name": "Eastern Conference 2023-24",
        "params": {
            "season": "2023-24",
            "season_type_all_star": "Regular Season",
            "conference_nullable": "East",
        },
        "expected_status": "success",
        "min_rows": 15,
    },
]
