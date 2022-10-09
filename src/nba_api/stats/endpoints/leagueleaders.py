from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueID, PerMode48, Scope, Season, SeasonTypeAllStar, StatCategoryAbbreviation


class LeagueLeaders(Endpoint):
    endpoint = 'leagueleaders'
    expected_data = {'LeagueLeaders': ['PLAYER_ID', 'RANK', 'PLAYER', 'TEAM', 'GP', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'EFF', 'AST_TOV', 'STL_TOV']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 league_id=LeagueID.default,
                 per_mode48=PerMode48.default,
                 scope=Scope.default,
                 season=Season.default,
                 season_type_all_star=SeasonTypeAllStar.default,
                 stat_category_abbreviation=StatCategoryAbbreviation.default,
                 active_flag_nullable='',
                 proxy=None,
                 headers=None,
                 timeout=30,
                 get_request=True):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
                'LeagueID': league_id,
                'PerMode': per_mode48,
                'Scope': scope,
                'Season': season,
                'SeasonType': season_type_all_star,
                'StatCategory': stat_category_abbreviation,
                'ActiveFlag': active_flag_nullable
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
        self.league_leaders = Endpoint.DataSet(data=data_sets['LeagueLeaders'])
