"""Unit tests for BoxScoreSummaryV3 endpoint."""

import json
import pytest
from pathlib import Path
from unittest.mock import Mock, patch
from pandas import DataFrame

from nba_api.stats.endpoints import BoxScoreSummaryV3
from nba_api.stats.endpoints._parsers import NBAStatsBoxscoreSummaryParserV3


@pytest.fixture
def json_fixture():
    """Load the BoxScoreSummaryV3 JSON fixture."""
    fixture_path = Path(__file__).parent / "data" / "boxscoresummaryv3.json"
    with open(fixture_path) as f:
        return json.load(f)


@pytest.fixture
def parser(json_fixture):
    """Create a parser instance with the JSON fixture."""
    return NBAStatsBoxscoreSummaryParserV3(json_fixture)


class TestNBAStatsBoxscoreSummaryParserV3:
    """Test the BoxScoreSummary v3 parser."""

    def test_parser_initialization(self, parser, json_fixture):
        """Test that parser initializes correctly."""
        assert parser.nba_dict == json_fixture

    def test_get_game_summary_headers(self, parser):
        """Test GameSummary headers match expected_data."""
        from nba_api.stats.endpoints._expected_data.boxscoresummaryv3 import (
            _EXPECTED_DATA,
        )

        headers = parser.get_game_summary_headers()
        assert headers == _EXPECTED_DATA["GameSummary"]

    def test_get_game_summary_data(self, parser):
        """Test GameSummary data extraction."""
        data = parser.get_game_summary_data()

        assert len(data) == 1
        assert data[0][0] == "0022500142"  # gameId
        assert data[0][1] == "20251101/SACMIL"  # gameCode
        assert data[0][2] == 3  # gameStatus
        assert data[0][3] == "Final"  # gameStatusText

    def test_get_game_info_headers(self, parser):
        """Test GameInfo headers match expected_data."""
        from nba_api.stats.endpoints._expected_data.boxscoresummaryv3 import (
            _EXPECTED_DATA,
        )

        headers = parser.get_game_info_headers()
        assert headers == _EXPECTED_DATA["GameInfo"]

    def test_get_game_info_data(self, parser):
        """Test GameInfo data extraction."""
        data = parser.get_game_info_data()

        assert len(data) == 1
        assert data[0][0] == "0022500142"  # gameId
        assert data[0][1] == "2025-11-01T17:00:00Z"  # gameDate
        assert data[0][2] == 17341  # attendance
        assert data[0][3] == "2:36"  # gameDuration

    def test_get_arena_info_headers(self, parser):
        """Test ArenaInfo headers match expected_data."""
        from nba_api.stats.endpoints._expected_data.boxscoresummaryv3 import (
            _EXPECTED_DATA,
        )

        headers = parser.get_arena_info_headers()
        assert headers == _EXPECTED_DATA["ArenaInfo"]

    def test_get_arena_info_data(self, parser):
        """Test ArenaInfo data extraction."""
        data = parser.get_arena_info_data()

        assert len(data) == 1
        assert data[0][0] == "0022500142"  # gameId
        assert data[0][1] == 642  # arenaId
        assert data[0][2] == "Fiserv Forum"  # arenaName
        assert data[0][3] == "Milwaukee"  # arenaCity
        assert data[0][4] == "WI"  # arenaState
        assert data[0][5] == "US"  # arenaCountry
        assert data[0][6] == "Central"  # arenaTimezone

    def test_get_officials_headers(self, parser):
        """Test Officials headers match expected_data."""
        from nba_api.stats.endpoints._expected_data.boxscoresummaryv3 import (
            _EXPECTED_DATA,
        )

        headers = parser.get_officials_headers()
        assert headers == _EXPECTED_DATA["Officials"]

    def test_get_officials_data(self, parser):
        """Test Officials data extraction."""
        data = parser.get_officials_data()

        assert len(data) == 3  # Three officials in fixture
        assert data[0][0] == "0022500142"  # gameId
        assert data[0][1] == 201245  # personId
        assert data[0][2] == "Marat Kogut"  # name

    def test_get_line_score_headers(self, parser):
        """Test LineScore headers match expected_data."""
        from nba_api.stats.endpoints._expected_data.boxscoresummaryv3 import (
            _EXPECTED_DATA,
        )

        headers = parser.get_line_score_headers()
        assert headers == _EXPECTED_DATA["LineScore"]

    def test_get_line_score_data(self, parser):
        """Test LineScore data extraction."""
        data = parser.get_line_score_data()

        assert len(data) == 2  # Two teams
        # Check structure includes gameId, teamId, scores
        assert data[0][0] == "0022500142"  # gameId
        assert isinstance(data[0][1], int)  # teamId

    def test_get_inactive_players_headers(self, parser):
        """Test InactivePlayers headers match expected_data."""
        from nba_api.stats.endpoints._expected_data.boxscoresummaryv3 import (
            _EXPECTED_DATA,
        )

        headers = parser.get_inactive_players_headers()
        assert headers == _EXPECTED_DATA["InactivePlayers"]

    def test_get_inactive_players_data(self, parser):
        """Test InactivePlayers data extraction."""
        data = parser.get_inactive_players_data()

        # Data should be a list (may be empty if no inactive players)
        assert isinstance(data, list)
        # Each row should have gameId in first column
        if data:
            assert data[0][0] == "0022500142"

    def test_get_last_five_meetings_headers(self, parser):
        """Test LastFiveMeetings headers match expected_data."""
        from nba_api.stats.endpoints._expected_data.boxscoresummaryv3 import (
            _EXPECTED_DATA,
        )

        headers = parser.get_last_five_meetings_headers()
        assert headers == _EXPECTED_DATA["LastFiveMeetings"]

    def test_get_last_five_meetings_data(self, parser):
        """Test LastFiveMeetings data extraction."""
        data = parser.get_last_five_meetings_data()

        # Data should be a list (may be empty or have up to 5 games)
        assert isinstance(data, list)
        assert len(data) <= 5

    def test_get_other_stats_headers(self, parser):
        """Test OtherStats headers match expected_data."""
        from nba_api.stats.endpoints._expected_data.boxscoresummaryv3 import (
            _EXPECTED_DATA,
        )

        headers = parser.get_other_stats_headers()
        assert headers == _EXPECTED_DATA["OtherStats"]

    def test_get_other_stats_data(self, parser):
        """Test OtherStats data extraction."""
        data = parser.get_other_stats_data()

        # Should have two rows (home and away team)
        assert len(data) == 2
        # Check structure
        assert data[0][0] == "0022500142"  # gameId
        assert isinstance(data[0][1], (int, type(None)))  # teamId

    def test_get_available_video_headers(self, parser):
        """Test AvailableVideo headers match expected_data."""
        from nba_api.stats.endpoints._expected_data.boxscoresummaryv3 import (
            _EXPECTED_DATA,
        )

        headers = parser.get_available_video_headers()
        assert headers == _EXPECTED_DATA["AvailableVideo"]

    def test_get_available_video_data(self, parser):
        """Test AvailableVideo data extraction."""
        data = parser.get_available_video_data()

        assert len(data) == 1
        assert data[0][0] == "0022500142"  # gameId

    def test_parser_with_missing_postgame_charts(self, json_fixture):
        """Test parser handles missing postgameCharts gracefully."""
        # Remove postgameCharts to test defensive coding
        modified_fixture = json_fixture.copy()
        del modified_fixture["boxScoreSummary"]["postgameCharts"]

        parser = NBAStatsBoxscoreSummaryParserV3(modified_fixture)
        data = parser.get_other_stats_data()

        # Should return two rows with None values
        assert len(data) == 2
        # Most fields should be None when postgameCharts is missing
        assert data[0][5] is None  # points should be None


