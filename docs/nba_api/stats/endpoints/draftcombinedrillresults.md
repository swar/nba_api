# DraftCombineDrillResults
##### [nba_api/stats/endpoints/draftcombinedrillresults.py](https://github.com/swar/nba_api/blob/master/nba_api/stats/endpoints/draftcombinedrillresults.py)

##### Endpoint URL
>[https://stats.nba.com/stats/draftcombinedrillresults](https://stats.nba.com/stats/draftcombinedrillresults)

##### Valid URL
>[https://stats.nba.com/stats/draftcombinedrillresults?LeagueID=00&SeasonYear=2018](https://stats.nba.com/stats/draftcombinedrillresults?LeagueID=00&SeasonYear=2018)

## Parameters
API Parameter Name | Python Parameter Variable | Pattern | Required | Nullable
------------ | ------------ | :-----------: | :---: | :---:
[_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id | `^(00)\|(10)\|(20)$` | `Y` |  | 
[_**SeasonYear**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonYear) | season_year |  | `Y` |  | 

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
    "last_validated_date": "2019-04-07",
    "nullable_parameters": [],
    "parameter_patterns": {
        "LeagueID": "^(00)|(10)|(20)$",
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

Last validated 2019-04-07