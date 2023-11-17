# PlayerNextNGames
##### [nba_api/stats/endpoints/playernextngames.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/playernextngames.py)

##### Endpoint URL
>[https://stats.nba.com/stats/playernextngames](https://stats.nba.com/stats/playernextngames)

##### Valid URL
>[https://stats.nba.com/stats/playernextngames?LeagueID=&NumberOfGames=2147483647&PlayerID=2544&Season=2019-20&SeasonType=Regular+Season](https://stats.nba.com/stats/playernextngames?LeagueID=&NumberOfGames=2147483647&PlayerID=2544&Season=2019-20&SeasonType=Regular+Season)

## Parameters
| API Parameter Name                                                                                                        | Python Parameter Variable |                                Pattern                                 | Required | Nullable |
|---------------------------------------------------------------------------------------------------------------------------|---------------------------|:----------------------------------------------------------------------:|:--------:|:--------:|
| [_**NumberOfGames**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#NumberOfGames) | number_of_games           |                                                                        |   `Y`    |          | 
| [_**PlayerID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerID)           | player_id                 |                                                                        |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)               | season_all                |                        `^(\d{4}-\d{2})\|(ALL)$`                        |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType)       | season_type_all_star      | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All-Star)\|(All Star)$` |   `Y`    |          | 
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)           | league_id_nullable        |                                                                        |          |   `Y`    | 

## Data Sets
#### NextNGames `next_n_games`
```text
['GAME_ID', 'GAME_DATE', 'HOME_TEAM_ID', 'VISITOR_TEAM_ID', 'HOME_TEAM_NAME', 'VISITOR_TEAM_NAME', 'HOME_TEAM_ABBREVIATION', 'VISITOR_TEAM_ABBREVIATION', 'HOME_TEAM_NICKNAME', 'VISITOR_TEAM_NICKNAME', 'GAME_TIME', 'HOME_WL', 'VISITOR_WL']
```


## JSON
```json
{
    "data_sets": {
        "NextNGames": [
            "GAME_ID",
            "GAME_DATE",
            "HOME_TEAM_ID",
            "VISITOR_TEAM_ID",
            "HOME_TEAM_NAME",
            "VISITOR_TEAM_NAME",
            "HOME_TEAM_ABBREVIATION",
            "VISITOR_TEAM_ABBREVIATION",
            "HOME_TEAM_NICKNAME",
            "VISITOR_TEAM_NICKNAME",
            "GAME_TIME",
            "HOME_WL",
            "VISITOR_WL"
        ]
    },
    "endpoint": "PlayerNextNGames",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [
        "LeagueID"
    ],
    "parameter_patterns": {
        "LeagueID": null,
        "NumberOfGames": null,
        "PlayerID": null,
        "Season": "^(\\d{4}-\\d{2})|(ALL)$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All-Star)|(All Star)$"
    },
    "parameters": [
        "LeagueID",
        "NumberOfGames",
        "PlayerID",
        "Season",
        "SeasonType"
    ],
    "required_parameters": [
        "NumberOfGames",
        "PlayerID",
        "Season",
        "SeasonType"
    ],
    "status": "success"
}
```

Last validated 2020-08-16