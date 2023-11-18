# CommonAllPlayers
##### [nba_api/stats/endpoints/commonallplayers.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/commonallplayers.py)

##### Endpoint URL
>[https://stats.nba.com/stats/commonallplayers](https://stats.nba.com/stats/commonallplayers)

##### Valid URL
>[https://stats.nba.com/stats/commonallplayers?IsOnlyCurrentSeason=0&LeagueID=00&Season=2019-20](https://stats.nba.com/stats/commonallplayers?IsOnlyCurrentSeason=0&LeagueID=00&Season=2019-20)

## Parameters
| API Parameter Name                                                                                                                    | Python Parameter Variable |  Pattern  | Required | Nullable |
|---------------------------------------------------------------------------------------------------------------------------------------|---------------------------|:---------:|:--------:|:--------:|
| [_**IsOnlyCurrentSeason**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#IsOnlyCurrentSeason) | is_only_current_season    |           |   `Y`    |          | 
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)                       | league_id                 | `^\d{2}$` |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)                           | season                    |           |   `Y`    |          | 

## Data Sets
#### CommonAllPlayers `common_all_players`
```text
['PERSON_ID', 'DISPLAY_LAST_COMMA_FIRST', 'DISPLAY_FIRST_LAST', 'ROSTERSTATUS', 'FROM_YEAR', 'TO_YEAR', 'PLAYERCODE', 'TEAM_ID', 'TEAM_CITY', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'TEAM_CODE', 'GAMES_PLAYED_FLAG', 'OTHERLEAGUE_EXPERIENCE_CH']
```


## JSON
```json
{
    "data_sets": {
        "CommonAllPlayers": [
            "PERSON_ID",
            "DISPLAY_LAST_COMMA_FIRST",
            "DISPLAY_FIRST_LAST",
            "ROSTERSTATUS",
            "FROM_YEAR",
            "TO_YEAR",
            "PLAYERCODE",
            "TEAM_ID",
            "TEAM_CITY",
            "TEAM_NAME",
            "TEAM_ABBREVIATION",
            "TEAM_CODE",
            "GAMES_PLAYED_FLAG",
            "OTHERLEAGUE_EXPERIENCE_CH"
        ]
    },
    "endpoint": "CommonAllPlayers",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [],
    "parameter_patterns": {
        "IsOnlyCurrentSeason": null,
        "LeagueID": "^\\d{2}$",
        "Season": null
    },
    "parameters": [
        "IsOnlyCurrentSeason",
        "LeagueID",
        "Season"
    ],
    "required_parameters": [
        "IsOnlyCurrentSeason",
        "LeagueID",
        "Season"
    ],
    "status": "success"
}
```

Last validated 2020-08-16