from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import Season, SeasonTypeAllStar, LeagueIDNullable


class TeamGameLog(Endpoint):
    endpoint = "teamgamelog"
    expected_data = {
        "TeamGameLog": [
            "Team_ID",
            "Game_ID",
            "GAME_DATE",
            "MATCHUP",
            "WL",
            "W",
            "L",
            "W_PCT",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "STL",
            "BLK",
            "TOV",
            "PF",
            "PTS",
        ]
    }

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(
        self,
        team_id,
        season=Season.default,
        season_type_all_star=SeasonTypeAllStar.default,
        date_from_nullable="",
        date_to_nullable="",
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
            "TeamID": team_id,
            "Season": season,
            "SeasonType": season_type_all_star,
            "DateFrom": date_from_nullable,
            "DateTo": date_to_nullable,
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
        self.team_game_log = Endpoint.DataSet(data=data_sets["TeamGameLog"])
