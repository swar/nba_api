"""Unit tests for GravityLeaders endpoint."""

from typing import Any, Dict
from unittest.mock import Mock, patch

import pytest

from nba_api.stats.endpoints import GravityLeaders
from .data.gravityleaders import GRAVITYLEADERS_SAMPLE


@pytest.fixture
def json_fixture() -> Dict[str, Any]:
    """Load the GravityLeaders fixture."""
    return GRAVITYLEADERS_SAMPLE


class TestGravityLeadersEndpoint:
    """Test the GravityLeaders endpoint."""

    def test_endpoint_initialization_without_request(self):
        """Test endpoint initializes without making HTTP request."""
        endpoint = GravityLeaders(season="2024-25", get_request=False)

        assert endpoint.parameters["Season"] == "2024-25"
        assert endpoint.endpoint == "gravityleaders"

    def test_endpoint_initialization_with_filters(self):
        """Test endpoint initializes with various filter parameters."""
        endpoint = GravityLeaders(
            league_id="00",
            season="2023-24",
            season_type_all_star="Playoffs",
            get_request=False,
        )

        assert endpoint.parameters["LeagueID"] == "00"
        assert endpoint.parameters["Season"] == "2023-24"
        assert endpoint.parameters["SeasonType"] == "Playoffs"

    def test_expected_data_structure(self):
        """Test that expected_data has all required datasets."""
        assert "leaders" in GravityLeaders.expected_data
        assert isinstance(GravityLeaders.expected_data["leaders"], list)
        assert len(GravityLeaders.expected_data["leaders"]) == 27

    def test_expected_data_fields(self):
        """Test that expected_data contains key gravity tracking fields."""
        leaders_fields = GravityLeaders.expected_data["leaders"]

        # Verify key player identification fields
        assert "PLAYERID" in leaders_fields
        assert "FIRSTNAME" in leaders_fields
        assert "LASTNAME" in leaders_fields
        assert "TEAMID" in leaders_fields
        assert "TEAMABBREVIATION" in leaders_fields

        # Verify gravity score fields
        assert "FRAMES" in leaders_fields
        assert "GRAVITYSCORE" in leaders_fields
        assert "AVGGRAVITYSCORE" in leaders_fields

        # Verify on-ball perimeter fields
        assert "ONBALLPERIMETERFRAMES" in leaders_fields
        assert "ONBALLPERIMETERGRAVITYSCORE" in leaders_fields
        assert "AVGONBALLPERIMETERGRAVITYSCORE" in leaders_fields

        # Verify off-ball perimeter fields
        assert "OFFBALLPERIMETERFRAMES" in leaders_fields
        assert "OFFBALLPERIMETERGRAVITYSCORE" in leaders_fields
        assert "AVGOFFBALLPERIMETERGRAVITYSCORE" in leaders_fields

        # Verify on-ball interior fields
        assert "ONBALLINTERIORFRAMES" in leaders_fields
        assert "ONBALLINTERIORGRAVITYSCORE" in leaders_fields
        assert "AVGONBALLINTERIORGRAVITYSCORE" in leaders_fields

        # Verify off-ball interior fields
        assert "OFFBALLINTERIORFRAMES" in leaders_fields
        assert "OFFBALLINTERIORGRAVITYSCORE" in leaders_fields
        assert "AVGOFFBALLINTERIORGRAVITYSCORE" in leaders_fields

        # Verify standard stats
        assert "GAMESPLAYED" in leaders_fields
        assert "MINUTES" in leaders_fields
        assert "PTS" in leaders_fields
        assert "REB" in leaders_fields
        assert "AST" in leaders_fields

    @patch("nba_api.stats.library.http.NBAStatsHTTP.send_api_request")
    def test_endpoint_with_mocked_request(self, mock_request, json_fixture):
        """Test endpoint processes response correctly."""
        # Mock the HTTP response
        mock_response = Mock()
        mock_response.get_dict.return_value = json_fixture
        mock_response.get_data_sets.return_value = {
            "leaders": {
                "headers": [
                    "PLAYERID",
                    "FIRSTNAME",
                    "LASTNAME",
                    "TEAMID",
                    "TEAMABBREVIATION",
                    "GRAVITYSCORE",
                    "AVGGRAVITYSCORE",
                ],
                "data": [
                    [201939, "Stephen", "Curry", 1610612744, "GSW", 20.8209629629, 20.3848295],
                    [201142, "Kevin", "Durant", 1610612745, "HOU", 16.9147741935, 17.1987082],
                ],
            },
        }
        mock_request.return_value = mock_response

        endpoint = GravityLeaders(season="2024-25")

        # Verify the endpoint was called
        mock_request.assert_called_once()

        # Verify datasets are accessible
        assert hasattr(endpoint, "league_leaders")
        assert endpoint.league_leaders is not None

    def test_dataset_attributes_initialized(self):
        """Test that all dataset attributes are initialized in __init__."""
        endpoint = GravityLeaders(season="2024-25", get_request=False)

        # All dataset attributes should be None before request
        assert endpoint.league_leaders is None

    def test_json_fixture_structure(self, json_fixture):
        """Test that the JSON fixture has expected structure."""
        assert "params" in json_fixture
        assert "leaders" in json_fixture

        params = json_fixture["params"]
        assert "leagueId" in params
        assert "seasonYear" in params
        assert "seasonType" in params

        leaders = json_fixture["leaders"]
        assert isinstance(leaders, list)
        assert len(leaders) > 0

    def test_json_fixture_leader_fields(self, json_fixture):
        """Test that leader records have expected fields."""
        first_leader = json_fixture["leaders"][0]

        # Verify player identification fields
        assert "PLAYERID" in first_leader
        assert "FIRSTNAME" in first_leader
        assert "LASTNAME" in first_leader
        assert "TEAMID" in first_leader
        assert "TEAMABBREVIATION" in first_leader

        # Verify gravity tracking fields
        assert "FRAMES" in first_leader
        assert "GRAVITYSCORE" in first_leader
        assert "AVGGRAVITYSCORE" in first_leader
        assert "ONBALLPERIMETERFRAMES" in first_leader
        assert "ONBALLPERIMETERGRAVITYSCORE" in first_leader
        assert "AVGONBALLPERIMETERGRAVITYSCORE" in first_leader
        assert "OFFBALLPERIMETERFRAMES" in first_leader
        assert "OFFBALLPERIMETERGRAVITYSCORE" in first_leader
        assert "AVGOFFBALLPERIMETERGRAVITYSCORE" in first_leader

        # Verify standard stats
        assert "GAMESPLAYED" in first_leader
        assert "MINUTES" in first_leader
        assert "PTS" in first_leader
        assert "REB" in first_leader
        assert "AST" in first_leader

    def test_fixture_has_multiple_players(self, json_fixture):
        """Test that fixture contains multiple player records for testing."""
        leaders = json_fixture["leaders"]
        assert len(leaders) >= 2

        # Verify different players
        player_ids = [leader["PLAYERID"] for leader in leaders]
        assert len(player_ids) == len(set(player_ids))  # All unique

    def test_fixture_gravity_score_values(self, json_fixture):
        """Test that gravity scores are realistic numeric values."""
        first_leader = json_fixture["leaders"][0]

        # Gravity scores should be numeric (can be positive or negative)
        assert isinstance(first_leader["GRAVITYSCORE"], (int, float))
        assert isinstance(first_leader["AVGGRAVITYSCORE"], (int, float))
        assert isinstance(first_leader["ONBALLPERIMETERGRAVITYSCORE"], (int, float))
        assert isinstance(first_leader["AVGONBALLPERIMETERGRAVITYSCORE"], (int, float))
