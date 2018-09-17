# DraftCombineStats

##### Endpoint URL
>[https://stats.nba.com/stats/draftcombinestats](https://stats.nba.com/stats/draftcombinestats)

##### Valid URL
>[https://stats.nba.com/stats/draftcombinestats?LeagueID=00&SeasonYear=2017-18](https://stats.nba.com/stats/draftcombinestats?LeagueID=00&SeasonYear=2017-18)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**LeagueID**_ | `^(00)\|(10)\|(20)$` | `Y` |  | 
_**SeasonYear**_ | `^(\d{4}-\d{2})\|(All Time)$` | `Y` |  | 

## Data Sets
#### DraftCombineStats `draft_combine_stats`
```text
['SEASON', 'PLAYER_ID', 'FIRST_NAME', 'LAST_NAME', 'PLAYER_NAME', 'POSITION', 'HEIGHT_WO_SHOES', 'HEIGHT_WO_SHOES_FT_IN', 'HEIGHT_W_SHOES', 'HEIGHT_W_SHOES_FT_IN', 'WEIGHT', 'WINGSPAN', 'WINGSPAN_FT_IN', 'STANDING_REACH', 'STANDING_REACH_FT_IN', 'BODY_FAT_PCT', 'HAND_LENGTH', 'HAND_WIDTH', 'STANDING_VERTICAL_LEAP', 'MAX_VERTICAL_LEAP', 'LANE_AGILITY_TIME', 'MODIFIED_LANE_AGILITY_TIME', 'THREE_QUARTER_SPRINT', 'BENCH_PRESS', 'SPOT_FIFTEEN_CORNER_LEFT', 'SPOT_FIFTEEN_BREAK_LEFT', 'SPOT_FIFTEEN_TOP_KEY', 'SPOT_FIFTEEN_BREAK_RIGHT', 'SPOT_FIFTEEN_CORNER_RIGHT', 'SPOT_COLLEGE_CORNER_LEFT', 'SPOT_COLLEGE_BREAK_LEFT', 'SPOT_COLLEGE_TOP_KEY', 'SPOT_COLLEGE_BREAK_RIGHT', 'SPOT_COLLEGE_CORNER_RIGHT', 'SPOT_NBA_CORNER_LEFT', 'SPOT_NBA_BREAK_LEFT', 'SPOT_NBA_TOP_KEY', 'SPOT_NBA_BREAK_RIGHT', 'SPOT_NBA_CORNER_RIGHT', 'OFF_DRIB_FIFTEEN_BREAK_LEFT', 'OFF_DRIB_FIFTEEN_TOP_KEY', 'OFF_DRIB_FIFTEEN_BREAK_RIGHT', 'OFF_DRIB_COLLEGE_BREAK_LEFT', 'OFF_DRIB_COLLEGE_TOP_KEY', 'OFF_DRIB_COLLEGE_BREAK_RIGHT', 'ON_MOVE_FIFTEEN', 'ON_MOVE_COLLEGE']
```


## JSON
```json
{
    "data_sets": {
        "DraftCombineStats": [
            "SEASON",
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
            "HAND_WIDTH",
            "STANDING_VERTICAL_LEAP",
            "MAX_VERTICAL_LEAP",
            "LANE_AGILITY_TIME",
            "MODIFIED_LANE_AGILITY_TIME",
            "THREE_QUARTER_SPRINT",
            "BENCH_PRESS",
            "SPOT_FIFTEEN_CORNER_LEFT",
            "SPOT_FIFTEEN_BREAK_LEFT",
            "SPOT_FIFTEEN_TOP_KEY",
            "SPOT_FIFTEEN_BREAK_RIGHT",
            "SPOT_FIFTEEN_CORNER_RIGHT",
            "SPOT_COLLEGE_CORNER_LEFT",
            "SPOT_COLLEGE_BREAK_LEFT",
            "SPOT_COLLEGE_TOP_KEY",
            "SPOT_COLLEGE_BREAK_RIGHT",
            "SPOT_COLLEGE_CORNER_RIGHT",
            "SPOT_NBA_CORNER_LEFT",
            "SPOT_NBA_BREAK_LEFT",
            "SPOT_NBA_TOP_KEY",
            "SPOT_NBA_BREAK_RIGHT",
            "SPOT_NBA_CORNER_RIGHT",
            "OFF_DRIB_FIFTEEN_BREAK_LEFT",
            "OFF_DRIB_FIFTEEN_TOP_KEY",
            "OFF_DRIB_FIFTEEN_BREAK_RIGHT",
            "OFF_DRIB_COLLEGE_BREAK_LEFT",
            "OFF_DRIB_COLLEGE_TOP_KEY",
            "OFF_DRIB_COLLEGE_BREAK_RIGHT",
            "ON_MOVE_FIFTEEN",
            "ON_MOVE_COLLEGE"
        ]
    },
    "endpoint": "DraftCombineStats",
    "nullable_parameters": [],
    "parameter_patterns": {
        "LeagueID": "^(00)|(10)|(20)$",
        "SeasonYear": "^(\\d{4}-\\d{2})|(All Time)$"
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