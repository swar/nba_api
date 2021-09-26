
import re
from tools.stats.endpoint_analysis.data import parameter_pattern_regex, missing_parameter_regex

def get_patterns_from_response(nba_stats_response):
    parameter_patterns = {}

    # TODO: Move to a response_validation method
    # If the response is an HTML the endpoint is likely invalid
    if re.search('<.*?>', nba_stats_response.get_response()): return []
    
    # The NBA Stats returns text delimited by a ';'.
    # Spltting on the ';' allows us to inspect each of the messages.
    matches = nba_stats_response.get_response().split(';')

    re_missing_parameter_regex = re.compile(missing_parameter_regex)

    invalid_parameter_index = re_missing_parameter_regex.groupindex['invalid_parameter'] - 1

    for match in matches:
        parameter_regex_match = re.match(parameter_pattern_regex, match)
        invalid_parameter_match = re_missing_parameter_regex.findall(match)
        # invalid_parameter_match = re.match(missing_parameter_regex, match)
        prop = None
        pattern = None
        
        if parameter_regex_match:
            prop = parameter_regex_match.group(1)
            pattern = parameter_regex_match.group(2)
            prop = prop.replace(' ', '')
        elif invalid_parameter_match:
            prop = invalid_parameter_match[0][invalid_parameter_index]
            prop = prop.replace(' ', '')
        elif match in [' Invalid date', '<Error><Message>An error has occurred.</Message></Error>', 'Invalid game date',
                       ' Invalid game date', 'Invalid parameters', ' Invalid parameters', 'Invalid parameter', ' Invalid parameter']:
            pass
        elif nba_stats_response.valid_json():
            pass
        elif not parameter_regex_match and not invalid_parameter_match and 'Invalid date' not in nba_stats_response.get_response() and 'must be between' not in nba_stats_response.get_response():
            raise Exception('Failed to match error.', match)

        if prop:
            parameter_patterns[prop] = pattern

    return parameter_patterns