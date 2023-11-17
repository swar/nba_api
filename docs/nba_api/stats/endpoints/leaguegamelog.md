# LeagueGameLog
##### [nba_api/stats/endpoints/leaguegamelog.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/leaguegamelog.py)

##### Endpoint URL
>[https://stats.nba.com/stats/leaguegamelog](https://stats.nba.com/stats/leaguegamelog)

##### Valid URL
>[https://stats.nba.com/stats/leaguegamelog?Counter=0&DateFrom=&DateTo=&Direction=ASC&LeagueID=00&PlayerOrTeam=T&Season=2019-20&SeasonType=Regular+Season&Sorter=DATE](https://stats.nba.com/stats/leaguegamelog?Counter=0&DateFrom=&DateTo=&Direction=ASC&LeagueID=00&PlayerOrTeam=T&Season=2019-20&SeasonType=Regular+Season&Sorter=DATE)

## Parameters
| API Parameter Name                                                                                                      | Python Parameter Variable   |                                                                      Pattern                                                                      | Required | Nullable |
|-------------------------------------------------------------------------------------------------------------------------|-----------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------:|:--------:|:--------:|
| [_**Counter**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Counter)           | counter                     |                                                                                                                                                   |   `Y`    |          | 
| [_**Direction**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Direction)       | direction                   |                                                                 `^(ASC)\|(DESC)$`                                                                 |   `Y`    |          | 
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)         | league_id                   |                                                                                                                                                   |   `Y`    |          | 
| [_**PlayerOrTeam**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerOrTeam) | player_or_team_abbreviation |                                                                   `^(P)\|(T)$`                                                                    |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)             | season                      |                                                                                                                                                   |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType)     | season_type_all_star        |                                      `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)\|(All-Star)$`                                       |   `Y`    |          | 
| [_**Sorter**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Sorter)             | sorter                      | `^((FGM)\|(FGA)\|(FG_PCT)\|(FG3M)\|(FG3A)\|(FG3_PCT)\|(FTM)\|(FTA)\|(FT_PCT)\|(OREB)\|(DREB)\|(AST)\|(STL)\|(BLK)\|(TOV)\|(REB)\|(PTS)\|(DATE))$` |   `Y`    |          | 
| [_**DateTo**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateTo)             | date_to_nullable            |                                                                                                                                                   |          |   `Y`    | 
| [_**DateFrom**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateFrom)         | date_from_nullable          |                                                                                                                                                   |          |   `Y`    | 

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
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [
        "DateFrom",
        "DateTo"
    ],
    "parameter_patterns": {
        "Counter": null,
        "DateFrom": null,
        "DateTo": null,
        "Direction": "^(ASC)|(DESC)$",
        "LeagueID": null,
        "PlayerOrTeam": "^(P)|(T)$",
        "Season": null,
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
        "Counter",
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

Last validated 2020-08-16