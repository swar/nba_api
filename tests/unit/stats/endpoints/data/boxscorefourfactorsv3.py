"""Test data for boxscorefourfactorsv3 endpoint.

Contains minimal fixture representing API response structure.

Full API response available in:
docs/nba_api/stats/endpoints/responses/boxscorefourfactorsv3.json
"""

BOXSCOREFOURFACTORSV3_SAMPLE = {
    "meta": {"version": 1, "request": "", "time": ""},
    "boxScoreFourFactors": {
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
                        "minutes": "12:46",
                        "effectiveFieldGoalPercentage": 0.341,
                        "freeThrowAttemptRate": 0.136,
                        "teamTurnoverPercentage": 0.239,
                        "offensiveReboundPercentage": 0.0,
                        "oppEffectiveFieldGoalPercentage": 0.667,
                        "oppFreeThrowAttemptRate": 0.083,
                        "oppTeamTurnoverPercentage": 0.077,
                        "oppOffensiveReboundPercentage": 0.111,
                    },
                }
            ],
            "statistics": {
                "minutes": "200:00",
                "effectiveFieldGoalPercentage": 0.463,
                "freeThrowAttemptRate": 0.388,
                "teamTurnoverPercentage": 0.153,
                "offensiveReboundPercentage": 0.186,
                "oppEffectiveFieldGoalPercentage": 0.674,
                "oppFreeThrowAttemptRate": 0.145,
                "oppTeamTurnoverPercentage": 0.198,
                "oppOffensiveReboundPercentage": 0.179,
            },
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
                        "minutes": "24:21",
                        "effectiveFieldGoalPercentage": 0.688,
                        "freeThrowAttemptRate": 0.04,
                        "teamTurnoverPercentage": 0.143,
                        "offensiveReboundPercentage": 0.0,
                        "oppEffectiveFieldGoalPercentage": 0.318,
                        "oppFreeThrowAttemptRate": 0.477,
                        "oppTeamTurnoverPercentage": 0.238,
                        "oppOffensiveReboundPercentage": 0.0,
                    },
                }
            ],
            "statistics": {
                "minutes": "200:00",
                "effectiveFieldGoalPercentage": 0.674,
                "freeThrowAttemptRate": 0.145,
                "teamTurnoverPercentage": 0.198,
                "offensiveReboundPercentage": 0.179,
                "oppEffectiveFieldGoalPercentage": 0.463,
                "oppFreeThrowAttemptRate": 0.388,
                "oppTeamTurnoverPercentage": 0.153,
                "oppOffensiveReboundPercentage": 0.186,
            },
        },
    },
}
