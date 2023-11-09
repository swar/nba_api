from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import EndPeriod, StartPeriod


class PlayByPlayV2(Endpoint):
    endpoint = "playbyplayv2"
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
            "PERSON1TYPE",
            "PLAYER1_ID",
            "PLAYER1_NAME",
            "PLAYER1_TEAM_ID",
            "PLAYER1_TEAM_CITY",
            "PLAYER1_TEAM_NICKNAME",
            "PLAYER1_TEAM_ABBREVIATION",
            "PERSON2TYPE",
            "PLAYER2_ID",
            "PLAYER2_NAME",
            "PLAYER2_TEAM_ID",
            "PLAYER2_TEAM_CITY",
            "PLAYER2_TEAM_NICKNAME",
            "PLAYER2_TEAM_ABBREVIATION",
            "PERSON3TYPE",
            "PLAYER3_ID",
            "PLAYER3_NAME",
            "PLAYER3_TEAM_ID",
            "PLAYER3_TEAM_CITY",
            "PLAYER3_TEAM_NICKNAME",
            "PLAYER3_TEAM_ABBREVIATION",
            "VIDEO_AVAILABLE_FLAG",
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
