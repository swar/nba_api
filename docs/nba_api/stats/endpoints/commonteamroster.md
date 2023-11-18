# CommonTeamRoster
##### [nba_api/stats/endpoints/commonteamroster.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/commonteamroster.py)

##### Endpoint URL
>[https://stats.nba.com/stats/commonteamroster](https://stats.nba.com/stats/commonteamroster)

##### Valid URL
>[https://stats.nba.com/stats/commonteamroster?LeagueID=&Season=2019-20&TeamID=1610612739](https://stats.nba.com/stats/commonteamroster?LeagueID=&Season=2019-20&TeamID=1610612739)

## Parameters
| API Parameter Name                                                                                              | Python Parameter Variable | Pattern | Required | Nullable |
|-----------------------------------------------------------------------------------------------------------------|---------------------------|:-------:|:--------:|:--------:|
| [_**TeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TeamID)     | team_id                   |         |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)     | season                    |         |   `Y`    |          | 
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id_nullable        |         |          |   `Y`    | 

## Data Sets
#### Coaches `coaches`
```text
['TEAM_ID', 'SEASON', 'COACH_ID', 'FIRST_NAME', 'LAST_NAME', 'COACH_NAME', 'IS_ASSISTANT', 'COACH_TYPE', 'SORT_SEQUENCE']
```

#### CommonTeamRoster `common_team_roster`
```text
['TeamID', 'SEASON', 'LeagueID', 'PLAYER', 'PLAYER_SLUG', 'NUM', 'POSITION', 'HEIGHT', 'WEIGHT', 'BIRTH_DATE', 'AGE', 'EXP', 'SCHOOL', 'PLAYER_ID']
```


## JSON
```json
{
    "data_sets": {
        "Coaches": [
            "TEAM_ID",
            "SEASON",
            "COACH_ID",
            "FIRST_NAME",
            "LAST_NAME",
            "COACH_NAME",
            "IS_ASSISTANT",
            "COACH_TYPE",
            "SORT_SEQUENCE"
        ],
        "CommonTeamRoster": [
            "TeamID",
            "SEASON",
            "LeagueID",
            "PLAYER",
            "PLAYER_SLUG",
            "NUM",
            "POSITION",
            "HEIGHT",
            "WEIGHT",
            "BIRTH_DATE",
            "AGE",
            "EXP",
            "SCHOOL",
            "PLAYER_ID"
        ]
    },
    "endpoint": "CommonTeamRoster",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [
        "LeagueID"
    ],
    "parameter_patterns": {
        "LeagueID": null,
        "Season": null,
        "TeamID": null
    },
    "parameters": [
        "LeagueID",
        "Season",
        "TeamID"
    ],
    "required_parameters": [
        "Season",
        "TeamID"
    ],
    "status": "success"
}
```

Last validated 2020-08-16
