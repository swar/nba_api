# DraftCombineSpotShooting
##### [nba_api/stats/endpoints/draftcombinespotshooting.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/draftcombinespotshooting.py)

##### Endpoint URL
>[https://stats.nba.com/stats/draftcombinespotshooting](https://stats.nba.com/stats/draftcombinespotshooting)

##### Valid URL
>[https://stats.nba.com/stats/draftcombinespotshooting?LeagueID=00&SeasonYear=2019](https://stats.nba.com/stats/draftcombinespotshooting?LeagueID=00&SeasonYear=2019)

## Parameters
| API Parameter Name                                                                                                  | Python Parameter Variable | Pattern | Required | Nullable |
|---------------------------------------------------------------------------------------------------------------------|---------------------------|:-------:|:--------:|:--------:|
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)     | league_id                 |         |   `Y`    |          | 
| [_**SeasonYear**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonYear) | season_year               |         |   `Y`    |          | 

## Data Sets
#### Results `results`
```text
['TEMP_PLAYER_ID', 'PLAYER_ID', 'FIRST_NAME', 'LAST_NAME', 'PLAYER_NAME', 'POSITION', 'FIFTEEN_CORNER_LEFT_MADE', 'FIFTEEN_CORNER_LEFT_ATTEMPT', 'FIFTEEN_CORNER_LEFT_PCT', 'FIFTEEN_BREAK_LEFT_MADE', 'FIFTEEN_BREAK_LEFT_ATTEMPT', 'FIFTEEN_BREAK_LEFT_PCT', 'FIFTEEN_TOP_KEY_MADE', 'FIFTEEN_TOP_KEY_ATTEMPT', 'FIFTEEN_TOP_KEY_PCT', 'FIFTEEN_BREAK_RIGHT_MADE', 'FIFTEEN_BREAK_RIGHT_ATTEMPT', 'FIFTEEN_BREAK_RIGHT_PCT', 'FIFTEEN_CORNER_RIGHT_MADE', 'FIFTEEN_CORNER_RIGHT_ATTEMPT', 'FIFTEEN_CORNER_RIGHT_PCT', 'COLLEGE_CORNER_LEFT_MADE', 'COLLEGE_CORNER_LEFT_ATTEMPT', 'COLLEGE_CORNER_LEFT_PCT', 'COLLEGE_BREAK_LEFT_MADE', 'COLLEGE_BREAK_LEFT_ATTEMPT', 'COLLEGE_BREAK_LEFT_PCT', 'COLLEGE_TOP_KEY_MADE', 'COLLEGE_TOP_KEY_ATTEMPT', 'COLLEGE_TOP_KEY_PCT', 'COLLEGE_BREAK_RIGHT_MADE', 'COLLEGE_BREAK_RIGHT_ATTEMPT', 'COLLEGE_BREAK_RIGHT_PCT', 'COLLEGE_CORNER_RIGHT_MADE', 'COLLEGE_CORNER_RIGHT_ATTEMPT', 'COLLEGE_CORNER_RIGHT_PCT', 'NBA_CORNER_LEFT_MADE', 'NBA_CORNER_LEFT_ATTEMPT', 'NBA_CORNER_LEFT_PCT', 'NBA_BREAK_LEFT_MADE', 'NBA_BREAK_LEFT_ATTEMPT', 'NBA_BREAK_LEFT_PCT', 'NBA_TOP_KEY_MADE', 'NBA_TOP_KEY_ATTEMPT', 'NBA_TOP_KEY_PCT', 'NBA_BREAK_RIGHT_MADE', 'NBA_BREAK_RIGHT_ATTEMPT', 'NBA_BREAK_RIGHT_PCT', 'NBA_CORNER_RIGHT_MADE', 'NBA_CORNER_RIGHT_ATTEMPT', 'NBA_CORNER_RIGHT_PCT']
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
            "FIFTEEN_CORNER_LEFT_MADE",
            "FIFTEEN_CORNER_LEFT_ATTEMPT",
            "FIFTEEN_CORNER_LEFT_PCT",
            "FIFTEEN_BREAK_LEFT_MADE",
            "FIFTEEN_BREAK_LEFT_ATTEMPT",
            "FIFTEEN_BREAK_LEFT_PCT",
            "FIFTEEN_TOP_KEY_MADE",
            "FIFTEEN_TOP_KEY_ATTEMPT",
            "FIFTEEN_TOP_KEY_PCT",
            "FIFTEEN_BREAK_RIGHT_MADE",
            "FIFTEEN_BREAK_RIGHT_ATTEMPT",
            "FIFTEEN_BREAK_RIGHT_PCT",
            "FIFTEEN_CORNER_RIGHT_MADE",
            "FIFTEEN_CORNER_RIGHT_ATTEMPT",
            "FIFTEEN_CORNER_RIGHT_PCT",
            "COLLEGE_CORNER_LEFT_MADE",
            "COLLEGE_CORNER_LEFT_ATTEMPT",
            "COLLEGE_CORNER_LEFT_PCT",
            "COLLEGE_BREAK_LEFT_MADE",
            "COLLEGE_BREAK_LEFT_ATTEMPT",
            "COLLEGE_BREAK_LEFT_PCT",
            "COLLEGE_TOP_KEY_MADE",
            "COLLEGE_TOP_KEY_ATTEMPT",
            "COLLEGE_TOP_KEY_PCT",
            "COLLEGE_BREAK_RIGHT_MADE",
            "COLLEGE_BREAK_RIGHT_ATTEMPT",
            "COLLEGE_BREAK_RIGHT_PCT",
            "COLLEGE_CORNER_RIGHT_MADE",
            "COLLEGE_CORNER_RIGHT_ATTEMPT",
            "COLLEGE_CORNER_RIGHT_PCT",
            "NBA_CORNER_LEFT_MADE",
            "NBA_CORNER_LEFT_ATTEMPT",
            "NBA_CORNER_LEFT_PCT",
            "NBA_BREAK_LEFT_MADE",
            "NBA_BREAK_LEFT_ATTEMPT",
            "NBA_BREAK_LEFT_PCT",
            "NBA_TOP_KEY_MADE",
            "NBA_TOP_KEY_ATTEMPT",
            "NBA_TOP_KEY_PCT",
            "NBA_BREAK_RIGHT_MADE",
            "NBA_BREAK_RIGHT_ATTEMPT",
            "NBA_BREAK_RIGHT_PCT",
            "NBA_CORNER_RIGHT_MADE",
            "NBA_CORNER_RIGHT_ATTEMPT",
            "NBA_CORNER_RIGHT_PCT"
        ]
    },
    "endpoint": "DraftCombineSpotShooting",
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