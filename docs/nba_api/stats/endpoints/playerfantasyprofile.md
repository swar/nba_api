# PlayerFantasyProfile

##### Endpoint URL
>[https://stats.nba.com/stats/playerfantasyprofile](https://stats.nba.com/stats/playerfantasyprofile)

##### Valid URL
>[https://stats.nba.com/stats/playerfantasyprofile?LeagueID=&MeasureType=Base&PaceAdjust=N&PerMode=Totals&PlayerID=2544&PlusMinus=N&Rank=N&Season=2017-18&SeasonType=Regular+Season](https://stats.nba.com/stats/playerfantasyprofile?LeagueID=&MeasureType=Base&PaceAdjust=N&PerMode=Totals&PlayerID=2544&PlusMinus=N&Rank=N&Season=2017-18&SeasonType=Regular+Season)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**MeasureType**_ | `^(Base)$` | `Y` |  | 
_**PaceAdjust**_ | `^(N)$` | `Y` |  | 
_**PerMode**_ | `^(Totals)\|(PerGame)\|(Per36)$` | `Y` |  | 
_**PlayerID**_ |  | `Y` |  | 
_**PlusMinus**_ | `^(N)$` | `Y` |  | 
_**Rank**_ | `^(N)$` | `Y` |  | 
_**Season**_ | `^\d{4}-\d{2}$` | `Y` |  | 
_**SeasonType**_ | `^(Regular Season)\|(Pre Season)\|(Playoffs)$` | `Y` |  | 
_**LeagueID**_ | `(00)\|(20)\|(10)` |  | `Y` | 

## Data Sets
#### DaysRestModified `days_rest_modified`
```text
['GROUP_SET', 'GROUP_VALUE', 'SEASON_YEAR', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'DD2', 'TD3', 'FAN_DUEL_PTS']
```

#### LastNGames `last_n_games`
```text
['GROUP_SET', 'GROUP_VALUE', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'DD2', 'TD3', 'FAN_DUEL_PTS']
```

#### Location `location`
```text
['GROUP_SET', 'GROUP_VALUE', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'DD2', 'TD3', 'FAN_DUEL_PTS']
```

#### Opponent `opponent`
```text
['GROUP_SET', 'GROUP_VALUE', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'DD2', 'TD3', 'FAN_DUEL_PTS']
```

#### Overall `overall`
```text
['GROUP_SET', 'GROUP_VALUE', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'DD2', 'TD3', 'FAN_DUEL_PTS']
```


## JSON
```json
{
    "data_sets": {
        "DaysRestModified": [
            "GROUP_SET",
            "GROUP_VALUE",
            "SEASON_YEAR",
            "GP",
            "W",
            "L",
            "W_PCT",
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
            "TOV",
            "STL",
            "BLK",
            "BLKA",
            "PF",
            "PFD",
            "PTS",
            "PLUS_MINUS",
            "DD2",
            "TD3",
            "FAN_DUEL_PTS"
        ],
        "LastNGames": [
            "GROUP_SET",
            "GROUP_VALUE",
            "GP",
            "W",
            "L",
            "W_PCT",
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
            "TOV",
            "STL",
            "BLK",
            "BLKA",
            "PF",
            "PFD",
            "PTS",
            "PLUS_MINUS",
            "DD2",
            "TD3",
            "FAN_DUEL_PTS"
        ],
        "Location": [
            "GROUP_SET",
            "GROUP_VALUE",
            "GP",
            "W",
            "L",
            "W_PCT",
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
            "TOV",
            "STL",
            "BLK",
            "BLKA",
            "PF",
            "PFD",
            "PTS",
            "PLUS_MINUS",
            "DD2",
            "TD3",
            "FAN_DUEL_PTS"
        ],
        "Opponent": [
            "GROUP_SET",
            "GROUP_VALUE",
            "GP",
            "W",
            "L",
            "W_PCT",
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
            "TOV",
            "STL",
            "BLK",
            "BLKA",
            "PF",
            "PFD",
            "PTS",
            "PLUS_MINUS",
            "DD2",
            "TD3",
            "FAN_DUEL_PTS"
        ],
        "Overall": [
            "GROUP_SET",
            "GROUP_VALUE",
            "GP",
            "W",
            "L",
            "W_PCT",
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
            "TOV",
            "STL",
            "BLK",
            "BLKA",
            "PF",
            "PFD",
            "PTS",
            "PLUS_MINUS",
            "DD2",
            "TD3",
            "FAN_DUEL_PTS"
        ]
    },
    "endpoint": "PlayerFantasyProfile",
    "nullable_parameters": [
        "LeagueID"
    ],
    "parameter_patterns": {
        "LeagueID": "(00)|(20)|(10)",
        "MeasureType": "^(Base)$",
        "PaceAdjust": "^(N)$",
        "PerMode": "^(Totals)|(PerGame)|(Per36)$",
        "PlayerID": null,
        "PlusMinus": "^(N)$",
        "Rank": "^(N)$",
        "Season": "^\\d{4}-\\d{2}$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)$"
    },
    "parameters": [
        "LeagueID",
        "MeasureType",
        "PaceAdjust",
        "PerMode",
        "PlayerID",
        "PlusMinus",
        "Rank",
        "Season",
        "SeasonType"
    ],
    "required_parameters": [
        "MeasureType",
        "PaceAdjust",
        "PerMode",
        "PlayerID",
        "PlusMinus",
        "Rank",
        "Season",
        "SeasonType"
    ],
    "status": "success"
}
```

Last validated 2018-09-16