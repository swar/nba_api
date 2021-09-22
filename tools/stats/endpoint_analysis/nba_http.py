
from nba_api.stats.library.http import NBAStatsHTTP, NBAStatsResponse
import time

def send_api_request(endpoint: str, parameters: list):

    # Minimum time to wait without getting throttled
    time.sleep(.600)

    # Send API request to NBA Stats endpoint
    nba_stats_response = NBAStatsHTTP().send_api_request(endpoint=endpoint,  parameters=parameters)
    return nba_stats_response

def validate_nba_stats_response(nba_stats_response: NBAStatsResponse):
    if '<title>NBA.com/Stats  | 404 Page Not Found </title>' in nba_stats_response.get_response():
        status = 'deprecated'
        return status, None, None, None