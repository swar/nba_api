from nba_api.live.nba.endpoints._base import Endpoint
from nba_api.live.nba.library.http import NBALiveHTTP


class Odds(Endpoint):
    """Endpoint for retrieving live betting odds for NBA games."""

    endpoint_url = "odds/odds_todaysGames.json" # Oddly enough, this doesn't only return today's games
    expected_data = {
        "games": [
            {
                "gameId": "",
                "sr_id": "",
                "srMatchId": "",
                "homeTeamId": "",
                "awayTeamId": "",
                "markets": [
                    {
                        "name": "",
                        "odds_type_id": 0,
                        "group_name": "",
                        "books": [
                            {
                                "id": "",
                                "name": "",
                                "outcomes": [
                                    {
                                        "odds_field_id": 0,
                                        "type": "",
                                        "odds": "",
                                        "opening_odds": "",
                                        "odds_trend": "",
                                        "spread": None,        # For spread markets
                                        "opening_spread": None # For spread markets
                                    },
                                    {
                                        "odds_field_id": 0,
                                        "type": "",
                                        "odds": "",
                                        "opening_odds": "",
                                        "odds_trend": "",
                                        "spread": None,        # For spread markets
                                        "opening_spread": None # For spread markets
                                    }
                                ],
                                "url": "",
                                "countryCode": ""
                            }
                        ]
                    }
                ]
            }
        ]
    }

    nba_response = None
    data_sets = None
    games = None
    headers = None

    def __init__(self, proxy=None, headers=None, timeout=30, get_request=True):
        """
        Initialize the Odds endpoint.
        
        Args:
            proxy (str, optional): Proxy URL to use for the request
            headers (dict, optional): Custom HTTP headers
            timeout (int, optional): Request timeout in seconds (default: 30)
            get_request (bool, optional): Whether to fetch data immediately (default: True)
        """
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        if get_request:
            self.get_request()

    def get_request(self):
        """Fetch the odds data from the NBA API."""
        self.nba_response = NBALiveHTTP().send_api_request(
            endpoint=self.endpoint_url,
            parameters={},
            proxy=self.proxy,
            headers=self.headers,
            timeout=self.timeout,
        )
        self.load_response()

    def load_response(self):
        """Process the API response and load the games data."""
        data_sets = self.nba_response.get_dict()
        if "games" in data_sets:
            self.games = Endpoint.DataSet(data=data_sets["games"])

    def get_games(self):
        """
        Get the games data.
        
        Returns:
            Endpoint.DataSet: Dataset containing games and their odds
        """
        return self.games
