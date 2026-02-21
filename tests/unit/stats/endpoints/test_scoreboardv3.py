"""Unit tests for ScoreboardV3 endpoint."""

from unittest.mock import Mock, patch

from nba_api.stats.endpoints import ScoreboardV3
from nba_api.stats.endpoints._parsers.scoreboardv3 import (
    NBAStatsScoreboardV3Parser,
)

from .data.scoreboardv3 import SCOREBOARDV3_SAMPLE


class TestScoreboardV3Endpoint:
    """Test the ScoreboardV3 endpoint."""

    def test_endpoint_initialization_without_request(self):
        """Test endpoint initializes without making HTTP request."""
        endpoint = ScoreboardV3(game_date="2025-11-05", get_request=False)

        assert endpoint.parameters["GameDate"] == "2025-11-05"
        assert endpoint.parameters["LeagueID"] == "00"
        assert endpoint.endpoint == "scoreboardv3"

    def test_endpoint_initialization_with_custom_league(self):
        """Test endpoint accepts custom league_id parameter."""
        endpoint = ScoreboardV3(
            game_date="2025-11-05", league_id="10", get_request=False
        )

        assert endpoint.parameters["GameDate"] == "2025-11-05"
        assert endpoint.parameters["LeagueID"] == "10"

    def test_expected_data_structure(self):
        """Test that expected_data has all required datasets."""
        from nba_api.stats.endpoints._expected_data.scoreboardv3 import (
            _EXPECTED_DATA,
        )

        expected_datasets = [
            "ScoreboardInfo",
            "GameHeader",
            "LineScore",
            "GameLeaders",
            "TeamLeaders",
            "Broadcasters",
        ]

        for dataset in expected_datasets:
            assert dataset in _EXPECTED_DATA
            assert isinstance(_EXPECTED_DATA[dataset], list)
            assert len(_EXPECTED_DATA[dataset]) > 0

    def test_expected_data_matches_parser_headers(self):
        """Test that expected_data matches parser header methods."""
        from nba_api.stats.endpoints._expected_data.scoreboardv3 import (
            _EXPECTED_DATA,
        )

        parser = NBAStatsScoreboardV3Parser(SCOREBOARDV3_SAMPLE)

        # Verify headers match
        assert parser.get_scoreboard_info_headers() == tuple(
            _EXPECTED_DATA["ScoreboardInfo"]
        )
        assert parser.get_game_header_headers() == tuple(_EXPECTED_DATA["GameHeader"])
        assert parser.get_line_score_headers() == tuple(_EXPECTED_DATA["LineScore"])
        assert parser.get_game_leaders_headers() == tuple(_EXPECTED_DATA["GameLeaders"])
        assert parser.get_team_leaders_headers() == tuple(_EXPECTED_DATA["TeamLeaders"])
        assert parser.get_broadcasters_headers() == tuple(
            _EXPECTED_DATA["Broadcasters"]
        )

    @patch("nba_api.stats.library.http.NBAStatsHTTP.send_api_request")
    def test_endpoint_with_mocked_request(self, mock_request):
        """Test endpoint processes response correctly."""
        # Mock the HTTP response
        mock_response = Mock()
        mock_response.get_dict.return_value = SCOREBOARDV3_SAMPLE
        mock_response.get_data_sets.return_value = {
            "ScoreboardInfo": {"headers": [], "data": []},
            "GameHeader": {"headers": [], "data": []},
            "LineScore": {"headers": [], "data": []},
            "GameLeaders": {"headers": [], "data": []},
            "TeamLeaders": {"headers": [], "data": []},
            "Broadcasters": {"headers": [], "data": []},
        }
        mock_request.return_value = mock_response

        endpoint = ScoreboardV3(game_date="2025-11-05")

        # Verify the endpoint was called
        mock_request.assert_called_once()

        # Verify get_data_sets was called with the endpoint name
        mock_response.get_data_sets.assert_called_once_with("scoreboardv3")

        # Verify datasets are accessible
        assert hasattr(endpoint, "scoreboard_info")
        assert hasattr(endpoint, "game_header")
        assert hasattr(endpoint, "line_score")
        assert hasattr(endpoint, "game_leaders")
        assert hasattr(endpoint, "team_leaders")
        assert hasattr(endpoint, "broadcasters")

    def test_dataset_attributes_initialized(self):
        """Test that all dataset attributes are initialized in __init__."""
        endpoint = ScoreboardV3(game_date="2025-11-05", get_request=False)

        # All dataset attributes should be None before request
        assert endpoint.scoreboard_info is None
        assert endpoint.game_header is None
        assert endpoint.line_score is None
        assert endpoint.game_leaders is None
        assert endpoint.team_leaders is None
        assert endpoint.broadcasters is None

    def test_endpoint_has_standard_attributes(self):
        """Test that endpoint has all standard Endpoint attributes."""
        endpoint = ScoreboardV3(game_date="2025-11-05", get_request=False)

        # Standard endpoint attributes
        assert hasattr(endpoint, "endpoint")
        assert hasattr(endpoint, "expected_data")
        assert hasattr(endpoint, "nba_response")
        assert hasattr(endpoint, "data_sets")
        assert hasattr(endpoint, "parameters")
        assert hasattr(endpoint, "proxy")
        assert hasattr(endpoint, "timeout")

    def test_endpoint_supports_custom_timeout(self):
        """Test that custom timeout parameter is respected."""
        endpoint = ScoreboardV3(game_date="2025-11-05", timeout=60, get_request=False)

        assert endpoint.timeout == 60

    def test_endpoint_supports_custom_headers(self):
        """Test that custom headers parameter is respected."""
        custom_headers = {"User-Agent": "test-agent"}
        endpoint = ScoreboardV3(
            game_date="2025-11-05", headers=custom_headers, get_request=False
        )

        assert endpoint.headers == custom_headers

    def test_endpoint_supports_proxy(self):
        """Test that proxy parameter is supported."""
        endpoint = ScoreboardV3(
            game_date="2025-11-05", proxy="http://proxy:8080", get_request=False
        )

        assert endpoint.proxy == "http://proxy:8080"
