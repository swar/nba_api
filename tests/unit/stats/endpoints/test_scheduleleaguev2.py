"""Unit tests for ScheduleLeagueV2 endpoint."""

from unittest.mock import Mock, patch

import pytest

from nba_api.stats.endpoints import ScheduleLeagueV2
from nba_api.stats.library.parserv3 import NBAStatsScheduleLeagueV2Parser

from .data.scheduleleaguev2 import (
    SCHEDULELEAGUEV2_2015_16,
    SCHEDULELEAGUEV2_2020_21,
)


@pytest.fixture
def json_fixture_2020():
    """Get the ScheduleLeagueV2 2020-21 test data."""
    return SCHEDULELEAGUEV2_2020_21


@pytest.fixture
def json_fixture_2015():
    """Get the ScheduleLeagueV2 2015-16 test data."""
    return SCHEDULELEAGUEV2_2015_16


@pytest.fixture
def parser_2020(json_fixture_2020):
    """Create a parser instance with the 2020-21 JSON fixture."""
    return NBAStatsScheduleLeagueV2Parser(json_fixture_2020)


@pytest.fixture
def parser_2015(json_fixture_2015):
    """Create a parser instance with the 2015-16 JSON fixture."""
    return NBAStatsScheduleLeagueV2Parser(json_fixture_2015)


class TestNBAStatsScheduleLeagueV2Parser:
    """Test the ScheduleLeagueV2 parser."""

    def test_parser_initialization_2020(self, parser_2020, json_fixture_2020):
        """Test that parser initializes correctly with 2020-21 data."""
        assert parser_2020.nba_dict == json_fixture_2020

    def test_parser_initialization_2015(self, parser_2015, json_fixture_2015):
        """Test that parser initializes correctly with 2015-16 data."""
        assert parser_2015.nba_dict == json_fixture_2015

    def test_get_weeks_headers_2020(self, parser_2020):
        """Test weeks headers extraction with 2020-21 data (has weeks)."""
        headers = parser_2020.get_weeks_headers()

        assert isinstance(headers, tuple)
        assert "leagueId" in headers
        assert "seasonYear" in headers
        assert "weekNumber" in headers
        assert "weekName" in headers
        assert "startDate" in headers
        assert "endDate" in headers

    def test_get_weeks_headers_2015(self, parser_2015):
        """Test weeks headers extraction with 2015-16 data (empty weeks array).

        The parser should return default headers when weeks array is empty.
        """
        headers = parser_2015.get_weeks_headers()

        assert isinstance(headers, tuple)
        assert "leagueId" in headers
        assert "seasonYear" in headers
        assert "weekNumber" in headers
        assert "weekName" in headers
        assert "startDate" in headers
        assert "endDate" in headers

    def test_get_weeks_data_2020(self, parser_2020):
        """Test weeks data extraction with 2020-21 data."""
        data = parser_2020.get_weeks_data()

        assert isinstance(data, list)
        assert len(data) > 0
        # Each row should have leagueId, seasonYear, and week data
        assert data[0][0] == "00"  # leagueId
        assert data[0][1] == "2020-21"  # seasonYear

    def test_get_weeks_data_2015(self, parser_2015):
        """Test weeks data extraction with 2015-16 data (empty weeks)."""
        data = parser_2015.get_weeks_data()

        # Should return empty list since weeks array is empty
        assert isinstance(data, list)
        assert len(data) == 0

    def test_get_games_headers_2020(self, parser_2020):
        """Test games headers extraction with 2020-21 data."""
        headers = parser_2020.get_games_headers()

        assert isinstance(headers, tuple)
        assert "leagueId" in headers
        assert "seasonYear" in headers
        assert "gameDate" in headers
        assert "gameId" in headers
        assert "homeTeam_teamId" in headers
        assert "awayTeam_teamId" in headers

    def test_get_games_headers_2015(self, parser_2015):
        """Test games headers extraction with 2015-16 data."""
        headers = parser_2015.get_games_headers()

        assert isinstance(headers, tuple)
        assert "leagueId" in headers
        assert "seasonYear" in headers
        assert "gameDate" in headers

    def test_get_games_data_2020(self, parser_2020):
        """Test games data extraction with 2020-21 data."""
        data = parser_2020.get_games_data()

        assert isinstance(data, list)
        assert len(data) > 0
        # Each row should have leagueId, seasonYear, gameDate, and game data
        assert data[0][0] == "00"  # leagueId
        assert data[0][1] == "2020-21"  # seasonYear

    def test_get_games_data_2015(self, parser_2015):
        """Test games data extraction with 2015-16 data."""
        data = parser_2015.get_games_data()

        assert isinstance(data, list)
        assert len(data) > 0
        assert data[0][0] == "00"  # leagueId
        assert data[0][1] == "2015-16"  # seasonYear

    def test_get_data_sets_2020(self, parser_2020):
        """Test complete data extraction with 2020-21 data."""
        results = parser_2020.get_data_sets()

        assert "SeasonGames" in results
        assert "SeasonWeeks" in results
        assert results["SeasonGames"] is not None
        assert results["SeasonWeeks"] is not None

    def test_get_data_sets_2015(self, parser_2015):
        """Test complete data extraction with 2015-16 data.

        Should succeed even with empty weeks array by using default headers.
        """
        results = parser_2015.get_data_sets()

        assert "SeasonGames" in results
        assert "SeasonWeeks" in results
        assert results["SeasonGames"] is not None
        assert results["SeasonWeeks"] is not None
        # Weeks data should be empty list
        assert results["SeasonWeeks"]["data"] == []


