"""Unit tests for BoxScoreTraditionalV3 get_normalized_dict() and get_normalized_json() methods.

Tests for GitHub issue #602: https://github.com/swar/nba_api/issues/602
"""

import json
import pytest
from nba_api.stats.endpoints.boxscoretraditionalv3 import BoxScoreTraditionalV3
from nba_api.stats.library.http import NBAStatsResponse
from .data.boxscoretraditionalv3 import BOXSCORETRADITIONALV3_SAMPLE


class MockResponse(NBAStatsResponse):
    """Mock NBA Stats HTTP response."""

    def __init__(self, data):
        # Call parent with dummy values for response, status_code, and url
        super().__init__(json.dumps(data), 200, "http://mock.url")
        self._mock_data = data

    def get_dict(self):
        return self._mock_data


class TestBoxScoreTraditionalV3Normalized:
    """Test normalized dict/json methods for BoxScoreTraditionalV3 endpoint."""

    def test_get_normalized_dict_returns_data(self):
        """Test that get_normalized_dict() returns non-empty data for V3 endpoints."""
        # Create endpoint with mocked response
        endpoint = BoxScoreTraditionalV3(game_id="0022500165", get_request=False)
        endpoint.nba_response = MockResponse(BOXSCORETRADITIONALV3_SAMPLE)
        endpoint.load_response()

        # Call get_normalized_dict()
        result = endpoint.get_normalized_dict()

        # Verify it returns non-empty data
        assert isinstance(result, dict)
        assert len(result) > 0, "get_normalized_dict() should not return empty dict"

        # Verify expected datasets are present
        assert "PlayerStats" in result
        assert "TeamStats" in result
        assert "TeamStarterBenchStats" in result

    def test_get_normalized_dict_structure(self):
        """Test that get_normalized_dict() returns correct structure."""
        endpoint = BoxScoreTraditionalV3(game_id="0022500165", get_request=False)
        endpoint.nba_response = MockResponse(BOXSCORETRADITIONALV3_SAMPLE)
        endpoint.load_response()

        result = endpoint.get_normalized_dict()

        # Each dataset should be a list of dicts
        assert isinstance(result["PlayerStats"], list)
        assert isinstance(result["TeamStats"], list)
        assert isinstance(result["TeamStarterBenchStats"], list)

        # Check that rows are dicts with proper keys
        if result["PlayerStats"]:
            first_player = result["PlayerStats"][0]
            assert isinstance(first_player, dict)
            assert "gameId" in first_player
            assert "personId" in first_player
            assert "firstName" in first_player
            assert "points" in first_player

        if result["TeamStats"]:
            first_team = result["TeamStats"][0]
            assert isinstance(first_team, dict)
            assert "gameId" in first_team
            assert "teamId" in first_team
            assert "teamName" in first_team
            assert "points" in first_team

    def test_get_normalized_json_returns_data(self):
        """Test that get_normalized_json() returns non-empty JSON string."""
        endpoint = BoxScoreTraditionalV3(game_id="0022500165", get_request=False)
        endpoint.nba_response = MockResponse(BOXSCORETRADITIONALV3_SAMPLE)
        endpoint.load_response()

        result = endpoint.get_normalized_json()

        # Verify it returns non-empty JSON string
        assert isinstance(result, str)
        assert len(result) > 2, "get_normalized_json() should not return empty JSON"
        assert result != "{}", "get_normalized_json() should not return empty object"

        # Verify it's valid JSON
        parsed = json.loads(result)
        assert isinstance(parsed, dict)
        assert len(parsed) > 0

    def test_get_normalized_json_is_valid_json(self):
        """Test that get_normalized_json() returns valid, parseable JSON."""
        endpoint = BoxScoreTraditionalV3(game_id="0022500165", get_request=False)
        endpoint.nba_response = MockResponse(BOXSCORETRADITIONALV3_SAMPLE)
        endpoint.load_response()

        json_str = endpoint.get_normalized_json()
        parsed = json.loads(json_str)

        # Verify structure matches get_normalized_dict()
        dict_result = endpoint.get_normalized_dict()
        assert parsed == dict_result

    def test_get_normalized_dict_player_data_correctness(self):
        """Test that normalized PlayerStats data is correct."""
        endpoint = BoxScoreTraditionalV3(game_id="0022500165", get_request=False)
        endpoint.nba_response = MockResponse(BOXSCORETRADITIONALV3_SAMPLE)
        endpoint.load_response()

        result = endpoint.get_normalized_dict()
        player_stats = result["PlayerStats"]

        # Should have 2 players based on fixture
        assert len(player_stats) == 2

        # Check first player (Jayson Tatum)
        tatum = player_stats[0]
        assert tatum["gameId"] == "0022500165"
        assert tatum["teamId"] == 1610612738  # BOS
        assert tatum["personId"] == 1630162
        assert tatum["firstName"] == "Jayson"
        assert tatum["familyName"] == "Tatum"
        assert tatum["points"] == 32
        assert tatum["plusMinusPoints"] == 12

    def test_get_normalized_dict_team_data_correctness(self):
        """Test that normalized TeamStats data is correct."""
        endpoint = BoxScoreTraditionalV3(game_id="0022500165", get_request=False)
        endpoint.nba_response = MockResponse(BOXSCORETRADITIONALV3_SAMPLE)
        endpoint.load_response()

        result = endpoint.get_normalized_dict()
        team_stats = result["TeamStats"]

        # Should have 2 teams
        assert len(team_stats) == 2

        # Check home team (Celtics)
        celtics = team_stats[0]
        assert celtics["gameId"] == "0022500165"
        assert celtics["teamId"] == 1610612738
        assert celtics["teamCity"] == "Boston"
        assert celtics["teamName"] == "Celtics"
        assert celtics["points"] == 122
        assert celtics["plusMinusPoints"] == 14

        # Check away team (Warriors)
        warriors = team_stats[1]
        assert warriors["teamId"] == 1610612744
        assert warriors["teamCity"] == "Golden State"
        assert warriors["points"] == 108
        assert warriors["plusMinusPoints"] == -14

    def test_regression_issue_602(self):
        """Regression test for GitHub issue #602.

        Issue #602 reported that get_normalized_dict() and get_normalized_json()
        returned empty values for BoxScoreTraditionalV3 endpoint.

        This test ensures the bug does not reoccur.
        """
        endpoint = BoxScoreTraditionalV3(game_id="0022500165", get_request=False)
        endpoint.nba_response = MockResponse(BOXSCORETRADITIONALV3_SAMPLE)
        endpoint.load_response()

        # Test get_normalized_dict()
        normalized_dict = endpoint.get_normalized_dict()
        assert normalized_dict != {}, "Issue #602: get_normalized_dict() returns empty dict"
        assert len(normalized_dict) > 0, "Issue #602: get_normalized_dict() has no data"

        # Test get_normalized_json()
        normalized_json = endpoint.get_normalized_json()
        assert normalized_json != "{}", "Issue #602: get_normalized_json() returns empty JSON"
        assert len(normalized_json) > 2, "Issue #602: get_normalized_json() has no data"

        # Verify the JSON is parseable and non-empty
        parsed = json.loads(normalized_json)
        assert len(parsed) > 0, "Issue #602: Parsed JSON is empty"
