endpoint_documentation_template = """# {endpoint}
##### [nba_api/stats/endpoints/{endpoint__lowercase}.py](https://github.com/swar/nba_api/blob/master/nba_api/stats/endpoints/{endpoint__lowercase}.py)

##### Endpoint URL
>[https://stats.nba.com/stats/{endpoint__lowercase}](https://stats.nba.com/stats/{endpoint__lowercase})

##### Valid URL
>[https://stats.nba.com/stats/{endpoint__lowercase}?{query_string_parameters}](https://stats.nba.com/stats/{endpoint__lowercase}?{query_string_parameters})

## Parameters
API Parameter Name | Python Parameter Variable | Pattern | Required | Nullable
------------ | ------------ | :-----------: | :---: | :---:
{parameters}

## Data Sets
{data_sets}

## JSON
```json
{json}
```

Last validated {validated_date}"""

data_set_template = """#### {data_set_name} `{method_name}`
```text
{columns}
```
"""

parameter_line_template = """[_**{api_parameter_name}**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#{api_parameter_name}) | {python_parameter_variable} | {pattern} | {required} | {nullable} | """
