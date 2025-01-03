import pytest
import requests
from unittest.mock import Mock
from nba_api.library.http import NBAHTTP
from nba_api.stats.endpoints import AllTimeLeadersGrids

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
    try:
        _ = AllTimeLeadersGrids(topx=5)
    except KeyError:
        # This is expected due to the mock response.
        pass
    
    # Verify the session's get method was called
    assert mock_session.get.called
    
    # Verify the call parameters
    call_kwargs = mock_session.get.call_args.kwargs
    assert 'params' in call_kwargs
    assert 'TopX' in dict(call_kwargs['params'])
    assert dict(call_kwargs['params'])['TopX'] == 5

def test_session_headers_persistence():
    # Create session with custom headers
    session = requests.Session()
    custom_user_agent = 'CustomBot/1.0'
    session.headers.update({'User-Agent': custom_user_agent})
    
    # Set as global session
    NBAHTTP.set_session(session)
    
    # Verify headers are maintained
    current_session = NBAHTTP.get_session()
    assert current_session.headers['User-Agent'] == custom_user_agent

@pytest.fixture(autouse=True)
def cleanup():
    # Reset session before each test
    NBAHTTP._session = None
    yield
    # Clean up after each test
    NBAHTTP._session = None
