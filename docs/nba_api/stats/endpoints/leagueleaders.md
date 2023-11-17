# LeagueLeaders
##### [nba_api/stats/endpoints/leagueleaders.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/leagueleaders.py)

##### Endpoint URL
>[https://stats.nba.com/stats/leagueleaders](https://stats.nba.com/stats/leagueleaders)

##### Valid URL
>[https://stats.nba.com/stats/leagueleaders?ActiveFlag=&LeagueID=00&PerMode=Totals&Scope=S&Season=2019-20&SeasonType=Regular+Season&StatCategory=PTS](https://stats.nba.com/stats/leagueleaders?ActiveFlag=&LeagueID=00&PerMode=Totals&Scope=S&Season=2019-20&SeasonType=Regular+Season&StatCategory=PTS)

## Parameters
| API Parameter Name                                                                                                      | Python Parameter Variable  |                          Pattern                           | Required | Nullable |
|-------------------------------------------------------------------------------------------------------------------------|----------------------------|:----------------------------------------------------------:|:--------:|:--------:|
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)         | league_id                  |                         `^\d{2}$`                          |   `Y`    |          | 
| [_**PerMode**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PerMode)           | per_mode48                 |              `^(Totals)\|(PerGame)\|(Per48)$`              |   `Y`    |          | 
| [_**Scope**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Scope)               | scope                      |                  `^(RS)\|(S)\|(Rookies)$`                  |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)             | season                     |                                                            |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType)     | season_type_all_star       | `^(Regular Season)\|(Playoffs)\|(All Star)\|(Pre Season)$` |   `Y`    |          | 
| [_**StatCategory**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#StatCategory) | stat_category_abbreviation |                                                            |   `Y`    |          | 
| [_**ActiveFlag**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#ActiveFlag)     | active_flag_nullable       |                                                            |          |   `Y`    | 

## Data Sets
#### LeagueLeaders `league_leaders`
```text
['PLAYER_ID', 'RANK', 'PLAYER', 'TEAM', 'GP', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'EFF', 'AST_TOV', 'STL_TOV']
```


## JSON
```json
{
    "data_sets": {
        "LeagueLeaders": [
            "PLAYER_ID",
            "RANK",
            "PLAYER",
            "TEAM",
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
            "PTS",
            "EFF",
            "AST_TOV",
            "STL_TOV"
        ]
    },
    "endpoint": "LeagueLeaders",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [
        "ActiveFlag"
    ],
    "parameter_patterns": {
        "ActiveFlag": null,
        "LeagueID": "^\\d{2}$",
        "PerMode": "^(Totals)|(PerGame)|(Per48)$",
        "Scope": "^(RS)|(S)|(Rookies)$",
        "Season": null,
        "SeasonType": "^(Regular Season)|(Playoffs)|(All Star)|(Pre Season)$",
        "StatCategory": null
    },
    "parameters": [
        "ActiveFlag",
        "LeagueID",
        "PerMode",
        "Scope",
        "Season",
        "SeasonType",
        "StatCategory"
    ],
    "required_parameters": [
        "LeagueID",
        "PerMode",
        "Scope",
        "Season",
        "SeasonType",
        "StatCategory"
    ],
    "status": "success"
}
```

Last validated 2020-08-16