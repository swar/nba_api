# BoxScoreDefensive
##### [nba_api/stats/endpoints/boxscoredefensive.py](https://github.com/swar/nba_api/blob/master/nba_api/stats/endpoints/boxscoredefensive.py)

##### Endpoint URL
>[https://stats.nba.com/stats/boxscoredefensive](https://stats.nba.com/stats/boxscoredefensive)

##### Valid URL
>[https://stats.nba.com/stats/boxscoredefensive?GameID=0021700807](https://stats.nba.com/stats/boxscoredefensive?GameID=0021700807)

## Parameters
API Parameter Name | Python Parameter Variable | Pattern | Required | Nullable
------------ | ------------ | :-----------: | :---: | :---:
[_**GameID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameID) | game_id | `^\d{10}$` | `Y` |  | 

## Data Sets
#### PlayerDefensiveStats `player_defensive_stats`
```text
['GAME_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_CITY', 'TEAM_NICKNAME', 'PLAYER_ID', 'PLAYER_NAME', 'START_POSITION', 'COMMENT', 'MIN', 'POSS', 'PLAYER_PTS', 'TEAM_PTS', 'DREB', 'AST', 'TOV', 'STL', 'BLK', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'SFL', 'DEF_FLS', 'CFGM', 'CFGA', 'CFG_PCT', 'CFG3M', 'CFG3A', 'CFG3_PCT']
```


## JSON
```json
{
    "data_sets": {
        "PlayerDefensiveStats": [
            "GAME_ID",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_CITY",
            "TEAM_NICKNAME",
            "PLAYER_ID",
            "PLAYER_NAME",
            "START_POSITION",
            "COMMENT",
            "MIN",
            "POSS",
            "PLAYER_PTS",
            "TEAM_PTS",
            "DREB",
            "AST",
            "TOV",
            "STL",
            "BLK",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "SFL",
            "DEF_FLS",
            "CFGM",
            "CFGA",
            "CFG_PCT",
            "CFG3M",
            "CFG3A",
            "CFG3_PCT"
        ]
    },
    "endpoint": "BoxScoreDefensive",
    "last_validated_date": "2019-04-07",
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

Last validated 2019-04-07