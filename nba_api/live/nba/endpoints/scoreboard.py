from nba_api.live.nba.endpoints._base import Endpoint
from nba_api.live.nba.library.http import NBALiveHTTP

class ScoreBoard(Endpoint):
    endpoint_url = 'scoreboard/todaysScoreboard_00.json'
    expected_data = {'meta': {'version': 0, 'request': '', 'time': '', 'code': 0}, 'scoreboard': {'gameDate': '', 'leagueId': '', 'leagueName': '', 'games': [{'gameId': '', 'gameCode': '', 'gameStatus': 0, 'gameStatusText': '', 'period': 0, 'gameClock': '', 'gameTimeUTC': '', 'gameEt': '', 'regulationPeriods': 0, 'seriesGameNumber': '', 'seriesText': '', 'homeTeam': {'teamId': 0, 'teamName': '', 'teamCity': '', 'teamTricode': '', 'wins': 0, 'losses': 0, 'score': 0, 'inBonus': None, 'timeoutsRemaining': 0, 'periods': [{'period': 0, 'periodType': '', 'score': 0}]}, 'awayTeam': {'teamId': 0, 'teamName': '', 'teamCity': '', 'teamTricode': '', 'wins': 0, 'losses': 0, 'score': 0, 'inBonus': None, 'timeoutsRemaining': 0, 'periods': [{'period': 0, 'periodType': '', 'score': 0}]}, 'gameLeaders': {'homeLeaders': {'personId': 0, 'name': '', 'jerseyNum': '', 'position': '', 'teamTricode': '', 'playerSlug': None, 'points': 0, 'rebounds': 0, 'assists': 0}, 'awayLeaders': {'personId': 0, 'name': '', 'jerseyNum': '', 'position': '', 'teamTricode': '', 'playerSlug': None, 'points': 0, 'rebounds': 0, 'assists': 0}}, 'pbOdds': {'team': None, 'odds': 0.0, 'suspended': 0}}]}}

    #DataSets
    games = Endpoint.DataSet()
    game_date = None

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 proxy=None,
                 headers=None,
                 timeout=30,
                 get_request=True):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        if get_request:
            self.get_request()
 
    def get_request(self):
        self.nba_response = NBALiveHTTP().send_api_request(
            endpoint=self.endpoint_url,
            parameters = {},
            proxy=self.proxy,
            headers=self.headers,
            timeout=self.timeout
        )
        self.load_response()
        
    def load_response(self):
        data_sets = self.nba_response.get_dict()
        if 'scoreboard' in data_sets and 'games' in data_sets['scoreboard']:
            self.games = Endpoint.DataSet(data=data_sets['scoreboard']['games'])
            if 'gameDate' in self.games.get_dict():
                self.gamedate = Endpoint.DataSet(data=data_sets['scoreboard']['gameDate'])
