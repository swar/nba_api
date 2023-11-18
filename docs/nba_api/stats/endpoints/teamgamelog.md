# TeamGameLog
##### [nba_api/stats/endpoints/teamgamelog.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/teamgamelog.py)

##### Endpoint URL
>[https://stats.nba.com/stats/teamgamelog](https://stats.nba.com/stats/teamgamelog)

##### Valid URL
>[https://stats.nba.com/stats/teamgamelog?DateFrom=&DateTo=&LeagueID=&Season=2019-20&SeasonType=Regular+Season&TeamID=1610612739](https://stats.nba.com/stats/teamgamelog?DateFrom=&DateTo=&LeagueID=&Season=2019-20&SeasonType=Regular+Season&TeamID=1610612739)

## Parameters
| API Parameter Name                                                                                                  | Python Parameter Variable |                                       Pattern                                       | Required | Nullable |
|---------------------------------------------------------------------------------------------------------------------|---------------------------|:-----------------------------------------------------------------------------------:|:--------:|:--------:|
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)         | season                    |                                                                                     |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType) | season_type_all_star      | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All-Star)\|(All Star)\|(Preseason)$` |   `Y`    |          | 
| [_**TeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TeamID)         | team_id                   |                                                                                     |   `Y`    |          | 
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)     | league_id_nullable        |                                                                                     |          |   `Y`    | 
| [_**DateTo**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateTo)         | date_to_nullable          |                                                                                     |          |   `Y`    | 
| [_**DateFrom**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateFrom)     | date_from_nullable        |                                                                                     |          |   `Y`    | 

## Data Sets
#### TeamGameLog `team_game_log`
```text
['Team_ID', 'Game_ID', 'GAME_DATE', 'MATCHUP', 'WL', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```


## JSON
```json
{
    "data_sets": {
        "TeamGameLog": [
            "Team_ID",
            "Game_ID",
            "GAME_DATE",
            "MATCHUP",
            "WL",
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
            "STL",
            "BLK",
            "TOV",
            "PF",
            "PTS"
        ]
    },
    "endpoint": "TeamGameLog",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [
        "DateFrom",
        "DateTo",
        "LeagueID"
    ],
    "parameter_patterns": {
        "DateFrom": null,
        "DateTo": null,
        "LeagueID": null,
        "Season": null,
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All-Star)|(All Star)|(Preseason)$",
        "TeamID": null
    },
    "parameters": [
        "DateFrom",
        "DateTo",
        "LeagueID",
        "Season",
        "SeasonType",
        "TeamID"
    ],
    "required_parameters": [
        "Season",
        "SeasonType",
        "TeamID"
    ],
    "status": "success"
}
```

Last validated 2020-08-16