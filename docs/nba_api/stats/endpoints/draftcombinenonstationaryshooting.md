# DraftCombineNonStationaryShooting
##### [nba_api/stats/endpoints/draftcombinenonstationaryshooting.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/draftcombinenonstationaryshooting.py)

##### Endpoint URL
>[https://stats.nba.com/stats/draftcombinenonstationaryshooting](https://stats.nba.com/stats/draftcombinenonstationaryshooting)

##### Valid URL
>[https://stats.nba.com/stats/draftcombinenonstationaryshooting?LeagueID=00&SeasonYear=2019](https://stats.nba.com/stats/draftcombinenonstationaryshooting?LeagueID=00&SeasonYear=2019)

## Parameters
| API Parameter Name                                                                                                  | Python Parameter Variable | Pattern | Required | Nullable |
|---------------------------------------------------------------------------------------------------------------------|---------------------------|:-------:|:--------:|:--------:|
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)     | league_id                 |         |   `Y`    |          | 
| [_**SeasonYear**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonYear) | season_year               |         |   `Y`    |          | 

## Data Sets
#### Results `results`
```text
['TEMP_PLAYER_ID', 'PLAYER_ID', 'FIRST_NAME', 'LAST_NAME', 'PLAYER_NAME', 'POSITION', 'OFF_DRIB_FIFTEEN_BREAK_LEFT_MADE', 'OFF_DRIB_FIFTEEN_BREAK_LEFT_ATTEMPT', 'OFF_DRIB_FIFTEEN_BREAK_LEFT_PCT', 'OFF_DRIB_FIFTEEN_TOP_KEY_MADE', 'OFF_DRIB_FIFTEEN_TOP_KEY_ATTEMPT', 'OFF_DRIB_FIFTEEN_TOP_KEY_PCT', 'OFF_DRIB_FIFTEEN_BREAK_RIGHT_MADE', 'OFF_DRIB_FIFTEEN_BREAK_RIGHT_ATTEMPT', 'OFF_DRIB_FIFTEEN_BREAK_RIGHT_PCT', 'OFF_DRIB_COLLEGE_BREAK_LEFT_MADE', 'OFF_DRIB_COLLEGE_BREAK_LEFT_ATTEMPT', 'OFF_DRIB_COLLEGE_BREAK_LEFT_PCT', 'OFF_DRIB_COLLEGE_TOP_KEY_MADE', 'OFF_DRIB_COLLEGE_TOP_KEY_ATTEMPT', 'OFF_DRIB_COLLEGE_TOP_KEY_PCT', 'OFF_DRIB_COLLEGE_BREAK_RIGHT_MADE', 'OFF_DRIB_COLLEGE_BREAK_RIGHT_ATTEMPT', 'OFF_DRIB_COLLEGE_BREAK_RIGHT_PCT', 'ON_MOVE_FIFTEEN_MADE', 'ON_MOVE_FIFTEEN_ATTEMPT', 'ON_MOVE_FIFTEEN_PCT', 'ON_MOVE_COLLEGE_MADE', 'ON_MOVE_COLLEGE_ATTEMPT', 'ON_MOVE_COLLEGE_PCT']
```


## JSON
```json
{
    "data_sets": {
        "Results": [
            "TEMP_PLAYER_ID",
            "PLAYER_ID",
            "FIRST_NAME",
            "LAST_NAME",
            "PLAYER_NAME",
            "POSITION",
            "OFF_DRIB_FIFTEEN_BREAK_LEFT_MADE",
            "OFF_DRIB_FIFTEEN_BREAK_LEFT_ATTEMPT",
            "OFF_DRIB_FIFTEEN_BREAK_LEFT_PCT",
            "OFF_DRIB_FIFTEEN_TOP_KEY_MADE",
            "OFF_DRIB_FIFTEEN_TOP_KEY_ATTEMPT",
            "OFF_DRIB_FIFTEEN_TOP_KEY_PCT",
            "OFF_DRIB_FIFTEEN_BREAK_RIGHT_MADE",
            "OFF_DRIB_FIFTEEN_BREAK_RIGHT_ATTEMPT",
            "OFF_DRIB_FIFTEEN_BREAK_RIGHT_PCT",
            "OFF_DRIB_COLLEGE_BREAK_LEFT_MADE",
            "OFF_DRIB_COLLEGE_BREAK_LEFT_ATTEMPT",
            "OFF_DRIB_COLLEGE_BREAK_LEFT_PCT",
            "OFF_DRIB_COLLEGE_TOP_KEY_MADE",
            "OFF_DRIB_COLLEGE_TOP_KEY_ATTEMPT",
            "OFF_DRIB_COLLEGE_TOP_KEY_PCT",
            "OFF_DRIB_COLLEGE_BREAK_RIGHT_MADE",
            "OFF_DRIB_COLLEGE_BREAK_RIGHT_ATTEMPT",
            "OFF_DRIB_COLLEGE_BREAK_RIGHT_PCT",
            "ON_MOVE_FIFTEEN_MADE",
            "ON_MOVE_FIFTEEN_ATTEMPT",
            "ON_MOVE_FIFTEEN_PCT",
            "ON_MOVE_COLLEGE_MADE",
            "ON_MOVE_COLLEGE_ATTEMPT",
            "ON_MOVE_COLLEGE_PCT"
        ]
    },
    "endpoint": "DraftCombineNonStationaryShooting",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [],
    "parameter_patterns": {
        "LeagueID": null,
        "SeasonYear": null
    },
    "parameters": [
        "LeagueID",
        "SeasonYear"
    ],
    "required_parameters": [
        "LeagueID",
        "SeasonYear"
    ],
    "status": "success"
}
```

Last validated 2020-08-16