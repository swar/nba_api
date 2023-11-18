# PlayerFantasyProfileBarGraph
##### [nba_api/stats/endpoints/playerfantasyprofilebargraph.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/playerfantasyprofilebargraph.py)

##### Endpoint URL
>[https://stats.nba.com/stats/playerfantasyprofilebargraph](https://stats.nba.com/stats/playerfantasyprofilebargraph)

##### Valid URL
>[https://stats.nba.com/stats/playerfantasyprofilebargraph?LeagueID=&PlayerID=2544&Season=2019-20&SeasonType=](https://stats.nba.com/stats/playerfantasyprofilebargraph?LeagueID=&PlayerID=2544&Season=2019-20&SeasonType=)

## Parameters
| API Parameter Name                                                                                                  | Python Parameter Variable     |                          Pattern                           | Required | Nullable |
|---------------------------------------------------------------------------------------------------------------------|-------------------------------|:----------------------------------------------------------:|:--------:|:--------:|
| [_**PlayerID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerID)     | player_id                     |                                                            |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)         | season                        |                                                            |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType) | season_type_all_star_nullable | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$` |          |   `Y`    | 
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)     | league_id_nullable            |                                                            |          |   `Y`    | 

## Data Sets
#### LastFiveGamesAvg `last_five_games_avg`
```text
['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_ABBREVIATION', 'FAN_DUEL_PTS', 'NBA_FANTASY_PTS', 'PTS', 'REB', 'AST', 'FG3M', 'FT_PCT', 'STL', 'BLK', 'TOV', 'FG_PCT']
```

#### SeasonAvg `season_avg`
```text
['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_ABBREVIATION', 'FAN_DUEL_PTS', 'NBA_FANTASY_PTS', 'PTS', 'REB', 'AST', 'FG3M', 'FT_PCT', 'STL', 'BLK', 'TOV', 'FG_PCT']
```


## JSON
```json
{
    "data_sets": {
        "LastFiveGamesAvg": [
            "PLAYER_ID",
            "PLAYER_NAME",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "FAN_DUEL_PTS",
            "NBA_FANTASY_PTS",
            "PTS",
            "REB",
            "AST",
            "FG3M",
            "FT_PCT",
            "STL",
            "BLK",
            "TOV",
            "FG_PCT"
        ],
        "SeasonAvg": [
            "PLAYER_ID",
            "PLAYER_NAME",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "FAN_DUEL_PTS",
            "NBA_FANTASY_PTS",
            "PTS",
            "REB",
            "AST",
            "FG3M",
            "FT_PCT",
            "STL",
            "BLK",
            "TOV",
            "FG_PCT"
        ]
    },
    "endpoint": "PlayerFantasyProfileBarGraph",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [
        "LeagueID",
        "SeasonType"
    ],
    "parameter_patterns": {
        "LeagueID": null,
        "PlayerID": null,
        "Season": null,
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$"
    },
    "parameters": [
        "LeagueID",
        "PlayerID",
        "Season",
        "SeasonType"
    ],
    "required_parameters": [
        "PlayerID",
        "Season"
    ],
    "status": "success"
}
```

Last validated 2020-08-16