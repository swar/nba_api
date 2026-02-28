"""Unit tests for BoxScorePlayerTrackV3 parser."""

import pytest

from nba_api.stats.endpoints._parsers.boxscoreplayertrackv3 import (
    PLAYER_METADATA_FIELDS,
    PLAYERTRACK_STATS_FIELDS,
    TEAM_METADATA_FIELDS,
    NBAStatsBoxscorePlayerTrackV3Parser,
)

from .data.boxscoreplayertrackv3 import BOXSCOREPLAYERTRACKV3_SAMPLE


@pytest.fixture
def json_fixture():
    """Return the BoxScorePlayerTrackV3 sample fixture."""
    return BOXSCOREPLAYERTRACKV3_SAMPLE


class TestBoxScorePlayerTrackV3ParserConstants:
    """Test parser constants."""

    def test_team_metadata_fields(self):
        """Test that TEAM_METADATA_FIELDS contains expected fields."""
        assert "teamId" in TEAM_METADATA_FIELDS
        assert "teamCity" in TEAM_METADATA_FIELDS
        assert "teamName" in TEAM_METADATA_FIELDS
        assert "teamTricode" in TEAM_METADATA_FIELDS
        assert "teamSlug" in TEAM_METADATA_FIELDS
        assert len(TEAM_METADATA_FIELDS) == 5

    def test_player_metadata_fields(self):
        """Test that PLAYER_METADATA_FIELDS contains expected fields."""
        assert "personId" in PLAYER_METADATA_FIELDS
        assert "firstName" in PLAYER_METADATA_FIELDS
        assert "familyName" in PLAYER_METADATA_FIELDS
        assert "nameI" in PLAYER_METADATA_FIELDS
        assert "playerSlug" in PLAYER_METADATA_FIELDS
        assert "position" in PLAYER_METADATA_FIELDS
        assert "comment" in PLAYER_METADATA_FIELDS
        assert "jerseyNum" in PLAYER_METADATA_FIELDS
        assert len(PLAYER_METADATA_FIELDS) == 8

    def test_playertrack_stats_fields(self):
        """Test that PLAYERTRACK_STATS_FIELDS contains all expected statistics."""
        expected_stats = {
            "minutes",
            "speed",
            "distance",
            "reboundChancesOffensive",
            "reboundChancesDefensive",
            "reboundChancesTotal",
            "touches",
            "secondaryAssists",
            "freeThrowAssists",
            "passes",
            "assists",
            "contestedFieldGoalsMade",
            "contestedFieldGoalsAttempted",
            "contestedFieldGoalPercentage",
            "uncontestedFieldGoalsMade",
            "uncontestedFieldGoalsAttempted",
            "uncontestedFieldGoalsPercentage",
            "fieldGoalPercentage",
            "defendedAtRimFieldGoalsMade",
            "defendedAtRimFieldGoalsAttempted",
            "defendedAtRimFieldGoalPercentage",
        }
        assert set(PLAYERTRACK_STATS_FIELDS) == expected_stats
        assert len(PLAYERTRACK_STATS_FIELDS) == 21


class TestBoxScorePlayerTrackV3ParserInitialization:
    """Test parser initialization."""

    def test_parser_initialization(self, json_fixture):
        """Test parser initializes correctly with fixture data."""
        parser = NBAStatsBoxscorePlayerTrackV3Parser(json_fixture)

        assert parser.nba_dict == json_fixture
        assert "boxScorePlayerTrack" in parser.nba_dict
        assert parser.boxscore == json_fixture["boxScorePlayerTrack"]

    def test_parser_initialization_with_missing_root_key(self):
        """Test parser handles missing boxScorePlayerTrack key gracefully."""
        empty_dict = {}
        parser = NBAStatsBoxscorePlayerTrackV3Parser(empty_dict)

        assert parser.nba_dict == empty_dict
        assert parser.boxscore == {}


