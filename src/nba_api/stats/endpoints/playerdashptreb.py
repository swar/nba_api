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


class PlayerDashPtReb(Endpoint):
    endpoint = "playerdashptreb"
    expected_data = {
        "NumContestedRebounding": [
            "PLAYER_ID",
            "PLAYER_NAME_LAST_FIRST",
            "SORT_ORDER",
            "G",
            "REB_NUM_CONTESTING_RANGE",
            "REB_FREQUENCY",
            "OREB",
            "DREB",
            "REB",
            "C_OREB",
            "C_DREB",
            "C_REB",
            "C_REB_PCT",
            "UC_OREB",
            "UC_DREB",
            "UC_REB",
            "UC_REB_PCT",
        ],
        "OverallRebounding": [
            "PLAYER_ID",
            "PLAYER_NAME_LAST_FIRST",
            "G",
            "OVERALL",
            "REB_FREQUENCY",
            "OREB",
            "DREB",
            "REB",
            "C_OREB",
            "C_DREB",
            "C_REB",
            "C_REB_PCT",
            "UC_OREB",
            "UC_DREB",
            "UC_REB",
            "UC_REB_PCT",
        ],
        "RebDistanceRebounding": [
            "PLAYER_ID",
            "PLAYER_NAME_LAST_FIRST",
            "SORT_ORDER",
            "G",
            "REB_DIST_RANGE",
            "REB_FREQUENCY",
            "OREB",
            "DREB",
            "REB",
            "C_OREB",
            "C_DREB",
            "C_REB",
            "C_REB_PCT",
            "UC_OREB",
            "UC_DREB",
            "UC_REB",
            "UC_REB_PCT",
        ],
        "ShotDistanceRebounding": [
            "PLAYER_ID",
            "PLAYER_NAME_LAST_FIRST",
            "SORT_ORDER",
            "G",
            "SHOT_DIST_RANGE",
            "REB_FREQUENCY",
            "OREB",
            "DREB",
            "REB",
            "C_OREB",
            "C_DREB",
            "C_REB",
            "C_REB_PCT",
            "UC_OREB",
            "UC_DREB",
            "UC_REB",
            "UC_REB_PCT",
        ],
        "ShotTypeRebounding": [
            "PLAYER_ID",
            "PLAYER_NAME_LAST_FIRST",
            "SORT_ORDER",
            "G",
            "SHOT_TYPE_RANGE",
            "REB_FREQUENCY",
            "OREB",
            "DREB",
            "REB",
            "C_OREB",
            "C_DREB",
            "C_REB",
            "C_REB_PCT",
            "UC_OREB",
            "UC_DREB",
            "UC_REB",
            "UC_REB_PCT",
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
        player_id,
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
            "PlayerID": player_id,
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
        self.num_contested_rebounding = Endpoint.DataSet(
            data=data_sets["NumContestedRebounding"]
        )
        self.overall_rebounding = Endpoint.DataSet(data=data_sets["OverallRebounding"])
        self.reb_distance_rebounding = Endpoint.DataSet(
            data=data_sets["RebDistanceRebounding"]
        )
        self.shot_distance_rebounding = Endpoint.DataSet(
            data=data_sets["ShotDistanceRebounding"]
        )
        self.shot_type_rebounding = Endpoint.DataSet(
            data=data_sets["ShotTypeRebounding"]
        )
