# AssistLeaders
##### [nba_api/stats/endpoints/assistleaders.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/assistleaders.py)

##### Endpoint URL
>[https://stats.nba.com/stats/assistleaders](https://stats.nba.com/stats/assistleaders)

##### Valid URL
>[https://stats.nba.com/stats/assistleaders?LeagueID=00&PerMode=Totals&PlayerOrTeam=Team&Season=2019-20&SeasonType=Regular+Season](https://stats.nba.com/stats/assistleaders?LeagueID=00&PerMode=Totals&PlayerOrTeam=Team&Season=2019-20&SeasonType=Regular+Season)

## Parameters
| API Parameter Name                                                                                                      | Python Parameter Variable |                           Pattern                            | Required | Nullable |
|-------------------------------------------------------------------------------------------------------------------------|---------------------------|:------------------------------------------------------------:|:--------:|:--------:|
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)         | league_id                 |                          `^\d{2}$`                           |   `Y`    |          | 
| [_**PerMode**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PerMode)           | per_mode_simple           |                   `^(Totals)\|(PerGame)$`                    |   `Y`    |          | 
| [_**PlayerOrTeam**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerOrTeam) | player_or_team            |                     `^(Player)\|(Team)$`                     |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)             | season                    |                      `^(\d{4}-\d{2})$`                       |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType)     | season_type_playoffs      | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(Pre-Season)$` |   `Y`    |          | 

## Data Sets
#### AssistLeaders `assist_leaders`
```text
['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'AST']
```


## JSON
```json
{
    "data_sets": {
        "AssistLeaders": [
            "RANK",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "AST"
        ]
    },
    "endpoint": "AssistLeaders",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [],
    "parameter_patterns": {
        "LeagueID": "^\\d{2}$",
        "PerMode": "^(Totals)|(PerGame)$",
        "PlayerOrTeam": "^(Player)|(Team)$",
        "Season": "^(\\d{4}-\\d{2})$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(Pre-Season)$"
    },
    "parameters": [
        "LeagueID",
        "PerMode",
        "PlayerOrTeam",
        "Season",
        "SeasonType"
    ],
    "required_parameters": [
        "LeagueID",
        "PerMode",
        "PlayerOrTeam",
        "Season",
        "SeasonType"
    ],
    "status": "success"
}
```

Last validated 2020-08-16