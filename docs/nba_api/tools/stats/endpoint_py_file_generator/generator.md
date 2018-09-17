# generator.py
>/tools/endpoint_py_file_generator/generator.py

## Objects

### `get_endpoint_contents`(_`endpoint`_, _`endpoint_analysis`_)

returns _`file_contents`_

This function will return the contents of the .py file for that specific endpoint.

### `generate_endpoint_file`(_`endpoint`_, _`file_contents`_)

This function will create the .py file for the endpoint and file contents inputted.

### `generate_endpoint_files` ( \[_`endpoints_information=load_endpoint_file()`_\] )

This function will create all the .py files from the endpoints information file.
