# LeagueDashPlayerStats

##### Endpoint URL
>[https://stats.nba.com/stats/leaguedashplayerstats](https://stats.nba.com/stats/leaguedashplayerstats)

##### Valid URL
>[https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=10&LeagueID=&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=&PaceAdjust=N&PerMode=Totals&Period=1&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=&VsConference=&VsDivision=&Weight=](https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=10&LeagueID=&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=&PaceAdjust=N&PerMode=Totals&Period=1&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=&VsConference=&VsDivision=&Weight=)

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
_**PlusMinus**_ | `^(Y)\|(N)$` | `Y` |  | 
_**Rank**_ | `^(Y)\|(N)$` | `Y` |  | 
_**Season**_ | `^\d{4}-\d{2}$` | `Y` |  | 
_**SeasonType**_ | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$` | `Y` |  | 
_**Weight**_ |  |  | `Y` | 
_**VsDivision**_ | `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$` | `Y` | `Y` | 
_**VsConference**_ | `^((East)\|(West))?$` | `Y` | `Y` | 
_**TeamID**_ |  |  | `Y` | 
_**StarterBench**_ | `((Starters)\|(Bench))?` | `Y` | `Y` | 
_**ShotClockRange**_ | `((24-22)\|(22-18 Very Early)\|(18-15 Early)\|(15-7 Average)\|(7-4 Late)\|(4-0 Very Late)\|(ShotClock Off))?` |  | `Y` | 
_**SeasonSegment**_ | `^((Post All-Star)\|(Pre All-Star))?$` | `Y` | `Y` | 
_**PlayerPosition**_ | `((F)\|(C)\|(G)\|(C-F)\|(F-C)\|(F-G)\|(G-F))?` | `Y` | `Y` | 
_**PlayerExperience**_ | `((Rookie)\|(Sophomore)\|(Veteran))?` | `Y` | `Y` | 
_**PORound**_ |  |  | `Y` | 
_**Outcome**_ | `^((W)\|(L))?$` | `Y` | `Y` | 
_**Location**_ | `^((Home)\|(Road))?$` | `Y` | `Y` | 
_**LeagueID**_ | `(00)\|(20)\|(10)` |  | `Y` | 
_**Height**_ |  |  | `Y` | 
_**GameSegment**_ | `^((First Half)\|(Overtime)\|(Second Half))?$` | `Y` | `Y` | 
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
#### LeagueDashPlayerStats `league_dash_player_stats`
```text
['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_ABBREVIATION', 'AGE', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'NBA_FANTASY_PTS', 'DD2', 'TD3', 'GP_RANK', 'W_RANK', 'L_RANK', 'W_PCT_RANK', 'MIN_RANK', 'FGM_RANK', 'FGA_RANK', 'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 'FTM_RANK', 'FTA_RANK', 'FT_PCT_RANK', 'OREB_RANK', 'DREB_RANK', 'REB_RANK', 'AST_RANK', 'TOV_RANK', 'STL_RANK', 'BLK_RANK', 'BLKA_RANK', 'PF_RANK', 'PFD_RANK', 'PTS_RANK', 'PLUS_MINUS_RANK', 'NBA_FANTASY_PTS_RANK', 'DD2_RANK', 'TD3_RANK', 'CFID', 'CFPARAMS']
```


## JSON
```json
{
    "data_sets": {
        "LeagueDashPlayerStats": [
            "PLAYER_ID",
            "PLAYER_NAME",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "AGE",
            "GP",
            "W",
            "L",
            "W_PCT",
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
            "PLUS_MINUS",
            "NBA_FANTASY_PTS",
            "DD2",
            "TD3",
            "GP_RANK",
            "W_RANK",
            "L_RANK",
            "W_PCT_RANK",
            "MIN_RANK",
            "FGM_RANK",
            "FGA_RANK",
            "FG_PCT_RANK",
            "FG3M_RANK",
            "FG3A_RANK",
            "FG3_PCT_RANK",
            "FTM_RANK",
            "FTA_RANK",
            "FT_PCT_RANK",
            "OREB_RANK",
            "DREB_RANK",
            "REB_RANK",
            "AST_RANK",
            "TOV_RANK",
            "STL_RANK",
            "BLK_RANK",
            "BLKA_RANK",
            "PF_RANK",
            "PFD_RANK",
            "PTS_RANK",
            "PLUS_MINUS_RANK",
            "NBA_FANTASY_PTS_RANK",
            "DD2_RANK",
            "TD3_RANK",
            "CFID",
            "CFPARAMS"
        ]
    },
    "endpoint": "LeagueDashPlayerStats",
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
        "MeasureType": "^(Base)|(Advanced)|(Misc)|(Four Factors)|(Scoring)|(Opponent)|(Usage)|(Defense)$",
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
        "VsDivision",
        "Weight"
    ],
    "required_parameters": [
        "DateFrom",
        "DateTo",
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

Last validated 2018-10-08