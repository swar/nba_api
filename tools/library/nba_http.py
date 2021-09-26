
from nba_api.stats.library.http import NBAStatsHTTP, NBAStatsResponse
import re
import time

def send_api_request(endpoint: str, parameters: list):

    # Minimum time to wait without getting throttled
    time.sleep(.600)

    # Send API request to NBA Stats endpoint
    nba_stats_response = NBAStatsHTTP().send_api_request(endpoint=endpoint,  parameters=parameters)
    return nba_stats_response

# TODO: We likely just need to be checking HTTP Return codes;
#       Though a 200 w/o JSON would indicate an issue
def validate_nba_stats_response(nba_stats_response: NBAStatsResponse):
    if '<title>NBA.com/Stats  | 404 Page Not Found </title>' in nba_stats_response.get_response():
        return 'deprecated'

    # If the response is an HTML the endpoint is likely invalid
    if re.search('<.*?>', nba_stats_response.get_response()): 
            return 'deprecated'
