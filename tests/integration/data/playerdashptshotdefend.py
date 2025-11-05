"""
Test cases for PlayerDashPtShotDefend endpoint.

GitHub Issues:
- User reports: "team_id requirement needs to be taken off"
- User reports: "returns empty for certain seasons"

Test case format: (params_dict, expected_result, test_id)
    params_dict: Exact parameters to pass to endpoint
    expected_result: "has_data" | "empty" | "error"
    test_id: Short identifier for pytest (becomes test name)
"""

TEST_CASES = [
    # Basic smoke test - does endpoint work at all?
    (
        {"player_id": "2544"},  # LeBron James
        "has_data",
        "basic",
    ),
    # User reported: "works in 2015-16 but not 2020-21"
    (
        {"player_id": "2544", "season": "2015-16"},
        "has_data",
        "season_2015-16",
    ),
    (
        {"player_id": "2544", "season": "2020-21"},
        "has_data",
        "season_2020-21",
    ),
    # User reported: "playoffs returns no data"
    (
        {"player_id": "2544", "season": "2023-24", "season_type_all_star": "Playoffs"},
        "has_data",  # or "empty" if we expect no data
        "playoffs",
    ),
]
