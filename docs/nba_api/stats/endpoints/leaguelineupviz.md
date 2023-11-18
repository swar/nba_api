# LeagueLineupViz
##### [nba_api/stats/endpoints/leaguelineupviz.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/leaguelineupviz.py)

##### Endpoint URL
>[https://stats.nba.com/stats/leaguelineupviz](https://stats.nba.com/stats/leaguelineupviz)

##### Valid URL
>[https://stats.nba.com/stats/leaguelineupviz?Conference=&DateFrom=&DateTo=&Division=&GameSegment=&GroupQuantity=5&LastNGames=0&LeagueID=&Location=&MeasureType=Base&MinutesMin=10&Month=0&OpponentTeamID=0&Outcome=&PORound=&PaceAdjust=N&PerMode=Totals&Period=0&PlusMinus=N&Rank=N&Season=2019-20&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&TeamID=&VsConference=&VsDivision=](https://stats.nba.com/stats/leaguelineupviz?Conference=&DateFrom=&DateTo=&Division=&GameSegment=&GroupQuantity=5&LastNGames=0&LeagueID=&Location=&MeasureType=Base&MinutesMin=10&Month=0&OpponentTeamID=0&Outcome=&PORound=&PaceAdjust=N&PerMode=Totals&Period=0&PlusMinus=N&Rank=N&Season=2019-20&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&TeamID=&VsConference=&VsDivision=)

## Parameters
| API Parameter Name                                                                                                          | Python Parameter Variable     |                                                                    Pattern                                                                    | Required | Nullable |
|-----------------------------------------------------------------------------------------------------------------------------|-------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------:|:--------:|:--------:|
| [_**GroupQuantity**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GroupQuantity)   | group_quantity                |                                                                                                                                               |   `Y`    |          | 
| [_**LastNGames**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LastNGames)         | last_n_games                  |                                                                                                                                               |   `Y`    |          | 
| [_**MeasureType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#MeasureType)       | measure_type_detailed_defense |                           `^(Base)\|(Advanced)\|(Misc)\|(Four Factors)\|(Scoring)\|(Opponent)\|(Usage)\|(Defense)$`                           |   `Y`    |          | 
| [_**MinutesMin**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#MinutesMin)         | minutes_min                   |                                                                                                                                               |   `Y`    |          | 
| [_**Month**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Month)                   | month                         |                                                                                                                                               |   `Y`    |          | 
| [_**OpponentTeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#OpponentTeamID) | opponent_team_id              |                                                                                                                                               |   `Y`    |          | 
| [_**PaceAdjust**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PaceAdjust)         | pace_adjust                   |                                                                 `^(Y)\|(N)$`                                                                  |   `Y`    |          | 
| [_**PerMode**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PerMode)               | per_mode_detailed             | `^(Totals)\|(PerGame)\|(MinutesPer)\|(Per48)\|(Per40)\|(Per36)\|(PerMinute)\|(PerPossession)\|(PerPlay)\|(Per100Possessions)\|(Per100Plays)$` |   `Y`    |          | 
| [_**Period**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Period)                 | period                        |                                                                                                                                               |   `Y`    |          | 
| [_**PlusMinus**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlusMinus)           | plus_minus                    |                                                                 `^(Y)\|(N)$`                                                                  |   `Y`    |          | 
| [_**Rank**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Rank)                     | rank                          |                                                                 `^(Y)\|(N)$`                                                                  |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)                 | season                        |                                                                                                                                               |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType)         | season_type_all_star          |                                          `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$`                                           |   `Y`    |          | 
| [_**VsDivision**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsDivision)         | vs_division_nullable          |                        `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$`                         |   `Y`    |   `Y`    | 
| [_**VsConference**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsConference)     | vs_conference_nullable        |                                                             `^((East)\|(West))?$`                                                             |   `Y`    |   `Y`    | 
| [_**TeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TeamID)                 | team_id_nullable              |                                                                                                                                               |          |   `Y`    | 
| [_**ShotClockRange**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#ShotClockRange) | shot_clock_range_nullable     |                 `((24-22)\|(22-18 Very Early)\|(18-15 Early)\|(15-7 Average)\|(7-4 Late)\|(4-0 Very Late)\|(ShotClock Off))?`                 |          |   `Y`    | 
| [_**SeasonSegment**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonSegment)   | season_segment_nullable       |                                                    `^((Post All-Star)\|(Pre All-Star))?$`                                                     |   `Y`    |   `Y`    | 
| [_**PORound**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PORound)               | po_round_nullable             |                                                                                                                                               |          |   `Y`    | 
| [_**Outcome**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Outcome)               | outcome_nullable              |                                                                `^((W)\|(L))?$`                                                                |   `Y`    |   `Y`    | 
| [_**Location**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Location)             | location_nullable             |                                                             `^((Home)\|(Road))?$`                                                             |   `Y`    |   `Y`    | 
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)             | league_id_nullable            |                                                                                                                                               |          |   `Y`    | 
| [_**GameSegment**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameSegment)       | game_segment_nullable         |                                                `^((First Half)\|(Overtime)\|(Second Half))?$`                                                 |   `Y`    |   `Y`    | 
| [_**Division**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Division)             | division_simple_nullable      |                                 `((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest))?`                                  |          |   `Y`    | 
| [_**DateTo**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateTo)                 | date_to_nullable              |                                                                                                                                               |   `Y`    |   `Y`    | 
| [_**DateFrom**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateFrom)             | date_from_nullable            |                                                                                                                                               |   `Y`    |   `Y`    | 
| [_**Conference**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Conference)         | conference_nullable           |                                                              `((East)\|(West))?`                                                              |          |   `Y`    | 

## Data Sets
#### LeagueLineupViz `league_lineup_viz`
```text
['GROUP_ID', 'GROUP_NAME', 'TEAM_ID', 'TEAM_ABBREVIATION', 'MIN', 'OFF_RATING', 'DEF_RATING', 'NET_RATING', 'PACE', 'TS_PCT', 'FTA_RATE', 'TM_AST_PCT', 'PCT_FGA_2PT', 'PCT_FGA_3PT', 'PCT_PTS_2PT_MR', 'PCT_PTS_FB', 'PCT_PTS_FT', 'PCT_PTS_PAINT', 'PCT_AST_FGM', 'PCT_UAST_FGM', 'OPP_FG3_PCT', 'OPP_EFG_PCT', 'OPP_FTA_RATE', 'OPP_TOV_PCT']
```


## JSON
```json
{
    "data_sets": {
        "LeagueLineupViz": [
            "GROUP_ID",
            "GROUP_NAME",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "MIN",
            "OFF_RATING",
            "DEF_RATING",
            "NET_RATING",
            "PACE",
            "TS_PCT",
            "FTA_RATE",
            "TM_AST_PCT",
            "PCT_FGA_2PT",
            "PCT_FGA_3PT",
            "PCT_PTS_2PT_MR",
            "PCT_PTS_FB",
            "PCT_PTS_FT",
            "PCT_PTS_PAINT",
            "PCT_AST_FGM",
            "PCT_UAST_FGM",
            "OPP_FG3_PCT",
            "OPP_EFG_PCT",
            "OPP_FTA_RATE",
            "OPP_TOV_PCT"
        ]
    },
    "endpoint": "LeagueLineupViz",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [
        "Conference",
        "DateFrom",
        "DateTo",
        "Division",
        "GameSegment",
        "LeagueID",
        "Location",
        "Outcome",
        "PORound",
        "SeasonSegment",
        "ShotClockRange",
        "TeamID",
        "VsConference",
        "VsDivision"
    ],
    "parameter_patterns": {
        "Conference": "((East)|(West))?",
        "DateFrom": null,
        "DateTo": null,
        "Division": "((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest))?",
        "GameSegment": "^((First Half)|(Overtime)|(Second Half))?$",
        "GroupQuantity": null,
        "LastNGames": null,
        "LeagueID": null,
        "Location": "^((Home)|(Road))?$",
        "MeasureType": "^(Base)|(Advanced)|(Misc)|(Four Factors)|(Scoring)|(Opponent)|(Usage)|(Defense)$",
        "MinutesMin": null,
        "Month": null,
        "OpponentTeamID": null,
        "Outcome": "^((W)|(L))?$",
        "PORound": null,
        "PaceAdjust": "^(Y)|(N)$",
        "PerMode": "^(Totals)|(PerGame)|(MinutesPer)|(Per48)|(Per40)|(Per36)|(PerMinute)|(PerPossession)|(PerPlay)|(Per100Possessions)|(Per100Plays)$",
        "Period": null,
        "PlusMinus": "^(Y)|(N)$",
        "Rank": "^(Y)|(N)$",
        "Season": null,
        "SeasonSegment": "^((Post All-Star)|(Pre All-Star))?$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$",
        "ShotClockRange": "((24-22)|(22-18 Very Early)|(18-15 Early)|(15-7 Average)|(7-4 Late)|(4-0 Very Late)|(ShotClock Off))?",
        "TeamID": null,
        "VsConference": "^((East)|(West))?$",
        "VsDivision": "^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$"
    },
    "parameters": [
        "Conference",
        "DateFrom",
        "DateTo",
        "Division",
        "GameSegment",
        "GroupQuantity",
        "LastNGames",
        "LeagueID",
        "Location",
        "MeasureType",
        "MinutesMin",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "PORound",
        "PaceAdjust",
        "PerMode",
        "Period",
        "PlusMinus",
        "Rank",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "ShotClockRange",
        "TeamID",
        "VsConference",
        "VsDivision"
    ],
    "required_parameters": [
        "DateFrom",
        "DateTo",
        "GameSegment",
        "GroupQuantity",
        "LastNGames",
        "Location",
        "MeasureType",
        "MinutesMin",
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