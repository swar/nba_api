"""Unit tests for BoxScoreHustleV2 parser."""

import json
import pytest
from pathlib import Path

from nba_api.stats.endpoints._parsers.boxscorehustlev2 import (
    NBAStatsBoxscoreHustleV2Parser,
)


@pytest.fixture
def json_fixture():
    """Load the BoxScoreHustleV2 JSON fixture."""
    fixture_path = (
        Path(__file__).parents[4]
        / "docs"
        / "nba_api"
        / "stats"
        / "endpoints"
        / "responses"
        / "boxscorehustlev2.json"
    )

    if not fixture_path.exists():
        pytest.skip(f"Response file not found: {fixture_path}")

    with open(fixture_path) as f:
        return json.load(f)


@pytest.fixture
def parser(json_fixture):
    """Create a parser instance with the JSON fixture."""
    return NBAStatsBoxscoreHustleV2Parser(json_fixture)


class TestNBAStatsBoxscoreHustleV2Parser:
    """Test the BoxScoreHustle V2 parser."""

    def test_parser_initialization(self, parser, json_fixture):
        """Test that parser initializes correctly."""
        assert parser.nba_dict == json_fixture
        assert parser.boxscore == json_fixture["boxScoreHustle"]

    def test_get_team_headers(self, parser):
        """Test TeamStats headers match expected structure."""
        headers = parser.get_team_headers()

        assert isinstance(headers, tuple)
        # gameId + 5 team metadata + 17 hustle stats
        assert len(headers) == 23
        assert headers[0] == "gameId"
        assert headers[1:6] == ("teamId", "teamCity", "teamName", "teamTricode", "teamSlug")
        # Hustle stats fields
        assert "minutes" in headers
        assert "points" in headers
        assert "contestedShots" in headers
        assert "deflections" in headers
        assert "chargesDrawn" in headers
        assert "screenAssists" in headers
        assert "looseBallsRecoveredTotal" in headers
        assert "boxOuts" in headers

    def test_get_player_headers(self, parser):
        """Test PlayerStats headers match expected structure."""
        headers = parser.get_player_headers()

        assert isinstance(headers, tuple)
        # gameId + 5 team + 8 player + 17 hustle stats = 31
        assert len(headers) == 31
        assert headers[0] == "gameId"
        # Team metadata
        assert "teamId" in headers
        # Player metadata
        assert "personId" in headers
        assert "firstName" in headers
        assert "familyName" in headers
        # Hustle stats
        assert "contestedShots" in headers
        assert "deflections" in headers
        assert "chargesDrawn" in headers
        assert "screenAssists" in headers
        assert "looseBallsRecoveredTotal" in headers

    def test_get_team_data(self, parser, json_fixture):
        """Test TeamStats data extraction."""
        data = parser.get_team_data()

        assert len(data) == 2  # home and away

        # Check structure (each row should be a list)
        for row in data:
            assert isinstance(row, list)
            assert len(row) == 23  # Should match header count

        # Verify gameId is first column
        game_id = json_fixture["boxScoreHustle"]["gameId"]
        assert data[0][0] == game_id
        assert data[1][0] == game_id

    def test_get_player_data(self, parser, json_fixture):
        """Test PlayerStats data extraction."""
        data = parser.get_player_data()

        assert isinstance(data, list)
        assert len(data) > 0, "Should have player data"

        # Each row should be a list with correct column count
        for row in data:
            assert isinstance(row, list)
            assert len(row) == 31  # Should match header count

        # First column should be gameId
        game_id = json_fixture["boxScoreHustle"]["gameId"]
        for row in data:
            assert row[0] == game_id

    def test_get_data_sets(self, parser):
        """Test get_data_sets returns all datasets."""
        result = parser.get_data_sets()

        assert "TeamStats" in result
        assert "PlayerStats" in result

        # Check structure
        assert "headers" in result["TeamStats"]
        assert "data" in result["TeamStats"]
        assert len(result["TeamStats"]["data"]) == 2

        assert "headers" in result["PlayerStats"]
        assert "data" in result["PlayerStats"]
        assert len(result["PlayerStats"]["data"]) > 0

    def test_headers_contain_key_hustle_fields(self, parser):
        """Test that headers contain all key hustle statistics."""
        team_headers = parser.get_team_headers()
        player_headers = parser.get_player_headers()

        # Key hustle fields that should be in both
        hustle_fields = [
            "contestedShots",
            "contestedShots2pt",
            "contestedShots3pt",
            "deflections",
            "chargesDrawn",
            "screenAssists",
            "screenAssistPoints",
            "looseBallsRecoveredOffensive",
            "looseBallsRecoveredDefensive",
            "looseBallsRecoveredTotal",
            "offensiveBoxOuts",
            "defensiveBoxOuts",
            "boxOuts",
        ]

        for field in hustle_fields:
            assert field in team_headers, f"{field} should be in team headers"
            assert field in player_headers, f"{field} should be in player headers"

    def test_data_row_count_matches_headers(self, parser):
        """Test that each data row has same number of columns as headers."""
        result = parser.get_data_sets()

        # Check TeamStats
        team_headers = result["TeamStats"]["headers"]
        team_data = result["TeamStats"]["data"]
        for i, row in enumerate(team_data):
            assert len(row) == len(team_headers), (
                f"Team row {i} has {len(row)} columns but headers has {len(team_headers)}"
            )

        # Check PlayerStats
        player_headers = result["PlayerStats"]["headers"]
        player_data = result["PlayerStats"]["data"]
        for i, row in enumerate(player_data):
            assert len(row) == len(player_headers), (
                f"Player row {i} has {len(row)} columns but headers has {len(player_headers)}"
            )

    def test_parser_processes_both_teams(self, parser, json_fixture):
        """Test parser extracts data from both home and away teams."""
        data = parser.get_team_data()

        home_team_id = json_fixture["boxScoreHustle"]["homeTeamId"]
        away_team_id = json_fixture["boxScoreHustle"]["awayTeamId"]

        # Get teamId indices (second column after gameId)
        team_ids = [row[1] for row in data]

        assert home_team_id in team_ids, "Should have home team data"
        assert away_team_id in team_ids, "Should have away team data"

    def test_player_data_includes_both_teams(self, parser, json_fixture):
        """Test player data includes players from both teams."""
        data = parser.get_player_data()
        headers = parser.get_player_headers()

        # Get teamId index
        team_id_index = headers.index("teamId")

        team_ids = set(row[team_id_index] for row in data)

        home_team_id = json_fixture["boxScoreHustle"]["homeTeamId"]
        away_team_id = json_fixture["boxScoreHustle"]["awayTeamId"]

        assert home_team_id in team_ids, "Should have home team players"
        assert away_team_id in team_ids, "Should have away team players"

    def test_headers_return_list_in_data_sets(self, parser):
        """Test that get_data_sets returns headers as list."""
        result = parser.get_data_sets()

        # Headers should be lists (not tuples) in data_sets
        assert isinstance(result["TeamStats"]["headers"], list)
        assert isinstance(result["PlayerStats"]["headers"], list)
