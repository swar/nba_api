from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueID, Season


class DraftCombineSpotShooting(Endpoint):
    endpoint = 'draftcombinespotshooting'
    expected_data = {'Results': ['TEMP_PLAYER_ID', 'PLAYER_ID', 'FIRST_NAME', 'LAST_NAME', 'PLAYER_NAME', 'POSITION', 'FIFTEEN_CORNER_LEFT_MADE', 'FIFTEEN_CORNER_LEFT_ATTEMPT', 'FIFTEEN_CORNER_LEFT_PCT', 'FIFTEEN_BREAK_LEFT_MADE', 'FIFTEEN_BREAK_LEFT_ATTEMPT', 'FIFTEEN_BREAK_LEFT_PCT', 'FIFTEEN_TOP_KEY_MADE', 'FIFTEEN_TOP_KEY_ATTEMPT', 'FIFTEEN_TOP_KEY_PCT', 'FIFTEEN_BREAK_RIGHT_MADE', 'FIFTEEN_BREAK_RIGHT_ATTEMPT', 'FIFTEEN_BREAK_RIGHT_PCT', 'FIFTEEN_CORNER_RIGHT_MADE', 'FIFTEEN_CORNER_RIGHT_ATTEMPT', 'FIFTEEN_CORNER_RIGHT_PCT', 'COLLEGE_CORNER_LEFT_MADE', 'COLLEGE_CORNER_LEFT_ATTEMPT', 'COLLEGE_CORNER_LEFT_PCT', 'COLLEGE_BREAK_LEFT_MADE', 'COLLEGE_BREAK_LEFT_ATTEMPT', 'COLLEGE_BREAK_LEFT_PCT', 'COLLEGE_TOP_KEY_MADE', 'COLLEGE_TOP_KEY_ATTEMPT', 'COLLEGE_TOP_KEY_PCT', 'COLLEGE_BREAK_RIGHT_MADE', 'COLLEGE_BREAK_RIGHT_ATTEMPT', 'COLLEGE_BREAK_RIGHT_PCT', 'COLLEGE_CORNER_RIGHT_MADE', 'COLLEGE_CORNER_RIGHT_ATTEMPT', 'COLLEGE_CORNER_RIGHT_PCT', 'NBA_CORNER_LEFT_MADE', 'NBA_CORNER_LEFT_ATTEMPT', 'NBA_CORNER_LEFT_PCT', 'NBA_BREAK_LEFT_MADE', 'NBA_BREAK_LEFT_ATTEMPT', 'NBA_BREAK_LEFT_PCT', 'NBA_TOP_KEY_MADE', 'NBA_TOP_KEY_ATTEMPT', 'NBA_TOP_KEY_PCT', 'NBA_BREAK_RIGHT_MADE', 'NBA_BREAK_RIGHT_ATTEMPT', 'NBA_BREAK_RIGHT_PCT', 'NBA_CORNER_RIGHT_MADE', 'NBA_CORNER_RIGHT_ATTEMPT', 'NBA_CORNER_RIGHT_PCT']}

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
