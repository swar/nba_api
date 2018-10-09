# PlayerGameLog

##### Endpoint URL
>[https://stats.nba.com/stats/playergamelog](https://stats.nba.com/stats/playergamelog)

##### Valid URL
>[https://stats.nba.com/stats/playergamelog?DateFrom=&DateTo=&LeagueID=&PlayerID=2544&Season=2017-18&SeasonType=Regular+Season](https://stats.nba.com/stats/playergamelog?DateFrom=&DateTo=&LeagueID=&PlayerID=2544&Season=2017-18&SeasonType=Regular+Season)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**PlayerID**_ |  | `Y` |  | 
_**Season**_ | `^(\d{4}-\d{2})\|(ALL)$` | `Y` |  | 
_**SeasonType**_ | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All-Star)\|(All Star)$` | `Y` |  | 
_**LeagueID**_ | `(00)\|(20)\|(10)` |  | `Y` | 
_**DateTo**_ |  |  | `Y` | 
_**DateFrom**_ |  |  | `Y` | 

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
    "last_validated_date": "2018-10-08",
    "nullable_parameters": [
        "DateFrom",
        "DateTo",
        "LeagueID"
    ],
    "parameter_patterns": {
        "DateFrom": null,
        "DateTo": null,
        "LeagueID": "(00)|(20)|(10)",
        "PlayerID": null,
        "Season": "^(\\d{4}-\\d{2})|(ALL)$",
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

Last validated 2018-10-08