"""Scenario/issue-regression cases for PlayerDashPtShotDefend integration tests.

These scenarios represent reported behaviors and regression checks. Prefer
stable presence/range assertions over brittle exact-value assertions unless
values are reliably stable.
"""

ENDPOINT_CLASS = "PlayerDashPtShotDefend"

TEST_CASES = [
    {
        "name": "Basic test - LeBron 2023-24 Lakers",
        "params": {"player_id": "2544", "team_id": 1610612747, "season": "2023-24"},
        "expected_status": "success",
    },
    {
        "name": "Team ID zero - all teams",
        "params": {"player_id": "2544", "team_id": 0, "season": "2023-24"},
        "expected_status": "has_data",
    },
    {
        "name": "Playoffs 2023-24",
        "params": {
            "player_id": "2544",
            "team_id": 1610612747,
            "season": "2023-24",
            "season_type_all_star": "Playoffs",
        },
        "expected_status": "success",
    },
]
