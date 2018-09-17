# http.py
>/nba_api/library/http.py

The purpose of this module is to connect to the NBA website as well as store the response in a `NBAResponse` class.

This should be considered as a base file to build on-top of an NBA API location.

## `DEBUG`,`DEBUG_STORAGE`, `PROXY`

These variables are set in [`/nba_api/debug.py`](/docs/nba_api/debug.md)


## class `NBAResponse`

#### `__init__` (_`response`_, _`url`_)

Loads the response text and url on initiation.

#### `get_response`( )

returns `response`

This method will return the response returned by a request.

#### `get_dict`( )

This method will return a `dictionary` of the response. It wil fail if the response is not a json.

#### `get_json`( )

This method will return a `json` string of the response. It wil fail if the response is not a json.

#### `valid_json`( )

This method is used to help determine if the response is a valid `json` response.

#### `get_url`( )

This method will return the url that we used to request the result.


## class `NBAHTTP`

#### `nba_response`

This is used to set the `NBAResponse` class. 

#### `base_url`

This is used to set the base url of requests.

#### `headers`

This is used to set the headers of requests.

#### `clean_contents`(_`contents`_)

This method is used to clean any contents if any invalid values are returned.

#### `send_api_request`(_`endpoint`_, _`parameters`_ \[, _`referer=None`_, _`proxy=PROXY`_, _`raise_exception_on_error=False`_\] )

This method will send out an api request with the given endpoint, parameters, and referer on a given proxy. You can also enable the option to raise an exception any time a valid `json` response is not returned.
