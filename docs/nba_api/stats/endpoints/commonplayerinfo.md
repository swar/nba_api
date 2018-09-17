# CommonPlayerInfo

##### Endpoint URL
>[https://stats.nba.com/stats/commonplayerinfo](https://stats.nba.com/stats/commonplayerinfo)

##### Valid URL
>[https://stats.nba.com/stats/commonplayerinfo?LeagueID=&PlayerID=2544](https://stats.nba.com/stats/commonplayerinfo?LeagueID=&PlayerID=2544)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**PlayerID**_ |  | `Y` |  | 
_**LeagueID**_ | `(00)\|(20)\|(10)` |  | `Y` | 

## Data Sets
#### AvailableSeasons `available_seasons`
```text
['SEASON_ID']
```

#### CommonPlayerInfo `common_player_info`
```text
['PERSON_ID', 'FIRST_NAME', 'LAST_NAME', 'DISPLAY_FIRST_LAST', 'DISPLAY_LAST_COMMA_FIRST', 'DISPLAY_FI_LAST', 'BIRTHDATE', 'SCHOOL', 'COUNTRY', 'LAST_AFFILIATION', 'HEIGHT', 'WEIGHT', 'SEASON_EXP', 'JERSEY', 'POSITION', 'ROSTERSTATUS', 'TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'TEAM_CODE', 'TEAM_CITY', 'PLAYERCODE', 'FROM_YEAR', 'TO_YEAR', 'DLEAGUE_FLAG', 'GAMES_PLAYED_FLAG', 'DRAFT_YEAR', 'DRAFT_ROUND', 'DRAFT_NUMBER']
```

#### PlayerHeadlineStats `player_headline_stats`
```text
['PLAYER_ID', 'PLAYER_NAME', 'TimeFrame', 'PTS', 'AST', 'REB', 'PIE']
```


## JSON
```json
{
    "data_sets": {
        "AvailableSeasons": [
            "SEASON_ID"
        ],
        "CommonPlayerInfo": [
            "PERSON_ID",
            "FIRST_NAME",
            "LAST_NAME",
            "DISPLAY_FIRST_LAST",
            "DISPLAY_LAST_COMMA_FIRST",
            "DISPLAY_FI_LAST",
            "BIRTHDATE",
            "SCHOOL",
            "COUNTRY",
            "LAST_AFFILIATION",
            "HEIGHT",
            "WEIGHT",
            "SEASON_EXP",
            "JERSEY",
            "POSITION",
            "ROSTERSTATUS",
            "TEAM_ID",
            "TEAM_NAME",
            "TEAM_ABBREVIATION",
            "TEAM_CODE",
            "TEAM_CITY",
            "PLAYERCODE",
            "FROM_YEAR",
            "TO_YEAR",
            "DLEAGUE_FLAG",
            "GAMES_PLAYED_FLAG",
            "DRAFT_YEAR",
            "DRAFT_ROUND",
            "DRAFT_NUMBER"
        ],
        "PlayerHeadlineStats": [
            "PLAYER_ID",
            "PLAYER_NAME",
            "TimeFrame",
            "PTS",
            "AST",
            "REB",
            "PIE"
        ]
    },
    "endpoint": "CommonPlayerInfo",
    "nullable_parameters": [
        "LeagueID"
    ],
    "parameter_patterns": {
        "LeagueID": "(00)|(20)|(10)",
        "PlayerID": null
    },
    "parameters": [
        "LeagueID",
        "PlayerID"
    ],
    "required_parameters": [
        "PlayerID"
    ],
    "status": "success"
}
```

Last validated 2018-09-16