from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import (
    DefenseCategory,
    LeagueID,
    PerModeSimple,
    Season,
    SeasonTypeAllStar,
    ConferenceNullable,
    DivisionNullable,
    GameSegmentNullable,
    LastNGamesNullable,
    LocationNullable,
    MonthNullable,
    OutcomeNullable,
    PeriodNullable,
    SeasonSegmentNullable,
)


class LeagueDashPtTeamDefend(Endpoint):
    endpoint = "leaguedashptteamdefend"
    expected_data = {
        "LeagueDashPtTeamDefend": [
            "TEAM_ID",
            "TEAM_NAME",
            "TEAM_ABBREVIATION",
            "GP",
            "G",
            "FREQ",
            "D_FGM",
            "D_FGA",
            "D_FG_PCT",
            "NORMAL_FG_PCT",
            "PCT_PLUSMINUS",
        ]
    }

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(
        self,
        defense_category=DefenseCategory.default,
        league_id=LeagueID.default,
        per_mode_simple=PerModeSimple.default,
        season=Season.default,
        season_type_all_star=SeasonTypeAllStar.default,
        conference_nullable=ConferenceNullable.default,
        date_from_nullable="",
        date_to_nullable="",
        division_nullable=DivisionNullable.default,
        game_segment_nullable=GameSegmentNullable.default,
        last_n_games_nullable=LastNGamesNullable.default,
        location_nullable=LocationNullable.default,
        month_nullable=MonthNullable.default,
        opponent_team_id_nullable="",
        outcome_nullable=OutcomeNullable.default,
        po_round_nullable="",
        period_nullable=PeriodNullable.default,
        season_segment_nullable=SeasonSegmentNullable.default,
        team_id_nullable="",
        vs_conference_nullable=ConferenceNullable.default,
        vs_division_nullable=DivisionNullable.default,
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
            "DefenseCategory": defense_category,
            "LeagueID": league_id,
            "PerMode": per_mode_simple,
            "Season": season,
            "SeasonType": season_type_all_star,
            "Conference": conference_nullable,
            "DateFrom": date_from_nullable,
            "DateTo": date_to_nullable,
            "Division": division_nullable,
            "GameSegment": game_segment_nullable,
            "LastNGames": last_n_games_nullable,
            "Location": location_nullable,
            "Month": month_nullable,
            "OpponentTeamID": opponent_team_id_nullable,
            "Outcome": outcome_nullable,
            "PORound": po_round_nullable,
            "Period": period_nullable,
            "SeasonSegment": season_segment_nullable,
            "TeamID": team_id_nullable,
            "VsConference": vs_conference_nullable,
            "VsDivision": vs_division_nullable,
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
        self.league_dash_pt_team_defend = Endpoint.DataSet(
            data=data_sets["LeagueDashPtTeamDefend"]
        )
