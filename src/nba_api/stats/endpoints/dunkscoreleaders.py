"""
DunkScoreLeaders endpoint for NBA dunk tracking data.

This module provides the DunkScoreLeaders class for accessing comprehensive
dunk tracking information from the NBA Stats API, including biomechanics,
scores, and style metrics for every dunk.

Example:
    >>> from nba_api.stats.endpoints import DunkScoreLeaders
    >>> dunks = DunkScoreLeaders(season='2024-25')
    >>> df = dunks.dunks.get_data_frame()
    >>> print(df[['PLAYER_NAME', 'DUNK_SCORE', 'PLAYER_VERTICAL']].head())
"""

from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.endpoints._expected_data.dunkscoreleaders import _EXPECTED_DATA
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueIDNullable, Season, SeasonTypeAllStar


class DunkScoreLeaders(Endpoint):
    """
    DunkScoreLeaders endpoint for retrieving comprehensive dunk tracking data.

    The DunkScoreLeaders endpoint provides detailed information about every dunk including:
    - Dunk scores and subscores (jump, power, style, defensive contest)
    - Biomechanics (player vertical, hang time, takeoff distance)
    - Ball tracking (max height, speed through rim, distance traveled)
    - Dunk style indicators (reverse, 360, through the legs, alley-oop, etc.)
    - Player and team information
    - Assist details (passer info, pass length, catch distance)

    Args:
        league_id_nullable (str, optional): League ID ("00" for NBA). Defaults to "00".
        season (str, optional): Season in format "YYYY-YY". Defaults to current season.
        season_type_all_star (str, optional): Season type (e.g., "Regular Season").
        player_id_nullable (str, optional): Filter by specific player ID.
        team_id_nullable (str, optional): Filter by specific team ID.
        game_id_nullable (str, optional): Filter by specific game ID.
        proxy (str, optional): HTTP/HTTPS proxy for requests.
        headers (dict, optional): Custom HTTP headers.
        timeout (int, optional): Request timeout in seconds. Defaults to 30.
        get_request (bool, optional): Whether to fetch data immediately. Defaults to True.

    Attributes:
        dunks (DataSet): Dataset containing all dunk records with 55 fields.

    Example:
        >>> from nba_api.stats.endpoints import DunkScoreLeaders
        >>> # Get all dunks for 2024-25 season
        >>> dunks = DunkScoreLeaders(season='2024-25')
        >>> df = dunks.dunks.get_data_frame()
        >>>
        >>> # Filter by specific player
        >>> player_dunks = DunkScoreLeaders(
        ...     season='2024-25',
        ...     player_id_nullable='1630168'
        ... )
        >>> df = player_dunks.dunks.get_data_frame()
        >>> print(df[['PLAYER_NAME', 'DUNK_SCORE', 'PLAYER_VERTICAL', 'HANG_TIME']])
    """

    endpoint = "dunkscoreleaders"
    expected_data = _EXPECTED_DATA

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(
        self,
        league_id_nullable=LeagueIDNullable.default,
        season=Season.default,
        season_type_all_star=SeasonTypeAllStar.default,
        player_id_nullable="",
        team_id_nullable="",
        game_id_nullable="",
        proxy=None,
        headers=None,
        timeout=30,
        get_request=True,
    ):
        """
        Initialize DunkScoreLeaders endpoint.

        Args:
            league_id_nullable: League ID ("00" for NBA).
            season: Season in format "YYYY-YY" (e.g., "2024-25").
            season_type_all_star: Season type (e.g., "Regular Season", "Playoffs").
            player_id_nullable: Filter by specific player ID.
            team_id_nullable: Filter by specific team ID.
            game_id_nullable: Filter by specific game ID.
            proxy: HTTP/HTTPS proxy for requests.
            headers: Custom HTTP headers.
            timeout: Request timeout in seconds.
            get_request: Whether to fetch data immediately.
        """
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
            "LeagueID": league_id_nullable,
            "Season": season,
            "SeasonType": season_type_all_star,
            "PlayerID": player_id_nullable,
            "TeamID": team_id_nullable,
            "GameID": game_id_nullable,
        }

        # Initialize dataset attributes (prevents pylint warnings)
        self.dunks = None

        if get_request:
            self.get_request()

    def get_request(self):
        """
        Fetch data from the NBA API.

        Makes an HTTP request to the DunkScoreLeaders endpoint and loads
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

        Extracts the Dunks dataset from the API response and creates an
        accessible DataSet object containing all dunk records with detailed
        biomechanics and scoring information.
        """
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [
            Endpoint.DataSet(data=data_set)
            for data_set_name, data_set in data_sets.items()
        ]
        self.dunks = Endpoint.DataSet(data=data_sets["Dunks"])
