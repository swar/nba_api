"""Test data for TeamDashLineups endpoint.

Contains minimal fixture representing API response structure.

Full API response available in:
docs/nba_api/stats/endpoints/responses/teamdashlineups.json
"""

TEAMDASHLINEUPS_SAMPLE = {
    "resource": "teamdashlineups",
    "parameters": {
        "TeamID": 1610612739,
        "Season": "2024-25",
        "SeasonType": "Regular Season",
        "GroupQuantity": 5,
        "MeasureType": "Base",
        "PerMode": "Totals",
        "PlusMinus": "N",
        "PaceAdjust": "N",
        "Rank": "N",
        "LastNGames": 0,
        "Month": 0,
        "OpponentTeamID": 0,
        "Period": 0,
        "LeagueID": "00",
    },
    "resultSets": [
        {
            "name": "Lineups",
            "headers": [
                "GROUP_SET",
                "GROUP_ID",
                "GROUP_NAME",
                "GP",
                "W",
                "L",
                "W_PCT",
                "MIN",
                "FGM",
                "FGA",
                "FG_PCT",
            ],
            "rowSet": [
                [
                    "5 Man",
                    123456,
                    "Player1 - Player2 - Player3 - Player4 - Player5",
                    10,
                    7,
                    3,
                    0.700,
                    150.5,
                    55,
                    120,
                    0.458,
                ]
            ],
        },
        {
            "name": "Overall",
            "headers": [
                "GROUP_SET",
                "GROUP_VALUE",
                "TEAM_ID",
                "TEAM_ABBREVIATION",
                "TEAM_NAME",
                "GP",
                "W",
                "L",
                "W_PCT",
            ],
            "rowSet": [
                [
                    "Overall",
                    "Overall",
                    1610612739,
                    "CLE",
                    "Cleveland Cavaliers",
                    82,
                    50,
                    32,
                    0.610,
                ]
            ],
        },
    ],
}
