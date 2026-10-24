"""The 2.0 client: connection settings and the session every request goes through.

Settings are checked when the client is created, so a bad value fails right away
instead of on the first request.
"""

from datetime import datetime, timezone

import requests

from nba_api._core.cache import ResponseCache
from nba_api._core.headers import LIVE_HEADERS, STATS_HEADERS
from nba_api._core.response import Response
from nba_api.library.http import _redacted
from nba_api.library.proxy import as_proxies, redact, resolve_proxy

_UNSET = object()

# site: (URL template, default headers)
SITES = {
    "stats": ("https://stats.nba.com/stats/{endpoint}", STATS_HEADERS),
    "live": ("https://cdn.nba.com/static/json/liveData/{endpoint}", LIVE_HEADERS),
}


def _check_proxy(proxy):
    # Same values resolve_proxy() accepts: None (use NBA_API_PROXY), "" or False (no
    # proxy), a URL, or a list of URLs to pick from at random.
    if proxy is None or proxy is False or isinstance(proxy, str):
        return proxy
    if isinstance(proxy, (list, tuple)) and all(isinstance(p, str) for p in proxy):
        return list(proxy)
    raise TypeError("proxy must be a URL string, a list of URL strings, False or None")


def _check_headers(headers):
    if headers is None:
        return {}
    if not isinstance(headers, dict):
        raise TypeError(f"headers must be a dict, got {type(headers).__name__}")
    for name, value in headers.items():
        if not isinstance(name, str) or not (value is None or isinstance(value, str)):
            raise TypeError("header names must be strings and values strings or None")
    return dict(headers)


def _is_seconds(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and value > 0


def _check_timeout(timeout):
    # requests waits forever without a timeout, so None is not allowed.
    if _is_seconds(timeout):
        return timeout
    if (
        isinstance(timeout, tuple)
        and len(timeout) == 2
        and all(_is_seconds(t) for t in timeout)
    ):
        return timeout
    raise ValueError(
        "timeout must be a positive number of seconds or a (connect, read) tuple, "
        f"got {timeout!r}"
    )


class Client:
    def __init__(
        self,
        proxy=None,
        headers=None,
        timeout=30,
        cache=False,
        cache_size=_UNSET,
    ):
        self.proxy = _check_proxy(proxy)
        self.headers = _check_headers(headers)
        self.timeout = _check_timeout(timeout)

        if not isinstance(cache, bool):
            raise TypeError(f"cache must be True or False, got {cache!r}")
        if cache_size is not _UNSET and not cache:
            raise ValueError("cache_size was set but cache is off; pass cache=True")
        self.cache = (
            ResponseCache(128 if cache_size is _UNSET else cache_size)
            if cache
            else None
        )

        self.session = requests.Session()

    def merge_headers(self, defaults):
        """Return ``defaults`` with this client's headers on top; ``None`` removes one."""
        merged = {**defaults, **self.headers}
        return {name: value for name, value in merged.items() if value is not None}

    def get(self, site, endpoint, params=None):
        """Fetch ``endpoint`` from ``site`` ("stats" or "live") and return a Response.

        Uses the cache when it is on. Errors are not designed yet: requests
        exceptions pass through with proxy credentials masked, like 1.x.
        """
        if site not in SITES:
            raise ValueError(f"site must be one of {sorted(SITES)}, got {site!r}")
        url_template, default_headers = SITES[site]
        # Sorted like 1.x: some NBA endpoints care about parameter order.
        params = dict(sorted((params or {}).items()))

        key = ResponseCache.key(site, endpoint, params)
        if self.cache is not None:
            cached = self.cache.get(key)
            if cached is not None:
                return cached

        proxy = resolve_proxy(self.proxy)
        try:
            raw = self.session.get(
                url_template.format(endpoint=endpoint),
                params=params,
                headers=self.merge_headers(default_headers),
                proxies=as_proxies(proxy),
                timeout=self.timeout,
            )
        except requests.RequestException as e:
            raise _redacted(e, proxy) from None

        response = Response(
            site=site,
            endpoint=endpoint,
            params=params,
            url=redact(raw.url, proxy) if proxy else raw.url,
            status=raw.status_code,
            fetched_at=datetime.now(timezone.utc),
            text=raw.text,
        )
        if self.cache is not None and response.ok:
            self.cache.set(key, response)
        return response

    def close(self):
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        self.close()

    def __repr__(self):
        # Never show the proxy: it may hold credentials.
        proxy = "'***'" if self.proxy else repr(self.proxy)
        cache = (
            f"cache=True, cache_size={self.cache.size}"
            if self.cache is not None
            else "cache=False"
        )
        return f"Client(proxy={proxy}, timeout={self.timeout!r}, {cache})"
