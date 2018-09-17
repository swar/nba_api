from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueID, PerMode48, Scope, SeasonAll_Time, SeasonTypeAllStar, StatCategoryAbbreviation


class LeagueLeaders(Endpoint):
    endpoint = 'leagueleaders'
    expected_data = {'LeagueLeaders': ['PLAYER_ID', 'RANK', 'PLAYER', 'TEAM', 'GP', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'EFF', 'AST_TOV', 'STL_TOV']}

    def __init__(self,
                 league_id=LeagueID.default,
                 per_mode48=PerMode48.default,
                 scope=Scope.default,
                 season_all_time=SeasonAll_Time.default,
                 season_type_all_star=SeasonTypeAllStar.default,
                 stat_category_abbreviation=StatCategoryAbbreviation.default,
                 active_flag_nullable=''):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={
                'LeagueID': league_id,
                'PerMode': per_mode48,
                'Scope': scope,
                'Season': season_all_time,
                'SeasonType': season_type_all_star,
                'StatCategory': stat_category_abbreviation,
                'ActiveFlag': active_flag_nullable
            },
        )
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.league_leaders = Endpoint.DataSet(data=data_sets['LeagueLeaders'])
