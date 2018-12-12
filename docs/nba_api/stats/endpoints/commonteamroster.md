# CommonTeamRoster
##### [nba_api/stats/endpoints/commonteamroster.py](https://github.com/swar/nba_api/blob/master/nba_api/stats/endpoints/commonteamroster.py)

##### Endpoint URL
>[https://stats.nba.com/stats/commonteamroster](https://stats.nba.com/stats/commonteamroster)

##### Valid URL
>[https://stats.nba.com/stats/commonteamroster?LeagueID=&Season=2018-19&TeamID=1610612739](https://stats.nba.com/stats/commonteamroster?LeagueID=&Season=2018-19&TeamID=1610612739)

## Parameters
API Parameter Name | Python Parameter Variable | Pattern | Required | Nullable
------------ | ------------ | :-----------: | :---: | :---:
[_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season) | season | `^\d{4}-\d{2}$` | `Y` |  | 
[_**TeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TeamID) | team_id |  | `Y` |  | 
[_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id_nullable | `(00)\|(20)\|(10)` |  | `Y` | 

## Data Sets
#### Coaches `coaches`
```text
['TEAM_ID', 'SEASON', 'COACH_ID', 'FIRST_NAME', 'LAST_NAME', 'COACH_NAME', 'COACH_CODE', 'IS_ASSISTANT', 'COACH_TYPE', 'SCHOOL', 'SORT_SEQUENCE']
```

#### CommonTeamRoster `common_team_roster`
```text
['TeamID', 'SEASON', 'LeagueID', 'PLAYER', 'NUM', 'POSITION', 'HEIGHT', 'WEIGHT', 'BIRTH_DATE', 'AGE', 'EXP', 'SCHOOL', 'PLAYER_ID']
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
            "COACH_CODE",
            "IS_ASSISTANT",
            "COACH_TYPE",
            "SCHOOL",
            "SORT_SEQUENCE"
        ],
        "CommonTeamRoster": [
            "TeamID",
            "SEASON",
            "LeagueID",
            "PLAYER",
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
    "last_validated_date": "2018-12-11",
    "nullable_parameters": [
        "LeagueID"
    ],
    "parameter_patterns": {
        "LeagueID": "(00)|(20)|(10)",
        "Season": "^\\d{4}-\\d{2}$",
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

Last validated 2018-12-11