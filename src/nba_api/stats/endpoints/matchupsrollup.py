from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueID, PerModeSimple, Season, SeasonType


class MatchupsRollup(Endpoint):
    endpoint = 'matchupsrollup'
    expected_data = {'MatchupsRollup': ['SEASON_ID', 'POSITION', 'PERCENT_OF_TIME', 'DEF_PLAYER_ID', 'DEF_PLAYER_NAME', 'GP', 'MATCHUP_MIN', 'PARTIAL_POSS', 'PLAYER_PTS', 'TEAM_PTS', 'MATCHUP_AST', 'MATCHUP_TOV', 'MATCHUP_BLK', 'MATCHUP_FGM', 'MATCHUP_FGA', 'MATCHUP_FG_PCT', 'MATCHUP_FG3M', 'MATCHUP_FG3A', 'MATCHUP_FG3_PCT', 'MATCHUP_FTM', 'MATCHUP_FTA', 'SFL']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 league_id=LeagueID.default,
                 per_mode_simple=PerModeSimple.default,
                 season=Season.default,
                 season_type_playoffs=SeasonType.default,
                 def_player_id_nullable='',
                 def_team_id_nullable=None,
                 off_player_id_nullable='',
                 off_team_id_nullable=None,
                 proxy=None,
                 headers=None,
                 timeout=30,
                 get_request=True):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
                'LeagueID': league_id,
                'PerMode': per_mode_simple,
                'Season': season,
                'SeasonType': season_type_playoffs,
                'DefPlayerID': def_player_id_nullable,
                'DefTeamID': def_team_id_nullable,
                'OffPlayerID': off_player_id_nullable,
                'OffTeamID': off_team_id_nullable
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
        self.matchups_rollup = Endpoint.DataSet(data=data_sets['MatchupsRollup'])
