# InfographicFanDuelPlayer
##### [nba_api/stats/endpoints/infographicfanduelplayer.py](https://github.com/swar/nba_api/blob/master/nba_api/stats/endpoints/infographicfanduelplayer.py)

##### Endpoint URL
>[https://stats.nba.com/stats/infographicfanduelplayer](https://stats.nba.com/stats/infographicfanduelplayer)

##### Valid URL
>[https://stats.nba.com/stats/infographicfanduelplayer?GameID=0021700807](https://stats.nba.com/stats/infographicfanduelplayer?GameID=0021700807)

## Parameters
API Parameter Name | Python Parameter Class | Python Parameter Variable | Pattern | Required | Nullable
------------ | ------------ | ------------ | :-----------: | :---: | :---:
_**GameID**_ | [GameID](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameID) | game_id | `^\d{10}$` | `Y` |  | 

## Data Sets
#### FanDuelPlayer `fan_duel_player`
```text
['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'JERSEY_NUM', 'PLAYER_POSITION', 'LOCATION', 'FAN_DUEL_PTS', 'NBA_FANTASY_PTS', 'USG_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS']
```


## JSON
```json
{
    "data_sets": {
        "FanDuelPlayer": [
            "PLAYER_ID",
            "PLAYER_NAME",
            "TEAM_ID",
            "TEAM_NAME",
            "TEAM_ABBREVIATION",
            "JERSEY_NUM",
            "PLAYER_POSITION",
            "LOCATION",
            "FAN_DUEL_PTS",
            "NBA_FANTASY_PTS",
            "USG_PCT",
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
            "PLUS_MINUS"
        ]
    },
    "endpoint": "InfographicFanDuelPlayer",
    "last_validated_date": "2018-12-11",
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

Last validated 2018-12-11