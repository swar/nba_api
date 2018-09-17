from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import MeasureTypeBase, PaceAdjustNo, PerMode36, PlusMinusNo, RankNo, Season, SeasonType, LeagueIDNullable


class PlayerFantasyProfile(Endpoint):
    endpoint = 'playerfantasyprofile'
    expected_data = {'DaysRestModified': ['GROUP_SET', 'GROUP_VALUE', 'SEASON_YEAR', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'DD2', 'TD3', 'FAN_DUEL_PTS'], 'LastNGames': ['GROUP_SET', 'GROUP_VALUE', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'DD2', 'TD3', 'FAN_DUEL_PTS'], 'Location': ['GROUP_SET', 'GROUP_VALUE', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'DD2', 'TD3', 'FAN_DUEL_PTS'], 'Opponent': ['GROUP_SET', 'GROUP_VALUE', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'DD2', 'TD3', 'FAN_DUEL_PTS'], 'Overall': ['GROUP_SET', 'GROUP_VALUE', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'DD2', 'TD3', 'FAN_DUEL_PTS']}

    def __init__(self,
                 player_id,
                 measure_type_base=MeasureTypeBase.default,
                 pace_adjust_no=PaceAdjustNo.default,
                 per_mode36=PerMode36.default,
                 plus_minus_no=PlusMinusNo.default,
                 rank_no=RankNo.default,
                 season=Season.default,
                 season_type_playoffs=SeasonType.default,
                 league_id_nullable=LeagueIDNullable.default):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={
                'PlayerID': player_id,
                'MeasureType': measure_type_base,
                'PaceAdjust': pace_adjust_no,
                'PerMode': per_mode36,
                'PlusMinus': plus_minus_no,
                'Rank': rank_no,
                'Season': season,
                'SeasonType': season_type_playoffs,
                'LeagueID': league_id_nullable
            },
        )
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.days_rest_modified = Endpoint.DataSet(data=data_sets['DaysRestModified'])
        self.last_n_games = Endpoint.DataSet(data=data_sets['LastNGames'])
        self.location = Endpoint.DataSet(data=data_sets['Location'])
        self.opponent = Endpoint.DataSet(data=data_sets['Opponent'])
        self.overall = Endpoint.DataSet(data=data_sets['Overall'])
