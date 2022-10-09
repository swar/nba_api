from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueID, SeasonYear, SeasonType


class GLAlumBoxScoreSimilarityScore(Endpoint):
    endpoint = 'glalumboxscoresimilarityscore'
    expected_data = {'GLeagueAlumBoxScoreSimilarityScores': ['PERSON_2_ID', 'PERSON_2', 'TEAM_ID', 'SIMILARITY_SCORE']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 person2_id,
                 person1_id,
                 person1_league_id=LeagueID.default,
                 person1_season_year=SeasonYear.default,
                 person1_season_type=SeasonType.default,
                 person2_league_id=LeagueID.default,
                 person2_season_year=SeasonYear.default,
                 person2_season_type=SeasonType.default,
                 proxy=None,
                 headers=None,
                 timeout=30,
                 get_request=True):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
                'Person2Id': person2_id,
                'Person1Id': person1_id,
                'Person1LeagueId': person1_league_id,
                'Person1Season': person1_season_year,
                'Person1SeasonType': person1_season_type,
                'Person2LeagueId': person2_league_id,
                'Person2Season': person2_season_year,
                'Person2SeasonType': person2_season_type
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
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.g_league_alum_box_score_similarity_scores = Endpoint.DataSet(data=data_sets['GLeagueAlumBoxScoreSimilarityScores'])
