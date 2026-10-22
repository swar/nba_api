# generator.py
>/tools/stats/endpoint_py_file_generator/generator.py

## Objects

### `get_endpoint_contents`(_`endpoint`_, _`endpoint_analysis`_)

returns _`file_contents`_

This function will return the contents of the .py file for that specific endpoint.

### `generate_endpoint_file`(_`endpoint`_, _`file_contents`_, _`directory`_)

This function will create the .py file for the endpoint and file contents inputted.

### `generate_endpoint_files`( \[_`directory='endpoint_files'`_\] )

This function will create all the .py files from the endpoint analysis file (loaded with `load_endpoint_file()`).
