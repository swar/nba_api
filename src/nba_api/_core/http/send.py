"""Build one request, send it and wrap the reply in a Response."""

from datetime import datetime, timezone

import requests

from nba_api._core.http.response import Response
from nba_api._core.http.sites import SITES
from nba_api.library.http import _redacted
from nba_api.library.proxy import as_proxies, redact, resolve_proxy


def send(session, site, endpoint, params, headers, proxy, timeout):
    """Send one GET request and return a Response.

    ``params`` should already be sorted. ``proxy`` is the client's raw setting; it is
    resolved here, per request, so NBA_API_PROXY changes take effect right away.
    Errors are not designed yet: requests exceptions pass through with proxy
    credentials masked, like 1.x.
    """
    url_template, _ = SITES[site]
    proxy_url = resolve_proxy(proxy)
    try:
        raw = session.get(
            url_template.format(endpoint=endpoint),
            params=params,
            headers=headers,
            proxies=as_proxies(proxy_url),
            timeout=timeout,
        )
    except requests.RequestException as e:
        raise _redacted(e, proxy_url) from None

    return Response(
        site=site,
        endpoint=endpoint,
        params=params,
        url=redact(raw.url, proxy_url) if proxy_url else raw.url,
        status=raw.status_code,
        fetched_at=datetime.now(timezone.utc),
        text=raw.text,
    )
