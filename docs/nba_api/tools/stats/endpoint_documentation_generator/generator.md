# generator.py
>/tools/endpoint_py_file_generator/generator.py

## Objects

### `get_endpoint_query_string_parameters`(_`parameters`_, _`nullable_parameters`_, _`parameter_patterns`_)

returns _`valid_url`_

This function will return the query string for a url based on the parameters, nullable properties, and parameter patterns.

### `get_endpoint_documentation`(_`endpoint`_, _`endpoints_information`_)

returns _`documentation_text`_

This function will return the entire documentation text based on the endpoint and endpoints information provided.

### `generate_all_endpoint_documentation`( \[_`directory='endpoint_documentation'`_\] )

This function will generate all documentation text based on the endpoints in the endpoint_list.
