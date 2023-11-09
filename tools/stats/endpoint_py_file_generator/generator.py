import os

from .template import argument_template, no_default_argument_template
from .template import parameter_template, data_set_template, imports_template
from .template import file_template
from tools.stats.endpoint_analysis.analysis import load_endpoint_file
from tools.library.functions import get_python_variable_name
from tools.stats.library.mapping import parameter_variations, parameter_map


def get_endpoint_contents(endpoint, endpoint_analysis):
    arguments_list = []
    parameters_list = []
    data_set_lists = []
    imports_list = []

    nullable_parameters = endpoint_analysis["nullable_parameters"]
    parameters = endpoint_analysis["parameters"]
    parameter_patterns = endpoint_analysis["parameter_patterns"]
    data_sets = endpoint_analysis["data_sets"]

    parameters.sort()
    nullable_parameters.sort()

    for prop in sorted(parameters):
        if prop in nullable_parameters:
            continue
        pattern = parameter_patterns[prop]
        if pattern not in parameter_map[prop]["non-nullable"]:
            raise Exception(endpoint, pattern, prop, "non-nullable")
        parameter_key = parameter_map[prop]["non-nullable"][pattern]
        python_variable = get_python_variable_name(parameter_key)
        default_value = parameter_variations[parameter_key]["default_py_value"]
        if default_value is not None:
            if (
                default_value
                and ".default" in default_value
                and default_value.replace(".default", "") not in imports_list
            ):
                imports_list.append(default_value.replace(".default", ""))
            arguments_list.append(
                argument_template.format(
                    python_variable=python_variable, default_value=default_value
                )
            )
            parameters_list.append(
                parameter_template.format(
                    nba_parameter=prop, python_variable=python_variable
                )
            )
        else:
            # Orders parameters with no defaults first
            arguments_list.insert(
                0, no_default_argument_template.format(python_variable=python_variable)
            )
            parameters_list.insert(
                0,
                parameter_template.format(
                    nba_parameter=prop, python_variable=python_variable
                ),
            )

    for prop in nullable_parameters:
        pattern = parameter_patterns[prop]
        if pattern not in parameter_map[prop]["nullable"]:
            raise Exception(endpoint, pattern, prop, "nullable")
        parameter_key = parameter_map[prop]["nullable"][pattern]
        python_variable = get_python_variable_name(parameter_key)
        default_value = parameter_variations[parameter_key]["default_py_value"]
        if (
            default_value
            and ".default" in default_value
            and default_value.replace(".default", "") not in imports_list
        ):
            imports_list.append(default_value.replace(".default", ""))
        # Nullable parameters at the end
        arguments_list.insert(
            len(arguments_list),
            argument_template.format(
                python_variable=python_variable, default_value=default_value
            ),
        )
        parameters_list.insert(
            len(parameters_list),
            parameter_template.format(
                nba_parameter=prop, python_variable=python_variable
            ),
        )

    for key_name in data_sets:
        variable_name = get_python_variable_name(key_name)
        data_set_lists.append(
            data_set_template.format(variable_name=variable_name, key_name=key_name)
        )

    arguments = ",\n".join(arguments_list)
    parameters = ",\n".join(parameters_list)
    data_set_variables = "\n".join(data_set_lists)
    imports = ""
    if imports_list:
        imports = imports_template.format(imports_list=", ".join(imports_list))

    file_contents = file_template.format(
        imports=imports,
        endpoint=endpoint,
        endpoint_lowercase=endpoint.lower(),
        data_sets=data_sets,
        arguments=arguments,
        parameters=parameters,
        data_set_variables=data_set_variables,
    )

    return file_contents


def generate_endpoint_file(endpoint, file_contents, directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_name = "{endpoint_lowercase}.py".format(endpoint_lowercase=endpoint.lower())
    f = open(os.path.join(os.getcwd(), directory, file_name), "w")
    f.write(file_contents)
    f.close()


def generate_endpoint_files(directory="endpoint_files"):
    endpoints_information = load_endpoint_file()
    for endpoint, endpoint_analysis in endpoints_information.items():
        if endpoint_analysis["status"] != "success":
            continue
        file_contents = get_endpoint_contents(
            endpoint=endpoint, endpoint_analysis=endpoint_analysis
        )
        generate_endpoint_file(
            endpoint=endpoint, file_contents=file_contents, directory=directory
        )
