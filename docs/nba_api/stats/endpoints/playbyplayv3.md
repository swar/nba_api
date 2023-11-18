# PlayByPlayV3
##### [nba_apiv3/stats/endpoints/playbyplayv3.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/playbyplayv3.py)

##### Endpoint URL
>[https://stats.nba.com/stats/playbyplayv3](https://stats.nba.com/stats/playbyplayv3)

##### Valid URL
>[https://stats.nba.com/stats/playbyplayv3?EndPeriod=1&GameID=0021700807&StartPeriod=1](https://stats.nba.com/stats/playbyplayv3?EndPeriod=1&GameID=0021700807&StartPeriod=1)

## Parameters
| API Parameter Name                                                                                                            | Python Parameter Variable |  Pattern   | Required | Nullable |
|-------------------------------------------------------------------------------------------------------------------------------|---------------------------|:----------:|:--------:|:--------:|
| [_**EndPeriod**_](https://github.com/shufinskiy/nba_apiv3/blob/master/docs/nba_api/stats/library/parameters.md#EndPeriod)     | end_period                |            |   `Y`    |          | 
| [_**GameID**_](https://github.com/shufinskiy/nba_apiv3/blob/master/docs/nba_api/stats/library/parameters.md#GameID)           | game_id                   | `^\d{10}$` |   `Y`    |          | 
| [_**StartPeriod**_](https://github.com/shufinskiy/nba_apiv3/blob/master/docs/nba_api/stats/library/parameters.md#StartPeriod) | start_period              |            |   `Y`    |          | 

## Data Sets
#### AvailableVideo `available_video`
```text
['videoAvailable']
```

#### PlayByPlay `play_by_play`
```text
['gameId', 'actionNumber', 'clock', 'period', 'teamId', 'teamTricode', 'personId', 'playerName', 'playerNameI', 'xLegacy', 'yLegacy', 'shotDistance', 'shotResult', 'isFieldGoal', 'scoreHome', 'scoreAway', 'pointsTotal', 'location', 'description', 'actionType', 'subType', 'videoAvailable', 'actionId']
```


## JSON
```json
{
    "data_sets": {
        "AvailableVideo": [
            "videoAvailable"
        ],
        "PlayByPlay": [
            "gameId", 
            "actionNumber", 
            "clock",
            "period",
            "teamId",
            "teamTricode",
            "personId",
            "playerName",
            "playerNameI",
            "xLegacy",
            "yLegacy",
            "shotDistance",
            "shotResult",
            "isFieldGoal",
            "scoreHome",
            "scoreAway",
            "pointsTotal", 
            "location",
            "description",
            "actionType",
            "subType",
            "videoAvailable",
            "actionId"
        ]
    },
    "endpoint": "PlayByPlayV3",
    "last_validated_date": "2023-09-14",
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

Last validated 2023-09-14