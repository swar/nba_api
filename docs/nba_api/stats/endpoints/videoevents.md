# VideoEvents

##### Endpoint URL
>[https://stats.nba.com/stats/videoevents](https://stats.nba.com/stats/videoevents)

##### Valid URL
>[https://stats.nba.com/stats/videoevents?GameEventID=0&GameID=0021700807](https://stats.nba.com/stats/videoevents?GameEventID=0&GameID=0021700807)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**GameEventID**_ |  | `Y` |  | 
_**GameID**_ | `^(\d{10})?$` | `Y` |  | 

## Data Sets


## JSON
```json
{
    "data_sets": {},
    "endpoint": "VideoEvents",
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

Last validated 2018-09-16