# TeamDashboardByShootingSplits

##### Endpoint URL
>[https://stats.nba.com/stats/teamdashboardbyshootingsplits](https://stats.nba.com/stats/teamdashboardbyshootingsplits)

##### Valid URL
>[https://stats.nba.com/stats/teamdashboardbyshootingsplits?DateFrom=&DateTo=&GameSegment=&LastNGames=10&LeagueID=&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=&PaceAdjust=N&PerMode=Totals&Period=1&PlusMinus=N&Rank=N&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&TeamID=1610612739&VsConference=&VsDivision=](https://stats.nba.com/stats/teamdashboardbyshootingsplits?DateFrom=&DateTo=&GameSegment=&LastNGames=10&LeagueID=&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=&PaceAdjust=N&PerMode=Totals&Period=1&PlusMinus=N&Rank=N&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&TeamID=1610612739&VsConference=&VsDivision=)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**LastNGames**_ |  | `Y` |  | 
_**MeasureType**_ | `^(Base)\|(Advanced)\|(Misc)\|(Four Factors)\|(Scoring)\|(Opponent)\|(Usage)\|(Defense)$` | `Y` |  | 
_**Month**_ |  | `Y` |  | 
_**OpponentTeamID**_ |  | `Y` |  | 
_**PaceAdjust**_ | `^(Y)\|(N)$` | `Y` |  | 
_**PerMode**_ | `^(Totals)\|(PerGame)\|(MinutesPer)\|(Per48)\|(Per40)\|(Per36)\|(PerMinute)\|(PerPossession)\|(PerPlay)\|(Per100Possessions)\|(Per100Plays)$` | `Y` |  | 
_**Period**_ |  | `Y` |  | 
_**PlusMinus**_ | `^(Y)\|(N)$` | `Y` |  | 
_**Rank**_ | `^(Y)\|(N)$` | `Y` |  | 
_**Season**_ | `^\d{4}-\d{2}$` | `Y` |  | 
_**SeasonType**_ | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$` | `Y` |  | 
_**TeamID**_ |  | `Y` |  | 
_**VsDivision**_ | `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$` | `Y` | `Y` | 
_**VsConference**_ | `^((East)\|(West))?$` | `Y` | `Y` | 
_**ShotClockRange**_ | `((24-22)\|(22-18 Very Early)\|(18-15 Early)\|(15-7 Average)\|(7-4 Late)\|(4-0 Very Late)\|(ShotClock Off))?` |  | `Y` | 
_**SeasonSegment**_ | `^((Post All-Star)\|(Pre All-Star))?$` | `Y` | `Y` | 
_**PORound**_ |  |  | `Y` | 
_**Outcome**_ | `^((W)\|(L))?$` | `Y` | `Y` | 
_**Location**_ | `^((Home)\|(Road))?$` | `Y` | `Y` | 
_**LeagueID**_ | `(00)\|(20)\|(10)` |  | `Y` | 
_**GameSegment**_ | `^((First Half)\|(Overtime)\|(Second Half))?$` | `Y` | `Y` | 
_**DateTo**_ |  | `Y` | `Y` | 
_**DateFrom**_ |  | `Y` | `Y` | 

## Data Sets
#### AssistedBy `assisted_by`
```text
['GROUP_SET', 'PLAYER_ID', 'PLAYER_NAME', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'EFG_PCT', 'BLKA', 'PCT_AST_2PM', 'PCT_UAST_2PM', 'PCT_AST_3PM', 'PCT_UAST_3PM', 'PCT_AST_FGM', 'PCT_UAST_FGM', 'FGM_RANK', 'FGA_RANK', 'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 'EFG_PCT_RANK', 'BLKA_RANK', 'PCT_AST_2PM_RANK', 'PCT_UAST_2PM_RANK', 'PCT_AST_3PM_RANK', 'PCT_UAST_3PM_RANK', 'PCT_AST_FGM_RANK', 'PCT_UAST_FGM_RANK', 'CFID', 'CFPARAMS']
```

#### AssitedShotTeamDashboard `assited_shot_team_dashboard`
```text
['GROUP_SET', 'GROUP_VALUE', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'EFG_PCT', 'BLKA', 'PCT_AST_2PM', 'PCT_UAST_2PM', 'PCT_AST_3PM', 'PCT_UAST_3PM', 'PCT_AST_FGM', 'PCT_UAST_FGM', 'FGM_RANK', 'FGA_RANK', 'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 'EFG_PCT_RANK', 'BLKA_RANK', 'PCT_AST_2PM_RANK', 'PCT_UAST_2PM_RANK', 'PCT_AST_3PM_RANK', 'PCT_UAST_3PM_RANK', 'PCT_AST_FGM_RANK', 'PCT_UAST_FGM_RANK', 'CFID', 'CFPARAMS']
```

#### OverallTeamDashboard `overall_team_dashboard`
```text
['GROUP_SET', 'GROUP_VALUE', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'EFG_PCT', 'BLKA', 'PCT_AST_2PM', 'PCT_UAST_2PM', 'PCT_AST_3PM', 'PCT_UAST_3PM', 'PCT_AST_FGM', 'PCT_UAST_FGM', 'FGM_RANK', 'FGA_RANK', 'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 'EFG_PCT_RANK', 'BLKA_RANK', 'PCT_AST_2PM_RANK', 'PCT_UAST_2PM_RANK', 'PCT_AST_3PM_RANK', 'PCT_UAST_3PM_RANK', 'PCT_AST_FGM_RANK', 'PCT_UAST_FGM_RANK', 'CFID', 'CFPARAMS']
```

#### Shot5FTTeamDashboard `shot5_ft_team_dashboard`
```text
['GROUP_SET', 'GROUP_VALUE', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'EFG_PCT', 'BLKA', 'PCT_AST_2PM', 'PCT_UAST_2PM', 'PCT_AST_3PM', 'PCT_UAST_3PM', 'PCT_AST_FGM', 'PCT_UAST_FGM', 'FGM_RANK', 'FGA_RANK', 'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 'EFG_PCT_RANK', 'BLKA_RANK', 'PCT_AST_2PM_RANK', 'PCT_UAST_2PM_RANK', 'PCT_AST_3PM_RANK', 'PCT_UAST_3PM_RANK', 'PCT_AST_FGM_RANK', 'PCT_UAST_FGM_RANK', 'CFID', 'CFPARAMS']
```

#### Shot8FTTeamDashboard `shot8_ft_team_dashboard`
```text
['GROUP_SET', 'GROUP_VALUE', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'EFG_PCT', 'BLKA', 'PCT_AST_2PM', 'PCT_UAST_2PM', 'PCT_AST_3PM', 'PCT_UAST_3PM', 'PCT_AST_FGM', 'PCT_UAST_FGM', 'FGM_RANK', 'FGA_RANK', 'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 'EFG_PCT_RANK', 'BLKA_RANK', 'PCT_AST_2PM_RANK', 'PCT_UAST_2PM_RANK', 'PCT_AST_3PM_RANK', 'PCT_UAST_3PM_RANK', 'PCT_AST_FGM_RANK', 'PCT_UAST_FGM_RANK', 'CFID', 'CFPARAMS']
```

#### ShotAreaTeamDashboard `shot_area_team_dashboard`
```text
['GROUP_SET', 'GROUP_VALUE', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'EFG_PCT', 'BLKA', 'PCT_AST_2PM', 'PCT_UAST_2PM', 'PCT_AST_3PM', 'PCT_UAST_3PM', 'PCT_AST_FGM', 'PCT_UAST_FGM', 'FGM_RANK', 'FGA_RANK', 'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 'EFG_PCT_RANK', 'BLKA_RANK', 'PCT_AST_2PM_RANK', 'PCT_UAST_2PM_RANK', 'PCT_AST_3PM_RANK', 'PCT_UAST_3PM_RANK', 'PCT_AST_FGM_RANK', 'PCT_UAST_FGM_RANK', 'CFID', 'CFPARAMS']
```

#### ShotTypeTeamDashboard `shot_type_team_dashboard`
```text
['GROUP_SET', 'GROUP_VALUE', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'EFG_PCT', 'BLKA', 'PCT_AST_2PM', 'PCT_UAST_2PM', 'PCT_AST_3PM', 'PCT_UAST_3PM', 'PCT_AST_FGM', 'PCT_UAST_FGM', 'FGM_RANK', 'FGA_RANK', 'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 'EFG_PCT_RANK', 'BLKA_RANK', 'PCT_AST_2PM_RANK', 'PCT_UAST_2PM_RANK', 'PCT_AST_3PM_RANK', 'PCT_UAST_3PM_RANK', 'PCT_AST_FGM_RANK', 'PCT_UAST_FGM_RANK', 'CFID', 'CFPARAMS']
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
        "AssitedShotTeamDashboard": [
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
        "OverallTeamDashboard": [
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
        "Shot5FTTeamDashboard": [
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
        "Shot8FTTeamDashboard": [
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
        "ShotAreaTeamDashboard": [
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
        "ShotTypeTeamDashboard": [
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
        ]
    },
    "endpoint": "TeamDashboardByShootingSplits",
    "last_validated_date": "2018-10-08",
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
        "LeagueID": "(00)|(20)|(10)",
        "Location": "^((Home)|(Road))?$",
        "MeasureType": "^(Base)|(Advanced)|(Misc)|(Four Factors)|(Scoring)|(Opponent)|(Usage)|(Defense)$",
        "Month": null,
        "OpponentTeamID": null,
        "Outcome": "^((W)|(L))?$",
        "PORound": null,
        "PaceAdjust": "^(Y)|(N)$",
        "PerMode": "^(Totals)|(PerGame)|(MinutesPer)|(Per48)|(Per40)|(Per36)|(PerMinute)|(PerPossession)|(PerPlay)|(Per100Possessions)|(Per100Plays)$",
        "Period": null,
        "PlusMinus": "^(Y)|(N)$",
        "Rank": "^(Y)|(N)$",
        "Season": "^\\d{4}-\\d{2}$",
        "SeasonSegment": "^((Post All-Star)|(Pre All-Star))?$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$",
        "ShotClockRange": "((24-22)|(22-18 Very Early)|(18-15 Early)|(15-7 Average)|(7-4 Late)|(4-0 Very Late)|(ShotClock Off))?",
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
        "MeasureType",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "PORound",
        "PaceAdjust",
        "PerMode",
        "Period",
        "PlusMinus",
        "Rank",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "ShotClockRange",
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
        "MeasureType",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "PaceAdjust",
        "PerMode",
        "Period",
        "PlusMinus",
        "Rank",
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

Last validated 2018-10-08