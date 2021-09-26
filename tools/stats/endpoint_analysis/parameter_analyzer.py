from nba_api.stats.library.http import NBAStatsHTTP, NBAStatsResponse
import re
from tools.stats.endpoint_analysis.data import *
from tools.stats.library.mapping import parameter_variations, parameter_map

def get_required_parameters(endpoint, nba_stats_response: NBAStatsResponse):

    # Declare an empty list to hole the required parameters
    required_parameters = []
    
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
        
        # Check for exeptions (TODO perhaps move to another method)
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
def populate_required_parameters(required_parameters: dict):
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


def populate_missing_required_parameters(endpoint: str, required_parameters: dict):

    if endpoint in missing_required_parameters:
        for parameter, value in missing_required_parameters[endpoint].items():
            required_parameters[parameter] = value
    
    return required_parameters


def populate_all_parameters(all_parameters):
       # Update Parameter Pattern Mapping
    all_params = {}
    all_params_errors = {}

    # Iterate over every parameter creating a populated dictionary???
    for parameter in all_parameters:

        # If we find the parater within the known parameter map, populated it
        # with a known working value 
        if parameter in parameter_map:

            # If the parameter_map indicates that the value is non-nullable
            # the indicate this within the map_key
            if len(parameter_map[parameter]['non-nullable']):
                map_key = 'non-nullable'
            else:
                map_key = 'nullable'

            
            parameter_info_key = list(parameter_map[parameter][map_key].values())[0]
            parameter_info = parameter_variations[parameter_info_key]
            all_params[parameter] = parameter_info['parameter_value']
            all_params_errors[parameter] = parameter_info['parameter_error_value']

        # If we did not locate the parameter in the paramater_map, then this
        # must be a new parameter type that was previously undiscovered.
        else:
            print(parameter, 'not found in parameter map - minimal test')
            status = 'invalid'
            all_params[parameter] = 'a'
            all_params_errors[parameter] = 'a'

