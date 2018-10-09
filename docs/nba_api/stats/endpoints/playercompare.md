# PlayerCompare

##### Endpoint URL
>[https://stats.nba.com/stats/playercompare](https://stats.nba.com/stats/playercompare)

##### Valid URL
>[https://stats.nba.com/stats/playercompare?Conference=&DateFrom=&DateTo=&Division=&GameSegment=&LastNGames=10&LeagueID=&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PaceAdjust=N&PerMode=Totals&Period=1&PlayerIDList=202681%2C203078%2C2544%2C201567%2C203954&PlusMinus=N&Rank=N&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&VsConference=&VsDivision=&VsPlayerIDList=201566%2C201939%2C201935%2C201142%2C203076](https://stats.nba.com/stats/playercompare?Conference=&DateFrom=&DateTo=&Division=&GameSegment=&LastNGames=10&LeagueID=&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PaceAdjust=N&PerMode=Totals&Period=1&PlayerIDList=202681%2C203078%2C2544%2C201567%2C203954&PlusMinus=N&Rank=N&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&VsConference=&VsDivision=&VsPlayerIDList=201566%2C201939%2C201935%2C201142%2C203076)

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
_**PlayerIDList**_ |  | `Y` |  | 
_**PlusMinus**_ | `^(Y)\|(N)$` | `Y` |  | 
_**Rank**_ | `^(Y)\|(N)$` | `Y` |  | 
_**Season**_ | `^\d{4}-\d{2}$` | `Y` |  | 
_**SeasonType**_ | `^(Regular Season)\|(Pre Season)\|(Playoffs)$` | `Y` |  | 
_**VsPlayerIDList**_ |  | `Y` |  | 
_**VsDivision**_ | `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$` | `Y` | `Y` | 
_**VsConference**_ | `^((East)\|(West))?$` | `Y` | `Y` | 
_**ShotClockRange**_ |  |  | `Y` | 
_**SeasonSegment**_ | `^((Post All-Star)\|(Pre All-Star))?$` | `Y` | `Y` | 
_**Outcome**_ | `^((W)\|(L))?$` | `Y` | `Y` | 
_**Location**_ | `^((Home)\|(Road))?$` | `Y` | `Y` | 
_**LeagueID**_ | `(00)\|(20)\|(10)` |  | `Y` | 
_**GameSegment**_ | `^((First Half)\|(Overtime)\|(Second Half))?$` | `Y` | `Y` | 
_**Division**_ |  |  | `Y` | 
_**DateTo**_ |  | `Y` | `Y` | 
_**DateFrom**_ |  | `Y` | `Y` | 
_**Conference**_ | `^((East)\|(West))?$` |  | `Y` | 

## Data Sets
#### Individual `individual`
```text
['GROUP_SET', 'DESCRIPTION', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS']
```

#### OverallCompare `overall_compare`
```text
['GROUP_SET', 'DESCRIPTION', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS']
```


## JSON
```json
{
    "data_sets": {
        "Individual": [
            "GROUP_SET",
            "DESCRIPTION",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "TOV",
            "STL",
            "BLK",
            "BLKA",
            "PF",
            "PFD",
            "PTS",
            "PLUS_MINUS"
        ],
        "OverallCompare": [
            "GROUP_SET",
            "DESCRIPTION",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "TOV",
            "STL",
            "BLK",
            "BLKA",
            "PF",
            "PFD",
            "PTS",
            "PLUS_MINUS"
        ]
    },
    "endpoint": "PlayerCompare",
    "last_validated_date": "2018-10-08",
    "nullable_parameters": [
        "Conference",
        "DateFrom",
        "DateTo",
        "Division",
        "GameSegment",
        "LeagueID",
        "Location",
        "Outcome",
        "SeasonSegment",
        "ShotClockRange",
        "VsConference",
        "VsDivision"
    ],
    "parameter_patterns": {
        "Conference": "^((East)|(West))?$",
        "DateFrom": null,
        "DateTo": null,
        "Division": null,
        "GameSegment": "^((First Half)|(Overtime)|(Second Half))?$",
        "LastNGames": null,
        "LeagueID": "(00)|(20)|(10)",
        "Location": "^((Home)|(Road))?$",
        "MeasureType": "^(Base)|(Advanced)|(Misc)|(Four Factors)|(Scoring)|(Opponent)|(Usage)|(Defense)$",
        "Month": null,
        "OpponentTeamID": null,
        "Outcome": "^((W)|(L))?$",
        "PaceAdjust": "^(Y)|(N)$",
        "PerMode": "^(Totals)|(PerGame)|(MinutesPer)|(Per48)|(Per40)|(Per36)|(PerMinute)|(PerPossession)|(PerPlay)|(Per100Possessions)|(Per100Plays)$",
        "Period": null,
        "PlayerIDList": null,
        "PlusMinus": "^(Y)|(N)$",
        "Rank": "^(Y)|(N)$",
        "Season": "^\\d{4}-\\d{2}$",
        "SeasonSegment": "^((Post All-Star)|(Pre All-Star))?$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)$",
        "ShotClockRange": null,
        "VsConference": "^((East)|(West))?$",
        "VsDivision": "^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$",
        "VsPlayerIDList": null
    },
    "parameters": [
        "Conference",
        "DateFrom",
        "DateTo",
        "Division",
        "GameSegment",
        "LastNGames",
        "LeagueID",
        "Location",
        "MeasureType",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "PaceAdjust",
        "PerMode",
        "Period",
        "PlayerIDList",
        "PlusMinus",
        "Rank",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "ShotClockRange",
        "VsConference",
        "VsDivision",
        "VsPlayerIDList"
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
        "PlayerIDList",
        "PlusMinus",
        "Rank",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "VsConference",
        "VsDivision",
        "VsPlayerIDList"
    ],
    "status": "success"
}
```

Last validated 2018-10-08