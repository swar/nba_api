# PlayerGameLog
##### [nba_api/stats/endpoints/playergamelog.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/playergamelog.py)

##### Endpoint URL
>[https://stats.nba.com/stats/playergamelog](https://stats.nba.com/stats/playergamelog)

##### Valid URL
>[https://stats.nba.com/stats/playergamelog?DateFrom=&DateTo=&LeagueID=&PlayerID=2544&Season=2019-20&SeasonType=Regular+Season](https://stats.nba.com/stats/playergamelog?DateFrom=&DateTo=&LeagueID=&PlayerID=2544&Season=2019-20&SeasonType=Regular+Season)

## Parameters
| API Parameter Name                                                                                                  | Python Parameter Variable |                                Pattern                                 | Required | Nullable |
|---------------------------------------------------------------------------------------------------------------------|---------------------------|:----------------------------------------------------------------------:|:--------:|:--------:|
| [_**PlayerID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerID)     | player_id                 |                                                                        |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)         | season                    |                                                                        |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType) | season_type_all_star      | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All-Star)\|(All Star)$` |   `Y`    |          | 
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)     | league_id_nullable        |                                                                        |          |   `Y`    | 
| [_**DateTo**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateTo)         | date_to_nullable          |                                                                        |          |   `Y`    | 
| [_**DateFrom**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateFrom)     | date_from_nullable        |                                                                        |          |   `Y`    | 

## Data Sets
#### PlayerGameLog `player_game_log`
```text
['SEASON_ID', 'Player_ID', 'Game_ID', 'GAME_DATE', 'MATCHUP', 'WL', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'PLUS_MINUS', 'VIDEO_AVAILABLE']
```


## JSON
```json
{
    "data_sets": {
        "PlayerGameLog": [
            "SEASON_ID",
            "Player_ID",
            "Game_ID",
            "GAME_DATE",
            "MATCHUP",
            "WL",
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
            "STL",
            "BLK",
            "TOV",
            "PF",
            "PTS",
            "PLUS_MINUS",
            "VIDEO_AVAILABLE"
        ]
    },
    "endpoint": "PlayerGameLog",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [
        "DateFrom",
        "DateTo",
        "LeagueID"
    ],
    "parameter_patterns": {
        "DateFrom": null,
        "DateTo": null,
        "LeagueID": null,
        "PlayerID": null,
        "Season": null,
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All-Star)|(All Star)$"
    },
    "parameters": [
        "DateFrom",
        "DateTo",
        "LeagueID",
        "PlayerID",
        "Season",
        "SeasonType"
    ],
    "required_parameters": [
        "PlayerID",
        "Season",
        "SeasonType"
    ],
    "status": "success"
}
```

Last validated 2020-08-16