"""Unit tests for CommonTeamRoster endpoint."""

import pytest
from unittest.mock import Mock, patch

from nba_api.stats.endpoints import CommonTeamRoster


class TestCommonTeamRosterEndpoint:
    """Test the CommonTeamRoster endpoint."""

    def test_endpoint_initialization_without_request(self):
        """Test endpoint initializes without making HTTP request."""
        endpoint = CommonTeamRoster(team_id="1610612739", get_request=False)

        assert endpoint.parameters["TeamID"] == "1610612739"
        assert endpoint.endpoint == "commonteamroster"

    @patch("nba_api.stats.library.http.NBAStatsHTTP.send_api_request")
    def test_endpoint_with_both_datasets(self, mock_request):
        """Test endpoint processes response with both Coaches and CommonTeamRoster."""
        # Mock response with both datasets present
        mock_response = Mock()
        mock_response.get_data_sets.return_value = {
            "Coaches": {
                "headers": ["TEAM_ID", "SEASON", "COACH_ID", "FIRST_NAME", "LAST_NAME"],
                "data": [
                    ["1610612739", "2024-25", "123", "John", "Doe"],
                ],
            },
            "CommonTeamRoster": {
                "headers": ["TeamID", "SEASON", "PLAYER", "PLAYER_ID"],
                "data": [
                    ["1610612739", "2024-25", "Player One", "203999"],
                ],
            },
        }
        mock_request.return_value = mock_response

        endpoint = CommonTeamRoster(team_id="1610612739")

        # Verify both datasets are accessible
        assert hasattr(endpoint, "coaches")
        assert hasattr(endpoint, "common_team_roster")
        assert endpoint.coaches is not None
        assert endpoint.common_team_roster is not None

    @patch("nba_api.stats.library.http.NBAStatsHTTP.send_api_request")
    def test_endpoint_with_missing_coaches_dataset(self, mock_request):
        """Test endpoint handles missing Coaches dataset gracefully (#553)."""
        # Mock response with only CommonTeamRoster (no Coaches)
        mock_response = Mock()
        mock_response.get_data_sets.return_value = {
            "CommonTeamRoster": {
                "headers": ["TeamID", "SEASON", "PLAYER", "PLAYER_ID"],
                "data": [
                    ["1610612739", "2024-25", "Player One", "203999"],
                ],
            },
        }
        mock_request.return_value = mock_response

        # Should not raise KeyError
        endpoint = CommonTeamRoster(team_id="1610612739")

        # Verify coaches dataset exists but is empty
        assert hasattr(endpoint, "coaches")
        assert endpoint.coaches is not None
        coaches_df = endpoint.coaches.get_data_frame()
        assert len(coaches_df) == 0
        # Verify it has the expected columns
        assert list(coaches_df.columns) == [
            "TEAM_ID",
            "SEASON",
            "COACH_ID",
            "FIRST_NAME",
            "LAST_NAME",
            "COACH_NAME",
            "IS_ASSISTANT",
            "COACH_TYPE",
            "SORT_SEQUENCE",
        ]

        # Verify common_team_roster still works
        assert hasattr(endpoint, "common_team_roster")
        roster_df = endpoint.common_team_roster.get_data_frame()
        assert len(roster_df) == 1

    def test_expected_data_structure(self):
        """Test that expected_data has both required datasets."""
        assert "Coaches" in CommonTeamRoster.expected_data
        assert "CommonTeamRoster" in CommonTeamRoster.expected_data
        assert isinstance(CommonTeamRoster.expected_data["Coaches"], list)
        assert isinstance(CommonTeamRoster.expected_data["CommonTeamRoster"], list)
