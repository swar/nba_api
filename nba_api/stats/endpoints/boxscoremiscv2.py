from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import EndPeriod, EndRange, RangeType, StartPeriod, StartRange


class BoxScoreMiscV2(Endpoint):
    endpoint = 'boxscoremiscv2'
    expected_data = {'sqlPlayersMisc': ['GAME_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_CITY', 'PLAYER_ID', 'PLAYER_NAME', 'START_POSITION', 'COMMENT', 'MIN', 'PTS_OFF_TOV', 'PTS_2ND_CHANCE', 'PTS_FB', 'PTS_PAINT', 'OPP_PTS_OFF_TOV', 'OPP_PTS_2ND_CHANCE', 'OPP_PTS_FB', 'OPP_PTS_PAINT', 'BLK', 'BLKA', 'PF', 'PFD'], 'sqlTeamsMisc': ['GAME_ID', 'TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'TEAM_CITY', 'MIN', 'PTS_OFF_TOV', 'PTS_2ND_CHANCE', 'PTS_FB', 'PTS_PAINT', 'OPP_PTS_OFF_TOV', 'OPP_PTS_2ND_CHANCE', 'OPP_PTS_FB', 'OPP_PTS_PAINT', 'BLK', 'BLKA', 'PF', 'PFD']}

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
        self.sql_players_misc = Endpoint.DataSet(data=data_sets['sqlPlayersMisc'])
        self.sql_teams_misc = Endpoint.DataSet(data=data_sets['sqlTeamsMisc'])
