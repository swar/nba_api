from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import GameScopeDetailed, LeagueID, PlayerOrTeam, PlayerScope, Season, SeasonType


class DefenseHub(Endpoint):
    endpoint = 'defensehub'
    expected_data = {'DefenseHubStat1': ['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'DREB'], 'DefenseHubStat10': [], 'DefenseHubStat2': ['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'STL'], 'DefenseHubStat3': ['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'BLK'], 'DefenseHubStat4': ['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'TM_DEF_RATING'], 'DefenseHubStat5': ['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'OVERALL_PM'], 'DefenseHubStat6': ['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'THREEP_DFGPCT'], 'DefenseHubStat7': ['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'TWOP_DFGPCT'], 'DefenseHubStat8': ['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'FIFETEENF_DFGPCT'], 'DefenseHubStat9': ['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'DEF_RIM_PCT']}

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
                'SeasonType': season_type_playoffs
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
        self.defense_hub_stat1 = Endpoint.DataSet(data=data_sets['DefenseHubStat1'])
        self.defense_hub_stat10 = Endpoint.DataSet(data=data_sets['DefenseHubStat10'])
        self.defense_hub_stat2 = Endpoint.DataSet(data=data_sets['DefenseHubStat2'])
        self.defense_hub_stat3 = Endpoint.DataSet(data=data_sets['DefenseHubStat3'])
        self.defense_hub_stat4 = Endpoint.DataSet(data=data_sets['DefenseHubStat4'])
        self.defense_hub_stat5 = Endpoint.DataSet(data=data_sets['DefenseHubStat5'])
        self.defense_hub_stat6 = Endpoint.DataSet(data=data_sets['DefenseHubStat6'])
        self.defense_hub_stat7 = Endpoint.DataSet(data=data_sets['DefenseHubStat7'])
        self.defense_hub_stat8 = Endpoint.DataSet(data=data_sets['DefenseHubStat8'])
        self.defense_hub_stat9 = Endpoint.DataSet(data=data_sets['DefenseHubStat9'])
