from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP


class BoxScoreSummaryV2(Endpoint):
    endpoint = 'boxscoresummaryv2'
    expected_data = {'AvailableVideo': ['GAME_ID', 'VIDEO_AVAILABLE_FLAG', 'PT_AVAILABLE', 'PT_XYZ_AVAILABLE', 'WH_STATUS', 'HUSTLE_STATUS', 'HISTORICAL_STATUS'], 'GameInfo': ['GAME_DATE', 'ATTENDANCE', 'GAME_TIME'], 'GameSummary': ['GAME_DATE_EST', 'GAME_SEQUENCE', 'GAME_ID', 'GAME_STATUS_ID', 'GAME_STATUS_TEXT', 'GAMECODE', 'HOME_TEAM_ID', 'VISITOR_TEAM_ID', 'SEASON', 'LIVE_PERIOD', 'LIVE_PC_TIME', 'NATL_TV_BROADCASTER_ABBREVIATION', 'LIVE_PERIOD_TIME_BCAST', 'WH_STATUS'], 'InactivePlayers': ['PLAYER_ID', 'FIRST_NAME', 'LAST_NAME', 'JERSEY_NUM', 'TEAM_ID', 'TEAM_CITY', 'TEAM_NAME', 'TEAM_ABBREVIATION'], 'LastMeeting': ['GAME_ID', 'LAST_GAME_ID', 'LAST_GAME_DATE_EST', 'LAST_GAME_HOME_TEAM_ID', 'LAST_GAME_HOME_TEAM_CITY', 'LAST_GAME_HOME_TEAM_NAME', 'LAST_GAME_HOME_TEAM_ABBREVIATION', 'LAST_GAME_HOME_TEAM_POINTS', 'LAST_GAME_VISITOR_TEAM_ID', 'LAST_GAME_VISITOR_TEAM_CITY', 'LAST_GAME_VISITOR_TEAM_NAME', 'LAST_GAME_VISITOR_TEAM_CITY1', 'LAST_GAME_VISITOR_TEAM_POINTS'], 'LineScore': ['GAME_DATE_EST', 'GAME_SEQUENCE', 'GAME_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_CITY_NAME', 'TEAM_NICKNAME', 'TEAM_WINS_LOSSES', 'PTS_QTR1', 'PTS_QTR2', 'PTS_QTR3', 'PTS_QTR4', 'PTS_OT1', 'PTS_OT2', 'PTS_OT3', 'PTS_OT4', 'PTS_OT5', 'PTS_OT6', 'PTS_OT7', 'PTS_OT8', 'PTS_OT9', 'PTS_OT10', 'PTS'], 'Officials': ['OFFICIAL_ID', 'FIRST_NAME', 'LAST_NAME', 'JERSEY_NUM'], 'OtherStats': ['LEAGUE_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_CITY', 'PTS_PAINT', 'PTS_2ND_CHANCE', 'PTS_FB', 'LARGEST_LEAD', 'LEAD_CHANGES', 'TIMES_TIED', 'TEAM_TURNOVERS', 'TOTAL_TURNOVERS', 'TEAM_REBOUNDS', 'PTS_OFF_TO'], 'SeasonSeries': ['GAME_ID', 'HOME_TEAM_ID', 'VISITOR_TEAM_ID', 'GAME_DATE_EST', 'HOME_TEAM_WINS', 'HOME_TEAM_LOSSES', 'SERIES_LEADER']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 game_id,
                 proxy=None,
                 headers=None,
                 timeout=30,
                 get_request=True):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
                'GameID': game_id
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
        self.available_video = Endpoint.DataSet(data=data_sets['AvailableVideo'])
        self.game_info = Endpoint.DataSet(data=data_sets['GameInfo'])
        self.game_summary = Endpoint.DataSet(data=data_sets['GameSummary'])
        self.inactive_players = Endpoint.DataSet(data=data_sets['InactivePlayers'])
        self.last_meeting = Endpoint.DataSet(data=data_sets['LastMeeting'])
        self.line_score = Endpoint.DataSet(data=data_sets['LineScore'])
        self.officials = Endpoint.DataSet(data=data_sets['Officials'])
        self.other_stats = Endpoint.DataSet(data=data_sets['OtherStats'])
        self.season_series = Endpoint.DataSet(data=data_sets['SeasonSeries'])
