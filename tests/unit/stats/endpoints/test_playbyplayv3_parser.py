"""Unit tests for PlayByPlayV3 parser."""

import json
import pytest
from pathlib import Path

from nba_api.stats.endpoints._parsers.playbyplayv3 import (
    NBAStatsPlayByPlayParserV3,
)


@pytest.fixture
def json_fixture():
    """Load the PlayByPlayV3 JSON fixture."""
    fixture_path = (
        Path(__file__).parents[4]
        / "docs"
        / "nba_api"
        / "stats"
        / "endpoints"
        / "responses"
        / "playbyplayv3.json"
    )

    if not fixture_path.exists():
        pytest.skip(f"Response file not found: {fixture_path}")

    with open(fixture_path) as f:
        return json.load(f)


@pytest.fixture
def parser(json_fixture):
    """Create a parser instance with the JSON fixture."""
    return NBAStatsPlayByPlayParserV3(json_fixture)


class TestNBAStatsPlayByPlayParserV3:
    """Test the PlayByPlay V3 parser."""

    def test_parser_initialization(self, parser, json_fixture):
        """Test that parser initializes correctly."""
        assert parser.nba_dict == json_fixture

    def test_get_playbyplay_headers_returns_tuple(self, parser):
        """Test get_playbyplay_headers returns a tuple."""
        headers = parser.get_playbyplay_headers()

        assert isinstance(headers, tuple)
        assert len(headers) > 0

    def test_get_playbyplay_headers_structure(self, parser):
        """Test headers include expected fields."""
        headers = parser.get_playbyplay_headers()

        # Should have gameId first
        assert "gameId" in headers
        # Should have action fields
        assert "actionNumber" in headers
        assert "clock" in headers
        assert "period" in headers
        assert "teamId" in headers
        assert "personId" in headers
        assert "description" in headers
        assert "actionType" in headers

    def test_get_playbyplay_data(self, parser, json_fixture):
        """Test play-by-play data extraction."""
        data = parser.get_playbyplay_data()

        assert isinstance(data, list)
        assert len(data) > 0, "Should have play-by-play actions"

        # Each row should be a list
        assert all(isinstance(row, list) for row in data)

        # First column should be gameId
        game_id = json_fixture["game"]["gameId"]
        for row in data:
            assert row[0] == game_id

    def test_get_videoavailable_headers(self, parser):
        """Test video available headers."""
        headers = parser.get_videoavailable_headers()

        assert headers == "videoAvailable"

    def test_get_videoavailable_data(self, parser, json_fixture):
        """Test video available data extraction."""
        data = parser.get_videoavailable_data()

        # Should match the videoAvailable field from game
        expected = json_fixture["game"]["videoAvailable"]
        assert data == expected

    def test_get_data_sets(self, parser):
        """Test get_data_sets returns correct structure."""
        result = parser.get_data_sets()

        assert "PlayByPlay" in result
        assert "AvailableVideo" in result

        # Check PlayByPlay structure
        assert "headers" in result["PlayByPlay"]
        assert "data" in result["PlayByPlay"]
        assert isinstance(result["PlayByPlay"]["headers"], tuple)
        assert isinstance(result["PlayByPlay"]["data"], list)

        # Check AvailableVideo structure
        assert "headers" in result["AvailableVideo"]
        assert "data" in result["AvailableVideo"]
        assert isinstance(result["AvailableVideo"]["headers"], list)
        assert isinstance(result["AvailableVideo"]["data"], list)

    def test_data_row_count_matches_actions(self, parser, json_fixture):
        """Test that data rows match number of actions."""
        data = parser.get_playbyplay_data()
        actions_count = len(json_fixture["game"]["actions"])

        assert len(data) == actions_count

    def test_headers_contain_key_action_fields(self, parser):
        """Test that parser headers contain key play-by-play fields."""
        headers = parser.get_playbyplay_headers()

        # Essential fields
        assert "gameId" in headers
        assert "actionNumber" in headers
        assert "clock" in headers
        assert "period" in headers
        # Player/team fields
        assert "teamId" in headers
        assert "personId" in headers
        assert "playerName" in headers
        # Shot fields
        assert "shotDistance" in headers
        assert "shotResult" in headers
        # Score fields
        assert "scoreHome" in headers
        assert "scoreAway" in headers
        assert "pointsTotal" in headers

    def test_data_row_count_matches_headers(self, parser):
        """Test that each data row has same number of columns as headers."""
        result = parser.get_data_sets()
        headers = result["PlayByPlay"]["headers"]
        data = result["PlayByPlay"]["data"]

        for i, row in enumerate(data):
            assert len(row) == len(headers), (
                f"Row {i} has {len(row)} columns but headers has {len(headers)}"
            )
