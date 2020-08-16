from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueID, SeasonYear


class DraftBoard(Endpoint):
    endpoint = 'draftboard'
    expected_data = {'DraftBoard': ['PERSON_ID', 'PLAYER_NAME', 'SEASON', 'ROUND_NUMBER', 'ROUND_PICK', 'OVERALL_PICK', 'TEAM_ID', 'TEAM_CITY', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'ORGANIZATION', 'ORGANIZATION_TYPE', 'HEIGHT', 'WEIGHT', 'POSITION', 'JERSEY_NUMBER', 'BIRTHDATE', 'AGE']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 league_id=LeagueID.default,
                 season_year=SeasonYear.default,
                 college_nullable='',
                 overall_pick_nullable='',
                 round_num_nullable='',
                 round_pick_nullable='',
                 team_id_nullable='',
                 topx_nullable='',
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
                'Season': season_year,
                'College': college_nullable,
                'OverallPick': overall_pick_nullable,
                'RoundNum': round_num_nullable,
                'RoundPick': round_pick_nullable,
                'TeamID': team_id_nullable,
                'TopX': topx_nullable
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
        self.draft_board = Endpoint.DataSet(data=data_sets['DraftBoard'])
