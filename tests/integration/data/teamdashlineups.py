"""Test data for TeamDashLineups endpoint."""

# Endpoint class name (PascalCase)
ENDPOINT_CLASS = "TeamDashLineups"

# Test cases
TEST_CASES = [
    {
        "description": "Cleveland Cavaliers 5-man lineups 2024-25",
        "params": {
            "team_id": 1610612739,
            "season": "2024-25",
            "season_type_all_star": "Regular Season",
            "group_quantity": 5,
            "measure_type_detailed_defense": "Base",
            "per_mode_detailed": "Totals",
        },
        "expected": "success",
    },
    {
        "description": "Lakers 2-man lineups 2023-24",
        "params": {
            "team_id": 1610612747,
            "season": "2023-24",
            "season_type_all_star": "Regular Season",
            "group_quantity": 2,
            "measure_type_detailed_defense": "Base",
            "per_mode_detailed": "PerGame",
        },
        "expected": "has_data",
    },
    {
        "description": "Warriors 3-man lineups playoffs 2023-24",
        "params": {
            "team_id": 1610612744,
            "season": "2023-24",
            "season_type_all_star": "Playoffs",
            "group_quantity": 3,
            "measure_type_detailed_defense": "Advanced",
            "per_mode_detailed": "Totals",
        },
        "expected": "success",
    },
    {
        "description": "Celtics 4-man lineups with date range",
        "params": {
            "team_id": 1610612738,
            "season": "2023-24",
            "season_type_all_star": "Regular Season",
            "group_quantity": 4,
            "measure_type_detailed_defense": "Base",
            "per_mode_detailed": "Totals",
            "date_from_nullable": "2024-01-01",
            "date_to_nullable": "2024-03-31",
        },
        "expected": "has_data",
    },
]
