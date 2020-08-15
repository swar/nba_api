# analysis.py
>/tools/endpoint_analysis/analysis.py

## Objects

### `missing_parameter_regex`

Regular expression pattern for missing parameters.
>\s*?(?:The value '[^']+' is not valid for |The )?([A-z]+\s?[A-z0-9]*?)(?:property is required\.?| is required\.?(?:, pass 0 for default)?|\.)$

### `parameter_pattern_regex`

Regular expression pattern for parameter patterns.
>\s*The field ([A-z]+) must match the regular expression '([^']+)'\.(?:;|$)

### `get_patterns_from_response`(_`nba_stats_response`_)

returns _`parameter_patterns`_

This function will return all parameter patterns from an [`NBAStatsResponse`]() class. An `exception` will be raised if a response is outputted that has not been mapped. In which case, this function will need to be edited to account for the error.

### `get_required_parameters`(_`nba_stats_response`_)

returns _`required_parameters`_

This function will return all required parameters from an [`NBAStatsResponse`]() class. An `exception` will be raised if a response is outputted that has not been mapped. In which case, this function will need to be edited to account for the error.
 

### `required_parameters_test`(_`endpoint`_)

returns _`status`_, _`required_parameters`_, _`required_params`_, _`required_params_errors`_

This function will return status, all required parameters, required params, and required params errors by submitting an empty request. 

The purpose of this test is to retrieve all required parameters so that we can use them for the `minimal_requirement_test`.
 
### `minimal_requirement_tests`(_`endpoint`_, _`required_params`_ \[, _`pause=1`_\] )

returns _`status`_, _`all_parameters`_, _`data_sets`_, _`all_params_errors`_, _`nullable_parameters`_

This function will return status, all parameters and data sets, all params errors, and initial nullable_parameters by submitting a request with valid required parameters. If any parameter fails, it will replace those matches with values from the patterns that get returned from the errors. It will retry the request and return all values.

Usually, we will be able to make endpoints work by rearranging the mapping file, but please keep in mind the impact any changes will have on any other endpoints. The point of this entire process is to accurately map as many endpoints as possible, so we may have to make additional tests in order to map all endpoints. 
 
### `nullable_parameters_test`(_`endpoint`_, _`all_parameters`_)

returns `nullable_parameters`

This function will return nullable parameters by submitting a request with empty values for all parameters. The purpose of this test is to find which parameters will allow a nullable value. Sometimes an error will be raised by this function. The error is caused by a non-nullable value that does not throw a required error when all other values are null.

### `invalid_values_test`(_`endpoint`_, _`all_params_errors`_)

returns _`parameter_patterns`_

This function will return all parameter patterns by submitting a request with invalid values. Any parameters without a matching matter will be `null`. 

The purpose of this test is to retrieve all matching patterns. In order to do that, we must submit invalid values.

### `analyze_endpoint`(_`endpoint`_ \[, _`pause=1`_\] )

returns `endpoint_analysis`

This function will conduct tests on endpoints in order to map out all parameters. This information is dumped into a `dictionary`.

**Current Tests**

1. Required Parameters Test
2. Minimal Requirement Tests
3. Nullable Parameters Test
4. Invalid Values Test


### `load_endpoint_file`( \[_`file_path=None`_, _`file_name='analysis.json'`_\] )

returns `endpoints_information`

This function will load the contents of the `file_name` into a dictionary.

### `analyze_and_save_all_endpoints`( \[_`endpoints=endpoint_list`_, _`file_path=None`_, _`file_name='analysis.json'`_, _`pause=1`_\] )

This function will analyze and save all endpoints into JSON file at the `file_path`. Please note that this function will potentially initiate 100s of requests. Each test has a maximum of 5 requests and these fetches can add up depending on the amount of endpoints.

### `analyze_endpoint_with_attempts`(_`endpoint`_ \[, _`pause=1`_, _`attempts=5`_\] )

This function will analyze an endpoint up to the amount of attempts specified. It helps when random exceptions are being thrown during this process.

### `analyze_all_endpoints_with_threading`( \[_`endpoints=endpoint_list`_, _`pause=1`_\] )

This function will analyze all endpoints with threading to increase the speed of the analysis. Please note that this function will potentially initiate 100s of requests. Each test has a maximum of 5 requests and these fetches can add up depending on the amount of endpoints.
