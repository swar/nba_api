"""
PlayByPlay endpoint.

.. deprecated:: 2026-27
    This endpoint is deprecated. Please use PlayByPlayV3 instead.
    The NBA API no longer returns data for PlayByPlay (returns empty JSON).
"""

import warnings

from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import EndPeriod, StartPeriod


class PlayByPlay(Endpoint):
    """
    PlayByPlay endpoint.

    .. deprecated:: 2026-27
        **DEPRECATION WARNING:** This endpoint is deprecated.
        Please use :class:`~nba_api.stats.endpoints.PlayByPlayV3` instead.
        The NBA API no longer returns data for PlayByPlay (returns empty JSON).
    """

    endpoint = "playbyplay"
    expected_data = {
        "AvailableVideo": ["VIDEO_AVAILABLE_FLAG"],
        "PlayByPlay": [
            "GAME_ID",
            "EVENTNUM",
            "EVENTMSGTYPE",
            "EVENTMSGACTIONTYPE",
            "PERIOD",
            "WCTIMESTRING",
            "PCTIMESTRING",
            "HOMEDESCRIPTION",
            "NEUTRALDESCRIPTION",
            "VISITORDESCRIPTION",
            "SCORE",
            "SCOREMARGIN",
        ],
    }

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(
        self,
        game_id,
        end_period=EndPeriod.default,
        start_period=StartPeriod.default,
        proxy=None,
        headers=None,
        timeout=30,
        get_request=True,
    ):
        warnings.warn(
            "PlayByPlay is deprecated and will be removed in a future version. "
            "Please use PlayByPlayV3 instead. "
            "The NBA API no longer returns data for PlayByPlay (returns empty JSON).",
            DeprecationWarning,
            stacklevel=2,
        )
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
            "GameID": game_id,
            "EndPeriod": end_period,
            "StartPeriod": start_period,
        }
        if get_request:
            self.get_request()

    def get_request(self):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters=self.parameters,
            proxy=self.proxy,
            headers=self.headers,
            timeout=self.timeout,
        )
        self.load_response()

    def load_response(self):
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [
            Endpoint.DataSet(data=data_set)
            for data_set_name, data_set in data_sets.items()
        ]
        self.available_video = Endpoint.DataSet(data=data_sets["AvailableVideo"])
        self.play_by_play = Endpoint.DataSet(data=data_sets["PlayByPlay"])
