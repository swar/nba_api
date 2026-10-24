import pytest
import requests

from nba_api._core.client import Client
from nba_api._core.common.errors import HTTPStatusError
from nba_api._core.http.sites import LIVE_HEADERS, STATS_HEADERS

SECRET_PROXY = "http://user:hunter2@proxy.example:8080"


class FakeResponse:
    def __init__(self, status_code=200, text='{"ok": true}', url="https://x/y?a=1"):
        self.status_code = status_code
        self.text = text
        self.url = url


@pytest.fixture
def calls(monkeypatch):
    """Record every session.get call; tests set calls.reply to change the response."""

    class Calls(list):
        reply = FakeResponse()

    recorded = Calls()

    def fake_get(self, url, **kwargs):
        recorded.append({"url": url, **kwargs})
        if isinstance(recorded.reply, Exception):
            raise recorded.reply
        return recorded.reply

    monkeypatch.setattr(requests.Session, "get", fake_get)
    monkeypatch.delenv("NBA_API_PROXY", raising=False)
    monkeypatch.delenv("NBA_API_REQUIRE_PROXY", raising=False)
    return recorded


def test_stats_request(calls):
    response = Client(timeout=12).http.get(
        "stats", "commonplayerinfo", {"PlayerID": 2544}
    )
    (call,) = calls
    assert call["url"] == "https://stats.nba.com/stats/commonplayerinfo"
    assert call["params"] == {"PlayerID": 2544}
    assert call["headers"] == STATS_HEADERS
    assert call["timeout"] == 12
    assert call["proxies"] is None
    assert response.status == 200
    assert response.json() == {"ok": True}
    assert response.site == "stats"
    assert response.endpoint == "commonplayerinfo"
    assert response.fetched_at.tzinfo is not None


def test_live_request_uses_live_headers(calls):
    Client().http.get("live", "scoreboard/todaysScoreboard_00.json")
    (call,) = calls
    assert call["url"] == (
        "https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json"
    )
    assert call["headers"] == LIVE_HEADERS


def test_unknown_site_raises(calls):
    with pytest.raises(ValueError, match="site"):
        Client().http.get("espn", "x")
    assert calls == []


def test_params_are_sorted(calls):
    Client().http.get("stats", "x", {"b": 2, "a": 1})
    assert list(calls[0]["params"]) == ["a", "b"]


def test_client_headers_merge(calls):
    Client(headers={"User-Agent": "mine"}).http.get("stats", "x")
    assert calls[0]["headers"]["User-Agent"] == "mine"
    assert calls[0]["headers"]["Host"] == "stats.nba.com"


def test_proxy_is_used(calls):
    Client(proxy=SECRET_PROXY).http.get("stats", "x")
    assert calls[0]["proxies"] == {"http": SECRET_PROXY, "https": SECRET_PROXY}


def test_proxy_env_is_read_per_request(calls, monkeypatch):
    client = Client()
    monkeypatch.setenv("NBA_API_PROXY", SECRET_PROXY)
    client.http.get("stats", "x")
    assert calls[0]["proxies"] == {"http": SECRET_PROXY, "https": SECRET_PROXY}


def test_network_error_masks_proxy(calls):
    calls.reply = requests.ConnectionError(f"cannot reach {SECRET_PROXY}")
    with pytest.raises(requests.ConnectionError) as info:
        Client(proxy=SECRET_PROXY).http.get("stats", "x")
    assert "hunter2" not in str(info.value)


def test_no_cache_by_default(calls):
    client = Client()
    client.http.get("stats", "x")
    client.http.get("stats", "x")
    assert len(calls) == 2


def test_cache_returns_saved_response(calls):
    client = Client(cache=True)
    first = client.http.get("stats", "x", {"a": 1})
    second = client.http.get("stats", "x", {"a": 1})
    assert len(calls) == 1
    assert second is first


def test_errors_are_not_cached(calls):
    calls.reply = FakeResponse(status_code=500, text="")
    client = Client(cache=True)
    for _ in range(2):
        with pytest.raises(HTTPStatusError):
            client.http.get("stats", "x")
    assert len(calls) == 2


def test_redirects_are_not_followed(calls):
    Client().http.get("stats", "x")
    assert calls[0]["allow_redirects"] is False
