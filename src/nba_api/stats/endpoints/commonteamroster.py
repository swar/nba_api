from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import Season, LeagueIDNullable


class CommonTeamRoster(Endpoint):
    endpoint = 'commonteamroster'
    expected_data = {'Coaches': ['TEAM_ID', 'SEASON', 'COACH_ID', 'FIRST_NAME', 'LAST_NAME', 'COACH_NAME', 'IS_ASSISTANT', 'COACH_TYPE', 'SORT_SEQUENCE'], 'CommonTeamRoster': ['TeamID', 'SEASON', 'LeagueID', 'PLAYER', 'PLAYER_SLUG', 'NUM', 'POSITION', 'HEIGHT', 'WEIGHT', 'BIRTH_DATE', 'AGE', 'EXP', 'SCHOOL', 'PLAYER_ID']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 team_id,
                 season=Season.default,
                 league_id_nullable=LeagueIDNullable.default,
                 proxy=None,
                 headers=None,
                 timeout=30,
                 get_request=True):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
                'TeamID': team_id,
                'Season': season,
                'LeagueID': league_id_nullable
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
        self.coaches = Endpoint.DataSet(data=data_sets['Coaches'])
        self.common_team_roster = Endpoint.DataSet(data=data_sets['CommonTeamRoster'])
