from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueID, Season, SeasonTypeAllStar


class CumeStatsTeam(Endpoint):
    endpoint = "cumestatsteam"
    expected_data = {
        "GameByGameStats": [
            "JERSEY_NUM",
            "PLAYER",
            "PERSON_ID",
            "TEAM_ID",
            "GP",
            "GS",
            "ACTUAL_MINUTES",
            "ACTUAL_SECONDS",
            "FG",
            "FGA",
            "FG_PCT",
            "FG3",
            "FG3A",
            "FG3_PCT",
            "FT",
            "FTA",
            "FT_PCT",
            "OFF_REB",
            "DEF_REB",
            "TOT_REB",
            "AST",
            "PF",
            "DQ",
            "STL",
            "TURNOVERS",
            "BLK",
            "PTS",
            "MAX_ACTUAL_MINUTES",
            "MAX_ACTUAL_SECONDS",
            "MAX_REB",
            "MAX_AST",
            "MAX_STL",
            "MAX_TURNOVERS",
            "MAX_BLKP",
            "MAX_PTS",
            "AVG_ACTUAL_MINUTES",
            "AVG_ACTUAL_SECONDS",
            "AVG_REB",
            "AVG_AST",
            "AVG_STL",
            "AVG_TURNOVERS",
            "AVG_BLKP",
            "AVG_PTS",
            "PER_MIN_REB",
            "PER_MIN_AST",
            "PER_MIN_STL",
            "PER_MIN_TURNOVERS",
            "PER_MIN_BLK",
            "PER_MIN_PTS",
        ],
        "TotalTeamStats": [
            "CITY",
            "NICKNAME",
            "TEAM_ID",
            "W",
            "L",
            "W_HOME",
            "L_HOME",
            "W_ROAD",
            "L_ROAD",
            "TEAM_TURNOVERS",
            "TEAM_REBOUNDS",
            "GP",
            "GS",
            "ACTUAL_MINUTES",
            "ACTUAL_SECONDS",
            "FG",
            "FGA",
            "FG_PCT",
            "FG3",
            "FG3A",
            "FG3_PCT",
            "FT",
            "FTA",
            "FT_PCT",
            "OFF_REB",
            "DEF_REB",
            "TOT_REB",
            "AST",
            "PF",
            "STL",
            "TOTAL_TURNOVERS",
            "BLK",
            "PTS",
            "AVG_REB",
            "AVG_PTS",
            "DQ",
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
        game_ids,
        league_id=LeagueID.default,
        season=Season.default,
        season_type_all_star=SeasonTypeAllStar.default,
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
            "GameIDs": game_ids,
            "LeagueID": league_id,
            "Season": season,
            "SeasonType": season_type_all_star,
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
        self.game_by_game_stats = Endpoint.DataSet(data=data_sets["GameByGameStats"])
        self.total_team_stats = Endpoint.DataSet(data=data_sets["TotalTeamStats"])
