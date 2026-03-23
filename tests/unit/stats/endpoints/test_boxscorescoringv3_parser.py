"""Unit tests for BoxScoreScoringV3 parser."""

import pytest

from nba_api.stats.endpoints._parsers.boxscorescoringv3 import (
    NBAStatsBoxscoreScoringV3Parser,
)

from .data.boxscorescoringv3 import BOXSCORESCORINGV3_SAMPLE


@pytest.fixture
def json_fixture():
    """Return the BoxScoreScoringV3 sample fixture."""
    return BOXSCORESCORINGV3_SAMPLE


class TestBoxscoreScoringV3Parser:
    """Test the BoxScoreScoringV3 parser."""

    def test_parser_initialization(self, json_fixture):
        """Test parser initializes with JSON fixture."""
        parser = NBAStatsBoxscoreScoringV3Parser(json_fixture)

        assert parser.nba_dict == json_fixture
        assert parser.boxscore == json_fixture.get("boxScoreScoring", {})

    def test_get_team_headers(self, json_fixture):
        """Test team headers include all expected fields."""
        parser = NBAStatsBoxscoreScoringV3Parser(json_fixture)
        headers = parser.get_team_headers()

        # Verify structure: gameId + team metadata + scoring stats
        assert headers[0] == "gameId"
        assert "teamId" in headers
        assert "teamCity" in headers
        assert "teamName" in headers
        assert "teamTricode" in headers
        assert "teamSlug" in headers
        assert "minutes" in headers
        assert "percentageFieldGoalsAttempted2pt" in headers
        assert "percentagePoints2pt" in headers
        assert "percentageAssistedFGM" in headers
        assert "percentageUnassistedFGM" in headers

    def test_get_player_headers(self, json_fixture):
        """Test player headers include all expected fields."""
        parser = NBAStatsBoxscoreScoringV3Parser(json_fixture)
        headers = parser.get_player_headers()

        # Verify structure: gameId + team metadata + player metadata + scoring stats
        assert headers[0] == "gameId"
        assert "teamId" in headers
        assert "personId" in headers
        assert "firstName" in headers
        assert "familyName" in headers
        assert "nameI" in headers
        assert "playerSlug" in headers
        assert "position" in headers
        assert "comment" in headers
        assert "jerseyNum" in headers
        assert "percentagePoints3pt" in headers

    def test_get_team_data(self, json_fixture):
        """Test team data extraction."""
        parser = NBAStatsBoxscoreScoringV3Parser(json_fixture)
        team_data = parser.get_team_data()

        # Should have 2 rows: home and away team
        assert len(team_data) == 2

        # Each row should be a list
        for row in team_data:
            assert isinstance(row, list)

        # First row should be home team
        home_row = team_data[0]
        assert home_row[0] == "1022500165"  # gameId
        assert home_row[1] == 1611661323  # homeTeamId
        assert home_row[2] == "Connecticut"  # teamCity
        assert home_row[3] == "Sun"  # teamName
        assert home_row[4] == "CON"  # teamTricode
        assert home_row[5] == "sun"  # teamSlug

        # Second row should be away team
        away_row = team_data[1]
        assert away_row[0] == "1022500165"  # gameId
        assert away_row[1] == 1611661328  # awayTeamId
        assert away_row[2] == "Seattle"  # teamCity
        assert away_row[3] == "Storm"  # teamName
        assert away_row[4] == "SEA"  # teamTricode
        assert away_row[5] == "storm"  # teamSlug

    def test_get_player_data(self, json_fixture):
        """Test player data extraction."""
        parser = NBAStatsBoxscoreScoringV3Parser(json_fixture)
        player_data = parser.get_player_data()

        # Should have 2 rows: 1 away player + 1 home player
        assert len(player_data) == 2

        # Each row should be a list
        for row in player_data:
            assert isinstance(row, list)

        # First row should be away team player
        away_player_row = player_data[0]
        assert away_player_row[0] == "1022500165"  # gameId
        assert away_player_row[1] == 1611661328  # awayTeamId
        assert away_player_row[6] == 1628931  # personId (Gabby Williams)
        assert away_player_row[7] == "Gabby"  # firstName
        assert away_player_row[8] == "Williams"  # familyName

        # Second row should be home team player
        home_player_row = player_data[1]
        assert home_player_row[0] == "1022500165"  # gameId
        assert home_player_row[1] == 1611661323  # homeTeamId
        assert home_player_row[6] == 1642809  # personId (Saniya Rivers)
        assert home_player_row[7] == "Saniya"  # firstName
        assert home_player_row[8] == "Rivers"  # familyName

    def test_get_data_sets(self, json_fixture):
        """Test get_data_sets returns correctly structured dictionary."""
        parser = NBAStatsBoxscoreScoringV3Parser(json_fixture)
        data_sets = parser.get_data_sets()

        assert "TeamStats" in data_sets
        assert "PlayerStats" in data_sets

        # TeamStats should have headers and data
        team_stats = data_sets["TeamStats"]
        assert "headers" in team_stats
        assert "data" in team_stats
        assert isinstance(team_stats["headers"], list)
        assert isinstance(team_stats["data"], list)
        assert len(team_stats["data"]) == 2

        # PlayerStats should have headers and data
        player_stats = data_sets["PlayerStats"]
        assert "headers" in player_stats
        assert "data" in player_stats
        assert isinstance(player_stats["headers"], list)
        assert isinstance(player_stats["data"], list)
        assert len(player_stats["data"]) == 2

    def test_scoring_stats_fields_present(self, json_fixture):
        """Test that all scoring statistics fields are extracted."""
        parser = NBAStatsBoxscoreScoringV3Parser(json_fixture)
        team_data = parser.get_team_data()
        player_data = parser.get_player_data()

        # Home team row should have scoring stats values
        home_row = team_data[0]
        headers = parser.get_team_headers()

        # Find indices of specific stats
        idx_minutes = headers.index("minutes")
        idx_2pt = headers.index("percentageFieldGoalsAttempted2pt")
        idx_3pt = headers.index("percentageFieldGoalsAttempted3pt")
        idx_pts_2pt = headers.index("percentagePoints2pt")
        idx_assisted = headers.index("percentageAssistedFGM")

        # Verify values are extracted (should be numeric or None)
        assert home_row[idx_minutes] is not None
        assert home_row[idx_2pt] is not None
        assert home_row[idx_3pt] is not None
        assert home_row[idx_pts_2pt] is not None
        assert home_row[idx_assisted] is not None

        # Player data should also have these values
        player_headers = parser.get_player_headers()
        away_player_row = player_data[0]

        idx_minutes = player_headers.index("minutes")
        idx_2pt = player_headers.index("percentageFieldGoalsAttempted2pt")
        idx_3pt = player_headers.index("percentageFieldGoalsAttempted3pt")

        assert away_player_row[idx_minutes] is not None
        assert away_player_row[idx_2pt] is not None
        assert away_player_row[idx_3pt] is not None

    def test_defensive_get_calls(self, json_fixture):
        """Test that parser uses defensive .get() calls throughout."""
        parser = NBAStatsBoxscoreScoringV3Parser(json_fixture)

        # Should not raise KeyError even if fields are missing
        team_data = parser.get_team_data()
        player_data = parser.get_player_data()
        data_sets = parser.get_data_sets()

        # All should complete without errors
        assert team_data is not None
        assert player_data is not None
        assert data_sets is not None

    def test_parser_with_missing_statistics_field(self):
        """Test parser handles missing statistics field gracefully."""
        incomplete_dict = {
            "boxScoreScoring": {
                "gameId": "test123",
                "homeTeam": {
                    "teamId": 123,
                    "teamCity": "City",
                    "teamName": "Team",
                    "teamTricode": "ABC",
                    "teamSlug": "slug",
                    "players": [],
                    # Missing statistics field
                },
                "awayTeam": {
                    "teamId": 456,
                    "teamCity": "City2",
                    "teamName": "Team2",
                    "teamTricode": "XYZ",
                    "teamSlug": "slug2",
                    "players": [],
                    # Missing statistics field
                },
            }
        }

        parser = NBAStatsBoxscoreScoringV3Parser(incomplete_dict)
        team_data = parser.get_team_data()

        # Should still extract data without error
        assert len(team_data) == 2
        # Stats values will be None
        assert team_data[0][6] is None  # minutes should be None

    def test_parser_with_missing_players(self):
        """Test parser handles missing players gracefully."""
        dict_no_players = {
            "boxScoreScoring": {
                "gameId": "test123",
                "homeTeam": {
                    "teamId": 123,
                    "teamCity": "City",
                    "teamName": "Team",
                    "teamTricode": "ABC",
                    "teamSlug": "slug",
                    # Missing players field
                    "statistics": {
                        "minutes": "48:00",
                        "percentageFieldGoalsAttempted2pt": 0.5,
                    },
                },
                "awayTeam": {
                    "teamId": 456,
                    "teamCity": "City2",
                    "teamName": "Team2",
                    "teamTricode": "XYZ",
                    "teamSlug": "slug2",
                    # Missing players field
                    "statistics": {
                        "minutes": "48:00",
                        "percentageFieldGoalsAttempted2pt": 0.5,
                    },
                },
            }
        }

        parser = NBAStatsBoxscoreScoringV3Parser(dict_no_players)
        player_data = parser.get_player_data()

        # Should return empty list without error
        assert len(player_data) == 0
