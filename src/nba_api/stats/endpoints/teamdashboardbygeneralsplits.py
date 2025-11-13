import warnings
from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import (
    LastNGames,
    MeasureTypeDetailedDefense,
    Month,
    PaceAdjust,
    PerModeDetailed,
    Period,
    PlusMinus,
    Rank,
    Season,
    SeasonTypeAllStar,
    GameSegmentNullable,
    LeagueIDNullable,
    LocationNullable,
    OutcomeNullable,
    SeasonSegmentNullable,
    ShotClockRangeNullable,
    ConferenceNullable,
    DivisionNullable,
)


class TeamDashboardByGeneralSplits(Endpoint):
    """
    TeamDashboardByGeneralSplits endpoint for team statistics broken down by various splits.

    WARNING: Known NBA API Bug with plus_minus='Y'
    -------------------------------------------------
    When plus_minus='Y' is used, the NBA API returns incorrect differential/delta values
    instead of actual statistics, making the data unusable.

    Example of incorrect data with plus_minus='Y':
        Boston Celtics 2023-24 Playoffs:
        - FGM: -0.3 (should be 39.3)
        - FGA: -1.4 (should be 83.8)
        - FG_PCT: 0.004 (should be 0.469)
        - PTS: 8.1 (this is actually the plus/minus value, not points!)

    RECOMMENDATION: Always use plus_minus='N' (default)
        The PLUS_MINUS column will still be included and will contain correct values.

    Example (correct usage):
        >>> from nba_api.stats.endpoints import TeamDashboardByGeneralSplits
        >>> result = TeamDashboardByGeneralSplits(
        ...     team_id='1610612738',
        ...     season='2023-24',
        ...     season_type_all_star='Playoffs',
        ...     plus_minus='N'  # Use 'N' to get correct data
        ... )
        >>> df = result.overall_team_dashboard.get_data_frame()
        >>> # PLUS_MINUS column is available even with plus_minus='N'

    Attributes:
        days_rest_team_dashboard (DataSet): Stats split by days of rest.
        location_team_dashboard (DataSet): Stats split by home/away.
        month_team_dashboard (DataSet): Stats split by month.
        overall_team_dashboard (DataSet): Overall team stats.
        pre_post_all_star_team_dashboard (DataSet): Stats split by pre/post All-Star break.
        wins_losses_team_dashboard (DataSet): Stats split by wins/losses.
    """
    endpoint = "teamdashboardbygeneralsplits"
    expected_data = {
        "DaysRestTeamDashboard": [
            "GROUP_SET",
            "GROUP_VALUE",
            "TEAM_DAYS_REST_RANGE",
            "GP",
            "W",
            "L",
            "W_PCT",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "TOV",
            "STL",
            "BLK",
            "BLKA",
            "PF",
            "PFD",
            "PTS",
            "PLUS_MINUS",
            "GP_RANK",
            "W_RANK",
            "L_RANK",
            "W_PCT_RANK",
            "MIN_RANK",
            "FGM_RANK",
            "FGA_RANK",
            "FG_PCT_RANK",
            "FG3M_RANK",
            "FG3A_RANK",
            "FG3_PCT_RANK",
            "FTM_RANK",
            "FTA_RANK",
            "FT_PCT_RANK",
            "OREB_RANK",
            "DREB_RANK",
            "REB_RANK",
            "AST_RANK",
            "TOV_RANK",
            "STL_RANK",
            "BLK_RANK",
            "BLKA_RANK",
            "PF_RANK",
            "PFD_RANK",
            "PTS_RANK",
            "PLUS_MINUS_RANK",
            "CFID",
            "CFPARAMS",
        ],
        "LocationTeamDashboard": [
            "GROUP_SET",
            "GROUP_VALUE",
            "TEAM_GAME_LOCATION",
            "GP",
            "W",
            "L",
            "W_PCT",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "TOV",
            "STL",
            "BLK",
            "BLKA",
            "PF",
            "PFD",
            "PTS",
            "PLUS_MINUS",
            "GP_RANK",
            "W_RANK",
            "L_RANK",
            "W_PCT_RANK",
            "MIN_RANK",
            "FGM_RANK",
            "FGA_RANK",
            "FG_PCT_RANK",
            "FG3M_RANK",
            "FG3A_RANK",
            "FG3_PCT_RANK",
            "FTM_RANK",
            "FTA_RANK",
            "FT_PCT_RANK",
            "OREB_RANK",
            "DREB_RANK",
            "REB_RANK",
            "AST_RANK",
            "TOV_RANK",
            "STL_RANK",
            "BLK_RANK",
            "BLKA_RANK",
            "PF_RANK",
            "PFD_RANK",
            "PTS_RANK",
            "PLUS_MINUS_RANK",
            "CFID",
            "CFPARAMS",
        ],
        "MonthTeamDashboard": [
            "GROUP_SET",
            "GROUP_VALUE",
            "SEASON_MONTH_NAME",
            "GP",
            "W",
            "L",
            "W_PCT",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "TOV",
            "STL",
            "BLK",
            "BLKA",
            "PF",
            "PFD",
            "PTS",
            "PLUS_MINUS",
            "GP_RANK",
            "W_RANK",
            "L_RANK",
            "W_PCT_RANK",
            "MIN_RANK",
            "FGM_RANK",
            "FGA_RANK",
            "FG_PCT_RANK",
            "FG3M_RANK",
            "FG3A_RANK",
            "FG3_PCT_RANK",
            "FTM_RANK",
            "FTA_RANK",
            "FT_PCT_RANK",
            "OREB_RANK",
            "DREB_RANK",
            "REB_RANK",
            "AST_RANK",
            "TOV_RANK",
            "STL_RANK",
            "BLK_RANK",
            "BLKA_RANK",
            "PF_RANK",
            "PFD_RANK",
            "PTS_RANK",
            "PLUS_MINUS_RANK",
            "CFID",
            "CFPARAMS",
        ],
        "OverallTeamDashboard": [
            "GROUP_SET",
            "GROUP_VALUE",
            "SEASON_YEAR",
            "GP",
            "W",
            "L",
            "W_PCT",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "TOV",
            "STL",
            "BLK",
            "BLKA",
            "PF",
            "PFD",
            "PTS",
            "PLUS_MINUS",
            "GP_RANK",
            "W_RANK",
            "L_RANK",
            "W_PCT_RANK",
            "MIN_RANK",
            "FGM_RANK",
            "FGA_RANK",
            "FG_PCT_RANK",
            "FG3M_RANK",
            "FG3A_RANK",
            "FG3_PCT_RANK",
            "FTM_RANK",
            "FTA_RANK",
            "FT_PCT_RANK",
            "OREB_RANK",
            "DREB_RANK",
            "REB_RANK",
            "AST_RANK",
            "TOV_RANK",
            "STL_RANK",
            "BLK_RANK",
            "BLKA_RANK",
            "PF_RANK",
            "PFD_RANK",
            "PTS_RANK",
            "PLUS_MINUS_RANK",
            "CFID",
            "CFPARAMS",
        ],
        "PrePostAllStarTeamDashboard": [
            "GROUP_SET",
            "GROUP_VALUE",
            "SEASON_SEGMENT",
            "GP",
            "W",
            "L",
            "W_PCT",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "TOV",
            "STL",
            "BLK",
            "BLKA",
            "PF",
            "PFD",
            "PTS",
            "PLUS_MINUS",
            "GP_RANK",
            "W_RANK",
            "L_RANK",
            "W_PCT_RANK",
            "MIN_RANK",
            "FGM_RANK",
            "FGA_RANK",
            "FG_PCT_RANK",
            "FG3M_RANK",
            "FG3A_RANK",
            "FG3_PCT_RANK",
            "FTM_RANK",
            "FTA_RANK",
            "FT_PCT_RANK",
            "OREB_RANK",
            "DREB_RANK",
            "REB_RANK",
            "AST_RANK",
            "TOV_RANK",
            "STL_RANK",
            "BLK_RANK",
            "BLKA_RANK",
            "PF_RANK",
            "PFD_RANK",
            "PTS_RANK",
            "PLUS_MINUS_RANK",
            "CFID",
            "CFPARAMS",
        ],
        "WinsLossesTeamDashboard": [
            "GROUP_SET",
            "GROUP_VALUE",
            "GAME_RESULT",
            "GP",
            "W",
            "L",
            "W_PCT",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "TOV",
            "STL",
            "BLK",
            "BLKA",
            "PF",
            "PFD",
            "PTS",
            "PLUS_MINUS",
            "GP_RANK",
            "W_RANK",
            "L_RANK",
            "W_PCT_RANK",
            "MIN_RANK",
            "FGM_RANK",
            "FGA_RANK",
            "FG_PCT_RANK",
            "FG3M_RANK",
            "FG3A_RANK",
            "FG3_PCT_RANK",
            "FTM_RANK",
            "FTA_RANK",
            "FT_PCT_RANK",
            "OREB_RANK",
            "DREB_RANK",
            "REB_RANK",
            "AST_RANK",
            "TOV_RANK",
            "STL_RANK",
            "BLK_RANK",
            "BLKA_RANK",
            "PF_RANK",
            "PFD_RANK",
            "PTS_RANK",
            "PLUS_MINUS_RANK",
            "CFID",
            "CFPARAMS",
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
        measure_type_detailed_defense=MeasureTypeDetailedDefense.default,
        month=Month.default,
        opponent_team_id=0,
        pace_adjust=PaceAdjust.default,
        per_mode_detailed=PerModeDetailed.default,
        period=Period.default,
        plus_minus=PlusMinus.default,
        rank=Rank.default,
        season=Season.default,
        season_type_all_star=SeasonTypeAllStar.default,
        date_from_nullable="",
        date_to_nullable="",
        game_segment_nullable=GameSegmentNullable.default,
        league_id_nullable=LeagueIDNullable.default,
        location_nullable=LocationNullable.default,
        outcome_nullable=OutcomeNullable.default,
        po_round_nullable="",
        season_segment_nullable=SeasonSegmentNullable.default,
        shot_clock_range_nullable=ShotClockRangeNullable.default,
        vs_conference_nullable=ConferenceNullable.default,
        vs_division_nullable=DivisionNullable.default,
        proxy=None,
        headers=None,
        timeout=30,
        get_request=True,
    ):
        # Warn about NBA API bug with plus_minus='Y'
        if plus_minus == 'Y':
            warnings.warn(
                "NBA API Bug: Using plus_minus='Y' returns incorrect data. "
                "Statistics show differential/delta values instead of actual values "
                "(e.g., FGM=-0.3 instead of 39.3). Use plus_minus='N' instead. "
                "The PLUS_MINUS column will still be included with correct values.",
                UserWarning,
                stacklevel=2
            )

        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
            "TeamID": team_id,
            "LastNGames": last_n_games,
            "MeasureType": measure_type_detailed_defense,
            "Month": month,
            "OpponentTeamID": opponent_team_id,
            "PaceAdjust": pace_adjust,
            "PerMode": per_mode_detailed,
            "Period": period,
            "PlusMinus": plus_minus,
            "Rank": rank,
            "Season": season,
            "SeasonType": season_type_all_star,
            "DateFrom": date_from_nullable,
            "DateTo": date_to_nullable,
            "GameSegment": game_segment_nullable,
            "LeagueID": league_id_nullable,
            "Location": location_nullable,
            "Outcome": outcome_nullable,
            "PORound": po_round_nullable,
            "SeasonSegment": season_segment_nullable,
            "ShotClockRange": shot_clock_range_nullable,
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
        self.days_rest_team_dashboard = Endpoint.DataSet(
            data=data_sets["DaysRestTeamDashboard"]
        )
        self.location_team_dashboard = Endpoint.DataSet(
            data=data_sets["LocationTeamDashboard"]
        )
        self.month_team_dashboard = Endpoint.DataSet(
            data=data_sets["MonthTeamDashboard"]
        )
        self.overall_team_dashboard = Endpoint.DataSet(
            data=data_sets["OverallTeamDashboard"]
        )
        self.pre_post_all_star_team_dashboard = Endpoint.DataSet(
            data=data_sets["PrePostAllStarTeamDashboard"]
        )
        self.wins_losses_team_dashboard = Endpoint.DataSet(
            data=data_sets["WinsLossesTeamDashboard"]
        )
