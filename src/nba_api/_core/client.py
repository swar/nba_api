"""The 2.0 client: connection settings and the session every request goes through.

Settings are checked when the client is created, so a bad value fails right away
instead of on the first request.
"""

import requests

from nba_api._core.common.cache import ResponseCache
from nba_api._core.http.api import HTTP

_UNSET = object()


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
        self.http = HTTP(self)

    def merge_headers(self, defaults):
        """Return ``defaults`` with this client's headers on top; ``None`` removes one."""
        merged = {**defaults, **self.headers}
        return {name: value for name, value in merged.items() if value is not None}

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
