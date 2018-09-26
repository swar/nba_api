# Endpoint Analysis Format

### Endpoint Analysis JSON Format
```json
{
    "{endpoint}": {
        "status": "{status}",
        "endpoint": "{endpoint}",
        "data_sets": {},
        "parameters": [],
        "required_parameters": [],
        "nullable_parameters": [],
        "parameters_patterns": {
            "{property}": "{pattern}",
        }
    }
}
```

Name | Explanation
------------ | -------------
_**status**_ | This field will be 'success' or 'fail'. Success statuses have passed all tests required by the endpoint analysis.
_**endpoint**_ | The name of the endpoint.
_**data_sets**_ | The data sets that are returned by the endpoint and their data headers.
_**parameters**_ | All parameters for the endpoint.
_**required_parameters**_ | All parameters for the endpoint that throw a required flag. _Please note, required parameters can also be nullable. They just require a parameter to be passed._
_**nullable_parameters**_ | All parameters for the endpoint that do not require a value.
_**parameter_patterns**_ | Regular expression patterns for each parameter.
