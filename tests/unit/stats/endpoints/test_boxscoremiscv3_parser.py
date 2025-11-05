"""Unit tests for boxscoremiscv3 parser."""

import pytest

from nba_api.stats.endpoints._parsers.boxscoremiscv3 import (
    NBAStatsBoxscoreMiscV3Parser,
    TEAM_METADATA_FIELDS,
    PLAYER_METADATA_FIELDS,
    MISC_STATS_FIELDS,
)

from .data.boxscoremiscv3 import BOXSCOREMISCV3_SAMPLE


@pytest.fixture
def json_fixture():
    """Return the boxscoremiscv3 sample fixture."""
    return BOXSCOREMISCV3_SAMPLE


class TestBoxscoreMiscV3Parser:
    """Test the BoxscoreMiscV3 parser."""

    def test_parser_initialization(self, json_fixture):
        """Test parser initializes correctly with JSON fixture."""
        parser = NBAStatsBoxscoreMiscV3Parser(json_fixture)
        assert parser.nba_dict == json_fixture
        assert parser.boxscore == json_fixture.get("boxScoreMisc", {})

    def test_team_headers_structure(self, json_fixture):
        """Test team headers include all expected fields."""
        parser = NBAStatsBoxscoreMiscV3Parser(json_fixture)
        headers = parser.get_team_headers()

        # Should start with gameId
        assert headers[0] == "gameId"

        # Should include team metadata fields
        for i, field in enumerate(TEAM_METADATA_FIELDS):
            assert headers[1 + i] == field

        # Should include stats fields
        for i, field in enumerate(MISC_STATS_FIELDS):
            assert headers[1 + len(TEAM_METADATA_FIELDS) + i] == field

    def test_player_headers_structure(self, json_fixture):
        """Test player headers include all expected fields."""
        parser = NBAStatsBoxscoreMiscV3Parser(json_fixture)
        headers = parser.get_player_headers()

        # Should start with gameId
        assert headers[0] == "gameId"

        # Check structure: gameId + team_meta + player_meta + stats
        expected_length = (
            1 + len(TEAM_METADATA_FIELDS) + len(PLAYER_METADATA_FIELDS) +
            len(MISC_STATS_FIELDS)
        )
        assert len(headers) == expected_length

    def test_team_data_extraction(self, json_fixture):
        """Test team data is extracted correctly."""
        parser = NBAStatsBoxscoreMiscV3Parser(json_fixture)
        team_data = parser.get_team_data()

        # Should have 2 rows (home and away)
        assert len(team_data) == 2

        # Each row should be a list
        assert isinstance(team_data[0], list)
        assert isinstance(team_data[1], list)

        # Each row should have correct number of columns
        expected_cols = (
            1 + len(TEAM_METADATA_FIELDS) + len(MISC_STATS_FIELDS)
        )
        assert len(team_data[0]) == expected_cols
        assert len(team_data[1]) == expected_cols

        # Check gameId is present
        assert team_data[0][0] == "0022500148"
        assert team_data[1][0] == "0022500148"

    def test_player_data_extraction(self, json_fixture):
        """Test player data is extracted correctly."""
        parser = NBAStatsBoxscoreMiscV3Parser(json_fixture)
        player_data = parser.get_player_data()

        # Should have 2 players (1 from each team in fixture)
        assert len(player_data) == 2

        # Each row should be a list
        assert all(isinstance(row, list) for row in player_data)

        # Each row should have correct number of columns
        expected_cols = (
            1 + len(TEAM_METADATA_FIELDS) + len(PLAYER_METADATA_FIELDS) +
            len(MISC_STATS_FIELDS)
        )
        assert all(len(row) == expected_cols for row in player_data)

        # Check gameId is in each row
        assert all(row[0] == "0022500148" for row in player_data)

    def test_player_names_extracted(self, json_fixture):
        """Test player names are correctly extracted."""
        parser = NBAStatsBoxscoreMiscV3Parser(json_fixture)
        player_data = parser.get_player_data()

        # Player metadata starts after gameId + team metadata
        player_meta_start = 1 + len(TEAM_METADATA_FIELDS)

        # Find first name and family name indices
        first_name_idx = player_meta_start + 1  # personId at index 0
        family_name_idx = player_meta_start + 2

        # Extract names
        first_names = [row[first_name_idx] for row in player_data]
        family_names = [row[family_name_idx] for row in player_data]

        # Should have Shai and Zion
        assert "Shai" in first_names
        assert "Zion" in first_names
        assert "Gilgeous-Alexander" in family_names
        assert "Williamson" in family_names

    def test_player_stats_extracted(self, json_fixture):
        """Test player statistics are correctly extracted."""
        parser = NBAStatsBoxscoreMiscV3Parser(json_fixture)
        player_data = parser.get_player_data()

        # Stats start after gameId + team metadata + player metadata
        stats_start = (
            1 + len(TEAM_METADATA_FIELDS) + len(PLAYER_METADATA_FIELDS)
        )

        # Minutes index
        minutes_idx = stats_start
        pointsOffTurnovers_idx = stats_start + 1
        blocks_idx = stats_start + 9

        # Check Shai's stats (first player in awayTeam, so should be second in
        # our data due to ordering)
        shai_row = player_data[1]  # Away team is processed first
        assert shai_row[minutes_idx] == "29:59"
        assert shai_row[pointsOffTurnovers_idx] == 6
        assert shai_row[blocks_idx] == 0

        # Check Zion's stats
        zion_row = player_data[0]  # Home team is processed first alphabetically
        assert zion_row[minutes_idx] == "28:03"
        assert zion_row[pointsOffTurnovers_idx] == 4
        assert zion_row[blocks_idx] == 0

    def test_get_data_sets(self, json_fixture):
        """Test get_data_sets returns correct structure."""
        parser = NBAStatsBoxscoreMiscV3Parser(json_fixture)
        data_sets = parser.get_data_sets()

        # Should have both TeamStats and PlayerStats
        assert "TeamStats" in data_sets
        assert "PlayerStats" in data_sets

        # Each dataset should have headers and data
        assert "headers" in data_sets["TeamStats"]
        assert "data" in data_sets["TeamStats"]
        assert "headers" in data_sets["PlayerStats"]
        assert "data" in data_sets["PlayerStats"]

        # Verify data structure
        assert len(data_sets["TeamStats"]["data"]) == 2
        assert len(data_sets["PlayerStats"]["data"]) == 2

    def test_team_statistics_values(self, json_fixture):
        """Test team statistics values are correctly extracted."""
        parser = NBAStatsBoxscoreMiscV3Parser(json_fixture)
        team_data = parser.get_team_data()

        # Stats start after gameId + team metadata
        stats_start = 1 + len(TEAM_METADATA_FIELDS)

        # Indices for specific stats
        minutes_idx = stats_start
        pointsOffTurnovers_idx = stats_start + 1
        oppPointsOffTurnovers_idx = stats_start + 5

        # Home team (index 0)
        home_row = team_data[0]
        assert home_row[minutes_idx] == "240:00"
        assert home_row[pointsOffTurnovers_idx] == 25
        assert home_row[oppPointsOffTurnovers_idx] == 21

        # Away team (index 1)
        away_row = team_data[1]
        assert away_row[minutes_idx] == "240:00"
        assert away_row[pointsOffTurnovers_idx] == 21
        assert away_row[oppPointsOffTurnovers_idx] == 25

    def test_missing_fields_handled_gracefully(self):
        """Test parser handles missing fields gracefully with None values."""
        incomplete_data = {
            "boxScoreMisc": {
                "gameId": "TEST123",
                "homeTeam": {
                    "teamId": 111,
                    "teamCity": "Test",
                    "teamName": "Team",
                    "teamTricode": "TST",
                    "teamSlug": "test",
                    "players": [],
                    "statistics": {},  # Empty statistics
                },
                "awayTeam": {
                    "teamId": 222,
                    "teamCity": "Away",
                    "teamName": "Team",
                    "teamTricode": "AWY",
                    "teamSlug": "away",
                    "players": [],
                    "statistics": {},  # Empty statistics
                },
            }
        }

        parser = NBAStatsBoxscoreMiscV3Parser(incomplete_data)
        team_data = parser.get_team_data()

        # Should still process without error
        assert len(team_data) == 2
        # Stats should be None values
        assert team_data[0][1 + len(TEAM_METADATA_FIELDS)] is None
