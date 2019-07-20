# http.py
>/nba_api/stats/library/http.py

The purpose of this module is to connect to the NBA website as well as store the response in a `NBAStatsResponse` class.

This should be considered as a base file to build on-top of an NBA API location.

## `STATS_HEADERS`

Default Value

```python
STATS_HEADERS = {
    'Host': 'stats.nba.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
}
```

This variable is set in [`/nba_api/debug.py`](/docs/nba_api/debug.md)


## class `NBAStatsResponse`(_`NBAResponse`_)

#### `get_normalized_dict` (_`response`_, _`url`_)

Returns the data sets in a normalized `dictionary`.

```python
normalized_dict = {
  'DataSet1': [
    {'HEADER1': 'VALUE1', 'HEADER2': 'VALUE2', 'HEADER3': 'VALUE3' ...},
    {'HEADER1': 'VALUE4', 'HEADER2': 'VALUE5', 'HEADER3': 'VALUE6' ...}
  ],
  'DataSet2': [
    {'HEADER1': 'VALUE1', 'HEADER2': 'VALUE2', 'HEADER3': 'VALUE3' ...},
    {'HEADER1': 'VALUE4', 'HEADER2': 'VALUE5', 'HEADER3': 'VALUE6' ...}
  ]
}
```

#### `get_normalized_json`( )

Returns the data sets in a normalized `json`.

```json
{
  "DataSet1": [
    {"HEADER1": "VALUE1", "HEADER2": "VALUE2", "HEADER3": "VALUE3" ...},
    {"HEADER1": "VALUE4", "HEADER2": "VALUE5", "HEADER3": "VALUE6" ...} ...
  ],
  "DataSet2": [
    {"HEADER1": "VALUE1", "HEADER2": "VALUE2", "HEADER3": "VALUE3" ...},
    {"HEADER1": "VALUE4", "HEADER2": "VALUE5", "HEADER3": "VALUE6" ...} ...
  ]
}
```

returns `response`

This method will return the response returned by a request.

#### `get_parameters`( )

This method will return a `dictionary` of all your inputted parameters and values.

#### `get_headers_from_data_sets`( )

This method will return the names and headers of the data sets in a `dictionary`.

#### `get_data_sets`( )
```python
data_sets = { name: {'name': name, 'headers': [headers...], 'data': [[data1], [data2], ...]}, ...}
```
This method will return the data sets and values in a `dictionary`.


## class `NBAStatsHTTP`(_`NBAHTTP`_)

#### `nba_response`

The value is set to `NBAStatsResponse`.

#### `base_url`

Base URL Format: `http://stats.nba.com/stats/{endpoint}`

#### `headers`

The value is set to `STATS_HEADERS`

#### `clean_contents`(_`contents`_)

This method is set to remove json parsed error responses.
