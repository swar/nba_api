# PlayerNextNGames
##### [nba_api/stats/endpoints/playernextngames.py](https://github.com/swar/nba_api/blob/master/nba_api/stats/endpoints/playernextngames.py)

##### Endpoint URL
>[https://stats.nba.com/stats/playernextngames](https://stats.nba.com/stats/playernextngames)

##### Valid URL
>[https://stats.nba.com/stats/playernextngames?LeagueID=&NumberOfGames=2147483647&PlayerID=2544&Season=2018-19&SeasonType=Regular+Season](https://stats.nba.com/stats/playernextngames?LeagueID=&NumberOfGames=2147483647&PlayerID=2544&Season=2018-19&SeasonType=Regular+Season)

## Parameters
API Parameter Name | Python Parameter Variable | Parameter Mapping Class | Pattern | Required | Nullable
------------ | ------------ | ------------ | :-----------: | :---: | :---:
[_**NumberOfGames**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#NumberOfGames) | number_of_games | NumberOfGames |  | `Y` |  | 
[_**PlayerID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerID) | player_id | PlayerID |  | `Y` |  | 
[_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season) | season_all | SeasonAll | `^(\d{4}-\d{2})\|(ALL)$` | `Y` |  | 
[_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType) | season_type_all_star | SeasonTypeAllStar | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All-Star)\|(All Star)$` | `Y` |  | 
[_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id_nullable | LeagueIDNullable | `(00)\|(20)\|(10)` |  | `Y` | 

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
    "last_validated_date": "2018-12-11",
    "nullable_parameters": [
        "LeagueID"
    ],
    "parameter_patterns": {
        "LeagueID": "(00)|(20)|(10)",
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

Last validated 2018-12-11