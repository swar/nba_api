from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import (
    LeagueID,
    PerModeDetailed,
    SeasonTypeAllStar,
)


class FranchisePlayers(Endpoint):
    endpoint = "franchiseplayers"
    expected_data = {
        "FranchisePlayers": [
            "LEAGUE_ID",
            "TEAM_ID",
            "TEAM",
            "PERSON_ID",
            "PLAYER",
            "SEASON_TYPE",
            "ACTIVE_WITH_TEAM",
            "GP",
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
            "PF",
            "STL",
            "TOV",
            "BLK",
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
        league_id=LeagueID.default,
        per_mode_detailed=PerModeDetailed.default,
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
            "LeagueID": league_id,
            "PerMode": per_mode_detailed,
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
        self.franchise_players = Endpoint.DataSet(data=data_sets["FranchisePlayers"])
