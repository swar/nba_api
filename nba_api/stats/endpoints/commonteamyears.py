from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueID


class CommonTeamYears(Endpoint):
    endpoint = 'commonteamyears'
    expected_data = {'TeamYears': ['LEAGUE_ID', 'TEAM_ID', 'MIN_YEAR', 'MAX_YEAR', 'ABBREVIATION']}

    def __init__(self,
                 league_id=LeagueID.default):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={
                'LeagueID': league_id
            },
        )
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.team_years = Endpoint.DataSet(data=data_sets['TeamYears'])
