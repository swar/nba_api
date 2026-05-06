"""Tests for bug fixes in HTTP layer."""

from unittest.mock import Mock

import pytest
import requests

from nba_api.library.http import NBAHTTP, NBAResponse
from nba_api.stats.library.http import NBAStatsHTTP, NBAStatsResponse


@pytest.fixture(autouse=True)
def cleanup():
    NBAHTTP._session = None
    yield
    NBAHTTP._session = None


@pytest.fixture
def mock_session():
    session = Mock(spec=requests.Session)
    mock_response = Mock()
    mock_response.text = '{"resultSets": []}'
    mock_response.status_code = 200
    mock_response.url = "https://stats.nba.com/stats/test"
    session.get.return_value = mock_response
    return session


class TestHeadersMutationFix:
    """Headers dict must not be mutated when referer is passed."""

    def test_referer_does_not_mutate_class_headers(self, mock_session):
        NBAHTTP.set_session(mock_session)
        http = NBAStatsHTTP()
        original_headers = http.headers.copy()

        http.send_api_request(
            endpoint="test",
            parameters={},
            referer="https://www.nba.com/game/123",
        )

        assert http.headers == original_headers

    def test_referer_is_sent_in_request(self, mock_session):
        NBAHTTP.set_session(mock_session)
        http = NBAStatsHTTP()

        http.send_api_request(
            endpoint="test",
            parameters={},
            referer="https://www.nba.com/game/123",
        )

        call_kwargs = mock_session.get.call_args.kwargs
        assert call_kwargs["headers"]["Referer"] == "https://www.nba.com/game/123"

    def test_no_referer_uses_original_headers_object(self, mock_session):
        NBAHTTP.set_session(mock_session)
        http = NBAStatsHTTP()
        original_id = id(http.headers)

        http.send_api_request(
            endpoint="test",
            parameters={},
        )

        call_kwargs = mock_session.get.call_args.kwargs
        assert id(call_kwargs["headers"]) == original_id

    def test_custom_headers_override(self, mock_session):
        NBAHTTP.set_session(mock_session)
        http = NBAStatsHTTP()
        custom = {"X-Custom": "value"}

        http.send_api_request(
            endpoint="test",
            parameters={},
            headers=custom,
        )

        call_kwargs = mock_session.get.call_args.kwargs
        assert call_kwargs["headers"] == custom


class TestGetParserReturnsNone:
    """get_parser_for_endpoint returns None for unregistered endpoints."""

    def test_unregistered_endpoint_returns_none(self):
        from nba_api.stats.endpoints._parsers import get_parser_for_endpoint

        result = get_parser_for_endpoint("nonexistent_endpoint_xyz", {})
        assert result is None

    def test_registered_endpoint_returns_parser(self):
        from nba_api.stats.endpoints._parsers import get_parser_for_endpoint

        parser = get_parser_for_endpoint("boxscoreadvancedv3", {"some": "data"})
        assert parser is not None


class TestGetLegacyResults:
    """_get_legacy_results helper extracts resultSets/resultSet correctly."""

    def test_result_sets_plural(self):
        data = {"resultSets": [{"name": "A", "headers": [], "rowSet": []}]}
        result = NBAStatsResponse._get_legacy_results(data)
        assert result == [{"name": "A", "headers": [], "rowSet": []}]

    def test_result_set_singular(self):
        data = {"resultSet": {"name": "B", "headers": [], "rowSet": []}}
        result = NBAStatsResponse._get_legacy_results(data)
        assert result == {"name": "B", "headers": [], "rowSet": []}

    def test_neither_key_returns_none(self):
        data = {"someOtherKey": "value"}
        result = NBAStatsResponse._get_legacy_results(data)
        assert result is None

    def test_prefers_result_sets_over_result_set(self):
        data = {
            "resultSets": [{"name": "A"}],
            "resultSet": {"name": "B"},
        }
        result = NBAStatsResponse._get_legacy_results(data)
        assert result == [{"name": "A"}]


class TestGetDataSetsMissingKeys:
    """get_data_sets returns {} when legacy keys are missing."""

    def test_no_legacy_keys_returns_empty(self):
        resp = NBAStatsResponse(
            response='{"meta": {"version": 1}}',
            status_code=200,
            url="https://test",
        )
        assert resp.get_data_sets() == {}

    def test_no_legacy_keys_with_endpoint_no_parser(self):
        resp = NBAStatsResponse(
            response='{"meta": {"version": 1}}',
            status_code=200,
            url="https://test",
        )
        assert resp.get_data_sets(endpoint="nonexistent_xyz") == {}


class TestNBAResponseTypeHints:
    """Verify NBAResponse handles typed None values correctly."""

    def test_status_code_none(self):
        resp = NBAResponse(response="{}", status_code=None, url=None)
        assert resp.get_status_code() is None
        assert resp.get_url() is None

    def test_valid_json_check(self):
        resp = NBAResponse(response="not json", status_code=200, url="http://test")
        assert resp.valid_json() is False

    def test_valid_json_success(self):
        resp = NBAResponse(response='{"ok": true}', status_code=200, url="http://test")
        assert resp.valid_json() is True
