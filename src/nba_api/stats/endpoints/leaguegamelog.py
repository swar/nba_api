from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import (
    Direction,
    LeagueID,
    PlayerOrTeamAbbreviation,
    Season,
    SeasonTypeAllStar,
    Sorter,
)


class LeagueGameLog(Endpoint):
    endpoint = "leaguegamelog"
    expected_data = {
        "LeagueGameLog": [
            "SEASON_ID",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "GAME_ID",
            "GAME_DATE",
            "MATCHUP",
            "WL",
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
            "PLUS_MINUS",
            "VIDEO_AVAILABLE",
        ]
    }

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(
        self,
        counter=0,
        direction=Direction.default,
        league_id=LeagueID.default,
        player_or_team_abbreviation=PlayerOrTeamAbbreviation.default,
        season=Season.default,
        season_type_all_star=SeasonTypeAllStar.default,
        sorter=Sorter.default,
        date_from_nullable="",
        date_to_nullable="",
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
            "Counter": counter,
            "Direction": direction,
            "LeagueID": league_id,
            "PlayerOrTeam": player_or_team_abbreviation,
            "Season": season,
            "SeasonType": season_type_all_star,
            "Sorter": sorter,
            "DateFrom": date_from_nullable,
            "DateTo": date_to_nullable,
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
        self.league_game_log = Endpoint.DataSet(data=data_sets["LeagueGameLog"])
