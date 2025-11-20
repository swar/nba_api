"""Unit tests for TeamGameLog endpoint."""

import pytest

from nba_api.stats.endpoints import TeamGameLog


class TestTeamGameLogInitialization:
    """Test TeamGameLog initialization."""

    def test_endpoint_initialization_without_request(self):
        """Test endpoint initializes without making HTTP request."""
        endpoint = TeamGameLog(
            team_id='1610612747',
            season='2023-24',
            season_type_all_star='Regular Season',
            get_request=False
        )

        assert endpoint.parameters["TeamID"] == '1610612747'
        assert endpoint.parameters["Season"] == '2023-24'
        assert endpoint.parameters["SeasonType"] == 'Regular Season'
        assert endpoint.endpoint == "teamgamelog"

    def test_required_parameter_team_id(self):
        """Test that team_id is required."""
        with pytest.raises(TypeError):
            TeamGameLog(get_request=False)

    def test_optional_date_parameters(self):
        """Test date filtering parameters."""
        endpoint = TeamGameLog(
            team_id='1610612747',
            date_from_nullable='01/01/2024',
            date_to_nullable='01/31/2024',
            get_request=False
        )

        assert endpoint.parameters["DateFrom"] == '01/01/2024'
        assert endpoint.parameters["DateTo"] == '01/31/2024'

    def test_dataset_attributes_initialized(self):
        """Test that dataset attributes are initialized in __init__."""
        endpoint = TeamGameLog(
            team_id='1610612747',
            get_request=False
        )

        # Dataset attribute should be None before request
        assert endpoint.team_game_log is None

    def test_expected_data_structure(self):
        """Test that expected_data has required fields."""
        assert "TeamGameLog" in TeamGameLog.expected_data
        expected_fields = TeamGameLog.expected_data["TeamGameLog"]

        # Check for key fields
        assert "Team_ID" in expected_fields
        assert "Game_ID" in expected_fields
        assert "GAME_DATE" in expected_fields
        assert "MATCHUP" in expected_fields
        assert "WL" in expected_fields
        assert "PTS" in expected_fields
