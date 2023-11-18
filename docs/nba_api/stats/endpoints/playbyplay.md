# PlayByPlay
##### [nba_api/stats/endpoints/playbyplay.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/playbyplay.py)

##### Endpoint URL
>[https://stats.nba.com/stats/playbyplay](https://stats.nba.com/stats/playbyplay)

##### Valid URL
>[https://stats.nba.com/stats/playbyplay?EndPeriod=1&GameID=0021700807&StartPeriod=1](https://stats.nba.com/stats/playbyplay?EndPeriod=1&GameID=0021700807&StartPeriod=1)

## Parameters
| API Parameter Name                                                                                                    | Python Parameter Variable |  Pattern   | Required | Nullable |
|-----------------------------------------------------------------------------------------------------------------------|---------------------------|:----------:|:--------:|:--------:|
| [_**EndPeriod**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EndPeriod)     | end_period                |            |   `Y`    |          | 
| [_**GameID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameID)           | game_id                   | `^\d{10}$` |   `Y`    |          | 
| [_**StartPeriod**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#StartPeriod) | start_period              |            |   `Y`    |          | 

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
    "last_validated_date": "2020-08-15",
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

Last validated 2020-08-16