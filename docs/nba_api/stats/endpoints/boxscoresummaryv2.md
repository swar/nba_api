# BoxScoreSummaryV2
##### [nba_api/stats/endpoints/boxscoresummaryv2.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/boxscoresummaryv2.py)

##### Endpoint URL
>[https://stats.nba.com/stats/boxscoresummaryv2](https://stats.nba.com/stats/boxscoresummaryv2)

##### Valid URL
>[https://stats.nba.com/stats/boxscoresummaryv2?GameID=0021700807](https://stats.nba.com/stats/boxscoresummaryv2?GameID=0021700807)

## Parameters
| API Parameter Name                                                                                          | Python Parameter Variable |  Pattern   | Required | Nullable |
|-------------------------------------------------------------------------------------------------------------|---------------------------|:----------:|:--------:|:--------:|
| [_**GameID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameID) | game_id                   | `^\d{10}$` |   `Y`    |          | 

## Data Sets
#### AvailableVideo `available_video`
```text
['GAME_ID', 'VIDEO_AVAILABLE_FLAG', 'PT_AVAILABLE', 'PT_XYZ_AVAILABLE', 'WH_STATUS', 'HUSTLE_STATUS', 'HISTORICAL_STATUS']
```

#### GameInfo `game_info`
```text
['GAME_DATE', 'ATTENDANCE', 'GAME_TIME']
```

#### GameSummary `game_summary`
```text
['GAME_DATE_EST', 'GAME_SEQUENCE', 'GAME_ID', 'GAME_STATUS_ID', 'GAME_STATUS_TEXT', 'GAMECODE', 'HOME_TEAM_ID', 'VISITOR_TEAM_ID', 'SEASON', 'LIVE_PERIOD', 'LIVE_PC_TIME', 'NATL_TV_BROADCASTER_ABBREVIATION', 'LIVE_PERIOD_TIME_BCAST', 'WH_STATUS']
```

#### InactivePlayers `inactive_players`
```text
['PLAYER_ID', 'FIRST_NAME', 'LAST_NAME', 'JERSEY_NUM', 'TEAM_ID', 'TEAM_CITY', 'TEAM_NAME', 'TEAM_ABBREVIATION']
```

#### LastMeeting `last_meeting`
```text
['GAME_ID', 'LAST_GAME_ID', 'LAST_GAME_DATE_EST', 'LAST_GAME_HOME_TEAM_ID', 'LAST_GAME_HOME_TEAM_CITY', 'LAST_GAME_HOME_TEAM_NAME', 'LAST_GAME_HOME_TEAM_ABBREVIATION', 'LAST_GAME_HOME_TEAM_POINTS', 'LAST_GAME_VISITOR_TEAM_ID', 'LAST_GAME_VISITOR_TEAM_CITY', 'LAST_GAME_VISITOR_TEAM_NAME', 'LAST_GAME_VISITOR_TEAM_CITY1', 'LAST_GAME_VISITOR_TEAM_POINTS']
```

#### LineScore `line_score`
```text
['GAME_DATE_EST', 'GAME_SEQUENCE', 'GAME_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_CITY_NAME', 'TEAM_NICKNAME', 'TEAM_WINS_LOSSES', 'PTS_QTR1', 'PTS_QTR2', 'PTS_QTR3', 'PTS_QTR4', 'PTS_OT1', 'PTS_OT2', 'PTS_OT3', 'PTS_OT4', 'PTS_OT5', 'PTS_OT6', 'PTS_OT7', 'PTS_OT8', 'PTS_OT9', 'PTS_OT10', 'PTS']
```

#### Officials `officials`
```text
['OFFICIAL_ID', 'FIRST_NAME', 'LAST_NAME', 'JERSEY_NUM']
```

#### OtherStats `other_stats`
```text
['LEAGUE_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_CITY', 'PTS_PAINT', 'PTS_2ND_CHANCE', 'PTS_FB', 'LARGEST_LEAD', 'LEAD_CHANGES', 'TIMES_TIED', 'TEAM_TURNOVERS', 'TOTAL_TURNOVERS', 'TEAM_REBOUNDS', 'PTS_OFF_TO']
```

#### SeasonSeries `season_series`
```text
['GAME_ID', 'HOME_TEAM_ID', 'VISITOR_TEAM_ID', 'GAME_DATE_EST', 'HOME_TEAM_WINS', 'HOME_TEAM_LOSSES', 'SERIES_LEADER']
```


## JSON
```json
{
    "data_sets": {
        "AvailableVideo": [
            "GAME_ID",
            "VIDEO_AVAILABLE_FLAG",
            "PT_AVAILABLE",
            "PT_XYZ_AVAILABLE",
            "WH_STATUS",
            "HUSTLE_STATUS",
            "HISTORICAL_STATUS"
        ],
        "GameInfo": [
            "GAME_DATE",
            "ATTENDANCE",
            "GAME_TIME"
        ],
        "GameSummary": [
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
            "LIVE_PERIOD_TIME_BCAST",
            "WH_STATUS"
        ],
        "InactivePlayers": [
            "PLAYER_ID",
            "FIRST_NAME",
            "LAST_NAME",
            "JERSEY_NUM",
            "TEAM_ID",
            "TEAM_CITY",
            "TEAM_NAME",
            "TEAM_ABBREVIATION"
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
            "TEAM_NICKNAME",
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
            "PTS"
        ],
        "Officials": [
            "OFFICIAL_ID",
            "FIRST_NAME",
            "LAST_NAME",
            "JERSEY_NUM"
        ],
        "OtherStats": [
            "LEAGUE_ID",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_CITY",
            "PTS_PAINT",
            "PTS_2ND_CHANCE",
            "PTS_FB",
            "LARGEST_LEAD",
            "LEAD_CHANGES",
            "TIMES_TIED",
            "TEAM_TURNOVERS",
            "TOTAL_TURNOVERS",
            "TEAM_REBOUNDS",
            "PTS_OFF_TO"
        ],
        "SeasonSeries": [
            "GAME_ID",
            "HOME_TEAM_ID",
            "VISITOR_TEAM_ID",
            "GAME_DATE_EST",
            "HOME_TEAM_WINS",
            "HOME_TEAM_LOSSES",
            "SERIES_LEADER"
        ]
    },
    "endpoint": "BoxScoreSummaryV2",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [],
    "parameter_patterns": {
        "GameID": "^\\d{10}$"
    },
    "parameters": [
        "GameID"
    ],
    "required_parameters": [
        "GameID"
    ],
    "status": "success"
}
```

Last validated 2020-08-16