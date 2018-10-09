# LeagueGameLog

##### Endpoint URL
>[https://stats.nba.com/stats/leaguegamelog](https://stats.nba.com/stats/leaguegamelog)

##### Valid URL
>[https://stats.nba.com/stats/leaguegamelog?Counter=0&DateFrom=&DateTo=&Direction=ASC&LeagueID=00&PlayerOrTeam=T&Season=2017-18&SeasonType=Regular+Season&Sorter=DATE](https://stats.nba.com/stats/leaguegamelog?Counter=0&DateFrom=&DateTo=&Direction=ASC&LeagueID=00&PlayerOrTeam=T&Season=2017-18&SeasonType=Regular+Season&Sorter=DATE)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**Counter**_ |  |  |  | 
_**Direction**_ | `^(ASC)\|(DESC)$` | `Y` |  | 
_**LeagueID**_ | `^(00)\|(20)$` | `Y` |  | 
_**PlayerOrTeam**_ | `^(P)\|(T)$` | `Y` |  | 
_**Season**_ | `^(\d{4}-\d{2})\|(ALLTIME)$` | `Y` |  | 
_**SeasonType**_ | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)\|(All-Star)$` | `Y` |  | 
_**Sorter**_ | `^((FGM)\|(FGA)\|(FG_PCT)\|(FG3M)\|(FG3A)\|(FG3_PCT)\|(FTM)\|(FTA)\|(FT_PCT)\|(OREB)\|(DREB)\|(AST)\|(STL)\|(BLK)\|(TOV)\|(REB)\|(PTS)\|(DATE))$` | `Y` |  | 
_**DateTo**_ |  |  | `Y` | 
_**DateFrom**_ |  |  | `Y` | 

## Data Sets
#### LeagueGameLog `league_game_log`
```text
['SEASON_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'GAME_ID', 'GAME_DATE', 'MATCHUP', 'WL', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'PLUS_MINUS', 'VIDEO_AVAILABLE']
```


## JSON
```json
{
    "data_sets": {
        "LeagueGameLog": [
            "SEASON_ID",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "GAME_ID",
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
    "endpoint": "LeagueGameLog",
    "last_validated_date": "2018-10-08",
    "nullable_parameters": [
        "DateFrom",
        "DateTo"
    ],
    "parameter_patterns": {
        "Counter": null,
        "DateFrom": null,
        "DateTo": null,
        "Direction": "^(ASC)|(DESC)$",
        "LeagueID": "^(00)|(20)$",
        "PlayerOrTeam": "^(P)|(T)$",
        "Season": "^(\\d{4}-\\d{2})|(ALLTIME)$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)|(All-Star)$",
        "Sorter": "^((FGM)|(FGA)|(FG_PCT)|(FG3M)|(FG3A)|(FG3_PCT)|(FTM)|(FTA)|(FT_PCT)|(OREB)|(DREB)|(AST)|(STL)|(BLK)|(TOV)|(REB)|(PTS)|(DATE))$"
    },
    "parameters": [
        "Counter",
        "DateFrom",
        "DateTo",
        "Direction",
        "LeagueID",
        "PlayerOrTeam",
        "Season",
        "SeasonType",
        "Sorter"
    ],
    "required_parameters": [
        "Direction",
        "LeagueID",
        "PlayerOrTeam",
        "Season",
        "SeasonType",
        "Sorter"
    ],
    "status": "success"
}
```

Last validated 2018-10-08