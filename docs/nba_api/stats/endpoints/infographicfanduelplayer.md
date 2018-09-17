# InfographicFanDuelPlayer

##### Endpoint URL
>[https://stats.nba.com/stats/infographicfanduelplayer](https://stats.nba.com/stats/infographicfanduelplayer)

##### Valid URL
>[https://stats.nba.com/stats/infographicfanduelplayer?GameID=0021700807](https://stats.nba.com/stats/infographicfanduelplayer?GameID=0021700807)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**GameID**_ | `^\d{10}$` | `Y` |  | 

## Data Sets
#### FanDuelPlayer `fan_duel_player`
```text
['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'JERSEY_NUM', 'PLAYER_POSITION', 'LOCATION', 'FAN_DUEL_PTS', 'NBA_FANTASY_PTS', 'USG_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS']
```


## JSON
```json
{
    "data_sets": {
        "FanDuelPlayer": [
            "PLAYER_ID",
            "PLAYER_NAME",
            "TEAM_ID",
            "TEAM_NAME",
            "TEAM_ABBREVIATION",
            "JERSEY_NUM",
            "PLAYER_POSITION",
            "LOCATION",
            "FAN_DUEL_PTS",
            "NBA_FANTASY_PTS",
            "USG_PCT",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "TOV",
            "STL",
            "BLK",
            "BLKA",
            "PF",
            "PFD",
            "PTS",
            "PLUS_MINUS"
        ]
    },
    "endpoint": "InfographicFanDuelPlayer",
    "nullable_parameters": [],
    "parameter_patterns": {
        "GameID": "^\\d{10}$"
    },
    "parameters": [
        "GameID"
    ],
    "required_parameters": [
        "GameID"
    ],
    "status": "success"
}
```

Last validated 2018-09-16