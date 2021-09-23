from nba_api.stats.library.http import NBAStatsHTTP, NBAStatsResponse
import re
from tools.stats.endpoint_analysis.data import *
from tools.stats.library.mapping import parameter_variations, parameter_map

def get_required_parameters(endpoint, nba_stats_response: NBAStatsResponse):

    # Declare an empty list to hole the required parameters
    required_parameters = []
    
    # TODO: Move to a response_validation method
    # If the response is an HTML the endpoint is likely invalid
    if re.search('<.*?>', nba_stats_response.get_response()): return required_parameters
    
    # Compile regex for parameters
    re_parameter_regex = re.compile(missing_parameter_regex)

    # Identify the index of the 'required_parameter' capture group
    # GroupIndexes start at 1 while arrays start at 0
    required_parameter_index = re_parameter_regex.groupindex['required_parameter'] - 1
    
    # Find all matches for the compiled regex
    matches = re_parameter_regex.findall(nba_stats_response.get_response())

    # Examine all matches selecting only those that have a value in the 'required_parameter' index
    for match in matches:
        
        # Assign value from index
        required_parameter = match[required_parameter_index]
        
        # Check for empty
        if not required_parameter: continue # value is empty
        
        # Check for exeptions (perhaps move to another method)
        if required_parameter == 'Runtype':
            required_parameter = 'RunType'

        # Append required parameter
        required_parameters.append(required_parameter)

# Not sure about this code
# ------------------
        # if match:
        #     raise Exception('Failed to find matches.')

        # if nba_stats_response.valid_json():
        #     continue
        # elif not required_parameter:
        #     raise Exception('Failed to find required_parameter in match.', match)
        # required_parameter = required_parameter.group(1).replace(' ', '')
# ------------------

    # Adding required parameters that need overriding
    if endpoint in missing_required_parameters:
        for parameter in missing_required_parameters[endpoint]:
            if parameter in required_parameters:
                continue
            required_parameters.append(parameter)
    return required_parameters


# This Method populates the required parameters for sending a valid GET request.
def required_parameters_test(required_parameters):
    status = 'success'

    required_params = {}
    required_params_errors = {}
    for prop in required_parameters:
        if prop in parameter_map:
            if len(parameter_map[prop]['non-nullable']):
                map_key = 'non-nullable'
            else:
                map_key = 'nullable'
            parameter_info_key = list(parameter_map[prop][map_key].values())[0]
            parameter_info = parameter_variations[parameter_info_key]
            required_params[prop] = parameter_info['parameter_value']
            required_params_errors[prop] = parameter_info['parameter_error_value']
        else:
            print('Property "{prop}" not in parameter_map'.format(prop=prop))
            status = 'invalid'
            required_params[prop] = '0'
            required_params_errors[prop] = 'a'

    return status, required_parameters, required_params, required_params_errors