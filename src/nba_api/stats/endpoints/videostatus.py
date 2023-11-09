from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import GameDate, LeagueID


class VideoStatus(Endpoint):
    endpoint = "videostatus"
    expected_data = {
        "VideoStatus": [
            "GAME_ID",
            "GAME_DATE",
            "VISITOR_TEAM_ID",
            "VISITOR_TEAM_CITY",
            "VISITOR_TEAM_NAME",
            "VISITOR_TEAM_ABBREVIATION",
            "HOME_TEAM_ID",
            "HOME_TEAM_CITY",
            "HOME_TEAM_NAME",
            "HOME_TEAM_ABBREVIATION",
            "GAME_STATUS",
            "GAME_STATUS_TEXT",
            "IS_AVAILABLE",
            "PT_XYZ_AVAILABLE",
        ]
    }

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(
        self,
        game_date=GameDate.default,
        league_id=LeagueID.default,
        proxy=None,
        headers=None,
        timeout=30,
        get_request=True,
    ):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {"GameDate": game_date, "LeagueID": league_id}
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
        self.video_status = Endpoint.DataSet(data=data_sets["VideoStatus"])
