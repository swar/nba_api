# LeagueDashTeamStats
##### [nba_api/stats/endpoints/leaguedashteamstats.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/leaguedashteamstats.py)

##### Endpoint URL
>[https://stats.nba.com/stats/leaguedashteamstats](https://stats.nba.com/stats/leaguedashteamstats)

##### Valid URL
>[https://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&LastNGames=0&LeagueID=&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=&PaceAdjust=N&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2019-20&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=&TwoWay=&VsConference=&VsDivision=](https://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&LastNGames=0&LeagueID=&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=&PaceAdjust=N&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2019-20&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=&TwoWay=&VsConference=&VsDivision=)

## Parameters
| API Parameter Name                                                                                                              | Python Parameter Variable             |                                                                    Pattern                                                                    | Required | Nullable |
|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------:|:--------:|:--------:|
| [_**LastNGames**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LastNGames)             | last_n_games                          |                                                                                                                                               |   `Y`    |          | 
| [_**MeasureType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#MeasureType)           | measure_type_detailed_defense         |                           `^(Base)\|(Advanced)\|(Misc)\|(Four Factors)\|(Scoring)\|(Opponent)\|(Usage)\|(Defense)$`                           |   `Y`    |          | 
| [_**Month**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Month)                       | month                                 |                                                                                                                                               |   `Y`    |          | 
| [_**OpponentTeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#OpponentTeamID)     | opponent_team_id                      |                                                                                                                                               |   `Y`    |          | 
| [_**PaceAdjust**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PaceAdjust)             | pace_adjust                           |                                                                 `^(Y)\|(N)$`                                                                  |   `Y`    |          | 
| [_**PerMode**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PerMode)                   | per_mode_detailed                     | `^(Totals)\|(PerGame)\|(MinutesPer)\|(Per48)\|(Per40)\|(Per36)\|(PerMinute)\|(PerPossession)\|(PerPlay)\|(Per100Possessions)\|(Per100Plays)$` |   `Y`    |          | 
| [_**Period**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Period)                     | period                                |                                                                                                                                               |   `Y`    |          | 
| [_**PlusMinus**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlusMinus)               | plus_minus                            |                                                                 `^(Y)\|(N)$`                                                                  |   `Y`    |          | 
| [_**Rank**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Rank)                         | rank                                  |                                                                 `^(Y)\|(N)$`                                                                  |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)                     | season                                |                                                                                                                                               |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType)             | season_type_all_star                  |                                          `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$`                                           |   `Y`    |          | 
| [_**VsDivision**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsDivision)             | vs_division_nullable                  |                        `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$`                         |   `Y`    |   `Y`    | 
| [_**VsConference**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsConference)         | vs_conference_nullable                |                                                             `^((East)\|(West))?$`                                                             |   `Y`    |   `Y`    | 
| [_**TwoWay**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TwoWay)                     | two_way_nullable                      |                                                                                                                                               |          |   `Y`    | 
| [_**TeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TeamID)                     | team_id_nullable                      |                                                                                                                                               |          |   `Y`    | 
| [_**StarterBench**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#StarterBench)         | starter_bench_nullable                |                                                           `((Starters)\|(Bench))?`                                                            |          |   `Y`    | 
| [_**ShotClockRange**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#ShotClockRange)     | shot_clock_range_nullable             |                 `((24-22)\|(22-18 Very Early)\|(18-15 Early)\|(15-7 Average)\|(7-4 Late)\|(4-0 Very Late)\|(ShotClock Off))?`                 |          |   `Y`    | 
| [_**SeasonSegment**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonSegment)       | season_segment_nullable               |                                                    `^((Post All-Star)\|(Pre All-Star))?$`                                                     |   `Y`    |   `Y`    | 
| [_**PlayerPosition**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerPosition)     | player_position_abbreviation_nullable |                                                `((F)\|(C)\|(G)\|(C-F)\|(F-C)\|(F-G)\|(G-F))?`                                                 |          |   `Y`    | 
| [_**PlayerExperience**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerExperience) | player_experience_nullable            |                                                     `((Rookie)\|(Sophomore)\|(Veteran))?`                                                     |          |   `Y`    | 
| [_**PORound**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PORound)                   | po_round_nullable                     |                                                                                                                                               |          |   `Y`    | 
| [_**Outcome**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Outcome)                   | outcome_nullable                      |                                                                `^((W)\|(L))?$`                                                                |   `Y`    |   `Y`    | 
| [_**Location**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Location)                 | location_nullable                     |                                                             `^((Home)\|(Road))?$`                                                             |   `Y`    |   `Y`    | 
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)                 | league_id_nullable                    |                                                                                                                                               |          |   `Y`    | 
| [_**GameSegment**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameSegment)           | game_segment_nullable                 |                                                `^((First Half)\|(Overtime)\|(Second Half))?$`                                                 |   `Y`    |   `Y`    | 
| [_**GameScope**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameScope)               | game_scope_simple_nullable            |                                                          `((Yesterday)\|(Last 10))?`                                                          |          |   `Y`    | 
| [_**Division**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Division)                 | division_simple_nullable              |                                 `((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest))?`                                  |          |   `Y`    | 
| [_**DateTo**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateTo)                     | date_to_nullable                      |                                                                                                                                               |   `Y`    |   `Y`    | 
| [_**DateFrom**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateFrom)                 | date_from_nullable                    |                                                                                                                                               |   `Y`    |   `Y`    | 
| [_**Conference**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Conference)             | conference_nullable                   |                                                              `((East)\|(West))?`                                                              |          |   `Y`    | 

## Data Sets
#### LeagueDashTeamStats `league_dash_team_stats`
```text
['TEAM_ID', 'TEAM_NAME', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'GP_RANK', 'W_RANK', 'L_RANK', 'W_PCT_RANK', 'MIN_RANK', 'FGM_RANK', 'FGA_RANK', 'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 'FTM_RANK', 'FTA_RANK', 'FT_PCT_RANK', 'OREB_RANK', 'DREB_RANK', 'REB_RANK', 'AST_RANK', 'TOV_RANK', 'STL_RANK', 'BLK_RANK', 'BLKA_RANK', 'PF_RANK', 'PFD_RANK', 'PTS_RANK', 'PLUS_MINUS_RANK', 'CFID', 'CFPARAMS']
```


## JSON
```json
{
    "data_sets": {
        "LeagueDashTeamStats": [
            "TEAM_ID",
            "TEAM_NAME",
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
            "CFID",
            "CFPARAMS"
        ]
    },
    "endpoint": "LeagueDashTeamStats",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [
        "Conference",
        "DateFrom",
        "DateTo",
        "Division",
        "GameScope",
        "GameSegment",
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
        "TwoWay",
        "VsConference",
        "VsDivision"
    ],
    "parameter_patterns": {
        "Conference": "((East)|(West))?",
        "DateFrom": null,
        "DateTo": null,
        "Division": "((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest))?",
        "GameScope": "((Yesterday)|(Last 10))?",
        "GameSegment": "^((First Half)|(Overtime)|(Second Half))?$",
        "LastNGames": null,
        "LeagueID": null,
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
        "Season": null,
        "SeasonSegment": "^((Post All-Star)|(Pre All-Star))?$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$",
        "ShotClockRange": "((24-22)|(22-18 Very Early)|(18-15 Early)|(15-7 Average)|(7-4 Late)|(4-0 Very Late)|(ShotClock Off))?",
        "StarterBench": "((Starters)|(Bench))?",
        "TeamID": null,
        "TwoWay": null,
        "VsConference": "^((East)|(West))?$",
        "VsDivision": "^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$"
    },
    "parameters": [
        "Conference",
        "DateFrom",
        "DateTo",
        "Division",
        "GameScope",
        "GameSegment",
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
        "TwoWay",
        "VsConference",
        "VsDivision"
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
        "PlusMinus",
        "Rank",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "VsConference",
        "VsDivision"
    ],
    "status": "success"
}
```

Last validated 2020-08-16