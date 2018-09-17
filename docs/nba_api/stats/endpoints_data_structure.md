# class `Endpoint`

## `get_request_url`( )

Returns the url of the request.

## `get_available_data`( )

Returns the data set names that are in the object.

## `get_response`( )

Returns the raw `string` response.

## `get_dict`( )

Returns the response in a `dictionary`.

## `get_json`( )

Returns the response in a `json`.

## `get_normalized_dict`( )

Returns the response in a normalized `dictionary`.

## `get_normalized_json`( )

Returns the response in a normalized `json`.

## `get_data_frames`( )

Returns the a `list` of data sets in `DataFrame` objects.

## class `DataSet`

#### `__init__`(_`data`_)
```python
data = data_set
```
```python
data_set = {'name': name, 'headers': headers, 'data': data}
```

#### `get_json`( )
returns the data set in a `json` object.
```json
{"name": name, "headers": [headers...], "data": [[data1], [data2], ...]}
```

#### `get_dict`( )
returns the data set in a `dictionary` object.
```python
data_set = {'name': name, 'headers': [headers...], 'data': [[data1], [data2], ...]}
```

#### `get_data_frame`( )
returns the data set in a `DataFrame` object. If `pandas` fails to import, this method will raise an exception.

