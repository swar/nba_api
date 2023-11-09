from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueID, Season


class CommonAllPlayers(Endpoint):
    endpoint = "commonallplayers"
    expected_data = {
        "CommonAllPlayers": [
            "PERSON_ID",
            "DISPLAY_LAST_COMMA_FIRST",
            "DISPLAY_FIRST_LAST",
            "ROSTERSTATUS",
            "FROM_YEAR",
            "TO_YEAR",
            "PLAYERCODE",
            "TEAM_ID",
            "TEAM_CITY",
            "TEAM_NAME",
            "TEAM_ABBREVIATION",
            "TEAM_CODE",
            "GAMES_PLAYED_FLAG",
            "OTHERLEAGUE_EXPERIENCE_CH",
        ]
    }

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(
        self,
        is_only_current_season=0,
        league_id=LeagueID.default,
        season=Season.default,
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
            "IsOnlyCurrentSeason": is_only_current_season,
            "LeagueID": league_id,
            "Season": season,
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
        self.common_all_players = Endpoint.DataSet(data=data_sets["CommonAllPlayers"])
