import json
import threading
import time

from datetime import datetime
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import *
from tools.library.file_handler import load_file, save_file, get_file_path
from tools.library import nba_http
from tools.stats.library.mapping import endpoint_list, parameter_variations, parameter_map
from tools.library.nba_http import *
from tools.stats.endpoint_analysis.data import *
from tools.stats.endpoint_analysis.parameter_analyzer import *
from tools.stats.endpoint_analysis.pattern_analyzer import *

# def get_patterns_from_response(nba_stats_response): <-- Abstracted to pattern_analyzer.py
    
def minimal_requirement_tests(endpoint, required_params, pause=1):
    status = 'success'
    all_parameters = list(required_params.keys())

    # Populate required parameters for endpoints that do not pro
    required_params = populate_missing_required_parameters(endpoint, required_params)

    # Send NBA Stats API request with minimum required parameters. The goal is to seek a 200 HTTP Response Code.
    nba_stats_response = nba_http.send_api_request(endpoint=endpoint, parameters=required_params)

    # TODO: Fix Pattern Code 
    # 2. minimal requirement test with pattern matching
    # if not nba_stats_response.valid_json():
    #     parameter_patterns = get_patterns_from_response(nba_stats_response=nba_stats_response)
    #     # Overwrites param with parameter patterns on mismatches.
    #     for prop in required_params.keys():
    #         if prop in parameter_patterns:
    #             pattern = parameter_patterns[prop]
    #             if pattern in parameter_map[prop]['non-nullable']:
    #                 map_key = 'non-nullable'
    #             else:
    #                 map_key = 'nullable'
    #             parameter_info_key = parameter_map[prop][map_key][pattern]
    #             parameter_info = parameter_variations[parameter_info_key]
    #             required_params[prop] = parameter_info['parameter_value']
    #     time.sleep(pause)
    #     nba_stats_response = NBAStatsHTTP().send_api_request(endpoint=endpoint, parameters=required_params)

    # If we receive a valid json response then we can pull the datasets & headers form the return
    if nba_stats_response.valid_json():
        data_sets = nba_stats_response.get_headers_from_data_sets()
        all_parameters += list(nba_stats_response.get_parameters().keys())
    else:
        status = 'invalid'
        print(status, 'failed to pass minimal values test')
        data_sets = {}
    all_parameters = list(set(all_parameters))

    # populated_parameters = populate_all_parameters(all_parameters)

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

    nullable_parameters = []
    if nba_stats_response.get_parameters():
        response_parameters = nba_stats_response.get_parameters()
        for parameter, value in response_parameters.items():
            if value is None or value == "":
                nullable_parameters.append(parameter)

        for parameter in all_parameters:
            if parameter in response_parameters.keys():
                continue
            if endpoint in missing_required_parameters and parameter in missing_required_parameters[endpoint] \
                    and missing_required_parameters[endpoint][parameter]:
                continue
            nullable_parameters.append(parameter)

        nullable_parameters = list(set(nullable_parameters))

    return status, all_parameters, data_sets, all_params_errors, nullable_parameters


def nullable_parameters_test(endpoint, all_parameters):
    skip_endpoints = ['boxscoreadvancedv2', 'boxscorefourfactorsv2', 'boxscoremiscv2', 'boxscorescoringv2',
                      'boxscoretraditionalv2', 'boxscoreusagev2', 'winprobabilitypbp', 'alltimeleadersgrids',
                      'boxscoresimilarityscore', 'glalumboxscoresimilarityscore', 'playerestimatedmetrics',
                      'playertrackbucketsimilarityscore', 'playertrackranksimilaritycomp', 'playertracksimilarityscore',
                      'playertracksimilarityuniqueness', 'synergybucketsimilarityscore', 'synergysimilarityscore',
                      'teamestimatedmetrics']

    if endpoint.lower() in skip_endpoints:
        return []

    non_nullable_list = ['DefenseCategory']

    params = {prop: '' for prop in all_parameters if prop not in non_nullable_list and endpoint in missing_required_parameters and prop not in missing_required_parameters[endpoint]}
    nba_stats_response = NBAStatsHTTP().send_api_request(endpoint=endpoint, parameters=params)

    if 'An error has occurred.' in nba_stats_response.get_response() \
            or 'A value is required' in nba_stats_response.get_response():
        raise Exception('Failed to pass nullable parameters test. Possibly non-nullable value failing.')

    required_parameters = get_required_parameters(endpoint, nba_stats_response)
    nullable_parameters = [prop for prop in list(params.keys()) if prop not in required_parameters]
    if nba_stats_response.get_parameters():
        response_parameters = nba_stats_response.get_parameters()
        for parameter, value in response_parameters.items():
            if value is None or value == "":
                nullable_parameters.append(parameter)

        for parameter in all_parameters:
            if parameter in response_parameters.keys():
                continue
            if parameter in missing_required_parameters[endpoint] and missing_required_parameters[endpoint][parameter]:
                continue
            nullable_parameters.append(parameter)

    print(nullable_parameters)

    return nullable_parameters


def invalid_values_test(endpoint, all_params_errors):
    nba_stats_response = NBAStatsHTTP().send_api_request(endpoint=endpoint, parameters=all_params_errors)

    parameter_patterns = get_patterns_from_response(nba_stats_response=nba_stats_response)

    for param in list(all_params_errors.keys()):
        if param not in parameter_patterns:
            parameter_patterns[param] = None

    return parameter_patterns


