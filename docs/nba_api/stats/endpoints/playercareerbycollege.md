# PlayerCareerByCollege
##### [nba_api/stats/endpoints/playercareerbycollege.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/playercareerbycollege.py)

##### Endpoint URL
>[https://stats.nba.com/stats/playercareerbycollege](https://stats.nba.com/stats/playercareerbycollege)

##### Valid URL
>[https://stats.nba.com/stats/playercareerbycollege?College=Ohio+State&LeagueID=00&PerMode=Totals&Season=&SeasonType=Regular+Season](https://stats.nba.com/stats/playercareerbycollege?College=Ohio+State&LeagueID=00&PerMode=Totals&Season=&SeasonType=Regular+Season)

## Parameters
| API Parameter Name                                                                                                  | Python Parameter Variable |                          Pattern                           | Required | Nullable |
|---------------------------------------------------------------------------------------------------------------------|---------------------------|:----------------------------------------------------------:|:--------:|:--------:|
| [_**College**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#College)       | college                   |                                                            |   `Y`    |          | 
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)     | league_id                 |                                                            |   `Y`    |          | 
| [_**PerMode**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PerMode)       | per_mode_simple           |                                                            |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType) | season_type_all_star      | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$` |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)         | season_nullable           |                                                            |          |   `Y`    | 

## Data Sets
#### PlayerCareerByCollege `player_career_by_college`
```text
['PLAYER_ID', 'PLAYER_NAME', 'COLLEGE', 'GP', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```


## JSON
```json
{
    "data_sets": {
        "PlayerCareerByCollege": [
            "PLAYER_ID",
            "PLAYER_NAME",
            "COLLEGE",
            "GP",
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
            "PTS"
        ]
    },
    "endpoint": "PlayerCareerByCollege",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [
        "Season"
    ],
    "parameter_patterns": {
        "College": null,
        "LeagueID": null,
        "PerMode": null,
        "Season": null,
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$"
    },
    "parameters": [
        "College",
        "LeagueID",
        "PerMode",
        "Season",
        "SeasonType"
    ],
    "required_parameters": [
        "College",
        "LeagueID",
        "PerMode",
        "SeasonType"
    ],
    "status": "success"
}
```

Last validated 2020-08-16