from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import (
    ContextMeasureDetailed,
    LeagueID,
    Period,
    Season,
    SeasonTypeAllStar,
    GameSegmentNullable,
    LastNGamesNullable,
    LocationNullable,
    MonthNullable,
    OutcomeNullable,
    SeasonSegmentNullable,
    ConferenceNullable,
    DivisionNullable,
)


class ShotChartLineupDetail(Endpoint):
    endpoint = "shotchartlineupdetail"
    expected_data = {
        "ShotChartLineupDetail": [
            "GRID_TYPE",
            "GAME_ID",
            "GAME_EVENT_ID",
            "GROUP_ID",
            "GROUP_NAME",
            "PLAYER_ID",
            "PLAYER_NAME",
            "TEAM_ID",
            "TEAM_NAME",
            "PERIOD",
            "MINUTES_REMAINING",
            "SECONDS_REMAINING",
            "EVENT_TYPE",
            "ACTION_TYPE",
            "SHOT_TYPE",
            "SHOT_ZONE_BASIC",
            "SHOT_ZONE_AREA",
            "SHOT_ZONE_RANGE",
            "SHOT_DISTANCE",
            "LOC_X",
            "LOC_Y",
            "SHOT_ATTEMPTED_FLAG",
            "SHOT_MADE_FLAG",
            "GAME_DATE",
            "HTM",
            "VTM",
        ],
        "ShotChartLineupLeagueAverage": [
            "GRID_TYPE",
            "SHOT_ZONE_BASIC",
            "SHOT_ZONE_AREA",
            "SHOT_ZONE_RANGE",
            "FGA",
            "FGM",
            "FG_PCT",
        ],
    }

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(
        self,
        context_measure_detailed=ContextMeasureDetailed.default,
        group_id=0,
        league_id=LeagueID.default,
        period=Period.default,
        season=Season.default,
        season_type_all_star=SeasonTypeAllStar.default,
        context_filter_nullable="",
        date_from_nullable="",
        date_to_nullable="",
        game_id_nullable="",
        game_segment_nullable=GameSegmentNullable.default,
        last_n_games_nullable=LastNGamesNullable.default,
        location_nullable=LocationNullable.default,
        month_nullable=MonthNullable.default,
        opponent_team_id_nullable="",
        outcome_nullable=OutcomeNullable.default,
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
            "ContextMeasure": context_measure_detailed,
            "GROUP_ID": group_id,
            "LeagueID": league_id,
            "Period": period,
            "Season": season,
            "SeasonType": season_type_all_star,
            "ContextFilter": context_filter_nullable,
            "DateFrom": date_from_nullable,
            "DateTo": date_to_nullable,
            "GameID": game_id_nullable,
            "GameSegment": game_segment_nullable,
            "LastNGames": last_n_games_nullable,
            "Location": location_nullable,
            "Month": month_nullable,
            "OpponentTeamID": opponent_team_id_nullable,
            "Outcome": outcome_nullable,
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
        self.shot_chart_lineup_detail = Endpoint.DataSet(
            data=data_sets["ShotChartLineupDetail"]
        )
        self.shot_chart_lineup_league_average = Endpoint.DataSet(
            data=data_sets["ShotChartLineupLeagueAverage"]
        )
