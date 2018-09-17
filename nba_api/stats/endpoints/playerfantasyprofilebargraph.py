from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import Season, LeagueIDNullable, SeasonTypeAllStarNullable


class PlayerFantasyProfileBarGraph(Endpoint):
    endpoint = 'playerfantasyprofilebargraph'
    expected_data = {'LastFiveGamesAvg': ['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_ABBREVIATION', 'FAN_DUEL_PTS', 'NBA_FANTASY_PTS', 'PTS', 'REB', 'AST', 'FG3M', 'FT_PCT', 'STL', 'BLK', 'TOV', 'FG_PCT'], 'SeasonAvg': ['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_ABBREVIATION', 'FAN_DUEL_PTS', 'NBA_FANTASY_PTS', 'PTS', 'REB', 'AST', 'FG3M', 'FT_PCT', 'STL', 'BLK', 'TOV', 'FG_PCT']}

    def __init__(self,
                 player_id,
                 season=Season.default,
                 league_id_nullable=LeagueIDNullable.default,
                 season_type_all_star_nullable=SeasonTypeAllStarNullable.default):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={
                'PlayerID': player_id,
                'Season': season,
                'LeagueID': league_id_nullable,
                'SeasonType': season_type_all_star_nullable
            },
        )
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.last_five_games_avg = Endpoint.DataSet(data=data_sets['LastFiveGamesAvg'])
        self.season_avg = Endpoint.DataSet(data=data_sets['SeasonAvg'])
