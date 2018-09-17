from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueID, SeasonID


class TeamHistoricalLeaders(Endpoint):
    endpoint = 'teamhistoricalleaders'
    expected_data = {'CareerLeadersByTeam': ['TEAM_ID', 'PTS', 'PTS_PERSON_ID', 'PTS_PLAYER', 'AST', 'AST_PERSON_ID', 'AST_PLAYER', 'REB', 'REB_PERSON_ID', 'REB_PLAYER', 'BLK', 'BLK_PERSON_ID', 'BLK_PLAYER', 'STL', 'STL_PERSON_ID', 'STL_PLAYER', 'SEASON_YEAR']}

    def __init__(self,
                 team_id,
                 league_id=LeagueID.default,
                 season_id=SeasonID.default):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={
                'TeamID': team_id,
                'LeagueID': league_id,
                'SeasonID': season_id
            },
        )
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.career_leaders_by_team = Endpoint.DataSet(data=data_sets['CareerLeadersByTeam'])
