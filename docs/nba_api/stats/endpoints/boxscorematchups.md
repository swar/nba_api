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
['GAME_ID', 'OFF_TEAM_ID', 'OFF_TEAM_ABBREVIATION', 'OFF_TEAM_CITY', 'OFF_TEAM_NICKNAME', 'OFF_PLAYER_ID', 'OFF_PLAYER_NAME', 'DEF_TEAM_ID', 'DEF_TEAM_ABBREVIATION', 'DEF_TEAM_CITY', 'DEF_TEAM_NICKNAME', 'DEF_PLAYER_ID', 'DEF_PLAYER_NAME', 'MATCHUP_MIN', 'PARTIAL_POSS', 'PCT_DEFENDER_TOTAL_TIME', 'PCT_OFF_TOTAL_TIME', 'PCT_TOTAL_TIME_BOTH_ON', 'SWITCHES_ON', 'PLAYER_PTS', 'TEAM_PTS', 'MATCHUP_AST', 'MATCHUP_POTENTIAL_AST', 'MATCHUP_TOV', 'MATCHUP_BLK', 'MATCHUP_FGM', 'MATCHUP_FGA', 'MATCHUP_FG_PCT', 'MATCHUP_FG3M', 'MATCHUP_FG3A', 'MATCHUP_FG3_PCT', 'HELP_BLK', 'HELP_FGM', 'HELP_FGA', 'HELP_FG_PERC', 'MATCHUP_FTM', 'MATCHUP_FTA', 'SFL']
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
            "MATCHUP_MIN",
            "PARTIAL_POSS",
            "PCT_DEFENDER_TOTAL_TIME",
            "PCT_OFF_TOTAL_TIME",
            "PCT_TOTAL_TIME_BOTH_ON",
            "SWITCHES_ON",
            "PLAYER_PTS",
            "TEAM_PTS",
            "MATCHUP_AST",
            "MATCHUP_POTENTIAL_AST",
            "MATCHUP_TOV",
            "MATCHUP_BLK",
            "MATCHUP_FGM",
            "MATCHUP_FGA",
            "MATCHUP_FG_PCT",
            "MATCHUP_FG3M",
            "MATCHUP_FG3A",
            "MATCHUP_FG3_PCT",
            "HELP_BLK",
            "HELP_FGM",
            "HELP_FGA",
            "HELP_FG_PERC",
            "MATCHUP_FTM",
            "MATCHUP_FTA",
            "SFL"
        ]
    },
    "endpoint": "BoxScoreMatchups",
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

Last validated 2020-08-15