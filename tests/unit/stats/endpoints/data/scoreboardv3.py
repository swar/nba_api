"""Test data for ScoreboardV3 endpoint."""

SCOREBOARDV3_SAMPLE = {
    "meta": {
        "version": 1,
        "request": "http://nba.cloud/league/00/2025/11/05/scoreboard?Format=json",
        "time": "2025-11-06T12:00:34.034Z",
    },
    "scoreboard": {
        "gameDate": "2025-11-05",
        "leagueId": "00",
        "leagueName": "National Basketball Association",
        "games": [
            {
                "gameId": "0022500171",
                "gameCode": "20251105/PHICLE",
                "gameStatus": 3,
                "gameStatusText": "Final",
                "period": 4,
                "gameClock": "",
                "gameTimeUTC": "2025-11-06T00:00:00Z",
                "gameEt": "2025-11-05T19:00:00Z",
                "regulationPeriods": 4,
                "seriesGameNumber": "",
                "gameLabel": "",
                "gameSubLabel": "",
                "seriesText": "",
                "ifNecessary": False,
                "seriesConference": "",
                "poRoundDesc": "",
                "gameSubtype": "",
                "isNeutral": False,
                "gameLeaders": {
                    "homeLeaders": {
                        "personId": 1628378,
                        "name": "Donovan Mitchell",
                        "playerSlug": "donovan-mitchell",
                        "jerseyNum": "45",
                        "position": "G",
                        "teamTricode": "CLE",
                        "points": 46,
                        "rebounds": 4,
                        "assists": 8,
                    },
                    "awayLeaders": {
                        "personId": 1630178,
                        "name": "Tyrese Maxey",
                        "playerSlug": "tyrese-maxey",
                        "jerseyNum": "0",
                        "position": "G",
                        "teamTricode": "PHI",
                        "points": 27,
                        "rebounds": 7,
                        "assists": 9,
                    },
                },
                "teamLeaders": {
                    "homeLeaders": {
                        "personId": 1628378,
                        "name": "Donovan Mitchell",
                        "playerSlug": "donovan-mitchell",
                        "jerseyNum": "45",
                        "position": "G",
                        "teamTricode": "CLE",
                        "points": 31.9,
                        "rebounds": 2.6,
                        "assists": 5.0,
                    },
                    "awayLeaders": {
                        "personId": 1630178,
                        "name": "Tyrese Maxey",
                        "playerSlug": "tyrese-maxey",
                        "jerseyNum": "0",
                        "position": "G",
                        "teamTricode": "PHI",
                        "points": 33.5,
                        "rebounds": 5.1,
                        "assists": 8.5,
                    },
                    "seasonLeadersFlag": 0,
                },
                "broadcasters": {
                    "nationalBroadcasters": [
                        {
                            "broadcasterId": 2,
                            "broadcastDisplay": "ESPN",
                            "broadcasterTeamId": -1,
                            "broadcasterDescription": "",
                        }
                    ],
                    "nationalRadioBroadcasters": [],
                    "nationalOttBroadcasters": [],
                    "homeTvBroadcasters": [
                        {
                            "broadcasterId": 1001329,
                            "broadcastDisplay": "FDSNOH/RESN",
                            "broadcasterTeamId": 1610612739,
                            "broadcasterDescription": "",
                        }
                    ],
                    "homeRadioBroadcasters": [
                        {
                            "broadcasterId": 1001554,
                            "broadcastDisplay": "WTAM/WMMS/WJMO",
                            "broadcasterTeamId": 1610612739,
                            "broadcasterDescription": "",
                        }
                    ],
                    "homeOttBroadcasters": [],
                    "awayTvBroadcasters": [
                        {
                            "broadcasterId": 133,
                            "broadcastDisplay": "NBCSP",
                            "broadcasterTeamId": 1610612755,
                            "broadcasterDescription": "",
                        }
                    ],
                    "awayRadioBroadcasters": [
                        {
                            "broadcasterId": 1434,
                            "broadcastDisplay": "WPEN",
                            "broadcasterTeamId": 1610612755,
                            "broadcasterDescription": "",
                        }
                    ],
                    "awayOttBroadcasters": [],
                },
                "homeTeam": {
                    "teamId": 1610612739,
                    "teamName": "Cavaliers",
                    "teamCity": "Cleveland",
                    "teamTricode": "CLE",
                    "teamSlug": "cavaliers",
                    "wins": 9,
                    "losses": 0,
                    "score": 114,
                    "seed": 0,
                    "inBonus": None,
                    "timeoutsRemaining": 1,
                    "periods": [
                        {"period": 1, "periodType": "REGULAR", "score": 35},
                        {"period": 2, "periodType": "REGULAR", "score": 27},
                        {"period": 3, "periodType": "REGULAR", "score": 28},
                        {"period": 4, "periodType": "REGULAR", "score": 24},
                    ],
                },
                "awayTeam": {
                    "teamId": 1610612755,
                    "teamName": "76ers",
                    "teamCity": "Philadelphia",
                    "teamTricode": "PHI",
                    "teamSlug": "76ers",
                    "wins": 2,
                    "losses": 7,
                    "score": 106,
                    "seed": 0,
                    "inBonus": None,
                    "timeoutsRemaining": 2,
                    "periods": [
                        {"period": 1, "periodType": "REGULAR", "score": 24},
                        {"period": 2, "periodType": "REGULAR", "score": 27},
                        {"period": 3, "periodType": "REGULAR", "score": 25},
                        {"period": 4, "periodType": "REGULAR", "score": 30},
                    ],
                },
            }
        ],
    },
}
