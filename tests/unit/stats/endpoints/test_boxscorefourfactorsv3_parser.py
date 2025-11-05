"""Unit tests for BoxScoreFourFactorsV3 parser."""

import json
from pathlib import Path

import pytest

from nba_api.stats.endpoints._parsers.boxscorefourfactorsv3 import (
    NBAStatsBoxscoreFourFactorsV3Parser,
)

from .data.boxscorefourfactorsv3 import BOXSCOREFOURFACTORSV3_SAMPLE


@pytest.fixture
def parser():
    """Create parser instance with minimal test fixture."""
    return NBAStatsBoxscoreFourFactorsV3Parser(BOXSCOREFOURFACTORSV3_SAMPLE)


@pytest.fixture
def json_fixture():
    """Load full BoxScoreFourFactorsV3 JSON fixture."""
    fixture_path = (
        Path(__file__).parent.parent.parent.parent.parent
        / "docs"
        / "nba_api"
        / "stats"
        / "endpoints"
        / "responses"
        / "boxscorefourfactorsv3.json"
    )
    with open(fixture_path) as f:
        return json.load(f)


class TestNBAStatsBoxscoreFourFactorsV3Parser:
    """Test the BoxScoreFourFactorsV3 parser."""

    def test_parser_initialization(self, parser):
        """Test that parser initializes correctly."""
        assert parser.nba_dict == BOXSCOREFOURFACTORSV3_SAMPLE
        assert parser.boxscore == BOXSCOREFOURFACTORSV3_SAMPLE["boxScoreFourFactors"]

    def test_get_team_headers(self, parser):
        """Test team headers are explicit and comprehensive."""
        headers = parser.get_team_headers()

        assert isinstance(headers, tuple)
        # Core fields
        assert "gameId" in headers
        assert "teamId" in headers
        assert "teamCity" in headers
        # Four factors stats
        assert "minutes" in headers
        assert "effectiveFieldGoalPercentage" in headers
        assert "freeThrowAttemptRate" in headers
        assert "teamTurnoverPercentage" in headers
        assert "offensiveReboundPercentage" in headers
        assert "oppEffectiveFieldGoalPercentage" in headers
        assert "oppFreeThrowAttemptRate" in headers
        assert "oppTeamTurnoverPercentage" in headers
        assert "oppOffensiveReboundPercentage" in headers

    def test_get_player_headers(self, parser):
        """Test player headers are explicit and comprehensive."""
        headers = parser.get_player_headers()

        assert isinstance(headers, tuple)
        # Core fields
        assert "gameId" in headers
        assert "teamId" in headers
        assert "personId" in headers
        assert "firstName" in headers
        # Four factors stats (same as team)
        assert "effectiveFieldGoalPercentage" in headers
        assert "freeThrowAttemptRate" in headers
        assert "teamTurnoverPercentage" in headers
        assert "offensiveReboundPercentage" in headers
        assert "oppEffectiveFieldGoalPercentage" in headers

    def test_get_team_data(self, parser):
        """Test team data extraction."""
        data = parser.get_team_data()

        assert isinstance(data, list)
        assert len(data) == 2  # Home and away teams

        # Check home team
        home_row = data[0]
        assert home_row[0] == "1022500165"  # gameId
        assert home_row[1] == 1611661323  # teamId
        assert home_row[2] == "Connecticut"  # teamCity

    def test_get_player_data(self, parser):
        """Test player data extraction."""
        data = parser.get_player_data()

        assert isinstance(data, list)
        assert len(data) == 2  # One player per team in fixture

        # Check first player (away team listed first)
        player_row = data[0]
        assert player_row[0] == "1022500165"  # gameId
        assert player_row[1] == 1611661328  # teamId (away team)
        assert player_row[6] == 1628931  # personId

    def test_get_data_sets(self, parser):
        """Test complete data extraction."""
        results = parser.get_data_sets()

        assert "TeamStats" in results
        assert "PlayerStats" in results

        # Team stats
        assert "headers" in results["TeamStats"]
        assert "data" in results["TeamStats"]
        assert len(results["TeamStats"]["data"]) == 2

        # Player stats
        assert "headers" in results["PlayerStats"]
        assert "data" in results["PlayerStats"]
        assert len(results["PlayerStats"]["data"]) == 2

    def test_handles_missing_fields(self):
        """Test parser handles missing optional fields gracefully."""
        incomplete_data = {
            "boxScoreFourFactors": {
                "gameId": "123",
                "homeTeam": {
                    "teamId": 1,
                    "teamCity": "Test",
                    "teamName": "Team",
                    "teamTricode": "TST",
                    "teamSlug": "test",
                    "players": [],
                    "statistics": {},
                },
                "awayTeam": {
                    "teamId": 2,
                    "teamCity": "Away",
                    "teamName": "Team2",
                    "teamTricode": "AW",
                    "teamSlug": "away",
                    "players": [],
                    "statistics": {},
                },
            }
        }

        parser = NBAStatsBoxscoreFourFactorsV3Parser(incomplete_data)
        data = parser.get_team_data()

        # Should return data with None for missing fields
        assert len(data) == 2
        assert data[0][0] == "123"  # gameId present

    def test_parser_with_full_response(self, json_fixture):
        """Test parser handles complete API response."""
        parser = NBAStatsBoxscoreFourFactorsV3Parser(json_fixture)
        result = parser.get_data_sets()

        assert "TeamStats" in result
        assert "PlayerStats" in result

        # Should have data for both teams
        assert len(result["TeamStats"]["data"]) == 2

        # Should have data for all players
        player_count = len(result["PlayerStats"]["data"])
        assert player_count > 0
