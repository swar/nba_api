# PlayerFantasyProfileBarGraph

##### Endpoint URL
>[https://stats.nba.com/stats/playerfantasyprofilebargraph](https://stats.nba.com/stats/playerfantasyprofilebargraph)

##### Valid URL
>[https://stats.nba.com/stats/playerfantasyprofilebargraph?LeagueID=&PlayerID=2544&Season=2017-18&SeasonType=](https://stats.nba.com/stats/playerfantasyprofilebargraph?LeagueID=&PlayerID=2544&Season=2017-18&SeasonType=)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**PlayerID**_ |  | `Y` |  | 
_**Season**_ | `^\d{4}-\d{2}$` | `Y` |  | 
_**SeasonType**_ | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$` |  | `Y` | 
_**LeagueID**_ | `(00)\|(20)\|(10)` |  | `Y` | 

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
    "last_validated_date": "2018-10-08",
    "nullable_parameters": [
        "LeagueID",
        "SeasonType"
    ],
    "parameter_patterns": {
        "LeagueID": "(00)|(20)|(10)",
        "PlayerID": null,
        "Season": "^\\d{4}-\\d{2}$",
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

Last validated 2018-10-08