class TestBoxScorePlayerTrackV3ParserHeaders:
    """Test parser header generation."""

    def test_get_team_headers(self, json_fixture):
        """Test team headers are correctly formatted."""
        parser = NBAStatsBoxscorePlayerTrackV3Parser(json_fixture)
        headers = parser.get_team_headers()

        # Should have gameId + team metadata + stats fields
        assert isinstance(headers, tuple)
        assert headers[0] == "gameId"
        assert headers[1:6] == TEAM_METADATA_FIELDS
        assert headers[6:] == PLAYERTRACK_STATS_FIELDS
        assert len(headers) == 1 + len(TEAM_METADATA_FIELDS) + len(
            PLAYERTRACK_STATS_FIELDS
        )

    def test_get_player_headers(self, json_fixture):
        """Test player headers are correctly formatted."""
        parser = NBAStatsBoxscorePlayerTrackV3Parser(json_fixture)
        headers = parser.get_player_headers()

        # Should have gameId + team metadata + player metadata + stats fields
        assert isinstance(headers, tuple)
        assert headers[0] == "gameId"
        team_metadata_slice = slice(1, 6)
        player_metadata_slice = slice(6, 14)
        assert headers[team_metadata_slice] == TEAM_METADATA_FIELDS
        assert headers[player_metadata_slice] == PLAYER_METADATA_FIELDS
        assert headers[14:] == PLAYERTRACK_STATS_FIELDS
        expected_length = (
            1
            + len(TEAM_METADATA_FIELDS)
            + len(PLAYER_METADATA_FIELDS)
            + len(PLAYERTRACK_STATS_FIELDS)
        )
        assert len(headers) == expected_length


class TestBoxScorePlayerTrackV3ParserTeamData:
    """Test parser team data extraction."""

    def test_get_team_data_returns_list(self, json_fixture):
        """Test get_team_data returns a list."""
        parser = NBAStatsBoxscorePlayerTrackV3Parser(json_fixture)
        team_data = parser.get_team_data()

        assert isinstance(team_data, list)

    def test_get_team_data_has_two_rows(self, json_fixture):
        """Test get_team_data returns exactly 2 rows (home and away)."""
        parser = NBAStatsBoxscorePlayerTrackV3Parser(json_fixture)
        team_data = parser.get_team_data()

        assert len(team_data) == 2

    def test_get_team_data_row_structure(self, json_fixture):
        """Test each team data row has correct structure."""
        parser = NBAStatsBoxscorePlayerTrackV3Parser(json_fixture)
        team_data = parser.get_team_data()

        for row in team_data:
            assert isinstance(row, list)
            expected_length = (
                1 + len(TEAM_METADATA_FIELDS) + len(PLAYERTRACK_STATS_FIELDS)
            )
            assert len(row) == expected_length

    def test_get_team_data_contains_game_id(self, json_fixture):
        """Test team data rows contain gameId."""
        parser = NBAStatsBoxscorePlayerTrackV3Parser(json_fixture)
        team_data = parser.get_team_data()

        expected_game_id = json_fixture["boxScorePlayerTrack"]["gameId"]
        for row in team_data:
            assert row[0] == expected_game_id

    def test_get_team_data_contains_team_metadata(self, json_fixture):
        """Test team data rows contain team metadata."""
        parser = NBAStatsBoxscorePlayerTrackV3Parser(json_fixture)
        team_data = parser.get_team_data()

        # Check home team (parser iterates ["homeTeam", "awayTeam"] order)
        home_team = json_fixture["boxScorePlayerTrack"]["homeTeam"]
        home_row = team_data[0]  # Home team is first
        assert home_row[1] == home_team["teamId"]
        assert home_row[2] == home_team["teamCity"]
        assert home_row[3] == home_team["teamName"]
        assert home_row[4] == home_team["teamTricode"]
        assert home_row[5] == home_team["teamSlug"]

    def test_get_team_data_contains_statistics(self, json_fixture):
        """Test team data rows contain statistics."""
        parser = NBAStatsBoxscorePlayerTrackV3Parser(json_fixture)
        team_data = parser.get_team_data()

        # Check that statistics are populated
        # Skip gameId (index 0) and team metadata (indices 1-5)
        stats_start_index = 6
        home_row = team_data[0]  # Home team is first
        assert home_row[stats_start_index] == "240:00"  # minutes


