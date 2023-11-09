from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import (
    GameScopeDetailed,
    LeagueID,
    PlayerOrTeam,
    PlayerScope,
    Season,
    SeasonType,
    StatType,
)


class HomePageV2(Endpoint):
    endpoint = "homepagev2"
    expected_data = {
        "HomePageStat1": ["RANK", "TEAM_ID", "TEAM_ABBREVIATION", "TEAM_NAME", "PTS"],
        "HomePageStat2": ["RANK", "TEAM_ID", "TEAM_ABBREVIATION", "TEAM_NAME", "REB"],
        "HomePageStat3": ["RANK", "TEAM_ID", "TEAM_ABBREVIATION", "TEAM_NAME", "AST"],
        "HomePageStat4": ["RANK", "TEAM_ID", "TEAM_ABBREVIATION", "TEAM_NAME", "STL"],
        "HomePageStat5": [
            "RANK",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "FG_PCT",
        ],
        "HomePageStat6": [
            "RANK",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "FT_PCT",
        ],
        "HomePageStat7": [
            "RANK",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "FG3_PCT",
        ],
        "HomePageStat8": ["RANK", "TEAM_ID", "TEAM_ABBREVIATION", "TEAM_NAME", "BLK"],
    }

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(
        self,
        game_scope_detailed=GameScopeDetailed.default,
        league_id=LeagueID.default,
        player_or_team=PlayerOrTeam.default,
        player_scope=PlayerScope.default,
        season=Season.default,
        season_type_playoffs=SeasonType.default,
        stat_type=StatType.default,
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
            "GameScope": game_scope_detailed,
            "LeagueID": league_id,
            "PlayerOrTeam": player_or_team,
            "PlayerScope": player_scope,
            "Season": season,
            "SeasonType": season_type_playoffs,
            "StatType": stat_type,
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
        self.home_page_stat1 = Endpoint.DataSet(data=data_sets["HomePageStat1"])
        self.home_page_stat2 = Endpoint.DataSet(data=data_sets["HomePageStat2"])
        self.home_page_stat3 = Endpoint.DataSet(data=data_sets["HomePageStat3"])
        self.home_page_stat4 = Endpoint.DataSet(data=data_sets["HomePageStat4"])
        self.home_page_stat5 = Endpoint.DataSet(data=data_sets["HomePageStat5"])
        self.home_page_stat6 = Endpoint.DataSet(data=data_sets["HomePageStat6"])
        self.home_page_stat7 = Endpoint.DataSet(data=data_sets["HomePageStat7"])
        self.home_page_stat8 = Endpoint.DataSet(data=data_sets["HomePageStat8"])
