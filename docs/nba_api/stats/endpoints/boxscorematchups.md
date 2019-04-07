# BoxScoreMatchups
##### [nba_api/stats/endpoints/boxscorematchups.py](https://github.com/swar/nba_api/blob/master/nba_api/stats/endpoints/boxscorematchups.py)

##### Endpoint URL
>[https://stats.nba.com/stats/boxscorematchups](https://stats.nba.com/stats/boxscorematchups)

##### Valid URL
>[https://stats.nba.com/stats/boxscorematchups?GameID=0021700807](https://stats.nba.com/stats/boxscorematchups?GameID=0021700807)

## Parameters
API Parameter Name | Python Parameter Variable | Pattern | Required | Nullable
------------ | ------------ | :-----------: | :---: | :---:
[_**GameID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameID) | game_id | `^\d{10}$` | `Y` |  | 

## Data Sets
#### PlayerMatchupsStats `player_matchups_stats`
```text
['GAME_ID', 'OFF_TEAM_ID', 'OFF_TEAM_ABBREVIATION', 'OFF_TEAM_CITY', 'OFF_TEAM_NICKNAME', 'OFF_PLAYER_ID', 'OFF_PLAYER_NAME', 'DEF_TEAM_ID', 'DEF_TEAM_ABBREVIATION', 'DEF_TEAM_CITY', 'DEF_TEAM_NICKNAME', 'DEF_PLAYER_ID', 'DEF_PLAYER_NAME', 'POSS', 'OFF_MATCHUP_PCT', 'PLAYER_PTS', 'TEAM_PTS', 'AST', 'TOV', 'BLK', 'HELP_BLK', 'HELP_BLK_REC', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'SFL', 'DEF_FOULS', 'OFF_FOULS']
```


## JSON
```json
{
    "data_sets": {
        "PlayerMatchupsStats": [
            "GAME_ID",
            "OFF_TEAM_ID",
            "OFF_TEAM_ABBREVIATION",
            "OFF_TEAM_CITY",
            "OFF_TEAM_NICKNAME",
            "OFF_PLAYER_ID",
            "OFF_PLAYER_NAME",
            "DEF_TEAM_ID",
            "DEF_TEAM_ABBREVIATION",
            "DEF_TEAM_CITY",
            "DEF_TEAM_NICKNAME",
            "DEF_PLAYER_ID",
            "DEF_PLAYER_NAME",
            "POSS",
            "OFF_MATCHUP_PCT",
            "PLAYER_PTS",
            "TEAM_PTS",
            "AST",
            "TOV",
            "BLK",
            "HELP_BLK",
            "HELP_BLK_REC",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "SFL",
            "DEF_FOULS",
            "OFF_FOULS"
        ]
    },
    "endpoint": "BoxScoreMatchups",
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