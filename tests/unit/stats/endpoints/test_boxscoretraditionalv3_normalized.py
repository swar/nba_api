import json
import pytest
from nba_api.stats.endpoints.boxscoretraditionalv3 import BoxScoreTraditionalV3
from nba_api.stats.library.http import NBAStatsResponse
from .data.boxscoretraditionalv3 import BOXSCORETRADITIONALV3_SAMPLE


class MockResponse(NBAStatsResponse):

    def __init__(self, data):
        super().__init__(json.dumps(data), 200, "http://mock.url")
        self._mock_data = data

    def get_dict(self):
        return self._mock_data


class TestBoxScoreTraditionalV3Normalized:

    def test_get_normalized_dict_returns_data(self):
        endpoint = BoxScoreTraditionalV3(game_id="0022500165", get_request=False)
        endpoint.nba_response = MockResponse(BOXSCORETRADITIONALV3_SAMPLE)
        endpoint.load_response()

        result = endpoint.get_normalized_dict()

        assert isinstance(result, dict)
        assert len(result) > 0, "get_normalized_dict() should not return empty dict"

        assert "PlayerStats" in result
        assert "TeamStats" in result
        assert "TeamStarterBenchStats" in result

    def test_get_normalized_dict_structure(self):
        endpoint = BoxScoreTraditionalV3(game_id="0022500165", get_request=False)
        endpoint.nba_response = MockResponse(BOXSCORETRADITIONALV3_SAMPLE)
        endpoint.load_response()

        result = endpoint.get_normalized_dict()

        assert isinstance(result["PlayerStats"], list)
        assert isinstance(result["TeamStats"], list)
        assert isinstance(result["TeamStarterBenchStats"], list)

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
        endpoint = BoxScoreTraditionalV3(game_id="0022500165", get_request=False)
        endpoint.nba_response = MockResponse(BOXSCORETRADITIONALV3_SAMPLE)
        endpoint.load_response()

        result = endpoint.get_normalized_json()

        assert isinstance(result, str)
        assert len(result) > 2, "get_normalized_json() should not return empty JSON"
        assert result != "{}", "get_normalized_json() should not return empty object"

        parsed = json.loads(result)
        assert isinstance(parsed, dict)
        assert len(parsed) > 0

    def test_get_normalized_json_is_valid_json(self):
        endpoint = BoxScoreTraditionalV3(game_id="0022500165", get_request=False)
        endpoint.nba_response = MockResponse(BOXSCORETRADITIONALV3_SAMPLE)
        endpoint.load_response()

        json_str = endpoint.get_normalized_json()
        parsed = json.loads(json_str)

        dict_result = endpoint.get_normalized_dict()
        assert parsed == dict_result

    def test_get_normalized_dict_player_data_correctness(self):
        endpoint = BoxScoreTraditionalV3(game_id="0022500165", get_request=False)
        endpoint.nba_response = MockResponse(BOXSCORETRADITIONALV3_SAMPLE)
        endpoint.load_response()

        result = endpoint.get_normalized_dict()
        player_stats = result["PlayerStats"]

        assert len(player_stats) == 2

        tatum = player_stats[0]
        assert tatum["gameId"] == "0022500165"
        assert tatum["teamId"] == 1610612738
        assert tatum["personId"] == 1630162
        assert tatum["firstName"] == "Jayson"
        assert tatum["familyName"] == "Tatum"
        assert tatum["points"] == 32
        assert tatum["plusMinusPoints"] == 12

    def test_get_normalized_dict_team_data_correctness(self):
        endpoint = BoxScoreTraditionalV3(game_id="0022500165", get_request=False)
        endpoint.nba_response = MockResponse(BOXSCORETRADITIONALV3_SAMPLE)
        endpoint.load_response()

        result = endpoint.get_normalized_dict()
        team_stats = result["TeamStats"]

        assert len(team_stats) == 2

        celtics = team_stats[0]
        assert celtics["gameId"] == "0022500165"
        assert celtics["teamId"] == 1610612738
        assert celtics["teamCity"] == "Boston"
        assert celtics["teamName"] == "Celtics"
        assert celtics["points"] == 122
        assert celtics["plusMinusPoints"] == 14

        warriors = team_stats[1]
        assert warriors["teamId"] == 1610612744
        assert warriors["teamCity"] == "Golden State"
        assert warriors["points"] == 108
        assert warriors["plusMinusPoints"] == -14

    def test_regression_issue_602(self):
        endpoint = BoxScoreTraditionalV3(game_id="0022500165", get_request=False)
        endpoint.nba_response = MockResponse(BOXSCORETRADITIONALV3_SAMPLE)
        endpoint.load_response()

        normalized_dict = endpoint.get_normalized_dict()
        assert normalized_dict != {}, "Issue #602: get_normalized_dict() returns empty dict"
        assert len(normalized_dict) > 0, "Issue #602: get_normalized_dict() has no data"

        normalized_json = endpoint.get_normalized_json()
        assert normalized_json != "{}", "Issue #602: get_normalized_json() returns empty JSON"
        assert len(normalized_json) > 2, "Issue #602: get_normalized_json() has no data"

        parsed = json.loads(normalized_json)
        assert len(parsed) > 0, "Issue #602: Parsed JSON is empty"
