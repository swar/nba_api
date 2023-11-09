import json
import pytest
from nba_api.library.http import NBAHTTP, NBAResponse
from nba_api.live.nba.endpoints import playbyplay
from nba_api.live.nba.library.http import NBALiveHTTP

content = {
    "meta": {
        "version": 1,
        "code": 200,
        "request": "http://nba.cloud/games/0022000180/playbyplay?Format=json",
        "time": "2021-01-15 23:48:58.906160",
    },
    "game": {
        "gameId": "0022000180",
        "actions": [
            {
                "actionNumber": 4,
                "clock": "PT11M58.00S",
                "timeActual": "2021-01-16T00:40:31.3Z",
                "period": 1,
                "periodType": "REGULAR",
                "teamId": 1610612738,
                "teamTricode": "BOS",
                "actionType": "jumpball",
                "subType": "recovered",
                "descriptor": "startperiod",
                "qualifiers": [],
                "personId": 1629684,
                "x": None,
                "y": None,
                "possession": 1610612738,
                "scoreHome": "0",
                "scoreAway": "0",
                "edited": "2021-01-16T00:40:31Z",
                "orderNumber": 40000,
                "xLegacy": None,
                "yLegacy": None,
                "isFieldGoal": 0,
                "jumpBallRecoveredName": "G. Williams",
                "jumpBallRecoverdPersonId": 1629684,
                "side": None,
                "playerName": "Williams",
                "playerNameI": "G. Williams",
                "personIdsFilter": [1629684, 202684, 202696],
                "jumpBallWonPlayerName": "Thompson",
                "jumpBallWonPersonId": 202684,
                "description": "Jump Ball T. Thompson vs. N. Vucevic: Tip to G. Williams",
                "jumpBallLostPlayerName": "Vucevic",
                "jumpBallLostPersonId": 202696,
            }
        ],
    },
}
actions = [
    {
        "actionNumber": 4,
        "clock": "PT11M58.00S",
        "timeActual": "2021-01-16T00:40:31.3Z",
        "period": 1,
        "periodType": "REGULAR",
        "teamId": 1610612738,
        "teamTricode": "BOS",
        "actionType": "jumpball",
        "subType": "recovered",
        "descriptor": "startperiod",
        "qualifiers": [],
        "personId": 1629684,
        "x": None,
        "y": None,
        "possession": 1610612738,
        "scoreHome": "0",
        "scoreAway": "0",
        "edited": "2021-01-16T00:40:31Z",
        "orderNumber": 40000,
        "xLegacy": None,
        "yLegacy": None,
        "isFieldGoal": 0,
        "jumpBallRecoveredName": "G. Williams",
        "jumpBallRecoverdPersonId": 1629684,
        "side": None,
        "playerName": "Williams",
        "playerNameI": "G. Williams",
        "personIdsFilter": [1629684, 202684, 202696],
        "jumpBallWonPlayerName": "Thompson",
        "jumpBallWonPersonId": 202684,
        "description": "Jump Ball T. Thompson vs. N. Vucevic: Tip to G. Williams",
        "jumpBallLostPlayerName": "Vucevic",
        "jumpBallLostPersonId": 202696,
    }
]
game_id = "0022000180"


@pytest.fixture
def nba_http_patch(monkeypatch):
    class MockResponse(object):
        def __init__(*args, **kwargs):
            pass

        def send_api_request(
            self,
            endpoint,
            parameters,
            referer=None,
            proxy=None,
            headers=None,
            timeout=None,
            raise_exception_on_error=False,
        ):
            url = NBALiveHTTP.base_url.format(endpoint=endpoint)
            return NBAResponse(response=json.dumps(content), status_code=200, url=url)

    monkeypatch.setattr(NBAHTTP, "send_api_request", MockResponse.send_api_request)


def test_get_request_url(nba_http_patch):
    assert (
        playbyplay.PlayByPlay(game_id).get_request_url()
        == "https://cdn.nba.com/static/json/liveData/playbyplay/playbyplay_0022000180.json"
    )


def test_get_actions_dict(nba_http_patch):
    assert playbyplay.PlayByPlay(game_id).actions.get_dict() == actions


def test_get_dict(nba_http_patch):
    assert playbyplay.PlayByPlay(game_id).get_dict() == content
