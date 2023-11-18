# HomePageV2
##### [nba_api/stats/endpoints/homepagev2.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/homepagev2.py)

##### Endpoint URL
>[https://stats.nba.com/stats/homepagev2](https://stats.nba.com/stats/homepagev2)

##### Valid URL
>[https://stats.nba.com/stats/homepagev2?GameScope=Season&LeagueID=00&PlayerOrTeam=Team&PlayerScope=All+Players&Season=2019-20&SeasonType=Regular+Season&StatType=Traditional](https://stats.nba.com/stats/homepagev2?GameScope=Season&LeagueID=00&PlayerOrTeam=Team&PlayerScope=All+Players&Season=2019-20&SeasonType=Regular+Season&StatType=Traditional)

## Parameters
| API Parameter Name                                                                                                      | Python Parameter Variable |                    Pattern                     | Required | Nullable |
|-------------------------------------------------------------------------------------------------------------------------|---------------------------|:----------------------------------------------:|:--------:|:--------:|
| [_**GameScope**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameScope)       | game_scope_detailed       | `^(Season)\|(Last 10)\|(Yesterday)\|(Finals)$` |   `Y`    |          | 
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)         | league_id                 |                   `^\d{2}$`                    |   `Y`    |          | 
| [_**PlayerOrTeam**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerOrTeam) | player_or_team            |              `^(Player)\|(Team)$`              |   `Y`    |          | 
| [_**PlayerScope**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerScope)   | player_scope              |          `^(All Players)\|(Rookies)$`          |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)             | season                    |                                                |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType)     | season_type_playoffs      | `^(Regular Season)\|(Pre Season)\|(Playoffs)$` |   `Y`    |          | 
| [_**StatType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#StatType)         | stat_type                 |   `^(Traditional)\|(Advanced)\|(Tracking)$`    |   `Y`    |          | 

## Data Sets
#### HomePageStat1 `home_page_stat1`
```text
['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'PTS']
```

#### HomePageStat2 `home_page_stat2`
```text
['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'REB']
```

#### HomePageStat3 `home_page_stat3`
```text
['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'AST']
```

#### HomePageStat4 `home_page_stat4`
```text
['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'STL']
```

#### HomePageStat5 `home_page_stat5`
```text
['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'FG_PCT']
```

#### HomePageStat6 `home_page_stat6`
```text
['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'FT_PCT']
```

#### HomePageStat7 `home_page_stat7`
```text
['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'FG3_PCT']
```

#### HomePageStat8 `home_page_stat8`
```text
['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'BLK']
```


## JSON
```json
{
    "data_sets": {
        "HomePageStat1": [
            "RANK",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "PTS"
        ],
        "HomePageStat2": [
            "RANK",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "REB"
        ],
        "HomePageStat3": [
            "RANK",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "AST"
        ],
        "HomePageStat4": [
            "RANK",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "STL"
        ],
        "HomePageStat5": [
            "RANK",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "FG_PCT"
        ],
        "HomePageStat6": [
            "RANK",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "FT_PCT"
        ],
        "HomePageStat7": [
            "RANK",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "FG3_PCT"
        ],
        "HomePageStat8": [
            "RANK",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "BLK"
        ]
    },
    "endpoint": "HomePageV2",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [],
    "parameter_patterns": {
        "GameScope": "^(Season)|(Last 10)|(Yesterday)|(Finals)$",
        "LeagueID": "^\\d{2}$",
        "PlayerOrTeam": "^(Player)|(Team)$",
        "PlayerScope": "^(All Players)|(Rookies)$",
        "Season": null,
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)$",
        "StatType": "^(Traditional)|(Advanced)|(Tracking)$"
    },
    "parameters": [
        "GameScope",
        "LeagueID",
        "PlayerOrTeam",
        "PlayerScope",
        "Season",
        "SeasonType",
        "StatType"
    ],
    "required_parameters": [
        "GameScope",
        "LeagueID",
        "PlayerOrTeam",
        "PlayerScope",
        "Season",
        "SeasonType",
        "StatType"
    ],
    "status": "success"
}
```

Last validated 2020-08-16