# CommonPlayerInfo
##### [nba_api/stats/endpoints/commonplayerinfo.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/commonplayerinfo.py)

##### Endpoint URL
>[https://stats.nba.com/stats/commonplayerinfo](https://stats.nba.com/stats/commonplayerinfo)

##### Valid URL
>[https://stats.nba.com/stats/commonplayerinfo?LeagueID=&PlayerID=2544](https://stats.nba.com/stats/commonplayerinfo?LeagueID=&PlayerID=2544)

## Parameters
| API Parameter Name                                                                                              | Python Parameter Variable | Pattern | Required | Nullable |
|-----------------------------------------------------------------------------------------------------------------|---------------------------|:-------:|:--------:|:--------:|
| [_**PlayerID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerID) | player_id                 |         |   `Y`    |          | 
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id_nullable        |         |          |   `Y`    | 

## Data Sets
#### AvailableSeasons `available_seasons`
```text
['SEASON_ID']
```

#### CommonPlayerInfo `common_player_info`
```text
['PERSON_ID', 'FIRST_NAME', 'LAST_NAME', 'DISPLAY_FIRST_LAST', 'DISPLAY_LAST_COMMA_FIRST', 'DISPLAY_FI_LAST', 'PLAYER_SLUG', 'BIRTHDATE', 'SCHOOL', 'COUNTRY', 'LAST_AFFILIATION', 'HEIGHT', 'WEIGHT', 'SEASON_EXP', 'JERSEY', 'POSITION', 'ROSTERSTATUS', 'TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'TEAM_CODE', 'TEAM_CITY', 'PLAYERCODE', 'FROM_YEAR', 'TO_YEAR', 'DLEAGUE_FLAG', 'NBA_FLAG', 'GAMES_PLAYED_FLAG', 'DRAFT_YEAR', 'DRAFT_ROUND', 'DRAFT_NUMBER']
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
            "PLAYER_SLUG",
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
            "NBA_FLAG",
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
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [
        "LeagueID"
    ],
    "parameter_patterns": {
        "LeagueID": null,
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

Last validated 2020-08-16