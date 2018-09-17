# generator.py
>/tools/parameter_documentation_generator/generator.py

## Objects

### `_get_class_information`(_`cls`_, \[_`variable_names_to_exclude=None`_\] )

returns _`variables`_, _`variable_names_to_exclude`_

This function will return variables inside of a class, as well as additional information such as if the variable is a default value or if it is a function.

### `get_library_classes`( \[_`module=mapping`_\] )

This function will return a dictionary of library classes that contains classes and their variable contents.

### `get_parameter_map_parameters`( )

returns _`parameters`_

This function will return all parameters inside of our [`parameter_map`]().

### `get_parameter_map_patterns`( )

returns _`parameters`_

This function will return a dictionary of all parameter patterns inside of our [`parameter_map`]().

### `_get_variable_table_from_library_class`(_`library_class`_)

returns _`variable_body`_

This function will return the formatted variable body of the documentation.

### `_get_class_documentation_text`(_`parameter`_, _`pattern_info`_, _`library_classes`_)

returns _`file_contents`_

This function will return the contents of the documentation for the specified pattern information.

### `get_parameter_documentation_text`( )

returns _`file_contents`_

This function will return the file contents of the parameter documentation file.

### `generate_parameter_documentation_file`( \[_`directory='parameter_documentation'`_, _`file_name='endpoint_parameters.md'`_\] )

This function will generate the documentation file for the `parameters.py` file.
