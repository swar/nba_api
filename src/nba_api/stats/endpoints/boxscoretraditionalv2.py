"""
BoxScoreTraditionalV2 endpoint.

.. deprecated:: 2025-26
    This endpoint is deprecated. Please use BoxScoreTraditionalV3 instead.
    Data is no longer being published for BoxScoreTraditionalV2 as of the 2025-26 NBA season.
"""
import warnings

from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import (
    EndPeriod,
    EndRange,
    RangeType,
    StartPeriod,
    StartRange,
)


class BoxScoreTraditionalV2(Endpoint):
    """
    BoxScoreTraditionalV2 endpoint.

    .. deprecated:: 2025-26
        **DEPRECATION WARNING:** This endpoint is deprecated.
        Please use :class:`~nba_api.stats.endpoints.BoxScoreTraditionalV3` instead.
        Data is no longer being published for BoxScoreTraditionalV2 as of the 2025-26 NBA season.

    Args:
        game_id (str): NBA game ID.
        end_period (int, optional): End period for range.
        end_range (int, optional): End range value.
        range_type (int, optional): Range type parameter.
        start_period (int, optional): Start period for range.
        start_range (int, optional): Start range value.
        proxy (str, optional): HTTP/HTTPS proxy for requests.
        headers (dict, optional): Custom HTTP headers.
        timeout (int, optional): Request timeout in seconds. Defaults to 30.
        get_request (bool, optional): Whether to fetch data immediately. Defaults to True.
    """
    endpoint = "boxscoretraditionalv2"
    expected_data = {
        "PlayerStats": [
            "GAME_ID",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_CITY",
            "PLAYER_ID",
            "PLAYER_NAME",
            "START_POSITION",
            "COMMENT",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "STL",
            "BLK",
            "TO",
            "PF",
            "PTS",
            "PLUS_MINUS",
        ],
        "TeamStarterBenchStats": [
            "GAME_ID",
            "TEAM_ID",
            "TEAM_NAME",
            "TEAM_ABBREVIATION",
            "TEAM_CITY",
            "STARTERS_BENCH",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "STL",
            "BLK",
            "TO",
            "PF",
            "PTS",
        ],
        "TeamStats": [
            "GAME_ID",
            "TEAM_ID",
            "TEAM_NAME",
            "TEAM_ABBREVIATION",
            "TEAM_CITY",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "STL",
            "BLK",
            "TO",
            "PF",
            "PTS",
            "PLUS_MINUS",
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
        end_range=EndRange.default,
        range_type=RangeType.default,
        start_period=StartPeriod.default,
        start_range=StartRange.default,
        proxy=None,
        headers=None,
        timeout=30,
        get_request=True,
    ):
        warnings.warn(
            "BoxScoreTraditionalV2 is deprecated and will be removed in a future version. "
            "Please use BoxScoreTraditionalV3 instead. "
            "Data is no longer being published for BoxScoreTraditionalV2 as of the 2025-26 NBA season.",
            DeprecationWarning,
            stacklevel=2
        )
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
            "GameID": game_id,
            "EndPeriod": end_period,
            "EndRange": end_range,
            "RangeType": range_type,
            "StartPeriod": start_period,
            "StartRange": start_range,
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
        self.player_stats = Endpoint.DataSet(data=data_sets["PlayerStats"])
        self.team_starter_bench_stats = Endpoint.DataSet(
            data=data_sets["TeamStarterBenchStats"]
        )
        self.team_stats = Endpoint.DataSet(data=data_sets["TeamStats"])
