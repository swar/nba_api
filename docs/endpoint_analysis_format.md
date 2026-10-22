# Endpoint analysis format

The [endpoint analyzer](nba_api/tools/stats/endpoint_analysis/analysis.md) writes its results to `analysis.json` in the format below. The [code](nba_api/tools/stats/endpoint_py_file_generator/generator.md) and [documentation](nba_api/tools/stats/endpoint_documentation_generator/generator.md) generators read this file.

```json
{
    "{endpoint}": {
        "status": "{status}",
        "endpoint": "{endpoint}",
        "data_sets": {},
        "parameters": [],
        "required_parameters": [],
        "nullable_parameters": [],
        "parameter_patterns": {
            "{property}": "{pattern}"
        }
    }
}
```

| Field | Description |
|---|---|
| _**status**_ | `success` or `fail`. `success` means the endpoint passed every check the analyzer runs. |
| _**endpoint**_ | The name of the endpoint. |
| _**data_sets**_ | The data sets that are returned by the endpoint and their data headers. |
| _**parameters**_ | All parameters for the endpoint. |
| _**required_parameters**_ | All parameters for the endpoint that throw a required flag. _Please note, required parameters can also be nullable. They just require a parameter to be passed._ |
| _**nullable_parameters**_ | All parameters for the endpoint that do not require a value. |
| _**parameter_patterns**_ | Regular expression patterns for each parameter. |
