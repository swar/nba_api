import sys
import inspect

from .template import (
    header_template,
    regex_pattern_body_template,
    regex_pattern_line_template,
)
from .template import variable_body_template, variable_line_template

from nba_api.stats.library import parameters
from tools.library.file_handler import save_file, get_file_path
from tools.stats.library.mapping import parameter_map, parameter_variations


def _get_class_information(cls, variable_names_to_exclude=None):
    if not variable_names_to_exclude:
        variable_names_to_exclude = []
    variables = []
    default = getattr(cls, "default")
    for var in dir(cls):
        variable = {}

        if "__" in var or var == "default" or var in variable_names_to_exclude:
            continue

        var_name = var
        is_function = False
        if inspect.isfunction(var):
            is_function = True
            var_name = "{var_name}()".format(var_name=var_name)

        default_value = getattr(cls, var)
        variable["name"] = var_name
        variable["default_value"] = default_value
        variable["default"] = default_value == default
        variable["function"] = is_function
        variable_names_to_exclude.append(var)
        variables.append(variable)
    return variables, variable_names_to_exclude


def get_library_classes(module=parameters):
    library_classes = {}
    classes = inspect.getmembers(sys.modules[module.__name__], inspect.isclass)
    for name, cls in classes:
        if name == cls.__module__:  # Skip imports
            continue
        variables, variable_names = _get_class_information(cls=cls)
        for c in cls.mro():  # Check parent classes as well.
            if name == c.__module__:  # Skip imports
                continue
            additional_variables, variable_names = _get_class_information(
                cls=cls, variable_names_to_exclude=variable_names
            )
            variables += additional_variables
            library_classes[name] = variables
    return library_classes


def get_parameter_map_parameters():
    parameters = list(parameter_map.keys())
    parameters.sort()
    return parameters


def get_parameter_map_patterns():
    parameter_patterns = {}
    for parameter in get_parameter_map_parameters():
        pattern_info = {}
        nullable_dict = parameter_map[parameter]["nullable"]
        non_nullable_dict = parameter_map[parameter]["non-nullable"]
        for pattern, pattern_key in nullable_dict.items():
            if pattern_key not in pattern_info:
                pattern_info[pattern_key] = [pattern]
            else:
                pattern_info[pattern_key].append(pattern)

        for pattern, pattern_key in non_nullable_dict.items():
            if pattern_key not in pattern_info:
                pattern_info[pattern_key] = [pattern]
            else:
                pattern_info[pattern_key].append(pattern)
        parameter_patterns[parameter] = pattern_info
    return parameter_patterns


def _get_variable_table_from_library_class(library_class):
    variable_lines = []
    for variable in library_class:
        name = variable["name"]
        value = variable["default_value"]
        is_default = variable["default"]
        is_function = variable["function"]
        additional_tags = []
        if is_default:
            additional_tags.append("`default` ")
        if is_function:
            additional_tags.append("`function` ")
        if additional_tags:
            additional_tags = " ".join(additional_tags)
        else:
            additional_tags = ""
        if callable(value):
            value = "{}()".format(name)
        variable_line = variable_line_template.format(
            name=name, value=value, additional_tags=additional_tags
        ).replace("``", "")
        if is_default:
            variable_lines.insert(0, variable_line)
        else:
            variable_lines.append(variable_line)
    variable_body = variable_body_template.format(variables="\n".join(variable_lines))
    return variable_body


def _get_class_documentation_text(parameter, pattern_info, library_classes):
    file_contents = header_template.format(parameter_name=parameter)
    empty_contents = False
    for pattern_key in sorted(pattern_info.keys()):
        patterns = pattern_info[pattern_key]
        regex_patterns = [
            regex_pattern_line_template.format(pattern=pattern)
            for pattern in patterns
            if pattern
        ]
        default_py_value = parameter_variations[pattern_key]["default_py_value"]
        if default_py_value and ".default" in default_py_value:
            default_py_value = default_py_value.replace(".default", "")
            class_name = default_py_value
            if regex_patterns:
                file_contents += regex_pattern_body_template.format(
                    regex_patterns="\n".join(regex_patterns), python_class=class_name
                )
            variable_body = _get_variable_table_from_library_class(
                library_class=library_classes[class_name]
            )
            file_contents += variable_body
        else:
            empty_contents = True
    if empty_contents:
        file_contents += "No available information.\n\n"
    return file_contents


def get_parameter_documentation_text():
    library_classes = get_library_classes()
    parameter_patterns = get_parameter_map_patterns()
    file_contents = "# Endpoint Parameters\n\n"
    for parameter, pattern_info in parameter_patterns.items():
        file_contents += _get_class_documentation_text(
            parameter=parameter,
            pattern_info=pattern_info,
            library_classes=library_classes,
        )
    return file_contents


def generate_parameter_documentation_file(
    directory="parameter_documentation", file_name="parameters.md"
):
    contents = get_parameter_documentation_text()
    file_path = get_file_path(directory)
    save_file(file_path=file_path, file_name=file_name, contents=contents)
