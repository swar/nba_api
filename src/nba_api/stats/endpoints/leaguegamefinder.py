"""
LeagueGameFinder endpoint for finding games based on various filters.

Example:
    >>> from nba_api.stats.endpoints import LeagueGameFinder
    >>> # Get Lakers games from 2023-24 season
    >>> games = LeagueGameFinder(
    ...     player_or_team_abbreviation='T',
    ...     team_id_nullable='1610612747',
    ...     season_nullable='2023-24'
    ... )
    >>> df = games.league_game_finder_results.get_data_frame()

Important Notes:
    **Date Filtering (Issue #526):**
    The date_from_nullable and date_to_nullable parameters work correctly and
    filter games by date range. Use format 'YYYY-MM-DD'.

    Example - filter by date range:
        >>> # Get all games in January 2024
        >>> games = LeagueGameFinder(
        ...     player_or_team_abbreviation='T',
        ...     date_from_nullable='2024-01-01',
        ...     date_to_nullable='2024-01-31'
        ... )
        >>> df = games.league_game_finder_results.get_data_frame()

    Note: Do not use 'DateBegin/DateEnd' parameters - these are ignored by the
    NBA API. The correct parameters are date_from_nullable/date_to_nullable.

    **Known API Limitation (Issue #446):**
    The game_id_nullable parameter does NOT filter results. The NBA Stats API
    ignores this parameter and returns all games matching other criteria.

    Workaround - filter results client-side:
        >>> # API call (game_id_nullable is ignored)
        >>> games = LeagueGameFinder(
        ...     player_or_team_abbreviation='T',
        ...     season_nullable='2023-24',
        ...     game_id_nullable='0022301181'  # This is ignored by API
        ... )
        >>> df = games.league_game_finder_results.get_data_frame()
        >>> # Filter for specific game
        >>> specific_game = df[df['GAME_ID'] == '0022301181']

    Using season_nullable helps reduce the result set size before filtering.
"""

import warnings

from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import (
    PlayerOrTeamAbbreviation,
    ConferenceNullable,
    DivisionSimpleNullable,
    LeagueIDNullable,
    LocationNullable,
    OutcomeNullable,
    SeasonNullable,
    SeasonSegmentNullable,
    SeasonTypeNullable,
    StarterBenchNullable,
    DivisionNullable,
)


