# BoxScoreHustle
##### [nba_api/stats/endpoints/boxscorehustle.py](https://github.com/swar/nba_api/blob/master/nba_api/stats/endpoints/boxscorehustle.py)

##### Endpoint URL
>[https://stats.nba.com/stats/hustlestatsboxscore](https://stats.nba.com/stats/hustlestatsboxscore)

##### Valid URL
>[https://stats.nba.com/stats/hustlestatsboxscore?GameID=0021700807](https://stats.nba.com/stats/boxscoreadvancedv2?EndPeriod=1&EndRange=0&GameID=0021700807&RangeType=0&StartPeriod=1&StartRange=0)

## Parameters
API Parameter Name | Python Parameter Variable | Pattern | Required | Nullable
------------ | ------------ | :-----------: | :---: | :---:
[_**GameID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameID) | game_id | `^\d{10}$` | `Y` |  | 

## Data Sets
#### HustleStatsAvailable `hustle_stats_available`
```text
['GAME_ID', 'HUSTLE_STATUS']
```
#### PlayerStats `player_stats`
```text
['GAME_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_CITY', 'PLAYER_ID', 'PLAYER_NAME', 'START_POSITION', 'COMMENT', 'MINUTES', 'PTS', 'CONTESTED_SHOTS', 'CONTESTED_SHOTS_2PT', 'CONTESTED_SHOTS_3PT', 'DEFLECTIONS', 'CHARGES_DRAWN', 'SCREEN_ASSISTS', 'SCREEN_AST_PTS', 'OFF_LOOSE_BALLS_RECOVERED', 'DEF_LOOSE_BALLS_RECOVERED', 'LOOSE_BALLS_RECOVERED', 'OFF_BOXOUTS', 'DEF_BOXOUTS', 'BOX_OUT_PLAYER_TEAM_REBS', 'BOX_OUT_PLAYER_REBS', 'BOX_OUTS']
```

#### TeamStats `team_stats`
```text
['GAME_ID', 'TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'TEAM_CITY', 'MINUTES', 'PTS', 'SCREEN_ASSISTS', 'SCREEN_AST_PTS', 'OFF_LOOSE_BALLS_RECOVERED', 'DEF_LOOSE_BALLS_RECOVERED', 'LOOSE_BALLS_RECOVERED', 'OFF_BOXOUTS', 'DEF_BOXOUTS', 'BOX_OUT_PLAYER_TEAM_REBS', 'BOX_OUT_PLAYER_REBS', 'BOX_OUTS']
```


## JSON
```json
{
    "data_sets": {
        "HustleStatsAvailable": [
          "GAME_ID", 
          "HUSTLE_STATUS"
        ],
        "PlayerStats": [
          "GAME_ID", 
          "TEAM_ID", 
          "TEAM_ABBREVIATION", 
          "TEAM_CITY", 
          "PLAYER_ID", 
          "PLAYER_NAME",
          "START_POSITION", 
          "COMMENT", 
          "MINUTES", 
          "PTS", 
          "CONTESTED_SHOTS",
          "CONTESTED_SHOTS_2PT", 
          "CONTESTED_SHOTS_3PT", 
          "DEFLECTIONS", 
          "CHARGES_DRAWN",
          "SCREEN_ASSISTS", 
          "SCREEN_AST_PTS", 
          "OFF_LOOSE_BALLS_RECOVERED",
          "DEF_LOOSE_BALLS_RECOVERED", 
          "LOOSE_BALLS_RECOVERED", 
          "OFF_BOXOUTS", 
          "DEF_BOXOUTS",
          "BOX_OUT_PLAYER_TEAM_REBS", 
          "BOX_OUT_PLAYER_REBS", 
          "BOX_OUTS"
        ],
        "TeamStats": [
          "GAME_ID", 
          "TEAM_ID", 
          "TEAM_NAME", 
          "TEAM_ABBREVIATION", 
          "TEAM_CITY", 
          "MINUTES",
          "PTS", 
          "SCREEN_ASSISTS", 
          "SCREEN_AST_PTS", 
          "OFF_LOOSE_BALLS_RECOVERED",
          "DEF_LOOSE_BALLS_RECOVERED", 
          "LOOSE_BALLS_RECOVERED", 
          "OFF_BOXOUTS", 
          "DEF_BOXOUTS",
          "BOX_OUT_PLAYER_TEAM_REBS", 
          "BOX_OUT_PLAYER_REBS", 
          "BOX_OUTS"
        ]
    },
    "endpoint": "BoxScoreHustle",
    "last_validated_date": "2023-05-10",
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

Last validated 2023-05-10