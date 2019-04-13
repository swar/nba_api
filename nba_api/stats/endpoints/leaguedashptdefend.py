from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import DefenseCategory, LeagueID, PerModeSimple, Season, SeasonTypeAllStar, ConferenceNullable, DivisionNullable, GameSegmentNullable, LastNGamesNullable, LocationNullable, MonthNullable, OutcomeNullable, PeriodNullable, PlayerExperienceNullable, PlayerPositionNullable, SeasonSegmentNullable, StarterBenchNullable


class LeagueDashPtDefend(Endpoint):
    endpoint = 'leaguedashptdefend'
    expected_data = {'LeagueDashPTDefend': ['CLOSE_DEF_PERSON_ID', 'PLAYER_NAME', 'PLAYER_LAST_TEAM_ID', 'PLAYER_LAST_TEAM_ABBREVIATION', 'PLAYER_POSITION', 'AGE', 'GP', 'G', 'FREQ', 'D_FGM', 'D_FGA', 'D_FG_PCT', 'NORMAL_FG_PCT', 'PCT_PLUSMINUS']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 defense_category=DefenseCategory.default,
                 league_id=LeagueID.default,
                 per_mode_simple=PerModeSimple.default,
                 season=Season.default,
                 season_type_all_star=SeasonTypeAllStar.default,
                 college_nullable='',
                 conference_nullable=ConferenceNullable.default,
                 country_nullable='',
                 date_from_nullable='',
                 date_to_nullable='',
                 division_nullable=DivisionNullable.default,
                 draft_pick_nullable='',
                 draft_year_nullable='',
                 game_segment_nullable=GameSegmentNullable.default,
                 height_nullable='',
                 last_n_games_nullable=LastNGamesNullable.default,
                 location_nullable=LocationNullable.default,
                 month_nullable=MonthNullable.default,
                 opponent_team_id_nullable='',
                 outcome_nullable=OutcomeNullable.default,
                 po_round_nullable='',
                 period_nullable=PeriodNullable.default,
                 player_experience_nullable=PlayerExperienceNullable.default,
                 player_id_nullable='',
                 player_position_nullable=PlayerPositionNullable.default,
                 season_segment_nullable=SeasonSegmentNullable.default,
                 starter_bench_nullable=StarterBenchNullable.default,
                 team_id_nullable='',
                 vs_conference_nullable=ConferenceNullable.default,
                 vs_division_nullable=DivisionNullable.default,
                 weight_nullable='',
                 proxy=None,
                 headers=None,
                 timeout=30,
                 get_request=True):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
                'DefenseCategory': defense_category,
                'LeagueID': league_id,
                'PerMode': per_mode_simple,
                'Season': season,
                'SeasonType': season_type_all_star,
                'College': college_nullable,
                'Conference': conference_nullable,
                'Country': country_nullable,
                'DateFrom': date_from_nullable,
                'DateTo': date_to_nullable,
                'Division': division_nullable,
                'DraftPick': draft_pick_nullable,
                'DraftYear': draft_year_nullable,
                'GameSegment': game_segment_nullable,
                'Height': height_nullable,
                'LastNGames': last_n_games_nullable,
                'Location': location_nullable,
                'Month': month_nullable,
                'OpponentTeamID': opponent_team_id_nullable,
                'Outcome': outcome_nullable,
                'PORound': po_round_nullable,
                'Period': period_nullable,
                'PlayerExperience': player_experience_nullable,
                'PlayerID': player_id_nullable,
                'PlayerPosition': player_position_nullable,
                'SeasonSegment': season_segment_nullable,
                'StarterBench': starter_bench_nullable,
                'TeamID': team_id_nullable,
                'VsConference': vs_conference_nullable,
                'VsDivision': vs_division_nullable,
                'Weight': weight_nullable
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
        self.league_dash_p_tdefend = Endpoint.DataSet(data=data_sets['LeagueDashPTDefend'])
