# DraftCombinePlayerAnthro

##### Endpoint URL
>[https://stats.nba.com/stats/draftcombineplayeranthro](https://stats.nba.com/stats/draftcombineplayeranthro)

##### Valid URL
>[https://stats.nba.com/stats/draftcombineplayeranthro?LeagueID=00&SeasonYear=2017-18](https://stats.nba.com/stats/draftcombineplayeranthro?LeagueID=00&SeasonYear=2017-18)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**LeagueID**_ | `^(00)\|(10)\|(20)$` | `Y` |  | 
_**SeasonYear**_ | `^\d{4}-\d{2}$` | `Y` |  | 

## Data Sets
#### Results `results`
```text
['TEMP_PLAYER_ID', 'PLAYER_ID', 'FIRST_NAME', 'LAST_NAME', 'PLAYER_NAME', 'POSITION', 'HEIGHT_WO_SHOES', 'HEIGHT_WO_SHOES_FT_IN', 'HEIGHT_W_SHOES', 'HEIGHT_W_SHOES_FT_IN', 'WEIGHT', 'WINGSPAN', 'WINGSPAN_FT_IN', 'STANDING_REACH', 'STANDING_REACH_FT_IN', 'BODY_FAT_PCT', 'HAND_LENGTH', 'HAND_WIDTH']
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
            "HEIGHT_WO_SHOES",
            "HEIGHT_WO_SHOES_FT_IN",
            "HEIGHT_W_SHOES",
            "HEIGHT_W_SHOES_FT_IN",
            "WEIGHT",
            "WINGSPAN",
            "WINGSPAN_FT_IN",
            "STANDING_REACH",
            "STANDING_REACH_FT_IN",
            "BODY_FAT_PCT",
            "HAND_LENGTH",
            "HAND_WIDTH"
        ]
    },
    "endpoint": "DraftCombinePlayerAnthro",
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