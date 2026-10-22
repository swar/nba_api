# debug.py
>/src/nba_api/library/debug/debug.py

This module holds package-wide settings for debug mode, response caching, and the default proxy. The HTTP clients read these values **once, when they are first imported**, so a setting must be in place before you import any endpoint.

For most uses, prefer the per-request `proxy`, `headers`, and `timeout` arguments that every endpoint accepts (see [Stats examples](stats/examples.md)). They need no global configuration.

## `PROXY`

`str` — default `""` (no proxy)

The proxy used by every request that does not pass its own `proxy` argument. It is read from the `NBA_API_PROXY` environment variable:

```bash
export NBA_API_PROXY='http://user:pass@proxy.example.com:8080'
```

If the variable is not set in the environment, `debug.py` also looks for a `.env` file in the **current working directory** and loads `KEY=VALUE` lines from it. Values already set in the environment take precedence.

```text
# .env
NBA_API_PROXY=http://user:pass@proxy.example.com:8080
```

SOCKS proxies (`socks5://...`) also work, but require [PySocks](https://pypi.org/project/PySocks/) (`pip install "requests[socks]"`).

> [!CAUTION]
> Keep proxy credentials out of version control: add `.env` to your `.gitignore`. Exceptions raised by `requests` can include the full proxy URL, credentials included, so check tracebacks before sharing them in issues.

How a request picks its proxy:

| `proxy` argument | Proxy used |
|---|---|
| not passed / `None` | `PROXY` (from `NBA_API_PROXY`) |
| `""` (empty string) | none, even if `NBA_API_PROXY` is set |
| a URL string | that URL |
| a list of URLs | one chosen at random for each request |

## `DEBUG`

`bool` — default `False`

When `True`, the HTTP clients print `DEBUG MODE` on import and report which proxy was picked when `proxy` is a list. Combined with `DEBUG_STORAGE`, they also print each request's endpoint, parameters, URL, and cache hits.

## `DEBUG_STORAGE`

`bool` — default `False`

When `True` **and** `DEBUG` is also `True`, every response is saved to a text file and reused for identical later requests, avoiding repeated calls while developing. Files are written to `library/debug/debug_storage/` inside the installed `nba_api` package, named `<endpoint>-<md5 of the query string>.txt`. Delete that directory to clear the cache.

## `STATS_HEADERS`

`dict` — not defined by default

If you define `STATS_HEADERS` in `debug.py`, it **replaces** the default request headers for both the stats (`stats.nba.com`) and live (`cdn.nba.com`) clients. To change headers for a single request, pass `headers=` to the endpoint instead.
