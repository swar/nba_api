# debug.py
>/src/nba_api/library/debug/debug.py

This module holds package-wide settings for debug mode and response caching. The HTTP clients read `DEBUG` and `DEBUG_STORAGE` **once, when they are first imported**, so set them before you import any endpoint. Proxy configuration no longer lives here; see [`PROXY`](#proxy) below.

For most uses, prefer the per-request `proxy`, `headers`, and `timeout` arguments that every endpoint accepts (see [Stats examples](stats/examples.md)). They need no global configuration.

## `PROXY`

`str` — default `""`. **Deprecated.** Set the `NBA_API_PROXY` environment variable, or pass `proxy=`, instead.

The proxy is resolved on every request (not at import time), so you can change it between calls. It comes from, in order:

| Source | Proxy used |
|---|---|
| `proxy=` a URL string | that URL |
| `proxy=` a list of URLs | one chosen at random for each request |
| `proxy=""` | none, even if `NBA_API_PROXY` is set |
| `proxy` not passed / `None` | the `NBA_API_PROXY` environment variable |
| nothing above | `PROXY` in this module, with a `FutureWarning` |

```bash
export NBA_API_PROXY='http://user:pass@proxy.example.com:8080'
```

`.env` files are **not** read. Export the variable in your shell, or load a `.env` yourself (for example with `direnv` or `set -a; source .env; set +a`).

SOCKS proxies (`socks5://...`) also work, but require [PySocks](https://pypi.org/project/PySocks/) (`pip install "requests[socks]"`).

Proxy credentials are masked (`scheme://***@host`) in exceptions raised by the HTTP clients, but still keep them out of version control and logs.

### Requiring a proxy

Set `NBA_API_REQUIRE_PROXY=1` to make any request raise `nba_api.library.proxy.ProxyRequiredError` *before a connection is opened* when no proxy resolves. `proxy=""` does not bypass it. The project's live tests use this so they can never reach NBA.com directly.

## `DEBUG`

`bool` — default `False`

When `True`, the HTTP clients print `DEBUG MODE` on import and report the (credential-masked) proxy that was picked. Combined with `DEBUG_STORAGE`, they also print each request's endpoint, parameters, URL, and cache hits.

## `DEBUG_STORAGE`

`bool` — default `False`

When `True` **and** `DEBUG` is also `True`, every response is saved to a text file and reused for identical later requests, avoiding repeated calls while developing. Files are written to `library/debug/debug_storage/` inside the installed `nba_api` package, named `<endpoint>-<md5 of the query string>.txt`. Delete that directory to clear the cache.

## `STATS_HEADERS`

`dict` — not defined by default

If you define `STATS_HEADERS` in `debug.py`, it **replaces** the default request headers for both the stats (`stats.nba.com`) and live (`cdn.nba.com`) clients. To change headers for a single request, pass `headers=` to the endpoint instead.
