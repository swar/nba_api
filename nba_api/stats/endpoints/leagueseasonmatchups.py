from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueID, Season, SeasonType, OutcomeNullable, PerModeSimpleNullable


class LeagueSeasonMatchups(Endpoint):
    endpoint = 'leagueseasonmatchups'
    expected_data = {'SeasonMatchups': ['OFF_TEAM_ID', 'OFF_TEAM_ABBREVIATION', 'OFF_TEAM_CITY', 'OFF_TEAM_NICKNAME', 'OFF_PLAYER_ID', 'OFF_PLAYER_NAME', 'DEF_TEAM_ID', 'DEF_TEAM_ABBREVIATION', 'DEF_TEAM_CITY', 'DEF_TEAM_NICKNAME', 'DEF_PLAYER_ID', 'DEF_PLAYER_NAME', 'GP', 'POSS', 'OFF_MATCHUP_PCT', 'PLAYER_PTS', 'PLAYER_PTS_DIFF', 'TEAM_PTS', 'TEAM_PTS_DIFF', 'AST', 'TOV', 'BLK', 'HELP_BLK', 'HELP_BLK_REC', 'FGM', 'FGA', 'FGA_DIFF', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'SFL', 'DEF_FOULS', 'OFF_FOULS']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 league_id=LeagueID.default,
                 season=Season.default,
                 season_type_playoffs=SeasonType.default,
                 date_from_nullable='',
                 date_to_nullable='',
                 def_player_id_nullable='',
                 def_team_id_nullable=None,
                 off_player_id_nullable='',
                 off_team_id_nullable=None,
                 outcome_nullable=OutcomeNullable.default,
                 po_round_nullable='',
                 per_mode_simple_nullable=PerModeSimpleNullable.default,
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
                'Season': season,
                'SeasonType': season_type_playoffs,
                'DateFrom': date_from_nullable,
                'DateTo': date_to_nullable,
                'DefPlayerID': def_player_id_nullable,
                'DefTeamID': def_team_id_nullable,
                'OffPlayerID': off_player_id_nullable,
                'OffTeamID': off_team_id_nullable,
                'Outcome': outcome_nullable,
                'PORound': po_round_nullable,
                'PerMode': per_mode_simple_nullable
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
        self.season_matchups = Endpoint.DataSet(data=data_sets['SeasonMatchups'])
