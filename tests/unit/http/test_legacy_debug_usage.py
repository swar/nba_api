import importlib
from unittest.mock import Mock, mock_open, patch

import pytest
import requests

from nba_api.live.nba.endpoints import scoreboard
from nba_api.stats.endpoints import assistleaders

DEFAULT_STATS_HEADERS = {
    "Host": "stats.nba.com",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": "https://www.nba.com/",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Sec-Ch-Ua": '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Fetch-Dest": "empty",
}

DEFAULT_LIVE_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "cdn.nba.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
}

NEW_STATS_HEADERS = {
    "Host": "nba.com",
    "User-Agent": "NBA API - Unit Test Client/1.0",
}

PROXY_URL = "http://proxy.example:8080"
PROXIES = {"http": PROXY_URL, "https": PROXY_URL}

MOCK_RESPONSE_TEXT = '{"resource":"assistleaders","parameters":{"LeagueID":"00","Season":"2025-26","SeasonType":"Regular Season","PerMode":"Totals","PlayerOrTeam":"Team"},"resultSets":[{"name":"AssistLeaders","headers":["RANK","TEAM_ID","TEAM_ABBREVIATION","TEAM_NAME","AST"],"rowSet":[[1,1610612737,"ATL","Atlanta Hawks",1760],[2,1610612762,"UTA","Utah Jazz",1712],[3,1610612748,"MIA","Miami Heat",1667],[4,1610612741,"CHI","Chicago Bulls",1656],[5,1610612761,"TOR","Toronto Raptors",1636]]}]}'
MOCK_LIVE_RESPONSE_TEXT = '{"meta":{"version":1,"request":"","time":"","code":200},"scoreboard":{"gameDate":"2025-02-25","leagueId":"00","leagueName":"National Basketball Association","games":[]}}'

MOCK_RESPONSE = Mock()
MOCK_RESPONSE.url = "https://nba.com/stats/assistleaders"
MOCK_RESPONSE.status_code = 200
MOCK_RESPONSE.text = MOCK_RESPONSE_TEXT

MOCK_LIVE_RESPONSE = Mock()
MOCK_LIVE_RESPONSE.url = (
    "https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json"
)
MOCK_LIVE_RESPONSE.status_code = 200
MOCK_LIVE_RESPONSE.text = MOCK_LIVE_RESPONSE_TEXT


def reload_http_modules(reload_debug=True):
    """Reload http modules to reset any cached header/proxy/debug state.

    Parameters
    ----------
    reload_debug:
        When True (default) the debug module is reloaded first, which is
        correct for variables that are commented-out in debug.py (PROXY,
        STATS_HEADERS) because those re-execute without overwriting the patch.
        Set to False when patching variables that ARE assigned in debug.py
        (DEBUG, DEBUG_STORAGE) so the reload does not reset the patched value
        before http.py imports it.
    """
    import nba_api.library.debug.debug
    import nba_api.library.http
    import nba_api.stats.library.http

    if reload_debug:
        importlib.reload(nba_api.library.debug.debug)
    importlib.reload(nba_api.library.http)
    importlib.reload(nba_api.stats.library.http)
    importlib.reload(assistleaders)


def send_stats_endpoint(capture="headers", **endpoint_kwargs):
    """Call the AssistLeaders endpoint and return a captured Session.get kwarg.

    Parameters
    ----------
    capture:
        The keyword argument name to extract from the outgoing ``Session.get``
        call.  Use ``"headers"`` (default) to inspect request headers, or
        ``"proxies"`` to inspect the proxy configuration.
    """
    with patch.object(
        requests.Session, "get", return_value=MOCK_RESPONSE
    ) as mock_request:
        assistleaders.AssistLeaders(**endpoint_kwargs)

    assert mock_request.called

    _, call_kwargs = mock_request.call_args
    return call_kwargs.get(capture)


def send_live_endpoint(capture="headers", **endpoint_kwargs):
    """Call the ScoreBoard live endpoint and return a captured Session.get kwarg.

    Parameters
    ----------
    capture:
        The keyword argument name to extract from the outgoing ``Session.get``
        call.  Use ``"headers"`` (default) to inspect request headers, or
        ``"proxies"`` to inspect the proxy configuration.
    """
    with patch.object(
        requests.Session, "get", return_value=MOCK_LIVE_RESPONSE
    ) as mock_request:
        scoreboard.ScoreBoard(**endpoint_kwargs)

    assert mock_request.called

    _, call_kwargs = mock_request.call_args
    return call_kwargs.get(capture)


@pytest.fixture(autouse=True)
def reset_http_modules_after_test():
    """Reload http modules after each test to prevent DEBUG flag and class-reference contamination."""
    yield
    reload_http_modules()


