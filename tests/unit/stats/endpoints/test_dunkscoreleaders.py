"""Unit tests for DunkScoreLeaders endpoint."""

import json
from pathlib import Path
from typing import Any, Dict
from unittest.mock import Mock, patch

import pytest

from nba_api.stats.endpoints import DunkScoreLeaders


@pytest.fixture
def json_fixture() -> Dict[str, Any]:
    """Load the DunkScoreLeaders JSON fixture."""
    fixture_path = Path(__file__).parent / "data" / "dunkscoreleaders.json"
    with open(fixture_path, encoding="utf-8") as f:
        return json.load(f)


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

        assert "Dunks" in _EXPECTED_DATA
        assert isinstance(_EXPECTED_DATA["Dunks"], list)
        assert len(_EXPECTED_DATA["Dunks"]) == 55

    def test_expected_data_fields(self):
        """Test that expected_data contains key dunk tracking fields."""
        from nba_api.stats.endpoints._expected_data.dunkscoreleaders import (
            _EXPECTED_DATA,
        )

        dunks_fields = _EXPECTED_DATA["Dunks"]

        # Verify key fields are present
        assert "GAME_ID" in dunks_fields
        assert "PLAYER_NAME" in dunks_fields
        assert "DUNK_SCORE" in dunks_fields
        assert "PLAYER_VERTICAL" in dunks_fields
        assert "HANG_TIME" in dunks_fields
        assert "TAKEOFF_DISTANCE" in dunks_fields
        assert "ALLEY_OOP" in dunks_fields
        assert "VIDEO_AVAILABLE" in dunks_fields

    @patch("nba_api.stats.library.http.NBAStatsHTTP.send_api_request")
    def test_endpoint_with_mocked_request(self, mock_request, json_fixture):
        """Test endpoint processes response correctly."""
        # Mock the HTTP response
        mock_response = Mock()
        mock_response.get_dict.return_value = json_fixture
        mock_response.get_data_sets.return_value = {
            "Dunks": {
                "headers": [
                    "GAME_ID",
                    "PLAYER_NAME",
                    "DUNK_SCORE",
                    "PLAYER_VERTICAL",
                ],
                "data": [
                    ["0022500101", "Onyeka Okongwu", 117.8, 32.338],
                    ["0022500095", "Zion Williamson", 117.5, 33.582],
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

    def test_expected_data_matches_json_structure(self, json_fixture):
        """Test that expected_data field count matches JSON structure."""
        from nba_api.stats.endpoints._expected_data.dunkscoreleaders import (
            _EXPECTED_DATA,
        )

        first_dunk = json_fixture["dunks"][0]
        expected_field_count = len(_EXPECTED_DATA["Dunks"])
        actual_field_count = len(first_dunk.keys())

        assert (
            expected_field_count == actual_field_count
        ), f"Expected {expected_field_count} fields, but found {actual_field_count} in JSON"
