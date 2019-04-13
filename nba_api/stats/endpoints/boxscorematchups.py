from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP


class BoxScoreMatchups(Endpoint):
    endpoint = 'boxscorematchups'
    expected_data = {'PlayerMatchupsStats': ['GAME_ID', 'OFF_TEAM_ID', 'OFF_TEAM_ABBREVIATION', 'OFF_TEAM_CITY', 'OFF_TEAM_NICKNAME', 'OFF_PLAYER_ID', 'OFF_PLAYER_NAME', 'DEF_TEAM_ID', 'DEF_TEAM_ABBREVIATION', 'DEF_TEAM_CITY', 'DEF_TEAM_NICKNAME', 'DEF_PLAYER_ID', 'DEF_PLAYER_NAME', 'POSS', 'OFF_MATCHUP_PCT', 'PLAYER_PTS', 'TEAM_PTS', 'AST', 'TOV', 'BLK', 'HELP_BLK', 'HELP_BLK_REC', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'SFL', 'DEF_FOULS', 'OFF_FOULS']}

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
        self.player_matchups_stats = Endpoint.DataSet(data=data_sets['PlayerMatchupsStats'])
