# DraftCombineNonStationaryShooting

##### Endpoint URL
>[https://stats.nba.com/stats/draftcombinenonstationaryshooting](https://stats.nba.com/stats/draftcombinenonstationaryshooting)

##### Valid URL
>[https://stats.nba.com/stats/draftcombinenonstationaryshooting?LeagueID=00&SeasonYear=2017-18](https://stats.nba.com/stats/draftcombinenonstationaryshooting?LeagueID=00&SeasonYear=2017-18)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**LeagueID**_ | `^(00)\|(10)\|(20)$` | `Y` |  | 
_**SeasonYear**_ | `^\d{4}-\d{2}$` | `Y` |  | 

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
    "last_validated_date": "2018-10-08",
    "nullable_parameters": [],
    "parameter_patterns": {
        "LeagueID": "^(00)|(10)|(20)$",
        "SeasonYear": "^\\d{4}-\\d{2}$"
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

Last validated 2018-10-08