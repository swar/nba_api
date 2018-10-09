# PlayerAwards

##### Endpoint URL
>[https://stats.nba.com/stats/playerawards](https://stats.nba.com/stats/playerawards)

##### Valid URL
>[https://stats.nba.com/stats/playerawards?PlayerID=2544](https://stats.nba.com/stats/playerawards?PlayerID=2544)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**PlayerID**_ |  | `Y` |  | 

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
    "last_validated_date": "2018-10-08",
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

Last validated 2018-10-08