class TestBoxScoreSummaryV3Endpoint:
    """Test the BoxScoreSummaryV3 endpoint."""

    def test_endpoint_initialization_without_request(self):
        """Test endpoint initializes without making HTTP request."""
        endpoint = BoxScoreSummaryV3(game_id="0022500142", get_request=False)

        assert endpoint.parameters == {"GameID": "0022500142"}
        assert endpoint.endpoint == "boxscoresummaryv3"

    def test_expected_data_structure(self):
        """Test that expected_data has all required datasets."""
        from nba_api.stats.endpoints._expected_data.boxscoresummaryv3 import (
            _EXPECTED_DATA,
        )

        expected_datasets = [
            "GameSummary",
            "GameInfo",
            "ArenaInfo",
            "Officials",
            "LineScore",
            "InactivePlayers",
            "LastFiveMeetings",
            "OtherStats",
            "AvailableVideo",
        ]

        for dataset in expected_datasets:
            assert dataset in _EXPECTED_DATA
            assert isinstance(_EXPECTED_DATA[dataset], list)
            assert len(_EXPECTED_DATA[dataset]) > 0

    def test_expected_data_matches_parser_headers(self):
        """Test that expected_data matches parser header methods."""
        from nba_api.stats.endpoints._expected_data.boxscoresummaryv3 import (
            _EXPECTED_DATA,
        )

        # Create a minimal JSON structure for parser
        minimal_json = {
            "boxScoreSummary": {
                "gameId": "0022500142",
                "gameCode": "test",
                "gameStatus": 3,
                "gameStatusText": "Final",
                "period": 4,
                "gameClock": "PT00M00.00S",
                "gameTimeUTC": "2025-11-01T21:00:00Z",
                "gameEt": "2025-11-01T17:00:00Z",
                "awayTeamId": 1,
                "homeTeamId": 2,
                "duration": "2:00",
                "attendance": 0,
                "sellout": 0,
                "arena": {},
                "officials": [],
                "homeTeam": {},
                "awayTeam": {},
                "lastFiveMeetings": [],
                "postgameCharts": {"homeTeam": {}, "awayTeam": {}},
                "videoAvailable": 0,
            }
        }

        parser = NBAStatsBoxscoreSummaryParserV3(minimal_json)

        # Verify headers match
        assert parser.get_game_summary_headers() == _EXPECTED_DATA["GameSummary"]
        assert parser.get_game_info_headers() == _EXPECTED_DATA["GameInfo"]
        assert parser.get_arena_info_headers() == _EXPECTED_DATA["ArenaInfo"]
        assert parser.get_officials_headers() == _EXPECTED_DATA["Officials"]
        assert parser.get_line_score_headers() == _EXPECTED_DATA["LineScore"]
        assert (
            parser.get_inactive_players_headers() == _EXPECTED_DATA["InactivePlayers"]
        )
        assert (
            parser.get_last_five_meetings_headers()
            == _EXPECTED_DATA["LastFiveMeetings"]
        )
        assert parser.get_other_stats_headers() == _EXPECTED_DATA["OtherStats"]
        assert parser.get_available_video_headers() == _EXPECTED_DATA["AvailableVideo"]

    @patch("nba_api.stats.library.http.NBAStatsHTTP.send_api_request")
    def test_endpoint_with_mocked_request(self, mock_request, json_fixture):
        """Test endpoint processes response correctly."""
        # Mock the HTTP response
        mock_response = Mock()
        mock_response.get_dict.return_value = json_fixture
        mock_response.get_data_sets.return_value = {
            "GameSummary": {"headers": [], "data": []},
            "GameInfo": {"headers": [], "data": []},
            "ArenaInfo": {"headers": [], "data": []},
            "Officials": {"headers": [], "data": []},
            "LineScore": {"headers": [], "data": []},
            "InactivePlayers": {"headers": [], "data": []},
            "LastFiveMeetings": {"headers": [], "data": []},
            "OtherStats": {"headers": [], "data": []},
            "AvailableVideo": {"headers": [], "data": []},
        }
        mock_request.return_value = mock_response

        endpoint = BoxScoreSummaryV3(game_id="0022500142")

        # Verify the endpoint was called
        mock_request.assert_called_once()

        # Verify datasets are accessible
        assert hasattr(endpoint, "game_summary")
        assert hasattr(endpoint, "game_info")
        assert hasattr(endpoint, "arena_info")
        assert hasattr(endpoint, "officials")
        assert hasattr(endpoint, "line_score")
        assert hasattr(endpoint, "inactive_players")
        assert hasattr(endpoint, "last_five_meetings")
        assert hasattr(endpoint, "other_stats")
        assert hasattr(endpoint, "available_video")

    def test_dataset_attributes_initialized(self):
        """Test that all dataset attributes are initialized in __init__."""
        endpoint = BoxScoreSummaryV3(game_id="0022500142", get_request=False)

        # All dataset attributes should be None before request
        assert endpoint.game_summary is None
        assert endpoint.game_info is None
        assert endpoint.arena_info is None
        assert endpoint.officials is None
        assert endpoint.line_score is None
        assert endpoint.inactive_players is None
        assert endpoint.last_five_meetings is None
        assert endpoint.other_stats is None
        assert endpoint.available_video is None
