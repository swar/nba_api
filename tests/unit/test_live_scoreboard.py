import json
import pytest
from nba_api.library.http import NBAHTTP, NBAResponse
from nba_api.live.nba.endpoints import scoreboard
from nba_api.live.nba.library.http import NBALiveHTTP

content = {
    "meta": {
        "version": 1,
        "request": "https://nba-prod-us-east-1-mediaops-stats.s3.amazonaws.com/NBA/liveData/scoreboard/todaysScoreboard_00.json",
        "time": "2021-01-16 02:21:14.2114",
        "code": 200,
    },
    "scoreboard": {
        "gameDate": "2021-01-16",
        "leagueId": "00",
        "leagueName": "National Basketball Association",
        "games": [
            {
                "gameId": "0022000194",
                "gameCode": "20210116/INDPHX",
                "gameStatus": 1,
                "gameStatusText": "PPD",
                "period": 0,
                "gameClock": "",
                "gameTimeUTC": "2021-01-17T02:00:00Z",
                "gameEt": "2021-01-16T21:00:00Z",
                "regulationPeriods": 4,
                "seriesGameNumber": "",
                "seriesText": "",
                "homeTeam": {
                    "teamId": 1610612756,
                    "teamName": "Suns",
                    "teamCity": "Phoenix",
                    "teamTricode": "PHX",
                    "wins": 7,
                    "losses": 4,
                    "score": 0,
                    "inBonus": None,
                    "timeoutsRemaining": 0,
                    "periods": [
                        {"period": 1, "periodType": "REGULAR", "score": 0},
                        {"period": 2, "periodType": "REGULAR", "score": 0},
                        {"period": 3, "periodType": "REGULAR", "score": 0},
                        {"period": 4, "periodType": "REGULAR", "score": 0},
                    ],
                },
                "awayTeam": {
                    "teamId": 1610612754,
                    "teamName": "Pacers",
                    "teamCity": "Indiana",
                    "teamTricode": "IND",
                    "wins": 8,
                    "losses": 4,
                    "score": 0,
                    "inBonus": None,
                    "timeoutsRemaining": 0,
                    "periods": [
                        {"period": 1, "periodType": "REGULAR", "score": 0},
                        {"period": 2, "periodType": "REGULAR", "score": 0},
                        {"period": 3, "periodType": "REGULAR", "score": 0},
                        {"period": 4, "periodType": "REGULAR", "score": 0},
                    ],
                },
                "gameLeaders": {
                    "homeLeaders": {
                        "personId": 0,
                        "name": "",
                        "jerseyNum": "",
                        "position": "",
                        "teamTricode": "PHX",
                        "playerSlug": None,
                        "points": 0,
                        "rebounds": 0,
                        "assists": 0,
                    },
                    "awayLeaders": {
                        "personId": 0,
                        "name": "",
                        "jerseyNum": "",
                        "position": "",
                        "teamTricode": "IND",
                        "playerSlug": None,
                        "points": 0,
                        "rebounds": 0,
                        "assists": 0,
                    },
                },
                "pbOdds": {"team": None, "odds": 0.0, "suspended": 1},
            },
            {
                "gameId": "0022000189",
                "gameCode": "20210116/HOUSAS",
                "gameStatus": 1,
                "gameStatusText": "5:00 pm ET",
                "period": 0,
                "gameClock": "",
                "gameTimeUTC": "2021-01-16T22:00:00Z",
                "gameEt": "2021-01-16T17:00:00Z",
                "regulationPeriods": 4,
                "seriesGameNumber": "",
                "seriesText": "",
                "homeTeam": {
                    "teamId": 1610612759,
                    "teamName": "Spurs",
                    "teamCity": "San Antonio",
                    "teamTricode": "SAS",
                    "wins": 6,
                    "losses": 6,
                    "score": 0,
                    "inBonus": None,
                    "timeoutsRemaining": 0,
                    "periods": [
                        {"period": 1, "periodType": "REGULAR", "score": 0},
                        {"period": 2, "periodType": "REGULAR", "score": 0},
                        {"period": 3, "periodType": "REGULAR", "score": 0},
                        {"period": 4, "periodType": "REGULAR", "score": 0},
                    ],
                },
                "awayTeam": {
                    "teamId": 1610612745,
                    "teamName": "Rockets",
                    "teamCity": "Houston",
                    "teamTricode": "HOU",
                    "wins": 4,
                    "losses": 6,
                    "score": 0,
                    "inBonus": None,
                    "timeoutsRemaining": 0,
                    "periods": [
                        {"period": 1, "periodType": "REGULAR", "score": 0},
                        {"period": 2, "periodType": "REGULAR", "score": 0},
                        {"period": 3, "periodType": "REGULAR", "score": 0},
                        {"period": 4, "periodType": "REGULAR", "score": 0},
                    ],
                },
                "gameLeaders": {
                    "homeLeaders": {
                        "personId": 0,
                        "name": "",
                        "jerseyNum": "",
                        "position": "",
                        "teamTricode": "SAS",
                        "playerSlug": None,
                        "points": 0,
                        "rebounds": 0,
                        "assists": 0,
                    },
                    "awayLeaders": {
                        "personId": 0,
                        "name": "",
                        "jerseyNum": "",
                        "position": "",
                        "teamTricode": "HOU",
                        "playerSlug": None,
                        "points": 0,
                        "rebounds": 0,
                        "assists": 0,
                    },
                },
                "pbOdds": {"team": None, "odds": 0.0, "suspended": 1},
            },
        ],
    },
}

