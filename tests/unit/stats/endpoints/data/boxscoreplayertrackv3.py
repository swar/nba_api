"""Test data for boxscoreplayertrackv3 endpoint.

Contains minimal fixture representing API response structure.

Full API response available in:
docs/nba_api/stats/endpoints/responses/boxscoreplayertrackv3.json
"""

BOXSCOREPLAYERTRACKV3_SAMPLE = {
    "meta": {
        "version": 1,
        "request": "http://nba.cloud/games/0022500148/boxscoreplayertrack?Format=json",
        "time": "2025-11-05T17:45:29.4529Z"
    },
    "boxScorePlayerTrack": {
        "gameId": "0022500148",
        "awayTeamId": 1610612740,
        "homeTeamId": 1610612760,
        "homeTeam": {
            "teamId": 1610612760,
            "teamCity": "Oklahoma City",
            "teamName": "Thunder",
            "teamTricode": "OKC",
            "teamSlug": "thunder",
            "players": [
                {
                    "personId": 1630598,
                    "firstName": "Aaron",
                    "familyName": "Wiggins",
                    "nameI": "A. Wiggins",
                    "playerSlug": "aaron-wiggins",
                    "position": "F",
                    "comment": "",
                    "jerseyNum": "21",
                    "statistics": {
                        "minutes": "26:29",
                        "speed": 4.37,
                        "distance": 1.8,
                        "reboundChancesOffensive": 1,
                        "reboundChancesDefensive": 1,
                        "reboundChancesTotal": 2,
                        "touches": 43,
                        "secondaryAssists": 0,
                        "freeThrowAssists": 0,
                        "passes": 30,
                        "assists": 1,
                        "contestedFieldGoalsMade": 3,
                        "contestedFieldGoalsAttempted": 4,
                        "contestedFieldGoalPercentage": 0.75,
                        "uncontestedFieldGoalsMade": 3,
                        "uncontestedFieldGoalsAttempted": 7,
                        "uncontestedFieldGoalsPercentage": 0.429,
                        "fieldGoalPercentage": 0.545,
                        "defendedAtRimFieldGoalsMade": 1,
                        "defendedAtRimFieldGoalsAttempted": 1,
                        "defendedAtRimFieldGoalPercentage": 1.0
                    }
                }
            ],
            "statistics": {
                "minutes": "240:00",
                "distance": 16.45,
                "reboundChancesOffensive": 27,
                "reboundChancesDefensive": 55,
                "reboundChancesTotal": 75,
                "touches": 388,
                "secondaryAssists": 1,
                "freeThrowAssists": 1,
                "passes": 271,
                "assists": 33,
                "contestedFieldGoalsMade": 19,
                "contestedFieldGoalsAttempted": 24,
                "contestedFieldGoalPercentage": 0.792,
                "uncontestedFieldGoalsMade": 28,
                "uncontestedFieldGoalsAttempted": 60,
                "uncontestedFieldGoalsPercentage": 0.467,
                "fieldGoalPercentage": 0.56,
                "defendedAtRimFieldGoalsMade": 11,
                "defendedAtRimFieldGoalsAttempted": 18,
                "defendedAtRimFieldGoalPercentage": 0.611
            }
        },
        "awayTeam": {
            "teamId": 1610612740,
            "teamCity": "New Orleans",
            "teamName": "Pelicans",
            "teamTricode": "NOP",
            "teamSlug": "pelicans",
            "players": [
                {
                    "personId": 1630530,
                    "firstName": "Trey",
                    "familyName": "Murphy III",
                    "nameI": "T. Murphy III",
                    "playerSlug": "trey-murphy-iii",
                    "position": "F",
                    "comment": "",
                    "jerseyNum": "25",
                    "statistics": {
                        "minutes": "32:04",
                        "speed": 4.4,
                        "distance": 2.2,
                        "reboundChancesOffensive": 2,
                        "reboundChancesDefensive": 8,
                        "reboundChancesTotal": 10,
                        "touches": 51,
                        "secondaryAssists": 1,
                        "freeThrowAssists": 0,
                        "passes": 36,
                        "assists": 2,
                        "contestedFieldGoalsMade": 2,
                        "contestedFieldGoalsAttempted": 4,
                        "contestedFieldGoalPercentage": 0.5,
                        "uncontestedFieldGoalsMade": 5,
                        "uncontestedFieldGoalsAttempted": 9,
                        "uncontestedFieldGoalsPercentage": 0.556,
                        "fieldGoalPercentage": 0.538,
                        "defendedAtRimFieldGoalsMade": 3,
                        "defendedAtRimFieldGoalsAttempted": 3,
                        "defendedAtRimFieldGoalPercentage": 1.0
                    }
                }
            ],
            "statistics": {
                "minutes": "240:00",
                "distance": 16.71,
                "reboundChancesOffensive": 26,
                "reboundChancesDefensive": 46,
                "reboundChancesTotal": 70,
                "touches": 413,
                "secondaryAssists": 2,
                "freeThrowAssists": 2,
                "passes": 293,
                "assists": 26,
                "contestedFieldGoalsMade": 16,
                "contestedFieldGoalsAttempted": 36,
                "contestedFieldGoalPercentage": 0.444,
                "uncontestedFieldGoalsMade": 19,
                "uncontestedFieldGoalsAttempted": 44,
                "uncontestedFieldGoalsPercentage": 0.432,
                "fieldGoalPercentage": 0.438,
                "defendedAtRimFieldGoalsMade": 20,
                "defendedAtRimFieldGoalsAttempted": 22,
                "defendedAtRimFieldGoalPercentage": 0.909
            }
        }
    }
}
