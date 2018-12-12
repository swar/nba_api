# CommonAllPlayers
##### [nba_api/stats/endpoints/commonallplayers.py](https://github.com/swar/nba_api/blob/master/nba_api/stats/endpoints/commonallplayers.py)

##### Endpoint URL
>[https://stats.nba.com/stats/commonallplayers](https://stats.nba.com/stats/commonallplayers)

##### Valid URL
>[https://stats.nba.com/stats/commonallplayers?IsOnlyCurrentSeason=0&LeagueID=00&Season=2018-19](https://stats.nba.com/stats/commonallplayers?IsOnlyCurrentSeason=0&LeagueID=00&Season=2018-19)

## Parameters
API Parameter Name | Python Parameter Class | Python Parameter Variable | Pattern | Required | Nullable
------------ | ------------ | ------------ | :-----------: | :---: | :---:
_**IsOnlyCurrentSeason**_ | [IsOnlyCurrentSeason](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#IsOnlyCurrentSeason) | is_only_current_season |  | `Y` |  | 
_**LeagueID**_ | [LeagueID](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id | `^\d{2}$` | `Y` |  | 
_**Season**_ | [Season](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season) | season | `^\d{4}-\d{2}$` | `Y` |  | 

## Data Sets
#### CommonAllPlayers `common_all_players`
```text
['PERSON_ID', 'DISPLAY_LAST_COMMA_FIRST', 'DISPLAY_FIRST_LAST', 'ROSTERSTATUS', 'FROM_YEAR', 'TO_YEAR', 'PLAYERCODE', 'TEAM_ID', 'TEAM_CITY', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'TEAM_CODE', 'GAMES_PLAYED_FLAG']
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
            "GAMES_PLAYED_FLAG"
        ]
    },
    "endpoint": "CommonAllPlayers",
    "last_validated_date": "2018-12-11",
    "nullable_parameters": [],
    "parameter_patterns": {
        "IsOnlyCurrentSeason": null,
        "LeagueID": "^\\d{2}$",
        "Season": "^\\d{4}-\\d{2}$"
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

Last validated 2018-12-11