# PlayerAwards
##### [nba_api/stats/endpoints/playerawards.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/playerawards.py)

##### Endpoint URL
>[https://stats.nba.com/stats/playerawards](https://stats.nba.com/stats/playerawards)

##### Valid URL
>[https://stats.nba.com/stats/playerawards?PlayerID=2544](https://stats.nba.com/stats/playerawards?PlayerID=2544)

## Parameters
| API Parameter Name                                                                                              | Python Parameter Variable | Pattern | Required | Nullable |
|-----------------------------------------------------------------------------------------------------------------|---------------------------|:-------:|:--------:|:--------:|
| [_**PlayerID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerID) | player_id                 |         |   `Y`    |          | 

## Data Sets
#### PlayerAwards `player_awards`
```text
['PERSON_ID', 'FIRST_NAME', 'LAST_NAME', 'TEAM', 'DESCRIPTION', 'ALL_NBA_TEAM_NUMBER', 'SEASON', 'MONTH', 'WEEK', 'CONFERENCE', 'TYPE', 'SUBTYPE1', 'SUBTYPE2', 'SUBTYPE3']
```


## JSON
```json
{
    "data_sets": {
        "PlayerAwards": [
            "PERSON_ID",
            "FIRST_NAME",
            "LAST_NAME",
            "TEAM",
            "DESCRIPTION",
            "ALL_NBA_TEAM_NUMBER",
            "SEASON",
            "MONTH",
            "WEEK",
            "CONFERENCE",
            "TYPE",
            "SUBTYPE1",
            "SUBTYPE2",
            "SUBTYPE3"
        ]
    },
    "endpoint": "PlayerAwards",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [],
    "parameter_patterns": {
        "PlayerID": null
    },
    "parameters": [
        "PlayerID"
    ],
    "required_parameters": [
        "PlayerID"
    ],
    "status": "success"
}
```

Last validated 2020-08-16