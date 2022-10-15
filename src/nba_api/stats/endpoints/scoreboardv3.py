from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import DayOffset, GameDate, LeagueID


class ScoreboardV3(Endpoint):
    endpoint = 'scoreboardv3'

    expected_data = {"meta":{"version":1,"request":"http://nba.cloud/league/00/2022/10/14/scoreboard?Format=json","time":"2022-10-15T00:32:46.3246Z"},"scoreboard":{"gameDate":"2022-10-14","leagueId":"00","leagueName":"National Basketball Association","games":[{"gameId":"0012200062","gameCode":"20221014/HOUIND","gameStatus":3,"gameStatusText":"Final","period":4,"gameClock":"","gameTimeUTC":"2022-10-14T23:00:00Z","gameEt":"2022-10-14T19:00:00Z","regulationPeriods":4,"seriesGameNumber":"","seriesText":"","ifNecessary":False,"gameLeaders":{"homeLeaders":{"personId":1631097,"name":"Bennedict Mathurin","playerSlug":"bennedict-mathurin","jerseyNum":"00","position":"G-F","teamTricode":"IND","points":18,"rebounds":5,"assists":3},"awayLeaders":{"personId":1630224,"name":"Jalen Green","playerSlug":"jalen-green","jerseyNum":"0","position":"G","teamTricode":"HOU","points":33,"rebounds":1,"assists":3}},"teamLeaders":{"homeLeaders":{"personId":1631097,"name":"Bennedict Mathurin","playerSlug":"bennedict-mathurin","jerseyNum":"00","position":"G-F","teamTricode":"IND","points":19.8,"rebounds":3.8,"assists":1.3},"awayLeaders":{"personId":1630224,"name":"Jalen Green","playerSlug":"jalen-green","jerseyNum":"0","position":"G","teamTricode":"HOU","points":22.0,"rebounds":3.0,"assists":3.3},"seasonLeadersFlag":0},"broadcasters":{"nationalBroadcasters":[],"homeTvBroadcasters":[{"broadcasterId":1000341,"broadcastDisplay":"BSIN"}],"homeRadioBroadcasters":[],"awayTvBroadcasters":[{"broadcasterId":1000208,"broadcastDisplay":"Rockets.com"}],"awayRadioBroadcasters":[{"broadcasterId":1000704,"broadcastDisplay":"KBME/KAMA-HD2"}]},"homeTeam":{"teamId":1610612754,"teamName":"Pacers","teamCity":"Indiana","teamTricode":"IND","teamSlug":"pacers","wins":2,"losses":2,"score":114,"seed":0,"inBonus":None,"timeoutsRemaining":0,"periods":[{"period":1,"periodType":"REGULAR","score":29}]},"awayTeam":{"teamId":1610612745,"teamName":"Rockets","teamCity":"Houston","teamTricode":"HOU","teamSlug":"rockets","wins":3,"losses":1,"score":122,"seed":0,"inBonus":None,"timeoutsRemaining":1,"periods":[{"period":1,"periodType":"REGULAR","score":39}]}}]}}

    nba_response = None
    data_sets = None
    score_board_date = None
    games = None
    headers = None

    def __init__(self,
                 game_date=GameDate.default,
                 league_id=LeagueID.default,
                 proxy=None,
                 headers=None,
                 timeout=30,
                 get_request=True):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout

        self.parameters = {
            'GameDate': game_date,
            'LeagueID': league_id
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
        data_sets = self.nba_response.get_dict()

        if 'scoreboard' in data_sets:
            self.score_board_date = data_sets['scoreboard']['gameDate']

            if 'games' in data_sets['scoreboard']:
                self.games = Endpoint.DataSet(data=data_sets['scoreboard']['games'])
