import pytest
import json
from nba_api.library.http import NBAHTTP, NBAResponse
from nba_api.live.nba.endpoints import boxscore
from nba_api.live.nba.library.http import NBALiveHTTP

content = {
    "meta": {
        "version": 1,
        "code": 200,
        "request": "http://nba.cloud/games/0022000180/boxscore?Format=json",
        "time": "2021-01-15 23:51:25.282704",
    },
    "game": {
        "gameId": "0022000180",
        "gameTimeLocal": "2021-01-15T19:30:00-05:00",
        "gameTimeUTC": "2021-01-16T00:30:00Z",
        "gameTimeHome": "2021-01-15T19:30:00-05:00",
        "gameTimeAway": "2021-01-15T19:30:00-05:00",
        "gameEt": "2021-01-15T19:30:00-05:00",
        "duration": 125,
        "gameCode": "20210115/ORLBOS",
        "gameStatusText": "Final",
        "gameStatus": 3,
        "regulationPeriods": 4,
        "period": 4,
        "gameClock": "PT00M00.00S",
        "attendance": 0,
        "sellout": "0",
        "arena": {
            "arenaId": 17,
            "arenaName": "TD Garden",
            "arenaCity": "Boston",
            "arenaState": "MA",
            "arenaCountry": "US",
            "arenaTimezone": "America/New_York",
        },
        "officials": [
            {
                "personId": 201638,
                "name": "Brent Barnaky",
                "nameI": "B. Barnaky",
                "firstName": "Brent",
                "familyName": "Barnaky",
                "jerseyNum": "36",
                "assignment": "OFFICIAL1",
            }
        ],
        "homeTeam": {
            "teamId": 1610612738,
            "teamName": "Celtics",
            "teamCity": "Boston",
            "teamTricode": "BOS",
            "score": 124,
            "inBonus": "1",
            "timeoutsRemaining": 2,
            "periods": [{"period": 1, "periodType": "REGULAR", "score": 34}],
            "players": [
                {
                    "status": "ACTIVE",
                    "order": 1,
                    "personId": 1627759,
                    "jerseyNum": "7",
                    "position": "SF",
                    "starter": "1",
                    "oncourt": "0",
                    "played": "1",
                    "statistics": {
                        "assists": 8,
                        "blocks": 0,
                        "blocksReceived": 0,
                        "fieldGoalsAttempted": 12,
                        "fieldGoalsMade": 6,
                        "fieldGoalsPercentage": 0.5,
                        "foulsOffensive": 0,
                        "foulsDrawn": 4,
                        "foulsPersonal": 1,
                        "foulsTechnical": 0,
                        "freeThrowsAttempted": 7,
                        "freeThrowsMade": 7,
                        "freeThrowsPercentage": 1.0,
                        "minus": 50.0,
                        "minutes": "PT25M01.00S",
                        "minutesCalculated": "PT25M",
                        "plus": 65.0,
                        "plusMinusPoints": 15.0,
                        "points": 21,
                        "pointsFastBreak": 0,
                        "pointsInThePaint": 6,
                        "pointsSecondChance": 0,
                        "reboundsDefensive": 2,
                        "reboundsOffensive": 0,
                        "reboundsTotal": 2,
                        "steals": 1,
                        "threePointersAttempted": 5,
                        "threePointersMade": 2,
                        "threePointersPercentage": 0.4,
                        "turnovers": 2,
                        "twoPointersAttempted": 7,
                        "twoPointersMade": 4,
                        "twoPointersPercentage": 0.5714285714285711,
                    },
                    "name": "Jaylen Brown",
                    "nameI": "J. Brown",
                    "firstName": "Jaylen",
                    "familyName": "Brown",
                }
            ],
            "statistics": {
                "assists": 25,
                "assistsTurnoverRatio": 2.27272727272727,
                "benchPoints": 66,
                "biggestLead": 29,
                "biggestLeadScore": "72-101",
                "biggestScoringRun": 13,
                "biggestScoringRunScore": "72-101",
                "blocks": 4,
                "blocksReceived": 1,
                "fastBreakPointsAttempted": 9,
                "fastBreakPointsMade": 5,
                "fastBreakPointsPercentage": 0.555555555555556,
                "fieldGoalsAttempted": 88,
                "fieldGoalsEffectiveAdjusted": 0.607954545454545,
                "fieldGoalsMade": 45,
                "fieldGoalsPercentage": 0.511363636363636,
                "foulsOffensive": 0,
                "foulsDrawn": 16,
                "foulsPersonal": 18,
                "foulsTeam": 18,
                "foulsTechnical": 0,
                "foulsTeamTechnical": 0,
                "freeThrowsAttempted": 19,
                "freeThrowsMade": 17,
                "freeThrowsPercentage": 0.894736842105263,
                "leadChanges": 4,
                "minutes": "PT240M00.00S",
                "minutesCalculated": "PT240M",
                "points": 124,
                "pointsAgainst": 97,
                "pointsFastBreak": 13,
                "pointsFromTurnovers": 16,
                "pointsInThePaint": 48,
                "pointsInThePaintAttempted": 36,
                "pointsInThePaintMade": 24,
                "pointsInThePaintPercentage": 0.666666666666666,
                "pointsSecondChance": 11,
                "reboundsDefensive": 39,
                "reboundsOffensive": 6,
                "reboundsPersonal": 45,
                "reboundsTeam": 6,
                "reboundsTeamDefensive": 2,
                "reboundsTeamOffensive": 4,
                "reboundsTotal": 51,
                "secondChancePointsAttempted": 6,
                "secondChancePointsMade": 4,
                "secondChancePointsPercentage": 0.666666666666666,
                "steals": 7,
                "threePointersAttempted": 42,
                "threePointersMade": 17,
                "threePointersPercentage": 0.40476190476190504,
                "timeLeading": "PT47M16.00S",
                "timesTied": 0,
                "trueShootingAttempts": 96.36,
                "trueShootingPercentage": 0.6434205064342051,
                "turnovers": 10,
                "turnoversTeam": 1,
                "turnoversTotal": 11,
                "twoPointersAttempted": 46,
                "twoPointersMade": 28,
                "twoPointersPercentage": 0.608695652173913,
            },
        },
        "awayTeam": {
            "teamId": 1610612753,
            "teamName": "Magic",
            "teamCity": "Orlando",
            "teamTricode": "ORL",
            "score": 97,
            "inBonus": "1",
            "timeoutsRemaining": 2,
            "periods": [{"period": 1, "periodType": "REGULAR", "score": 28}],
            "players": [
                {
                    "status": "ACTIVE",
                    "order": 1,
                    "personId": 203516,
                    "jerseyNum": "11",
                    "position": "SF",
                    "starter": "1",
                    "oncourt": "0",
                    "played": "1",
                    "statistics": {
                        "assists": 0,
                        "blocks": 0,
                        "blocksReceived": 0,
                        "fieldGoalsAttempted": 4,
                        "fieldGoalsMade": 1,
                        "fieldGoalsPercentage": 0.25,
                        "foulsOffensive": 0,
                        "foulsDrawn": 0,
                        "foulsPersonal": 3,
                        "foulsTechnical": 0,
                        "freeThrowsAttempted": 0,
                        "freeThrowsMade": 0,
                        "freeThrowsPercentage": 0.0,
                        "minus": 41.0,
                        "minutes": "PT14M34.00S",
                        "minutesCalculated": "PT14M",
                        "plus": 36.0,
                        "plusMinusPoints": -5.0,
                        "points": 2,
                        "pointsFastBreak": 0,
                        "pointsInThePaint": 2,
                        "pointsSecondChance": 0,
                        "reboundsDefensive": 1,
                        "reboundsOffensive": 0,
                        "reboundsTotal": 1,
                        "steals": 0,
                        "threePointersAttempted": 2,
                        "threePointersMade": 0,
                        "threePointersPercentage": 0.0,
                        "turnovers": 0,
                        "twoPointersAttempted": 2,
                        "twoPointersMade": 1,
                        "twoPointersPercentage": 0.5,
                    },
                    "name": "James Ennis III",
                    "nameI": "J. Ennis III",
                    "firstName": "James",
                    "familyName": "Ennis III",
                }
            ],
            "statistics": {
                "assists": 14,
                "assistsTurnoverRatio": 1.07692307692308,
                "benchPoints": 33,
                "biggestLead": 1,
                "biggestLeadScore": "4-3",
                "biggestScoringRun": 13,
                "biggestScoringRunScore": "72-101",
                "blocks": 1,
                "blocksReceived": 4,
                "fastBreakPointsAttempted": 7,
                "fastBreakPointsMade": 2,
                "fastBreakPointsPercentage": 0.28571428571428603,
                "fieldGoalsAttempted": 94,
                "fieldGoalsEffectiveAdjusted": 0.441489361702128,
                "fieldGoalsMade": 38,
                "fieldGoalsPercentage": 0.404255319148936,
                "foulsOffensive": 2,
                "foulsDrawn": 18,
                "foulsPersonal": 16,
                "foulsTeam": 14,
                "foulsTechnical": 1,
                "foulsTeamTechnical": 0,
                "freeThrowsAttempted": 22,
                "freeThrowsMade": 14,
                "freeThrowsPercentage": 0.636363636363636,
                "leadChanges": 4,
                "minutes": "PT240M00.00S",
                "minutesCalculated": "PT240M",
                "points": 97,
                "pointsAgainst": 124,
                "pointsFastBreak": 8,
                "pointsFromTurnovers": 10,
                "pointsInThePaint": 52,
                "pointsInThePaintAttempted": 47,
                "pointsInThePaintMade": 26,
                "pointsInThePaintPercentage": 0.553191489361702,
                "pointsSecondChance": 20,
                "reboundsDefensive": 31,
                "reboundsOffensive": 15,
                "reboundsPersonal": 46,
                "reboundsTeam": 12,
                "reboundsTeamDefensive": 4,
                "reboundsTeamOffensive": 8,
                "reboundsTotal": 58,
                "secondChancePointsAttempted": 16,
                "secondChancePointsMade": 9,
                "secondChancePointsPercentage": 0.5625,
                "steals": 5,
                "threePointersAttempted": 28,
                "threePointersMade": 7,
                "threePointersPercentage": 0.25,
                "timeLeading": "PT00M30.00S",
                "timesTied": 0,
                "trueShootingAttempts": 103.68,
                "trueShootingPercentage": 0.46778549382716,
                "turnovers": 11,
                "turnoversTeam": 2,
                "turnoversTotal": 13,
                "twoPointersAttempted": 66,
                "twoPointersMade": 31,
                "twoPointersPercentage": 0.46969696969696995,
            },
        },
    },
}
game_details = {
    "gameId": "0022000180",
    "gameTimeLocal": "2021-01-15T19:30:00-05:00",
    "gameTimeUTC": "2021-01-16T00:30:00Z",
    "gameTimeHome": "2021-01-15T19:30:00-05:00",
    "gameTimeAway": "2021-01-15T19:30:00-05:00",
    "gameEt": "2021-01-15T19:30:00-05:00",
    "duration": 125,
    "gameCode": "20210115/ORLBOS",
    "gameStatusText": "Final",
    "gameStatus": 3,
    "regulationPeriods": 4,
    "period": 4,
    "gameClock": "PT00M00.00S",
    "attendance": 0,
    "sellout": "0",
}
home_team_stats = {
    "teamId": 1610612738,
    "teamName": "Celtics",
    "teamCity": "Boston",
    "teamTricode": "BOS",
    "score": 124,
    "inBonus": "1",
    "timeoutsRemaining": 2,
    "periods": [{"period": 1, "periodType": "REGULAR", "score": 34}],
    "statistics": {
        "assists": 25,
        "assistsTurnoverRatio": 2.27272727272727,
        "benchPoints": 66,
        "biggestLead": 29,
        "biggestLeadScore": "72-101",
        "biggestScoringRun": 13,
        "biggestScoringRunScore": "72-101",
        "blocks": 4,
        "blocksReceived": 1,
        "fastBreakPointsAttempted": 9,
        "fastBreakPointsMade": 5,
        "fastBreakPointsPercentage": 0.555555555555556,
        "fieldGoalsAttempted": 88,
        "fieldGoalsEffectiveAdjusted": 0.607954545454545,
        "fieldGoalsMade": 45,
        "fieldGoalsPercentage": 0.511363636363636,
        "foulsOffensive": 0,
        "foulsDrawn": 16,
        "foulsPersonal": 18,
        "foulsTeam": 18,
        "foulsTechnical": 0,
        "foulsTeamTechnical": 0,
        "freeThrowsAttempted": 19,
        "freeThrowsMade": 17,
        "freeThrowsPercentage": 0.894736842105263,
        "leadChanges": 4,
        "minutes": "PT240M00.00S",
        "minutesCalculated": "PT240M",
        "points": 124,
        "pointsAgainst": 97,
        "pointsFastBreak": 13,
        "pointsFromTurnovers": 16,
        "pointsInThePaint": 48,
        "pointsInThePaintAttempted": 36,
        "pointsInThePaintMade": 24,
        "pointsInThePaintPercentage": 0.666666666666666,
        "pointsSecondChance": 11,
        "reboundsDefensive": 39,
        "reboundsOffensive": 6,
        "reboundsPersonal": 45,
        "reboundsTeam": 6,
        "reboundsTeamDefensive": 2,
        "reboundsTeamOffensive": 4,
        "reboundsTotal": 51,
        "secondChancePointsAttempted": 6,
        "secondChancePointsMade": 4,
        "secondChancePointsPercentage": 0.666666666666666,
        "steals": 7,
        "threePointersAttempted": 42,
        "threePointersMade": 17,
        "threePointersPercentage": 0.40476190476190504,
        "timeLeading": "PT47M16.00S",
        "timesTied": 0,
        "trueShootingAttempts": 96.36,
        "trueShootingPercentage": 0.6434205064342051,
        "turnovers": 10,
        "turnoversTeam": 1,
        "turnoversTotal": 11,
        "twoPointersAttempted": 46,
        "twoPointersMade": 28,
        "twoPointersPercentage": 0.608695652173913,
    },
}
away_team_stats = {
    "teamId": 1610612753,
    "teamName": "Magic",
    "teamCity": "Orlando",
    "teamTricode": "ORL",
    "score": 97,
    "inBonus": "1",
    "timeoutsRemaining": 2,
    "periods": [{"period": 1, "periodType": "REGULAR", "score": 28}],
    "statistics": {
        "assists": 14,
        "assistsTurnoverRatio": 1.07692307692308,
        "benchPoints": 33,
        "biggestLead": 1,
        "biggestLeadScore": "4-3",
        "biggestScoringRun": 13,
        "biggestScoringRunScore": "72-101",
        "blocks": 1,
        "blocksReceived": 4,
        "fastBreakPointsAttempted": 7,
        "fastBreakPointsMade": 2,
        "fastBreakPointsPercentage": 0.28571428571428603,
        "fieldGoalsAttempted": 94,
        "fieldGoalsEffectiveAdjusted": 0.441489361702128,
        "fieldGoalsMade": 38,
        "fieldGoalsPercentage": 0.404255319148936,
        "foulsOffensive": 2,
        "foulsDrawn": 18,
        "foulsPersonal": 16,
        "foulsTeam": 14,
        "foulsTechnical": 1,
        "foulsTeamTechnical": 0,
        "freeThrowsAttempted": 22,
        "freeThrowsMade": 14,
        "freeThrowsPercentage": 0.636363636363636,
        "leadChanges": 4,
        "minutes": "PT240M00.00S",
        "minutesCalculated": "PT240M",
        "points": 97,
        "pointsAgainst": 124,
        "pointsFastBreak": 8,
        "pointsFromTurnovers": 10,
        "pointsInThePaint": 52,
        "pointsInThePaintAttempted": 47,
        "pointsInThePaintMade": 26,
        "pointsInThePaintPercentage": 0.553191489361702,
        "pointsSecondChance": 20,
        "reboundsDefensive": 31,
        "reboundsOffensive": 15,
        "reboundsPersonal": 46,
        "reboundsTeam": 12,
        "reboundsTeamDefensive": 4,
        "reboundsTeamOffensive": 8,
        "reboundsTotal": 58,
        "secondChancePointsAttempted": 16,
        "secondChancePointsMade": 9,
        "secondChancePointsPercentage": 0.5625,
        "steals": 5,
        "threePointersAttempted": 28,
        "threePointersMade": 7,
        "threePointersPercentage": 0.25,
        "timeLeading": "PT00M30.00S",
        "timesTied": 0,
        "trueShootingAttempts": 103.68,
        "trueShootingPercentage": 0.46778549382716,
        "turnovers": 11,
        "turnoversTeam": 2,
        "turnoversTotal": 13,
        "twoPointersAttempted": 66,
        "twoPointersMade": 31,
        "twoPointersPercentage": 0.46969696969696995,
    },
}
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


