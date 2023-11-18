# TeamPlayerOnOffDetails
##### [nba_api/stats/endpoints/teamplayeronoffdetails.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/teamplayeronoffdetails.py)

##### Endpoint URL
>[https://stats.nba.com/stats/teamplayeronoffdetails](https://stats.nba.com/stats/teamplayeronoffdetails)

##### Valid URL
>[https://stats.nba.com/stats/teamplayeronoffdetails?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PaceAdjust=N&PerMode=Totals&Period=0&PlusMinus=N&Rank=N&Season=2019-20&SeasonSegment=&SeasonType=Regular+Season&TeamID=1610612739&VsConference=&VsDivision=](https://stats.nba.com/stats/teamplayeronoffdetails?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PaceAdjust=N&PerMode=Totals&Period=0&PlusMinus=N&Rank=N&Season=2019-20&SeasonSegment=&SeasonType=Regular+Season&TeamID=1610612739&VsConference=&VsDivision=)

## Parameters
| API Parameter Name                                                                                                          | Python Parameter Variable     |                                                                    Pattern                                                                    | Required | Nullable |
|-----------------------------------------------------------------------------------------------------------------------------|-------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------:|:--------:|:--------:|
| [_**LastNGames**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LastNGames)         | last_n_games                  |                                                                                                                                               |   `Y`    |          | 
| [_**MeasureType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#MeasureType)       | measure_type_detailed_defense |                           `^(Base)\|(Advanced)\|(Misc)\|(Four Factors)\|(Scoring)\|(Opponent)\|(Usage)\|(Defense)$`                           |   `Y`    |          | 
| [_**Month**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Month)                   | month                         |                                                                                                                                               |   `Y`    |          | 
| [_**OpponentTeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#OpponentTeamID) | opponent_team_id              |                                                                                                                                               |   `Y`    |          | 
| [_**PaceAdjust**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PaceAdjust)         | pace_adjust                   |                                                                 `^(Y)\|(N)$`                                                                  |   `Y`    |          | 
| [_**PerMode**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PerMode)               | per_mode_detailed             | `^(Totals)\|(PerGame)\|(MinutesPer)\|(Per48)\|(Per40)\|(Per36)\|(PerMinute)\|(PerPossession)\|(PerPlay)\|(Per100Possessions)\|(Per100Plays)$` |   `Y`    |          | 
| [_**Period**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Period)                 | period                        |                                                                                                                                               |   `Y`    |          | 
| [_**PlusMinus**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlusMinus)           | plus_minus                    |                                                                 `^(Y)\|(N)$`                                                                  |   `Y`    |          | 
| [_**Rank**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Rank)                     | rank                          |                                                                 `^(Y)\|(N)$`                                                                  |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)                 | season                        |                                                                                                                                               |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType)         | season_type_all_star          |                                          `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$`                                           |   `Y`    |          | 
| [_**TeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TeamID)                 | team_id                       |                                                                                                                                               |   `Y`    |          | 
| [_**VsDivision**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsDivision)         | vs_division_nullable          |                        `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$`                         |   `Y`    |   `Y`    | 
| [_**VsConference**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsConference)     | vs_conference_nullable        |                                                             `^((East)\|(West))?$`                                                             |   `Y`    |   `Y`    | 
| [_**SeasonSegment**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonSegment)   | season_segment_nullable       |                                                    `^((Post All-Star)\|(Pre All-Star))?$`                                                     |   `Y`    |   `Y`    | 
| [_**Outcome**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Outcome)               | outcome_nullable              |                                                                `^((W)\|(L))?$`                                                                |   `Y`    |   `Y`    | 
| [_**Location**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Location)             | location_nullable             |                                                             `^((Home)\|(Road))?$`                                                             |   `Y`    |   `Y`    | 
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)             | league_id_nullable            |                                                                                                                                               |          |   `Y`    | 
| [_**GameSegment**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameSegment)       | game_segment_nullable         |                                                `^((First Half)\|(Overtime)\|(Second Half))?$`                                                 |   `Y`    |   `Y`    | 
| [_**DateTo**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateTo)                 | date_to_nullable              |                                                                                                                                               |   `Y`    |   `Y`    | 
| [_**DateFrom**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateFrom)             | date_from_nullable            |                                                                                                                                               |   `Y`    |   `Y`    | 

## Data Sets
#### OverallTeamPlayerOnOffDetails `overall_team_player_on_off_details`
```text
['GROUP_SET', 'GROUP_VALUE', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'GP_RANK', 'W_RANK', 'L_RANK', 'W_PCT_RANK', 'MIN_RANK', 'FGM_RANK', 'FGA_RANK', 'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 'FTM_RANK', 'FTA_RANK', 'FT_PCT_RANK', 'OREB_RANK', 'DREB_RANK', 'REB_RANK', 'AST_RANK', 'TOV_RANK', 'STL_RANK', 'BLK_RANK', 'BLKA_RANK', 'PF_RANK', 'PFD_RANK', 'PTS_RANK', 'PLUS_MINUS_RANK']
```

#### PlayersOffCourtTeamPlayerOnOffDetails `players_off_court_team_player_on_off_details`
```text
['GROUP_SET', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'VS_PLAYER_ID', 'VS_PLAYER_NAME', 'COURT_STATUS', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'GP_RANK', 'W_RANK', 'L_RANK', 'W_PCT_RANK', 'MIN_RANK', 'FGM_RANK', 'FGA_RANK', 'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 'FTM_RANK', 'FTA_RANK', 'FT_PCT_RANK', 'OREB_RANK', 'DREB_RANK', 'REB_RANK', 'AST_RANK', 'TOV_RANK', 'STL_RANK', 'BLK_RANK', 'BLKA_RANK', 'PF_RANK', 'PFD_RANK', 'PTS_RANK', 'PLUS_MINUS_RANK']
```

#### PlayersOnCourtTeamPlayerOnOffDetails `players_on_court_team_player_on_off_details`
```text
['GROUP_SET', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'VS_PLAYER_ID', 'VS_PLAYER_NAME', 'COURT_STATUS', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'GP_RANK', 'W_RANK', 'L_RANK', 'W_PCT_RANK', 'MIN_RANK', 'FGM_RANK', 'FGA_RANK', 'FG_PCT_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 'FTM_RANK', 'FTA_RANK', 'FT_PCT_RANK', 'OREB_RANK', 'DREB_RANK', 'REB_RANK', 'AST_RANK', 'TOV_RANK', 'STL_RANK', 'BLK_RANK', 'BLKA_RANK', 'PF_RANK', 'PFD_RANK', 'PTS_RANK', 'PLUS_MINUS_RANK']
```


## JSON
```json
{
    "data_sets": {
        "OverallTeamPlayerOnOffDetails": [
            "GROUP_SET",
            "GROUP_VALUE",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
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
            "PLUS_MINUS_RANK"
        ],
        "PlayersOffCourtTeamPlayerOnOffDetails": [
            "GROUP_SET",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "VS_PLAYER_ID",
            "VS_PLAYER_NAME",
            "COURT_STATUS",
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
            "PLUS_MINUS_RANK"
        ],
        "PlayersOnCourtTeamPlayerOnOffDetails": [
            "GROUP_SET",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "VS_PLAYER_ID",
            "VS_PLAYER_NAME",
            "COURT_STATUS",
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
            "PLUS_MINUS_RANK"
        ]
    },
    "endpoint": "TeamPlayerOnOffDetails",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [
        "DateFrom",
        "DateTo",
        "GameSegment",
        "LeagueID",
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
        "LeagueID": null,
        "Location": "^((Home)|(Road))?$",
        "MeasureType": "^(Base)|(Advanced)|(Misc)|(Four Factors)|(Scoring)|(Opponent)|(Usage)|(Defense)$",
        "Month": null,
        "OpponentTeamID": null,
        "Outcome": "^((W)|(L))?$",
        "PaceAdjust": "^(Y)|(N)$",
        "PerMode": "^(Totals)|(PerGame)|(MinutesPer)|(Per48)|(Per40)|(Per36)|(PerMinute)|(PerPossession)|(PerPlay)|(Per100Possessions)|(Per100Plays)$",
        "Period": null,
        "PlusMinus": "^(Y)|(N)$",
        "Rank": "^(Y)|(N)$",
        "Season": null,
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
        "TeamID",
        "VsConference",
        "VsDivision"
    ],
    "status": "success"
}
```

Last validated 2020-08-16