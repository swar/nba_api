"""Unit tests for BoxScoreMatchupsV3 parser."""

import json
from pathlib import Path

import pytest

from nba_api.stats.endpoints._parsers.boxscorematchupsv3 import (
    NBAStatsBoxscoreMatchupsParserV3,
)


@pytest.fixture
def json_fixture():
    """Load the BoxScoreMatchupsV3 JSON fixture."""
    fixture_path = (
        Path(__file__).parents[4]
        / "docs"
        / "nba_api"
        / "stats"
        / "endpoints"
        / "responses"
        / "boxscorematchupsv3.json"
    )

    if not fixture_path.exists():
        pytest.skip(f"Response file not found: {fixture_path}")

    with open(fixture_path) as f:
        return json.load(f)


@pytest.fixture
def parser(json_fixture):
    """Create a parser instance with the JSON fixture."""
    return NBAStatsBoxscoreMatchupsParserV3(json_fixture)


class TestNBAStatsBoxscoreMatchupsParserV3:
    """Test the BoxScoreMatchups V3 parser."""

    def test_parser_initialization(self, parser, json_fixture):
        """Test that parser initializes correctly."""
        assert parser.nba_dict == json_fixture

    def test_get_players_headers_returns_list(self, parser):
        """Test get_players_headers returns a list."""
        headers = parser.get_players_headers()

        assert isinstance(headers, list)
        assert len(headers) > 0

    def test_get_players_headers_structure(self, parser):
        """Test headers include expected fields."""
        headers = parser.get_players_headers()

        # Check for key fields with Off/Def suffixes
        assert "gameId" in headers
        assert any("Off" in h for h in headers), "Should have offensive player fields"
        assert any("Def" in h for h in headers), "Should have defensive player fields"
        # Team metadata
        assert any("team" in h.lower() for h in headers)

    def test_get_player_data(self, parser):
        """Test player matchup data extraction."""
        data = parser.get_player_data()

        assert isinstance(data, list)
        assert len(data) > 0, "Should have player matchup data"

        # Each row should be a list
        assert all(isinstance(row, list) for row in data)

    def test_get_data_sets(self, parser):
        """Test get_data_sets returns correct structure."""
        result = parser.get_data_sets()

        assert "PlayerStats" in result
        assert "headers" in result["PlayerStats"]
        assert "data" in result["PlayerStats"]

        assert isinstance(result["PlayerStats"]["headers"], list)
        assert isinstance(result["PlayerStats"]["data"], list)

    def test_headers_contain_key_fields(self, parser):
        """Test that parser headers contain key matchup fields."""
        headers = parser.get_players_headers()

        # Check for essential fields
        assert "gameId" in headers
        assert "teamId" in headers
        # Offensive player fields
        assert "personIdOff" in headers
        assert "firstNameOff" in headers
        # Defensive player fields
        assert "personIdDef" in headers
        assert "firstNameDef" in headers
        # Matchup statistics
        assert "matchupMinutes" in headers
        assert "playerPoints" in headers

    def test_data_row_count_matches_headers(self, parser):
        """Test that each data row has same number of columns as headers."""
        result = parser.get_data_sets()
        headers = result["PlayerStats"]["headers"]
        data = result["PlayerStats"]["data"]

        for i, row in enumerate(data):
            assert len(row) == len(headers), (
                f"Row {i} has {len(row)} columns but headers has {len(headers)}"
            )

    def test_parser_handles_nested_matchups(self, parser, json_fixture):
        """Test parser correctly processes nested matchup structure."""
        # Verify the fixture has nested structure
        assert "boxScoreMatchups" in json_fixture
        assert "homeTeam" in json_fixture["boxScoreMatchups"]
        assert "players" in json_fixture["boxScoreMatchups"]["homeTeam"]

        # Verify parser extracts data from nested structure
        data = parser.get_player_data()
        assert len(data) > 0, "Should extract data from nested matchups"

    def test_game_id_in_all_rows(self, parser, json_fixture):
        """Test that gameId appears in all data rows."""
        game_id = json_fixture["boxScoreMatchups"]["gameId"]
        data = parser.get_player_data()

        for row in data:
            assert row[0] == game_id, "First column should be gameId"
