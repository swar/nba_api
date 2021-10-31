from nba_api.live.nba.endpoints._base import Endpoint
from nba_api.live.nba.library.http import NBALiveHTTP

class PlayByPlay(Endpoint):
    endpoint_url = 'playbyplay/playbyplay_{game_id}.json'
    expected_data = {'meta': {'version': 1, 'code': 200, 'request': 'http://nba.cloud/games/0022000180/playbyplay?Format=json', 'time': '2021-01-15 23:48:58.906160'}, 'game': {'gameId': '0022000180', 'actions': [{'actionNumber': 4, 'clock': 'PT11M58.00S', 'timeActual': '2021-01-16T00:40:31.3Z', 'period': 1, 'periodType': 'REGULAR', 'teamId': 1610612738, 'teamTricode': 'BOS', 'actionType': 'jumpball', 'subType': 'recovered', 'descriptor': 'startperiod', 'qualifiers': [], 'personId': 1629684, 'x': None, 'y': None, 'possession': 1610612738, 'scoreHome': '0', 'scoreAway': '0', 'edited': '2021-01-16T00:40:31Z', 'orderNumber': 40000, 'xLegacy': None, 'yLegacy': None, 'isFieldGoal': 0, 'jumpBallRecoveredName': 'G. Williams', 'jumpBallRecoverdPersonId': 1629684, 'side': None, 'playerName': 'Williams', 'playerNameI': 'G. Williams', 'personIdsFilter': [1629684, 202684, 202696], 'jumpBallWonPlayerName': 'Thompson', 'jumpBallWonPersonId': 202684, 'description': 'Jump Ball T. Thompson vs. N. Vucevic: Tip to G. Williams', 'jumpBallLostPlayerName': 'Vucevic', 'jumpBallLostPersonId': 202696}]}}

    #Data Sets
    game = Endpoint.DataSet
    officials = Endpoint.DataSet
    home_team = Endpoint.DataSet
    away_team = Endpoint.DataSet

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 game_id,
                 proxy=None,
                 headers=None,
                 timeout=30,
                 get_request=True):
        self.game_id = game_id
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        if get_request:
            self.get_request()
 
    def get_request(self):
        self.nba_response = NBALiveHTTP().send_api_request(
            endpoint=self.endpoint_url.format(game_id=self.game_id),
            parameters = {},
            proxy=self.proxy,
            headers=self.headers,
            timeout=self.timeout
        )
        self.load_response()
        
    def load_response(self):
        data_sets = self.nba_response.get_dict()
        if 'game' in data_sets and 'actions' in data_sets['game']:
            self.actions = Endpoint.DataSet(data=data_sets['game']['actions'])
