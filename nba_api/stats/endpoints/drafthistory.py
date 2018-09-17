from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueID, SeasonYearNullable


class DraftHistory(Endpoint):
    endpoint = 'drafthistory'
    expected_data = {'DraftHistory': ['PERSON_ID', 'PLAYER_NAME', 'SEASON', 'ROUND_NUMBER', 'ROUND_PICK', 'OVERALL_PICK', 'TEAM_ID', 'TEAM_CITY', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'ORGANIZATION', 'ORGANIZATION_TYPE']}

    def __init__(self,
                 league_id=LeagueID.default,
                 college_nullable='',
                 overall_pick_nullable='',
                 round_num_nullable='',
                 round_pick_nullable='',
                 season_year_nullable=SeasonYearNullable.default,
                 team_id_nullable='',
                 topx_nullable=''):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={
                'LeagueID': league_id,
                'College': college_nullable,
                'OverallPick': overall_pick_nullable,
                'RoundNum': round_num_nullable,
                'RoundPick': round_pick_nullable,
                'Season': season_year_nullable,
                'TeamID': team_id_nullable,
                'TopX': topx_nullable
            },
        )
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.draft_history = Endpoint.DataSet(data=data_sets['DraftHistory'])
