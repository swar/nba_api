"""
ScoreboardV3 endpoint for NBA daily game schedule and scores.

This module provides the ScoreboardV3 class for accessing daily game information
including scores, standings, game status, leaders, and broadcast information.

Example:
    >>> from nba_api.stats.endpoints import ScoreboardV3
    >>> scoreboard = ScoreboardV3(game_date='2025-11-05')
    >>> games = scoreboard.game_header.get_data_frame()
"""

from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.endpoints._expected_data.scoreboardv3 import _EXPECTED_DATA
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import GameDate, LeagueID


class ScoreboardV3(Endpoint):
    """
    ScoreboardV3 endpoint for retrieving daily game schedule and scores.

    The ScoreboardV3 endpoint provides comprehensive game information for a given date:
    - Scoreboard info (game date, league info)
    - Game headers (status, timing, teams, series info)
    - Line scores (team scores, records, timeouts)
    - Game leaders (top performers for each game)

    Args:
        game_date (str): Required. Game date in YYYY-MM-DD format.
        league_id (str, optional): League ID ('00' for NBA). Defaults to LeagueID.default.
        proxy (str, optional): HTTP/HTTPS proxy for requests.
        headers (dict, optional): Custom HTTP headers.
        timeout (int, optional): Request timeout in seconds. Defaults to 30.
        get_request (bool, optional): Whether to fetch data immediately. Defaults to True.

    Attributes:
        scoreboard_info (DataSet): Top-level scoreboard information.
        game_header (DataSet): Core game information for all games.
        line_score (DataSet): Team scores and records.
        game_leaders (DataSet): Per-game leaders statistics (who led in THIS game).
        team_leaders (DataSet): Season leaders for each team (season averages).
        broadcasters (DataSet): Broadcaster information (TV, radio, OTT).

    Example:
        >>> from nba_api.stats.endpoints import ScoreboardV3
        >>> # Get scoreboard for a specific date
        >>> scoreboard = ScoreboardV3(game_date='2025-11-05')
        >>>
        >>> # Get game headers as DataFrame
        >>> games_df = scoreboard.game_header.get_data_frame()
        >>> print(games_df[['gameId', 'gameStatusText', 'homeTeam', 'awayTeam']])
        >>>
        >>> # Get line scores
        >>> scores_df = scoreboard.line_score.get_data_frame()
        >>> print(scores_df[['teamCity', 'teamName', 'wins', 'losses', 'score']])
        >>>
        >>> # Get game leaders
        >>> leaders_df = scoreboard.game_leaders.get_data_frame()
        >>> print(leaders_df[['name', 'leaderType', 'points', 'rebounds', 'assists']])
    """

    endpoint = "scoreboardv3"
    expected_data = _EXPECTED_DATA

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(
        self,
        game_date,
        league_id=LeagueID.default,
        proxy=None,
        headers=None,
        timeout=30,
        get_request=True,
    ):
        """
        Initialize ScoreboardV3 endpoint.

        Args:
            game_date (str): Game date in YYYY-MM-DD format.
            league_id (str, optional): League ID ('00' for NBA). Defaults to LeagueID.default.
            proxy (str, optional): HTTP/HTTPS proxy for requests.
            headers (dict, optional): Custom HTTP headers.
            timeout (int, optional): Request timeout in seconds. Defaults to 30.
            get_request (bool, optional): Whether to fetch data immediately.
                                         Defaults to True.
        """
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
            "GameDate": game_date,
            "LeagueID": league_id,
        }

        # Initialize dataset attributes (populated in load_response)
        self.scoreboard_info = None
        self.game_header = None
        self.line_score = None
        self.game_leaders = None
        self.team_leaders = None
        self.broadcasters = None

        if get_request:
            self.get_request()

    def get_request(self):
        """
        Fetch data from the NBA API.

        Makes an HTTP request to the ScoreboardV3 endpoint and loads
        the response into DataSet objects.
        """
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters=self.parameters,
            proxy=self.proxy,
            headers=self.headers,
            timeout=self.timeout,
        )
        self.load_response()

    def load_response(self):
        """
        Parse API response and load data into DataSet objects.

        Extracts all 6 datasets from the API response and creates accessible
        DataSet objects for each:
        - ScoreboardInfo: Game date and league information
        - GameHeader: Core game information
        - LineScore: Team scores and records
        - GameLeaders: Per-game leader statistics
        - TeamLeaders: Season leader statistics
        - Broadcasters: Broadcaster information
        """
        data_sets = self.nba_response.get_data_sets(self.endpoint)
        self.data_sets = [
            Endpoint.DataSet(data=data_set)
            for data_set_name, data_set in data_sets.items()
        ]
        self.scoreboard_info = Endpoint.DataSet(data=data_sets["ScoreboardInfo"])
        self.game_header = Endpoint.DataSet(data=data_sets["GameHeader"])
        self.line_score = Endpoint.DataSet(data=data_sets["LineScore"])
        self.game_leaders = Endpoint.DataSet(data=data_sets["GameLeaders"])
        self.team_leaders = Endpoint.DataSet(data=data_sets["TeamLeaders"])
        self.broadcasters = Endpoint.DataSet(data=data_sets["Broadcasters"])
