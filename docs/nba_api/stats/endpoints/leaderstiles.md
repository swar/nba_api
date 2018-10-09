# LeadersTiles

##### Endpoint URL
>[https://stats.nba.com/stats/leaderstiles](https://stats.nba.com/stats/leaderstiles)

##### Valid URL
>[https://stats.nba.com/stats/leaderstiles?GameScope=Season&LeagueID=00&PlayerOrTeam=Team&PlayerScope=All+Players&Season=2017-18&SeasonType=Regular+Season&Stat=PTS](https://stats.nba.com/stats/leaderstiles?GameScope=Season&LeagueID=00&PlayerOrTeam=Team&PlayerScope=All+Players&Season=2017-18&SeasonType=Regular+Season&Stat=PTS)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**GameScope**_ | `^(Season)\|(Last 10)\|(Yesterday)\|(Finals)$` | `Y` |  | 
_**LeagueID**_ | `^\d{2}$` | `Y` |  | 
_**PlayerOrTeam**_ | `^(Player)\|(Team)$` | `Y` |  | 
_**PlayerScope**_ | `^(All Players)\|(Rookies)$` | `Y` |  | 
_**Season**_ | `^\d{4}-\d{2}$` | `Y` |  | 
_**SeasonType**_ | `^(Regular Season)\|(Pre Season)\|(Playoffs)$` | `Y` |  | 
_**Stat**_ | `^(PTS)\|(REB)\|(AST)\|(FG_PCT)\|(FT_PCT)\|(FG3_PCT)\|(STL)\|(BLK)$` | `Y` |  | 

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
    "last_validated_date": "2018-10-08",
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

Last validated 2018-10-08