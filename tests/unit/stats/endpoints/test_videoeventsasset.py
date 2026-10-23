"""Unit tests for VideoEventsAsset endpoint."""

import pytest

from nba_api.stats.endpoints import VideoEventsAsset


class TestVideoEventsAssetInitialization:
    """Test VideoEventsAsset initialization."""

    def test_endpoint_initialization_without_request(self):
        """Test endpoint initializes without making HTTP request."""
        endpoint = VideoEventsAsset(
            game_id="0022300001", game_event_id=7, get_request=False
        )

        assert endpoint.parameters == {"GameID": "0022300001", "GameEventID": 7}
        assert endpoint.endpoint == "videoeventsasset"

    def test_game_event_id_defaults_to_zero(self):
        """Test game_event_id is optional."""
        endpoint = VideoEventsAsset(game_id="0022300001", get_request=False)

        assert endpoint.parameters["GameEventID"] == 0

    def test_required_parameter_game_id(self):
        """Test that game_id is required."""
        with pytest.raises(TypeError):
            VideoEventsAsset(get_request=False)
