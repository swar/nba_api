"""Test data for GravityLeaders endpoint.

Contains sample fixture representing API response structure for gravity tracking data.
Gravity score measures how much defensive attention a player draws.
"""

GRAVITYLEADERS_SAMPLE = {
    "params": {
        "leagueId": "00",
        "seasonType": "Regular Season",
        "seasonYear": "2025-26",
    },
    "leaders": [
        {
            "PLAYERID": 201939,
            "FIRSTNAME": "Stephen",
            "LASTNAME": "Curry",
            "TEAMID": 1610612744,
            "TEAMABBREVIATION": "GSW",
            "TEAMNAME": "Warriors",
            "TEAMCITY": "Golden State",
            "FRAMES": 129230,
            "GRAVITYSCORE": 20.8209629629,
            "AVGGRAVITYSCORE": 20.3848295,
            "ONBALLPERIMETERFRAMES": 34126,
            "ONBALLPERIMETERGRAVITYSCORE": 15.075037037,
            "AVGONBALLPERIMETERGRAVITYSCORE": 15.2041822,
            "OFFBALLPERIMETERFRAMES": 59988,
            "OFFBALLPERIMETERGRAVITYSCORE": 30.0528888888,
            "AVGOFFBALLPERIMETERGRAVITYSCORE": 29.6918001,
            "ONBALLINTERIORFRAMES": 5323,
            "ONBALLINTERIORGRAVITYSCORE": -0.3829259259,
            "AVGONBALLINTERIORGRAVITYSCORE": -2.7228089,
            "OFFBALLINTERIORFRAMES": 29793,
            "OFFBALLINTERIORGRAVITYSCORE": 9.3562592592,
            "AVGOFFBALLINTERIORGRAVITYSCORE": 7.4414369,
            "GAMESPLAYED": 27,
            "MINUTES": 32.1,
            "PTS": 28.7,
            "REB": 3.9,
            "AST": 4.4,
        },
        {
            "PLAYERID": 201142,
            "FIRSTNAME": "Kevin",
            "LASTNAME": "Durant",
            "TEAMID": 1610612756,
            "TEAMABBREVIATION": "PHX",
            "TEAMNAME": "Suns",
            "TEAMCITY": "Phoenix",
            "FRAMES": 194892,
            "GRAVITYSCORE": 16.9147741935,
            "AVGGRAVITYSCORE": 17.1987082,
            "ONBALLPERIMETERFRAMES": 48413,
            "ONBALLPERIMETERGRAVITYSCORE": 16.7305806451,
            "AVGONBALLPERIMETERGRAVITYSCORE": 16.3980093,
            "OFFBALLPERIMETERFRAMES": 108980,
            "OFFBALLPERIMETERGRAVITYSCORE": 17.9372580645,
            "AVGOFFBALLPERIMETERGRAVITYSCORE": 18.1062386,
            "ONBALLINTERIORFRAMES": 12750,
            "ONBALLINTERIORGRAVITYSCORE": 13.7198064516,
            "AVGONBALLINTERIORGRAVITYSCORE": 13.133238,
            "OFFBALLINTERIORFRAMES": 24749,
            "OFFBALLINTERIORGRAVITYSCORE": 14.6121935483,
            "AVGOFFBALLINTERIORGRAVITYSCORE": 15.65223,
            "GAMESPLAYED": 31,
            "MINUTES": 36.2,
            "PTS": 25.7,
            "REB": 5.1,
            "AST": 4.6,
        },
        {
            "PLAYERID": 1629029,
            "FIRSTNAME": "Luka",
            "LASTNAME": "Doncic",
            "TEAMID": 1610612742,
            "TEAMABBREVIATION": "DAL",
            "TEAMNAME": "Mavericks",
            "TEAMCITY": "Dallas",
            "FRAMES": 142000,
            "GRAVITYSCORE": 16.1114615384,
            "AVGGRAVITYSCORE": 16.3204622,
            "ONBALLPERIMETERFRAMES": 59194,
            "ONBALLPERIMETERGRAVITYSCORE": 19.7494230769,
            "AVGONBALLPERIMETERGRAVITYSCORE": 19.920647,
            "OFFBALLPERIMETERFRAMES": 56295,
            "OFFBALLPERIMETERGRAVITYSCORE": 17.7826538461,
            "AVGOFFBALLPERIMETERGRAVITYSCORE": 17.6898707,
            "ONBALLINTERIORFRAMES": 14338,
            "ONBALLINTERIORGRAVITYSCORE": 5.3840384615,
            "AVGONBALLINTERIORGRAVITYSCORE": 5.6644044,
            "OFFBALLINTERIORFRAMES": 12173,
            "OFFBALLINTERIORGRAVITYSCORE": 3.5398461538,
            "AVGOFFBALLINTERIORGRAVITYSCORE": 5.5885452,
            "GAMESPLAYED": 26,
            "MINUTES": 36.5,
            "PTS": 33.7,
            "REB": 8.1,
            "AST": 8.7,
        },
    ],
}

# Edge case fixtures for testing lenient error handling
GRAVITYLEADERS_EMPTY = {"leaders": []}

GRAVITYLEADERS_MISSING_LEADERS = {}

GRAVITYLEADERS_INVALID_LEADERS_TYPE = {"leaders": "not_a_list"}

GRAVITYLEADERS_MIXED_VALID_INVALID = {
    "leaders": [
        {
            "PLAYERID": 12345,
            "FIRSTNAME": "Valid",
            "LASTNAME": "Player",
            "GRAVITYSCORE": 10.5,
        },
        "invalid_string_entry",
        None,
        123,
        {
            "PLAYERID": 67890,
            "FIRSTNAME": "Another",
            "LASTNAME": "Valid",
            "GRAVITYSCORE": 8.2,
        },
    ]
}

GRAVITYLEADERS_PARTIAL_FIELDS = {
    "leaders": [
        {
            "PLAYERID": 11111,
            "FIRSTNAME": "Partial",
            "LASTNAME": "Fields",
            # Missing most fields - should return None for missing
        }
    ]
}
