from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueID, PerModeSimple, PlayerOrTeamAbbreviation, SeasonTypeAllStar, Season, PlayTypeNullable, TypeGroupingNullable


class SynergyPlayTypes(Endpoint):
    endpoint = 'synergyplaytypes'
    expected_data = {'SynergyPlayType': ['SEASON_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'PLAY_TYPE', 'TYPE_GROUPING', 'PERCENTILE', 'GP', 'POSS_PCT', 'PPP', 'FG_PCT', 'FT_POSS_PCT', 'TOV_POSS_PCT', 'SF_POSS_PCT', 'PLUSONE_POSS_PCT', 'SCORE_POSS_PCT', 'EFG_PCT', 'POSS', 'PTS', 'FGM', 'FGA', 'FGMX']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 league_id=LeagueID.default,
                 per_mode_simple=PerModeSimple.default,
                 player_or_team_abbreviation=PlayerOrTeamAbbreviation.default,
                 season_type_all_star=SeasonTypeAllStar.default,
                 season=Season.default,
                 play_type_nullable=PlayTypeNullable.default,
                 type_grouping_nullable=TypeGroupingNullable.default,
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
                'PlayerOrTeam': player_or_team_abbreviation,
                'SeasonType': season_type_all_star,
                'SeasonYear': season,
                'PlayType': play_type_nullable,
                'TypeGrouping': type_grouping_nullable
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
        self.synergy_play_type = Endpoint.DataSet(data=data_sets['SynergyPlayType'])
