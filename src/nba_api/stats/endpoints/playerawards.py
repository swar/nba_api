from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP


class PlayerAwards(Endpoint):
    endpoint = "playerawards"
    expected_data = {
        "PlayerAwards": [
            "PERSON_ID",
            "FIRST_NAME",
            "LAST_NAME",
            "TEAM",
            "DESCRIPTION",
            "ALL_NBA_TEAM_NUMBER",
            "SEASON",
            "MONTH",
            "WEEK",
            "CONFERENCE",
            "TYPE",
            "SUBTYPE1",
            "SUBTYPE2",
            "SUBTYPE3",
        ]
    }

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(
        self, player_id, proxy=None, headers=None, timeout=30, get_request=True
    ):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {"PlayerID": player_id}
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
        self.player_awards = Endpoint.DataSet(data=data_sets["PlayerAwards"])
