endpoint_documentation_template = '''# {endpoint}

##### Endpoint URL
>[https://stats.nba.com/stats/{endpoint__lowercase}](https://stats.nba.com/stats/{endpoint__lowercase})

##### Valid URL
>[https://stats.nba.com/stats/{endpoint__lowercase}?{query_string_parameters}](https://stats.nba.com/stats/{endpoint__lowercase}?{query_string_parameters})

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
{parameters}

## Data Sets
{data_sets}

## JSON
```json
{json}
```

Last validated {validated_date}'''

data_set_template = '''#### {data_set_name} `{method_name}`
```text
{columns}
```
'''

parameter_line_template = '''_**{parameter}**_ | {pattern} | {required} | {nullable} | '''