# LeagueDashPtTeamDefend

##### Endpoint URL
>[https://stats.nba.com/stats/leaguedashptteamdefend](https://stats.nba.com/stats/leaguedashptteamdefend)

##### Valid URL
>[https://stats.nba.com/stats/leaguedashptteamdefend?Conference=&DateFrom=&DateTo=&DefenseCategory=Overall&Division=&GameSegment=&LastNGames=&LeagueID=00&Location=&Month=&OpponentTeamID=&Outcome=&PORound=&PerMode=Totals&Period=&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&TeamID=&VsConference=&VsDivision=](https://stats.nba.com/stats/leaguedashptteamdefend?Conference=&DateFrom=&DateTo=&DefenseCategory=Overall&Division=&GameSegment=&LastNGames=&LeagueID=00&Location=&Month=&OpponentTeamID=&Outcome=&PORound=&PerMode=Totals&Period=&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&TeamID=&VsConference=&VsDivision=)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**DefenseCategory**_ | `^((Overall)\|(3 Pointers)\|(2 Pointers)\|(Less Than 6Ft)\|(Less Than 10Ft)\|(Greater Than 15Ft))?$` | `Y` |  | 
_**LeagueID**_ | `^\d{2}$` | `Y` |  | 
_**PerMode**_ | `^(Totals)\|(PerGame)$` | `Y` |  | 
_**Season**_ | `^\d{4}-\d{2}$` | `Y` |  | 
_**SeasonType**_ | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$` | `Y` |  | 
_**VsDivision**_ | `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$` |  | `Y` | 
_**VsConference**_ | `^((East)\|(West))?$` |  | `Y` | 
_**TeamID**_ |  |  | `Y` | 
_**SeasonSegment**_ | `^((Post All-Star)\|(Pre All-Star))?$` |  | `Y` | 
_**Period**_ |  |  | `Y` | 
_**PORound**_ |  |  | `Y` | 
_**Outcome**_ | `^((W)\|(L))?$` |  | `Y` | 
_**OpponentTeamID**_ |  |  | `Y` | 
_**Month**_ |  |  | `Y` | 
_**Location**_ | `^((Home)\|(Road))?$` |  | `Y` | 
_**LastNGames**_ |  |  | `Y` | 
_**GameSegment**_ | `^((First Half)\|(Overtime)\|(Second Half))?$` |  | `Y` | 
_**Division**_ | `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$` |  | `Y` | 
_**DateTo**_ |  |  | `Y` | 
_**DateFrom**_ |  |  | `Y` | 
_**Conference**_ | `^((East)\|(West))?$` |  | `Y` | 

## Data Sets
#### LeagueDashPtTeamDefend `league_dash_pt_team_defend`
```text
['TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'GP', 'G', 'FREQ', 'D_FGM', 'D_FGA', 'D_FG_PCT', 'NORMAL_FG_PCT', 'PCT_PLUSMINUS']
```


## JSON
```json
{
    "data_sets": {
        "LeagueDashPtTeamDefend": [
            "TEAM_ID",
            "TEAM_NAME",
            "TEAM_ABBREVIATION",
            "GP",
            "G",
            "FREQ",
            "D_FGM",
            "D_FGA",
            "D_FG_PCT",
            "NORMAL_FG_PCT",
            "PCT_PLUSMINUS"
        ]
    },
    "endpoint": "LeagueDashPtTeamDefend",
    "nullable_parameters": [
        "Conference",
        "DateFrom",
        "DateTo",
        "Division",
        "GameSegment",
        "LastNGames",
        "Location",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "PORound",
        "Period",
        "SeasonSegment",
        "TeamID",
        "VsConference",
        "VsDivision"
    ],
    "parameter_patterns": {
        "Conference": "^((East)|(West))?$",
        "DateFrom": null,
        "DateTo": null,
        "DefenseCategory": "^((Overall)|(3 Pointers)|(2 Pointers)|(Less Than 6Ft)|(Less Than 10Ft)|(Greater Than 15Ft))?$",
        "Division": "^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$",
        "GameSegment": "^((First Half)|(Overtime)|(Second Half))?$",
        "LastNGames": null,
        "LeagueID": "^\\d{2}$",
        "Location": "^((Home)|(Road))?$",
        "Month": null,
        "OpponentTeamID": null,
        "Outcome": "^((W)|(L))?$",
        "PORound": null,
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
        "Conference",
        "DateFrom",
        "DateTo",
        "DefenseCategory",
        "Division",
        "GameSegment",
        "LastNGames",
        "LeagueID",
        "Location",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "PORound",
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
        "DefenseCategory",
        "LeagueID",
        "PerMode",
        "Season",
        "SeasonType"
    ],
    "status": "success"
}
```

Last validated 2018-09-16