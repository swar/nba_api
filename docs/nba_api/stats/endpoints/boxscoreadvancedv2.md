# BoxScoreAdvancedV2

##### Endpoint URL
>[https://stats.nba.com/stats/boxscoreadvancedv2](https://stats.nba.com/stats/boxscoreadvancedv2)

##### Valid URL
>[https://stats.nba.com/stats/boxscoreadvancedv2?EndPeriod=1&EndRange=0&GameID=0021700807&RangeType=0&StartPeriod=1&StartRange=0](https://stats.nba.com/stats/boxscoreadvancedv2?EndPeriod=1&EndRange=0&GameID=0021700807&RangeType=0&StartPeriod=1&StartRange=0)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**EndPeriod**_ |  | `Y` |  | 
_**EndRange**_ |  | `Y` |  | 
_**GameID**_ | `^\d{10}$` | `Y` |  | 
_**RangeType**_ |  | `Y` |  | 
_**StartPeriod**_ |  | `Y` |  | 
_**StartRange**_ |  | `Y` |  | 

## Data Sets
#### PlayerStats `player_stats`
```text
['GAME_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_CITY', 'PLAYER_ID', 'PLAYER_NAME', 'START_POSITION', 'COMMENT', 'MIN', 'OFF_RATING', 'DEF_RATING', 'NET_RATING', 'AST_PCT', 'AST_TOV', 'AST_RATIO', 'OREB_PCT', 'DREB_PCT', 'REB_PCT', 'TM_TOV_PCT', 'EFG_PCT', 'TS_PCT', 'USG_PCT', 'PACE', 'PIE']
```

#### TeamStats `team_stats`
```text
['GAME_ID', 'TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'TEAM_CITY', 'MIN', 'OFF_RATING', 'DEF_RATING', 'NET_RATING', 'AST_PCT', 'AST_TOV', 'AST_RATIO', 'OREB_PCT', 'DREB_PCT', 'REB_PCT', 'TM_TOV_PCT', 'EFG_PCT', 'TS_PCT', 'USG_PCT', 'PACE', 'PIE']
```


## JSON
```json
{
    "data_sets": {
        "PlayerStats": [
            "GAME_ID",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_CITY",
            "PLAYER_ID",
            "PLAYER_NAME",
            "START_POSITION",
            "COMMENT",
            "MIN",
            "OFF_RATING",
            "DEF_RATING",
            "NET_RATING",
            "AST_PCT",
            "AST_TOV",
            "AST_RATIO",
            "OREB_PCT",
            "DREB_PCT",
            "REB_PCT",
            "TM_TOV_PCT",
            "EFG_PCT",
            "TS_PCT",
            "USG_PCT",
            "PACE",
            "PIE"
        ],
        "TeamStats": [
            "GAME_ID",
            "TEAM_ID",
            "TEAM_NAME",
            "TEAM_ABBREVIATION",
            "TEAM_CITY",
            "MIN",
            "OFF_RATING",
            "DEF_RATING",
            "NET_RATING",
            "AST_PCT",
            "AST_TOV",
            "AST_RATIO",
            "OREB_PCT",
            "DREB_PCT",
            "REB_PCT",
            "TM_TOV_PCT",
            "EFG_PCT",
            "TS_PCT",
            "USG_PCT",
            "PACE",
            "PIE"
        ]
    },
    "endpoint": "BoxScoreAdvancedV2",
    "nullable_parameters": [],
    "parameter_patterns": {
        "EndPeriod": null,
        "EndRange": null,
        "GameID": "^\\d{10}$",
        "RangeType": null,
        "StartPeriod": null,
        "StartRange": null
    },
    "parameters": [
        "EndPeriod",
        "EndRange",
        "GameID",
        "RangeType",
        "StartPeriod",
        "StartRange"
    ],
    "required_parameters": [
        "EndPeriod",
        "EndRange",
        "GameID",
        "RangeType",
        "StartPeriod",
        "StartRange"
    ],
    "status": "success"
}
```

Last validated 2018-09-16