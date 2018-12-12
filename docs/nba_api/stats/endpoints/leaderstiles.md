# LeadersTiles
##### [nba_api/stats/endpoints/leaderstiles.py](https://github.com/swar/nba_api/blob/master/nba_api/stats/endpoints/leaderstiles.py)

##### Endpoint URL
>[https://stats.nba.com/stats/leaderstiles](https://stats.nba.com/stats/leaderstiles)

##### Valid URL
>[https://stats.nba.com/stats/leaderstiles?GameScope=Season&LeagueID=00&PlayerOrTeam=Team&PlayerScope=All+Players&Season=2018-19&SeasonType=Regular+Season&Stat=PTS](https://stats.nba.com/stats/leaderstiles?GameScope=Season&LeagueID=00&PlayerOrTeam=Team&PlayerScope=All+Players&Season=2018-19&SeasonType=Regular+Season&Stat=PTS)

## Parameters
API Parameter Name | Python Parameter Class | Python Parameter Variable | Pattern | Required | Nullable
------------ | ------------ | ------------ | :-----------: | :---: | :---:
_**GameScope**_ | [GameScopeDetailed](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameScope) | game_scope_detailed | `^(Season)\|(Last 10)\|(Yesterday)\|(Finals)$` | `Y` |  | 
_**LeagueID**_ | [LeagueID](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id | `^\d{2}$` | `Y` |  | 
_**PlayerOrTeam**_ | [PlayerOrTeam](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerOrTeam) | player_or_team | `^(Player)\|(Team)$` | `Y` |  | 
_**PlayerScope**_ | [PlayerScope](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerScope) | player_scope | `^(All Players)\|(Rookies)$` | `Y` |  | 
_**Season**_ | [Season](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season) | season | `^\d{4}-\d{2}$` | `Y` |  | 
_**SeasonType**_ | [SeasonTypePlayoffs](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType) | season_type_playoffs | `^(Regular Season)\|(Pre Season)\|(Playoffs)$` | `Y` |  | 
_**Stat**_ | [Stat](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Stat) | stat | `^(PTS)\|(REB)\|(AST)\|(FG_PCT)\|(FT_PCT)\|(FG3_PCT)\|(STL)\|(BLK)$` | `Y` |  | 

## Data Sets
#### AllTimeSeasonHigh `all_time_season_high`
```text
['TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'SEASON_YEAR', 'PTS']
```

#### LastSeasonHigh `last_season_high`
```text
['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'PTS']
```

#### LeadersTiles `leaders_tiles`
```text
['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'PTS']
```

#### LowSeasonHigh `low_season_high`
```text
['TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'SEASON_YEAR', 'PTS']
```


## JSON
```json
{
    "data_sets": {
        "AllTimeSeasonHigh": [
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "SEASON_YEAR",
            "PTS"
        ],
        "LastSeasonHigh": [
            "RANK",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "PTS"
        ],
        "LeadersTiles": [
            "RANK",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "PTS"
        ],
        "LowSeasonHigh": [
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "SEASON_YEAR",
            "PTS"
        ]
    },
    "endpoint": "LeadersTiles",
    "last_validated_date": "2018-12-11",
    "nullable_parameters": [],
    "parameter_patterns": {
        "GameScope": "^(Season)|(Last 10)|(Yesterday)|(Finals)$",
        "LeagueID": "^\\d{2}$",
        "PlayerOrTeam": "^(Player)|(Team)$",
        "PlayerScope": "^(All Players)|(Rookies)$",
        "Season": "^\\d{4}-\\d{2}$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)$",
        "Stat": "^(PTS)|(REB)|(AST)|(FG_PCT)|(FT_PCT)|(FG3_PCT)|(STL)|(BLK)$"
    },
    "parameters": [
        "GameScope",
        "LeagueID",
        "PlayerOrTeam",
        "PlayerScope",
        "Season",
        "SeasonType",
        "Stat"
    ],
    "required_parameters": [
        "GameScope",
        "LeagueID",
        "PlayerOrTeam",
        "PlayerScope",
        "Season",
        "SeasonType",
        "Stat"
    ],
    "status": "success"
}
```

Last validated 2018-12-11