"""Unit tests for PlayerGameLogs endpoint."""

from nba_api.stats.endpoints import PlayerGameLogs
from nba_api.stats.library.parameters import Season


class TestPlayerGameLogsInitialization:
    """Test PlayerGameLogs initialization."""

    def test_endpoint_initialization_without_request(self):
        """Test endpoint initializes without making HTTP request."""
        endpoint = PlayerGameLogs(
            player_id_nullable="2544",
            season_nullable="2023-24",
            get_request=False,
        )

        assert endpoint.parameters["PlayerID"] == "2544"
        assert endpoint.parameters["Season"] == "2023-24"
        assert endpoint.endpoint == "playergamelogs"

    def test_season_defaults_to_current_season(self):
        """The server answers 500 when Season is blank, so it defaults to the
        current season instead."""
        endpoint = PlayerGameLogs(get_request=False)

        assert endpoint.parameters["Season"] == Season.default
