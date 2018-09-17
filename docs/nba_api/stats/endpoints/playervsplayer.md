# PlayerVsPlayer

##### Endpoint URL
>[https://stats.nba.com/stats/playervsplayer](https://stats.nba.com/stats/playervsplayer)

##### Valid URL
>[https://stats.nba.com/stats/playervsplayer?DateFrom=&DateTo=&GameSegment=&LastNGames=10&LeagueID=&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PaceAdjust=N&PerMode=Totals&Period=1&PlayerID=2544&PlusMinus=N&Rank=N&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&VsConference=&VsDivision=&VsPlayerID=2544](https://stats.nba.com/stats/playervsplayer?DateFrom=&DateTo=&GameSegment=&LastNGames=10&LeagueID=&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PaceAdjust=N&PerMode=Totals&Period=1&PlayerID=2544&PlusMinus=N&Rank=N&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&VsConference=&VsDivision=&VsPlayerID=2544)

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
_**PlayerID**_ |  | `Y` |  | 
_**PlusMinus**_ | `^(Y)\|(N)$` | `Y` |  | 
_**Rank**_ | `^(Y)\|(N)$` | `Y` |  | 
_**Season**_ | `^\d{4}-\d{2}$` | `Y` |  | 
_**SeasonType**_ | `^(Regular Season)\|(Pre Season)\|(Playoffs)$` | `Y` |  | 
_**VsPlayerID**_ |  | `Y` |  | 
_**VsDivision**_ | `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$` | `Y` | `Y` | 
_**VsConference**_ | `^((East)\|(West))?$` | `Y` | `Y` | 
_**SeasonSegment**_ | `^((Post All-Star)\|(Pre All-Star))?$` | `Y` | `Y` | 
_**Outcome**_ | `^((W)\|(L))?$` | `Y` | `Y` | 
_**Location**_ | `^((Home)\|(Road))?$` | `Y` | `Y` | 
_**LeagueID**_ | `(00)\|(20)\|(10)` |  | `Y` | 
_**GameSegment**_ | `^((First Half)\|(Overtime)\|(Second Half))?$` | `Y` | `Y` | 
_**DateTo**_ |  | `Y` | `Y` | 
_**DateFrom**_ |  | `Y` | `Y` | 

## Data Sets
#### OnOffCourt `on_off_court`
```text
['GROUP_SET', 'PLAYER_ID', 'PLAYER_NAME', 'VS_PLAYER_ID', 'VS_PLAYER_NAME', 'COURT_STATUS', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'CFID', 'CFPARAMS']
```

#### Overall `overall`
```text
['GROUP_SET', 'GROUP_VALUE', 'PLAYER_ID', 'PLAYER_NAME', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'CFID', 'CFPARAMS']
```

#### PlayerInfo `player_info`
```text
['PERSON_ID', 'FIRST_NAME', 'LAST_NAME', 'DISPLAY_FIRST_LAST', 'DISPLAY_LAST_COMMA_FIRST', 'DISPLAY_FI_LAST', 'BIRTHDATE', 'SCHOOL', 'COUNTRY', 'LAST_AFFILIATION']
```

#### ShotAreaOffCourt `shot_area_off_court`
```text
['GROUP_SET', 'PLAYER_ID', 'PLAYER_NAME', 'VS_PLAYER_ID', 'VS_PLAYER_NAME', 'COURT_STATUS', 'GROUP_VALUE', 'FGM', 'FGA', 'FG_PCT', 'CFID', 'CFPARAMS']
```

#### ShotAreaOnCourt `shot_area_on_court`
```text
['GROUP_SET', 'PLAYER_ID', 'PLAYER_NAME', 'VS_PLAYER_ID', 'VS_PLAYER_NAME', 'COURT_STATUS', 'GROUP_VALUE', 'FGM', 'FGA', 'FG_PCT', 'CFID', 'CFPARAMS']
```

#### ShotAreaOverall `shot_area_overall`
```text
['GROUP_SET', 'GROUP_VALUE', 'PLAYER_ID', 'PLAYER_NAME', 'FGM', 'FGA', 'FG_PCT', 'CFID', 'CFPARAMS']
```

#### ShotDistanceOffCourt `shot_distance_off_court`
```text
['GROUP_SET', 'PLAYER_ID', 'PLAYER_NAME', 'VS_PLAYER_ID', 'VS_PLAYER_NAME', 'COURT_STATUS', 'GROUP_VALUE', 'FGM', 'FGA', 'FG_PCT', 'CFID', 'CFPARAMS']
```

#### ShotDistanceOnCourt `shot_distance_on_court`
```text
['GROUP_SET', 'PLAYER_ID', 'PLAYER_NAME', 'VS_PLAYER_ID', 'VS_PLAYER_NAME', 'COURT_STATUS', 'GROUP_VALUE', 'FGM', 'FGA', 'FG_PCT', 'CFID', 'CFPARAMS']
```

#### ShotDistanceOverall `shot_distance_overall`
```text
['GROUP_SET', 'GROUP_VALUE', 'PLAYER_ID', 'PLAYER_NAME', 'FGM', 'FGA', 'FG_PCT', 'CFID', 'CFPARAMS']
```

#### VsPlayerInfo `vs_player_info`
```text
['PERSON_ID', 'FIRST_NAME', 'LAST_NAME', 'DISPLAY_FIRST_LAST', 'DISPLAY_LAST_COMMA_FIRST', 'DISPLAY_FI_LAST', 'BIRTHDATE', 'SCHOOL', 'COUNTRY', 'LAST_AFFILIATION']
```


## JSON
```json
{
    "data_sets": {
        "OnOffCourt": [
            "GROUP_SET",
            "PLAYER_ID",
            "PLAYER_NAME",
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
            "CFID",
            "CFPARAMS"
        ],
        "Overall": [
            "GROUP_SET",
            "GROUP_VALUE",
            "PLAYER_ID",
            "PLAYER_NAME",
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
            "CFID",
            "CFPARAMS"
        ],
        "PlayerInfo": [
            "PERSON_ID",
            "FIRST_NAME",
            "LAST_NAME",
            "DISPLAY_FIRST_LAST",
            "DISPLAY_LAST_COMMA_FIRST",
            "DISPLAY_FI_LAST",
            "BIRTHDATE",
            "SCHOOL",
            "COUNTRY",
            "LAST_AFFILIATION"
        ],
        "ShotAreaOffCourt": [
            "GROUP_SET",
            "PLAYER_ID",
            "PLAYER_NAME",
            "VS_PLAYER_ID",
            "VS_PLAYER_NAME",
            "COURT_STATUS",
            "GROUP_VALUE",
            "FGM",
            "FGA",
            "FG_PCT",
            "CFID",
            "CFPARAMS"
        ],
        "ShotAreaOnCourt": [
            "GROUP_SET",
            "PLAYER_ID",
            "PLAYER_NAME",
            "VS_PLAYER_ID",
            "VS_PLAYER_NAME",
            "COURT_STATUS",
            "GROUP_VALUE",
            "FGM",
            "FGA",
            "FG_PCT",
            "CFID",
            "CFPARAMS"
        ],
        "ShotAreaOverall": [
            "GROUP_SET",
            "GROUP_VALUE",
            "PLAYER_ID",
            "PLAYER_NAME",
            "FGM",
            "FGA",
            "FG_PCT",
            "CFID",
            "CFPARAMS"
        ],
        "ShotDistanceOffCourt": [
            "GROUP_SET",
            "PLAYER_ID",
            "PLAYER_NAME",
            "VS_PLAYER_ID",
            "VS_PLAYER_NAME",
            "COURT_STATUS",
            "GROUP_VALUE",
            "FGM",
            "FGA",
            "FG_PCT",
            "CFID",
            "CFPARAMS"
        ],
        "ShotDistanceOnCourt": [
            "GROUP_SET",
            "PLAYER_ID",
            "PLAYER_NAME",
            "VS_PLAYER_ID",
            "VS_PLAYER_NAME",
            "COURT_STATUS",
            "GROUP_VALUE",
            "FGM",
            "FGA",
            "FG_PCT",
            "CFID",
            "CFPARAMS"
        ],
        "ShotDistanceOverall": [
            "GROUP_SET",
            "GROUP_VALUE",
            "PLAYER_ID",
            "PLAYER_NAME",
            "FGM",
            "FGA",
            "FG_PCT",
            "CFID",
            "CFPARAMS"
        ],
        "VsPlayerInfo": [
            "PERSON_ID",
            "FIRST_NAME",
            "LAST_NAME",
            "DISPLAY_FIRST_LAST",
            "DISPLAY_LAST_COMMA_FIRST",
            "DISPLAY_FI_LAST",
            "BIRTHDATE",
            "SCHOOL",
            "COUNTRY",
            "LAST_AFFILIATION"
        ]
    },
    "endpoint": "PlayerVsPlayer",
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
        "LeagueID": "(00)|(20)|(10)",
        "Location": "^((Home)|(Road))?$",
        "MeasureType": "^(Base)|(Advanced)|(Misc)|(Four Factors)|(Scoring)|(Opponent)|(Usage)|(Defense)$",
        "Month": null,
        "OpponentTeamID": null,
        "Outcome": "^((W)|(L))?$",
        "PaceAdjust": "^(Y)|(N)$",
        "PerMode": "^(Totals)|(PerGame)|(MinutesPer)|(Per48)|(Per40)|(Per36)|(PerMinute)|(PerPossession)|(PerPlay)|(Per100Possessions)|(Per100Plays)$",
        "Period": null,
        "PlayerID": null,
        "PlusMinus": "^(Y)|(N)$",
        "Rank": "^(Y)|(N)$",
        "Season": "^\\d{4}-\\d{2}$",
        "SeasonSegment": "^((Post All-Star)|(Pre All-Star))?$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)$",
        "VsConference": "^((East)|(West))?$",
        "VsDivision": "^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$",
        "VsPlayerID": null
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
        "PlayerID",
        "PlusMinus",
        "Rank",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "VsConference",
        "VsDivision",
        "VsPlayerID"
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
        "PlayerID",
        "PlusMinus",
        "Rank",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "VsConference",
        "VsDivision",
        "VsPlayerID"
    ],
    "status": "success"
}
```

Last validated 2018-09-16