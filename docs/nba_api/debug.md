# debug.py
>/nba_api/debug.py

The purpose of this module is to set the library into debug mode as well as set your proxy and headers.


## `DEBUG`

`boolean`

Set this value to `true` in order to enable debug mode.


## `DEBUG_STORAGE`

`boolean`

Set this value to `true` in order to enable text file saving of every request. Parameters are joined together and an MD5 hash is used to create the file name in a `debug_storage` folder. 

This feature is primarily used to help debug any issues as well as develop additional features.

This feature is dependent on `DEBUG` to be `true`. If not, then this feature will not be enabled, regardless of the setting.


## `PROXY`

`string`

```python
PROXY = '127.0.0.1:80'
```

Set this value to run requests through a proxy.

## `STATS_HEADERS`

`dictionary`

Set this value to override the headers of the `stats.nba.com` API Endpoints.
