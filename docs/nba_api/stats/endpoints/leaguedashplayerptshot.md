# LeagueDashPlayerPtShot

##### Endpoint URL
>[https://stats.nba.com/stats/leaguedashplayerptshot](https://stats.nba.com/stats/leaguedashplayerptshot)

##### Valid URL
>[https://stats.nba.com/stats/leaguedashplayerptshot?CloseDefDistRange=&College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&DribbleRange=&GameSegment=&GeneralRange=&Height=&LastNGames=&LeagueID=00&Location=&Month=&OpponentTeamID=&Outcome=&PORound=&PerMode=Totals&Period=&PlayerExperience=&PlayerPosition=&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&ShotDistRange=&StarterBench=&TeamID=&TouchTimeRange=&VsConference=&VsDivision=&Weight=](https://stats.nba.com/stats/leaguedashplayerptshot?CloseDefDistRange=&College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&DribbleRange=&GameSegment=&GeneralRange=&Height=&LastNGames=&LeagueID=00&Location=&Month=&OpponentTeamID=&Outcome=&PORound=&PerMode=Totals&Period=&PlayerExperience=&PlayerPosition=&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&ShotDistRange=&StarterBench=&TeamID=&TouchTimeRange=&VsConference=&VsDivision=&Weight=)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**LeagueID**_ | `^\d{2}$` | `Y` |  | 
_**PerMode**_ | `^(Totals)\|(PerGame)$` | `Y` |  | 
_**Season**_ | `^\d{4}-\d{2}$` | `Y` |  | 
_**SeasonType**_ | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$` | `Y` |  | 
_**Weight**_ |  |  | `Y` | 
_**VsDivision**_ | `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$` |  | `Y` | 
_**VsConference**_ | `^((East)\|(West))?$` |  | `Y` | 
_**TouchTimeRange**_ |  |  | `Y` | 
_**TeamID**_ |  |  | `Y` | 
_**StarterBench**_ |  |  | `Y` | 
_**ShotDistRange**_ |  |  | `Y` | 
_**ShotClockRange**_ |  |  | `Y` | 
_**SeasonSegment**_ | `^((Post All-Star)\|(Pre All-Star))?$` |  | `Y` | 
_**PlayerPosition**_ |  |  | `Y` | 
_**PlayerExperience**_ |  |  | `Y` | 
_**Period**_ |  |  | `Y` | 
_**PORound**_ |  |  | `Y` | 
_**Outcome**_ | `^((W)\|(L))?$` |  | `Y` | 
_**OpponentTeamID**_ |  |  | `Y` | 
_**Month**_ |  |  | `Y` | 
_**Location**_ | `^((Home)\|(Road))?$` |  | `Y` | 
_**LastNGames**_ |  |  | `Y` | 
_**Height**_ |  |  | `Y` | 
_**GeneralRange**_ |  |  | `Y` | 
_**GameSegment**_ | `^((First Half)\|(Overtime)\|(Second Half))?$` |  | `Y` | 
_**DribbleRange**_ |  |  | `Y` | 
_**DraftYear**_ |  |  | `Y` | 
_**DraftPick**_ |  |  | `Y` | 
_**Division**_ | `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$` |  | `Y` | 
_**DateTo**_ |  |  | `Y` | 
_**DateFrom**_ |  |  | `Y` | 
_**Country**_ |  |  | `Y` | 
_**Conference**_ | `^((East)\|(West))?$` |  | `Y` | 
_**College**_ |  |  | `Y` | 
_**CloseDefDistRange**_ |  |  | `Y` | 

## Data Sets
#### LeagueDashPTShots `league_dash_ptshots`
```text
['PLAYER_ID', 'PLAYER_NAME', 'PLAYER_LAST_TEAM_ID', 'PLAYER_LAST_TEAM_ABBREVIATION', 'AGE', 'GP', 'G', 'FGA_FREQUENCY', 'FGM', 'FGA', 'FG_PCT', 'EFG_PCT', 'FG2A_FREQUENCY', 'FG2M', 'FG2A', 'FG2_PCT', 'FG3A_FREQUENCY', 'FG3M', 'FG3A', 'FG3_PCT']
```


## JSON
```json
{
    "data_sets": {
        "LeagueDashPTShots": [
            "PLAYER_ID",
            "PLAYER_NAME",
            "PLAYER_LAST_TEAM_ID",
            "PLAYER_LAST_TEAM_ABBREVIATION",
            "AGE",
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
    "endpoint": "LeagueDashPlayerPtShot",
    "last_validated_date": "2018-10-08",
    "nullable_parameters": [
        "CloseDefDistRange",
        "College",
        "Conference",
        "Country",
        "DateFrom",
        "DateTo",
        "Division",
        "DraftPick",
        "DraftYear",
        "DribbleRange",
        "GameSegment",
        "GeneralRange",
        "Height",
        "LastNGames",
        "Location",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "PORound",
        "Period",
        "PlayerExperience",
        "PlayerPosition",
        "SeasonSegment",
        "ShotClockRange",
        "ShotDistRange",
        "StarterBench",
        "TeamID",
        "TouchTimeRange",
        "VsConference",
        "VsDivision",
        "Weight"
    ],
    "parameter_patterns": {
        "CloseDefDistRange": null,
        "College": null,
        "Conference": "^((East)|(West))?$",
        "Country": null,
        "DateFrom": null,
        "DateTo": null,
        "Division": "^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$",
        "DraftPick": null,
        "DraftYear": null,
        "DribbleRange": null,
        "GameSegment": "^((First Half)|(Overtime)|(Second Half))?$",
        "GeneralRange": null,
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
        "PlayerPosition": null,
        "Season": "^\\d{4}-\\d{2}$",
        "SeasonSegment": "^((Post All-Star)|(Pre All-Star))?$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$",
        "ShotClockRange": null,
        "ShotDistRange": null,
        "StarterBench": null,
        "TeamID": null,
        "TouchTimeRange": null,
        "VsConference": "^((East)|(West))?$",
        "VsDivision": "^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$",
        "Weight": null
    },
    "parameters": [
        "CloseDefDistRange",
        "College",
        "Conference",
        "Country",
        "DateFrom",
        "DateTo",
        "Division",
        "DraftPick",
        "DraftYear",
        "DribbleRange",
        "GameSegment",
        "GeneralRange",
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
        "PlayerPosition",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "ShotClockRange",
        "ShotDistRange",
        "StarterBench",
        "TeamID",
        "TouchTimeRange",
        "VsConference",
        "VsDivision",
        "Weight"
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

Last validated 2018-10-08