# PlayerDashPtReb

##### Endpoint URL
>[https://stats.nba.com/stats/playerdashptreb](https://stats.nba.com/stats/playerdashptreb)

##### Valid URL
>[https://stats.nba.com/stats/playerdashptreb?DateFrom=&DateTo=&GameSegment=&LastNGames=10&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PerMode=Totals&Period=1&PlayerID=2544&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&TeamID=1610612739&VsConference=&VsDivision=](https://stats.nba.com/stats/playerdashptreb?DateFrom=&DateTo=&GameSegment=&LastNGames=10&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PerMode=Totals&Period=1&PlayerID=2544&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&TeamID=1610612739&VsConference=&VsDivision=)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**LastNGames**_ |  | `Y` |  | 
_**LeagueID**_ | `(00)\|(20)\|(10)` |  |  | 
_**Month**_ |  | `Y` |  | 
_**OpponentTeamID**_ |  | `Y` |  | 
_**PerMode**_ | `^(Totals)\|(PerGame)$` | `Y` |  | 
_**Period**_ |  | `Y` |  | 
_**PlayerID**_ |  | `Y` |  | 
_**Season**_ | `^\d{4}-\d{2}$` | `Y` |  | 
_**SeasonType**_ | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$` | `Y` |  | 
_**TeamID**_ |  | `Y` |  | 
_**VsDivision**_ | `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$` | `Y` | `Y` | 
_**VsConference**_ | `^((East)\|(West))?$` | `Y` | `Y` | 
_**SeasonSegment**_ | `^((Post All-Star)\|(Pre All-Star))?$` | `Y` | `Y` | 
_**Outcome**_ | `^((W)\|(L))?$` | `Y` | `Y` | 
_**Location**_ | `^((Home)\|(Road))?$` | `Y` | `Y` | 
_**GameSegment**_ | `^((First Half)\|(Overtime)\|(Second Half))?$` | `Y` | `Y` | 
_**DateTo**_ |  | `Y` | `Y` | 
_**DateFrom**_ |  | `Y` | `Y` | 

## Data Sets
#### NumContestedRebounding `num_contested_rebounding`
```text
['PLAYER_ID', 'PLAYER_NAME_LAST_FIRST', 'SORT_ORDER', 'G', 'REB_NUM_CONTESTING_RANGE', 'REB_FREQUENCY', 'OREB', 'DREB', 'REB', 'C_OREB', 'C_DREB', 'C_REB', 'C_REB_PCT', 'UC_OREB', 'UC_DREB', 'UC_REB', 'UC_REB_PCT']
```

#### OverallRebounding `overall_rebounding`
```text
['PLAYER_ID', 'PLAYER_NAME_LAST_FIRST', 'G', 'OVERALL', 'REB_FREQUENCY', 'OREB', 'DREB', 'REB', 'C_OREB', 'C_DREB', 'C_REB', 'C_REB_PCT', 'UC_OREB', 'UC_DREB', 'UC_REB', 'UC_REB_PCT']
```

#### RebDistanceRebounding `reb_distance_rebounding`
```text
['PLAYER_ID', 'PLAYER_NAME_LAST_FIRST', 'SORT_ORDER', 'G', 'REB_DIST_RANGE', 'REB_FREQUENCY', 'OREB', 'DREB', 'REB', 'C_OREB', 'C_DREB', 'C_REB', 'C_REB_PCT', 'UC_OREB', 'UC_DREB', 'UC_REB', 'UC_REB_PCT']
```

#### ShotDistanceRebounding `shot_distance_rebounding`
```text
['PLAYER_ID', 'PLAYER_NAME_LAST_FIRST', 'SORT_ORDER', 'G', 'SHOT_DIST_RANGE', 'REB_FREQUENCY', 'OREB', 'DREB', 'REB', 'C_OREB', 'C_DREB', 'C_REB', 'C_REB_PCT', 'UC_OREB', 'UC_DREB', 'UC_REB', 'UC_REB_PCT']
```

#### ShotTypeRebounding `shot_type_rebounding`
```text
['PLAYER_ID', 'PLAYER_NAME_LAST_FIRST', 'SORT_ORDER', 'G', 'SHOT_TYPE_RANGE', 'REB_FREQUENCY', 'OREB', 'DREB', 'REB', 'C_OREB', 'C_DREB', 'C_REB', 'C_REB_PCT', 'UC_OREB', 'UC_DREB', 'UC_REB', 'UC_REB_PCT']
```


## JSON
```json
{
    "data_sets": {
        "NumContestedRebounding": [
            "PLAYER_ID",
            "PLAYER_NAME_LAST_FIRST",
            "SORT_ORDER",
            "G",
            "REB_NUM_CONTESTING_RANGE",
            "REB_FREQUENCY",
            "OREB",
            "DREB",
            "REB",
            "C_OREB",
            "C_DREB",
            "C_REB",
            "C_REB_PCT",
            "UC_OREB",
            "UC_DREB",
            "UC_REB",
            "UC_REB_PCT"
        ],
        "OverallRebounding": [
            "PLAYER_ID",
            "PLAYER_NAME_LAST_FIRST",
            "G",
            "OVERALL",
            "REB_FREQUENCY",
            "OREB",
            "DREB",
            "REB",
            "C_OREB",
            "C_DREB",
            "C_REB",
            "C_REB_PCT",
            "UC_OREB",
            "UC_DREB",
            "UC_REB",
            "UC_REB_PCT"
        ],
        "RebDistanceRebounding": [
            "PLAYER_ID",
            "PLAYER_NAME_LAST_FIRST",
            "SORT_ORDER",
            "G",
            "REB_DIST_RANGE",
            "REB_FREQUENCY",
            "OREB",
            "DREB",
            "REB",
            "C_OREB",
            "C_DREB",
            "C_REB",
            "C_REB_PCT",
            "UC_OREB",
            "UC_DREB",
            "UC_REB",
            "UC_REB_PCT"
        ],
        "ShotDistanceRebounding": [
            "PLAYER_ID",
            "PLAYER_NAME_LAST_FIRST",
            "SORT_ORDER",
            "G",
            "SHOT_DIST_RANGE",
            "REB_FREQUENCY",
            "OREB",
            "DREB",
            "REB",
            "C_OREB",
            "C_DREB",
            "C_REB",
            "C_REB_PCT",
            "UC_OREB",
            "UC_DREB",
            "UC_REB",
            "UC_REB_PCT"
        ],
        "ShotTypeRebounding": [
            "PLAYER_ID",
            "PLAYER_NAME_LAST_FIRST",
            "SORT_ORDER",
            "G",
            "SHOT_TYPE_RANGE",
            "REB_FREQUENCY",
            "OREB",
            "DREB",
            "REB",
            "C_OREB",
            "C_DREB",
            "C_REB",
            "C_REB_PCT",
            "UC_OREB",
            "UC_DREB",
            "UC_REB",
            "UC_REB_PCT"
        ]
    },
    "endpoint": "PlayerDashPtReb",
    "nullable_parameters": [
        "DateFrom",
        "DateTo",
        "GameSegment",
        "Location",
        "Outcome",
        "SeasonSegment",
        "VsConference",
        "VsDivision"
    ],
    "parameter_patterns": {
        "DateFrom": null,
        "DateTo": null,
        "GameSegment": "^((First Half)|(Overtime)|(Second Half))?$",
        "LastNGames": null,
        "LeagueID": "(00)|(20)|(10)",
        "Location": "^((Home)|(Road))?$",
        "Month": null,
        "OpponentTeamID": null,
        "Outcome": "^((W)|(L))?$",
        "PerMode": "^(Totals)|(PerGame)$",
        "Period": null,
        "PlayerID": null,
        "Season": "^\\d{4}-\\d{2}$",
        "SeasonSegment": "^((Post All-Star)|(Pre All-Star))?$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$",
        "TeamID": null,
        "VsConference": "^((East)|(West))?$",
        "VsDivision": "^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$"
    },
    "parameters": [
        "DateFrom",
        "DateTo",
        "GameSegment",
        "LastNGames",
        "LeagueID",
        "Location",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "PerMode",
        "Period",
        "PlayerID",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "TeamID",
        "VsConference",
        "VsDivision"
    ],
    "required_parameters": [
        "DateFrom",
        "DateTo",
        "GameSegment",
        "LastNGames",
        "Location",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "PerMode",
        "Period",
        "PlayerID",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "TeamID",
        "VsConference",
        "VsDivision"
    ],
    "status": "success"
}
```

Last validated 2018-09-16