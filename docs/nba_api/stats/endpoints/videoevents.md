# VideoEvents
##### [nba_api/stats/endpoints/videoevents.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/videoevents.py)

##### Endpoint URL
>[https://stats.nba.com/stats/videoevents](https://stats.nba.com/stats/videoevents)

##### Valid URL
>[https://stats.nba.com/stats/videoevents?GameEventID=0&GameID=0021700807](https://stats.nba.com/stats/videoevents?GameEventID=0&GameID=0021700807)

## Parameters
| API Parameter Name                                                                                                    | Python Parameter Variable |    Pattern    | Required | Nullable |
|-----------------------------------------------------------------------------------------------------------------------|---------------------------|:-------------:|:--------:|:--------:|
| [_**GameEventID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameEventID) | game_event_id             |               |   `Y`    |          | 
| [_**GameID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameID)           | game_id                   | `^(\d{10})?$` |   `Y`    |          | 

## Data Sets


## JSON
```json
{
    "data_sets": {},
    "endpoint": "VideoEvents",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [],
    "parameter_patterns": {
        "GameEventID": null,
        "GameID": "^(\\d{10})?$"
    },
    "parameters": [
        "GameEventID",
        "GameID"
    ],
    "required_parameters": [
        "GameEventID",
        "GameID"
    ],
    "status": "success"
}
```

Last validated 2020-08-16