"""Unit tests for BoxScoreDefensiveV2 parser."""

import json
from pathlib import Path

import pytest

from nba_api.stats.endpoints._parsers.boxscoredefensivev2 import (
    NBAStatsBoxscoreDefensiveV2Parser,
)

from .data.boxscoredefensivev2 import BOXSCOREDEFENSIVEV2_SAMPLE


@pytest.fixture
def parser():
    """Create parser instance with minimal test fixture."""
    return NBAStatsBoxscoreDefensiveV2Parser(BOXSCOREDEFENSIVEV2_SAMPLE)


@pytest.fixture
def json_fixture():
    """Load full BoxScoreDefensiveV2 JSON fixture."""
    fixture_path = (
        Path(__file__).parent.parent.parent.parent.parent
        / "docs"
        / "nba_api"
        / "stats"
        / "endpoints"
        / "responses"
        / "boxscoredefensivev2.json"
    )
    with open(fixture_path) as f:
        return json.load(f)


class TestNBAStatsBoxscoreDefensiveV2Parser:
    """Test the BoxScoreDefensiveV2 parser."""

    def test_parser_initialization(self, parser):
        """Test that parser initializes correctly."""
        assert parser.nba_dict == BOXSCOREDEFENSIVEV2_SAMPLE
        assert parser.boxscore == BOXSCOREDEFENSIVEV2_SAMPLE["boxScoreDefensive"]

    def test_get_team_headers(self, parser):
        """Test team headers are explicit and comprehensive."""
        headers = parser.get_team_headers()

        assert isinstance(headers, tuple)
        # Core fields
        assert "gameId" in headers
        assert "teamId" in headers
        assert "teamCity" in headers
        assert "teamName" in headers
        assert "teamTricode" in headers
        assert "teamSlug" in headers
        # Team stat
        assert "minutes" in headers

    def test_get_player_headers(self, parser):
        """Test player headers are explicit and comprehensive."""
        headers = parser.get_player_headers()

        assert isinstance(headers, tuple)
        # Core fields
        assert "gameId" in headers
        assert "teamId" in headers
        assert "personId" in headers
        assert "firstName" in headers
        assert "familyName" in headers
        assert "position" in headers
        # Defensive stats
        assert "matchupMinutes" in headers
        assert "partialPossessions" in headers
        assert "switchesOn" in headers
        assert "playerPoints" in headers
        assert "defensiveRebounds" in headers
        assert "matchupAssists" in headers
        assert "matchupTurnovers" in headers
        assert "steals" in headers
        assert "blocks" in headers
        assert "matchupFieldGoalsMade" in headers
        assert "matchupFieldGoalsAttempted" in headers
        assert "matchupFieldGoalPercentage" in headers
        assert "matchupThreePointersMade" in headers
        assert "matchupThreePointersAttempted" in headers
        assert "matchupThreePointerPercentage" in headers

    def test_get_team_data(self, parser):
        """Test team data extraction."""
        data = parser.get_team_data()

        assert isinstance(data, list)
        assert len(data) == 2  # Home and away teams

        # Check home team (first row)
        home_row = data[0]
        assert home_row[0] == "1022500165"  # gameId
        assert home_row[1] == 1611661323  # teamId
        assert home_row[2] == "Connecticut"  # teamCity
        assert home_row[3] == "Sun"  # teamName
        assert home_row[4] == "CON"  # teamTricode
        assert home_row[5] == "sun"  # teamSlug
        assert home_row[6] is None  # minutes

    def test_get_player_data(self, parser):
        """Test player data extraction."""
        data = parser.get_player_data()

        assert isinstance(data, list)
        assert len(data) == 2  # One player per team in fixture

        # Check first player (away team listed first)
        player_row = data[0]
        assert player_row[0] == "1022500165"  # gameId
        # Team info
        assert player_row[1] == 1611661328  # teamId (away team listed first)
        assert player_row[2] == "Seattle"  # teamCity
        # Player info
        assert player_row[6] == 1628931  # personId
        assert player_row[7] == "Gabby"  # firstName
        assert player_row[8] == "Williams"  # familyName
        # Stats (after gameId + 5 team fields + 8 player metadata fields = index 14)
        assert player_row[14] == "7:13"  # matchupMinutes
        assert player_row[15] == 40.6  # partialPossessions

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
            "boxScoreDefensive": {
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

        parser = NBAStatsBoxscoreDefensiveV2Parser(incomplete_data)
        data = parser.get_team_data()

        # Should return data with None for missing fields
        assert len(data) == 2
        assert data[0][0] == "123"  # gameId present

    def test_parser_with_full_response(self, json_fixture):
        """Test parser handles complete API response."""
        parser = NBAStatsBoxscoreDefensiveV2Parser(json_fixture)
        result = parser.get_data_sets()

        assert "TeamStats" in result
        assert "PlayerStats" in result

        # Should have data for both teams
        assert len(result["TeamStats"]["data"]) == 2

        # Should have data for all players
        player_count = len(result["PlayerStats"]["data"])
        assert player_count > 0  # At least some players

    def test_dataset_order_matches_expected_data(self, parser):
        """Test that dataset order matches expected_data in endpoint class.

        This prevents regressions where get_data_frames()[0] returns
        the wrong dataset (e.g., TeamStats instead of PlayerStats).
        """
        from nba_api.stats.endpoints.boxscoredefensivev2 import (
            BoxScoreDefensiveV2,
        )

        result = parser.get_data_sets()
        result_order = list(result.keys())
        expected_order = list(BoxScoreDefensiveV2.expected_data.keys())

        assert result_order == expected_order, (
            f"Dataset order mismatch: parser returns {result_order} "
            f"but expected_data defines {expected_order}"
        )