class LeagueGameFinder(Endpoint):
    endpoint = "leaguegamefinder"
    expected_data = {
        "LeagueGameFinderResults": [
            "SEASON_ID",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "GAME_ID",
            "GAME_DATE",
            "MATCHUP",
            "WL",
            "MIN",
            "PTS",
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
            "STL",
            "BLK",
            "TOV",
            "PF",
            "PLUS_MINUS",
        ]
    }

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(
        self,
        player_or_team_abbreviation=PlayerOrTeamAbbreviation.default,
        conference_nullable=ConferenceNullable.default,
        date_from_nullable="",
        date_to_nullable="",
        division_simple_nullable=DivisionSimpleNullable.default,
        draft_number_nullable="",
        draft_round_nullable="",
        draft_team_id_nullable="",
        draft_year_nullable="",
        eq_ast_nullable="",
        eq_blk_nullable="",
        eq_dd_nullable="",
        eq_dreb_nullable="",
        eq_fg3a_nullable="",
        eq_fg3m_nullable="",
        eq_fg3_pct_nullable="",
        eq_fga_nullable="",
        eq_fgm_nullable="",
        eq_fg_pct_nullable="",
        eq_fta_nullable="",
        eq_ftm_nullable="",
        eq_ft_pct_nullable="",
        eq_minutes_nullable="",
        eq_oreb_nullable="",
        eq_pf_nullable="",
        eq_pts_nullable="",
        eq_reb_nullable="",
        eq_stl_nullable="",
        eq_td_nullable="",
        eq_tov_nullable="",
        game_id_nullable="",
        gt_ast_nullable="",
        gt_blk_nullable="",
        gt_dd_nullable="",
        gt_dreb_nullable="",
        gt_fg3a_nullable="",
        gt_fg3m_nullable="",
        gt_fg3_pct_nullable="",
        gt_fga_nullable="",
        gt_fgm_nullable="",
        gt_fg_pct_nullable="",
        gt_fta_nullable="",
        gt_ftm_nullable="",
        gt_ft_pct_nullable="",
        gt_minutes_nullable="",
        gt_oreb_nullable="",
        gt_pf_nullable="",
        gt_pts_nullable="",
        gt_reb_nullable="",
        gt_stl_nullable="",
        gt_td_nullable="",
        gt_tov_nullable="",
        league_id_nullable=LeagueIDNullable.default,
        location_nullable=LocationNullable.default,
        lt_ast_nullable="",
        lt_blk_nullable="",
        lt_dd_nullable="",
        lt_dreb_nullable="",
        lt_fg3a_nullable="",
        lt_fg3m_nullable="",
        lt_fg3_pct_nullable="",
        lt_fga_nullable="",
        lt_fgm_nullable="",
        lt_fg_pct_nullable="",
        lt_fta_nullable="",
        lt_ftm_nullable="",
        lt_ft_pct_nullable="",
        lt_minutes_nullable="",
        lt_oreb_nullable="",
        lt_pf_nullable="",
        lt_pts_nullable="",
        lt_reb_nullable="",
        lt_stl_nullable="",
        lt_td_nullable="",
        lt_tov_nullable="",
        outcome_nullable=OutcomeNullable.default,
        po_round_nullable="",
        player_id_nullable="",
        rookie_year_nullable=SeasonNullable.default,
        season_nullable=SeasonNullable.default,
        season_segment_nullable=SeasonSegmentNullable.default,
        season_type_nullable=SeasonTypeNullable.default,
        starter_bench_nullable=StarterBenchNullable.default,
        team_id_nullable="",
        vs_conference_nullable=ConferenceNullable.default,
        vs_division_nullable=DivisionNullable.default,
        vs_team_id_nullable="",
        years_experience_nullable="",
        proxy=None,
        headers=None,
        timeout=30,
        get_request=True,
    ):
        # Warn users about game_id_nullable limitation (Issue #446)
        if game_id_nullable:
            warnings.warn(
                "The 'game_id_nullable' parameter is ignored by the NBA Stats API "
                "(Issue #446). Results will not be filtered by game ID. "
                "Workaround: Filter client-side using "
                "df[df['GAME_ID'] == '{}']".format(game_id_nullable),
                UserWarning,
                stacklevel=2
            )

        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
            "PlayerOrTeam": player_or_team_abbreviation,
            "Conference": conference_nullable,
            "DateFrom": date_from_nullable,
            "DateTo": date_to_nullable,
            "Division": division_simple_nullable,
            "DraftNumber": draft_number_nullable,
            "DraftRound": draft_round_nullable,
            "DraftTeamID": draft_team_id_nullable,
            "DraftYear": draft_year_nullable,
            "EqAST": eq_ast_nullable,
            "EqBLK": eq_blk_nullable,
            "EqDD": eq_dd_nullable,
            "EqDREB": eq_dreb_nullable,
            "EqFG3A": eq_fg3a_nullable,
            "EqFG3M": eq_fg3m_nullable,
            "EqFG3_PCT": eq_fg3_pct_nullable,
            "EqFGA": eq_fga_nullable,
            "EqFGM": eq_fgm_nullable,
            "EqFG_PCT": eq_fg_pct_nullable,
            "EqFTA": eq_fta_nullable,
            "EqFTM": eq_ftm_nullable,
            "EqFT_PCT": eq_ft_pct_nullable,
            "EqMINUTES": eq_minutes_nullable,
            "EqOREB": eq_oreb_nullable,
            "EqPF": eq_pf_nullable,
            "EqPTS": eq_pts_nullable,
            "EqREB": eq_reb_nullable,
            "EqSTL": eq_stl_nullable,
            "EqTD": eq_td_nullable,
            "EqTOV": eq_tov_nullable,
            "GameID": game_id_nullable,
            "GtAST": gt_ast_nullable,
            "GtBLK": gt_blk_nullable,
            "GtDD": gt_dd_nullable,
            "GtDREB": gt_dreb_nullable,
            "GtFG3A": gt_fg3a_nullable,
            "GtFG3M": gt_fg3m_nullable,
            "GtFG3_PCT": gt_fg3_pct_nullable,
            "GtFGA": gt_fga_nullable,
            "GtFGM": gt_fgm_nullable,
            "GtFG_PCT": gt_fg_pct_nullable,
            "GtFTA": gt_fta_nullable,
            "GtFTM": gt_ftm_nullable,
            "GtFT_PCT": gt_ft_pct_nullable,
            "GtMINUTES": gt_minutes_nullable,
            "GtOREB": gt_oreb_nullable,
            "GtPF": gt_pf_nullable,
            "GtPTS": gt_pts_nullable,
            "GtREB": gt_reb_nullable,
            "GtSTL": gt_stl_nullable,
            "GtTD": gt_td_nullable,
            "GtTOV": gt_tov_nullable,
            "LeagueID": league_id_nullable,
            "Location": location_nullable,
            "LtAST": lt_ast_nullable,
            "LtBLK": lt_blk_nullable,
            "LtDD": lt_dd_nullable,
            "LtDREB": lt_dreb_nullable,
            "LtFG3A": lt_fg3a_nullable,
            "LtFG3M": lt_fg3m_nullable,
            "LtFG3_PCT": lt_fg3_pct_nullable,
            "LtFGA": lt_fga_nullable,
            "LtFGM": lt_fgm_nullable,
            "LtFG_PCT": lt_fg_pct_nullable,
            "LtFTA": lt_fta_nullable,
            "LtFTM": lt_ftm_nullable,
            "LtFT_PCT": lt_ft_pct_nullable,
            "LtMINUTES": lt_minutes_nullable,
            "LtOREB": lt_oreb_nullable,
            "LtPF": lt_pf_nullable,
            "LtPTS": lt_pts_nullable,
            "LtREB": lt_reb_nullable,
            "LtSTL": lt_stl_nullable,
            "LtTD": lt_td_nullable,
            "LtTOV": lt_tov_nullable,
            "Outcome": outcome_nullable,
            "PORound": po_round_nullable,
            "PlayerID": player_id_nullable,
            "RookieYear": rookie_year_nullable,
            "Season": season_nullable,
            "SeasonSegment": season_segment_nullable,
            "SeasonType": season_type_nullable,
            "StarterBench": starter_bench_nullable,
            "TeamID": team_id_nullable,
            "VsConference": vs_conference_nullable,
            "VsDivision": vs_division_nullable,
            "VsTeamID": vs_team_id_nullable,
            "YearsExperience": years_experience_nullable,
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
        self.league_game_finder_results = Endpoint.DataSet(
            data=data_sets["LeagueGameFinderResults"]
        )
