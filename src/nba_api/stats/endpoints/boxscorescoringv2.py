from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import (
    EndPeriod,
    EndRange,
    RangeType,
    StartPeriod,
    StartRange,
)


class BoxScoreScoringV2(Endpoint):
    endpoint = "boxscorescoringv2"
    expected_data = {
        "sqlPlayersScoring": [
            "GAME_ID",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_CITY",
            "PLAYER_ID",
            "PLAYER_NAME",
            "START_POSITION",
            "COMMENT",
            "MIN",
            "PCT_FGA_2PT",
            "PCT_FGA_3PT",
            "PCT_PTS_2PT",
            "PCT_PTS_2PT_MR",
            "PCT_PTS_3PT",
            "PCT_PTS_FB",
            "PCT_PTS_FT",
            "PCT_PTS_OFF_TOV",
            "PCT_PTS_PAINT",
            "PCT_AST_2PM",
            "PCT_UAST_2PM",
            "PCT_AST_3PM",
            "PCT_UAST_3PM",
            "PCT_AST_FGM",
            "PCT_UAST_FGM",
        ],
        "sqlTeamsScoring": [
            "GAME_ID",
            "TEAM_ID",
            "TEAM_NAME",
            "TEAM_ABBREVIATION",
            "TEAM_CITY",
            "MIN",
            "PCT_FGA_2PT",
            "PCT_FGA_3PT",
            "PCT_PTS_2PT",
            "PCT_PTS_2PT_MR",
            "PCT_PTS_3PT",
            "PCT_PTS_FB",
            "PCT_PTS_FT",
            "PCT_PTS_OFF_TOV",
            "PCT_PTS_PAINT",
            "PCT_AST_2PM",
            "PCT_UAST_2PM",
            "PCT_AST_3PM",
            "PCT_UAST_3PM",
            "PCT_AST_FGM",
            "PCT_UAST_FGM",
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
        self.sql_players_scoring = Endpoint.DataSet(data=data_sets["sqlPlayersScoring"])
        self.sql_teams_scoring = Endpoint.DataSet(data=data_sets["sqlTeamsScoring"])
