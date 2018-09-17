# LeagueDashPtDefend

##### Endpoint URL
>[https://stats.nba.com/stats/leaguedashptdefend](https://stats.nba.com/stats/leaguedashptdefend)

##### Valid URL
>[https://stats.nba.com/stats/leaguedashptdefend?College=&Conference=&Country=&DateFrom=&DateTo=&DefenseCategory=Overall&Division=&DraftPick=&DraftYear=&GameSegment=&Height=&LastNGames=&LeagueID=00&Location=&Month=&OpponentTeamID=&Outcome=&PORound=&PerMode=Totals&Period=&PlayerExperience=&PlayerID=&PlayerPosition=&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=&VsConference=&VsDivision=&Weight=](https://stats.nba.com/stats/leaguedashptdefend?College=&Conference=&Country=&DateFrom=&DateTo=&DefenseCategory=Overall&Division=&DraftPick=&DraftYear=&GameSegment=&Height=&LastNGames=&LeagueID=00&Location=&Month=&OpponentTeamID=&Outcome=&PORound=&PerMode=Totals&Period=&PlayerExperience=&PlayerID=&PlayerPosition=&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=&VsConference=&VsDivision=&Weight=)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**DefenseCategory**_ | `^((Overall)|(3 Pointers)|(2 Pointers)|(Less Than 6Ft)|(Less Than 10Ft)|(Greater Than 15Ft))?$` | `Y` |  | 
_**LeagueID**_ | `^\d{2}$` | `Y` |  | 
_**PerMode**_ | `^(Totals)|(PerGame)$` | `Y` |  | 
_**Season**_ | `^\d{4}-\d{2}$` | `Y` |  | 
_**SeasonType**_ | `^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$` | `Y` |  | 
_**Weight**_ |  |  | `Y` | 
_**VsDivision**_ | `^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$` |  | `Y` | 
_**VsConference**_ | `^((East)|(West))?$` |  | `Y` | 
_**TeamID**_ |  |  | `Y` | 
_**StarterBench**_ |  |  | `Y` | 
_**SeasonSegment**_ | `^((Post All-Star)|(Pre All-Star))?$` |  | `Y` | 
_**PlayerPosition**_ |  |  | `Y` | 
_**PlayerID**_ |  |  | `Y` | 
_**PlayerExperience**_ |  |  | `Y` | 
_**Period**_ |  |  | `Y` | 
_**PORound**_ |  |  | `Y` | 
_**Outcome**_ | `^((W)|(L))?$` |  | `Y` | 
_**OpponentTeamID**_ |  |  | `Y` | 
_**Month**_ |  |  | `Y` | 
_**Location**_ | `^((Home)|(Road))?$` |  | `Y` | 
_**LastNGames**_ |  |  | `Y` | 
_**Height**_ |  |  | `Y` | 
_**GameSegment**_ | `^((First Half)|(Overtime)|(Second Half))?$` |  | `Y` | 
_**DraftYear**_ |  |  | `Y` | 
_**DraftPick**_ |  |  | `Y` | 
_**Division**_ | `^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$` |  | `Y` | 
_**DateTo**_ |  |  | `Y` | 
_**DateFrom**_ |  |  | `Y` | 
_**Country**_ |  |  | `Y` | 
_**Conference**_ | `^((East)|(West))?$` |  | `Y` | 
_**College**_ |  |  | `Y` | 

## Data Sets
#### LeagueDashPTDefend `league_dash_p_tdefend`
```text
['CLOSE_DEF_PERSON_ID', 'PLAYER_NAME', 'PLAYER_LAST_TEAM_ID', 'PLAYER_LAST_TEAM_ABBREVIATION', 'PLAYER_POSITION', 'AGE', 'GP', 'G', 'FREQ', 'D_FGM', 'D_FGA', 'D_FG_PCT', 'NORMAL_FG_PCT', 'PCT_PLUSMINUS']
```


## JSON
```json
{
    "data_sets": {
        "LeagueDashPTDefend": [
            "CLOSE_DEF_PERSON_ID",
            "PLAYER_NAME",
            "PLAYER_LAST_TEAM_ID",
            "PLAYER_LAST_TEAM_ABBREVIATION",
            "PLAYER_POSITION",
            "AGE",
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
    "endpoint": "LeagueDashPtDefend",
    "nullable_parameters": [
        "College",
        "Conference",
        "Country",
        "DateFrom",
        "DateTo",
        "Division",
        "DraftPick",
        "DraftYear",
        "GameSegment",
        "Height",
        "LastNGames",
        "Location",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "PORound",
        "Period",
        "PlayerExperience",
        "PlayerID",
        "PlayerPosition",
        "SeasonSegment",
        "StarterBench",
        "TeamID",
        "VsConference",
        "VsDivision",
        "Weight"
    ],
    "parameter_patterns": {
        "College": null,
        "Conference": "^((East)|(West))?$",
        "Country": null,
        "DateFrom": null,
        "DateTo": null,
        "DefenseCategory": "^((Overall)|(3 Pointers)|(2 Pointers)|(Less Than 6Ft)|(Less Than 10Ft)|(Greater Than 15Ft))?$",
        "Division": "^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$",
        "DraftPick": null,
        "DraftYear": null,
        "GameSegment": "^((First Half)|(Overtime)|(Second Half))?$",
        "Height": null,
        "LastNGames": null,
        "LeagueID": "^\\d{2}$",
        "Location": "^((Home)|(Road))?$",
        "Month": null,
        "OpponentTeamID": null,
        "Outcome": "^((W)|(L))?$",
        "PORound": null,
        "PerMode": "^(Totals)|(PerGame)$",
        "Period": null,
        "PlayerExperience": null,
        "PlayerID": null,
        "PlayerPosition": null,
        "Season": "^\\d{4}-\\d{2}$",
        "SeasonSegment": "^((Post All-Star)|(Pre All-Star))?$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$",
        "StarterBench": null,
        "TeamID": null,
        "VsConference": "^((East)|(West))?$",
        "VsDivision": "^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$",
        "Weight": null
    },
    "parameters": [
        "College",
        "Conference",
        "Country",
        "DateFrom",
        "DateTo",
        "DefenseCategory",
        "Division",
        "DraftPick",
        "DraftYear",
        "GameSegment",
        "Height",
        "LastNGames",
        "LeagueID",
        "Location",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "PORound",
        "PerMode",
        "Period",
        "PlayerExperience",
        "PlayerID",
        "PlayerPosition",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "StarterBench",
        "TeamID",
        "VsConference",
        "VsDivision",
        "Weight"
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