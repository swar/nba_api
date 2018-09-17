# CommonAllPlayers

##### Endpoint URL
>[https://stats.nba.com/stats/commonallplayers](https://stats.nba.com/stats/commonallplayers)

##### Valid URL
>[https://stats.nba.com/stats/commonallplayers?IsOnlyCurrentSeason=0&LeagueID=00&Season=2017-18](https://stats.nba.com/stats/commonallplayers?IsOnlyCurrentSeason=0&LeagueID=00&Season=2017-18)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**IsOnlyCurrentSeason**_ |  | `Y` |  | 
_**LeagueID**_ | `^\d{2}$` | `Y` |  | 
_**Season**_ | `^\d{4}-\d{2}$` | `Y` |  | 

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

Last validated 2018-09-16