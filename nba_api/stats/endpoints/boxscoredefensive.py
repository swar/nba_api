from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP


class BoxScoreDefensive(Endpoint):
    endpoint = 'boxscoredefensive'
    expected_data = {'PlayerDefensiveStats': ['GAME_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_CITY', 'TEAM_NICKNAME', 'PLAYER_ID', 'PLAYER_NAME', 'START_POSITION', 'COMMENT', 'MATCHUP_MIN', 'PARTIAL_POSS', 'SWITCHES_ON', 'PLAYER_PTS', 'DREB', 'MATCHUP_AST', 'MATCHUP_TOV', 'STL', 'BLK', 'MATCHUP_FGM', 'MATCHUP_FGA', 'MATCHUP_FG_PCT', 'MATCHUP_FG3M', 'MATCHUP_FG3A', 'MATCHUP_FG3_PCT'], 'Table1': [':1']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 game_id,
                 proxy=None,
                 headers=None,
                 timeout=30,
                 get_request=True):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
                'GameID': game_id
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
        self.player_defensive_stats = Endpoint.DataSet(data=data_sets['PlayerDefensiveStats'])
        self.table1 = Endpoint.DataSet(data=data_sets['Table1'])
