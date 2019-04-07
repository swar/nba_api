from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import RunType


class WinProbabilityPBP(Endpoint):
    endpoint = 'winprobabilitypbp'
    expected_data = {'GameInfo': ['GAME_ID', 'GAME_DATE', 'HOME_TEAM_ID', 'HOME_TEAM_ABR', 'HOME_TEAM_PTS', 'VISITOR_TEAM_ID', 'VISITOR_TEAM_ABR', 'VISITOR_TEAM_PTS'], 'WinProbPBP': ['GAME_ID', 'EVENT_NUM', 'HOME_PCT', 'VISITOR_PCT', 'HOME_PTS', 'VISITOR_PTS', 'HOME_SCORE_MARGIN', 'PERIOD', 'SECONDS_REMAINING', 'HOME_POSS_IND', 'HOME_G', 'DESCRIPTION', 'LOCATION', 'PCTIMESTRING', 'ISVISIBLE']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 game_id,
                 run_type=RunType.default,
                 proxy=None,
                 headers=None,
                 timeout=30,
                 get_request=True):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
                'GameID': game_id,
                'RunType': run_type
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
        self.game_info = Endpoint.DataSet(data=data_sets['GameInfo'])
        self.win_prob_p_bp = Endpoint.DataSet(data=data_sets['WinProbPBP'])
