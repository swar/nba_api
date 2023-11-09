from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import (
    LeagueID,
    SeasonNullable,
    SeasonTypeNullable,
)


class TeamInfoCommon(Endpoint):
    endpoint = "teaminfocommon"
    expected_data = {
        "AvailableSeasons": ["SEASON_ID"],
        "TeamInfoCommon": [
            "TEAM_ID",
            "SEASON_YEAR",
            "TEAM_CITY",
            "TEAM_NAME",
            "TEAM_ABBREVIATION",
            "TEAM_CONFERENCE",
            "TEAM_DIVISION",
            "TEAM_CODE",
            "W",
            "L",
            "PCT",
            "CONF_RANK",
            "DIV_RANK",
            "MIN_YEAR",
            "MAX_YEAR",
        ],
        "TeamSeasonRanks": [
            "LEAGUE_ID",
            "SEASON_ID",
            "TEAM_ID",
            "PTS_RANK",
            "PTS_PG",
            "REB_RANK",
            "REB_PG",
            "AST_RANK",
            "AST_PG",
            "OPP_PTS_RANK",
            "OPP_PTS_PG",
        ],
    }

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(
        self,
        team_id,
        league_id=LeagueID.default,
        season_nullable=SeasonNullable.default,
        season_type_nullable=SeasonTypeNullable.default,
        proxy=None,
        headers=None,
        timeout=30,
        get_request=True,
    ):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
            "TeamID": team_id,
            "LeagueID": league_id,
            "Season": season_nullable,
            "SeasonType": season_type_nullable,
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
        self.available_seasons = Endpoint.DataSet(data=data_sets["AvailableSeasons"])
        self.team_info_common = Endpoint.DataSet(data=data_sets["TeamInfoCommon"])
        self.team_season_ranks = Endpoint.DataSet(data=data_sets["TeamSeasonRanks"])
