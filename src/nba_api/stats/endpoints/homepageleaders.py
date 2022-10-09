from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import GameScopeDetailed, LeagueID, PlayerOrTeam, PlayerScope, Season, SeasonType, StatCategory


class HomePageLeaders(Endpoint):
    endpoint = 'homepageleaders'
    expected_data = {'HomePageLeaders': ['RANK', 'TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'PTS', 'FG_PCT', 'FG3_PCT', 'FT_PCT', 'EFG_PCT', 'TS_PCT', 'PTS_PER48'], 'LeagueAverage': ['PTS', 'FG_PCT', 'FG3_PCT', 'FT_PCT', 'EFG_PCT', 'TS_PCT', 'PTS_PER48'], 'LeagueMax': ['PTS', 'FG_PCT', 'FG3_PCT', 'FT_PCT', 'EFG_PCT', 'TS_PCT', 'PTS_PER48']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 game_scope_detailed=GameScopeDetailed.default,
                 league_id=LeagueID.default,
                 player_or_team=PlayerOrTeam.default,
                 player_scope=PlayerScope.default,
                 season=Season.default,
                 season_type_playoffs=SeasonType.default,
                 stat_category=StatCategory.default,
                 proxy=None,
                 headers=None,
                 timeout=30,
                 get_request=True):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
                'GameScope': game_scope_detailed,
                'LeagueID': league_id,
                'PlayerOrTeam': player_or_team,
                'PlayerScope': player_scope,
                'Season': season,
                'SeasonType': season_type_playoffs,
                'StatCategory': stat_category
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
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.home_page_leaders = Endpoint.DataSet(data=data_sets['HomePageLeaders'])
        self.league_average = Endpoint.DataSet(data=data_sets['LeagueAverage'])
        self.league_max = Endpoint.DataSet(data=data_sets['LeagueMax'])
