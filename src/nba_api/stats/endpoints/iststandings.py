from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueID, Season, Section


class ISTStandings(Endpoint):
    endpoint = "iststandings"
    expected_data = {
        "Standings": [
            "leagueId",
            "seasonYear",
            "teamId",
            "teamCity",
            "teamName",
            "teamAbbreviation",
            "teamSlug",
            "conference",
            "istGroup",
            "clinchIndicator",
            "clinchedIstKnockout",
            "clinchedIstGroup",
            "clinchedIstWildcard",
            "istWildcardRank",
            "istGroupRank",
            "istKnockoutRank",
            "wins",
            "losses",
            "pct",
            "istGroupGb",
            "istWildcardGb",
            "diff",
            "pts",
            "oppPts",
            "gameId1",
            "opponentTeamAbbreviation1",
            "location1",
            "gameStatus1",
            "gameStatusText1",
            "outcome1",
            "gameId2",
            "opponentTeamAbbreviation2",
            "location2",
            "gameStatus2",
            "gameStatusText2",
            "outcome2",
            "gameId3",
            "opponentTeamAbbreviation3",
            "location3",
            "gameStatus3",
            "gameStatusText3",
            "outcome3",
            "gameId4",
            "opponentTeamAbbreviation4",
            "location4",
            "gameStatus4",
            "gameStatusText4",
            "outcome4",
        ]
    }

    nba_response = None
    data_sets = None
    standings = None
    headers = None

    def __init__(
        self,
        league_id=LeagueID.default,
        season=Season.default,
        section=Section.default,
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
            "Section": section,
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
        self.standings = Endpoint.DataSet(data=data_sets["Standings"])