games = [
    {
        "gameId": "0022000194",
        "gameCode": "20210116/INDPHX",
        "gameStatus": 1,
        "gameStatusText": "PPD",
        "period": 0,
        "gameClock": "",
        "gameTimeUTC": "2021-01-17T02:00:00Z",
        "gameEt": "2021-01-16T21:00:00Z",
        "regulationPeriods": 4,
        "seriesGameNumber": "",
        "seriesText": "",
        "homeTeam": {
            "teamId": 1610612756,
            "teamName": "Suns",
            "teamCity": "Phoenix",
            "teamTricode": "PHX",
            "wins": 7,
            "losses": 4,
            "score": 0,
            "inBonus": None,
            "timeoutsRemaining": 0,
            "periods": [
                {"period": 1, "periodType": "REGULAR", "score": 0},
                {"period": 2, "periodType": "REGULAR", "score": 0},
                {"period": 3, "periodType": "REGULAR", "score": 0},
                {"period": 4, "periodType": "REGULAR", "score": 0},
            ],
        },
        "awayTeam": {
            "teamId": 1610612754,
            "teamName": "Pacers",
            "teamCity": "Indiana",
            "teamTricode": "IND",
            "wins": 8,
            "losses": 4,
            "score": 0,
            "inBonus": None,
            "timeoutsRemaining": 0,
            "periods": [
                {"period": 1, "periodType": "REGULAR", "score": 0},
                {"period": 2, "periodType": "REGULAR", "score": 0},
                {"period": 3, "periodType": "REGULAR", "score": 0},
                {"period": 4, "periodType": "REGULAR", "score": 0},
            ],
        },
        "gameLeaders": {
            "homeLeaders": {
                "personId": 0,
                "name": "",
                "jerseyNum": "",
                "position": "",
                "teamTricode": "PHX",
                "playerSlug": None,
                "points": 0,
                "rebounds": 0,
                "assists": 0,
            },
            "awayLeaders": {
                "personId": 0,
                "name": "",
                "jerseyNum": "",
                "position": "",
                "teamTricode": "IND",
                "playerSlug": None,
                "points": 0,
                "rebounds": 0,
                "assists": 0,
            },
        },
        "pbOdds": {"team": None, "odds": 0.0, "suspended": 1},
    },
    {
        "gameId": "0022000189",
        "gameCode": "20210116/HOUSAS",
        "gameStatus": 1,
        "gameStatusText": "5:00 pm ET",
        "period": 0,
        "gameClock": "",
        "gameTimeUTC": "2021-01-16T22:00:00Z",
        "gameEt": "2021-01-16T17:00:00Z",
        "regulationPeriods": 4,
        "seriesGameNumber": "",
        "seriesText": "",
        "homeTeam": {
            "teamId": 1610612759,
            "teamName": "Spurs",
            "teamCity": "San Antonio",
            "teamTricode": "SAS",
            "wins": 6,
            "losses": 6,
            "score": 0,
            "inBonus": None,
            "timeoutsRemaining": 0,
            "periods": [
                {"period": 1, "periodType": "REGULAR", "score": 0},
                {"period": 2, "periodType": "REGULAR", "score": 0},
                {"period": 3, "periodType": "REGULAR", "score": 0},
                {"period": 4, "periodType": "REGULAR", "score": 0},
            ],
        },
        "awayTeam": {
            "teamId": 1610612745,
            "teamName": "Rockets",
            "teamCity": "Houston",
            "teamTricode": "HOU",
            "wins": 4,
            "losses": 6,
            "score": 0,
            "inBonus": None,
            "timeoutsRemaining": 0,
            "periods": [
                {"period": 1, "periodType": "REGULAR", "score": 0},
                {"period": 2, "periodType": "REGULAR", "score": 0},
                {"period": 3, "periodType": "REGULAR", "score": 0},
                {"period": 4, "periodType": "REGULAR", "score": 0},
            ],
        },
        "gameLeaders": {
            "homeLeaders": {
                "personId": 0,
                "name": "",
                "jerseyNum": "",
                "position": "",
                "teamTricode": "SAS",
                "playerSlug": None,
                "points": 0,
                "rebounds": 0,
                "assists": 0,
            },
            "awayLeaders": {
                "personId": 0,
                "name": "",
                "jerseyNum": "",
                "position": "",
                "teamTricode": "HOU",
                "playerSlug": None,
                "points": 0,
                "rebounds": 0,
                "assists": 0,
            },
        },
        "pbOdds": {"team": None, "odds": 0.0, "suspended": 1},
    },
]


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


def test_get_score_board_date(nba_http_patch):
    assert scoreboard.ScoreBoard().score_board_date == "2021-01-16"


def test_get_games_dict(nba_http_patch):
    assert scoreboard.ScoreBoard().games.get_dict() == games


def test_get_request_url(nba_http_patch):
    assert (
        scoreboard.ScoreBoard().get_request_url()
        == "https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json"
    )


def test_get_dict(nba_http_patch):
    assert scoreboard.ScoreBoard().get_dict() == content
