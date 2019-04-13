from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import DayOffset, GameDate, LeagueID


class Scoreboard(Endpoint):
    endpoint = 'scoreboard'
    expected_data = {'Available': ['GAME_ID', 'PT_AVAILABLE'], 'EastConfStandingsByDay': ['TEAM_ID', 'LEAGUE_ID', 'SEASON_ID', 'STANDINGSDATE', 'CONFERENCE', 'TEAM', 'G', 'W', 'L', 'W_PCT', 'HOME_RECORD', 'ROAD_RECORD'], 'GameHeader': ['GAME_DATE_EST', 'GAME_SEQUENCE', 'GAME_ID', 'GAME_STATUS_ID', 'GAME_STATUS_TEXT', 'GAMECODE', 'HOME_TEAM_ID', 'VISITOR_TEAM_ID', 'SEASON', 'LIVE_PERIOD', 'LIVE_PC_TIME', 'NATL_TV_BROADCASTER_ABBREVIATION', 'LIVE_PERIOD_TIME_BCAST', 'WH_STATUS'], 'LastMeeting': ['GAME_ID', 'LAST_GAME_ID', 'LAST_GAME_DATE_EST', 'LAST_GAME_HOME_TEAM_ID', 'LAST_GAME_HOME_TEAM_CITY', 'LAST_GAME_HOME_TEAM_NAME', 'LAST_GAME_HOME_TEAM_ABBREVIATION', 'LAST_GAME_HOME_TEAM_POINTS', 'LAST_GAME_VISITOR_TEAM_ID', 'LAST_GAME_VISITOR_TEAM_CITY', 'LAST_GAME_VISITOR_TEAM_NAME', 'LAST_GAME_VISITOR_TEAM_CITY1', 'LAST_GAME_VISITOR_TEAM_POINTS'], 'LineScore': ['GAME_DATE_EST', 'GAME_SEQUENCE', 'GAME_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_CITY_NAME', 'TEAM_WINS_LOSSES', 'PTS_QTR1', 'PTS_QTR2', 'PTS_QTR3', 'PTS_QTR4', 'PTS_OT1', 'PTS_OT2', 'PTS_OT3', 'PTS_OT4', 'PTS_OT5', 'PTS_OT6', 'PTS_OT7', 'PTS_OT8', 'PTS_OT9', 'PTS_OT10', 'PTS', 'FG_PCT', 'FT_PCT', 'FG3_PCT', 'AST', 'REB', 'TOV'], 'SeriesStandings': ['GAME_ID', 'HOME_TEAM_ID', 'VISITOR_TEAM_ID', 'GAME_DATE_EST', 'HOME_TEAM_WINS', 'HOME_TEAM_LOSSES', 'SERIES_LEADER'], 'WestConfStandingsByDay': ['TEAM_ID', 'LEAGUE_ID', 'SEASON_ID', 'STANDINGSDATE', 'CONFERENCE', 'TEAM', 'G', 'W', 'L', 'W_PCT', 'HOME_RECORD', 'ROAD_RECORD']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 day_offset=DayOffset.default,
                 game_date=GameDate.default,
                 league_id=LeagueID.default,
                 proxy=None,
                 headers=None,
                 timeout=30,
                 get_request=True):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
                'DayOffset': day_offset,
                'GameDate': game_date,
                'LeagueID': league_id
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
        self.available = Endpoint.DataSet(data=data_sets['Available'])
        self.east_conf_standings_by_day = Endpoint.DataSet(data=data_sets['EastConfStandingsByDay'])
        self.game_header = Endpoint.DataSet(data=data_sets['GameHeader'])
        self.last_meeting = Endpoint.DataSet(data=data_sets['LastMeeting'])
        self.line_score = Endpoint.DataSet(data=data_sets['LineScore'])
        self.series_standings = Endpoint.DataSet(data=data_sets['SeriesStandings'])
        self.west_conf_standings_by_day = Endpoint.DataSet(data=data_sets['WestConfStandingsByDay'])
