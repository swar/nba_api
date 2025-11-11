"""Unit tests for TeamDashLineups endpoint."""

from typing import Any, Dict
from unittest.mock import Mock, patch

import pytest

from nba_api.stats.endpoints import TeamDashLineups
from .data.teamdashlineups import TEAMDASHLINEUPS_SAMPLE


@pytest.fixture
def json_fixture() -> Dict[str, Any]:
    """Load the TeamDashLineups fixture."""
    return TEAMDASHLINEUPS_SAMPLE


class TestTeamDashLineupsEndpoint:
    """Test the TeamDashLineups endpoint."""

    def test_endpoint_initialization_without_request(self):
        """Test endpoint initializes without making HTTP request."""
        endpoint = TeamDashLineups(
            team_id=1610612739,
            season="2024-25",
            get_request=False
        )

        assert endpoint.parameters["TeamID"] == 1610612739
        assert endpoint.parameters["Season"] == "2024-25"
        assert endpoint.endpoint == "teamdashlineups"

    def test_endpoint_initialization_with_filters(self):
        """Test endpoint initializes with various filter parameters."""
        endpoint = TeamDashLineups(
            team_id=1610612739,
            season="2024-25",
            season_type_all_star="Regular Season",
            group_quantity=5,
            measure_type_detailed_defense="Base",
            per_mode_detailed="Totals",
            date_from_nullable="2024-10-01",
            date_to_nullable="2024-12-31",
            get_request=False,
        )

        assert endpoint.parameters["TeamID"] == 1610612739
        assert endpoint.parameters["Season"] == "2024-25"
        assert endpoint.parameters["SeasonType"] == "Regular Season"
        assert endpoint.parameters["GroupQuantity"] == 5
        assert endpoint.parameters["MeasureType"] == "Base"
        assert endpoint.parameters["PerMode"] == "Totals"
        assert endpoint.parameters["DateFrom"] == "2024-10-01"
        assert endpoint.parameters["DateTo"] == "2024-12-31"

    def test_expected_data_structure(self):
        """Test that expected_data has all required datasets."""
        assert "Lineups" in TeamDashLineups.expected_data
        assert "Overall" in TeamDashLineups.expected_data
        assert isinstance(TeamDashLineups.expected_data["Lineups"], list)
        assert isinstance(TeamDashLineups.expected_data["Overall"], list)

    def test_expected_data_lineups_fields(self):
        """Test that expected_data contains key lineup fields."""
        lineups_fields = TeamDashLineups.expected_data["Lineups"]

        # Verify key fields are present
        assert "GROUP_SET" in lineups_fields
        assert "GROUP_ID" in lineups_fields
        assert "GROUP_NAME" in lineups_fields
        assert "GP" in lineups_fields
        assert "W" in lineups_fields
        assert "L" in lineups_fields
        assert "W_PCT" in lineups_fields
        assert "MIN" in lineups_fields
        assert "FGM" in lineups_fields
        assert "FGA" in lineups_fields
        assert "FG_PCT" in lineups_fields
        assert "PTS" in lineups_fields
        assert "PLUS_MINUS" in lineups_fields

    def test_expected_data_overall_fields(self):
        """Test that expected_data contains key overall fields."""
        overall_fields = TeamDashLineups.expected_data["Overall"]

        # Verify key fields are present
        assert "GROUP_SET" in overall_fields
        assert "GROUP_VALUE" in overall_fields
        assert "TEAM_ID" in overall_fields
        assert "TEAM_ABBREVIATION" in overall_fields
        assert "TEAM_NAME" in overall_fields
        assert "GP" in overall_fields
        assert "W" in overall_fields
        assert "L" in overall_fields
        assert "W_PCT" in overall_fields
        assert "PTS" in overall_fields
        assert "PLUS_MINUS" in overall_fields

    @patch("nba_api.stats.library.http.NBAStatsHTTP.send_api_request")
    def test_endpoint_with_mocked_request(self, mock_request, json_fixture):
        """Test endpoint processes response correctly."""
        # Mock the HTTP response
        mock_response = Mock()
        mock_response.get_dict.return_value = json_fixture
        mock_response.get_data_sets.return_value = {
            "Lineups": {
                "headers": [
                    "GROUP_SET",
                    "GROUP_ID",
                    "GROUP_NAME",
                    "GP",
                    "W",
                    "L",
                    "W_PCT",
                    "MIN",
                    "PTS",
                ],
                "data": [
                    [
                        "5 Man",
                        123456,
                        "Player1 - Player2 - Player3 - Player4 - Player5",
                        10,
                        7,
                        3,
                        0.700,
                        150.5,
                        150,
                    ]
                ],
            },
            "Overall": {
                "headers": [
                    "GROUP_SET",
                    "GROUP_VALUE",
                    "TEAM_ID",
                    "TEAM_ABBREVIATION",
                    "TEAM_NAME",
                    "GP",
                    "W",
                    "L",
                    "W_PCT",
                    "PTS",
                ],
                "data": [
                    [
                        "Overall",
                        "Overall",
                        1610612739,
                        "CLE",
                        "Cleveland Cavaliers",
                        82,
                        50,
                        32,
                        0.610,
                        9200,
                    ]
                ],
            },
        }
        mock_request.return_value = mock_response

        endpoint = TeamDashLineups(team_id=1610612739, season="2024-25")

        # Verify the endpoint was called
        mock_request.assert_called_once()

        # Verify datasets are accessible
        assert hasattr(endpoint, "lineups")
        assert hasattr(endpoint, "overall")
        assert endpoint.lineups is not None
        assert endpoint.overall is not None

    def test_dataset_attributes_initialized(self):
        """Test that all dataset attributes are initialized in __init__."""
        endpoint = TeamDashLineups(
            team_id=1610612739,
            season="2024-25",
            get_request=False
        )

        # Dataset attributes should not exist before request
        # (They're created in load_response, not __init__)
        assert not hasattr(endpoint, "lineups") or endpoint.lineups is None
        assert not hasattr(endpoint, "overall") or endpoint.overall is None

    def test_json_fixture_structure(self, json_fixture):
        """Test that the JSON fixture has expected structure."""
        assert "resource" in json_fixture
        assert "parameters" in json_fixture
        assert "resultSets" in json_fixture

        assert json_fixture["resource"] == "teamdashlineups"
        assert isinstance(json_fixture["resultSets"], list)
        assert len(json_fixture["resultSets"]) == 2

    def test_json_fixture_result_sets(self, json_fixture):
        """Test that JSON fixture has correct result sets."""
        result_sets = json_fixture["resultSets"]

        # Find Lineups and Overall datasets
        lineups_set = next(
            (rs for rs in result_sets if rs["name"] == "Lineups"), None
        )
        overall_set = next(
            (rs for rs in result_sets if rs["name"] == "Overall"), None
        )

        assert lineups_set is not None
        assert overall_set is not None
        assert "headers" in lineups_set
        assert "rowSet" in lineups_set
        assert "headers" in overall_set
        assert "rowSet" in overall_set

    def test_fixture_has_key_fields(self, json_fixture):
        """Test that fixture has key fields for testing.

        Note: This is a minimal fixture. Full API response with all 55+
        fields is available in:
        docs/nba_api/stats/endpoints/responses/teamdashlineups.json
        """
        result_sets = json_fixture["resultSets"]

        lineups_set = next(
            (rs for rs in result_sets if rs["name"] == "Lineups"), None
        )
        overall_set = next(
            (rs for rs in result_sets if rs["name"] == "Overall"), None
        )

        # Verify fixture has minimum required fields for testing
        assert "GROUP_SET" in lineups_set["headers"]
        assert "GROUP_NAME" in lineups_set["headers"]
        assert "GP" in lineups_set["headers"]

        assert "TEAM_ID" in overall_set["headers"]
        assert "TEAM_NAME" in overall_set["headers"]
        assert "W_PCT" in overall_set["headers"]

    def test_required_parameters(self):
        """Test that team_id is required parameter."""
        # This should work - team_id is required
        endpoint = TeamDashLineups(team_id=1610612739, get_request=False)
        assert endpoint.parameters["TeamID"] == 1610612739

    def test_optional_parameters_defaults(self):
        """Test that optional parameters use correct defaults."""
        endpoint = TeamDashLineups(team_id=1610612739, get_request=False)

        # Verify some default values (note: parameter library returns strings)
        assert endpoint.parameters["LastNGames"] == "0"
        assert endpoint.parameters["Month"] == "0"
        assert endpoint.parameters["OpponentTeamID"] == 0
        assert endpoint.parameters["Period"] == "0"
        assert endpoint.parameters["DateFrom"] == ""
        assert endpoint.parameters["DateTo"] == ""
