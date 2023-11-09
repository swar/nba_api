from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import (
    NumberOfGames,
    SeasonAll,
    SeasonTypeAllStar,
    LeagueIDNullable,
)


class PlayerNextNGames(Endpoint):
    endpoint = "playernextngames"
    expected_data = {
        "NextNGames": [
            "GAME_ID",
            "GAME_DATE",
            "HOME_TEAM_ID",
            "VISITOR_TEAM_ID",
            "HOME_TEAM_NAME",
            "VISITOR_TEAM_NAME",
            "HOME_TEAM_ABBREVIATION",
            "VISITOR_TEAM_ABBREVIATION",
            "HOME_TEAM_NICKNAME",
            "VISITOR_TEAM_NICKNAME",
            "GAME_TIME",
            "HOME_WL",
            "VISITOR_WL",
        ]
    }

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(
        self,
        player_id,
        number_of_games=NumberOfGames.default,
        season_all=SeasonAll.default,
        season_type_all_star=SeasonTypeAllStar.default,
        league_id_nullable=LeagueIDNullable.default,
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
            "PlayerID": player_id,
            "NumberOfGames": number_of_games,
            "Season": season_all,
            "SeasonType": season_type_all_star,
            "LeagueID": league_id_nullable,
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
        self.next_n_games = Endpoint.DataSet(data=data_sets["NextNGames"])
