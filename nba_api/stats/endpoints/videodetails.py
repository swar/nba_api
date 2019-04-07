from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import ContextMeasureDetailed, EndPeriod, EndRange, LastNGames, LeagueID, Month, Period, RangeType, Season, SeasonTypeAllStar, StartPeriod, StartRange, AheadBehindNullable, ClutchTimeNullable, GameSegmentNullable, LocationNullable, OutcomeNullable, PointDiffNullable, PositionNullable, SeasonNullable, SeasonSegmentNullable, ConferenceNullable, DivisionNullable


class VideoDetails(Endpoint):
    endpoint = 'videodetails'
    expected_data = {}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 team_id,
                 player_id,
                 game_id,
                 context_measure_detailed=ContextMeasureDetailed.default,
                 end_period=EndPeriod.default,
                 end_range=EndRange.default,
                 last_n_games=LastNGames.default,
                 league_id=LeagueID.default,
                 month=Month.default,
                 opponent_team_id=0,
                 period=Period.default,
                 range_type=RangeType.default,
                 season=Season.default,
                 season_type_all_star=SeasonTypeAllStar.default,
                 start_period=StartPeriod.default,
                 start_range=StartRange.default,
                 ahead_behind_nullable=AheadBehindNullable.default,
                 clutch_time_nullable=ClutchTimeNullable.default,
                 context_filter_nullable='',
                 date_from_nullable='',
                 date_to_nullable='',
                 game_segment_nullable=GameSegmentNullable.default,
                 location_nullable=LocationNullable.default,
                 outcome_nullable=OutcomeNullable.default,
                 point_diff_nullable=PointDiffNullable.default,
                 position_nullable=PositionNullable.default,
                 rookie_year_nullable=SeasonNullable.default,
                 season_segment_nullable=SeasonSegmentNullable.default,
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
                'GameID': game_id,
                'ContextMeasure': context_measure_detailed,
                'EndPeriod': end_period,
                'EndRange': end_range,
                'LastNGames': last_n_games,
                'LeagueID': league_id,
                'Month': month,
                'OpponentTeamID': opponent_team_id,
                'Period': period,
                'RangeType': range_type,
                'Season': season,
                'SeasonType': season_type_all_star,
                'StartPeriod': start_period,
                'StartRange': start_range,
                'AheadBehind': ahead_behind_nullable,
                'ClutchTime': clutch_time_nullable,
                'ContextFilter': context_filter_nullable,
                'DateFrom': date_from_nullable,
                'DateTo': date_to_nullable,
                'GameSegment': game_segment_nullable,
                'Location': location_nullable,
                'Outcome': outcome_nullable,
                'PointDiff': point_diff_nullable,
                'Position': position_nullable,
                'RookieYear': rookie_year_nullable,
                'SeasonSegment': season_segment_nullable,
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

