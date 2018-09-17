from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import EndPeriod, StartPeriod


class PlayByPlay(Endpoint):
    endpoint = 'playbyplay'
    expected_data = {'AvailableVideo': ['VIDEO_AVAILABLE_FLAG'], 'PlayByPlay': ['GAME_ID', 'EVENTNUM', 'EVENTMSGTYPE', 'EVENTMSGACTIONTYPE', 'PERIOD', 'WCTIMESTRING', 'PCTIMESTRING', 'HOMEDESCRIPTION', 'NEUTRALDESCRIPTION', 'VISITORDESCRIPTION', 'SCORE', 'SCOREMARGIN']}

    def __init__(self,
                 game_id,
                 end_period=EndPeriod.default,
                 start_period=StartPeriod.default):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={
                'GameID': game_id,
                'EndPeriod': end_period,
                'StartPeriod': start_period
            },
        )
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.available_video = Endpoint.DataSet(data=data_sets['AvailableVideo'])
        self.play_by_play = Endpoint.DataSet(data=data_sets['PlayByPlay'])
