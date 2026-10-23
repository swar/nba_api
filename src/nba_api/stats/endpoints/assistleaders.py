"""
AssistLeaders endpoint.

.. deprecated:: 2026-27
    This endpoint is deprecated. Please use LeagueDashPlayerStats or LeagueDashTeamStats for assist totals instead.
    The NBA API no longer returns data for AssistLeaders (it returns the NBA.com homepage instead).
"""

import warnings

from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import (
    LeagueID,
    PerModeSimple,
    PlayerOrTeam,
    Season,
    SeasonType,
)


class AssistLeaders(Endpoint):
    """
    AssistLeaders endpoint.

    .. deprecated:: 2026-27
        **DEPRECATION WARNING:** This endpoint is deprecated.
        Please use :class:`~nba_api.stats.endpoints.LeagueDashPlayerStats` or :class:`~nba_api.stats.endpoints.LeagueDashTeamStats` for assist totals instead.
        The NBA API no longer returns data for AssistLeaders (it returns the NBA.com homepage instead).
    """

    endpoint = "assistleaders"
    expected_data = {
        "AssistLeaders": ["RANK", "TEAM_ID", "TEAM_ABBREVIATION", "TEAM_NAME", "AST"]
    }

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(
        self,
        league_id=LeagueID.default,
        per_mode_simple=PerModeSimple.default,
        player_or_team=PlayerOrTeam.default,
        season=Season.default,
        season_type_playoffs=SeasonType.default,
        proxy=None,
        headers=None,
        timeout=30,
        get_request=True,
    ):
        warnings.warn(
            "AssistLeaders is deprecated and will be removed in a future version. "
            "Please use LeagueDashPlayerStats or LeagueDashTeamStats for assist totals instead. "
            "The NBA API no longer returns data for AssistLeaders (it returns the NBA.com homepage instead).",
            DeprecationWarning,
            stacklevel=2,
        )
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
            "LeagueID": league_id,
            "PerMode": per_mode_simple,
            "PlayerOrTeam": player_or_team,
            "Season": season,
            "SeasonType": season_type_playoffs,
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
        self.assist_leaders = Endpoint.DataSet(data=data_sets["AssistLeaders"])
