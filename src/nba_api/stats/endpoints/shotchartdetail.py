from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import ContextMeasureSimple, LastNGames, LeagueID, Month, Period, SeasonTypeAllStar, AheadBehindNullable, ClutchTimeNullable, EndPeriodNullable, EndRangeNullable, GameSegmentNullable, LocationNullable, OutcomeNullable, PlayerPositionNullable, PointDiffNullable, PositionNullable, RangeTypeNullable, SeasonNullable, SeasonSegmentNullable, StartPeriodNullable, StartRangeNullable, ConferenceNullable, DivisionNullable


class ShotChartDetail(Endpoint):
    endpoint = 'shotchartdetail'
    expected_data = {'LeagueAverages': ['GRID_TYPE', 'SHOT_ZONE_BASIC', 'SHOT_ZONE_AREA', 'SHOT_ZONE_RANGE', 'FGA', 'FGM', 'FG_PCT'], 'Shot_Chart_Detail': ['GRID_TYPE', 'GAME_ID', 'GAME_EVENT_ID', 'PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_NAME', 'PERIOD', 'MINUTES_REMAINING', 'SECONDS_REMAINING', 'EVENT_TYPE', 'ACTION_TYPE', 'SHOT_TYPE', 'SHOT_ZONE_BASIC', 'SHOT_ZONE_AREA', 'SHOT_ZONE_RANGE', 'SHOT_DISTANCE', 'LOC_X', 'LOC_Y', 'SHOT_ATTEMPTED_FLAG', 'SHOT_MADE_FLAG', 'GAME_DATE', 'HTM', 'VTM']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 team_id,
                 player_id,
                 context_measure_simple=ContextMeasureSimple.default,
                 last_n_games=LastNGames.default,
                 league_id=LeagueID.default,
                 month=Month.default,
                 opponent_team_id=0,
                 period=Period.default,
                 season_type_all_star=SeasonTypeAllStar.default,
                 ahead_behind_nullable=AheadBehindNullable.default,
                 clutch_time_nullable=ClutchTimeNullable.default,
                 context_filter_nullable='',
                 date_from_nullable='',
                 date_to_nullable='',
                 end_period_nullable=EndPeriodNullable.default,
                 end_range_nullable=EndRangeNullable.default,
                 game_id_nullable='',
                 game_segment_nullable=GameSegmentNullable.default,
                 location_nullable=LocationNullable.default,
                 outcome_nullable=OutcomeNullable.default,
                 player_position_nullable=PlayerPositionNullable.default,
                 point_diff_nullable=PointDiffNullable.default,
                 position_nullable=PositionNullable.default,
                 range_type_nullable=RangeTypeNullable.default,
                 rookie_year_nullable=SeasonNullable.default,
                 season_nullable=SeasonNullable.default,
                 season_segment_nullable=SeasonSegmentNullable.default,
                 start_period_nullable=StartPeriodNullable.default,
                 start_range_nullable=StartRangeNullable.default,
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
                'TeamID': team_id,
                'PlayerID': player_id,
                'ContextMeasure': context_measure_simple,
                'LastNGames': last_n_games,
                'LeagueID': league_id,
                'Month': month,
                'OpponentTeamID': opponent_team_id,
                'Period': period,
                'SeasonType': season_type_all_star,
                'AheadBehind': ahead_behind_nullable,
                'ClutchTime': clutch_time_nullable,
                'ContextFilter': context_filter_nullable,
                'DateFrom': date_from_nullable,
                'DateTo': date_to_nullable,
                'EndPeriod': end_period_nullable,
                'EndRange': end_range_nullable,
                'GameID': game_id_nullable,
                'GameSegment': game_segment_nullable,
                'Location': location_nullable,
                'Outcome': outcome_nullable,
                'PlayerPosition': player_position_nullable,
                'PointDiff': point_diff_nullable,
                'Position': position_nullable,
                'RangeType': range_type_nullable,
                'RookieYear': rookie_year_nullable,
                'Season': season_nullable,
                'SeasonSegment': season_segment_nullable,
                'StartPeriod': start_period_nullable,
                'StartRange': start_range_nullable,
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
        self.league_averages = Endpoint.DataSet(data=data_sets['LeagueAverages'])
        self.shot_chart_detail = Endpoint.DataSet(data=data_sets['Shot_Chart_Detail'])
