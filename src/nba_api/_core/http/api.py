"""``client.http``: the low-level way to call any NBA endpoint with the client's settings."""

from nba_api._core.common.cache import ResponseCache
from nba_api._core.http.send import send
from nba_api._core.http.sites import SITES


class HTTP:
    def __init__(self, client):
        self._client = client

    def get(self, site, endpoint, params=None):
        """Fetch ``endpoint`` from ``site`` ("stats" or "live") and return a Response.

        Uses the client's proxy, headers, timeout and session. With the cache on, a
        repeat call returns the saved Response; only a 200 with valid JSON is saved.
        """
        if site not in SITES:
            raise ValueError(f"site must be one of {sorted(SITES)}, got {site!r}")
        client = self._client
        # Sorted like 1.x: some NBA endpoints care about parameter order.
        params = dict(sorted((params or {}).items()))

        key = ResponseCache.key(site, endpoint, params)
        if client.cache is not None:
            cached = client.cache.get(key)
            if cached is not None:
                return cached

        _, default_headers = SITES[site]
        response = send(
            client.session,
            site,
            endpoint,
            params,
            headers=client.merge_headers(default_headers),
            proxy=client.proxy,
            timeout=client.timeout,
        )
        if client.cache is not None and response.ok:
            client.cache.set(key, response)
        return response
