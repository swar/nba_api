from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import (
    EndPeriod,
    EndRange,
    RangeType,
    StartPeriod,
    StartRange,
)


class BoxScoreMiscV2(Endpoint):
    endpoint = "boxscoremiscv2"
    expected_data = {
        "sqlPlayersMisc": [
            "GAME_ID",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_CITY",
            "PLAYER_ID",
            "PLAYER_NAME",
            "START_POSITION",
            "COMMENT",
            "MIN",
            "PTS_OFF_TOV",
            "PTS_2ND_CHANCE",
            "PTS_FB",
            "PTS_PAINT",
            "OPP_PTS_OFF_TOV",
            "OPP_PTS_2ND_CHANCE",
            "OPP_PTS_FB",
            "OPP_PTS_PAINT",
            "BLK",
            "BLKA",
            "PF",
            "PFD",
        ],
        "sqlTeamsMisc": [
            "GAME_ID",
            "TEAM_ID",
            "TEAM_NAME",
            "TEAM_ABBREVIATION",
            "TEAM_CITY",
            "MIN",
            "PTS_OFF_TOV",
            "PTS_2ND_CHANCE",
            "PTS_FB",
            "PTS_PAINT",
            "OPP_PTS_OFF_TOV",
            "OPP_PTS_2ND_CHANCE",
            "OPP_PTS_FB",
            "OPP_PTS_PAINT",
            "BLK",
            "BLKA",
            "PF",
            "PFD",
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
        self.sql_players_misc = Endpoint.DataSet(data=data_sets["sqlPlayersMisc"])
        self.sql_teams_misc = Endpoint.DataSet(data=data_sets["sqlTeamsMisc"])
