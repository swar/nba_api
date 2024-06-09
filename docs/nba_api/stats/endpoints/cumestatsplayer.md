# CumeStatsPlayer
##### [nba_api/stats/endpoints/cumestatsplayer.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/cumestatsplayer.py)

##### Endpoint URL
>[https://stats.nba.com/stats/cumestatsplayer](https://stats.nba.com/stats/cumestatsplayer)

##### Valid URL
>[https://stats.nba.com/stats/cumestatsplayer?GameIDs=0021700807&LeagueID=00&PlayerID=2544&Season=2019-20&SeasonType=Regular+Season](https://stats.nba.com/stats/cumestatsplayer?GameIDs=0021700807&LeagueID=00&PlayerID=2544&Season=2019-20&SeasonType=Regular+Season)

## Parameters
| API Parameter Name                                                                                                  | Python Parameter Variable |                          Pattern                           | Required | Nullable |
|---------------------------------------------------------------------------------------------------------------------|---------------------------|:----------------------------------------------------------:|:--------:|:--------:|
| [_**GameIDs**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameIDs)       | game_ids                  | `^(GameID1\|GameID2\|GameID3)$`                            |   `Y`    |          | 
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)     | league_id                 |                                                            |   `Y`    |          | 
| [_**PlayerID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerID)     | player_id                 |                                                            |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)         | season                    |                                                            |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType) | season_type_all_star      | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$` |   `Y`    |          | 

## Data Sets
#### GameByGameStats `game_by_game_stats`
```text
['DATE_EST', 'VISITOR_TEAM', 'HOME_TEAM', 'GP', 'GS', 'ACTUAL_MINUTES', 'ACTUAL_SECONDS', 'FG', 'FGA', 'FG_PCT', 'FG3', 'FG3A', 'FG3_PCT', 'FT', 'FTA', 'FT_PCT', 'OFF_REB', 'DEF_REB', 'TOT_REB', 'AVG_TOT_REB', 'AST', 'PF', 'DQ', 'STL', 'TURNOVERS', 'BLK', 'PTS', 'AVG_PTS']
```

#### TotalPlayerStats `total_player_stats`
```text
['DISPLAY_FI_LAST', 'PERSON_ID', 'JERSEY_NUM', 'GP', 'GS', 'ACTUAL_MINUTES', 'ACTUAL_SECONDS', 'FG', 'FGA', 'FG_PCT', 'FG3', 'FG3A', 'FG3_PCT', 'FT', 'FTA', 'FT_PCT', 'OFF_REB', 'DEF_REB', 'TOT_REB', 'AST', 'PF', 'DQ', 'STL', 'TURNOVERS', 'BLK', 'PTS', 'MAX_ACTUAL_MINUTES', 'MAX_ACTUAL_SECONDS', 'MAX_REB', 'MAX_AST', 'MAX_STL', 'MAX_TURNOVERS', 'MAX_BLK', 'MAX_PTS', 'AVG_ACTUAL_MINUTES', 'AVG_ACTUAL_SECONDS', 'AVG_TOT_REB', 'AVG_AST', 'AVG_STL', 'AVG_TURNOVERS', 'AVG_BLK', 'AVG_PTS', 'PER_MIN_TOT_REB', 'PER_MIN_AST', 'PER_MIN_STL', 'PER_MIN_TURNOVERS', 'PER_MIN_BLK', 'PER_MIN_PTS']
```


## JSON
```json
{
    "data_sets": {
        "GameByGameStats": [
            "DATE_EST",
            "VISITOR_TEAM",
            "HOME_TEAM",
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
            "AVG_TOT_REB",
            "AST",
            "PF",
            "DQ",
            "STL",
            "TURNOVERS",
            "BLK",
            "PTS",
            "AVG_PTS"
        ],
        "TotalPlayerStats": [
            "DISPLAY_FI_LAST",
            "PERSON_ID",
            "JERSEY_NUM",
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
            "MAX_BLK",
            "MAX_PTS",
            "AVG_ACTUAL_MINUTES",
            "AVG_ACTUAL_SECONDS",
            "AVG_TOT_REB",
            "AVG_AST",
            "AVG_STL",
            "AVG_TURNOVERS",
            "AVG_BLK",
            "AVG_PTS",
            "PER_MIN_TOT_REB",
            "PER_MIN_AST",
            "PER_MIN_STL",
            "PER_MIN_TURNOVERS",
            "PER_MIN_BLK",
            "PER_MIN_PTS"
        ]
    },
    "endpoint": "CumeStatsPlayer",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [],
    "parameter_patterns": {
        "GameIDs": null,
        "LeagueID": null,
        "PlayerID": null,
        "Season": null,
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$"
    },
    "parameters": [
        "GameIDs",
        "LeagueID",
        "PlayerID",
        "Season",
        "SeasonType"
    ],
    "required_parameters": [
        "GameIDs",
        "LeagueID",
        "PlayerID",
        "Season",
        "SeasonType"
    ],
    "status": "success"
}
```

Last validated 2020-08-16