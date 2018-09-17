# Input / Output Definitions

### `nba_stats_response`
[`NBAStatsResponse`]() class

### `endpoint`
```python
endpoint = 'endpoint'
```

### `endpoints`
```python
endpoints = ['endpoint1',  'endpoint2', ...]
```

### `endpoint_analysis`
```python
endpoint_analysis = {
    'status': status,
    'endpoint': endpoint,
    'parameters': all_parameters,
    'required_parameters': required_parameters,
    'nullable_parameters': nullable_parameters,
    'parameter_patterns': parameter_patterns,
    'data_sets': data_sets,
}
```

### `endpoints_information`
```python
endpoints_information = {'endpoint1': endpoint_analysis, ...}
```

### `params`, `required_params`, `params_errors`, `required_params_errors`
```python
params = {'endpoint': 'error_value', ...}
```

### `parameter_patterns`
```python
parameter_patterns = {'endpoint': 'pattern', ...}
```

### `status`
status can be either `success`, `invalid`, or `deprecated`

`success` Endpoint has passed all tests.

`invalid` Endpoint has not passed all tests.

`deprecated` Endpoint returns a 404 error page.

```python
status = 'status'
```

### `all_parameters`
```python
all_parameters = ['parameter1',  'parameter2', ...]
```

### `required_parameters`
```python
required_parameters = ['parameter1',  'parameter2', ...]
```

### `nullable_parameters`
```python
nullable_parameters = ['parameter1',  'parameter2', ...]
```

### `data_sets`
The data sets returned by the [`NBAStatsResponse`]() class.