# ScoreboardV2
##### [nba_api/stats/endpoints/scoreboardv2.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/scoreboardv2.py)

##### Endpoint URL
>[https://stats.nba.com/stats/scoreboardv2](https://stats.nba.com/stats/scoreboardv2)

##### Valid URL
>[https://stats.nba.com/stats/scoreboardv2?DayOffset=0&GameDate=2020-08-16&LeagueID=00](https://stats.nba.com/stats/scoreboardv2?DayOffset=0&GameDate=2020-08-16&LeagueID=00)

## Parameters
| API Parameter Name                                                                                                | Python Parameter Variable |    Pattern    | Required | Nullable |
|-------------------------------------------------------------------------------------------------------------------|---------------------------|:-------------:|:--------:|:--------:|
| [_**DayOffset**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DayOffset) | day_offset                | `^-{0,1}\d+$` |   `Y`    |          | 
| [_**GameDate**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameDate)   | game_date                 |               |   `Y`    |          | 
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)   | league_id                 |   `^\d{2}$`   |   `Y`    |          | 

## Data Sets
#### Available `available`
```text
['GAME_ID', 'PT_AVAILABLE']
```

#### EastConfStandingsByDay `east_conf_standings_by_day`
```text
['TEAM_ID', 'LEAGUE_ID', 'SEASON_ID', 'STANDINGSDATE', 'CONFERENCE', 'TEAM', 'G', 'W', 'L', 'W_PCT', 'HOME_RECORD', 'ROAD_RECORD', 'RETURNTOPLAY']
```

#### GameHeader `game_header`
```text
['GAME_DATE_EST', 'GAME_SEQUENCE', 'GAME_ID', 'GAME_STATUS_ID', 'GAME_STATUS_TEXT', 'GAMECODE', 'HOME_TEAM_ID', 'VISITOR_TEAM_ID', 'SEASON', 'LIVE_PERIOD', 'LIVE_PC_TIME', 'NATL_TV_BROADCASTER_ABBREVIATION', 'HOME_TV_BROADCASTER_ABBREVIATION', 'AWAY_TV_BROADCASTER_ABBREVIATION', 'LIVE_PERIOD_TIME_BCAST', 'ARENA_NAME', 'WH_STATUS']
```

#### LastMeeting `last_meeting`
```text
['GAME_ID', 'LAST_GAME_ID', 'LAST_GAME_DATE_EST', 'LAST_GAME_HOME_TEAM_ID', 'LAST_GAME_HOME_TEAM_CITY', 'LAST_GAME_HOME_TEAM_NAME', 'LAST_GAME_HOME_TEAM_ABBREVIATION', 'LAST_GAME_HOME_TEAM_POINTS', 'LAST_GAME_VISITOR_TEAM_ID', 'LAST_GAME_VISITOR_TEAM_CITY', 'LAST_GAME_VISITOR_TEAM_NAME', 'LAST_GAME_VISITOR_TEAM_CITY1', 'LAST_GAME_VISITOR_TEAM_POINTS']
```

#### LineScore `line_score`
```text
['GAME_DATE_EST', 'GAME_SEQUENCE', 'GAME_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_CITY_NAME', 'TEAM_NAME', 'TEAM_WINS_LOSSES', 'PTS_QTR1', 'PTS_QTR2', 'PTS_QTR3', 'PTS_QTR4', 'PTS_OT1', 'PTS_OT2', 'PTS_OT3', 'PTS_OT4', 'PTS_OT5', 'PTS_OT6', 'PTS_OT7', 'PTS_OT8', 'PTS_OT9', 'PTS_OT10', 'PTS', 'FG_PCT', 'FT_PCT', 'FG3_PCT', 'AST', 'REB', 'TOV']
```

#### SeriesStandings `series_standings`
```text
['GAME_ID', 'HOME_TEAM_ID', 'VISITOR_TEAM_ID', 'GAME_DATE_EST', 'HOME_TEAM_WINS', 'HOME_TEAM_LOSSES', 'SERIES_LEADER']
```

#### TeamLeaders `team_leaders`
```text
['GAME_ID', 'TEAM_ID', 'TEAM_CITY', 'TEAM_NICKNAME', 'TEAM_ABBREVIATION', 'PTS_PLAYER_ID', 'PTS_PLAYER_NAME', 'PTS', 'REB_PLAYER_ID', 'REB_PLAYER_NAME', 'REB', 'AST_PLAYER_ID', 'AST_PLAYER_NAME', 'AST']
```

#### TicketLinks `ticket_links`
```text
['GAME_ID', 'LEAG_TIX']
```

#### WestConfStandingsByDay `west_conf_standings_by_day`
```text
['TEAM_ID', 'LEAGUE_ID', 'SEASON_ID', 'STANDINGSDATE', 'CONFERENCE', 'TEAM', 'G', 'W', 'L', 'W_PCT', 'HOME_RECORD', 'ROAD_RECORD']
```

#### WinProbability `win_probability`
```text
[]
```


## JSON
```json
{
    "data_sets": {
        "Available": [
            "GAME_ID",
            "PT_AVAILABLE"
        ],
        "EastConfStandingsByDay": [
            "TEAM_ID",
            "LEAGUE_ID",
            "SEASON_ID",
            "STANDINGSDATE",
            "CONFERENCE",
            "TEAM",
            "G",
            "W",
            "L",
            "W_PCT",
            "HOME_RECORD",
            "ROAD_RECORD",
            "RETURNTOPLAY"
        ],
        "GameHeader": [
            "GAME_DATE_EST",
            "GAME_SEQUENCE",
            "GAME_ID",
            "GAME_STATUS_ID",
            "GAME_STATUS_TEXT",
            "GAMECODE",
            "HOME_TEAM_ID",
            "VISITOR_TEAM_ID",
            "SEASON",
            "LIVE_PERIOD",
            "LIVE_PC_TIME",
            "NATL_TV_BROADCASTER_ABBREVIATION",
            "HOME_TV_BROADCASTER_ABBREVIATION",
            "AWAY_TV_BROADCASTER_ABBREVIATION",
            "LIVE_PERIOD_TIME_BCAST",
            "ARENA_NAME",
            "WH_STATUS"
        ],
        "LastMeeting": [
            "GAME_ID",
            "LAST_GAME_ID",
            "LAST_GAME_DATE_EST",
            "LAST_GAME_HOME_TEAM_ID",
            "LAST_GAME_HOME_TEAM_CITY",
            "LAST_GAME_HOME_TEAM_NAME",
            "LAST_GAME_HOME_TEAM_ABBREVIATION",
            "LAST_GAME_HOME_TEAM_POINTS",
            "LAST_GAME_VISITOR_TEAM_ID",
            "LAST_GAME_VISITOR_TEAM_CITY",
            "LAST_GAME_VISITOR_TEAM_NAME",
            "LAST_GAME_VISITOR_TEAM_CITY1",
            "LAST_GAME_VISITOR_TEAM_POINTS"
        ],
        "LineScore": [
            "GAME_DATE_EST",
            "GAME_SEQUENCE",
            "GAME_ID",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_CITY_NAME",
            "TEAM_NAME",
            "TEAM_WINS_LOSSES",
            "PTS_QTR1",
            "PTS_QTR2",
            "PTS_QTR3",
            "PTS_QTR4",
            "PTS_OT1",
            "PTS_OT2",
            "PTS_OT3",
            "PTS_OT4",
            "PTS_OT5",
            "PTS_OT6",
            "PTS_OT7",
            "PTS_OT8",
            "PTS_OT9",
            "PTS_OT10",
            "PTS",
            "FG_PCT",
            "FT_PCT",
            "FG3_PCT",
            "AST",
            "REB",
            "TOV"
        ],
        "SeriesStandings": [
            "GAME_ID",
            "HOME_TEAM_ID",
            "VISITOR_TEAM_ID",
            "GAME_DATE_EST",
            "HOME_TEAM_WINS",
            "HOME_TEAM_LOSSES",
            "SERIES_LEADER"
        ],
        "TeamLeaders": [
            "GAME_ID",
            "TEAM_ID",
            "TEAM_CITY",
            "TEAM_NICKNAME",
            "TEAM_ABBREVIATION",
            "PTS_PLAYER_ID",
            "PTS_PLAYER_NAME",
            "PTS",
            "REB_PLAYER_ID",
            "REB_PLAYER_NAME",
            "REB",
            "AST_PLAYER_ID",
            "AST_PLAYER_NAME",
            "AST"
        ],
        "TicketLinks": [
            "GAME_ID",
            "LEAG_TIX"
        ],
        "WestConfStandingsByDay": [
            "TEAM_ID",
            "LEAGUE_ID",
            "SEASON_ID",
            "STANDINGSDATE",
            "CONFERENCE",
            "TEAM",
            "G",
            "W",
            "L",
            "W_PCT",
            "HOME_RECORD",
            "ROAD_RECORD"
        ],
        "WinProbability": []
    },
    "endpoint": "ScoreboardV2",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [],
    "parameter_patterns": {
        "DayOffset": "^-{0,1}\\d+$",
        "GameDate": null,
        "LeagueID": "^\\d{2}$"
    },
    "parameters": [
        "DayOffset",
        "GameDate",
        "LeagueID"
    ],
    "required_parameters": [
        "DayOffset",
        "GameDate",
        "LeagueID"
    ],
    "status": "success"
}
```

Last validated 2020-08-16