class TestBoxScorePlayerTrackV3ParserPlayerData:
    """Test parser player data extraction."""

    def test_get_player_data_returns_list(self, json_fixture):
        """Test get_player_data returns a list."""
        parser = NBAStatsBoxscorePlayerTrackV3Parser(json_fixture)
        player_data = parser.get_player_data()

        assert isinstance(player_data, list)

    def test_get_player_data_has_correct_count(self, json_fixture):
        """Test get_player_data returns correct number of players."""
        parser = NBAStatsBoxscorePlayerTrackV3Parser(json_fixture)
        player_data = parser.get_player_data()

        # Fixture has 1 home player and 1 away player
        assert len(player_data) == 2

    def test_get_player_data_row_structure(self, json_fixture):
        """Test each player data row has correct structure."""
        parser = NBAStatsBoxscorePlayerTrackV3Parser(json_fixture)
        player_data = parser.get_player_data()

        expected_length = (
            1
            + len(TEAM_METADATA_FIELDS)
            + len(PLAYER_METADATA_FIELDS)
            + len(PLAYERTRACK_STATS_FIELDS)
        )
        for row in player_data:
            assert isinstance(row, list)
            assert len(row) == expected_length

    def test_get_player_data_contains_game_id(self, json_fixture):
        """Test player data rows contain gameId."""
        parser = NBAStatsBoxscorePlayerTrackV3Parser(json_fixture)
        player_data = parser.get_player_data()

        expected_game_id = json_fixture["boxScorePlayerTrack"]["gameId"]
        for row in player_data:
            assert row[0] == expected_game_id

    def test_get_player_data_contains_team_metadata(self, json_fixture):
        """Test player data rows contain team metadata."""
        parser = NBAStatsBoxscorePlayerTrackV3Parser(json_fixture)
        player_data = parser.get_player_data()

        away_team = json_fixture["boxScorePlayerTrack"]["awayTeam"]
        away_row = player_data[0]  # First player is from away team
        assert away_row[1] == away_team["teamId"]
        assert away_row[2] == away_team["teamCity"]
        assert away_row[3] == away_team["teamName"]

    def test_get_player_data_contains_player_metadata(self, json_fixture):
        """Test player data rows contain player metadata."""
        parser = NBAStatsBoxscorePlayerTrackV3Parser(json_fixture)
        player_data = parser.get_player_data()

        away_team = json_fixture["boxScorePlayerTrack"]["awayTeam"]
        expected_player = away_team["players"][0]
        away_row = player_data[0]

        # Player metadata starts at index 6 (after gameId + team metadata)
        player_metadata_start = 6
        assert away_row[player_metadata_start] == expected_player["personId"]
        assert away_row[player_metadata_start + 1] == expected_player["firstName"]
        assert away_row[player_metadata_start + 2] == expected_player["familyName"]

    def test_get_player_data_contains_statistics(self, json_fixture):
        """Test player data rows contain statistics."""
        parser = NBAStatsBoxscorePlayerTrackV3Parser(json_fixture)
        player_data = parser.get_player_data()

        away_team = json_fixture["boxScorePlayerTrack"]["awayTeam"]
        expected_player = away_team["players"][0]
        expected_stats = expected_player["statistics"]
        away_row = player_data[0]

        # Statistics start at index 14
        stats_start_index = 14
        assert away_row[stats_start_index] == expected_stats["minutes"]
        assert away_row[stats_start_index + 1] == expected_stats["speed"]
        assert away_row[stats_start_index + 2] == expected_stats["distance"]


