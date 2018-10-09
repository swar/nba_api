# HomePageV2

##### Endpoint URL
>[https://stats.nba.com/stats/homepagev2](https://stats.nba.com/stats/homepagev2)

##### Valid URL
>[https://stats.nba.com/stats/homepagev2?GameScope=Season&LeagueID=00&PlayerOrTeam=Team&PlayerScope=All+Players&Season=2017-18&SeasonType=Regular+Season&StatType=Traditional](https://stats.nba.com/stats/homepagev2?GameScope=Season&LeagueID=00&PlayerOrTeam=Team&PlayerScope=All+Players&Season=2017-18&SeasonType=Regular+Season&StatType=Traditional)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**GameScope**_ | `^(Season)\|(Last 10)\|(Yesterday)\|(Finals)$` | `Y` |  | 
_**LeagueID**_ | `^\d{2}$` | `Y` |  | 
_**PlayerOrTeam**_ | `^(Player)\|(Team)$` | `Y` |  | 
_**PlayerScope**_ | `^(All Players)\|(Rookies)$` | `Y` |  | 
_**Season**_ | `^\d{4}-\d{2}$` | `Y` |  | 
_**SeasonType**_ | `^(Regular Season)\|(Pre Season)\|(Playoffs)$` | `Y` |  | 
_**StatType**_ | `^(Traditional)\|(Advanced)\|(Tracking)$` | `Y` |  | 

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
    "last_validated_date": "2018-10-08",
    "nullable_parameters": [],
    "parameter_patterns": {
        "GameScope": "^(Season)|(Last 10)|(Yesterday)|(Finals)$",
        "LeagueID": "^\\d{2}$",
        "PlayerOrTeam": "^(Player)|(Team)$",
        "PlayerScope": "^(All Players)|(Rookies)$",
        "Season": "^\\d{4}-\\d{2}$",
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

Last validated 2018-10-08