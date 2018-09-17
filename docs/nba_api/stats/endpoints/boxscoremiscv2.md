# BoxScoreMiscV2

##### Endpoint URL
>[https://stats.nba.com/stats/boxscoremiscv2](https://stats.nba.com/stats/boxscoremiscv2)

##### Valid URL
>[https://stats.nba.com/stats/boxscoremiscv2?EndPeriod=1&EndRange=0&GameID=0021700807&RangeType=0&StartPeriod=1&StartRange=0](https://stats.nba.com/stats/boxscoremiscv2?EndPeriod=1&EndRange=0&GameID=0021700807&RangeType=0&StartPeriod=1&StartRange=0)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**EndPeriod**_ |  | `Y` |  | 
_**EndRange**_ |  | `Y` |  | 
_**GameID**_ | `^\d{10}$` | `Y` |  | 
_**RangeType**_ |  | `Y` |  | 
_**StartPeriod**_ |  | `Y` |  | 
_**StartRange**_ |  | `Y` |  | 

## Data Sets
#### sqlPlayersMisc `sql_players_misc`
```text
['GAME_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_CITY', 'PLAYER_ID', 'PLAYER_NAME', 'START_POSITION', 'COMMENT', 'MIN', 'PTS_OFF_TOV', 'PTS_2ND_CHANCE', 'PTS_FB', 'PTS_PAINT', 'OPP_PTS_OFF_TOV', 'OPP_PTS_2ND_CHANCE', 'OPP_PTS_FB', 'OPP_PTS_PAINT', 'BLK', 'BLKA', 'PF', 'PFD']
```

#### sqlTeamsMisc `sql_teams_misc`
```text
['GAME_ID', 'TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'TEAM_CITY', 'MIN', 'PTS_OFF_TOV', 'PTS_2ND_CHANCE', 'PTS_FB', 'PTS_PAINT', 'OPP_PTS_OFF_TOV', 'OPP_PTS_2ND_CHANCE', 'OPP_PTS_FB', 'OPP_PTS_PAINT', 'BLK', 'BLKA', 'PF', 'PFD']
```


## JSON
```json
{
    "data_sets": {
        "sqlPlayersMisc": [
            "GAME_ID",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_CITY",
            "PLAYER_ID",
            "PLAYER_NAME",
            "START_POSITION",
            "COMMENT",
            "MIN",
            "PTS_OFF_TOV",
            "PTS_2ND_CHANCE",
            "PTS_FB",
            "PTS_PAINT",
            "OPP_PTS_OFF_TOV",
            "OPP_PTS_2ND_CHANCE",
            "OPP_PTS_FB",
            "OPP_PTS_PAINT",
            "BLK",
            "BLKA",
            "PF",
            "PFD"
        ],
        "sqlTeamsMisc": [
            "GAME_ID",
            "TEAM_ID",
            "TEAM_NAME",
            "TEAM_ABBREVIATION",
            "TEAM_CITY",
            "MIN",
            "PTS_OFF_TOV",
            "PTS_2ND_CHANCE",
            "PTS_FB",
            "PTS_PAINT",
            "OPP_PTS_OFF_TOV",
            "OPP_PTS_2ND_CHANCE",
            "OPP_PTS_FB",
            "OPP_PTS_PAINT",
            "BLK",
            "BLKA",
            "PF",
            "PFD"
        ]
    },
    "endpoint": "BoxScoreMiscV2",
    "nullable_parameters": [],
    "parameter_patterns": {
        "EndPeriod": null,
        "EndRange": null,
        "GameID": "^\\d{10}$",
        "RangeType": null,
        "StartPeriod": null,
        "StartRange": null
    },
    "parameters": [
        "EndPeriod",
        "EndRange",
        "GameID",
        "RangeType",
        "StartPeriod",
        "StartRange"
    ],
    "required_parameters": [
        "EndPeriod",
        "EndRange",
        "GameID",
        "RangeType",
        "StartPeriod",
        "StartRange"
    ],
    "status": "success"
}
```

Last validated 2018-09-16