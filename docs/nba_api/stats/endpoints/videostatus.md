# VideoStatus

##### Endpoint URL
>[https://stats.nba.com/stats/videostatus](https://stats.nba.com/stats/videostatus)

##### Valid URL
>[https://stats.nba.com/stats/videostatus?GameDate=2018-09-16&LeagueID=00](https://stats.nba.com/stats/videostatus?GameDate=2018-09-16&LeagueID=00)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**GameDate**_ |  | `Y` |  | 
_**LeagueID**_ | `^\d{2}$` | `Y` |  | 

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

Last validated 2018-09-16