@pytest.fixture(params=["stats", "live"])
def send_endpoint(request):
    """Pytest fixture to call either a stats or live endpoint based on the test parameterization."""
    if request.param == "stats":
        return send_stats_endpoint
    elif request.param == "live":
        return send_live_endpoint
    else:
        raise ValueError(f"Unsupported endpoint type: {request.param}")


# Test Headers
def test_stats_endpoint_default_headers():
    headers = send_stats_endpoint()
    assert headers == DEFAULT_STATS_HEADERS


def test_stats_endpoint_custom_headers_in_call():
    headers = send_stats_endpoint(headers=NEW_STATS_HEADERS)
    assert headers == NEW_STATS_HEADERS


def test_stats_endpoint_custom_headers_in_legacy_debug_module(monkeypatch):
    debug_headers = NEW_STATS_HEADERS.copy()
    debug_headers["Some-Header"] = "Some Value"
    monkeypatch.setattr(
        target="nba_api.library.debug.debug.STATS_HEADERS",
        name=debug_headers,
        raising=False,
    )
    reload_http_modules()  # Reload Modules to ensure patched debug headers are used
    headers = send_stats_endpoint()
    assert headers == debug_headers


def test_live_endpoint_default_headers():
    headers = send_live_endpoint()
    assert headers == DEFAULT_LIVE_HEADERS


def test_live_endpoint_custom_headers_in_call():
    headers = send_live_endpoint(headers=NEW_STATS_HEADERS)
    assert headers == NEW_STATS_HEADERS


def test_live_endpoint_custom_headers_in_legacy_debug_module_does_not_affect_endpoint(
    monkeypatch,
):
    debug_headers = NEW_STATS_HEADERS.copy()
    debug_headers["Some-Header"] = "Some Value"
    monkeypatch.setattr(
        target="nba_api.library.debug.debug.STATS_HEADERS",
        name=debug_headers,
        raising=False,
    )
    reload_http_modules()  # Reload Modules to ensure patched debug headers are used
    headers = send_live_endpoint()
    assert headers == DEFAULT_LIVE_HEADERS


# Test Proxy
def test_stats_endpoint_default_no_proxy(send_endpoint):
    proxies = send_endpoint(capture="proxies")
    assert proxies is None


def test_stats_endpoint_custom_proxy_in_call(send_endpoint):
    proxies = send_endpoint(proxy=PROXY_URL, capture="proxies")
    assert proxies == PROXIES


def test_stats_endpoint_customer_proxy_in_legacy_debug_module(
    send_endpoint, monkeypatch
):
    monkeypatch.setattr(
        target="nba_api.library.debug.debug.PROXY", name=PROXY_URL, raising=False
    )
    reload_http_modules()  # Reload Modules to ensure patched debug proxy is used
    proxies = send_endpoint(capture="proxies")
    assert proxies == PROXIES


# Test DEBUG
def test_debug_variable_default_false():
    import nba_api.library.http

    assert not nba_api.library.http.DEBUG


def test_debug_variable_set_in_legacy_debug_module(monkeypatch):
    monkeypatch.setattr(
        target="nba_api.library.debug.debug.DEBUG", name=True, raising=False
    )
    reload_http_modules(reload_debug=False)  # Don't reload debug.py, its already set
    import nba_api.library.http

    assert nba_api.library.http.DEBUG


# Test DEBUG_STORAGE
def test_debug_storage_variable_default_false():
    import nba_api.library.http

    assert not nba_api.library.http.DEBUG_STORAGE


def test_debug_storage_variable_set_in_legacy_debug_module(monkeypatch):
    monkeypatch.setattr(
        target="nba_api.library.debug.debug.DEBUG_STORAGE", name=True, raising=False
    )
    reload_http_modules(reload_debug=False)  # Don't reload debug.py, its already set
    import nba_api.library.http

    assert nba_api.library.http.DEBUG_STORAGE


@pytest.mark.parametrize(
    "is_file_cached", [True, False], ids=["file_is_cached", "file_is_not_cached"]
)
def test_debug_storage_caching(is_file_cached, monkeypatch):
    """When DEBUG + DEBUG_STORAGE are active and a cache file exists, Session.get is not called."""
    monkeypatch.setattr(
        target="nba_api.library.debug.debug.DEBUG", name=True, raising=False
    )
    monkeypatch.setattr(
        target="nba_api.library.debug.debug.DEBUG_STORAGE", name=True, raising=False
    )
    reload_http_modules(reload_debug=False)  # Don't reload debug.py, its already set
    with (
        patch("os.path.exists", return_value=True),
        patch("os.path.isfile", return_value=is_file_cached),
        patch("builtins.open", mock_open(read_data=MOCK_RESPONSE_TEXT)),
        patch.object(requests.Session, "get", return_value=MOCK_RESPONSE) as mock_get,
    ):
        assistleaders.AssistLeaders()

    assert (not mock_get.called) if is_file_cached else mock_get.called
