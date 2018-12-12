# VideoStatus
##### [nba_api/stats/endpoints/videostatus.py](https://github.com/swar/nba_api/blob/master/nba_api/stats/endpoints/videostatus.py)

##### Endpoint URL
>[https://stats.nba.com/stats/videostatus](https://stats.nba.com/stats/videostatus)

##### Valid URL
>[https://stats.nba.com/stats/videostatus?GameDate=2018-12-11&LeagueID=00](https://stats.nba.com/stats/videostatus?GameDate=2018-12-11&LeagueID=00)

## Parameters
API Parameter Name | Python Parameter Variable | Parameter Mapping Class | Pattern | Required | Nullable
------------ | ------------ | ------------ | :-----------: | :---: | :---:
[_**GameDate**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameDate) | game_date | GameDate |  | `Y` |  | 
[_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id | LeagueID | `^\d{2}$` | `Y` |  | 

## Data Sets
#### VideoStatus `video_status`
```text
['GAME_ID', 'GAME_DATE', 'VISITOR_TEAM_ID', 'VISITOR_TEAM_CITY', 'VISITOR_TEAM_NAME', 'VISITOR_TEAM_ABBREVIATION', 'HOME_TEAM_ID', 'HOME_TEAM_CITY', 'HOME_TEAM_NAME', 'HOME_TEAM_ABBREVIATION', 'GAME_STATUS', 'GAME_STATUS_TEXT', 'IS_AVAILABLE', 'PT_XYZ_AVAILABLE']
```


## JSON
```json
{
    "data_sets": {
        "VideoStatus": [
            "GAME_ID",
            "GAME_DATE",
            "VISITOR_TEAM_ID",
            "VISITOR_TEAM_CITY",
            "VISITOR_TEAM_NAME",
            "VISITOR_TEAM_ABBREVIATION",
            "HOME_TEAM_ID",
            "HOME_TEAM_CITY",
            "HOME_TEAM_NAME",
            "HOME_TEAM_ABBREVIATION",
            "GAME_STATUS",
            "GAME_STATUS_TEXT",
            "IS_AVAILABLE",
            "PT_XYZ_AVAILABLE"
        ]
    },
    "endpoint": "VideoStatus",
    "last_validated_date": "2018-12-11",
    "nullable_parameters": [],
    "parameter_patterns": {
        "GameDate": null,
        "LeagueID": "^\\d{2}$"
    },
    "parameters": [
        "GameDate",
        "LeagueID"
    ],
    "required_parameters": [
        "GameDate",
        "LeagueID"
    ],
    "status": "success"
}
```

Last validated 2018-12-11