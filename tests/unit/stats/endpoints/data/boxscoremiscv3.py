"""Test data for boxscoremiscv3 endpoint.

Contains minimal fixture representing API response structure.

Full API response available in:
docs/nba_api/stats/endpoints/responses/boxscoremiscv3.json
"""

BOXSCOREMISCV3_SAMPLE = {
    "meta": {
        "version": 1,
        "request": "http://nba.cloud/games/0022500148/boxscoremisc?Format=json",
        "time": "2025-11-05T20:02:52.252Z"
    },
    "boxScoreMisc": {
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
                    "personId": 1628983,
                    "firstName": "Shai",
                    "familyName": "Gilgeous-Alexander",
                    "nameI": "S. Gilgeous-Alexander",
                    "playerSlug": "shai-gilgeous-alexander",
                    "position": "G",
                    "comment": "",
                    "jerseyNum": "2",
                    "statistics": {
                        "minutes": "29:59",
                        "pointsOffTurnovers": 6,
                        "pointsSecondChance": 2,
                        "pointsFastBreak": 2,
                        "pointsPaint": 10,
                        "oppPointsOffTurnovers": 11,
                        "oppPointsSecondChance": 8,
                        "oppPointsFastBreak": 8,
                        "oppPointsPaint": 24,
                        "blocks": 0,
                        "blocksAgainst": 2,
                        "foulsPersonal": 1,
                        "foulsDrawn": 8
                    }
                }
            ],
            "statistics": {
                "minutes": "240:00",
                "pointsOffTurnovers": 25,
                "pointsSecondChance": 17,
                "pointsFastBreak": 18,
                "pointsPaint": 48,
                "oppPointsOffTurnovers": 21,
                "oppPointsSecondChance": 8,
                "oppPointsFastBreak": 10,
                "oppPointsPaint": 38,
                "blocks": 5,
                "blocksAgainst": 3,
                "foulsPersonal": 22,
                "foulsDrawn": 22
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
                    "personId": 1629627,
                    "firstName": "Zion",
                    "familyName": "Williamson",
                    "nameI": "Z. Williamson",
                    "playerSlug": "zion-williamson",
                    "position": "F",
                    "comment": "",
                    "jerseyNum": "1",
                    "statistics": {
                        "minutes": "28:03",
                        "pointsOffTurnovers": 4,
                        "pointsSecondChance": 1,
                        "pointsFastBreak": 3,
                        "pointsPaint": 14,
                        "oppPointsOffTurnovers": 14,
                        "oppPointsSecondChance": 15,
                        "oppPointsFastBreak": 12,
                        "oppPointsPaint": 28,
                        "blocks": 0,
                        "blocksAgainst": 1,
                        "foulsPersonal": 3,
                        "foulsDrawn": 9
                    }
                }
            ],
            "statistics": {
                "minutes": "240:00",
                "pointsOffTurnovers": 21,
                "pointsSecondChance": 8,
                "pointsFastBreak": 10,
                "pointsPaint": 38,
                "oppPointsOffTurnovers": 25,
                "oppPointsSecondChance": 17,
                "oppPointsFastBreak": 18,
                "oppPointsPaint": 48,
                "blocks": 3,
                "blocksAgainst": 5,
                "foulsPersonal": 22,
                "foulsDrawn": 22
            }
        }
    }
}
