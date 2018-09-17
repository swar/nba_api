from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueID


class FranchiseHistory(Endpoint):
    endpoint = 'franchisehistory'
    expected_data = {'DefunctTeams': ['LEAGUE_ID', 'TEAM_ID', 'TEAM_CITY', 'TEAM_NAME', 'START_YEAR', 'END_YEAR', 'YEARS', 'GAMES', 'WINS', 'LOSSES', 'WIN_PCT', 'PO_APPEARANCES', 'DIV_TITLES', 'CONF_TITLES', 'LEAGUE_TITLES'], 'FranchiseHistory': ['LEAGUE_ID', 'TEAM_ID', 'TEAM_CITY', 'TEAM_NAME', 'START_YEAR', 'END_YEAR', 'YEARS', 'GAMES', 'WINS', 'LOSSES', 'WIN_PCT', 'PO_APPEARANCES', 'DIV_TITLES', 'CONF_TITLES', 'LEAGUE_TITLES']}

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
        self.defunct_teams = Endpoint.DataSet(data=data_sets['DefunctTeams'])
        self.franchise_history = Endpoint.DataSet(data=data_sets['FranchiseHistory'])
