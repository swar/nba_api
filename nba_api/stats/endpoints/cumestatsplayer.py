from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueID, Season, SeasonTypeAllStar


class CumeStatsPlayer(Endpoint):
    endpoint = 'cumestatsplayer'
    expected_data = {'GameByGameStats': ['DATE_EST', 'VISITOR_TEAM', 'HOME_TEAM', 'GP', 'GS', 'ACTUAL_MINUTES', 'ACTUAL_SECONDS', 'FG', 'FGA', 'FG_PCT', 'FG3', 'FG3A', 'FG3_PCT', 'FT', 'FTA', 'FT_PCT', 'OFF_REB', 'DEF_REB', 'TOT_REB', 'AVG_TOT_REB', 'AST', 'PF', 'DQ', 'STL', 'TURNOVERS', 'BLK', 'PTS', 'AVG_PTS'], 'TotalPlayerStats': ['DISPLAY_FI_LAST', 'PERSON_ID', 'JERSEY_NUM', 'GP', 'GS', 'ACTUAL_MINUTES', 'ACTUAL_SECONDS', 'FG', 'FGA', 'FG_PCT', 'FG3', 'FG3A', 'FG3_PCT', 'FT', 'FTA', 'FT_PCT', 'OFF_REB', 'DEF_REB', 'TOT_REB', 'AST', 'PF', 'DQ', 'STL', 'TURNOVERS', 'BLK', 'PTS', 'MAX_ACTUAL_MINUTES', 'MAX_ACTUAL_SECONDS', 'MAX_REB', 'MAX_AST', 'MAX_STL', 'MAX_TURNOVERS', 'MAX_BLK', 'MAX_PTS', 'AVG_ACTUAL_MINUTES', 'AVG_ACTUAL_SECONDS', 'AVG_TOT_REB', 'AVG_AST', 'AVG_STL', 'AVG_TURNOVERS', 'AVG_BLK', 'AVG_PTS', 'PER_MIN_TOT_REB', 'PER_MIN_AST', 'PER_MIN_STL', 'PER_MIN_TURNOVERS', 'PER_MIN_BLK', 'PER_MIN_PTS']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 player_id,
                 game_ids,
                 league_id=LeagueID.default,
                 season=Season.default,
                 season_type_all_star=SeasonTypeAllStar.default,
                 proxy=None,
                 headers=None,
                 timeout=30,
                 get_request=True):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
                'PlayerID': player_id,
                'GameIDs': game_ids,
                'LeagueID': league_id,
                'Season': season,
                'SeasonType': season_type_all_star
        }
        if get_request:
            self.get_request()
    
    def get_request(self):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters=self.parameters,
            proxy=self.proxy,
            headers=self.headers,
            timeout=self.timeout,
        )
        self.load_response()
        
    def load_response(self):
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.game_by_game_stats = Endpoint.DataSet(data=data_sets['GameByGameStats'])
        self.total_player_stats = Endpoint.DataSet(data=data_sets['TotalPlayerStats'])
