from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueIDNullable


class CommonPlayerInfo(Endpoint):
    endpoint = 'commonplayerinfo'
    expected_data = {'AvailableSeasons': ['SEASON_ID'], 'CommonPlayerInfo': ['PERSON_ID', 'FIRST_NAME', 'LAST_NAME', 'DISPLAY_FIRST_LAST', 'DISPLAY_LAST_COMMA_FIRST', 'DISPLAY_FI_LAST', 'BIRTHDATE', 'SCHOOL', 'COUNTRY', 'LAST_AFFILIATION', 'HEIGHT', 'WEIGHT', 'SEASON_EXP', 'JERSEY', 'POSITION', 'ROSTERSTATUS', 'TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'TEAM_CODE', 'TEAM_CITY', 'PLAYERCODE', 'FROM_YEAR', 'TO_YEAR', 'DLEAGUE_FLAG', 'GAMES_PLAYED_FLAG', 'DRAFT_YEAR', 'DRAFT_ROUND', 'DRAFT_NUMBER'], 'PlayerHeadlineStats': ['PLAYER_ID', 'PLAYER_NAME', 'TimeFrame', 'PTS', 'AST', 'REB', 'PIE']}

    def __init__(self,
                 player_id,
                 league_id_nullable=LeagueIDNullable.default):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={
                'PlayerID': player_id,
                'LeagueID': league_id_nullable
            },
        )
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.available_seasons = Endpoint.DataSet(data=data_sets['AvailableSeasons'])
        self.common_player_info = Endpoint.DataSet(data=data_sets['CommonPlayerInfo'])
        self.player_headline_stats = Endpoint.DataSet(data=data_sets['PlayerHeadlineStats'])
