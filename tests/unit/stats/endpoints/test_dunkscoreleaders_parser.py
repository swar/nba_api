"""Unit tests for DunkScoreLeaders parser."""

import pytest

from nba_api.stats.endpoints._parsers.dunkscoreleaders import (
    NBAStatsDunkScoreLeadersParser,
)

from .data.dunkscoreleaders import DUNKSCORELEADERS_SAMPLE


@pytest.fixture
def json_fixture():
    """Load the DunkScoreLeaders fixture."""
    return DUNKSCORELEADERS_SAMPLE


@pytest.fixture
def parser(json_fixture):
    """Create a parser instance with the JSON fixture."""
    return NBAStatsDunkScoreLeadersParser(json_fixture)


class TestNBAStatsDunkScoreLeadersParser:
    """Test the DunkScoreLeaders parser."""

    def test_parser_initialization(self, parser, json_fixture):
        """Test that parser initializes correctly."""
        assert parser.nba_dict == json_fixture
        assert parser.dunks == json_fixture["dunks"]

    def test_get_dunkscoreleaders_headers_returns_list(self, parser):
        """Test get_dunkscoreleaders_headers returns a list."""
        headers = parser.get_dunkscoreleaders_headers()

        assert isinstance(headers, list)
        assert len(headers) > 0

    def test_get_dunkscoreleaders_headers_structure(self, parser, json_fixture):
        """Test headers include expected fields."""
        headers = parser.get_dunkscoreleaders_headers()
        first_dunk_keys = list(json_fixture["dunks"][0].keys())

        assert "gameId" in headers
        assert "gameDate" in headers
        assert "matchup" in headers
        assert "period" in headers
        assert "gameClockTime" in headers
        assert "eventNum" in headers
        assert "playerId" in headers
        assert "playerName" in headers
        assert "firstName" in headers
        assert "lastName" in headers
        assert "teamId" in headers
        assert "teamName" in headers
        assert "teamCity" in headers
        assert "teamAbbreviation" in headers
        assert "dunkScore" in headers
        assert "jumpSubscore" in headers
        assert "powerSubscore" in headers
        assert "styleSubscore" in headers
        assert "defensiveContestSubscore" in headers
        assert "maxBallHeight" in headers
        assert "ballSpeedThroughRim" in headers
        assert "playerVertical" in headers
        assert "hangTime" in headers
        assert "takeoffDistance" in headers
        assert "reverseDunk" in headers
        assert "dunk360" in headers
        assert "throughTheLegs" in headers
        assert "alleyOop" in headers
        assert "tipIn" in headers
        assert "selfOop" in headers
        assert "playerRotation" in headers
        assert "playerLateralSpeed" in headers
        assert "ballDistanceTraveled" in headers
        assert "ballReachBack" in headers
        assert "totalBallAcceleration" in headers
        assert "dunkingHand" in headers
        assert "jumpingFoot" in headers
        assert "passLength" in headers
        assert "catchingHand" in headers
        assert "catchDistance" in headers
        assert "lateralCatchDistance" in headers
        assert "passerId" in headers
        assert "passerName" in headers
        assert "passerFirstName" in headers
        assert "passerLastName" in headers
        assert "passReleasePoint" in headers
        assert "shooterId" in headers
        assert "shooterName" in headers
        assert "shooterFirstName" in headers
        assert "shooterLastName" in headers
        assert "shotReleasePoint" in headers
        assert "shotLength" in headers
        assert "defensiveContestLevel" in headers
        assert "possibleAttemptedCharge" in headers
        assert "videoAvailable" in headers

        # The parser headers should contain all keys from the data
        for key in first_dunk_keys:
            assert key in headers

    def test_get_dunkscoreleaders_data(self, parser, json_fixture):
        """Test dunk score leaders data extraction."""
        data = parser.get_dunkscoreleaders_data()

        assert isinstance(data, list)
        assert len(data) == len(json_fixture["dunks"]), "Should have row for each dunk"

        # Each row should be a list
        assert all(isinstance(row, list) for row in data)

    def test_get_data_sets(self, parser):
        """Test get_data_sets returns correct structure."""
        result = parser.get_data_sets()

        assert "DunkScoreLeaders" in result

        # Check DunkScoreLeaders structure
        assert "headers" in result["DunkScoreLeaders"]
        assert "data" in result["DunkScoreLeaders"]
        assert isinstance(result["DunkScoreLeaders"]["headers"], list)
        assert isinstance(result["DunkScoreLeaders"]["data"], list)
