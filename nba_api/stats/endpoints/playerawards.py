from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP


class PlayerAwards(Endpoint):
    endpoint = 'playerawards'
    expected_data = {'PlayerAwards': ['PERSON_ID', 'FIRST_NAME', 'LAST_NAME', 'TEAM', 'DESCRIPTION', 'ALL_NBA_TEAM_NUMBER', 'SEASON', 'MONTH', 'WEEK', 'CONFERENCE', 'TYPE', 'SUBTYPE1', 'SUBTYPE2', 'SUBTYPE3']}

    def __init__(self,
                 player_id):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={
                'PlayerID': player_id
            },
        )
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.player_awards = Endpoint.DataSet(data=data_sets['PlayerAwards'])