class TestScheduleLeagueV2Endpoint:
    """Test the ScheduleLeagueV2 endpoint."""

    def test_endpoint_initialization_without_request(self):
        """Test endpoint initializes without making HTTP request."""
        endpoint = ScheduleLeagueV2(season="2020-21", get_request=False)

        assert endpoint.parameters == {"LeagueID": "00", "Season": "2020-21"}
        assert endpoint.endpoint == "scheduleleaguev2"

    def test_expected_data_structure(self):
        """Test that expected_data has all required datasets."""
        expected_datasets = ["SeasonGames", "SeasonWeeks"]

        for dataset in expected_datasets:
            assert dataset in ScheduleLeagueV2.expected_data
            assert isinstance(ScheduleLeagueV2.expected_data[dataset], list)
            assert len(ScheduleLeagueV2.expected_data[dataset]) > 0

    @patch("nba_api.stats.library.http.NBAStatsHTTP.send_api_request")
    def test_endpoint_with_mocked_request_2020(self, mock_request, json_fixture_2020):
        """Test endpoint processes 2020-21 response correctly."""
        # Mock the HTTP response
        mock_response = Mock()
        mock_response.get_dict.return_value = json_fixture_2020

        # Create parser to get actual data
        parser = NBAStatsScheduleLeagueV2Parser(json_fixture_2020)
        mock_response.get_data_sets.return_value = parser.get_data_sets()
        mock_request.return_value = mock_response

        endpoint = ScheduleLeagueV2(season="2020-21")

        # Verify the endpoint was called
        mock_request.assert_called_once()

        # Verify datasets are accessible
        assert hasattr(endpoint, "season_games")
        assert hasattr(endpoint, "season_weeks")
        assert endpoint.season_games is not None
        assert endpoint.season_weeks is not None

    @patch("nba_api.stats.library.http.NBAStatsHTTP.send_api_request")
    def test_endpoint_with_mocked_request_2015(self, mock_request, json_fixture_2015):
        """Test endpoint with 2015-16 response (empty weeks array)."""
        # Mock the HTTP response
        mock_response = Mock()
        mock_response.get_dict.return_value = json_fixture_2015

        # Create parser to get actual data
        parser = NBAStatsScheduleLeagueV2Parser(json_fixture_2015)
        mock_response.get_data_sets.return_value = parser.get_data_sets()
        mock_request.return_value = mock_response

        endpoint = ScheduleLeagueV2(season="2015-16")

        # Verify the endpoint was called
        mock_request.assert_called_once()

        # Verify datasets are accessible
        assert hasattr(endpoint, "season_games")
        assert hasattr(endpoint, "season_weeks")
        assert endpoint.season_games is not None
        assert endpoint.season_weeks is not None

    def test_dataset_attributes_initialized(self):
        """Test that all dataset attributes are initialized in __init__."""
        endpoint = ScheduleLeagueV2(season="2020-21", get_request=False)

        # All dataset attributes should be None before request
        assert endpoint.season_games is None
        assert endpoint.season_weeks is None
