# LeagueDashPlayerBioStats

##### Endpoint URL
>[https://stats.nba.com/stats/leaguedashplayerbiostats](https://stats.nba.com/stats/leaguedashplayerbiostats)

##### Valid URL
>[https://stats.nba.com/stats/leaguedashplayerbiostats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=&LeagueID=&Location=&Month=&OpponentTeamID=&Outcome=&PORound=&PerMode=Totals&Period=&PlayerExperience=&PlayerPosition=&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=&VsConference=&VsDivision=&Weight=](https://stats.nba.com/stats/leaguedashplayerbiostats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=&LeagueID=&Location=&Month=&OpponentTeamID=&Outcome=&PORound=&PerMode=Totals&Period=&PlayerExperience=&PlayerPosition=&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=&VsConference=&VsDivision=&Weight=)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**PerMode**_ | `^(Totals)\|(PerGame)$` | `Y` |  | 
_**Season**_ | `^\d{4}-\d{2}$` | `Y` |  | 
_**SeasonType**_ | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$` | `Y` |  | 
_**Weight**_ |  |  | `Y` | 
_**VsDivision**_ | `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$` |  | `Y` | 
_**VsConference**_ | `^((East)\|(West))?$` |  | `Y` | 
_**TeamID**_ |  |  | `Y` | 
_**StarterBench**_ | `((Starters)\|(Bench))?` |  | `Y` | 
_**ShotClockRange**_ | `((24-22)\|(22-18 Very Early)\|(18-15 Early)\|(15-7 Average)\|(7-4 Late)\|(4-0 Very Late)\|(ShotClock Off))?` |  | `Y` | 
_**SeasonSegment**_ | `^((Post All-Star)\|(Pre All-Star))?$` |  | `Y` | 
_**PlayerPosition**_ | `((F)\|(C)\|(G)\|(C-F)\|(F-C)\|(F-G)\|(G-F))?` |  | `Y` | 
_**PlayerExperience**_ | `((Rookie)\|(Sophomore)\|(Veteran))?` |  | `Y` | 
_**Period**_ |  |  | `Y` | 
_**PORound**_ |  |  | `Y` | 
_**Outcome**_ | `^((W)\|(L))?$` |  | `Y` | 
_**OpponentTeamID**_ |  |  | `Y` | 
_**Month**_ |  |  | `Y` | 
_**Location**_ | `^((Home)\|(Road))?$` |  | `Y` | 
_**LeagueID**_ | `(00)\|(20)\|(10)` | `Y` | `Y` | 
_**LastNGames**_ |  |  | `Y` | 
_**Height**_ |  |  | `Y` | 
_**GameSegment**_ | `^((First Half)\|(Overtime)\|(Second Half))?$` |  | `Y` | 
_**GameScope**_ | `((Yesterday)\|(Last 10))?` |  | `Y` | 
_**DraftYear**_ |  |  | `Y` | 
_**DraftPick**_ |  |  | `Y` | 
_**Division**_ | `((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest))?` |  | `Y` | 
_**DateTo**_ |  |  | `Y` | 
_**DateFrom**_ |  |  | `Y` | 
_**Country**_ |  |  | `Y` | 
_**Conference**_ | `((East)\|(West))?` |  | `Y` | 
_**College**_ |  |  | `Y` | 

## Data Sets
#### LeagueDashPlayerBioStats `league_dash_player_bio_stats`
```text
['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_ABBREVIATION', 'AGE', 'PLAYER_HEIGHT', 'PLAYER_HEIGHT_INCHES', 'PLAYER_WEIGHT', 'COLLEGE', 'COUNTRY', 'DRAFT_YEAR', 'DRAFT_ROUND', 'DRAFT_NUMBER', 'GP', 'PTS', 'REB', 'AST', 'NET_RATING', 'OREB_PCT', 'DREB_PCT', 'USG_PCT', 'TS_PCT', 'AST_PCT']
```


## JSON
```json
{
    "data_sets": {
        "LeagueDashPlayerBioStats": [
            "PLAYER_ID",
            "PLAYER_NAME",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "AGE",
            "PLAYER_HEIGHT",
            "PLAYER_HEIGHT_INCHES",
            "PLAYER_WEIGHT",
            "COLLEGE",
            "COUNTRY",
            "DRAFT_YEAR",
            "DRAFT_ROUND",
            "DRAFT_NUMBER",
            "GP",
            "PTS",
            "REB",
            "AST",
            "NET_RATING",
            "OREB_PCT",
            "DREB_PCT",
            "USG_PCT",
            "TS_PCT",
            "AST_PCT"
        ]
    },
    "endpoint": "LeagueDashPlayerBioStats",
    "last_validated_date": "2018-10-08",
    "nullable_parameters": [
        "College",
        "Conference",
        "Country",
        "DateFrom",
        "DateTo",
        "Division",
        "DraftPick",
        "DraftYear",
        "GameScope",
        "GameSegment",
        "Height",
        "LastNGames",
        "LeagueID",
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
        "StarterBench",
        "TeamID",
        "VsConference",
        "VsDivision",
        "Weight"
    ],
    "parameter_patterns": {
        "College": null,
        "Conference": "((East)|(West))?",
        "Country": null,
        "DateFrom": null,
        "DateTo": null,
        "Division": "((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest))?",
        "DraftPick": null,
        "DraftYear": null,
        "GameScope": "((Yesterday)|(Last 10))?",
        "GameSegment": "^((First Half)|(Overtime)|(Second Half))?$",
        "Height": null,
        "LastNGames": null,
        "LeagueID": "(00)|(20)|(10)",
        "Location": "^((Home)|(Road))?$",
        "Month": null,
        "OpponentTeamID": null,
        "Outcome": "^((W)|(L))?$",
        "PORound": null,
        "PerMode": "^(Totals)|(PerGame)$",
        "Period": null,
        "PlayerExperience": "((Rookie)|(Sophomore)|(Veteran))?",
        "PlayerPosition": "((F)|(C)|(G)|(C-F)|(F-C)|(F-G)|(G-F))?",
        "Season": "^\\d{4}-\\d{2}$",
        "SeasonSegment": "^((Post All-Star)|(Pre All-Star))?$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$",
        "ShotClockRange": "((24-22)|(22-18 Very Early)|(18-15 Early)|(15-7 Average)|(7-4 Late)|(4-0 Very Late)|(ShotClock Off))?",
        "StarterBench": "((Starters)|(Bench))?",
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
        "Division",
        "DraftPick",
        "DraftYear",
        "GameScope",
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
        "PlayerPosition",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "ShotClockRange",
        "StarterBench",
        "TeamID",
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