class TestBoxScorePlayerTrackV3ParserDataSets:
    """Test parser get_data_sets method."""

    def test_get_data_sets_returns_dict(self, json_fixture):
        """Test get_data_sets returns a dictionary."""
        parser = NBAStatsBoxscorePlayerTrackV3Parser(json_fixture)
        data_sets = parser.get_data_sets()

        assert isinstance(data_sets, dict)

    def test_get_data_sets_has_required_keys(self, json_fixture):
        """Test get_data_sets has TeamStats and PlayerStats keys."""
        parser = NBAStatsBoxscorePlayerTrackV3Parser(json_fixture)
        data_sets = parser.get_data_sets()

        assert "TeamStats" in data_sets
        assert "PlayerStats" in data_sets
        assert len(data_sets) == 2

    def test_get_data_sets_structure(self, json_fixture):
        """Test each dataset has headers and data."""
        parser = NBAStatsBoxscorePlayerTrackV3Parser(json_fixture)
        data_sets = parser.get_data_sets()

        for _dataset_name, dataset in data_sets.items():
            assert isinstance(dataset, dict)
            assert "headers" in dataset
            assert "data" in dataset
            assert isinstance(dataset["headers"], list)
            assert isinstance(dataset["data"], list)

    def test_team_stats_dataset(self, json_fixture):
        """Test TeamStats dataset."""
        parser = NBAStatsBoxscorePlayerTrackV3Parser(json_fixture)
        data_sets = parser.get_data_sets()

        team_stats = data_sets["TeamStats"]
        assert len(team_stats["headers"]) == 1 + len(TEAM_METADATA_FIELDS) + len(
            PLAYERTRACK_STATS_FIELDS
        )
        assert len(team_stats["data"]) == 2

    def test_player_stats_dataset(self, json_fixture):
        """Test PlayerStats dataset."""
        parser = NBAStatsBoxscorePlayerTrackV3Parser(json_fixture)
        data_sets = parser.get_data_sets()

        player_stats = data_sets["PlayerStats"]
        assert len(player_stats["headers"]) == 1 + len(TEAM_METADATA_FIELDS) + len(
            PLAYER_METADATA_FIELDS
        ) + len(PLAYERTRACK_STATS_FIELDS)
        assert len(player_stats["data"]) == 2  # 1 home + 1 away player


class TestBoxScorePlayerTrackV3ParserEdgeCases:
    """Test parser edge cases."""

    def test_parser_with_empty_boxscore(self):
        """Test parser handles empty boxScorePlayerTrack gracefully."""
        empty_response = {"boxScorePlayerTrack": {}}
        parser = NBAStatsBoxscorePlayerTrackV3Parser(empty_response)

        team_data = parser.get_team_data()
        assert isinstance(team_data, list)
        assert len(team_data) == 2  # Should still return 2 rows with None values

    def test_parser_with_no_players(self):
        """Test parser handles teams with no players."""
        response = {
            "boxScorePlayerTrack": {
                "gameId": "0022500001",
                "homeTeam": {
                    "teamId": 1610612760,
                    "teamCity": "Oklahoma City",
                    "teamName": "Thunder",
                    "teamTricode": "OKC",
                    "teamSlug": "thunder",
                    "players": [],
                    "statistics": {},
                },
                "awayTeam": {
                    "teamId": 1610612740,
                    "teamCity": "New Orleans",
                    "teamName": "Pelicans",
                    "teamTricode": "NOP",
                    "teamSlug": "pelicans",
                    "players": [],
                    "statistics": {},
                },
            }
        }
        parser = NBAStatsBoxscorePlayerTrackV3Parser(response)

        player_data = parser.get_player_data()
        assert isinstance(player_data, list)
        assert len(player_data) == 0

    def test_parser_with_missing_statistics(self):
        """Test parser handles players with missing statistics fields."""
        response = {
            "boxScorePlayerTrack": {
                "gameId": "0022500001",
                "homeTeam": {
                    "teamId": 1610612760,
                    "teamCity": "Oklahoma City",
                    "teamName": "Thunder",
                    "teamTricode": "OKC",
                    "teamSlug": "thunder",
                    "players": [
                        {
                            "personId": 1630598,
                            "firstName": "Aaron",
                            "familyName": "Wiggins",
                            "nameI": "A. Wiggins",
                            "playerSlug": "aaron-wiggins",
                            "position": "F",
                            "comment": "",
                            "jerseyNum": "21",
                            "statistics": {"minutes": "26:29", "speed": 4.37},
                        }
                    ],
                    "statistics": {},
                },
                "awayTeam": {
                    "teamId": 1610612740,
                    "teamCity": "New Orleans",
                    "teamName": "Pelicans",
                    "teamTricode": "NOP",
                    "teamSlug": "pelicans",
                    "players": [],
                    "statistics": {},
                },
            }
        }
        parser = NBAStatsBoxscorePlayerTrackV3Parser(response)

        player_data = parser.get_player_data()
        assert len(player_data) == 1
        # Row should have None for missing stats fields
        assert player_data[0][14] == "26:29"  # minutes
        assert player_data[0][15] == 4.37  # speed
        assert player_data[0][16] is None  # distance (missing)
