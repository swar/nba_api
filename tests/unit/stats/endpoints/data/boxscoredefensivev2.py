"""Test data for boxscoredefensivev2 endpoint.

Contains minimal fixture representing API response structure.

Full API response available in:
docs/nba_api/stats/endpoints/responses/boxscoredefensivev2.json
"""

BOXSCOREDEFENSIVEV2_SAMPLE = {
    "meta": {"version": 1, "request": "", "time": ""},
    "boxScoreDefensive": {
        "gameId": "1022500165",
        "awayTeamId": 1611661328,
        "homeTeamId": 1611661323,
        "homeTeam": {
            "teamId": 1611661323,
            "teamCity": "Connecticut",
            "teamName": "Sun",
            "teamTricode": "CON",
            "teamSlug": "sun",
            "players": [
                {
                    "personId": 1642809,
                    "firstName": "Saniya",
                    "familyName": "Rivers",
                    "nameI": "S. Rivers",
                    "playerSlug": "saniya-rivers",
                    "position": "F",
                    "comment": "",
                    "jerseyNum": "",
                    "statistics": {
                        "matchupMinutes": "4:36",
                        "partialPossessions": 26.3,
                        "switchesOn": 0,
                        "playerPoints": 5,
                        "defensiveRebounds": 0,
                        "matchupAssists": 1,
                        "matchupTurnovers": 0,
                        "steals": 0,
                        "blocks": 0,
                        "matchupFieldGoalsMade": 2,
                        "matchupFieldGoalsAttempted": 5,
                        "matchupFieldGoalPercentage": 0.4,
                        "matchupThreePointersMade": 1,
                        "matchupThreePointersAttempted": 2,
                        "matchupThreePointerPercentage": 0.5,
                    },
                }
            ],
            "statistics": {"minutes": None},
        },
        "awayTeam": {
            "teamId": 1611661328,
            "teamCity": "Seattle",
            "teamName": "Storm",
            "teamTricode": "SEA",
            "teamSlug": "storm",
            "players": [
                {
                    "personId": 1628931,
                    "firstName": "Gabby",
                    "familyName": "Williams",
                    "nameI": "G. Williams",
                    "playerSlug": "gabby-williams",
                    "position": "F",
                    "comment": "",
                    "jerseyNum": "",
                    "statistics": {
                        "matchupMinutes": "7:13",
                        "partialPossessions": 40.6,
                        "switchesOn": 0,
                        "playerPoints": 20,
                        "defensiveRebounds": 1,
                        "matchupAssists": 3,
                        "matchupTurnovers": 1,
                        "steals": 0,
                        "blocks": 1,
                        "matchupFieldGoalsMade": 9,
                        "matchupFieldGoalsAttempted": 13,
                        "matchupFieldGoalPercentage": 0.692,
                        "matchupThreePointersMade": 2,
                        "matchupThreePointersAttempted": 4,
                        "matchupThreePointerPercentage": 0.5,
                    },
                }
            ],
            "statistics": {"minutes": None},
        },
    },
}
