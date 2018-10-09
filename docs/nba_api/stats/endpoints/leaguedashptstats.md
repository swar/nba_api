# LeagueDashPtStats

##### Endpoint URL
>[https://stats.nba.com/stats/leaguedashptstats](https://stats.nba.com/stats/leaguedashptstats)

##### Valid URL
>[https://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=10&LeagueID=&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=&PerMode=Totals&PlayerExperience=&PlayerOrTeam=Team&PlayerPosition=&PtMeasureType=SpeedDistance&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=&VsConference=&VsDivision=&Weight=](https://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=10&LeagueID=&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=&PerMode=Totals&PlayerExperience=&PlayerOrTeam=Team&PlayerPosition=&PtMeasureType=SpeedDistance&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=&VsConference=&VsDivision=&Weight=)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**LastNGames**_ |  | `Y` |  | 
_**Month**_ |  | `Y` |  | 
_**OpponentTeamID**_ |  | `Y` |  | 
_**PerMode**_ | `^(Totals)\|(PerGame)$` | `Y` |  | 
_**PlayerOrTeam**_ | `^(Player)\|(Team)$` | `Y` |  | 
_**PtMeasureType**_ | `^(SpeedDistance)\|(Rebounding)\|(Possessions)\|(CatchShoot)\|(PullUpShot)\|(Defense)\|(Drives)\|(Passing)\|(ElbowTouch)\|(PostTouch)\|(PaintTouch)\|(Efficiency)$` | `Y` |  | 
_**Season**_ | `^\d{4}-\d{2}$` | `Y` |  | 
_**SeasonType**_ | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$` | `Y` |  | 
_**Weight**_ |  |  | `Y` | 
_**VsDivision**_ | `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$` | `Y` | `Y` | 
_**VsConference**_ | `^((East)\|(West))?$` | `Y` | `Y` | 
_**TeamID**_ |  |  | `Y` | 
_**StarterBench**_ | `((Starters)\|(Bench))?` | `Y` | `Y` | 
_**SeasonSegment**_ | `^((Post All-Star)\|(Pre All-Star))?$` | `Y` | `Y` | 
_**PlayerPosition**_ | `((F)\|(C)\|(G)\|(C-F)\|(F-C)\|(F-G)\|(G-F))?` | `Y` | `Y` | 
_**PlayerExperience**_ | `((Rookie)\|(Sophomore)\|(Veteran))?` | `Y` | `Y` | 
_**PORound**_ |  |  | `Y` | 
_**Outcome**_ | `^((W)\|(L))?$` | `Y` | `Y` | 
_**Location**_ | `^((Home)\|(Road))?$` | `Y` | `Y` | 
_**LeagueID**_ | `(00)\|(20)\|(10)` |  | `Y` | 
_**Height**_ |  |  | `Y` | 
_**GameScope**_ | `((Yesterday)\|(Last 10))?` | `Y` | `Y` | 
_**DraftYear**_ |  |  | `Y` | 
_**DraftPick**_ |  |  | `Y` | 
_**Division**_ | `((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest))?` |  | `Y` | 
_**DateTo**_ |  | `Y` | `Y` | 
_**DateFrom**_ |  | `Y` | `Y` | 
_**Country**_ |  |  | `Y` | 
_**Conference**_ | `((East)\|(West))?` |  | `Y` | 
_**College**_ |  |  | `Y` | 

## Data Sets
#### LeagueDashPtStats `league_dash_pt_stats`
```text
['TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'GP', 'W', 'L', 'MIN', 'DIST_FEET', 'DIST_MILES', 'DIST_MILES_OFF', 'DIST_MILES_DEF', 'AVG_SPEED', 'AVG_SPEED_OFF', 'AVG_SPEED_DEF']
```


## JSON
```json
{
    "data_sets": {
        "LeagueDashPtStats": [
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "GP",
            "W",
            "L",
            "MIN",
            "DIST_FEET",
            "DIST_MILES",
            "DIST_MILES_OFF",
            "DIST_MILES_DEF",
            "AVG_SPEED",
            "AVG_SPEED_OFF",
            "AVG_SPEED_DEF"
        ]
    },
    "endpoint": "LeagueDashPtStats",
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
        "Height",
        "LeagueID",
        "Location",
        "Outcome",
        "PORound",
        "PlayerExperience",
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
        "Conference": "((East)|(West))?",
        "Country": null,
        "DateFrom": null,
        "DateTo": null,
        "Division": "((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest))?",
        "DraftPick": null,
        "DraftYear": null,
        "GameScope": "((Yesterday)|(Last 10))?",
        "Height": null,
        "LastNGames": null,
        "LeagueID": "(00)|(20)|(10)",
        "Location": "^((Home)|(Road))?$",
        "Month": null,
        "OpponentTeamID": null,
        "Outcome": "^((W)|(L))?$",
        "PORound": null,
        "PerMode": "^(Totals)|(PerGame)$",
        "PlayerExperience": "((Rookie)|(Sophomore)|(Veteran))?",
        "PlayerOrTeam": "^(Player)|(Team)$",
        "PlayerPosition": "((F)|(C)|(G)|(C-F)|(F-C)|(F-G)|(G-F))?",
        "PtMeasureType": "^(SpeedDistance)|(Rebounding)|(Possessions)|(CatchShoot)|(PullUpShot)|(Defense)|(Drives)|(Passing)|(ElbowTouch)|(PostTouch)|(PaintTouch)|(Efficiency)$",
        "Season": "^\\d{4}-\\d{2}$",
        "SeasonSegment": "^((Post All-Star)|(Pre All-Star))?$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$",
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
        "Height",
        "LastNGames",
        "LeagueID",
        "Location",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "PORound",
        "PerMode",
        "PlayerExperience",
        "PlayerOrTeam",
        "PlayerPosition",
        "PtMeasureType",
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
        "DateFrom",
        "DateTo",
        "GameScope",
        "LastNGames",
        "Location",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "PerMode",
        "PlayerExperience",
        "PlayerOrTeam",
        "PlayerPosition",
        "PtMeasureType",
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

Last validated 2018-10-08