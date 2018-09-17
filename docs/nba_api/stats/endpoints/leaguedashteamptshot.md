# LeagueDashTeamPtShot

##### Endpoint URL
>[https://stats.nba.com/stats/leaguedashteamptshot](https://stats.nba.com/stats/leaguedashteamptshot)

##### Valid URL
>[https://stats.nba.com/stats/leaguedashteamptshot?CloseDefDistRange=&Conference=&DateFrom=&DateTo=&Division=&DribbleRange=&GameSegment=&GeneralRange=&LastNGames=&LeagueID=00&Location=&Month=&OpponentTeamID=&Outcome=&PORound=&PerMode=Totals&Period=&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&ShotDistRange=&TeamID=&TouchTimeRange=&VsConference=&VsDivision=](https://stats.nba.com/stats/leaguedashteamptshot?CloseDefDistRange=&Conference=&DateFrom=&DateTo=&Division=&DribbleRange=&GameSegment=&GeneralRange=&LastNGames=&LeagueID=00&Location=&Month=&OpponentTeamID=&Outcome=&PORound=&PerMode=Totals&Period=&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&ShotDistRange=&TeamID=&TouchTimeRange=&VsConference=&VsDivision=)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**LeagueID**_ | `^\d{2}$` | `Y` |  | 
_**PerMode**_ | `^(Totals)\|(PerGame)$` | `Y` |  | 
_**Season**_ | `^\d{4}-\d{2}$` | `Y` |  | 
_**SeasonType**_ | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$` | `Y` |  | 
_**VsDivision**_ | `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$` |  | `Y` | 
_**VsConference**_ | `^((East)\|(West))?$` |  | `Y` | 
_**TouchTimeRange**_ |  |  | `Y` | 
_**TeamID**_ |  |  | `Y` | 
_**ShotDistRange**_ |  |  | `Y` | 
_**ShotClockRange**_ |  |  | `Y` | 
_**SeasonSegment**_ | `^((Post All-Star)\|(Pre All-Star))?$` |  | `Y` | 
_**Period**_ |  |  | `Y` | 
_**PORound**_ |  |  | `Y` | 
_**Outcome**_ | `^((W)\|(L))?$` |  | `Y` | 
_**OpponentTeamID**_ |  |  | `Y` | 
_**Month**_ |  |  | `Y` | 
_**Location**_ | `^((Home)\|(Road))?$` |  | `Y` | 
_**LastNGames**_ |  |  | `Y` | 
_**GeneralRange**_ |  |  | `Y` | 
_**GameSegment**_ | `^((First Half)\|(Overtime)\|(Second Half))?$` |  | `Y` | 
_**DribbleRange**_ |  |  | `Y` | 
_**Division**_ | `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$` |  | `Y` | 
_**DateTo**_ |  |  | `Y` | 
_**DateFrom**_ |  |  | `Y` | 
_**Conference**_ | `^((East)\|(West))?$` |  | `Y` | 
_**CloseDefDistRange**_ |  |  | `Y` | 

## Data Sets
#### LeagueDashPTShots `league_dash_ptshots`
```text
['TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'GP', 'G', 'FGA_FREQUENCY', 'FGM', 'FGA', 'FG_PCT', 'EFG_PCT', 'FG2A_FREQUENCY', 'FG2M', 'FG2A', 'FG2_PCT', 'FG3A_FREQUENCY', 'FG3M', 'FG3A', 'FG3_PCT']
```


## JSON
```json
{
    "data_sets": {
        "LeagueDashPTShots": [
            "TEAM_ID",
            "TEAM_NAME",
            "TEAM_ABBREVIATION",
            "GP",
            "G",
            "FGA_FREQUENCY",
            "FGM",
            "FGA",
            "FG_PCT",
            "EFG_PCT",
            "FG2A_FREQUENCY",
            "FG2M",
            "FG2A",
            "FG2_PCT",
            "FG3A_FREQUENCY",
            "FG3M",
            "FG3A",
            "FG3_PCT"
        ]
    },
    "endpoint": "LeagueDashTeamPtShot",
    "nullable_parameters": [
        "CloseDefDistRange",
        "Conference",
        "DateFrom",
        "DateTo",
        "Division",
        "DribbleRange",
        "GameSegment",
        "GeneralRange",
        "LastNGames",
        "Location",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "PORound",
        "Period",
        "SeasonSegment",
        "ShotClockRange",
        "ShotDistRange",
        "TeamID",
        "TouchTimeRange",
        "VsConference",
        "VsDivision"
    ],
    "parameter_patterns": {
        "CloseDefDistRange": null,
        "Conference": "^((East)|(West))?$",
        "DateFrom": null,
        "DateTo": null,
        "Division": "^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$",
        "DribbleRange": null,
        "GameSegment": "^((First Half)|(Overtime)|(Second Half))?$",
        "GeneralRange": null,
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
        "ShotClockRange": null,
        "ShotDistRange": null,
        "TeamID": null,
        "TouchTimeRange": null,
        "VsConference": "^((East)|(West))?$",
        "VsDivision": "^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$"
    },
    "parameters": [
        "CloseDefDistRange",
        "Conference",
        "DateFrom",
        "DateTo",
        "Division",
        "DribbleRange",
        "GameSegment",
        "GeneralRange",
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
        "ShotClockRange",
        "ShotDistRange",
        "TeamID",
        "TouchTimeRange",
        "VsConference",
        "VsDivision"
    ],
    "required_parameters": [
        "LeagueID",
        "PerMode",
        "Season",
        "SeasonType"
    ],
    "status": "success"
}
```

Last validated 2018-09-16