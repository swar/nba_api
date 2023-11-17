# DefenseHub
##### [nba_api/stats/endpoints/defensehub.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/defensehub.py)

##### Endpoint URL
>[https://stats.nba.com/stats/defensehub](https://stats.nba.com/stats/defensehub)

##### Valid URL
>[https://stats.nba.com/stats/defensehub?GameScope=Season&LeagueID=00&PlayerOrTeam=Team&PlayerScope=All+Players&Season=2019-20&SeasonType=Regular+Season](https://stats.nba.com/stats/defensehub?GameScope=Season&LeagueID=00&PlayerOrTeam=Team&PlayerScope=All+Players&Season=2019-20&SeasonType=Regular+Season)

## Parameters
| API Parameter Name                                                                                                      | Python Parameter Variable |                    Pattern                     | Required | Nullable |
|-------------------------------------------------------------------------------------------------------------------------|---------------------------|:----------------------------------------------:|:--------:|:--------:|
| [_**GameScope**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameScope)       | game_scope_detailed       | `^(Season)\|(Last 10)\|(Yesterday)\|(Finals)$` |   `Y`    |          | 
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)         | league_id                 |                   `^\d{2}$`                    |   `Y`    |          | 
| [_**PlayerOrTeam**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerOrTeam) | player_or_team            |              `^(Player)\|(Team)$`              |   `Y`    |          | 
| [_**PlayerScope**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerScope)   | player_scope              |          `^(All Players)\|(Rookies)$`          |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)             | season                    |                                                |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType)     | season_type_playoffs      | `^(Regular Season)\|(Pre Season)\|(Playoffs)$` |   `Y`    |          | 

## Data Sets
#### DefenseHubStat1 `defense_hub_stat1`
```text
['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'DREB']
```

#### DefenseHubStat10 `defense_hub_stat10`
```text
[]
```

#### DefenseHubStat2 `defense_hub_stat2`
```text
['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'STL']
```

#### DefenseHubStat3 `defense_hub_stat3`
```text
['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'BLK']
```

#### DefenseHubStat4 `defense_hub_stat4`
```text
['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'TM_DEF_RATING']
```

#### DefenseHubStat5 `defense_hub_stat5`
```text
['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'OVERALL_PM']
```

#### DefenseHubStat6 `defense_hub_stat6`
```text
['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'THREEP_DFGPCT']
```

#### DefenseHubStat7 `defense_hub_stat7`
```text
['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'TWOP_DFGPCT']
```

#### DefenseHubStat8 `defense_hub_stat8`
```text
['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'FIFETEENF_DFGPCT']
```

#### DefenseHubStat9 `defense_hub_stat9`
```text
['RANK', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'DEF_RIM_PCT']
```


## JSON
```json
{
    "data_sets": {
        "DefenseHubStat1": [
            "RANK",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "DREB"
        ],
        "DefenseHubStat10": [],
        "DefenseHubStat2": [
            "RANK",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "STL"
        ],
        "DefenseHubStat3": [
            "RANK",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "BLK"
        ],
        "DefenseHubStat4": [
            "RANK",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "TM_DEF_RATING"
        ],
        "DefenseHubStat5": [
            "RANK",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "OVERALL_PM"
        ],
        "DefenseHubStat6": [
            "RANK",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "THREEP_DFGPCT"
        ],
        "DefenseHubStat7": [
            "RANK",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "TWOP_DFGPCT"
        ],
        "DefenseHubStat8": [
            "RANK",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "FIFETEENF_DFGPCT"
        ],
        "DefenseHubStat9": [
            "RANK",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "DEF_RIM_PCT"
        ]
    },
    "endpoint": "DefenseHub",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [],
    "parameter_patterns": {
        "GameScope": "^(Season)|(Last 10)|(Yesterday)|(Finals)$",
        "LeagueID": "^\\d{2}$",
        "PlayerOrTeam": "^(Player)|(Team)$",
        "PlayerScope": "^(All Players)|(Rookies)$",
        "Season": null,
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)$"
    },
    "parameters": [
        "GameScope",
        "LeagueID",
        "PlayerOrTeam",
        "PlayerScope",
        "Season",
        "SeasonType"
    ],
    "required_parameters": [
        "GameScope",
        "LeagueID",
        "PlayerOrTeam",
        "PlayerScope",
        "Season",
        "SeasonType"
    ],
    "status": "success"
}
```

Last validated 2020-08-16