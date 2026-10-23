"""Box score parsers label every row with the game's home and away team IDs."""

import importlib

import pytest

from nba_api.stats.endpoints._parsers import _PARSER_REGISTRY
from nba_api.stats.endpoints._parsers._home_away import add_home_away_ids

BOX_SCORES = [
    "boxscoreadvancedv3",
    "boxscoredefensivev2",
    "boxscorefourfactorsv3",
    "boxscorehustlev2",
    "boxscoremiscv3",
    "boxscoreplayertrackv3",
    "boxscorescoringv3",
    "boxscoretraditionalv3",
    "boxscoreusagev3",
]


def test_add_home_away_ids_appends_to_every_row():
    data_sets = {"A": {"headers": ("gameId", "teamId"), "data": [["g", 1], ["g", 2]]}}

    add_home_away_ids(data_sets, {"homeTeamId": 1, "awayTeamId": 2})

    assert data_sets["A"]["headers"] == ["gameId", "teamId", "homeTeamId", "awayTeamId"]
    assert data_sets["A"]["data"] == [["g", 1, 1, 2], ["g", 2, 1, 2]]


@pytest.mark.parametrize("endpoint", BOX_SCORES)
def test_box_score_rows_carry_home_and_away_team_ids(endpoint):
    data = importlib.import_module(f"tests.unit.stats.endpoints.data.{endpoint}")
    sample = getattr(data, f"{endpoint.upper()}_SAMPLE")
    boxscore = next(
        v for v in sample.values() if isinstance(v, dict) and "homeTeamId" in v
    )
    home, away = boxscore["homeTeamId"], boxscore["awayTeamId"]

    data_sets = _PARSER_REGISTRY[endpoint](sample).get_data_sets()

    for name, data_set in data_sets.items():
        headers = data_set["headers"]
        assert headers[-2:] == ["homeTeamId", "awayTeamId"], name
        team_ids = {row[headers.index("teamId")] for row in data_set["data"]}
        assert team_ids <= {home, away}, name
        for row in data_set["data"]:
            assert row[-2:] == [home, away], name
