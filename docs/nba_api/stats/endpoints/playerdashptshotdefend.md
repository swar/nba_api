# PlayerDashPtShotDefend

##### Endpoint URL
>[https://stats.nba.com/stats/playerdashptshotdefend](https://stats.nba.com/stats/playerdashptshotdefend)

##### Valid URL
>[https://stats.nba.com/stats/playerdashptshotdefend?DateFrom=&DateTo=&GameSegment=&LastNGames=10&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PerMode=Totals&Period=1&PlayerID=2544&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&TeamID=1610612739&VsConference=&VsDivision=](https://stats.nba.com/stats/playerdashptshotdefend?DateFrom=&DateTo=&GameSegment=&LastNGames=10&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PerMode=Totals&Period=1&PlayerID=2544&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&TeamID=1610612739&VsConference=&VsDivision=)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**LastNGames**_ |  | `Y` |  | 
_**LeagueID**_ | `(00)|(20)|(10)` |  |  | 
_**Month**_ |  | `Y` |  | 
_**OpponentTeamID**_ |  | `Y` |  | 
_**PerMode**_ | `^(Totals)|(PerGame)$` | `Y` |  | 
_**Period**_ |  | `Y` |  | 
_**PlayerID**_ |  | `Y` |  | 
_**Season**_ | `^\d{4}-\d{2}$` | `Y` |  | 
_**SeasonType**_ | `^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$` | `Y` |  | 
_**TeamID**_ |  | `Y` |  | 
_**VsDivision**_ | `^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$` | `Y` | `Y` | 
_**VsConference**_ | `^((East)|(West))?$` | `Y` | `Y` | 
_**SeasonSegment**_ | `^((Post All-Star)|(Pre All-Star))?$` | `Y` | `Y` | 
_**Outcome**_ | `^((W)|(L))?$` | `Y` | `Y` | 
_**Location**_ | `^((Home)|(Road))?$` | `Y` | `Y` | 
_**GameSegment**_ | `^((First Half)|(Overtime)|(Second Half))?$` | `Y` | `Y` | 
_**DateTo**_ |  | `Y` | `Y` | 
_**DateFrom**_ |  | `Y` | `Y` | 

## Data Sets
#### DefendingShots `defending_shots`
```text
['CLOSE_DEF_PERSON_ID', 'GP', 'G', 'DEFENSE_CATEGORY', 'FREQ', 'D_FGM', 'D_FGA', 'D_FG_PCT', 'NORMAL_FG_PCT', 'PCT_PLUSMINUS']
```


## JSON
```json
{
    "data_sets": {
        "DefendingShots": [
            "CLOSE_DEF_PERSON_ID",
            "GP",
            "G",
            "DEFENSE_CATEGORY",
            "FREQ",
            "D_FGM",
            "D_FGA",
            "D_FG_PCT",
            "NORMAL_FG_PCT",
            "PCT_PLUSMINUS"
        ]
    },
    "endpoint": "PlayerDashPtShotDefend",
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