import json

from tools.library.file_handler import save_file
from tools.stats.library.mapping import endpoint_list
from tools.stats.endpoint_analysis import analysis as endpoint_analysis
from tools.stats.endpoint_py_file_generator import generator as py_file_generator
from tools.stats.endpoint_documentation_generator import generator as endpoint_documentation_generator
from tools.stats.parameter_documentation_generator import generator as parameter_documentation_generator


# List of specific endpoints to analyze
USER_ENDPOINTS = ['CommonPlayoffSeries']
# USER_ENDPOINTS = endpoint_list  # To analyze all endpoints


# If True, will output a complete analysis.json file at end which can be used to compare w/ existing analysis.json file
# WILL NOT OVERWRITE EXISTING analysis_archive/stats/analysis.json file
COMBINE_WITH_EXISTING_ANALYSIS_JSON_AT_END = True


def valid_endpoints_remaining():
    endpoints_information = endpoint_analysis.load_endpoint_file()
    endpoints_remaining = False

    for endpoint, endpoint_data in endpoints_information.items():
        if endpoint_data['status'] == 'success':
            return True

    return endpoints_remaining


def create_new_analysis_json():
    file_path_existing_analysis = '../analysis_archive/stats'
    file_path_new_analysis = 'endpoint_analysis'
    existing_analysis_json = endpoint_analysis.load_endpoint_file(file_path=file_path_existing_analysis)
    new_analysis_json = endpoint_analysis.load_endpoint_file(file_path=file_path_new_analysis)

    if not existing_analysis_json or not new_analysis_json:
        print(f"{file_path_existing_analysis}/analysis.json and/or {file_path_new_analysis}/analysis.json could "
              f"not be loaded correctly")
        return

    for endpoint, endpoint_data in new_analysis_json.items():
        existing_analysis_json[endpoint] = endpoint_data

    existing_analysis_json = json.dumps(existing_analysis_json, sort_keys=True, indent=4)
    save_file(file_path=file_path_new_analysis, file_name='complete_analysis.json', contents=existing_analysis_json)
    print("Completed file can be found @ {file_path_new_analysis}/complete_analysis.json")


def analyze_endpoints_and_create_files(endpoints):

    # Second item of each tuple is True if endpoints are needed as keyword argument
    steps_to_complete = [
        (py_file_generator.generate_endpoint_file, False),
        (endpoint_documentation_generator.generate_endpoint_documentation, True),
        (parameter_documentation_generator.generate_parameter_documentation_file, False)
    ]

    # Initial endpoint analysis will generate needed analysis.json file for file & doc generators
    if not endpoints or type(endpoints) != list:
        print("Initial endpoints not valid. Check length > 0 and is a valid list.")
        steps_to_complete = []
    else:
        endpoint_analysis.analyze_and_save_endpoints(endpoints=endpoints)

    for next_step in steps_to_complete:
        # Check generated analysis.json file at each step to ensure there's a valid endpoint worth continuing for
        if not valid_endpoints_remaining():
            print("No valid endpoints remain, stopped before:", next_step[0].__name__)
            steps_to_complete = []
            break
        if next_step[1]:
            next_step[0](endpoints=endpoints)
        else:
            next_step[0]()

    if steps_to_complete and COMBINE_WITH_EXISTING_ANALYSIS_JSON_AT_END:
        create_new_analysis_json()


analyze_endpoints_and_create_files(USER_ENDPOINTS)
