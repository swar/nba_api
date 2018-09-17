from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import SeasonAll, SeasonTypeAllStar, LeagueIDNullable


class PlayerGameLog(Endpoint):
    endpoint = 'playergamelog'
    expected_data = {'PlayerGameLog': ['SEASON_ID', 'Player_ID', 'Game_ID', 'GAME_DATE', 'MATCHUP', 'WL', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'PLUS_MINUS', 'VIDEO_AVAILABLE']}

    def __init__(self,
                 player_id,
                 season_all=SeasonAll.default,
                 season_type_all_star=SeasonTypeAllStar.default,
                 date_from_nullable='',
                 date_to_nullable='',
                 league_id_nullable=LeagueIDNullable.default):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={
                'PlayerID': player_id,
                'Season': season_all,
                'SeasonType': season_type_all_star,
                'DateFrom': date_from_nullable,
                'DateTo': date_to_nullable,
                'LeagueID': league_id_nullable
            },
        )
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.player_game_log = Endpoint.DataSet(data=data_sets['PlayerGameLog'])
