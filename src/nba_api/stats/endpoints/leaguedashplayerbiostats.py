from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import (
    LeagueID,
    PerModeSimple,
    Season,
    SeasonTypeAllStar,
    ConferenceNullable,
    DivisionSimpleNullable,
    GameScopeSimpleNullable,
    GameSegmentNullable,
    LastNGamesNullable,
    LocationNullable,
    MonthNullable,
    OutcomeNullable,
    PeriodNullable,
    PlayerExperienceNullable,
    PlayerPositionAbbreviationNullable,
    SeasonSegmentNullable,
    ShotClockRangeNullable,
    StarterBenchNullable,
    DivisionNullable,
)


class LeagueDashPlayerBioStats(Endpoint):
    endpoint = "leaguedashplayerbiostats"
    expected_data = {
        "LeagueDashPlayerBioStats": [
            "PLAYER_ID",
            "PLAYER_NAME",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "AGE",
            "PLAYER_HEIGHT",
            "PLAYER_HEIGHT_INCHES",
            "PLAYER_WEIGHT",
            "COLLEGE",
            "COUNTRY",
            "DRAFT_YEAR",
            "DRAFT_ROUND",
            "DRAFT_NUMBER",
            "GP",
            "PTS",
            "REB",
            "AST",
            "NET_RATING",
            "OREB_PCT",
            "DREB_PCT",
            "USG_PCT",
            "TS_PCT",
            "AST_PCT",
        ]
    }

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(
        self,
        league_id=LeagueID.default,
        per_mode_simple=PerModeSimple.default,
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
        game_segment_nullable=GameSegmentNullable.default,
        height_nullable="",
        last_n_games_nullable=LastNGamesNullable.default,
        location_nullable=LocationNullable.default,
        month_nullable=MonthNullable.default,
        opponent_team_id_nullable="",
        outcome_nullable=OutcomeNullable.default,
        po_round_nullable="",
        period_nullable=PeriodNullable.default,
        player_experience_nullable=PlayerExperienceNullable.default,
        player_position_abbreviation_nullable=PlayerPositionAbbreviationNullable.default,
        season_segment_nullable=SeasonSegmentNullable.default,
        shot_clock_range_nullable=ShotClockRangeNullable.default,
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
            "LeagueID": league_id,
            "PerMode": per_mode_simple,
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
            "GameSegment": game_segment_nullable,
            "Height": height_nullable,
            "LastNGames": last_n_games_nullable,
            "Location": location_nullable,
            "Month": month_nullable,
            "OpponentTeamID": opponent_team_id_nullable,
            "Outcome": outcome_nullable,
            "PORound": po_round_nullable,
            "Period": period_nullable,
            "PlayerExperience": player_experience_nullable,
            "PlayerPosition": player_position_abbreviation_nullable,
            "SeasonSegment": season_segment_nullable,
            "ShotClockRange": shot_clock_range_nullable,
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
        self.league_dash_player_bio_stats = Endpoint.DataSet(
            data=data_sets["LeagueDashPlayerBioStats"]
        )
