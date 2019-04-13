from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueID, SeasonYear


class DraftCombineNonStationaryShooting(Endpoint):
    endpoint = 'draftcombinenonstationaryshooting'
    expected_data = {'Results': ['TEMP_PLAYER_ID', 'PLAYER_ID', 'FIRST_NAME', 'LAST_NAME', 'PLAYER_NAME', 'POSITION', 'OFF_DRIB_FIFTEEN_BREAK_LEFT_MADE', 'OFF_DRIB_FIFTEEN_BREAK_LEFT_ATTEMPT', 'OFF_DRIB_FIFTEEN_BREAK_LEFT_PCT', 'OFF_DRIB_FIFTEEN_TOP_KEY_MADE', 'OFF_DRIB_FIFTEEN_TOP_KEY_ATTEMPT', 'OFF_DRIB_FIFTEEN_TOP_KEY_PCT', 'OFF_DRIB_FIFTEEN_BREAK_RIGHT_MADE', 'OFF_DRIB_FIFTEEN_BREAK_RIGHT_ATTEMPT', 'OFF_DRIB_FIFTEEN_BREAK_RIGHT_PCT', 'OFF_DRIB_COLLEGE_BREAK_LEFT_MADE', 'OFF_DRIB_COLLEGE_BREAK_LEFT_ATTEMPT', 'OFF_DRIB_COLLEGE_BREAK_LEFT_PCT', 'OFF_DRIB_COLLEGE_TOP_KEY_MADE', 'OFF_DRIB_COLLEGE_TOP_KEY_ATTEMPT', 'OFF_DRIB_COLLEGE_TOP_KEY_PCT', 'OFF_DRIB_COLLEGE_BREAK_RIGHT_MADE', 'OFF_DRIB_COLLEGE_BREAK_RIGHT_ATTEMPT', 'OFF_DRIB_COLLEGE_BREAK_RIGHT_PCT', 'ON_MOVE_FIFTEEN_MADE', 'ON_MOVE_FIFTEEN_ATTEMPT', 'ON_MOVE_FIFTEEN_PCT', 'ON_MOVE_COLLEGE_MADE', 'ON_MOVE_COLLEGE_ATTEMPT', 'ON_MOVE_COLLEGE_PCT']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 league_id=LeagueID.default,
                 season_year=SeasonYear.default,
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
                'SeasonYear': season_year
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
        self.results = Endpoint.DataSet(data=data_sets['Results'])
