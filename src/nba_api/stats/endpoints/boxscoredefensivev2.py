from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP


class BoxScoreDefensiveV2(Endpoint):
    endpoint = "boxscoredefensivev2"
    expected_data = {
        "PlayerStats": [
            "gameId",
            "teamId",
            "teamCity",
            "teamName",
            "teamTricode",
            "teamSlug",
            "personId",
            "firstName",
            "familyName",
            "nameI",
            "playerSlug",
            "position",
            "comment",
            "jerseyNum",
            "matchupMinutes",
            "partialPossessions",
            "switchesOn",
            "playerPoints",
            "defensiveRebounds",
            "matchupAssists",
            "matchupTurnovers",
            "steals",
            "blocks",
            "matchupFieldGoalsMade",
            "matchupFieldGoalsAttempted",
            "matchupFieldGoalPercentage",
            "matchupThreePointersMade",
            "matchupThreePointersAttempted",
            "matchupThreePointerPercentage",
        ],
        "TeamStats": [
            "gameId",
            "teamId",
            "teamCity",
            "teamName",
            "teamTricode",
            "teamSlug",
            "minutes",
        ],
    }

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self, game_id, proxy=None, headers=None, timeout=30, get_request=True):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {"GameID": game_id}
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
        data_sets = self.nba_response.get_data_sets(self.endpoint)
        self.data_sets = [
            Endpoint.DataSet(data=data_set)
            for data_set_name, data_set in data_sets.items()
        ]
        self.player_stats = Endpoint.DataSet(data=data_sets["PlayerStats"])
        self.team_stats = Endpoint.DataSet(data=data_sets["TeamStats"])
