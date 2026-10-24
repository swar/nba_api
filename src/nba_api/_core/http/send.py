"""Build one request, send it and wrap the reply in a Response."""

from datetime import datetime, timezone

import requests

from nba_api._core.common.errors import (
    ProxyError,
    TransportError,
    _ConnectionError,
    _ConnectTimeout,
    _ReadTimeout,
)
from nba_api._core.http.check import check
from nba_api._core.http.response import Response
from nba_api._core.http.sites import SITES
from nba_api.library.proxy import as_proxies, redact, resolve_proxy

# Most specific first: ConnectTimeout and ProxyError are also ConnectionErrors.
_TRANSPORT_ERRORS = (
    (requests.exceptions.ProxyError, ProxyError),
    (requests.ConnectTimeout, _ConnectTimeout),
    (requests.ReadTimeout, _ReadTimeout),
    (requests.ConnectionError, _ConnectionError),
)

_HINT = (
    " stats.nba.com often stops answering cloud and data-center IPs, which shows up "
    "as a timeout or reset; a proxy usually helps. Some endpoints also hang on IDs "
    "that don't exist."
)


def _transport_error(error, site, endpoint, proxy_url):
    cls = next(
        (ours for theirs, ours in _TRANSPORT_ERRORS if isinstance(error, theirs)),
        TransportError,
    )
    detail = redact(error, proxy_url) if proxy_url else str(error)
    hint = " Check the proxy URL and credentials." if cls is ProxyError else _HINT
    return cls(f"Request to {site} {endpoint!r} failed: {detail}.{hint}")


def send(session, site, endpoint, params, headers, proxy, timeout):
    """Send one GET request and return a Response, or raise an NBAAPIError.

    ``params`` should already be sorted. ``proxy`` is the client's raw setting; it is
    resolved here, per request, so NBA_API_PROXY changes take effect right away.
    """
    url_template, _ = SITES[site]
    proxy_url = resolve_proxy(proxy)
    error = None
    try:
        raw = session.get(
            url_template.format(endpoint=endpoint),
            params=params,
            headers=headers,
            proxies=as_proxies(proxy_url),
            timeout=timeout,
            # An unknown stats endpoint redirects forever; fail on the first hop.
            allow_redirects=False,
        )
    except requests.RequestException as e:
        error = _transport_error(e, site, endpoint, proxy_url)
    if error is not None:
        # Raised outside the except block so the original error isn't kept as
        # __context__: it and its urllib3 causes can contain the proxy URL.
        raise error

    response = Response(
        site=site,
        endpoint=endpoint,
        params=params,
        url=redact(raw.url, proxy_url) if proxy_url else raw.url,
        status=raw.status_code,
        fetched_at=datetime.now(timezone.utc),
        text=raw.text,
    )
    check(response)
    return response
