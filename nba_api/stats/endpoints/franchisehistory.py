from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueID


class FranchiseHistory(Endpoint):
    endpoint = 'franchisehistory'
    expected_data = {'DefunctTeams': ['LEAGUE_ID', 'TEAM_ID', 'TEAM_CITY', 'TEAM_NAME', 'START_YEAR', 'END_YEAR', 'YEARS', 'GAMES', 'WINS', 'LOSSES', 'WIN_PCT', 'PO_APPEARANCES', 'DIV_TITLES', 'CONF_TITLES', 'LEAGUE_TITLES'], 'FranchiseHistory': ['LEAGUE_ID', 'TEAM_ID', 'TEAM_CITY', 'TEAM_NAME', 'START_YEAR', 'END_YEAR', 'YEARS', 'GAMES', 'WINS', 'LOSSES', 'WIN_PCT', 'PO_APPEARANCES', 'DIV_TITLES', 'CONF_TITLES', 'LEAGUE_TITLES']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
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
        self.defunct_teams = Endpoint.DataSet(data=data_sets['DefunctTeams'])
        self.franchise_history = Endpoint.DataSet(data=data_sets['FranchiseHistory'])
