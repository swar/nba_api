from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import (
    LastNGames,
    Month,
    PerModeSimple,
    PlayerOrTeam,
    PtMeasureType,
    Season,
    SeasonTypeAllStar,
    ConferenceNullable,
    DivisionSimpleNullable,
    GameScopeSimpleNullable,
    LeagueIDNullable,
    LocationNullable,
    OutcomeNullable,
    PlayerExperienceNullable,
    PlayerPositionAbbreviationNullable,
    SeasonSegmentNullable,
    StarterBenchNullable,
    DivisionNullable,
)


class LeagueDashPtStats(Endpoint):
    endpoint = "leaguedashptstats"
    expected_data = {
        "LeagueDashPtStats": [
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "GP",
            "W",
            "L",
            "MIN",
            "DIST_FEET",
            "DIST_MILES",
            "DIST_MILES_OFF",
            "DIST_MILES_DEF",
            "AVG_SPEED",
            "AVG_SPEED_OFF",
            "AVG_SPEED_DEF",
        ]
    }

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(
        self,
        last_n_games=LastNGames.default,
        month=Month.default,
        opponent_team_id=0,
        per_mode_simple=PerModeSimple.default,
        player_or_team=PlayerOrTeam.default,
        pt_measure_type=PtMeasureType.default,
        season=Season.default,
        season_type_all_star=SeasonTypeAllStar.default,
        college_nullable="",
        conference_nullable=ConferenceNullable.default,
        country_nullable="",
        date_from_nullable="",
        date_to_nullable="",
        division_simple_nullable=DivisionSimpleNullable.default,
        draft_pick_nullable="",
        draft_year_nullable="",
        game_scope_simple_nullable=GameScopeSimpleNullable.default,
        height_nullable="",
        league_id_nullable=LeagueIDNullable.default,
        location_nullable=LocationNullable.default,
        outcome_nullable=OutcomeNullable.default,
        po_round_nullable="",
        player_experience_nullable=PlayerExperienceNullable.default,
        player_position_abbreviation_nullable=PlayerPositionAbbreviationNullable.default,
        season_segment_nullable=SeasonSegmentNullable.default,
        starter_bench_nullable=StarterBenchNullable.default,
        team_id_nullable="",
        vs_conference_nullable=ConferenceNullable.default,
        vs_division_nullable=DivisionNullable.default,
        weight_nullable="",
        proxy=None,
        headers=None,
        timeout=30,
        get_request=True,
    ):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
            "LastNGames": last_n_games,
            "Month": month,
            "OpponentTeamID": opponent_team_id,
            "PerMode": per_mode_simple,
            "PlayerOrTeam": player_or_team,
            "PtMeasureType": pt_measure_type,
            "Season": season,
            "SeasonType": season_type_all_star,
            "College": college_nullable,
            "Conference": conference_nullable,
            "Country": country_nullable,
            "DateFrom": date_from_nullable,
            "DateTo": date_to_nullable,
            "Division": division_simple_nullable,
            "DraftPick": draft_pick_nullable,
            "DraftYear": draft_year_nullable,
            "GameScope": game_scope_simple_nullable,
            "Height": height_nullable,
            "LeagueID": league_id_nullable,
            "Location": location_nullable,
            "Outcome": outcome_nullable,
            "PORound": po_round_nullable,
            "PlayerExperience": player_experience_nullable,
            "PlayerPosition": player_position_abbreviation_nullable,
            "SeasonSegment": season_segment_nullable,
            "StarterBench": starter_bench_nullable,
            "TeamID": team_id_nullable,
            "VsConference": vs_conference_nullable,
            "VsDivision": vs_division_nullable,
            "Weight": weight_nullable,
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
        self.data_sets = [
            Endpoint.DataSet(data=data_set)
            for data_set_name, data_set in data_sets.items()
        ]
        self.league_dash_pt_stats = Endpoint.DataSet(
            data=data_sets["LeagueDashPtStats"]
        )
