from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueID, PerModeSimple, SeasonType


class AllTimeLeadersGrids(Endpoint):
    endpoint = 'alltimeleadersgrids'
    expected_data = {'ASTLeaders': ['PLAYER_ID', 'PLAYER_NAME', 'AST', 'AST_RANK'], 'BLKLeaders': ['PLAYER_ID', 'PLAYER_NAME', 'BLK', 'BLK_RANK'], 'DREBLeaders': ['PLAYER_ID', 'PLAYER_NAME', 'DREB', 'DREB_RANK'], 'FG3ALeaders': ['PLAYER_ID', 'PLAYER_NAME', 'FG3A', 'FG3A_RANK'], 'FG3MLeaders': ['PLAYER_ID', 'PLAYER_NAME', 'FG3M', 'FG3M_RANK'], 'FG3_PCTLeaders': ['PLAYER_ID', 'PLAYER_NAME', 'FG3_PCT', 'FG3_PCT_RANK'], 'FGALeaders': ['PLAYER_ID', 'PLAYER_NAME', 'FGA', 'FGA_RANK'], 'FGMLeaders': ['PLAYER_ID', 'PLAYER_NAME', 'FGM', 'FGM_RANK'], 'FG_PCTLeaders': ['PLAYER_ID', 'PLAYER_NAME', 'FG_PCT', 'FG_PCT_RANK'], 'FTALeaders': ['PLAYER_ID', 'PLAYER_NAME', 'FTA', 'FTA_RANK'], 'FTMLeaders': ['PLAYER_ID', 'PLAYER_NAME', 'FTM', 'FTM_RANK'], 'FT_PCTLeaders': ['PLAYER_ID', 'PLAYER_NAME', 'FT_PCT', 'FT_PCT_RANK'], 'GPLeaders': ['PLAYER_ID', 'PLAYER_NAME', 'GP', 'GP_RANK'], 'OREBLeaders': ['PLAYER_ID', 'PLAYER_NAME', 'OREB', 'OREB_RANK'], 'PFLeaders': ['PLAYER_ID', 'PLAYER_NAME', 'PF', 'PF_RANK'], 'PTSLeaders': ['PLAYER_ID', 'PLAYER_NAME', 'PTS', 'PTS_RANK'], 'REBLeaders': ['PLAYER_ID', 'PLAYER_NAME', 'REB', 'REB_RANK'], 'STLLeaders': ['PLAYER_ID', 'PLAYER_NAME', 'STL', 'STL_RANK'], 'TOVLeaders': ['PLAYER_ID', 'PLAYER_NAME', 'TOV', 'TOV_RANK']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 league_id=LeagueID.default,
                 per_mode_simple=PerModeSimple.default,
                 season_type=SeasonType.default,
                 topx=10,
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
                'SeasonType': season_type,
                'TopX': topx
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
        self.ast_leaders = Endpoint.DataSet(data=data_sets['ASTLeaders'])
        self.blk_leaders = Endpoint.DataSet(data=data_sets['BLKLeaders'])
        self.dreb_leaders = Endpoint.DataSet(data=data_sets['DREBLeaders'])
        self.fg3_a_leaders = Endpoint.DataSet(data=data_sets['FG3ALeaders'])
        self.fg3_m_leaders = Endpoint.DataSet(data=data_sets['FG3MLeaders'])
        self.fg3_pct_leaders = Endpoint.DataSet(data=data_sets['FG3_PCTLeaders'])
        self.fga_leaders = Endpoint.DataSet(data=data_sets['FGALeaders'])
        self.fgm_leaders = Endpoint.DataSet(data=data_sets['FGMLeaders'])
        self.fg_pct_leaders = Endpoint.DataSet(data=data_sets['FG_PCTLeaders'])
        self.fta_leaders = Endpoint.DataSet(data=data_sets['FTALeaders'])
        self.ftm_leaders = Endpoint.DataSet(data=data_sets['FTMLeaders'])
        self.ft_pct_leaders = Endpoint.DataSet(data=data_sets['FT_PCTLeaders'])
        self.g_p_leaders = Endpoint.DataSet(data=data_sets['GPLeaders'])
        self.oreb_leaders = Endpoint.DataSet(data=data_sets['OREBLeaders'])
        self.pf_leaders = Endpoint.DataSet(data=data_sets['PFLeaders'])
        self.pts_leaders = Endpoint.DataSet(data=data_sets['PTSLeaders'])
        self.reb_leaders = Endpoint.DataSet(data=data_sets['REBLeaders'])
        self.stl_leaders = Endpoint.DataSet(data=data_sets['STLLeaders'])
        self.tov_leaders = Endpoint.DataSet(data=data_sets['TOVLeaders'])
