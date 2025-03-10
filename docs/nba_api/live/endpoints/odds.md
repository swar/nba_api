# Betting Odds
##### [nba_api/live/nba/endpoints/odds.py](https://github.com/swar/nba_api/blob/master/nba_api/live/nba/endpoints/odds.py)

##### Endpoint URL
>[https://cdn.nba.com/static/json/liveData/odds/odds_todaysGames.json](https://cdn.nba.com/static/json/liveData/odds/odds_todaysGames.json)

## Parameters
API Parameter Name | Python Parameter Variable | Pattern | Required | Nullable
------------ | ------------ | :-----------: | :---: | :---:
proxy | proxy | `None` | `N` | `Y`
headers | headers | `None` | `N` | `Y`
timeout | timeout | `^\d+$` | `N` | `Y`
get_request | get_request | `^(true\|false)$` | `N` | `N`

## Data Sets
#### Games `games`
```text
["gameId", "sr_id", "srMatchId", "homeTeamId", "awayTeamId", "markets"]
```

#### Markets `markets`
```text
["name", "odds_type_id", "group_name", "books"]
```

#### Books `books`
```text
["id", "name", "outcomes", "url", "countryCode"]
```

#### Outcomes `outcomes`
```text
["odds_field_id", "type", "odds", "opening_odds", "odds_trend", "spread", "opening_spread"]
```

## About Data Sets
Key | Description | Type | Example
------------ | ------------ | ------------ | ------------
`gameId` | NBA game ID | `string` | `"0022400913"`
`sr_id` | Sports Radar ID | `string` | `"sr:match:52632103"`
`srMatchId` | Sports Radar Match ID | `string` | `"52632103"`
`homeTeamId` | NBA team ID for home team | `string` | `"1610612745"`
`awayTeamId` | NBA team ID for away team | `string` | `"1610612740"`
`name` | Market type name | `string` | `"2way"`, `"spread"`
`odds_type_id` | Market type identifier | `integer` | `1`, `4`
`group_name` | Market grouping | `string` | `"regular"`
`id` | Sportsbook identifier | `string` | `"sr:book:108"`
`countryCode` | Sportsbook country code | `string` | `"US"`, `"AUS"`
`odds_field_id` | Outcome identifier | `integer` | `1`, `2`, `10`, `12`
`type` | Bet type | `string` | `"home"`, `"away"`
`odds` | Current odds | `string` | `"1.370"`
`opening_odds` | Opening odds | `string` | `"1.360"`
`odds_trend` | Odds movement direction | `string` | `"up"`, `"down"`
`spread` | Point spread (spread markets only) | `string/null` | `"-6.5"`
`opening_spread` | Opening spread (spread markets only) | `number/null` | `-7.5`

> Note: The NBA's Game ID, i.e. 0022400913, is a 10-digit code:
```
GameID Structure (10 digits)
┌─────────────────────┐
│ XX │ X │ XX │ XXXXX │
└─────────────────────┘
 ▲    ▲    ▲    ▲
 │    │    │    │
 │    │    │    └── Game Number (00001-99999)
 │    │    │
 │    │    └── Season (24 = 2024-25)
 │    │
 │    └── Season Type
 │        1: Pre-Season
 │        2: Regular Season
 │        3: All-Star
 │        4: Playoffs
 │        5: Play-In
 │        6: In-Season Tournament
 │
 └── League ID
     00: National Basketball Association (NBA)
     01: ABA
     10: Women's National Basketball Association (WNBA)
     15: NBA Summer League
     20: NBA G League
     12: NBA 2K League (E-Sports)
     ??: Basketball Africa League (BAL)
```

## JSON
```json
{
    "games": [
        {
            "gameId": "0022400913",
            "sr_id": "sr:match:52632103",
            "srMatchId": "52632103",
            "homeTeamId": "1610612745",
            "awayTeamId": "1610612740",
            "markets": [
                {
                    "name": "2way",
                    "odds_type_id": 1,
                    "group_name": "regular",
                    "books": [
                        {
                            "id": "sr:book:108",
                            "name": "Sportsbet",
                            "outcomes": [
                                {
                                    "odds_field_id": 1,
                                    "type": "home",
                                    "odds": "1.370",
                                    "opening_odds": "1.360",
                                    "odds_trend": "up"
                                },
                                {
                                    "odds_field_id": 2,
                                    "type": "away",
                                    "odds": "3.220",
                                    "opening_odds": "3.300",
                                    "odds_trend": "down"
                                }
                            ],
                            "url": "https://sportsbet.com.au",
                            "countryCode": "AUS"
                        }
                    ]
                }
            ]
        }
    ]
}
```

Last validated 2025-03-10