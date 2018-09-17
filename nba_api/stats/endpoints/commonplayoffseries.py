from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import Season, LeagueIDNullable


class CommonPlayoffSeries(Endpoint):
    endpoint = 'commonplayoffseries'
    expected_data = {'PlayoffSeries': ['GAME_ID', 'HOME_TEAM_ID', 'VISITOR_TEAM_ID', 'SERIES_ID', 'GAME_NUM']}

    def __init__(self,
                 season=Season.default,
                 league_id_nullable=LeagueIDNullable.default,
                 series_id_nullable=''):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={
                'Season': season,
                'LeagueID': league_id_nullable,
                'SeriesID': series_id_nullable
            },
        )
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.playoff_series = Endpoint.DataSet(data=data_sets['PlayoffSeries'])
