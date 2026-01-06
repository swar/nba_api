from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import (
    LeagueID,
    Season,
    SeasonTypeAllStar,
)


class GravityLeaders(Endpoint):
    endpoint = "gravityleaders"
    expected_data = {
        "leaders": [
            "PLAYERID",
            "FIRSTNAME",
            "LASTNAME",
            "TEAMID",
            "TEAMABBREVIATION",
            "TEAMNAME",
            "TEAMCITY",
            "FRAMES",
            "GRAVITYSCORE",
            "AVGGRAVITYSCORE",
            "ONBALLPERIMETERFRAMES",
            "ONBALLPERIMETERGRAVITYSCORE",
            "AVGONBALLPERIMETERGRAVITYSCORE",
            "OFFBALLPERIMETERFRAMES",
            "OFFBALLPERIMETERGRAVITYSCORE",
            "AVGOFFBALLPERIMETERGRAVITYSCORE",
            "ONBALLINTERIORFRAMES",
            "ONBALLINTERIORGRAVITYSCORE",
            "AVGONBALLINTERIORGRAVITYSCORE",
            "OFFBALLINTERIORFRAMES",
            "OFFBALLINTERIORGRAVITYSCORE",
            "AVGOFFBALLINTERIORGRAVITYSCORE",
            "GAMESPLAYED",
            "MINUTES",
            "PTS",
            "REB",
            "AST",
        ]
    }

    nba_response = None
    data_sets = None
    headers = None

    def __init__(
        self,
        league_id=LeagueID.default,
        season=Season.default,
        season_type_all_star=SeasonTypeAllStar.default,
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
            "LeagueID": league_id,
            "Season": season,
            "SeasonType": season_type_all_star,
        }

        # Initialize dataset attributes
        self.league_leaders = None

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

        # Validate response structure
        if not isinstance(data_sets, dict):
            raise ValueError(
                f"Invalid response structure from NBA API: expected dict, "
                f"got {type(data_sets).__name__}"
            )

        # Validate required dataset exists
        if "leaders" not in data_sets:
            available_keys = list(data_sets.keys())
            raise ValueError(
                f"API response missing required 'leaders' dataset. "
                f"Available datasets: {available_keys}. "
                f"This may indicate invalid parameters or an API change. "
                f"Parameters used: {self.parameters}"
            )

        self.data_sets = [
            Endpoint.DataSet(data=data_set)
            for data_set_name, data_set in data_sets.items()
        ]
        self.league_leaders = Endpoint.DataSet(data=data_sets["leaders"])
