from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueID, Season


class DraftCombineNonStationaryShooting(Endpoint):
    endpoint = 'draftcombinenonstationaryshooting'
    expected_data = {'Results': ['TEMP_PLAYER_ID', 'PLAYER_ID', 'FIRST_NAME', 'LAST_NAME', 'PLAYER_NAME', 'POSITION', 'OFF_DRIB_FIFTEEN_BREAK_LEFT_MADE', 'OFF_DRIB_FIFTEEN_BREAK_LEFT_ATTEMPT', 'OFF_DRIB_FIFTEEN_BREAK_LEFT_PCT', 'OFF_DRIB_FIFTEEN_TOP_KEY_MADE', 'OFF_DRIB_FIFTEEN_TOP_KEY_ATTEMPT', 'OFF_DRIB_FIFTEEN_TOP_KEY_PCT', 'OFF_DRIB_FIFTEEN_BREAK_RIGHT_MADE', 'OFF_DRIB_FIFTEEN_BREAK_RIGHT_ATTEMPT', 'OFF_DRIB_FIFTEEN_BREAK_RIGHT_PCT', 'OFF_DRIB_COLLEGE_BREAK_LEFT_MADE', 'OFF_DRIB_COLLEGE_BREAK_LEFT_ATTEMPT', 'OFF_DRIB_COLLEGE_BREAK_LEFT_PCT', 'OFF_DRIB_COLLEGE_TOP_KEY_MADE', 'OFF_DRIB_COLLEGE_TOP_KEY_ATTEMPT', 'OFF_DRIB_COLLEGE_TOP_KEY_PCT', 'OFF_DRIB_COLLEGE_BREAK_RIGHT_MADE', 'OFF_DRIB_COLLEGE_BREAK_RIGHT_ATTEMPT', 'OFF_DRIB_COLLEGE_BREAK_RIGHT_PCT', 'ON_MOVE_FIFTEEN_MADE', 'ON_MOVE_FIFTEEN_ATTEMPT', 'ON_MOVE_FIFTEEN_PCT', 'ON_MOVE_COLLEGE_MADE', 'ON_MOVE_COLLEGE_ATTEMPT', 'ON_MOVE_COLLEGE_PCT']}

    def __init__(self,
                 league_id=LeagueID.default,
                 season=Season.default):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={
                'LeagueID': league_id,
                'SeasonYear': season
            },
        )
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.results = Endpoint.DataSet(data=data_sets['Results'])
