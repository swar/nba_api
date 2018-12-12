# LeagueGameLog
##### [nba_api/stats/endpoints/leaguegamelog.py](https://github.com/swar/nba_api/blob/master/nba_api/stats/endpoints/leaguegamelog.py)

##### Endpoint URL
>[https://stats.nba.com/stats/leaguegamelog](https://stats.nba.com/stats/leaguegamelog)

##### Valid URL
>[https://stats.nba.com/stats/leaguegamelog?Counter=0&DateFrom=&DateTo=&Direction=ASC&LeagueID=00&PlayerOrTeam=T&Season=2018-19&SeasonType=Regular+Season&Sorter=DATE](https://stats.nba.com/stats/leaguegamelog?Counter=0&DateFrom=&DateTo=&Direction=ASC&LeagueID=00&PlayerOrTeam=T&Season=2018-19&SeasonType=Regular+Season&Sorter=DATE)

## Parameters
API Parameter Name | Python Parameter Variable | Parameter Mapping Class | Pattern | Required | Nullable
------------ | ------------ | ------------ | :-----------: | :---: | :---:
[_**Counter**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Counter) | counter | Counter |  |  |  | 
[_**Direction**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Direction) | direction | Direction | `^(ASC)\|(DESC)$` | `Y` |  | 
[_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id | LeagueID | `^(00)\|(20)$` | `Y` |  | 
[_**PlayerOrTeam**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerOrTeam) | player_or_team_abbreviation | PlayerOrTeamAbbreviation | `^(P)\|(T)$` | `Y` |  | 
[_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season) | season_all_time | SeasonAllTime | `^(\d{4}-\d{2})\|(ALLTIME)$` | `Y` |  | 
[_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType) | season_type_all_star | SeasonTypeAllStar | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)\|(All-Star)$` | `Y` |  | 
[_**Sorter**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Sorter) | sorter | Sorter | `^((FGM)\|(FGA)\|(FG_PCT)\|(FG3M)\|(FG3A)\|(FG3_PCT)\|(FTM)\|(FTA)\|(FT_PCT)\|(OREB)\|(DREB)\|(AST)\|(STL)\|(BLK)\|(TOV)\|(REB)\|(PTS)\|(DATE))$` | `Y` |  | 
[_**DateTo**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateTo) | date_to_nullable | DateToNullable |  |  | `Y` | 
[_**DateFrom**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateFrom) | date_from_nullable | DateFromNullable |  |  | `Y` | 

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
    "last_validated_date": "2018-12-11",
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

Last validated 2018-12-11