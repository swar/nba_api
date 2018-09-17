# PlayersVsPlayers

##### Endpoint URL
>[https://stats.nba.com/stats/playersvsplayers](https://stats.nba.com/stats/playersvsplayers)

##### Valid URL
>[https://stats.nba.com/stats/playersvsplayers?Conference=&DateFrom=&DateTo=&Division=&GameSegment=&LastNGames=10&LeagueID=&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PaceAdjust=N&PerMode=Totals&Period=1&PlayerID1=202681&PlayerID2=203078&PlayerID3=202681&PlayerID4=201567&PlayerID5=203954&PlayerTeamID=1610612739&PlusMinus=N&Rank=N&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&VsConference=&VsDivision=&VsPlayerID1=201566&VsPlayerID2=201939&VsPlayerID3=201935&VsPlayerID4=201142&VsPlayerID5=203076&VsTeamID=1610612765](https://stats.nba.com/stats/playersvsplayers?Conference=&DateFrom=&DateTo=&Division=&GameSegment=&LastNGames=10&LeagueID=&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PaceAdjust=N&PerMode=Totals&Period=1&PlayerID1=202681&PlayerID2=203078&PlayerID3=202681&PlayerID4=201567&PlayerID5=203954&PlayerTeamID=1610612739&PlusMinus=N&Rank=N&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&VsConference=&VsDivision=&VsPlayerID1=201566&VsPlayerID2=201939&VsPlayerID3=201935&VsPlayerID4=201142&VsPlayerID5=203076&VsTeamID=1610612765)

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
_**PlayerID1**_ |  | `Y` |  | 
_**PlayerID2**_ |  | `Y` |  | 
_**PlayerID3**_ |  | `Y` |  | 
_**PlayerID4**_ |  | `Y` |  | 
_**PlayerID5**_ |  | `Y` |  | 
_**PlayerTeamID**_ |  | `Y` |  | 
_**PlusMinus**_ | `^(Y)\|(N)$` | `Y` |  | 
_**Rank**_ | `^(Y)\|(N)$` | `Y` |  | 
_**Season**_ | `^\d{4}-\d{2}$` | `Y` |  | 
_**SeasonType**_ | `^(Regular Season)\|(Pre Season)\|(Playoffs)$` | `Y` |  | 
_**VsPlayerID1**_ |  | `Y` |  | 
_**VsPlayerID2**_ |  | `Y` |  | 
_**VsPlayerID3**_ |  | `Y` |  | 
_**VsPlayerID4**_ |  | `Y` |  | 
_**VsPlayerID5**_ |  | `Y` |  | 
_**VsTeamID**_ |  | `Y` |  | 
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
#### Combined `combined`
```text
['GROUP_SET', 'DESCRIPTION', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS']
```

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
        "Combined": [
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
    "endpoint": "PlayersVsPlayers",
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
        "PlayerID1": null,
        "PlayerID2": null,
        "PlayerID3": null,
        "PlayerID4": null,
        "PlayerID5": null,
        "PlayerTeamID": null,
        "PlusMinus": "^(Y)|(N)$",
        "Rank": "^(Y)|(N)$",
        "Season": "^\\d{4}-\\d{2}$",
        "SeasonSegment": "^((Post All-Star)|(Pre All-Star))?$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)$",
        "ShotClockRange": null,
        "VsConference": "^((East)|(West))?$",
        "VsDivision": "^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$",
        "VsPlayerID1": null,
        "VsPlayerID2": null,
        "VsPlayerID3": null,
        "VsPlayerID4": null,
        "VsPlayerID5": null,
        "VsTeamID": null
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
        "PlayerID1",
        "PlayerID2",
        "PlayerID3",
        "PlayerID4",
        "PlayerID5",
        "PlayerTeamID",
        "PlusMinus",
        "Rank",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "ShotClockRange",
        "VsConference",
        "VsDivision",
        "VsPlayerID1",
        "VsPlayerID2",
        "VsPlayerID3",
        "VsPlayerID4",
        "VsPlayerID5",
        "VsTeamID"
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
        "PlayerID1",
        "PlayerID2",
        "PlayerID3",
        "PlayerID4",
        "PlayerID5",
        "PlayerTeamID",
        "PlusMinus",
        "Rank",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "VsConference",
        "VsDivision",
        "VsPlayerID1",
        "VsPlayerID2",
        "VsPlayerID3",
        "VsPlayerID4",
        "VsPlayerID5",
        "VsTeamID"
    ],
    "status": "success"
}
```

Last validated 2018-09-16