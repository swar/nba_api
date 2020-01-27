from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import GameSegmentNullable, LastNGamesNullable, LeagueIDNullable, LocationNullable, MonthNullable, OutcomeNullable, PerModeSimpleNullable, PeriodNullable, SeasonNullable, SeasonSegmentNullable, SeasonTypeNullable, ShotClockRangeNullable, ConferenceNullable, DivisionNullable


class TeamGameLogs(Endpoint):
    endpoint = 'teamgamelogs'
    expected_data = {'TeamGameLogs': ['SEASON_YEAR', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'GAME_ID', 'GAME_DATE', 'MATCHUP', 'WL', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'GP_RANK', 'W_RANK', 'L_RANK', 'W_PCT_RANK', 'MIN_RANK', 'FGM_RANK', 'FGA_RANK', 'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 'FTM_RANK', 'FTA_RANK', 'FT_PCT_RANK', 'OREB_RANK', 'DREB_RANK', 'REB_RANK', 'AST_RANK', 'TOV_RANK', 'STL_RANK', 'BLK_RANK', 'BLKA_RANK', 'PF_RANK', 'PFD_RANK', 'PTS_RANK', 'PLUS_MINUS_RANK']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 date_from_nullable='',
                 date_to_nullable='',
                 game_segment_nullable=GameSegmentNullable.default,
                 last_n_games_nullable=LastNGamesNullable.default,
                 league_id_nullable=LeagueIDNullable.default,
                 location_nullable=LocationNullable.default,
                 measure_type_player_game_logs_nullable=None,
                 month_nullable=MonthNullable.default,
                 opp_team_id_nullable=None,
                 outcome_nullable=OutcomeNullable.default,
                 po_round_nullable='',
                 per_mode_simple_nullable=PerModeSimpleNullable.default,
                 period_nullable=PeriodNullable.default,
                 player_id_nullable='',
                 season_nullable=SeasonNullable.default,
                 season_segment_nullable=SeasonSegmentNullable.default,
                 season_type_nullable=SeasonTypeNullable.default,
                 shot_clock_range_nullable=ShotClockRangeNullable.default,
                 team_id_nullable='',
                 vs_conference_nullable=ConferenceNullable.default,
                 vs_division_nullable=DivisionNullable.default,
                 proxy=None,
                 headers=None,
                 timeout=30,
                 get_request=True):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
                'DateFrom': date_from_nullable,
                'DateTo': date_to_nullable,
                'GameSegment': game_segment_nullable,
                'LastNGames': last_n_games_nullable,
                'LeagueID': league_id_nullable,
                'Location': location_nullable,
                'MeasureType': measure_type_player_game_logs_nullable,
                'Month': month_nullable,
                'OppTeamID': opp_team_id_nullable,
                'Outcome': outcome_nullable,
                'PORound': po_round_nullable,
                'PerMode': per_mode_simple_nullable,
                'Period': period_nullable,
                'PlayerID': player_id_nullable,
                'Season': season_nullable,
                'SeasonSegment': season_segment_nullable,
                'SeasonType': season_type_nullable,
                'ShotClockRange': shot_clock_range_nullable,
                'TeamID': team_id_nullable,
                'VsConference': vs_conference_nullable,
                'VsDivision': vs_division_nullable
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
        self.team_game_logs = Endpoint.DataSet(data=data_sets['TeamGameLogs'])
