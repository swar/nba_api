# PlayerDashboardByShootingSplits
##### [nba_api/stats/endpoints/playerdashboardbyshootingsplits.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/playerdashboardbyshootingsplits.py)

##### Endpoint URL
>[https://stats.nba.com/stats/playerdashboardbyshootingsplits](https://stats.nba.com/stats/playerdashboardbyshootingsplits)

##### Valid URL
>[https://stats.nba.com/stats/playerdashboardbyshootingsplits?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=&PaceAdjust=N&PerMode=Totals&Period=0&PlayerID=2544&PlusMinus=N&Rank=N&Season=2019-20&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&VsConference=&VsDivision=](https://stats.nba.com/stats/playerdashboardbyshootingsplits?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=&PaceAdjust=N&PerMode=Totals&Period=0&PlayerID=2544&PlusMinus=N&Rank=N&Season=2019-20&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&VsConference=&VsDivision=)

## Parameters
| API Parameter Name                                                                                                          | Python Parameter Variable |                                                                    Pattern                                                                    | Required | Nullable |
|-----------------------------------------------------------------------------------------------------------------------------|---------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------:|:--------:|:--------:|
| [_**LastNGames**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LastNGames)         | last_n_games              |                                                                                                                                               |   `Y`    |          | 
| [_**MeasureType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#MeasureType)       | measure_type_detailed     |                                `^(Base)\|(Advanced)\|(Misc)\|(Four Factors)\|(Scoring)\|(Opponent)\|(Usage)$`                                 |   `Y`    |          | 
| [_**Month**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Month)                   | month                     |                                                                                                                                               |   `Y`    |          | 
| [_**OpponentTeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#OpponentTeamID) | opponent_team_id          |                                                                                                                                               |   `Y`    |          | 
| [_**PaceAdjust**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PaceAdjust)         | pace_adjust               |                                                                 `^(Y)\|(N)$`                                                                  |   `Y`    |          | 
| [_**PerMode**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PerMode)               | per_mode_detailed         | `^(Totals)\|(PerGame)\|(MinutesPer)\|(Per48)\|(Per40)\|(Per36)\|(PerMinute)\|(PerPossession)\|(PerPlay)\|(Per100Possessions)\|(Per100Plays)$` |   `Y`    |          | 
| [_**Period**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Period)                 | period                    |                                                                                                                                               |   `Y`    |          | 
| [_**PlayerID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerID)             | player_id                 |                                                                                                                                               |   `Y`    |          | 
| [_**PlusMinus**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlusMinus)           | plus_minus                |                                                                 `^(Y)\|(N)$`                                                                  |   `Y`    |          | 
| [_**Rank**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Rank)                     | rank                      |                                                                 `^(Y)\|(N)$`                                                                  |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)                 | season                    |                                                                                                                                               |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType)         | season_type_playoffs      |                                                `^(Regular Season)\|(Pre Season)\|(Playoffs)$`                                                 |   `Y`    |          | 
| [_**VsDivision**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsDivision)         | vs_division_nullable      |                        `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$`                         |   `Y`    |   `Y`    | 
| [_**VsConference**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsConference)     | vs_conference_nullable    |                                                             `^((East)\|(West))?$`                                                             |   `Y`    |   `Y`    | 
| [_**ShotClockRange**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#ShotClockRange) | shot_clock_range_nullable |                 `((24-22)\|(22-18 Very Early)\|(18-15 Early)\|(15-7 Average)\|(7-4 Late)\|(4-0 Very Late)\|(ShotClock Off))?`                 |          |   `Y`    | 
| [_**SeasonSegment**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonSegment)   | season_segment_nullable   |                                                    `^((Post All-Star)\|(Pre All-Star))?$`                                                     |   `Y`    |   `Y`    | 
| [_**PORound**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PORound)               | po_round_nullable         |                                                                                                                                               |          |   `Y`    | 
| [_**Outcome**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Outcome)               | outcome_nullable          |                                                                `^((W)\|(L))?$`                                                                |   `Y`    |   `Y`    | 
| [_**Location**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Location)             | location_nullable         |                                                             `^((Home)\|(Road))?$`                                                             |   `Y`    |   `Y`    | 
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)             | league_id_nullable        |                                                                                                                                               |          |   `Y`    | 
| [_**GameSegment**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameSegment)       | game_segment_nullable     |                                                `^((First Half)\|(Overtime)\|(Second Half))?$`                                                 |   `Y`    |   `Y`    | 
| [_**DateTo**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateTo)                 | date_to_nullable          |                                                                                                                                               |   `Y`    |   `Y`    | 
| [_**DateFrom**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateFrom)             | date_from_nullable        |                                                                                                                                               |   `Y`    |   `Y`    | 

## Data Sets
#### AssistedBy `assisted_by`
```text
['GROUP_SET', 'PLAYER_ID', 'PLAYER_NAME', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'EFG_PCT', 'BLKA', 'PCT_AST_2PM', 'PCT_UAST_2PM', 'PCT_AST_3PM', 'PCT_UAST_3PM', 'PCT_AST_FGM', 'PCT_UAST_FGM', 'FGM_RANK', 'FGA_RANK', 'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 'EFG_PCT_RANK', 'BLKA_RANK', 'PCT_AST_2PM_RANK', 'PCT_UAST_2PM_RANK', 'PCT_AST_3PM_RANK', 'PCT_UAST_3PM_RANK', 'PCT_AST_FGM_RANK', 'PCT_UAST_FGM_RANK', 'CFID', 'CFPARAMS']
```

#### AssitedShotPlayerDashboard `assited_shot_player_dashboard`
```text
['GROUP_SET', 'GROUP_VALUE', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'EFG_PCT', 'BLKA', 'PCT_AST_2PM', 'PCT_UAST_2PM', 'PCT_AST_3PM', 'PCT_UAST_3PM', 'PCT_AST_FGM', 'PCT_UAST_FGM', 'FGM_RANK', 'FGA_RANK', 'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 'EFG_PCT_RANK', 'BLKA_RANK', 'PCT_AST_2PM_RANK', 'PCT_UAST_2PM_RANK', 'PCT_AST_3PM_RANK', 'PCT_UAST_3PM_RANK', 'PCT_AST_FGM_RANK', 'PCT_UAST_FGM_RANK', 'CFID', 'CFPARAMS']
```

#### OverallPlayerDashboard `overall_player_dashboard`
```text
['GROUP_SET', 'GROUP_VALUE', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'EFG_PCT', 'BLKA', 'PCT_AST_2PM', 'PCT_UAST_2PM', 'PCT_AST_3PM', 'PCT_UAST_3PM', 'PCT_AST_FGM', 'PCT_UAST_FGM', 'FGM_RANK', 'FGA_RANK', 'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 'EFG_PCT_RANK', 'BLKA_RANK', 'PCT_AST_2PM_RANK', 'PCT_UAST_2PM_RANK', 'PCT_AST_3PM_RANK', 'PCT_UAST_3PM_RANK', 'PCT_AST_FGM_RANK', 'PCT_UAST_FGM_RANK', 'CFID', 'CFPARAMS']
```

#### Shot5FTPlayerDashboard `shot5_ft_player_dashboard`
```text
['GROUP_SET', 'GROUP_VALUE', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'EFG_PCT', 'BLKA', 'PCT_AST_2PM', 'PCT_UAST_2PM', 'PCT_AST_3PM', 'PCT_UAST_3PM', 'PCT_AST_FGM', 'PCT_UAST_FGM', 'FGM_RANK', 'FGA_RANK', 'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 'EFG_PCT_RANK', 'BLKA_RANK', 'PCT_AST_2PM_RANK', 'PCT_UAST_2PM_RANK', 'PCT_AST_3PM_RANK', 'PCT_UAST_3PM_RANK', 'PCT_AST_FGM_RANK', 'PCT_UAST_FGM_RANK', 'CFID', 'CFPARAMS']
```

#### Shot8FTPlayerDashboard `shot8_ft_player_dashboard`
```text
['GROUP_SET', 'GROUP_VALUE', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'EFG_PCT', 'BLKA', 'PCT_AST_2PM', 'PCT_UAST_2PM', 'PCT_AST_3PM', 'PCT_UAST_3PM', 'PCT_AST_FGM', 'PCT_UAST_FGM', 'FGM_RANK', 'FGA_RANK', 'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 'EFG_PCT_RANK', 'BLKA_RANK', 'PCT_AST_2PM_RANK', 'PCT_UAST_2PM_RANK', 'PCT_AST_3PM_RANK', 'PCT_UAST_3PM_RANK', 'PCT_AST_FGM_RANK', 'PCT_UAST_FGM_RANK', 'CFID', 'CFPARAMS']
```

#### ShotAreaPlayerDashboard `shot_area_player_dashboard`
```text
['GROUP_SET', 'GROUP_VALUE', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'EFG_PCT', 'BLKA', 'PCT_AST_2PM', 'PCT_UAST_2PM', 'PCT_AST_3PM', 'PCT_UAST_3PM', 'PCT_AST_FGM', 'PCT_UAST_FGM', 'FGM_RANK', 'FGA_RANK', 'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 'EFG_PCT_RANK', 'BLKA_RANK', 'PCT_AST_2PM_RANK', 'PCT_UAST_2PM_RANK', 'PCT_AST_3PM_RANK', 'PCT_UAST_3PM_RANK', 'PCT_AST_FGM_RANK', 'PCT_UAST_FGM_RANK', 'CFID', 'CFPARAMS']
```

#### ShotTypePlayerDashboard `shot_type_player_dashboard`
```text
['GROUP_SET', 'GROUP_VALUE', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'EFG_PCT', 'BLKA', 'PCT_AST_2PM', 'PCT_UAST_2PM', 'PCT_AST_3PM', 'PCT_UAST_3PM', 'PCT_AST_FGM', 'PCT_UAST_FGM', 'FGM_RANK', 'FGA_RANK', 'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 'EFG_PCT_RANK', 'BLKA_RANK', 'PCT_AST_2PM_RANK', 'PCT_UAST_2PM_RANK', 'PCT_AST_3PM_RANK', 'PCT_UAST_3PM_RANK', 'PCT_AST_FGM_RANK', 'PCT_UAST_FGM_RANK', 'CFID', 'CFPARAMS']
```

#### ShotTypeSummaryPlayerDashboard `shot_type_summary_player_dashboard`
```text
['GROUP_SET', 'GROUP_VALUE', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'EFG_PCT', 'BLKA', 'PCT_AST_2PM', 'PCT_UAST_2PM', 'PCT_AST_3PM', 'PCT_UAST_3PM', 'PCT_AST_FGM', 'PCT_UAST_FGM', 'CFID', 'CFPARAMS']
```


## JSON
```json
{
    "data_sets": {
        "AssistedBy": [
            "GROUP_SET",
            "PLAYER_ID",
            "PLAYER_NAME",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "EFG_PCT",
            "BLKA",
            "PCT_AST_2PM",
            "PCT_UAST_2PM",
            "PCT_AST_3PM",
            "PCT_UAST_3PM",
            "PCT_AST_FGM",
            "PCT_UAST_FGM",
            "FGM_RANK",
            "FGA_RANK",
            "FG_PCT_RANK",
            "FG3M_RANK",
            "FG3A_RANK",
            "FG3_PCT_RANK",
            "EFG_PCT_RANK",
            "BLKA_RANK",
            "PCT_AST_2PM_RANK",
            "PCT_UAST_2PM_RANK",
            "PCT_AST_3PM_RANK",
            "PCT_UAST_3PM_RANK",
            "PCT_AST_FGM_RANK",
            "PCT_UAST_FGM_RANK",
            "CFID",
            "CFPARAMS"
        ],
        "AssitedShotPlayerDashboard": [
            "GROUP_SET",
            "GROUP_VALUE",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "EFG_PCT",
            "BLKA",
            "PCT_AST_2PM",
            "PCT_UAST_2PM",
            "PCT_AST_3PM",
            "PCT_UAST_3PM",
            "PCT_AST_FGM",
            "PCT_UAST_FGM",
            "FGM_RANK",
            "FGA_RANK",
            "FG_PCT_RANK",
            "FG3M_RANK",
            "FG3A_RANK",
            "FG3_PCT_RANK",
            "EFG_PCT_RANK",
            "BLKA_RANK",
            "PCT_AST_2PM_RANK",
            "PCT_UAST_2PM_RANK",
            "PCT_AST_3PM_RANK",
            "PCT_UAST_3PM_RANK",
            "PCT_AST_FGM_RANK",
            "PCT_UAST_FGM_RANK",
            "CFID",
            "CFPARAMS"
        ],
        "OverallPlayerDashboard": [
            "GROUP_SET",
            "GROUP_VALUE",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "EFG_PCT",
            "BLKA",
            "PCT_AST_2PM",
            "PCT_UAST_2PM",
            "PCT_AST_3PM",
            "PCT_UAST_3PM",
            "PCT_AST_FGM",
            "PCT_UAST_FGM",
            "FGM_RANK",
            "FGA_RANK",
            "FG_PCT_RANK",
            "FG3M_RANK",
            "FG3A_RANK",
            "FG3_PCT_RANK",
            "EFG_PCT_RANK",
            "BLKA_RANK",
            "PCT_AST_2PM_RANK",
            "PCT_UAST_2PM_RANK",
            "PCT_AST_3PM_RANK",
            "PCT_UAST_3PM_RANK",
            "PCT_AST_FGM_RANK",
            "PCT_UAST_FGM_RANK",
            "CFID",
            "CFPARAMS"
        ],
        "Shot5FTPlayerDashboard": [
            "GROUP_SET",
            "GROUP_VALUE",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "EFG_PCT",
            "BLKA",
            "PCT_AST_2PM",
            "PCT_UAST_2PM",
            "PCT_AST_3PM",
            "PCT_UAST_3PM",
            "PCT_AST_FGM",
            "PCT_UAST_FGM",
            "FGM_RANK",
            "FGA_RANK",
            "FG_PCT_RANK",
            "FG3M_RANK",
            "FG3A_RANK",
            "FG3_PCT_RANK",
            "EFG_PCT_RANK",
            "BLKA_RANK",
            "PCT_AST_2PM_RANK",
            "PCT_UAST_2PM_RANK",
            "PCT_AST_3PM_RANK",
            "PCT_UAST_3PM_RANK",
            "PCT_AST_FGM_RANK",
            "PCT_UAST_FGM_RANK",
            "CFID",
            "CFPARAMS"
        ],
        "Shot8FTPlayerDashboard": [
            "GROUP_SET",
            "GROUP_VALUE",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "EFG_PCT",
            "BLKA",
            "PCT_AST_2PM",
            "PCT_UAST_2PM",
            "PCT_AST_3PM",
            "PCT_UAST_3PM",
            "PCT_AST_FGM",
            "PCT_UAST_FGM",
            "FGM_RANK",
            "FGA_RANK",
            "FG_PCT_RANK",
            "FG3M_RANK",
            "FG3A_RANK",
            "FG3_PCT_RANK",
            "EFG_PCT_RANK",
            "BLKA_RANK",
            "PCT_AST_2PM_RANK",
            "PCT_UAST_2PM_RANK",
            "PCT_AST_3PM_RANK",
            "PCT_UAST_3PM_RANK",
            "PCT_AST_FGM_RANK",
            "PCT_UAST_FGM_RANK",
            "CFID",
            "CFPARAMS"
        ],
        "ShotAreaPlayerDashboard": [
            "GROUP_SET",
            "GROUP_VALUE",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "EFG_PCT",
            "BLKA",
            "PCT_AST_2PM",
            "PCT_UAST_2PM",
            "PCT_AST_3PM",
            "PCT_UAST_3PM",
            "PCT_AST_FGM",
            "PCT_UAST_FGM",
            "FGM_RANK",
            "FGA_RANK",
            "FG_PCT_RANK",
            "FG3M_RANK",
            "FG3A_RANK",
            "FG3_PCT_RANK",
            "EFG_PCT_RANK",
            "BLKA_RANK",
            "PCT_AST_2PM_RANK",
            "PCT_UAST_2PM_RANK",
            "PCT_AST_3PM_RANK",
            "PCT_UAST_3PM_RANK",
            "PCT_AST_FGM_RANK",
            "PCT_UAST_FGM_RANK",
            "CFID",
            "CFPARAMS"
        ],
        "ShotTypePlayerDashboard": [
            "GROUP_SET",
            "GROUP_VALUE",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "EFG_PCT",
            "BLKA",
            "PCT_AST_2PM",
            "PCT_UAST_2PM",
            "PCT_AST_3PM",
            "PCT_UAST_3PM",
            "PCT_AST_FGM",
            "PCT_UAST_FGM",
            "FGM_RANK",
            "FGA_RANK",
            "FG_PCT_RANK",
            "FG3M_RANK",
            "FG3A_RANK",
            "FG3_PCT_RANK",
            "EFG_PCT_RANK",
            "BLKA_RANK",
            "PCT_AST_2PM_RANK",
            "PCT_UAST_2PM_RANK",
            "PCT_AST_3PM_RANK",
            "PCT_UAST_3PM_RANK",
            "PCT_AST_FGM_RANK",
            "PCT_UAST_FGM_RANK",
            "CFID",
            "CFPARAMS"
        ],
        "ShotTypeSummaryPlayerDashboard": [
            "GROUP_SET",
            "GROUP_VALUE",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "EFG_PCT",
            "BLKA",
            "PCT_AST_2PM",
            "PCT_UAST_2PM",
            "PCT_AST_3PM",
            "PCT_UAST_3PM",
            "PCT_AST_FGM",
            "PCT_UAST_FGM",
            "CFID",
            "CFPARAMS"
        ]
    },
    "endpoint": "PlayerDashboardByShootingSplits",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [
        "DateFrom",
        "DateTo",
        "GameSegment",
        "LeagueID",
        "Location",
        "Outcome",
        "PORound",
        "SeasonSegment",
        "ShotClockRange",
        "VsConference",
        "VsDivision"
    ],
    "parameter_patterns": {
        "DateFrom": null,
        "DateTo": null,
        "GameSegment": "^((First Half)|(Overtime)|(Second Half))?$",
        "LastNGames": null,
        "LeagueID": null,
        "Location": "^((Home)|(Road))?$",
        "MeasureType": "^(Base)|(Advanced)|(Misc)|(Four Factors)|(Scoring)|(Opponent)|(Usage)$",
        "Month": null,
        "OpponentTeamID": null,
        "Outcome": "^((W)|(L))?$",
        "PORound": null,
        "PaceAdjust": "^(Y)|(N)$",
        "PerMode": "^(Totals)|(PerGame)|(MinutesPer)|(Per48)|(Per40)|(Per36)|(PerMinute)|(PerPossession)|(PerPlay)|(Per100Possessions)|(Per100Plays)$",
        "Period": null,
        "PlayerID": null,
        "PlusMinus": "^(Y)|(N)$",
        "Rank": "^(Y)|(N)$",
        "Season": null,
        "SeasonSegment": "^((Post All-Star)|(Pre All-Star))?$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)$",
        "ShotClockRange": "((24-22)|(22-18 Very Early)|(18-15 Early)|(15-7 Average)|(7-4 Late)|(4-0 Very Late)|(ShotClock Off))?",
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
        "MeasureType",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "PORound",
        "PaceAdjust",
        "PerMode",
        "Period",
        "PlayerID",
        "PlusMinus",
        "Rank",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "ShotClockRange",
        "VsConference",
        "VsDivision"
    ],
    "required_parameters": [
        "DateFrom",
        "DateTo",
        "GameSegment",
        "LastNGames",
        "Location",
        "MeasureType",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "PaceAdjust",
        "PerMode",
        "Period",
        "PlayerID",
        "PlusMinus",
        "Rank",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "VsConference",
        "VsDivision"
    ],
    "status": "success"
}
```

Last validated 2020-08-16