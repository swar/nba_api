# BoxScorePlayerTrackV2
##### [nba_api/stats/endpoints/boxscoreplayertrackv2.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/boxscoreplayertrackv2.py)

##### Endpoint URL
>[https://stats.nba.com/stats/boxscoreplayertrackv2](https://stats.nba.com/stats/boxscoreplayertrackv2)

##### Valid URL
>[https://stats.nba.com/stats/boxscoreplayertrackv2?GameID=0021700807](https://stats.nba.com/stats/boxscoreplayertrackv2?GameID=0021700807)

## Parameters
| API Parameter Name                                                                                          | Python Parameter Variable |  Pattern   | Required | Nullable |
|-------------------------------------------------------------------------------------------------------------|---------------------------|:----------:|:--------:|:--------:|
| [_**GameID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameID) | game_id                   | `^\d{10}$` |   `Y`    |          | 

## Data Sets
#### PlayerStats `player_stats`
```text
['GAME_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_CITY', 'PLAYER_ID', 'PLAYER_NAME', 'START_POSITION', 'COMMENT', 'MIN', 'SPD', 'DIST', 'ORBC', 'DRBC', 'RBC', 'TCHS', 'SAST', 'FTAST', 'PASS', 'AST', 'CFGM', 'CFGA', 'CFG_PCT', 'UFGM', 'UFGA', 'UFG_PCT', 'FG_PCT', 'DFGM', 'DFGA', 'DFG_PCT']
```

#### TeamStats `team_stats`
```text
['GAME_ID', 'TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'TEAM_CITY', 'MIN', 'DIST', 'ORBC', 'DRBC', 'RBC', 'TCHS', 'SAST', 'FTAST', 'PASS', 'AST', 'CFGM', 'CFGA', 'CFG_PCT', 'UFGM', 'UFGA', 'UFG_PCT', 'FG_PCT', 'DFGM', 'DFGA', 'DFG_PCT']
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
            "SPD",
            "DIST",
            "ORBC",
            "DRBC",
            "RBC",
            "TCHS",
            "SAST",
            "FTAST",
            "PASS",
            "AST",
            "CFGM",
            "CFGA",
            "CFG_PCT",
            "UFGM",
            "UFGA",
            "UFG_PCT",
            "FG_PCT",
            "DFGM",
            "DFGA",
            "DFG_PCT"
        ],
        "TeamStats": [
            "GAME_ID",
            "TEAM_ID",
            "TEAM_NAME",
            "TEAM_ABBREVIATION",
            "TEAM_CITY",
            "MIN",
            "DIST",
            "ORBC",
            "DRBC",
            "RBC",
            "TCHS",
            "SAST",
            "FTAST",
            "PASS",
            "AST",
            "CFGM",
            "CFGA",
            "CFG_PCT",
            "UFGM",
            "UFGA",
            "UFG_PCT",
            "FG_PCT",
            "DFGM",
            "DFGA",
            "DFG_PCT"
        ]
    },
    "endpoint": "BoxScorePlayerTrackV2",
    "last_validated_date": "2020-08-15",
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

Last validated 2020-08-16