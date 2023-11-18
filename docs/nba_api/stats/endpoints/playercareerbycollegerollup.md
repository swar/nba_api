# PlayerCareerByCollegeRollup
##### [nba_api/stats/endpoints/playercareerbycollegerollup.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/playercareerbycollegerollup.py)

##### Endpoint URL
>[https://stats.nba.com/stats/playercareerbycollegerollup](https://stats.nba.com/stats/playercareerbycollegerollup)

##### Valid URL
>[https://stats.nba.com/stats/playercareerbycollegerollup?LeagueID=00&PerMode=Totals&Season=&SeasonType=Regular+Season](https://stats.nba.com/stats/playercareerbycollegerollup?LeagueID=00&PerMode=Totals&Season=&SeasonType=Regular+Season)

## Parameters
| API Parameter Name                                                                                                  | Python Parameter Variable |                          Pattern                           | Required | Nullable |
|---------------------------------------------------------------------------------------------------------------------|---------------------------|:----------------------------------------------------------:|:--------:|:--------:|
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)     | league_id                 |                                                            |   `Y`    |          | 
| [_**PerMode**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PerMode)       | per_mode_simple           |                                                            |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType) | season_type_all_star      | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$` |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)         | season_nullable           |                                                            |          |   `Y`    | 

## Data Sets
#### East `east`
```text
['REGION', 'SEED', 'COLLEGE', 'PLAYERS', 'GP', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```

#### Midwest `midwest`
```text
['REGION', 'SEED', 'COLLEGE', 'PLAYERS', 'GP', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```

#### South `south`
```text
['REGION', 'SEED', 'COLLEGE', 'PLAYERS', 'GP', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```

#### West `west`
```text
['REGION', 'SEED', 'COLLEGE', 'PLAYERS', 'GP', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```


## JSON
```json
{
    "data_sets": {
        "East": [
            "REGION",
            "SEED",
            "COLLEGE",
            "PLAYERS",
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
        ],
        "Midwest": [
            "REGION",
            "SEED",
            "COLLEGE",
            "PLAYERS",
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
        ],
        "South": [
            "REGION",
            "SEED",
            "COLLEGE",
            "PLAYERS",
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
        ],
        "West": [
            "REGION",
            "SEED",
            "COLLEGE",
            "PLAYERS",
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
    "endpoint": "PlayerCareerByCollegeRollup",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [
        "Season"
    ],
    "parameter_patterns": {
        "LeagueID": null,
        "PerMode": null,
        "Season": null,
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$"
    },
    "parameters": [
        "LeagueID",
        "PerMode",
        "Season",
        "SeasonType"
    ],
    "required_parameters": [
        "LeagueID",
        "PerMode",
        "SeasonType"
    ],
    "status": "success"
}
```

Last validated 2020-08-16