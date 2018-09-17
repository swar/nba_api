# LeagueDashTeamShotLocations

##### Endpoint URL
>[https://stats.nba.com/stats/leaguedashteamshotlocations](https://stats.nba.com/stats/leaguedashteamshotlocations)

##### Valid URL
>[https://stats.nba.com/stats/leaguedashteamshotlocations?Conference=&DateFrom=&DateTo=&DistanceRange=By+Zone&Division=&GameScope=&GameSegment=&LastNGames=10&LeagueID=&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=&PaceAdjust=N&PerMode=Totals&Period=1&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=&VsConference=&VsDivision=](https://stats.nba.com/stats/leaguedashteamshotlocations?Conference=&DateFrom=&DateTo=&DistanceRange=By+Zone&Division=&GameScope=&GameSegment=&LastNGames=10&LeagueID=&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=&PaceAdjust=N&PerMode=Totals&Period=1&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=&VsConference=&VsDivision=)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**DistanceRange**_ | `^(5ft Range)|(8ft Range)|(By Zone)$` | `Y` |  | 
_**LastNGames**_ |  | `Y` |  | 
_**MeasureType**_ | `^(Base)|(Opponent)$` | `Y` |  | 
_**Month**_ |  | `Y` |  | 
_**OpponentTeamID**_ |  | `Y` |  | 
_**PaceAdjust**_ | `^(Y)|(N)$` | `Y` |  | 
_**PerMode**_ | `^(Totals)|(PerGame)|(MinutesPer)|(Per48)|(Per40)|(Per36)|(PerMinute)|(PerPossession)|(PerPlay)|(Per100Possessions)|(Per100Plays)$` | `Y` |  | 
_**Period**_ |  | `Y` |  | 
_**PlusMinus**_ | `^(Y)|(N)$` | `Y` |  | 
_**Rank**_ | `^(Y)|(N)$` | `Y` |  | 
_**Season**_ | `^\d{4}-\d{2}$` | `Y` |  | 
_**SeasonType**_ | `^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$` | `Y` |  | 
_**VsDivision**_ | `^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$` | `Y` | `Y` | 
_**VsConference**_ | `^((East)|(West))?$` | `Y` | `Y` | 
_**TeamID**_ |  |  | `Y` | 
_**StarterBench**_ | `((Starters)|(Bench))?` | `Y` | `Y` | 
_**ShotClockRange**_ | `((24-22)|(22-18 Very Early)|(18-15 Early)|(15-7 Average)|(7-4 Late)|(4-0 Very Late)|(ShotClock Off))?` |  | `Y` | 
_**SeasonSegment**_ | `^((Post All-Star)|(Pre All-Star))?$` | `Y` | `Y` | 
_**PlayerPosition**_ | `((F)|(C)|(G)|(C-F)|(F-C)|(F-G)|(G-F))?` | `Y` | `Y` | 
_**PlayerExperience**_ | `((Rookie)|(Sophomore)|(Veteran))?` | `Y` | `Y` | 
_**PORound**_ |  |  | `Y` | 
_**Outcome**_ | `^((W)|(L))?$` | `Y` | `Y` | 
_**Location**_ | `^((Home)|(Road))?$` | `Y` | `Y` | 
_**LeagueID**_ | `(00)|(20)|(10)` |  | `Y` | 
_**GameSegment**_ | `^((First Half)|(Overtime)|(Second Half))?$` | `Y` | `Y` | 
_**GameScope**_ | `((Yesterday)|(Last 10))?` | `Y` | `Y` | 
_**Division**_ | `((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest))?` |  | `Y` | 
_**DateTo**_ |  | `Y` | `Y` | 
_**DateFrom**_ |  | `Y` | `Y` | 
_**Conference**_ | `((East)|(West))?` |  | `Y` | 

## Data Sets
#### ShotLocations `shot_locations`
```text
[{'columnNames': ['Restricted Area', 'In The Paint (Non-RA)', 'Mid-Range', 'Left Corner 3', 'Right Corner 3', 'Above the Break 3', 'Backcourt'], 'columnSpan': 3, 'columnsToSkip': 2, 'name': 'SHOT_CATEGORY'}, {'columnNames': ['TEAM_ID', 'TEAM_NAME', 'FGM', 'FGA', 'FG_PCT', 'FGM', 'FGA', 'FG_PCT', 'FGM', 'FGA', 'FG_PCT', 'FGM', 'FGA', 'FG_PCT', 'FGM', 'FGA', 'FG_PCT', 'FGM', 'FGA', 'FG_PCT', 'FGM', 'FGA', 'FG_PCT'], 'columnSpan': 1, 'name': 'columns'}]
```


## JSON
```json
{
    "data_sets": {
        "ShotLocations": [
            {
                "columnNames": [
                    "Restricted Area",
                    "In The Paint (Non-RA)",
                    "Mid-Range",
                    "Left Corner 3",
                    "Right Corner 3",
                    "Above the Break 3",
                    "Backcourt"
                ],
                "columnSpan": 3,
                "columnsToSkip": 2,
                "name": "SHOT_CATEGORY"
            },
            {
                "columnNames": [
                    "TEAM_ID",
                    "TEAM_NAME",
                    "FGM",
                    "FGA",
                    "FG_PCT",
                    "FGM",
                    "FGA",
                    "FG_PCT",
                    "FGM",
                    "FGA",
                    "FG_PCT",
                    "FGM",
                    "FGA",
                    "FG_PCT",
                    "FGM",
                    "FGA",
                    "FG_PCT",
                    "FGM",
                    "FGA",
                    "FG_PCT",
                    "FGM",
                    "FGA",
                    "FG_PCT"
                ],
                "columnSpan": 1,
                "name": "columns"
            }
        ]
    },
    "endpoint": "LeagueDashTeamShotLocations",
    "nullable_parameters": [
        "Conference",
        "DateFrom",
        "DateTo",
        "Division",
        "GameScope",
        "GameSegment",
        "LeagueID",
        "Location",
        "Outcome",
        "PORound",
        "PlayerExperience",
        "PlayerPosition",
        "SeasonSegment",
        "ShotClockRange",
        "StarterBench",
        "TeamID",
        "VsConference",
        "VsDivision"
    ],
    "parameter_patterns": {
        "Conference": "((East)|(West))?",
        "DateFrom": null,
        "DateTo": null,
        "DistanceRange": "^(5ft Range)|(8ft Range)|(By Zone)$",
        "Division": "((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest))?",
        "GameScope": "((Yesterday)|(Last 10))?",
        "GameSegment": "^((First Half)|(Overtime)|(Second Half))?$",
        "LastNGames": null,
        "LeagueID": "(00)|(20)|(10)",
        "Location": "^((Home)|(Road))?$",
        "MeasureType": "^(Base)|(Opponent)$",
        "Month": null,
        "OpponentTeamID": null,
        "Outcome": "^((W)|(L))?$",
        "PORound": null,
        "PaceAdjust": "^(Y)|(N)$",
        "PerMode": "^(Totals)|(PerGame)|(MinutesPer)|(Per48)|(Per40)|(Per36)|(PerMinute)|(PerPossession)|(PerPlay)|(Per100Possessions)|(Per100Plays)$",
        "Period": null,
        "PlayerExperience": "((Rookie)|(Sophomore)|(Veteran))?",
        "PlayerPosition": "((F)|(C)|(G)|(C-F)|(F-C)|(F-G)|(G-F))?",
        "PlusMinus": "^(Y)|(N)$",
        "Rank": "^(Y)|(N)$",
        "Season": "^\\d{4}-\\d{2}$",
        "SeasonSegment": "^((Post All-Star)|(Pre All-Star))?$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$",
        "ShotClockRange": "((24-22)|(22-18 Very Early)|(18-15 Early)|(15-7 Average)|(7-4 Late)|(4-0 Very Late)|(ShotClock Off))?",
        "StarterBench": "((Starters)|(Bench))?",
        "TeamID": null,
        "VsConference": "^((East)|(West))?$",
        "VsDivision": "^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$"
    },
    "parameters": [
        "Conference",
        "DateFrom",
        "DateTo",
        "DistanceRange",
        "Division",
        "GameScope",
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
        "PlayerExperience",
        "PlayerPosition",
        "PlusMinus",
        "Rank",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "ShotClockRange",
        "StarterBench",
        "TeamID",
        "VsConference",
        "VsDivision"
    ],
    "required_parameters": [
        "DateFrom",
        "DateTo",
        "DistanceRange",
        "GameScope",
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
        "PlayerExperience",
        "PlayerPosition",
        "PlusMinus",
        "Rank",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "StarterBench",
        "VsConference",
        "VsDivision"
    ],
    "status": "success"
}
```

Last validated 2018-09-16