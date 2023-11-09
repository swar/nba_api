from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import (
    LastNGames,
    LeagueID,
    Month,
    PerModeSimple,
    Period,
    Season,
    SeasonTypeAllStar,
    GameSegmentNullable,
    LocationNullable,
    OutcomeNullable,
    SeasonSegmentNullable,
    ConferenceNullable,
    DivisionNullable,
)


class TeamDashPtShots(Endpoint):
    endpoint = "teamdashptshots"
    expected_data = {
        "ClosestDefender10ftPlusShooting": [
            "TEAM_ID",
            "TEAM_NAME",
            "SORT_ORDER",
            "G",
            "CLOSE_DEF_DIST_RANGE",
            "FGA_FREQUENCY",
            "FGM",
            "FGA",
            "FG_PCT",
            "EFG_PCT",
            "FG2A_FREQUENCY",
            "FG2M",
            "FG2A",
            "FG2_PCT",
            "FG3A_FREQUENCY",
            "FG3M",
            "FG3A",
            "FG3_PCT",
        ],
        "ClosestDefenderShooting": [
            "TEAM_ID",
            "TEAM_NAME",
            "SORT_ORDER",
            "G",
            "CLOSE_DEF_DIST_RANGE",
            "FGA_FREQUENCY",
            "FGM",
            "FGA",
            "FG_PCT",
            "EFG_PCT",
            "FG2A_FREQUENCY",
            "FG2M",
            "FG2A",
            "FG2_PCT",
            "FG3A_FREQUENCY",
            "FG3M",
            "FG3A",
            "FG3_PCT",
        ],
        "DribbleShooting": [
            "TEAM_ID",
            "TEAM_NAME",
            "SORT_ORDER",
            "G",
            "DRIBBLE_RANGE",
            "FGA_FREQUENCY",
            "FGM",
            "FGA",
            "FG_PCT",
            "EFG_PCT",
            "FG2A_FREQUENCY",
            "FG2M",
            "FG2A",
            "FG2_PCT",
            "FG3A_FREQUENCY",
            "FG3M",
            "FG3A",
            "FG3_PCT",
        ],
        "GeneralShooting": [
            "TEAM_ID",
            "TEAM_NAME",
            "SORT_ORDER",
            "G",
            "SHOT_TYPE",
            "FGA_FREQUENCY",
            "FGM",
            "FGA",
            "FG_PCT",
            "EFG_PCT",
            "FG2A_FREQUENCY",
            "FG2M",
            "FG2A",
            "FG2_PCT",
            "FG3A_FREQUENCY",
            "FG3M",
            "FG3A",
            "FG3_PCT",
        ],
        "ShotClockShooting": [
            "TEAM_ID",
            "TEAM_NAME",
            "SORT_ORDER",
            "G",
            "SHOT_CLOCK_RANGE",
            "FGA_FREQUENCY",
            "FGM",
            "FGA",
            "FG_PCT",
            "EFG_PCT",
            "FG2A_FREQUENCY",
            "FG2M",
            "FG2A",
            "FG2_PCT",
            "FG3A_FREQUENCY",
            "FG3M",
            "FG3A",
            "FG3_PCT",
        ],
        "TouchTimeShooting": [
            "TEAM_ID",
            "TEAM_NAME",
            "SORT_ORDER",
            "G",
            "TOUCH_TIME_RANGE",
            "FGA_FREQUENCY",
            "FGM",
            "FGA",
            "FG_PCT",
            "EFG_PCT",
            "FG2A_FREQUENCY",
            "FG2M",
            "FG2A",
            "FG2_PCT",
            "FG3A_FREQUENCY",
            "FG3M",
            "FG3A",
            "FG3_PCT",
        ],
    }

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(
        self,
        team_id,
        last_n_games=LastNGames.default,
        league_id=LeagueID.default,
        month=Month.default,
        opponent_team_id=0,
        per_mode_simple=PerModeSimple.default,
        period=Period.default,
        season=Season.default,
        season_type_all_star=SeasonTypeAllStar.default,
        date_from_nullable="",
        date_to_nullable="",
        game_segment_nullable=GameSegmentNullable.default,
        location_nullable=LocationNullable.default,
        outcome_nullable=OutcomeNullable.default,
        season_segment_nullable=SeasonSegmentNullable.default,
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
            "TeamID": team_id,
            "LastNGames": last_n_games,
            "LeagueID": league_id,
            "Month": month,
            "OpponentTeamID": opponent_team_id,
            "PerMode": per_mode_simple,
            "Period": period,
            "Season": season,
            "SeasonType": season_type_all_star,
            "DateFrom": date_from_nullable,
            "DateTo": date_to_nullable,
            "GameSegment": game_segment_nullable,
            "Location": location_nullable,
            "Outcome": outcome_nullable,
            "SeasonSegment": season_segment_nullable,
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
        self.closest_defender10ft_plus_shooting = Endpoint.DataSet(
            data=data_sets["ClosestDefender10ftPlusShooting"]
        )
        self.closest_defender_shooting = Endpoint.DataSet(
            data=data_sets["ClosestDefenderShooting"]
        )
        self.dribble_shooting = Endpoint.DataSet(data=data_sets["DribbleShooting"])
        self.general_shooting = Endpoint.DataSet(data=data_sets["GeneralShooting"])
        self.shot_clock_shooting = Endpoint.DataSet(data=data_sets["ShotClockShooting"])
        self.touch_time_shooting = Endpoint.DataSet(data=data_sets["TouchTimeShooting"])
