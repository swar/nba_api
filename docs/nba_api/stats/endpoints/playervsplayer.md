# PlayerVsPlayer
##### [nba_api/stats/endpoints/playervsplayer.py](https://github.com/swar/nba_api/blob/master/nba_api/stats/endpoints/playervsplayer.py)

##### Endpoint URL
>[https://stats.nba.com/stats/playervsplayer](https://stats.nba.com/stats/playervsplayer)

##### Valid URL
>[https://stats.nba.com/stats/playervsplayer?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PaceAdjust=N&PerMode=Totals&Period=0&PlayerID=2544&PlusMinus=N&Rank=N&Season=2018-19&SeasonSegment=&SeasonType=Regular+Season&VsConference=&VsDivision=&VsPlayerID=2544](https://stats.nba.com/stats/playervsplayer?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PaceAdjust=N&PerMode=Totals&Period=0&PlayerID=2544&PlusMinus=N&Rank=N&Season=2018-19&SeasonSegment=&SeasonType=Regular+Season&VsConference=&VsDivision=&VsPlayerID=2544)

## Parameters
API Parameter Name | Python Parameter Class | Python Parameter Variable | Pattern | Required | Nullable
------------ | ------------ | ------------ | :-----------: | :---: | :---:
_**LastNGames**_ | [LastNGames](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LastNGames) | last_n_games |  | `Y` |  | 
_**MeasureType**_ | [MeasureTypeDetailedDefense](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#MeasureType) | measure_type_detailed_defense | `^(Base)\|(Advanced)\|(Misc)\|(Four Factors)\|(Scoring)\|(Opponent)\|(Usage)\|(Defense)$` | `Y` |  | 
_**Month**_ | [Month](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Month) | month |  | `Y` |  | 
_**OpponentTeamID**_ | [OpponentTeamID](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#OpponentTeamID) | opponent_team_id |  | `Y` |  | 
_**PaceAdjust**_ | [PaceAdjust](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PaceAdjust) | pace_adjust | `^(Y)\|(N)$` | `Y` |  | 
_**PerMode**_ | [PerModeDetailed](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PerMode) | per_mode_detailed | `^(Totals)\|(PerGame)\|(MinutesPer)\|(Per48)\|(Per40)\|(Per36)\|(PerMinute)\|(PerPossession)\|(PerPlay)\|(Per100Possessions)\|(Per100Plays)$` | `Y` |  | 
_**Period**_ | [Period](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Period) | period |  | `Y` |  | 
_**PlayerID**_ | [PlayerID](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerID) | player_id |  | `Y` |  | 
_**PlusMinus**_ | [PlusMinus](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlusMinus) | plus_minus | `^(Y)\|(N)$` | `Y` |  | 
_**Rank**_ | [Rank](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Rank) | rank | `^(Y)\|(N)$` | `Y` |  | 
_**Season**_ | [Season](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season) | season | `^\d{4}-\d{2}$` | `Y` |  | 
_**SeasonType**_ | [SeasonTypePlayoffs](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType) | season_type_playoffs | `^(Regular Season)\|(Pre Season)\|(Playoffs)$` | `Y` |  | 
_**VsPlayerID**_ | [VsPlayerID](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsPlayerID) | vs_player_id |  | `Y` |  | 
_**VsDivision**_ | [VsDivisionNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsDivision) | vs_division_nullable | `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$` | `Y` | `Y` | 
_**VsConference**_ | [VsConferenceNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsConference) | vs_conference_nullable | `^((East)\|(West))?$` | `Y` | `Y` | 
_**SeasonSegment**_ | [SeasonSegmentNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonSegment) | season_segment_nullable | `^((Post All-Star)\|(Pre All-Star))?$` | `Y` | `Y` | 
_**Outcome**_ | [OutcomeNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Outcome) | outcome_nullable | `^((W)\|(L))?$` | `Y` | `Y` | 
_**Location**_ | [LocationNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Location) | location_nullable | `^((Home)\|(Road))?$` | `Y` | `Y` | 
_**LeagueID**_ | [LeagueIDNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id_nullable | `(00)\|(20)\|(10)` |  | `Y` | 
_**GameSegment**_ | [GameSegmentNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameSegment) | game_segment_nullable | `^((First Half)\|(Overtime)\|(Second Half))?$` | `Y` | `Y` | 
_**DateTo**_ | [DateToNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateTo) | date_to_nullable |  | `Y` | `Y` | 
_**DateFrom**_ | [DateFromNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateFrom) | date_from_nullable |  | `Y` | `Y` | 

## Data Sets
#### OnOffCourt `on_off_court`
```text
['GROUP_SET', 'PLAYER_ID', 'PLAYER_NAME', 'VS_PLAYER_ID', 'VS_PLAYER_NAME', 'COURT_STATUS', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'NBA_FANTASY_PTS', 'CFID', 'CFPARAMS']
```

#### Overall `overall`
```text
['GROUP_SET', 'GROUP_VALUE', 'PLAYER_ID', 'PLAYER_NAME', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'NBA_FANTASY_PTS', 'CFID', 'CFPARAMS']
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
            "NBA_FANTASY_PTS",
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
            "NBA_FANTASY_PTS",
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
    "last_validated_date": "2018-12-11",
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

Last validated 2018-12-11