# CumeStatsTeam
##### [nba_api/stats/endpoints/cumestatsteam.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/cumestatsteam.py)

##### Endpoint URL
>[https://stats.nba.com/stats/cumestatsteam](https://stats.nba.com/stats/cumestatsteam)

##### Valid URL
>[https://stats.nba.com/stats/cumestatsteam?GameIDs=0021700807&LeagueID=00&Season=2019-20&SeasonType=Regular+Season&TeamID=1610612739](https://stats.nba.com/stats/cumestatsteam?GameIDs=0021700807&LeagueID=00&Season=2019-20&SeasonType=Regular+Season&TeamID=1610612739)

## Parameters
| API Parameter Name                                                                                                  | Python Parameter Variable |                          Pattern                           | Required | Nullable |
|---------------------------------------------------------------------------------------------------------------------|---------------------------|:----------------------------------------------------------:|:--------:|:--------:|
| [_**GameIDs**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameIDs)       | game_ids                  |                                                            |   `Y`    |          | 
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)     | league_id                 |                                                            |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)         | season                    |                                                            |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType) | season_type_all_star      | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$` |   `Y`    |          | 
| [_**TeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TeamID)         | team_id                   |                                                            |   `Y`    |          | 

## Data Sets
#### GameByGameStats `game_by_game_stats`
```text
['JERSEY_NUM', 'PLAYER', 'PERSON_ID', 'TEAM_ID', 'GP', 'GS', 'ACTUAL_MINUTES', 'ACTUAL_SECONDS', 'FG', 'FGA', 'FG_PCT', 'FG3', 'FG3A', 'FG3_PCT', 'FT', 'FTA', 'FT_PCT', 'OFF_REB', 'DEF_REB', 'TOT_REB', 'AST', 'PF', 'DQ', 'STL', 'TURNOVERS', 'BLK', 'PTS', 'MAX_ACTUAL_MINUTES', 'MAX_ACTUAL_SECONDS', 'MAX_REB', 'MAX_AST', 'MAX_STL', 'MAX_TURNOVERS', 'MAX_BLKP', 'MAX_PTS', 'AVG_ACTUAL_MINUTES', 'AVG_ACTUAL_SECONDS', 'AVG_REB', 'AVG_AST', 'AVG_STL', 'AVG_TURNOVERS', 'AVG_BLKP', 'AVG_PTS', 'PER_MIN_REB', 'PER_MIN_AST', 'PER_MIN_STL', 'PER_MIN_TURNOVERS', 'PER_MIN_BLK', 'PER_MIN_PTS']
```

#### TotalTeamStats `total_team_stats`
```text
['CITY', 'NICKNAME', 'TEAM_ID', 'W', 'L', 'W_HOME', 'L_HOME', 'W_ROAD', 'L_ROAD', 'TEAM_TURNOVERS', 'TEAM_REBOUNDS', 'GP', 'GS', 'ACTUAL_MINUTES', 'ACTUAL_SECONDS', 'FG', 'FGA', 'FG_PCT', 'FG3', 'FG3A', 'FG3_PCT', 'FT', 'FTA', 'FT_PCT', 'OFF_REB', 'DEF_REB', 'TOT_REB', 'AST', 'PF', 'STL', 'TOTAL_TURNOVERS', 'BLK', 'PTS', 'AVG_REB', 'AVG_PTS', 'DQ']
```


## JSON
```json
{
    "data_sets": {
        "GameByGameStats": [
            "JERSEY_NUM",
            "PLAYER",
            "PERSON_ID",
            "TEAM_ID",
            "GP",
            "GS",
            "ACTUAL_MINUTES",
            "ACTUAL_SECONDS",
            "FG",
            "FGA",
            "FG_PCT",
            "FG3",
            "FG3A",
            "FG3_PCT",
            "FT",
            "FTA",
            "FT_PCT",
            "OFF_REB",
            "DEF_REB",
            "TOT_REB",
            "AST",
            "PF",
            "DQ",
            "STL",
            "TURNOVERS",
            "BLK",
            "PTS",
            "MAX_ACTUAL_MINUTES",
            "MAX_ACTUAL_SECONDS",
            "MAX_REB",
            "MAX_AST",
            "MAX_STL",
            "MAX_TURNOVERS",
            "MAX_BLKP",
            "MAX_PTS",
            "AVG_ACTUAL_MINUTES",
            "AVG_ACTUAL_SECONDS",
            "AVG_REB",
            "AVG_AST",
            "AVG_STL",
            "AVG_TURNOVERS",
            "AVG_BLKP",
            "AVG_PTS",
            "PER_MIN_REB",
            "PER_MIN_AST",
            "PER_MIN_STL",
            "PER_MIN_TURNOVERS",
            "PER_MIN_BLK",
            "PER_MIN_PTS"
        ],
        "TotalTeamStats": [
            "CITY",
            "NICKNAME",
            "TEAM_ID",
            "W",
            "L",
            "W_HOME",
            "L_HOME",
            "W_ROAD",
            "L_ROAD",
            "TEAM_TURNOVERS",
            "TEAM_REBOUNDS",
            "GP",
            "GS",
            "ACTUAL_MINUTES",
            "ACTUAL_SECONDS",
            "FG",
            "FGA",
            "FG_PCT",
            "FG3",
            "FG3A",
            "FG3_PCT",
            "FT",
            "FTA",
            "FT_PCT",
            "OFF_REB",
            "DEF_REB",
            "TOT_REB",
            "AST",
            "PF",
            "STL",
            "TOTAL_TURNOVERS",
            "BLK",
            "PTS",
            "AVG_REB",
            "AVG_PTS",
            "DQ"
        ]
    },
    "endpoint": "CumeStatsTeam",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [],
    "parameter_patterns": {
        "GameIDs": null,
        "LeagueID": null,
        "Season": null,
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$",
        "TeamID": null
    },
    "parameters": [
        "GameIDs",
        "LeagueID",
        "Season",
        "SeasonType",
        "TeamID"
    ],
    "required_parameters": [
        "GameIDs",
        "LeagueID",
        "Season",
        "SeasonType",
        "TeamID"
    ],
    "status": "success"
}
```

Last validated 2020-08-16