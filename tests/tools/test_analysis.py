from nba_api.library.http import NBAHTTP
from nba_api.stats.library.http import NBAStatsHTTP, NBAStatsResponse
# from tools.stats.endpoint_analysis.parameters_analyzer import get_all_parameters_from_response, get_required_parameters_from_response, populate_all_parameters, populate_required_parameters
from tools.stats.library.mapping import parameter_map, parameter_variations
from tools.stats.endpoint_analysis.analysis import *
from tests.tools.data import nba_stats_response_400, nba_stats_response_200

# test_get_required_parameters_from_response
def test_get_required_parameters(monkeypatch):
   
    def mock_send_api_request(*args, **kwargs):
        return nba_stats_response_400

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(NBAStatsHTTP, "send_api_request", mock_send_api_request)

    nba_stats_response = NBAStatsHTTP.send_api_request('https://stats.nba.com/stats/PlayerIndex', {})

    required_parameters = get_required_parameters(endpoint='PlayerIndex', nba_stats_response=nba_stats_response)
    
    assert required_parameters == ['LeagueID', 'Season']

