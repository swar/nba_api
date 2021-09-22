import re
from tools.stats.endpoint_analysis.data import *
from tools.stats.library.mapping import endpoint_list, parameter_variations, parameter_map

def get_required_parameters(endpoint, nba_stats_response):
    required_parameters = []
    if re.search('<.*?>', nba_stats_response.get_response()):  # Skip if HTML Response
        required_parameters_matches = []
    else:
        required_parameters_matches = nba_stats_response.get_response().split(';')
        if not required_parameters_matches:
            raise Exception('Failed to find matches.')
    for match in required_parameters_matches:
        required_parameter = re.match(missing_parameter_regex, match)
        if nba_stats_response.valid_json():
            continue
        elif not required_parameter:
            raise Exception('Failed to find required_parameter in match.', match)
        required_parameter = required_parameter.group(1).replace(' ', '')
        # Fix case sensitivity
        if required_parameter == 'Runtype':
            required_parameter = 'RunType'
        required_parameters.append(required_parameter)

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