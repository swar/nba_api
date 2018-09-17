# BoxScoreTraditionalV2

##### Endpoint URL
>[https://stats.nba.com/stats/boxscoretraditionalv2](https://stats.nba.com/stats/boxscoretraditionalv2)

##### Valid URL
>[https://stats.nba.com/stats/boxscoretraditionalv2?EndPeriod=1&EndRange=0&GameID=0021700807&RangeType=0&StartPeriod=1&StartRange=0](https://stats.nba.com/stats/boxscoretraditionalv2?EndPeriod=1&EndRange=0&GameID=0021700807&RangeType=0&StartPeriod=1&StartRange=0)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**EndPeriod**_ |  | `Y` |  | 
_**EndRange**_ |  | `Y` |  | 
_**GameID**_ | `^\d{10}$` | `Y` |  | 
_**RangeType**_ |  | `Y` |  | 
_**StartPeriod**_ |  | `Y` |  | 
_**StartRange**_ |  | `Y` |  | 

## Data Sets
#### PlayerStats `player_stats`
```text
['GAME_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_CITY', 'PLAYER_ID', 'PLAYER_NAME', 'START_POSITION', 'COMMENT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TO', 'PF', 'PTS', 'PLUS_MINUS']
```

#### TeamStarterBenchStats `team_starter_bench_stats`
```text
['GAME_ID', 'TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'TEAM_CITY', 'STARTERS_BENCH', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TO', 'PF', 'PTS']
```

#### TeamStats `team_stats`
```text
['GAME_ID', 'TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'TEAM_CITY', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TO', 'PF', 'PTS', 'PLUS_MINUS']
```


## JSON
```json
{
    "data_sets": {
        "PlayerStats": [
            "GAME_ID",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_CITY",
            "PLAYER_ID",
            "PLAYER_NAME",
            "START_POSITION",
            "COMMENT",
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
            "TO",
            "PF",
            "PTS",
            "PLUS_MINUS"
        ],
        "TeamStarterBenchStats": [
            "GAME_ID",
            "TEAM_ID",
            "TEAM_NAME",
            "TEAM_ABBREVIATION",
            "TEAM_CITY",
            "STARTERS_BENCH",
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
            "TO",
            "PF",
            "PTS"
        ],
        "TeamStats": [
            "GAME_ID",
            "TEAM_ID",
            "TEAM_NAME",
            "TEAM_ABBREVIATION",
            "TEAM_CITY",
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
            "TO",
            "PF",
            "PTS",
            "PLUS_MINUS"
        ]
    },
    "endpoint": "BoxScoreTraditionalV2",
    "nullable_parameters": [],
    "parameter_patterns": {
        "EndPeriod": null,
        "EndRange": null,
        "GameID": "^\\d{10}$",
        "RangeType": null,
        "StartPeriod": null,
        "StartRange": null
    },
    "parameters": [
        "EndPeriod",
        "EndRange",
        "GameID",
        "RangeType",
        "StartPeriod",
        "StartRange"
    ],
    "required_parameters": [
        "EndPeriod",
        "EndRange",
        "GameID",
        "RangeType",
        "StartPeriod",
        "StartRange"
    ],
    "status": "success"
}
```

Last validated 2018-09-16