def test_get_request_url():
    assert (
        boxscore.BoxScore(game_id).get_request_url()
        == "https://cdn.nba.com/static/json/liveData/boxscore/boxscore_0022000180.json"
    )


def test_get_response(nba_http_patch):
    assert json.dumps(content) == boxscore.BoxScore(game_id).get_response()


def test_get_dict(nba_http_patch):
    assert boxscore.BoxScore(game_id).get_dict() == content


def test_game_dict(nba_http_patch):
    assert boxscore.BoxScore(game_id).game.get_dict() == content["game"]


def test_arena_dict(nba_http_patch):
    assert boxscore.BoxScore(game_id).arena.get_dict() == content["game"]["arena"]


def test_home_team_dict(nba_http_patch):
    assert (
        boxscore.BoxScore(game_id).home_team.get_dict() == content["game"]["homeTeam"]
    )


def test_home_team_stats(nba_http_patch):
    assert boxscore.BoxScore(game_id).home_team_stats.get_dict() == home_team_stats


def test_home_team_player_stats(nba_http_patch):
    assert (
        boxscore.BoxScore(game_id).home_team_player_stats.get_dict()
        == content["game"]["homeTeam"]["players"]
    )


def test_away_team_dict(nba_http_patch):
    assert (
        boxscore.BoxScore(game_id).away_team.get_dict() == content["game"]["awayTeam"]
    )


def test_away_team_stats(nba_http_patch):
    assert boxscore.BoxScore(game_id).away_team_stats.get_dict() == away_team_stats


def test_away_team_player_stats(nba_http_patch):
    assert (
        boxscore.BoxScore(game_id).away_team_player_stats.get_dict()
        == content["game"]["awayTeam"]["players"]
    )


def test_officials_dict(nba_http_patch):
    assert (
        boxscore.BoxScore(game_id).officials.get_dict() == content["game"]["officials"]
    )


def test_game_details_dict(nba_http_patch):
    assert boxscore.BoxScore(game_id).game_details.get_dict() == game_details
