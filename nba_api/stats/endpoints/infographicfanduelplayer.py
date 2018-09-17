from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP


class InfographicFanDuelPlayer(Endpoint):
    endpoint = 'infographicfanduelplayer'
    expected_data = {'FanDuelPlayer': ['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'JERSEY_NUM', 'PLAYER_POSITION', 'LOCATION', 'FAN_DUEL_PTS', 'NBA_FANTASY_PTS', 'USG_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS']}

    def __init__(self,
                 game_id):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={
                'GameID': game_id
            },
        )
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.fan_duel_player = Endpoint.DataSet(data=data_sets['FanDuelPlayer'])
