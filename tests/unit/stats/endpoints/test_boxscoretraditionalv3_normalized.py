import json
from unittest.mock import patch

import pytest

from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.endpoints.boxscoretraditionalv3 import BoxScoreTraditionalV3
from nba_api.stats.library.http import NBAStatsResponse

from .data.boxscoretraditionalv3 import BOXSCORETRADITIONALV3_SAMPLE

GAME_ID = "0022500165"


class MockResponse(NBAStatsResponse):
    def __init__(self, data):
        super().__init__(json.dumps(data), 200, "http://mock.url")
        self._mock_data = data

    def get_dict(self):
        return self._mock_data


@pytest.fixture
def endpoint():
    return BoxScoreTraditionalV3(game_id=GAME_ID, get_request=False)


@pytest.fixture
def loaded_endpoint(endpoint):
    endpoint.nba_response = MockResponse(BOXSCORETRADITIONALV3_SAMPLE)
    endpoint.load_response()
    return endpoint


@pytest.fixture
def normalized_dict(loaded_endpoint):
    return loaded_endpoint.get_normalized_dict()


class TestBoxScoreTraditionalV3Normalized:
    def test_get_normalized_dict_returns_data(self, normalized_dict):
        assert isinstance(normalized_dict, dict)
        assert len(normalized_dict) > 0, (
            "get_normalized_dict() should not return empty dict"
        )

        assert "PlayerStats" in normalized_dict
        assert "TeamStats" in normalized_dict
        assert "TeamStarterBenchStats" in normalized_dict

    def test_get_normalized_dict_structure(self, normalized_dict):
        result = normalized_dict

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

    def test_get_normalized_json_returns_data(self, loaded_endpoint):
        result = loaded_endpoint.get_normalized_json()

        assert isinstance(result, str)
        assert len(result) > 2, "get_normalized_json() should not return empty JSON"
        assert result != "{}", "get_normalized_json() should not return empty object"

        parsed = json.loads(result)
        assert isinstance(parsed, dict)
        assert len(parsed) > 0

    def test_get_normalized_json_is_valid_json(self, loaded_endpoint, normalized_dict):
        json_str = loaded_endpoint.get_normalized_json()
        parsed = json.loads(json_str)

        assert parsed == normalized_dict

    def test_get_normalized_dict_player_data_correctness(self, normalized_dict):
        result = normalized_dict
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

    def test_get_normalized_dict_team_data_correctness(self, normalized_dict):
        result = normalized_dict
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

    def test_regression_issue_602(self, loaded_endpoint, normalized_dict):
        assert normalized_dict != {}, (
            "Issue #602: get_normalized_dict() returns empty dict"
        )
        assert len(normalized_dict) > 0, "Issue #602: get_normalized_dict() has no data"

        normalized_json = loaded_endpoint.get_normalized_json()
        assert normalized_json != "{}", (
            "Issue #602: get_normalized_json() returns empty JSON"
        )
        assert len(normalized_json) > 2, "Issue #602: get_normalized_json() has no data"

        parsed = json.loads(normalized_json)
        assert len(parsed) > 0, "Issue #602: Parsed JSON is empty"

    def test_get_available_data_matches_normalized_keys(
        self, loaded_endpoint, normalized_dict
    ):
        assert set(loaded_endpoint.get_available_data()) == set(normalized_dict.keys())

    def test_load_response_initializes_data_sets_and_attributes(self, loaded_endpoint):
        assert len(loaded_endpoint.data_sets) == 3
        assert all(
            isinstance(data_set, Endpoint.DataSet)
            for data_set in loaded_endpoint.data_sets
        )

        assert isinstance(loaded_endpoint.player_stats, Endpoint.DataSet)
        assert isinstance(loaded_endpoint.team_starter_bench_stats, Endpoint.DataSet)
        assert isinstance(loaded_endpoint.team_stats, Endpoint.DataSet)

    def test_normalized_schema_matches_expected_data(self, normalized_dict):
        for (
            data_set_name,
            expected_headers,
        ) in BoxScoreTraditionalV3.expected_data.items():
            rows = normalized_dict[data_set_name]
            assert rows, f"{data_set_name} should contain fixture rows"
            assert sorted(rows[0].keys()) == sorted(expected_headers)

    def test_endpoint_initialization_with_custom_parameters(self):
        custom_headers = {"User-Agent": "test-agent"}
        endpoint = BoxScoreTraditionalV3(
            game_id=GAME_ID,
            end_period=2,
            end_range=24000,
            range_type=1,
            start_period=1,
            start_range=0,
            proxy="http://proxy.local:8080",
            headers=custom_headers,
            timeout=45,
            get_request=False,
        )

        assert endpoint.parameters == {
            "GameID": GAME_ID,
            "EndPeriod": 2,
            "EndRange": 24000,
            "RangeType": 1,
            "StartPeriod": 1,
            "StartRange": 0,
        }
        assert endpoint.proxy == "http://proxy.local:8080"
        assert endpoint.headers == custom_headers
        assert endpoint.timeout == 45

    @patch(
        "nba_api.stats.endpoints.boxscoretraditionalv3.NBAStatsHTTP.send_api_request"
    )
    def test_get_request_loads_response_data_sets(self, mock_send_request):
        mock_send_request.return_value = MockResponse(BOXSCORETRADITIONALV3_SAMPLE)

        endpoint = BoxScoreTraditionalV3(game_id=GAME_ID)

        mock_send_request.assert_called_once_with(
            endpoint="boxscoretraditionalv3",
            parameters={
                "GameID": GAME_ID,
                "EndPeriod": "0",
                "EndRange": "0",
                "RangeType": "0",
                "StartPeriod": "0",
                "StartRange": "0",
            },
            proxy=None,
            headers=None,
            timeout=30,
        )
        assert endpoint.get_request_url() == "http://mock.url"
        assert len(endpoint.get_normalized_dict()["TeamStarterBenchStats"]) == 4
