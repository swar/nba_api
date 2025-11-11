"""
BoxScoreSummary v3 endpoint for NBA game summary data.

This module provides the BoxScoreSummaryV3 class for accessing comprehensive
game summary information from the NBA Stats API, including game details,
arena information, officials, scores, inactive players, historical matchups,
and advanced statistics.

Example:
    >>> from nba_api.stats.endpoints import BoxScoreSummaryV3
    >>> summary = BoxScoreSummaryV3(game_id='0022500142')
    >>> game_data = summary.game_info.get_dict()
"""

from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.endpoints._expected_data.boxscoresummaryv3 import _EXPECTED_DATA
from nba_api.stats.library.http import NBAStatsHTTP


class BoxScoreSummaryV3(Endpoint):
    """
    BoxScoreSummary v3 endpoint for retrieving comprehensive game summary data.

    The BoxScoreSummaryV3 endpoint provides detailed game information including:
    - Game summary (status, teams, timing, attendance)
    - Game info (date, attendance, duration)
    - Arena information (location, details)
    - Game officials
    - Line scores (period-by-period scoring)
    - Inactive players
    - Historical matchups (last 5 meetings)
    - Advanced game statistics (points in paint, bench points, lead changes, etc.)
    - Video availability flags

    Args:
        game_id (str): Required. 10-digit NBA game ID (e.g., '0022500142').
        proxy (str, optional): HTTP/HTTPS proxy for requests.
        headers (dict, optional): Custom HTTP headers.
        timeout (int, optional): Request timeout in seconds. Defaults to 30.
        get_request (bool, optional): Whether to fetch data immediately. Defaults to True.

    Attributes:
        game_summary (DataSet): Core game information.
        game_info (DataSet): Game date, attendance, and duration.
        arena_info (DataSet): Arena location and details.
        officials (DataSet): Game officials information.
        line_score (DataSet): Period-by-period scores for both teams.
        inactive_players (DataSet): Players inactive for the game.
        last_five_meetings (DataSet): Up to 5 previous games between these teams.
        other_stats (DataSet): Advanced game statistics and metrics.
        available_video (DataSet): Video availability flags.

    Example:
        >>> from nba_api.stats.endpoints import BoxScoreSummaryV3
        >>> # Get game summary
        >>> summary = BoxScoreSummaryV3(game_id='0022500142')
        >>>
        >>> # Access game info as dictionary
        >>> game_info = summary.game_info.get_dict()
        >>> print(game_info)
        >>>
        >>> # Access team statistics as DataFrame
        >>> stats_df = summary.other_stats.get_data_frame()
        >>> print(stats_df[['teamCity', 'points', 'pointsInThePaint']])
        >>>
        >>> # Get all datasets as DataFrames
        >>> all_data = summary.get_data_frames()
    """

    endpoint = "boxscoresummaryv3"
    expected_data = _EXPECTED_DATA

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self, game_id, proxy=None, headers=None, timeout=30, get_request=True):
        """
        Initialize BoxScoreSummaryV3 endpoint.

        Args:
            game_id (str): 10-digit NBA game ID (e.g., '0022500142').
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
        self.parameters = {"GameID": game_id}

        # Initialize dataset attributes (populated in load_response)
        self.game_summary = None
        self.game_info = None
        self.arena_info = None
        self.officials = None
        self.line_score = None
        self.inactive_players = None
        self.last_five_meetings = None
        self.other_stats = None
        self.available_video = None

        if get_request:
            self.get_request()

    def get_request(self):
        """
        Fetch data from the NBA API.

        Makes an HTTP request to the BoxScoreSummaryV3 endpoint and loads
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

        Extracts all 9 datasets from the API response and creates accessible
        DataSet objects for each:
        - GameSummary: Core game information
        - GameInfo: Date, attendance, duration
        - ArenaInfo: Arena location and details
        - Officials: Game officials
        - LineScore: Period-by-period scores
        - InactivePlayers: Inactive players list
        - LastFiveMeetings: Historical matchups
        - OtherStats: Advanced game statistics
        - AvailableVideo: Video availability flags
        """
        data_sets = self.nba_response.get_data_sets(self.endpoint)
        self.data_sets = [
            Endpoint.DataSet(data=data_set)
            for data_set_name, data_set in data_sets.items()
        ]
        self.game_summary = Endpoint.DataSet(data=data_sets["GameSummary"])
        self.game_info = Endpoint.DataSet(data=data_sets["GameInfo"])
        self.arena_info = Endpoint.DataSet(data=data_sets["ArenaInfo"])
        self.officials = Endpoint.DataSet(data=data_sets["Officials"])
        self.line_score = Endpoint.DataSet(data=data_sets["LineScore"])
        self.inactive_players = Endpoint.DataSet(data=data_sets["InactivePlayers"])
        self.last_five_meetings = Endpoint.DataSet(data=data_sets["LastFiveMeetings"])
        self.other_stats = Endpoint.DataSet(data=data_sets["OtherStats"])
        self.available_video = Endpoint.DataSet(data=data_sets["AvailableVideo"])
