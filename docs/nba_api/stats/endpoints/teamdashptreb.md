# TeamDashPtReb
##### [nba_api/stats/endpoints/teamdashptreb.py](https://github.com/swar/nba_api/blob/master/nba_api/stats/endpoints/teamdashptreb.py)

##### Endpoint URL
>[https://stats.nba.com/stats/teamdashptreb](https://stats.nba.com/stats/teamdashptreb)

##### Valid URL
>[https://stats.nba.com/stats/teamdashptreb?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PerMode=Totals&Period=0&Season=2018-19&SeasonSegment=&SeasonType=Regular+Season&TeamID=1610612739&VsConference=&VsDivision=](https://stats.nba.com/stats/teamdashptreb?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PerMode=Totals&Period=0&Season=2018-19&SeasonSegment=&SeasonType=Regular+Season&TeamID=1610612739&VsConference=&VsDivision=)

## Parameters
API Parameter Name | Python Parameter Class | Python Parameter Variable | Pattern | Required | Nullable
------------ | ------------ | ------------ | :-----------: | :---: | :---:
_**LastNGames**_ | [LastNGames](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LastNGames) | last_n_games |  | `Y` |  | 
_**LeagueID**_ | [LeagueID](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id | `(00)\|(20)\|(10)` |  |  | 
_**Month**_ | [Month](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Month) | month |  | `Y` |  | 
_**OpponentTeamID**_ | [OpponentTeamID](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#OpponentTeamID) | opponent_team_id |  | `Y` |  | 
_**PerMode**_ | [PerModeSimple](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PerMode) | per_mode_simple | `^(Totals)\|(PerGame)$` | `Y` |  | 
_**Period**_ | [Period](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Period) | period |  | `Y` |  | 
_**Season**_ | [Season](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season) | season | `^\d{4}-\d{2}$` | `Y` |  | 
_**SeasonType**_ | [SeasonTypeAllStar](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType) | season_type_all_star | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$` | `Y` |  | 
_**TeamID**_ | [TeamID](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TeamID) | team_id |  | `Y` |  | 
_**VsDivision**_ | [VsDivisionNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsDivision) | vs_division_nullable | `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$` | `Y` | `Y` | 
_**VsConference**_ | [VsConferenceNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsConference) | vs_conference_nullable | `^((East)\|(West))?$` | `Y` | `Y` | 
_**SeasonSegment**_ | [SeasonSegmentNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonSegment) | season_segment_nullable | `^((Post All-Star)\|(Pre All-Star))?$` | `Y` | `Y` | 
_**Outcome**_ | [OutcomeNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Outcome) | outcome_nullable | `^((W)\|(L))?$` | `Y` | `Y` | 
_**Location**_ | [LocationNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Location) | location_nullable | `^((Home)\|(Road))?$` | `Y` | `Y` | 
_**GameSegment**_ | [GameSegmentNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameSegment) | game_segment_nullable | `^((First Half)\|(Overtime)\|(Second Half))?$` | `Y` | `Y` | 
_**DateTo**_ | [DateToNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateTo) | date_to_nullable |  | `Y` | `Y` | 
_**DateFrom**_ | [DateFromNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateFrom) | date_from_nullable |  | `Y` | `Y` | 

## Data Sets
#### NumContestedRebounding `num_contested_rebounding`
```text
['TEAM_ID', 'TEAM_NAME', 'SORT_ORDER', 'G', 'REB_NUM_CONTESTING_RANGE', 'REB_FREQUENCY', 'OREB', 'DREB', 'REB', 'C_OREB', 'C_DREB', 'C_REB', 'C_REB_PCT', 'UC_OREB', 'UC_DREB', 'UC_REB', 'UC_REB_PCT']
```

#### OverallRebounding `overall_rebounding`
```text
['TEAM_ID', 'TEAM_NAME', 'G', 'OVERALL', 'REB_FREQUENCY', 'OREB', 'DREB', 'REB', 'C_OREB', 'C_DREB', 'C_REB', 'C_REB_PCT', 'UC_OREB', 'UC_DREB', 'UC_REB', 'UC_REB_PCT']
```

#### RebDistanceRebounding `reb_distance_rebounding`
```text
['TEAM_ID', 'TEAM_NAME', 'SORT_ORDER', 'G', 'REB_DIST_RANGE', 'REB_FREQUENCY', 'OREB', 'DREB', 'REB', 'C_OREB', 'C_DREB', 'C_REB', 'C_REB_PCT', 'UC_OREB', 'UC_DREB', 'UC_REB', 'UC_REB_PCT']
```

#### ShotDistanceRebounding `shot_distance_rebounding`
```text
['TEAM_ID', 'TEAM_NAME', 'SORT_ORDER', 'G', 'SHOT_DIST_RANGE', 'REB_FREQUENCY', 'OREB', 'DREB', 'REB', 'C_OREB', 'C_DREB', 'C_REB', 'C_REB_PCT', 'UC_OREB', 'UC_DREB', 'UC_REB', 'UC_REB_PCT']
```

#### ShotTypeRebounding `shot_type_rebounding`
```text
['TEAM_ID', 'TEAM_NAME', 'SORT_ORDER', 'G', 'SHOT_TYPE_RANGE', 'REB_FREQUENCY', 'OREB', 'DREB', 'REB', 'C_OREB', 'C_DREB', 'C_REB', 'C_REB_PCT', 'UC_OREB', 'UC_DREB', 'UC_REB', 'UC_REB_PCT']
```


## JSON
```json
{
    "data_sets": {
        "NumContestedRebounding": [
            "TEAM_ID",
            "TEAM_NAME",
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
            "TEAM_ID",
            "TEAM_NAME",
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
            "TEAM_ID",
            "TEAM_NAME",
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
            "TEAM_ID",
            "TEAM_NAME",
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
            "TEAM_ID",
            "TEAM_NAME",
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
    "endpoint": "TeamDashPtReb",
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