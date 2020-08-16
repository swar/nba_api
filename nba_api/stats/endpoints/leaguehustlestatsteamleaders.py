from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import PerModeTime, Season, SeasonTypeAllStar, ConferenceNullable, DivisionSimpleNullable, LeagueIDNullable, LocationNullable, MonthNullable, OutcomeNullable, PlayerExperienceNullable, PlayerPositionNullable, SeasonSegmentNullable, DivisionNullable


class LeagueHustleStatsTeamLeaders(Endpoint):
    endpoint = 'leaguehustlestatsteamleaders'
    expected_data = {'Table5': ['TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'RANK', 'BOX_OUTS'], 'Table6': ['TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'RANK', 'BOX_OUTS'], 'TeamChargesDrawnLeaders': ['TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'RANK', 'CHARGES_DRAWN'], 'TeamContestedShotsLeaders': ['TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'RANK', 'CONTESTED_SHOTS'], 'TeamDeflectionsLeaders': ['TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'RANK', 'DEFLECTIONS'], 'TeamLooseBallLeaders': ['TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'RANK', 'LOOSE_BALLS_RECOVERED'], 'TeamScreenAssistLeaders': ['TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'RANK', 'SCREEN_ASSISTS']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 per_mode_time=PerModeTime.default,
                 season=Season.default,
                 season_type_all_star=SeasonTypeAllStar.default,
                 college_nullable='',
                 conference_nullable=ConferenceNullable.default,
                 country_nullable='',
                 date_from_nullable='',
                 date_to_nullable='',
                 division_simple_nullable=DivisionSimpleNullable.default,
                 draft_pick_nullable='',
                 draft_year_nullable='',
                 height_nullable='',
                 league_id_nullable=LeagueIDNullable.default,
                 location_nullable=LocationNullable.default,
                 month_nullable=MonthNullable.default,
                 opponent_team_id_nullable='',
                 outcome_nullable=OutcomeNullable.default,
                 po_round_nullable='',
                 player_experience_nullable=PlayerExperienceNullable.default,
                 player_position_nullable=PlayerPositionNullable.default,
                 season_segment_nullable=SeasonSegmentNullable.default,
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
                'PerMode': per_mode_time,
                'Season': season,
                'SeasonType': season_type_all_star,
                'College': college_nullable,
                'Conference': conference_nullable,
                'Country': country_nullable,
                'DateFrom': date_from_nullable,
                'DateTo': date_to_nullable,
                'Division': division_simple_nullable,
                'DraftPick': draft_pick_nullable,
                'DraftYear': draft_year_nullable,
                'Height': height_nullable,
                'LeagueID': league_id_nullable,
                'Location': location_nullable,
                'Month': month_nullable,
                'OpponentTeamID': opponent_team_id_nullable,
                'Outcome': outcome_nullable,
                'PORound': po_round_nullable,
                'PlayerExperience': player_experience_nullable,
                'PlayerPosition': player_position_nullable,
                'SeasonSegment': season_segment_nullable,
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
        self.table5 = Endpoint.DataSet(data=data_sets['Table5'])
        self.table6 = Endpoint.DataSet(data=data_sets['Table6'])
        self.team_charges_drawn_leaders = Endpoint.DataSet(data=data_sets['TeamChargesDrawnLeaders'])
        self.team_contested_shots_leaders = Endpoint.DataSet(data=data_sets['TeamContestedShotsLeaders'])
        self.team_deflections_leaders = Endpoint.DataSet(data=data_sets['TeamDeflectionsLeaders'])
        self.team_loose_ball_leaders = Endpoint.DataSet(data=data_sets['TeamLooseBallLeaders'])
        self.team_screen_assist_leaders = Endpoint.DataSet(data=data_sets['TeamScreenAssistLeaders'])
