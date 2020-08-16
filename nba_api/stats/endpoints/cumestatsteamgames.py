from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueID, Season, SeasonTypeAllStar, LocationNullable, OutcomeNullable, ConferenceNullable, DivisionNullable


class CumeStatsTeamGames(Endpoint):
    endpoint = 'cumestatsteamgames'
    expected_data = {'CumeStatsTeamGames': ['MATCHUP', 'GAME_ID']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 team_id,
                 league_id=LeagueID.default,
                 season=Season.default,
                 season_type_all_star=SeasonTypeAllStar.default,
                 location_nullable=LocationNullable.default,
                 outcome_nullable=OutcomeNullable.default,
                 season_id_nullable='',
                 vs_conference_nullable=ConferenceNullable.default,
                 vs_division_nullable=DivisionNullable.default,
                 vs_team_id_nullable='',
                 proxy=None,
                 headers=None,
                 timeout=30,
                 get_request=True):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
                'TeamID': team_id,
                'LeagueID': league_id,
                'Season': season,
                'SeasonType': season_type_all_star,
                'Location': location_nullable,
                'Outcome': outcome_nullable,
                'SeasonID': season_id_nullable,
                'VsConference': vs_conference_nullable,
                'VsDivision': vs_division_nullable,
                'VsTeamID': vs_team_id_nullable
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
        self.cume_stats_team_games = Endpoint.DataSet(data=data_sets['CumeStatsTeamGames'])
