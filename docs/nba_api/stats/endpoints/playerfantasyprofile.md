# PlayerFantasyProfile
##### [nba_api/stats/endpoints/playerfantasyprofile.py](https://github.com/swar/nba_api/blob/master/nba_api/stats/endpoints/playerfantasyprofile.py)

##### Endpoint URL
>[https://stats.nba.com/stats/playerfantasyprofile](https://stats.nba.com/stats/playerfantasyprofile)

##### Valid URL
>[https://stats.nba.com/stats/playerfantasyprofile?LeagueID=&MeasureType=Base&PaceAdjust=N&PerMode=Totals&PlayerID=2544&PlusMinus=N&Rank=N&Season=2018-19&SeasonType=Regular+Season](https://stats.nba.com/stats/playerfantasyprofile?LeagueID=&MeasureType=Base&PaceAdjust=N&PerMode=Totals&PlayerID=2544&PlusMinus=N&Rank=N&Season=2018-19&SeasonType=Regular+Season)

## Parameters
API Parameter Name | Python Parameter Variable | Parameter Mapping Class | Pattern | Required | Nullable
------------ | ------------ | ------------ | :-----------: | :---: | :---:
[_**MeasureType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#MeasureType) | measure_type_base | MeasureTypeBase | `^(Base)$` | `Y` |  | 
[_**PaceAdjust**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PaceAdjust) | pace_adjust_no | PaceAdjustNo | `^(N)$` | `Y` |  | 
[_**PerMode**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PerMode) | per_mode36 | PerMode36 | `^(Totals)\|(PerGame)\|(Per36)$` | `Y` |  | 
[_**PlayerID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerID) | player_id | PlayerID |  | `Y` |  | 
[_**PlusMinus**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlusMinus) | plus_minus_no | PlusMinusNo | `^(N)$` | `Y` |  | 
[_**Rank**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Rank) | rank_no | RankNo | `^(N)$` | `Y` |  | 
[_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season) | season | Season | `^\d{4}-\d{2}$` | `Y` |  | 
[_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType) | season_type_playoffs | SeasonTypePlayoffs | `^(Regular Season)\|(Pre Season)\|(Playoffs)$` | `Y` |  | 
[_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id_nullable | LeagueIDNullable | `(00)\|(20)\|(10)` |  | `Y` | 

## Data Sets
#### DaysRestModified `days_rest_modified`
```text
['GROUP_SET', 'GROUP_VALUE', 'SEASON_YEAR', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'DD2', 'TD3', 'FAN_DUEL_PTS', 'NBA_FANTASY_PTS']
```

#### LastNGames `last_n_games`
```text
['GROUP_SET', 'GROUP_VALUE', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'DD2', 'TD3', 'FAN_DUEL_PTS', 'NBA_FANTASY_PTS']
```

#### Location `location`
```text
['GROUP_SET', 'GROUP_VALUE', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'DD2', 'TD3', 'FAN_DUEL_PTS', 'NBA_FANTASY_PTS']
```

#### Opponent `opponent`
```text
['GROUP_SET', 'GROUP_VALUE', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'DD2', 'TD3', 'FAN_DUEL_PTS', 'NBA_FANTASY_PTS']
```

#### Overall `overall`
```text
['GROUP_SET', 'GROUP_VALUE', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'DD2', 'TD3', 'FAN_DUEL_PTS', 'NBA_FANTASY_PTS']
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
            "FAN_DUEL_PTS",
            "NBA_FANTASY_PTS"
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
            "FAN_DUEL_PTS",
            "NBA_FANTASY_PTS"
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
            "FAN_DUEL_PTS",
            "NBA_FANTASY_PTS"
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
            "FAN_DUEL_PTS",
            "NBA_FANTASY_PTS"
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
            "FAN_DUEL_PTS",
            "NBA_FANTASY_PTS"
        ]
    },
    "endpoint": "PlayerFantasyProfile",
    "last_validated_date": "2018-12-11",
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

Last validated 2018-12-11