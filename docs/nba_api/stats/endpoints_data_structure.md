# Endpoint data structure
>/src/nba_api/stats/endpoints/_base.py

Every stats endpoint class inherits from `Endpoint`, so the methods below work the same on all of them. Each data set the endpoint returns is also exposed as an attribute holding an `Endpoint.DataSet` (for example, `PlayerCareerStats(...).season_totals_regular_season`). The data set attributes for each endpoint are listed on its page in the [table of contents](../../table_of_contents.md).

## class `Endpoint`

#### `get_request`( )

Sends the request and loads the response. Called automatically by the constructor unless the endpoint was created with `get_request=False`.

#### `get_request_url`( )

Returns the URL of the request, including the query string.

#### `get_available_data`( )

Returns the names of the data sets in the response.

#### `get_response`( )

Returns the raw response text.

#### `get_dict`( )

Returns the full response as a `dict`.

#### `get_json`( )

Returns the full response as a JSON `str`.

#### `get_normalized_dict`( )

Returns every data set as a list of row dictionaries, keyed by data set name:

```python
{"DataSetName": [{"HEADER1": value, "HEADER2": value, ...}, ...], ...}
```

#### `get_normalized_json`( )

Returns `get_normalized_dict()` as a JSON `str`.

#### `get_data_frames`( )

Returns a `list` of pandas `DataFrame`s, one per data set, in the order the API returned them.

## class `Endpoint.DataSet`

#### `__init__`(_`data`_)

```python
data = {"headers": ["HEADER1", "HEADER2", ...], "data": [[row1...], [row2...], ...]}
```

#### `get_dict`( )

Returns the data set as a `dict` in the format above.

#### `get_json`( )

Returns the data set as a JSON `str` in the format above.

#### `get_data_frame`( )

Returns the data set as a pandas `DataFrame`. Data sets with multiple header levels get `MultiIndex` columns, and a data set without headers returns an empty `DataFrame`.
