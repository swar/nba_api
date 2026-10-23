# generator.py
>/tools/stats/endpoint_documentation_generator/generator.py

## Objects

### `get_endpoint_query_string_parameters`(_`parameters`_, _`nullable_parameters`_, _`parameter_patterns`_)

returns _`valid_url`_

This function will return the query string for a url based on the parameters, nullable properties, and parameter patterns.

### `get_endpoint_documentation`(_`endpoint`_, _`endpoints_information`_)

returns _`documentation_text`_

This function will return the entire documentation text based on the endpoint and endpoints information provided.

### `generate_boilerplate_endpoint_documentation`(_`instance`_ \[, _`directory='./docs'`_\] )

This function will generate documentation for a single endpoint from an endpoint instance (its `parameters` and `expected_data`) without running the endpoint analysis. Useful for endpoints the analyzer cannot handle.

### `generate_all_endpoint_documentation`( \[_`directory='endpoint_documentation'`_\] )

This function will generate all documentation text based on the endpoints in the endpoint_list.
