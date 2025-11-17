"""Unit tests for DunkScoreLeaders endpoint."""

from typing import Any, Dict
from unittest.mock import Mock, patch

import pytest

from nba_api.stats.endpoints import DunkScoreLeaders

from .data.dunkscoreleaders import DUNKSCORELEADERS_SAMPLE


@pytest.fixture
def json_fixture() -> Dict[str, Any]:
    """Load the DunkScoreLeaders fixture."""
    return DUNKSCORELEADERS_SAMPLE


class TestDunkScoreLeadersEndpoint:
    """Test the DunkScoreLeaders endpoint."""

    def test_endpoint_initialization_without_request(self):
        """Test endpoint initializes without making HTTP request."""
        endpoint = DunkScoreLeaders(season="2024-25", get_request=False)

        assert endpoint.parameters["Season"] == "2024-25"
        assert endpoint.endpoint == "dunkscoreleaders"

    def test_endpoint_initialization_with_filters(self):
        """Test endpoint initializes with various filter parameters."""
        endpoint = DunkScoreLeaders(
            season="2024-25",
            player_id_nullable="1630168",
            team_id_nullable="1610612737",
            game_id_nullable="0022500101",
            get_request=False,
        )

        assert endpoint.parameters["Season"] == "2024-25"
        assert endpoint.parameters["PlayerID"] == "1630168"
        assert endpoint.parameters["TeamID"] == "1610612737"
        assert endpoint.parameters["GameID"] == "0022500101"

    def test_expected_data_structure(self):
        """Test that expected_data has all required datasets."""
        from nba_api.stats.endpoints._expected_data.dunkscoreleaders import (
            _EXPECTED_DATA,
        )

        assert "dunks" in _EXPECTED_DATA
        assert isinstance(_EXPECTED_DATA["dunks"], list)
        assert len(_EXPECTED_DATA["dunks"]) == 55

    def test_expected_data_fields(self):
        """Test that expected_data contains key dunk tracking fields."""
        from nba_api.stats.endpoints._expected_data.dunkscoreleaders import (
            _EXPECTED_DATA,
        )

        dunks_fields = _EXPECTED_DATA["dunks"]

        # Verify key fields are present
        assert "gameId" in dunks_fields
        assert "gameDate" in dunks_fields
        assert "matchup" in dunks_fields
        assert "period" in dunks_fields
        assert "gameClockTime" in dunks_fields
        assert "eventNum" in dunks_fields
        assert "playerId" in dunks_fields
        assert "playerName" in dunks_fields
        assert "firstName" in dunks_fields
        assert "lastName" in dunks_fields
        assert "teamId" in dunks_fields
        assert "teamName" in dunks_fields
        assert "teamCity" in dunks_fields
        assert "teamAbbreviation" in dunks_fields
        assert "dunkScore" in dunks_fields
        assert "jumpSubscore" in dunks_fields
        assert "powerSubscore" in dunks_fields
        assert "styleSubscore" in dunks_fields
        assert "defensiveContestSubscore" in dunks_fields
        assert "maxBallHeight" in dunks_fields
        assert "ballSpeedThroughRim" in dunks_fields
        assert "playerVertical" in dunks_fields
        assert "hangTime" in dunks_fields
        assert "takeoffDistance" in dunks_fields
        assert "reverseDunk" in dunks_fields
        assert "dunk360" in dunks_fields
        assert "throughTheLegs" in dunks_fields
        assert "alleyOop" in dunks_fields
        assert "tipIn" in dunks_fields
        assert "selfOop" in dunks_fields
        assert "playerRotation" in dunks_fields
        assert "playerLateralSpeed" in dunks_fields
        assert "ballDistanceTraveled" in dunks_fields
        assert "ballReachBack" in dunks_fields
        assert "totalBallAcceleration" in dunks_fields
        assert "dunkingHand" in dunks_fields
        assert "jumpingFoot" in dunks_fields
        assert "passLength" in dunks_fields
        assert "catchingHand" in dunks_fields
        assert "catchDistance" in dunks_fields
        assert "lateralCatchDistance" in dunks_fields
        assert "passerId" in dunks_fields
        assert "passerName" in dunks_fields
        assert "passerFirstName" in dunks_fields
        assert "passerLastName" in dunks_fields
        assert "passReleasePoint" in dunks_fields
        assert "shooterId" in dunks_fields
        assert "shooterName" in dunks_fields
        assert "shooterFirstName" in dunks_fields
        assert "shooterLastName" in dunks_fields
        assert "shotReleasePoint" in dunks_fields
        assert "shotLength" in dunks_fields
        assert "defensiveContestLevel" in dunks_fields
        assert "possibleAttemptedCharge" in dunks_fields
        assert "videoAvailable" in dunks_fields

    @patch("nba_api.stats.library.http.NBAStatsHTTP.send_api_request")
    def test_endpoint_with_mocked_request(self, mock_request, json_fixture):
        """Test endpoint processes response correctly."""
        # Mock the HTTP response
        mock_response = Mock()
        mock_response.get_dict.return_value = json_fixture
        mock_response.get_data_sets.return_value = {
            "DunkScoreLeaders": {
                "headers": [
                    "gameId",
                    "gameDate",
                    "matchup",
                    "period",
                    "gameClockTime",
                    "eventNum",
                    "playerId",
                    "playerName",
                    "firstName",
                    "lastName",
                    "teamId",
                    "teamName",
                    "teamCity",
                    "teamAbbreviation",
                    "dunkScore",
                    "jumpSubscore",
                    "powerSubscore",
                    "styleSubscore",
                    "defensiveContestSubscore",
                    "maxBallHeight",
                    "ballSpeedThroughRim",
                    "playerVertical",
                    "hangTime",
                    "takeoffDistance",
                    "reverseDunk",
                    "dunk360",
                    "throughTheLegs",
                    "alleyOop",
                    "tipIn",
                    "selfOop",
                    "playerRotation",
                    "playerLateralSpeed",
                    "ballDistanceTraveled",
                    "ballReachBack",
                    "totalBallAcceleration",
                    "dunkingHand",
                    "jumpingFoot",
                    "passLength",
                    "catchingHand",
                    "catchDistance",
                    "lateralCatchDistance",
                    "passerId",
                    "passerName",
                    "passerFirstName",
                    "passerLastName",
                    "passReleasePoint",
                    "shooterId",
                    "shooterName",
                    "shooterFirstName",
                    "shooterLastName",
                    "shotReleasePoint",
                    "shotLength",
                    "defensiveContestLevel",
                    "possibleAttemptedCharge",
                    "videoAvailable",
                ],
                "data": [
                    [
                        "0022500101",
                        "10/25/2025 12:00:00 AM",
                        "OKC @ ATL",
                        1,
                        "11:06",
                        13,
                        1630168,
                        "Onyeka Okongwu",
                        "Onyeka",
                        "Okongwu",
                        1610612737,
                        "Hawks",
                        "Atlanta",
                        "ATL",
                        117.8,
                        82.6,
                        96.8,
                        69.1,
                        87.3,
                        10.9,
                        28.772,
                        32.338,
                        0.483,
                        6.494,
                        False,
                        False,
                        False,
                        False,
                        False,
                        False,
                        33.819,
                        4.321,
                        2.13,
                        1.072,
                        1.335,
                        "right",
                        "both",
                        0.0,
                        "",
                        0.0,
                        0.0,
                        0,
                        "",
                        "",
                        "",
                        "",
                        0,
                        "",
                        "",
                        "",
                        "",
                        0.0,
                        73.816,
                        False,
                        True,
                    ],
                    [
                        "0022500090",
                        "10/24/2025 12:00:00 AM",
                        "ATL @ ORL",
                        3,
                        "10:42",
                        408,
                        1630168,
                        "Onyeka Okongwu",
                        "Onyeka",
                        "Okongwu",
                        1610612737,
                        "Hawks",
                        "Atlanta",
                        "ATL",
                        63.1,
                        53.4,
                        42.9,
                        27.5,
                        49.8,
                        10.659,
                        22.009,
                        26.741,
                        0.416,
                        4.94,
                        False,
                        False,
                        False,
                        False,
                        False,
                        False,
                        33.881,
                        4.536,
                        1.814,
                        0.0,
                        0.556,
                        "both",
                        "both",
                        0.0,
                        "",
                        0.0,
                        0.0,
                        0,
                        "",
                        "",
                        "",
                        "",
                        0,
                        "",
                        "",
                        "",
                        "",
                        0.0,
                        53.863,
                        False,
                        True,
                    ],
                ],
            },
        }
        mock_request.return_value = mock_response

        endpoint = DunkScoreLeaders(season="2024-25")

        # Verify the endpoint was called
        mock_request.assert_called_once()

        # Verify datasets are accessible
        assert hasattr(endpoint, "dunks")
        assert endpoint.dunks is not None

    def test_dataset_attributes_initialized(self):
        """Test that all dataset attributes are initialized in __init__."""
        endpoint = DunkScoreLeaders(season="2024-25", get_request=False)

        # All dataset attributes should be None before request
        assert endpoint.dunks is None

    def test_json_fixture_structure(self, json_fixture):
        """Test that the JSON fixture has expected structure."""
        assert "params" in json_fixture
        assert "dunks" in json_fixture

        params = json_fixture["params"]
        assert "leagueId" in params
        assert "seasonType" in params
        assert "seasonYear" in params

        dunks = json_fixture["dunks"]
        assert isinstance(dunks, list)
        assert len(dunks) > 0

    def test_json_fixture_dunk_fields(self, json_fixture):
        """Test that dunk records have expected fields."""
        first_dunk = json_fixture["dunks"][0]

        # Verify key fields
        assert "gameId" in first_dunk
        assert "playerName" in first_dunk
        assert "dunkScore" in first_dunk
        assert "playerVertical" in first_dunk
        assert "hangTime" in first_dunk
        assert "takeoffDistance" in first_dunk
        assert "alleyOop" in first_dunk
        assert "videoAvailable" in first_dunk

    def test_fixture_has_key_fields(self, json_fixture):
        """Test that fixture has key fields for testing.

        Note: This is a minimal fixture with essential fields only.
        Full API response with all 55 fields is available in:
        docs/nba_api/stats/endpoints/responses/dunkscoreleaders.json
        """
        first_dunk = json_fixture["dunks"][0]

        # Verify fixture has minimum required fields for testing
        assert "gameId" in first_dunk
        assert "playerName" in first_dunk
        assert "dunkScore" in first_dunk
        assert "playerVertical" in first_dunk
        assert "hangTime" in first_dunk
        assert "videoAvailable" in first_dunk
