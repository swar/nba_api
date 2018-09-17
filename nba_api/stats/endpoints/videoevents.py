from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP


class VideoEvents(Endpoint):
    endpoint = 'videoevents'
    expected_data = {}

    def __init__(self,
                 game_id,
                 game_event_id=0):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={
                'GameID': game_id,
                'GameEventID': game_event_id
            },
        )
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]

