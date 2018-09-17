from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import EndPeriod, EndRange, RangeType, StartPeriod, StartRange


class BoxScoreFourFactorsV2(Endpoint):
    endpoint = 'boxscorefourfactorsv2'
    expected_data = {'sqlPlayersFourFactors': ['GAME_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_CITY', 'PLAYER_ID', 'PLAYER_NAME', 'START_POSITION', 'COMMENT', 'MIN', 'EFG_PCT', 'FTA_RATE', 'TM_TOV_PCT', 'OREB_PCT', 'OPP_EFG_PCT', 'OPP_FTA_RATE', 'OPP_TOV_PCT', 'OPP_OREB_PCT'], 'sqlTeamsFourFactors': ['GAME_ID', 'TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'TEAM_CITY', 'MIN', 'EFG_PCT', 'FTA_RATE', 'TM_TOV_PCT', 'OREB_PCT', 'OPP_EFG_PCT', 'OPP_FTA_RATE', 'OPP_TOV_PCT', 'OPP_OREB_PCT']}

    def __init__(self,
                 game_id,
                 end_period=EndPeriod.default,
                 end_range=EndRange.default,
                 range_type=RangeType.default,
                 start_period=StartPeriod.default,
                 start_range=StartRange.default):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={
                'GameID': game_id,
                'EndPeriod': end_period,
                'EndRange': end_range,
                'RangeType': range_type,
                'StartPeriod': start_period,
                'StartRange': start_range
            },
        )
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.sql_players_four_factors = Endpoint.DataSet(data=data_sets['sqlPlayersFourFactors'])
        self.sql_teams_four_factors = Endpoint.DataSet(data=data_sets['sqlTeamsFourFactors'])
