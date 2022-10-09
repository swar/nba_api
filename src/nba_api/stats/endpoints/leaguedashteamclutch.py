from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import AheadBehind, ClutchTime, LastNGames, MeasureTypeDetailedDefense, Month, PaceAdjust, PerModeDetailed, Period, PlusMinus, PointDiff, Rank, Season, SeasonTypeAllStar, ConferenceNullable, DivisionSimpleNullable, GameScopeSimpleNullable, GameSegmentNullable, LeagueIDNullable, LocationNullable, OutcomeNullable, PlayerExperienceNullable, PlayerPositionAbbreviationNullable, SeasonSegmentNullable, ShotClockRangeNullable, StarterBenchNullable, DivisionNullable


class LeagueDashTeamClutch(Endpoint):
    endpoint = 'leaguedashteamclutch'
    expected_data = {'LeagueDashTeamClutch': ['TEAM_ID', 'TEAM_NAME', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'GP_RANK', 'W_RANK', 'L_RANK', 'W_PCT_RANK', 'MIN_RANK', 'FGM_RANK', 'FGA_RANK', 'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 'FTM_RANK', 'FTA_RANK', 'FT_PCT_RANK', 'OREB_RANK', 'DREB_RANK', 'REB_RANK', 'AST_RANK', 'TOV_RANK', 'STL_RANK', 'BLK_RANK', 'BLKA_RANK', 'PF_RANK', 'PFD_RANK', 'PTS_RANK', 'PLUS_MINUS_RANK', 'CFID', 'CFPARAMS']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 ahead_behind=AheadBehind.default,
                 clutch_time=ClutchTime.default,
                 last_n_games=LastNGames.default,
                 measure_type_detailed_defense=MeasureTypeDetailedDefense.default,
                 month=Month.default,
                 opponent_team_id=0,
                 pace_adjust=PaceAdjust.default,
                 per_mode_detailed=PerModeDetailed.default,
                 period=Period.default,
                 plus_minus=PlusMinus.default,
                 point_diff=PointDiff.default,
                 rank=Rank.default,
                 season=Season.default,
                 season_type_all_star=SeasonTypeAllStar.default,
                 conference_nullable=ConferenceNullable.default,
                 date_from_nullable='',
                 date_to_nullable='',
                 division_simple_nullable=DivisionSimpleNullable.default,
                 game_scope_simple_nullable=GameScopeSimpleNullable.default,
                 game_segment_nullable=GameSegmentNullable.default,
                 league_id_nullable=LeagueIDNullable.default,
                 location_nullable=LocationNullable.default,
                 outcome_nullable=OutcomeNullable.default,
                 po_round_nullable='',
                 player_experience_nullable=PlayerExperienceNullable.default,
                 player_position_abbreviation_nullable=PlayerPositionAbbreviationNullable.default,
                 season_segment_nullable=SeasonSegmentNullable.default,
                 shot_clock_range_nullable=ShotClockRangeNullable.default,
                 starter_bench_nullable=StarterBenchNullable.default,
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
                'AheadBehind': ahead_behind,
                'ClutchTime': clutch_time,
                'LastNGames': last_n_games,
                'MeasureType': measure_type_detailed_defense,
                'Month': month,
                'OpponentTeamID': opponent_team_id,
                'PaceAdjust': pace_adjust,
                'PerMode': per_mode_detailed,
                'Period': period,
                'PlusMinus': plus_minus,
                'PointDiff': point_diff,
                'Rank': rank,
                'Season': season,
                'SeasonType': season_type_all_star,
                'Conference': conference_nullable,
                'DateFrom': date_from_nullable,
                'DateTo': date_to_nullable,
                'Division': division_simple_nullable,
                'GameScope': game_scope_simple_nullable,
                'GameSegment': game_segment_nullable,
                'LeagueID': league_id_nullable,
                'Location': location_nullable,
                'Outcome': outcome_nullable,
                'PORound': po_round_nullable,
                'PlayerExperience': player_experience_nullable,
                'PlayerPosition': player_position_abbreviation_nullable,
                'SeasonSegment': season_segment_nullable,
                'ShotClockRange': shot_clock_range_nullable,
                'StarterBench': starter_bench_nullable,
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
        self.league_dash_team_clutch = Endpoint.DataSet(data=data_sets['LeagueDashTeamClutch'])
