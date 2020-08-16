from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueID


class GameRotation(Endpoint):
    endpoint = 'gamerotation'
    expected_data = {'AwayTeam': ['GAME_ID', 'TEAM_ID', 'TEAM_CITY', 'TEAM_NAME', 'PERSON_ID', 'PLAYER_FIRST', 'PLAYER_LAST', 'IN_TIME_REAL', 'OUT_TIME_REAL', 'PLAYER_PTS', 'PT_DIFF', 'USG_PCT'], 'HomeTeam': ['GAME_ID', 'TEAM_ID', 'TEAM_CITY', 'TEAM_NAME', 'PERSON_ID', 'PLAYER_FIRST', 'PLAYER_LAST', 'IN_TIME_REAL', 'OUT_TIME_REAL', 'PLAYER_PTS', 'PT_DIFF', 'USG_PCT']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 game_id,
                 league_id=LeagueID.default,
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
                'LeagueID': league_id
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
        self.away_team = Endpoint.DataSet(data=data_sets['AwayTeam'])
        self.home_team = Endpoint.DataSet(data=data_sets['HomeTeam'])
