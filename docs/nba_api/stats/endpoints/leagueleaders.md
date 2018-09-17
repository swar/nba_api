# LeagueLeaders

##### Endpoint URL
>[https://stats.nba.com/stats/leagueleaders](https://stats.nba.com/stats/leagueleaders)

##### Valid URL
>[https://stats.nba.com/stats/leagueleaders?ActiveFlag=&LeagueID=00&PerMode=Totals&Scope=S&Season=2017-18&SeasonType=Regular+Season&StatCategory=PTS](https://stats.nba.com/stats/leagueleaders?ActiveFlag=&LeagueID=00&PerMode=Totals&Scope=S&Season=2017-18&SeasonType=Regular+Season&StatCategory=PTS)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**LeagueID**_ | `^\d{2}$` | `Y` |  | 
_**PerMode**_ | `^(Totals)|(PerGame)|(Per48)$` | `Y` |  | 
_**Scope**_ | `^(RS)|(S)|(Rookies)$` | `Y` |  | 
_**Season**_ | `^(\d{4}-\d{2})|(All Time)$` | `Y` |  | 
_**SeasonType**_ | `^(Regular Season)|(Playoffs)|(All Star)|(Pre Season)$` | `Y` |  | 
_**StatCategory**_ |  | `Y` |  | 
_**ActiveFlag**_ |  |  | `Y` | 

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
    "nullable_parameters": [
        "ActiveFlag"
    ],
    "parameter_patterns": {
        "ActiveFlag": null,
        "LeagueID": "^\\d{2}$",
        "PerMode": "^(Totals)|(PerGame)|(Per48)$",
        "Scope": "^(RS)|(S)|(Rookies)$",
        "Season": "^(\\d{4}-\\d{2})|(All Time)$",
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

Last validated 2018-09-16