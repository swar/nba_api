# PlayerDashPtReb
##### [nba_api/stats/endpoints/playerdashptreb.py](https://github.com/swar/nba_api/blob/master/nba_api/stats/endpoints/playerdashptreb.py)

##### Endpoint URL
>[https://stats.nba.com/stats/playerdashptreb](https://stats.nba.com/stats/playerdashptreb)

##### Valid URL
>[https://stats.nba.com/stats/playerdashptreb?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PerMode=Totals&Period=0&PlayerID=2544&Season=2018-19&SeasonSegment=&SeasonType=Regular+Season&TeamID=1610612739&VsConference=&VsDivision=](https://stats.nba.com/stats/playerdashptreb?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PerMode=Totals&Period=0&PlayerID=2544&Season=2018-19&SeasonSegment=&SeasonType=Regular+Season&TeamID=1610612739&VsConference=&VsDivision=)

## Parameters
API Parameter Name | Python Parameter Variable | Parameter Mapping Class | Pattern | Required | Nullable
------------ | ------------ | ------------ | :-----------: | :---: | :---:
[_**LastNGames**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LastNGames) | last_n_games | LastNGames |  | `Y` |  | 
[_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id | LeagueID | `(00)\|(20)\|(10)` |  |  | 
[_**Month**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Month) | month | Month |  | `Y` |  | 
[_**OpponentTeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#OpponentTeamID) | opponent_team_id | OpponentTeamID |  | `Y` |  | 
[_**PerMode**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PerMode) | per_mode_simple | PerModeSimple | `^(Totals)\|(PerGame)$` | `Y` |  | 
[_**Period**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Period) | period | Period |  | `Y` |  | 
[_**PlayerID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerID) | player_id | PlayerID |  | `Y` |  | 
[_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season) | season | Season | `^\d{4}-\d{2}$` | `Y` |  | 
[_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType) | season_type_all_star | SeasonTypeAllStar | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$` | `Y` |  | 
[_**TeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TeamID) | team_id | TeamID |  | `Y` |  | 
[_**VsDivision**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsDivision) | vs_division_nullable | VsDivisionNullable | `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$` | `Y` | `Y` | 
[_**VsConference**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsConference) | vs_conference_nullable | VsConferenceNullable | `^((East)\|(West))?$` | `Y` | `Y` | 
[_**SeasonSegment**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonSegment) | season_segment_nullable | SeasonSegmentNullable | `^((Post All-Star)\|(Pre All-Star))?$` | `Y` | `Y` | 
[_**Outcome**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Outcome) | outcome_nullable | OutcomeNullable | `^((W)\|(L))?$` | `Y` | `Y` | 
[_**Location**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Location) | location_nullable | LocationNullable | `^((Home)\|(Road))?$` | `Y` | `Y` | 
[_**GameSegment**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameSegment) | game_segment_nullable | GameSegmentNullable | `^((First Half)\|(Overtime)\|(Second Half))?$` | `Y` | `Y` | 
[_**DateTo**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateTo) | date_to_nullable | DateToNullable |  | `Y` | `Y` | 
[_**DateFrom**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateFrom) | date_from_nullable | DateFromNullable |  | `Y` | `Y` | 

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
    "last_validated_date": "2018-12-11",
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

Last validated 2018-12-11