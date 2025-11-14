"""Unit tests for TeamGameLogs endpoint."""

import pytest

from nba_api.stats.endpoints import TeamGameLogs


class TestTeamGameLogsInitialization:
    """Test TeamGameLogs initialization."""

    def test_endpoint_initialization_without_request(self):
        """Test endpoint initializes without making HTTP request."""
        endpoint = TeamGameLogs(
            team_id_nullable='1610612747',
            season_nullable='2023-24',
            season_type_nullable='Regular Season',
            get_request=False
        )

        assert endpoint.parameters["TeamID"] == '1610612747'
        assert endpoint.parameters["Season"] == '2023-24'
        assert endpoint.parameters["SeasonType"] == 'Regular Season'
        assert endpoint.endpoint == "teamgamelogs"

    def test_no_required_parameters(self):
        """Test that endpoint can be initialized with no parameters."""
        # Should not raise - all parameters are optional
        endpoint = TeamGameLogs(get_request=False)
        assert endpoint.endpoint == "teamgamelogs"

    def test_multiple_filter_parameters(self):
        """Test various filtering parameters."""
        endpoint = TeamGameLogs(
            team_id_nullable='1610612747',
            season_nullable='2023-24',
            location_nullable='Home',
            outcome_nullable='W',
            last_n_games_nullable='10',
            get_request=False
        )

        assert endpoint.parameters["TeamID"] == '1610612747'
        assert endpoint.parameters["Location"] == 'Home'
        assert endpoint.parameters["Outcome"] == 'W'
        assert endpoint.parameters["LastNGames"] == '10'

    def test_conference_and_division_filters(self):
        """Test conference and division filtering parameters."""
        endpoint = TeamGameLogs(
            vs_conference_nullable='East',
            vs_division_nullable='Atlantic',
            get_request=False
        )

        assert endpoint.parameters["VsConference"] == 'East'
        assert endpoint.parameters["VsDivision"] == 'Atlantic'

    def test_dataset_attributes_initialized(self):
        """Test that dataset attributes are initialized in __init__."""
        endpoint = TeamGameLogs(get_request=False)

        # Dataset attribute should be None before request
        assert endpoint.team_game_logs is None

    def test_expected_data_structure(self):
        """Test that expected_data has required fields including rank fields."""
        assert "TeamGameLogs" in TeamGameLogs.expected_data
        expected_fields = TeamGameLogs.expected_data["TeamGameLogs"]

        # Check for key fields
        assert "TEAM_ID" in expected_fields
        assert "TEAM_NAME" in expected_fields
        assert "GAME_ID" in expected_fields
        assert "GAME_DATE" in expected_fields
        assert "MATCHUP" in expected_fields
        assert "WL" in expected_fields
        assert "PTS" in expected_fields

        # Check for rank fields (unique to TeamGameLogs)
        assert "PTS_RANK" in expected_fields
        assert "AST_RANK" in expected_fields
        assert "REB_RANK" in expected_fields

    def test_measure_type_parameter(self):
        """Test measure type parameter."""
        endpoint = TeamGameLogs(
            measure_type_player_game_logs_nullable='Advanced',
            get_request=False
        )

        assert endpoint.parameters["MeasureType"] == 'Advanced'
