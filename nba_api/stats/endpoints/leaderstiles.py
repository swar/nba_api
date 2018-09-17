from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import GameScopeDetailed, LeagueID, PlayerOrTeam, PlayerScope, Season, SeasonType, Stat


class LeadersTiles(Endpoint):
    endpoint = 'leaderstiles'
    expected_data = {'AllTimeSeasonHigh': ['TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'SEASON_YEAR', 'PTS'], 'LastSeasonHigh': ['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'PTS'], 'LeadersTiles': ['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'PTS'], 'LowSeasonHigh': ['TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'SEASON_YEAR', 'PTS']}

    def __init__(self,
                 game_scope_detailed=GameScopeDetailed.default,
                 league_id=LeagueID.default,
                 player_or_team=PlayerOrTeam.default,
                 player_scope=PlayerScope.default,
                 season=Season.default,
                 season_type_playoffs=SeasonType.default,
                 stat=Stat.default):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={
                'GameScope': game_scope_detailed,
                'LeagueID': league_id,
                'PlayerOrTeam': player_or_team,
                'PlayerScope': player_scope,
                'Season': season,
                'SeasonType': season_type_playoffs,
                'Stat': stat
            },
        )
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.all_time_season_high = Endpoint.DataSet(data=data_sets['AllTimeSeasonHigh'])
        self.last_season_high = Endpoint.DataSet(data=data_sets['LastSeasonHigh'])
        self.leaders_tiles = Endpoint.DataSet(data=data_sets['LeadersTiles'])
        self.low_season_high = Endpoint.DataSet(data=data_sets['LowSeasonHigh'])
