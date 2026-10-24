from contextlib import suppress
from unittest.mock import Mock

import pytest
import requests

from nba_api.library.http import NBAHTTP, NBAResponse
from nba_api.live.nba.library.http import NBALiveHTTP
from nba_api.stats.endpoints import AllTimeLeadersGrids
from nba_api.stats.library.http import NBAStatsHTTP


@pytest.fixture
def mock_session():
    session = Mock(spec=requests.Session)
    # Mock the get method to return a response-like object
    mock_response = Mock()
    mock_response.text = '{"resource": "alltimeleadersgrids", "resultSets": {}}'
    mock_response.status_code = 200
    mock_response.url = "http://stats.nba.com/stats/alltimeleadersgrids"
    session.get.return_value = mock_response
    return session


def test_nbahttp_session_management():
    # Test default session creation
    assert NBAHTTP._session is None
    session = NBAHTTP.get_session()
    assert isinstance(session, requests.Session)

    # Test setting custom session
    custom_session = requests.Session()
    NBAHTTP.set_session(custom_session)
    assert NBAHTTP.get_session() == custom_session


def test_endpoint_uses_global_session(mock_session):
    # Set up global session
    NBAHTTP.set_session(mock_session)

    # Create endpoint and make request
    with suppress(KeyError):  # This is expected due to the mock response.
        _ = AllTimeLeadersGrids(topx=5)

    # Verify the session's get method was called
    assert mock_session.get.called

    # Verify the call parameters
    call_kwargs = mock_session.get.call_args.kwargs
    assert "params" in call_kwargs
    assert "TopX" in dict(call_kwargs["params"])
    assert dict(call_kwargs["params"])["TopX"] == 5


def test_session_headers_persistence():
    # Create session with custom headers
    session = requests.Session()
    custom_user_agent = "CustomBot/1.0"
    session.headers.update({"User-Agent": custom_user_agent})

    # Set as global session
    NBAHTTP.set_session(session)

    # Verify headers are maintained
    current_session = NBAHTTP.get_session()
    assert current_session.headers["User-Agent"] == custom_user_agent


@pytest.fixture(autouse=True)
def cleanup():
    # Reset session before each test
    NBAHTTP._session = None
    yield
    # Clean up after each test
    NBAHTTP._session = None


def test_referer_does_not_change_default_headers(mock_session):
    from nba_api.stats.library.http import NBAStatsHTTP

    NBAHTTP.set_session(mock_session)
    defaults = dict(NBAStatsHTTP.headers)

    NBAStatsHTTP().send_api_request(
        endpoint="alltimeleadersgrids", parameters={}, referer="https://example.com"
    )

    assert mock_session.get.call_args.kwargs["headers"]["Referer"] == (
        "https://example.com"
    )
    assert NBAStatsHTTP.headers == defaults


@pytest.mark.parametrize("http_class", [NBAHTTP, NBAStatsHTTP, NBALiveHTTP])
def test_clean_contents_replaces_api_error_body(http_class):
    cleaned = http_class().clean_contents('{"Message":"An error has occurred."}')
    assert not NBAResponse(response=cleaned, status_code=200, url="").valid_json()


@pytest.mark.parametrize("http_class", [NBAHTTP, NBAStatsHTTP, NBALiveHTTP])
def test_clean_contents_keeps_other_text(http_class):
    contents = '{"resultSets": []}'
    assert http_class().clean_contents(contents) == contents
