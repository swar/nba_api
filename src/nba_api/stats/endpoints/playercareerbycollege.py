from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import (
    LeagueID,
    PerModeSimple,
    SeasonTypeAllStar,
    SeasonNullable,
)


class PlayerCareerByCollege(Endpoint):
    endpoint = "playercareerbycollege"
    expected_data = {
        "PlayerCareerByCollege": [
            "PLAYER_ID",
            "PLAYER_NAME",
            "COLLEGE",
            "GP",
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
        college,
        league_id=LeagueID.default,
        per_mode_simple=PerModeSimple.default,
        season_type_all_star=SeasonTypeAllStar.default,
        season_nullable=SeasonNullable.default,
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
            "College": college,
            "LeagueID": league_id,
            "PerMode": per_mode_simple,
            "SeasonType": season_type_all_star,
            "Season": season_nullable,
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
        self.player_career_by_college = Endpoint.DataSet(
            data=data_sets["PlayerCareerByCollege"]
        )
