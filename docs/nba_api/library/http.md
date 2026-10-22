# http.py
>/src/nba_api/library/http.py

This module provides the HTTP client that every NBA.com API client builds on: `NBAHTTP` sends the request, and `NBAResponse` wraps the result. The stats client ([`NBAStatsHTTP`](../stats/library/http.md)) and the live client (`NBALiveHTTP`) subclass these and set their own base URL, headers, and response class.

## `DEBUG`, `DEBUG_STORAGE`, `PROXY`

Imported from [`debug.py`](../debug.md) when this module is first loaded.


## class `NBAResponse`

#### `__init__`(_`response`_, _`status_code`_, _`url`_)

Stores the response text, HTTP status code, and request URL.

#### `get_response`( )

Returns the raw response text.

#### `get_dict`( )

Returns the response parsed as a `dict`. Raises `json.JSONDecodeError` if the response is not JSON.

#### `get_json`( )

Returns the response as a JSON `str`. Raises `json.JSONDecodeError` if the response is not JSON.

#### `valid_json`( )

Returns `True` if the response parses as JSON, otherwise `False`.

#### `get_url`( )

Returns the URL that was requested, including the query string.


## class `NBAHTTP`

#### `nba_response`

The response class to wrap results in. Subclasses override it.

#### `base_url`

The URL template for requests, with an `{endpoint}` placeholder. `NBAHTTP` itself has none, so requests must be sent through a subclass.

#### `parameters`

The parameters of the most recent request.

#### `headers`

The default request headers.

#### `get_session`( ) — _classmethod_

Returns the `requests.Session` shared by all requests from this class, creating it on first use.

#### `set_session`(_`session`_) — _classmethod_

Replaces the shared session, for example to add retries or connection pooling:

```python
import requests
from requests.adapters import HTTPAdapter, Retry

from nba_api.stats.library.http import NBAStatsHTTP

session = requests.Session()
session.mount("https://", HTTPAdapter(max_retries=Retry(total=3, backoff_factor=1)))
NBAStatsHTTP.set_session(session)
```

#### `clean_contents`(_`contents`_)

A hook for subclasses to normalize the response text before it is wrapped. The base implementation returns it unchanged.

#### `send_api_request`(_`endpoint`_, _`parameters`_ \[, _`referer=None`_, _`proxy=None`_, _`headers=None`_, _`timeout=None`_, _`raise_exception_on_error=False`_\] )

Sends a `GET` request to `base_url` for `endpoint` with the given query `parameters`, and returns an instance of `nba_response`.

- `headers`: `None` uses the class's default `headers`. Any other value, including `{}`, replaces them entirely.
- `proxy`: `None` uses the default `PROXY`, `""` disables the proxy, and a list picks one at random. See [`debug.py`](../debug.md#proxy).
- `referer`: if set, added to the request headers as `Referer`.
- `timeout`: seconds to wait for a response. `None` waits indefinitely. Endpoints pass `30` by default.
- `raise_exception_on_error`: if `True`, raises an `Exception` when the response is not valid JSON.
