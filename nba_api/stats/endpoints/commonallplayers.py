from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueID, Season


class CommonAllPlayers(Endpoint):
    endpoint = 'commonallplayers'
    expected_data = {'CommonAllPlayers': ['PERSON_ID', 'DISPLAY_LAST_COMMA_FIRST', 'DISPLAY_FIRST_LAST', 'ROSTERSTATUS', 'FROM_YEAR', 'TO_YEAR', 'PLAYERCODE', 'TEAM_ID', 'TEAM_CITY', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'TEAM_CODE', 'GAMES_PLAYED_FLAG']}

    def __init__(self,
                 is_only_current_season=0,
                 league_id=LeagueID.default,
                 season=Season.default):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={
                'IsOnlyCurrentSeason': is_only_current_season,
                'LeagueID': league_id,
                'Season': season
            },
        )
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.common_all_players = Endpoint.DataSet(data=data_sets['CommonAllPlayers'])
