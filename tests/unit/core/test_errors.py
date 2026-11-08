"""Error handling, using bodies NBA.com actually sent in live tests on 2026-10-24."""

import pickle

import pytest
import requests

from nba_api._core.client import Client
from nba_api._core.common.errors import (
    BlockedError,
    HTTPStatusError,
    InvalidResponseError,
    NBAAPIError,
    NotFoundError,
    ParameterError,
    ProxyError,
    TransportError,
)

SECRET_PROXY = "http://user:hunter2@proxy.example:8080"

S3_ACCESS_DENIED = (
    '<?xml version="1.0" encoding="UTF-8"?>\n<Error><Code>AccessDenied</Code>'
    "<Message>Access Denied</Message><RequestId>KN2T52V9WZDY4FXS</RequestId></Error>"
)
# Shapes from issues #696 (stats, status 200) and #672 (live, status 403).
AKAMAI_STATS_PAGE = (
    "<html><body><h1>We are unable to process your request at the moment</h1>"
    "<p>Reference Number: 18.4a2c1702.1759853012.1b2f3c4</p></body></html>"
)
AKAMAI_LIVE_PAGE = (
    "<HTML><HEAD><TITLE>Access Denied</TITLE></HEAD><BODY><H1>Access Denied</H1>"
    'You don\'t have permission to access "http://cdn.nba.com/x.json" on this server.'
    "<P>Reference #18.6d3c1702.1759853012.2a3b4c5</BODY></HTML>"
)


class FakeResponse:
    def __init__(self, status_code=200, text='{"ok": true}', url="https://x/y"):
        self.status_code = status_code
        self.text = text
        self.url = url


@pytest.fixture
def reply(monkeypatch):
    """Set ``reply.value`` to the FakeResponse or exception session.get should give."""

    class Reply:
        value = FakeResponse()

    def fake_get(self, url, **kwargs):
        if isinstance(Reply.value, Exception):
            raise Reply.value
        return Reply.value

    monkeypatch.setattr(requests.Session, "get", fake_get)
    monkeypatch.delenv("NBA_API_PROXY", raising=False)
    monkeypatch.delenv("NBA_API_REQUIRE_PROXY", raising=False)
    return Reply


def fetch(site="stats", proxy=None):
    return Client(proxy=proxy).http.get(site, "endpoint")


def test_bad_enum_is_parameter_error(reply):
    reply.value = FakeResponse(400, '{"PerMode":["Invalid parameters"]}')
    with pytest.raises(ParameterError) as info:
        fetch()
    assert info.value.fields == {"PerMode": ["Invalid parameters"]}
    assert "PerMode (Invalid parameters)" in str(info.value)
    assert info.value.response.status == 400


def test_400_without_json(reply):
    reply.value = FakeResponse(400, "Bad Request")
    with pytest.raises(ParameterError, match="Bad Request"):
        fetch()


def test_empty_500_hints_at_parameters(reply):
    reply.value = FakeResponse(500, "")
    with pytest.raises(HTTPStatusError, match="bad or missing parameter"):
        fetch()


def test_other_status(reply):
    reply.value = FakeResponse(503, "Service Unavailable")
    with pytest.raises(HTTPStatusError, match="503.*Service Unavailable") as info:
        fetch()
    assert info.value.response.status == 503


def test_redirect_is_not_found(reply):
    reply.value = FakeResponse(302, "")
    with pytest.raises(NotFoundError, match="doesn't exist"):
        fetch()


def test_missing_live_file_is_not_found(reply):
    reply.value = FakeResponse(403, S3_ACCESS_DENIED)
    with pytest.raises(NotFoundError, match="2019-20"):
        fetch("live")


@pytest.mark.parametrize(
    ("status", "page", "reference"),
    [
        (200, AKAMAI_STATS_PAGE, "18.4a2c1702.1759853012.1b2f3c4"),
        (403, AKAMAI_LIVE_PAGE, "18.6d3c1702.1759853012.2a3b4c5"),
    ],
)
def test_block_page_is_blocked_error(reply, status, page, reference):
    reply.value = FakeResponse(status, page)
    with pytest.raises(BlockedError, match="not a bug") as info:
        fetch()
    assert reference in str(info.value)


def test_200_html_is_invalid_response(reply):
    reply.value = FakeResponse(200, "<html>something else</html>")
    with pytest.raises(InvalidResponseError, match="isn't JSON"):
        fetch()


def test_empty_200_is_invalid_response(reply):
    reply.value = FakeResponse(200, "")
    with pytest.raises(InvalidResponseError, match="empty"):
        fetch()


def test_nba_generic_error_body(reply):
    reply.value = FakeResponse(200, '{"Message":"An error has occurred."}')
    with pytest.raises(InvalidResponseError, match="generic error"):
        fetch()


@pytest.mark.parametrize("body", ["{}", '{"resultSets": []}'])
def test_valid_json_is_not_an_error(reply, body):
    # Empty results ("player doesn't exist") are for the endpoint layer to judge.
    reply.value = FakeResponse(200, body)
    assert fetch().text == body


@pytest.mark.parametrize(
    ("theirs", "requests_type"),
    [
        (requests.ConnectTimeout("t"), requests.ConnectTimeout),
        (requests.ReadTimeout("t"), requests.ReadTimeout),
        (requests.ConnectionError("reset"), requests.ConnectionError),
        (requests.RequestException("other"), requests.RequestException),
    ],
)
def test_transport_errors_keep_requests_types(reply, theirs, requests_type):
    reply.value = theirs
    with pytest.raises(TransportError) as info:
        fetch()
    assert isinstance(info.value, requests_type)
    assert isinstance(info.value, requests.Timeout) == isinstance(
        theirs, requests.Timeout
    )
    assert "proxy usually helps" in str(info.value)


def test_proxy_error(reply):
    reply.value = requests.exceptions.ProxyError(f"407 from {SECRET_PROXY}")
    with pytest.raises(ProxyError, match="Check the proxy") as info:
        fetch(proxy=SECRET_PROXY)
    assert isinstance(info.value, requests.exceptions.ProxyError)
    assert "hunter2" not in str(info.value)
    assert info.value.__cause__ is None
    assert info.value.__context__ is None


@pytest.mark.parametrize(
    "error_type",
    [
        BlockedError,
        HTTPStatusError,
        InvalidResponseError,
        NotFoundError,
        ParameterError,
        TransportError,
        ProxyError,
    ],
)
def test_all_errors_share_the_base(error_type):
    assert issubclass(error_type, NBAAPIError)


def test_errors_pickle_with_their_response(reply):
    reply.value = FakeResponse(400, '{"PerMode":["Invalid parameters"]}')
    with pytest.raises(ParameterError) as info:
        fetch()
    copy = pickle.loads(pickle.dumps(info.value))
    assert str(copy) == str(info.value)
    assert copy.response == info.value.response
    assert copy.fields == info.value.fields


def test_transport_error_pickles(reply):
    reply.value = requests.ReadTimeout("t")
    with pytest.raises(TransportError) as info:
        fetch()
    copy = pickle.loads(pickle.dumps(info.value))
    assert type(copy) is type(info.value)
    assert str(copy) == str(info.value)
