"""Test data for PlayByPlayV3 endpoint."""

# Minimal test fixture with representative sample
PLAYBYPLAYV3_SAMPLE = {
    "meta": {
        "version": 1,
        "request": "https://stats.nba.com/stats/playbyplayv3?GameID=0022400001",
        "time": "2024-10-22 23:15:42.123"
    },
    "game": {
        "gameId": "0022400001",
        "videoAvailable": 1,
        "actions": [
            {
                "actionNumber": 1,
                "clock": "PT12M00.00S",
                "period": 1,
                "teamId": 1610612739,
                "teamTricode": "CLE",
                "personId": 1629651,
                "playerName": "Evan Mobley",
                "playerNameI": "E. Mobley",
                "xLegacy": 50,
                "yLegacy": 25,
                "shotDistance": 0,
                "shotResult": None,
                "isFieldGoal": 0,
                "scoreHome": "0",
                "scoreAway": "0",
                "pointsTotal": 0,
                "location": "CLE",
                "description": "Jump Ball Mobley vs. Quickley",
                "actionType": "jumpball",
                "subType": "jump-ball",
                "videoAvailable": 1,
                "shotValue": None,
                "actionId": 1
            },
            {
                "actionNumber": 2,
                "clock": "PT11M45.00S",
                "period": 1,
                "teamId": 1610612752,
                "teamTricode": "NYK",
                "personId": 1630163,
                "playerName": "Immanuel Quickley",
                "playerNameI": "I. Quickley",
                "xLegacy": 240,
                "yLegacy": 190,
                "shotDistance": 24,
                "shotResult": "Made",
                "isFieldGoal": 1,
                "scoreHome": "0",
                "scoreAway": "3",
                "pointsTotal": 3,
                "location": "NYK",
                "description": "Quickley 24' 3PT Jump Shot",
                "actionType": "3pt",
                "subType": "jump-shot",
                "videoAvailable": 1,
                "shotValue": 3,
                "actionId": 2
            }
        ]
    }
}

# Test case: missing optional fields
PLAYBYPLAYV3_MINIMAL = {
    "game": {
        "gameId": "0022400999",
        "videoAvailable": 0,
        "actions": [
            {
                "actionNumber": 1,
                "clock": "PT12M00.00S",
                "period": 1,
                "teamId": None,
                "teamTricode": None,
                "personId": None,
                "playerName": None,
                "playerNameI": None,
                "xLegacy": None,
                "yLegacy": None,
                "shotDistance": None,
                "shotResult": None,
                "isFieldGoal": 0,
                "scoreHome": "0",
                "scoreAway": "0",
                "pointsTotal": 0,
                "location": None,
                "description": "Period Start",
                "actionType": "period",
                "subType": "start",
                "videoAvailable": 0,
                "shotValue": None,
                "actionId": 1
            }
        ]
    }
}

# Test case: empty actions (game not started)
PLAYBYPLAYV3_EMPTY = {
    "meta": {"version": 1},
    "game": {
        "gameId": "0022400888",
        "videoAvailable": 0,
        "actions": []
    }
}