def clean_parameters(endpoint, all_parameters, required_parameters, nullable_parameters, parameter_patterns):
    all_parameters = list(set(all_parameters))
    required_parameters = list(set(required_parameters))
    nullable_parameters = list(set(nullable_parameters))

    if endpoint not in parameter_override and endpoint not in remove_nullable_parameters:
        return all_parameters, required_parameters, nullable_parameters, parameter_patterns

    parameters = remove_nullable_parameters.get(endpoint, [])
    for parameter in parameters:
        if parameter in nullable_parameters:
            nullable_parameters.remove(parameter)

    parameters = parameter_override[endpoint]
    for old_parameter, new_parameter in parameters.items():
        if old_parameter in all_parameters:
            all_parameters.remove(old_parameter)
            all_parameters.append(new_parameter)
        if old_parameter in required_parameters:
            required_parameters.remove(old_parameter)
            required_parameters.append(new_parameter)
        if old_parameter in nullable_parameters:
            nullable_parameters.remove(old_parameter)
            nullable_parameters.append(new_parameter)
        if old_parameter in parameter_patterns:
            parameter_patterns[new_parameter] = parameter_patterns[old_parameter]
            del parameter_patterns[old_parameter]

    all_parameters = list(set(all_parameters))
    required_parameters = list(set(required_parameters))
    nullable_parameters = list(set(nullable_parameters))

    return all_parameters, required_parameters, nullable_parameters, parameter_patterns


def analyze_endpoint(endpoint, pause=1):

    # Send Initial Call to NBA
    nba_stats_response = nba_http.send_api_request(endpoint=endpoint, parameters={})

    # Get Required Parameters
    required_parameters = get_required_parameters(endpoint, nba_stats_response)

    # Testing endpoint with parameters that throw a require flag.
    status, required_parameters, required_params, required_params_errors = populate_required_parameters(required_parameters=required_parameters)

    # No need to continue if Endpoint is deprecated.
    if status == 'deprecated':
        return {'status': status, 'endpoint': endpoint, 'last_validated_date': str(datetime.now().date())}

    # Testing endpoint with the minimal amount of parameters required.
    status_test, all_parameters, data_sets, all_params_errors, nullable_parameters = \
        minimal_requirement_tests(endpoint=endpoint, required_params=required_params)

    if status_test == 'invalid':
        status = status_test

    # Testing endpoint with all parameters with empty values to see which ones are allowed to be nullable.
    nullable_parameters += nullable_parameters_test(endpoint=endpoint, all_parameters=all_parameters)
    nullable_parameters = list(set(nullable_parameters))

    # Testing endpoint with invalid values to grab matching patterns.
    parameter_patterns = {}
    parameter_patterns = invalid_values_test(endpoint=endpoint, all_params_errors=all_params_errors)

    if len(parameter_patterns) != len(all_parameters):
        print(endpoint, 'length of patterns does not equal all our parameters', parameter_patterns, all_parameters)
        status = 'invalid'

    all_parameters, required_parameters, nullable_parameters, parameter_patterns = clean_parameters(
        endpoint=endpoint,
        all_parameters=all_parameters,
        required_parameters=required_parameters,
        nullable_parameters=nullable_parameters,
        parameter_patterns=parameter_patterns
    )

    all_parameters.sort()
    required_parameters.sort()
    nullable_parameters.sort()

    endpoint_analysis = {
        'status': status,
        'endpoint': endpoint,
        'parameters': all_parameters,
        'required_parameters': required_parameters,
        'nullable_parameters': nullable_parameters,
        'parameter_patterns': parameter_patterns,
        'data_sets': data_sets,
        'last_validated_date': str(datetime.now().date()),
    }

    return endpoint_analysis


def load_endpoint_file(file_path=None, file_name='analysis.json'):
    if not file_path:
        file_path = get_file_path(directory_name='endpoint_analysis')
    try:
        endpoints_information = json.loads(load_file(file_path=file_path, file_name=file_name))
    except FileNotFoundError:
        endpoints_information = {}
    except ValueError:
        raise Exception('Endpoint file is not in valid a JSON format.')

    return endpoints_information


def analyze_and_save_all_endpoints(endpoints=endpoint_list, file_path=None, file_name='analysis.json', pause=1):
    if not file_path:
        file_path = get_file_path(directory_name='endpoint_analysis')
    endpoints_information = load_endpoint_file(file_name=file_name, file_path=file_path)

    for endpoint in endpoints:
        attempts = 0
        while attempts < 5:
            attempts += 1
            try:
                if endpoint in endpoints_information and endpoints_information[endpoint]['status'] in ['success', 'deprecated']:
                    print("skipping", endpoints_information[endpoint]['status'], endpoint)
                    continue

                endpoint_analysis = analyze_endpoint(endpoint=endpoint, pause=pause)
                endpoints_information[endpoint] = endpoint_analysis
                time.sleep(pause)

                contents = json.dumps(endpoints_information, sort_keys=True, indent=4)
                save_file(file_path=file_path, file_name=file_name, contents=contents)
                print(endpoint_analysis['status'], endpoint)
                break
            except:
                pass


def analyze_endpoint_with_attempts(endpoint, pause=1, attempts=5):
    attempt = 0
    while attempt <= attempts:
        attempt += 1
        try:
            return analyze_endpoint(endpoint=endpoint, pause=pause)
        except:
            pass


def analyze_all_endpoints_with_threading(endpoints=endpoint_list, pause=1):
    threads = {}

    for endpoint in endpoints:
        analyze_endpoint_with_attempts(endpoint, pause=1, attempts=1)
    #     t = threading.Thread(target=analyze_endpoint_with_attempts, kwargs=dict(endpoint=endpoint, pause=pause, attempts=10))
    #     threads[endpoint] = t
    #     t.start()

    # is_alive = True
    # while is_alive:
    #     print('>'*25)
    #     is_alive = False
    #     for key, thread in threads.items():
    #         if thread.is_alive():
    #             print(key, thread.is_alive())
    #             is_alive = True
    #     time.sleep(1)
