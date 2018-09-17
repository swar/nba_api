# PlayByPlay

##### Endpoint URL
>[https://stats.nba.com/stats/playbyplay](https://stats.nba.com/stats/playbyplay)

##### Valid URL
>[https://stats.nba.com/stats/playbyplay?EndPeriod=1&GameID=0021700807&StartPeriod=1](https://stats.nba.com/stats/playbyplay?EndPeriod=1&GameID=0021700807&StartPeriod=1)

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
['GAME_ID', 'EVENTNUM', 'EVENTMSGTYPE', 'EVENTMSGACTIONTYPE', 'PERIOD', 'WCTIMESTRING', 'PCTIMESTRING', 'HOMEDESCRIPTION', 'NEUTRALDESCRIPTION', 'VISITORDESCRIPTION', 'SCORE', 'SCOREMARGIN']
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
            "SCOREMARGIN"
        ]
    },
    "endpoint": "PlayByPlay",
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

Last validated 2018-09-16