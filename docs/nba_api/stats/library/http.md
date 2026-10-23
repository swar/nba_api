# http.py
>/src/nba_api/stats/library/http.py

This module provides the `stats.nba.com` client. It extends the shared [`http.py`](../../library/http.md) with stats-specific headers, a base URL, and a response class that turns the stats API's tabular `resultSets` into data sets.

## `STATS_HEADERS`

The default request headers. They imitate a desktop Chrome browser visiting `www.nba.com` (including `Referer`, `User-Agent`, and `Sec-Ch-Ua` headers), because `stats.nba.com` rejects or ignores many requests that don't look like they come from a browser. See the source for the exact values.

If `STATS_HEADERS` is defined in [`debug.py`](../../debug.md#stats_headers), that value is used instead. To override headers for a single request, pass `headers=` to the endpoint.


## class `NBAStatsResponse`(_`NBAResponse`_)

#### `get_normalized_dict`( )

Returns every data set as a list of row dictionaries, keyed by data set name. Works for both tabular and nested-JSON endpoints (after `get_data_sets(endpoint)` has been called, which endpoints do automatically).

```python
normalized_dict = {
    "DataSet1": [
        {"HEADER1": "VALUE1", "HEADER2": "VALUE2", ...},
        {"HEADER1": "VALUE3", "HEADER2": "VALUE4", ...},
    ],
    "DataSet2": [...],
}
```

#### `get_normalized_json`( )

Returns `get_normalized_dict()` as a JSON `str`.

#### `get_parameters`( )

Returns the request parameters as echoed back by the API in the response, as a `dict`. Returns `None` if the response is not JSON or contains no `parameters`.

#### `get_headers_from_data_sets`( )

Returns the column headers of each data set, keyed by data set name. Only supported for tabular `resultSets` responses; returns `{}` otherwise.

#### `get_data_sets`( \[_`endpoint=None`_\] )

Returns every data set with its headers and rows, keyed by data set name:

```python
data_sets = {
    "DataSet1": {"headers": ["HEADER1", "HEADER2", ...], "data": [[...], [...], ...]},
    ...
}
```

With no argument, the data sets are read from the tabular `resultSets` (or `resultSet`) in the response. Endpoints that return nested JSON instead pass their `endpoint` name, and parsing is delegated to that endpoint's parser in `stats/endpoints/_parsers/`.


## class `NBAStatsHTTP`(_`NBAHTTP`_)

#### `nba_response`

`NBAStatsResponse`

#### `base_url`

`https://stats.nba.com/stats/{endpoint}`

#### `headers`

`STATS_HEADERS`

#### `clean_contents`(_`contents`_)

Replaces the stats API's JSON error body (`{"Message":"An error has occurred."}`) with a non-JSON placeholder, so that `valid_json()` returns `False` for failed requests.
