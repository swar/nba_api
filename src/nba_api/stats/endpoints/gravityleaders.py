from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.endpoints._parsers import NBAStatsGravityLeadersParser
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import (
    LeagueID,
    Season,
    SeasonTypeAllStar,
)


class GravityLeaders(Endpoint):
    """
    Gravity quantifies how much a player pulls defenders towards them above expected,
    essentially measuring how much attention they draw compared to what the spacing on
    the floor predicts.
    """

    endpoint = "gravityleaders"
    expected_data = {"leaders": list(NBAStatsGravityLeadersParser.LEADER_FIELDS)}

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
        data_sets = self.nba_response.get_data_sets(self.endpoint)

        self.data_sets = [
            Endpoint.DataSet(data=data_set)
            for data_set_name, data_set in data_sets.items()
        ]
        self.leaders = Endpoint.DataSet(data=data_sets["leaders"])
