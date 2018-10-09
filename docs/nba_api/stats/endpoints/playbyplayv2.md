# PlayByPlayV2

##### Endpoint URL
>[https://stats.nba.com/stats/playbyplayv2](https://stats.nba.com/stats/playbyplayv2)

##### Valid URL
>[https://stats.nba.com/stats/playbyplayv2?EndPeriod=1&GameID=0021700807&StartPeriod=1](https://stats.nba.com/stats/playbyplayv2?EndPeriod=1&GameID=0021700807&StartPeriod=1)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**EndPeriod**_ |  | `Y` |  | 
_**GameID**_ | `^\d{10}$` | `Y` |  | 
_**StartPeriod**_ |  | `Y` |  | 

## Data Sets
#### AvailableVideo `available_video`
```text
['VIDEO_AVAILABLE_FLAG']
```

#### PlayByPlay `play_by_play`
```text
['GAME_ID', 'EVENTNUM', 'EVENTMSGTYPE', 'EVENTMSGACTIONTYPE', 'PERIOD', 'WCTIMESTRING', 'PCTIMESTRING', 'HOMEDESCRIPTION', 'NEUTRALDESCRIPTION', 'VISITORDESCRIPTION', 'SCORE', 'SCOREMARGIN', 'PERSON1TYPE', 'PLAYER1_ID', 'PLAYER1_NAME', 'PLAYER1_TEAM_ID', 'PLAYER1_TEAM_CITY', 'PLAYER1_TEAM_NICKNAME', 'PLAYER1_TEAM_ABBREVIATION', 'PERSON2TYPE', 'PLAYER2_ID', 'PLAYER2_NAME', 'PLAYER2_TEAM_ID', 'PLAYER2_TEAM_CITY', 'PLAYER2_TEAM_NICKNAME', 'PLAYER2_TEAM_ABBREVIATION', 'PERSON3TYPE', 'PLAYER3_ID', 'PLAYER3_NAME', 'PLAYER3_TEAM_ID', 'PLAYER3_TEAM_CITY', 'PLAYER3_TEAM_NICKNAME', 'PLAYER3_TEAM_ABBREVIATION']
```


## JSON
```json
{
    "data_sets": {
        "AvailableVideo": [
            "VIDEO_AVAILABLE_FLAG"
        ],
        "PlayByPlay": [
            "GAME_ID",
            "EVENTNUM",
            "EVENTMSGTYPE",
            "EVENTMSGACTIONTYPE",
            "PERIOD",
            "WCTIMESTRING",
            "PCTIMESTRING",
            "HOMEDESCRIPTION",
            "NEUTRALDESCRIPTION",
            "VISITORDESCRIPTION",
            "SCORE",
            "SCOREMARGIN",
            "PERSON1TYPE",
            "PLAYER1_ID",
            "PLAYER1_NAME",
            "PLAYER1_TEAM_ID",
            "PLAYER1_TEAM_CITY",
            "PLAYER1_TEAM_NICKNAME",
            "PLAYER1_TEAM_ABBREVIATION",
            "PERSON2TYPE",
            "PLAYER2_ID",
            "PLAYER2_NAME",
            "PLAYER2_TEAM_ID",
            "PLAYER2_TEAM_CITY",
            "PLAYER2_TEAM_NICKNAME",
            "PLAYER2_TEAM_ABBREVIATION",
            "PERSON3TYPE",
            "PLAYER3_ID",
            "PLAYER3_NAME",
            "PLAYER3_TEAM_ID",
            "PLAYER3_TEAM_CITY",
            "PLAYER3_TEAM_NICKNAME",
            "PLAYER3_TEAM_ABBREVIATION"
        ]
    },
    "endpoint": "PlayByPlayV2",
    "last_validated_date": "2018-10-08",
    "nullable_parameters": [],
    "parameter_patterns": {
        "EndPeriod": null,
        "GameID": "^\\d{10}$",
        "StartPeriod": null
    },
    "parameters": [
        "EndPeriod",
        "GameID",
        "StartPeriod"
    ],
    "required_parameters": [
        "EndPeriod",
        "GameID",
        "StartPeriod"
    ],
    "status": "success"
}
```

Last validated 2018-10-08