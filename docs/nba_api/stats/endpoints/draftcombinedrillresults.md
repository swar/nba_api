# DraftCombineDrillResults

##### Endpoint URL
>[https://stats.nba.com/stats/draftcombinedrillresults](https://stats.nba.com/stats/draftcombinedrillresults)

##### Valid URL
>[https://stats.nba.com/stats/draftcombinedrillresults?LeagueID=00&SeasonYear=2017-18](https://stats.nba.com/stats/draftcombinedrillresults?LeagueID=00&SeasonYear=2017-18)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**LeagueID**_ | `^(00)|(10)|(20)$` | `Y` |  | 
_**SeasonYear**_ | `^\d{4}-\d{2}$` | `Y` |  | 

## Data Sets
#### Results `results`
```text
['TEMP_PLAYER_ID', 'PLAYER_ID', 'FIRST_NAME', 'LAST_NAME', 'PLAYER_NAME', 'POSITION', 'STANDING_VERTICAL_LEAP', 'MAX_VERTICAL_LEAP', 'LANE_AGILITY_TIME', 'MODIFIED_LANE_AGILITY_TIME', 'THREE_QUARTER_SPRINT', 'BENCH_PRESS']
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
            "STANDING_VERTICAL_LEAP",
            "MAX_VERTICAL_LEAP",
            "LANE_AGILITY_TIME",
            "MODIFIED_LANE_AGILITY_TIME",
            "THREE_QUARTER_SPRINT",
            "BENCH_PRESS"
        ]
    },
    "endpoint": "DraftCombineDrillResults",
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

Last validated 2018-09-16