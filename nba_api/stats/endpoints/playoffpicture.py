from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueID, SeasonID


class PlayoffPicture(Endpoint):
    endpoint = 'playoffpicture'
    expected_data = {'EastConfPlayoffPicture': ['CONFERENCE', 'HIGH_SEED_RANK', 'HIGH_SEED_TEAM', 'HIGH_SEED_TEAM_ID', 'LOW_SEED_RANK', 'LOW_SEED_TEAM', 'LOW_SEED_TEAM_ID', 'HIGH_SEED_SERIES_W', 'HIGH_SEED_SERIES_L', 'HIGH_SEED_SERIES_REMAINING_G', 'HIGH_SEED_SERIES_REMAINING_HOME_G', 'HIGH_SEED_SERIES_REMAINING_AWAY_G'], 'EastConfRemainingGames': ['TEAM', 'TEAM_ID', 'REMAINING_G', 'REMAINING_HOME_G', 'REMAINING_AWAY_G'], 'EastConfStandings': ['CONFERENCE', 'RANK', 'TEAM', 'TEAM_ID', 'WINS', 'LOSSES', 'PCT', 'DIV', 'CONF', 'HOME', 'AWAY', 'GB', 'GR_OVER_500', 'GR_OVER_500_HOME', 'GR_OVER_500_AWAY', 'GR_UNDER_500', 'GR_UNDER_500_HOME', 'GR_UNDER_500_AWAY', 'RANKING_CRITERIA', 'CLINCHED_PLAYOFFS', 'CLINCHED_CONFERENCE', 'CLINCHED_DIVISION', 'ELIMINATED_PLAYOFFS', 'SOSA_REMAINING'], 'WestConfPlayoffPicture': ['CONFERENCE', 'HIGH_SEED_RANK', 'HIGH_SEED_TEAM', 'HIGH_SEED_TEAM_ID', 'LOW_SEED_RANK', 'LOW_SEED_TEAM', 'LOW_SEED_TEAM_ID', 'HIGH_SEED_SERIES_W', 'HIGH_SEED_SERIES_L', 'HIGH_SEED_SERIES_REMAINING_G', 'HIGH_SEED_SERIES_REMAINING_HOME_G', 'HIGH_SEED_SERIES_REMAINING_AWAY_G'], 'WestConfRemainingGames': ['TEAM', 'TEAM_ID', 'REMAINING_G', 'REMAINING_HOME_G', 'REMAINING_AWAY_G'], 'WestConfStandings': ['CONFERENCE', 'RANK', 'TEAM', 'TEAM_ID', 'WINS', 'LOSSES', 'PCT', 'DIV', 'CONF', 'HOME', 'AWAY', 'GB', 'GR_OVER_500', 'GR_OVER_500_HOME', 'GR_OVER_500_AWAY', 'GR_UNDER_500', 'GR_UNDER_500_HOME', 'GR_UNDER_500_AWAY', 'RANKING_CRITERIA', 'CLINCHED_PLAYOFFS', 'CLINCHED_CONFERENCE', 'CLINCHED_DIVISION', 'ELIMINATED_PLAYOFFS', 'SOSA_REMAINING']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 league_id=LeagueID.default,
                 season_id=SeasonID.default,
                 proxy=None,
                 headers=None,
                 timeout=30,
                 get_request=True):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
                'LeagueID': league_id,
                'SeasonID': season_id
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
        self.east_conf_playoff_picture = Endpoint.DataSet(data=data_sets['EastConfPlayoffPicture'])
        self.east_conf_remaining_games = Endpoint.DataSet(data=data_sets['EastConfRemainingGames'])
        self.east_conf_standings = Endpoint.DataSet(data=data_sets['EastConfStandings'])
        self.west_conf_playoff_picture = Endpoint.DataSet(data=data_sets['WestConfPlayoffPicture'])
        self.west_conf_remaining_games = Endpoint.DataSet(data=data_sets['WestConfRemainingGames'])
        self.west_conf_standings = Endpoint.DataSet(data=data_sets['WestConfStandings'])
