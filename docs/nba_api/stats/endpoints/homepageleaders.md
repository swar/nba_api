# HomePageLeaders

##### Endpoint URL
>[https://stats.nba.com/stats/homepageleaders](https://stats.nba.com/stats/homepageleaders)

##### Valid URL
>[https://stats.nba.com/stats/homepageleaders?GameScope=Season&LeagueID=00&PlayerOrTeam=Team&PlayerScope=All+Players&Season=2017-18&SeasonType=Regular+Season&StatCategory=Points](https://stats.nba.com/stats/homepageleaders?GameScope=Season&LeagueID=00&PlayerOrTeam=Team&PlayerScope=All+Players&Season=2017-18&SeasonType=Regular+Season&StatCategory=Points)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**GameScope**_ | `^(Season)\|(Last 10)\|(Yesterday)\|(Finals)$` | `Y` |  | 
_**LeagueID**_ | `^\d{2}$` | `Y` |  | 
_**PlayerOrTeam**_ | `^(Player)\|(Team)$` | `Y` |  | 
_**PlayerScope**_ | `^(All Players)\|(Rookies)$` | `Y` |  | 
_**Season**_ | `^\d{4}-\d{2}$` | `Y` |  | 
_**SeasonType**_ | `^(Regular Season)\|(Pre Season)\|(Playoffs)$` | `Y` |  | 
_**StatCategory**_ | `^(Points)\|(Rebounds)\|(Assists)\|(Defense)\|(Clutch)\|(Playmaking)\|(Efficiency)\|(Fast Break)\|(Scoring Breakdown)$` | `Y` |  | 

## Data Sets
#### HomePageLeaders `home_page_leaders`
```text
['RANK', 'TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'PTS', 'FG_PCT', 'FG3_PCT', 'FT_PCT', 'EFG_PCT', 'TS_PCT', 'PTS_PER48']
```

#### LeagueAverage `league_average`
```text
['PTS', 'FG_PCT', 'FG3_PCT', 'FT_PCT', 'EFG_PCT', 'TS_PCT', 'PTS_PER48']
```

#### LeagueMax `league_max`
```text
['PTS', 'FG_PCT', 'FG3_PCT', 'FT_PCT', 'EFG_PCT', 'TS_PCT', 'PTS_PER48']
```


## JSON
```json
{
    "data_sets": {
        "HomePageLeaders": [
            "RANK",
            "TEAM_ID",
            "TEAM_NAME",
            "TEAM_ABBREVIATION",
            "PTS",
            "FG_PCT",
            "FG3_PCT",
            "FT_PCT",
            "EFG_PCT",
            "TS_PCT",
            "PTS_PER48"
        ],
        "LeagueAverage": [
            "PTS",
            "FG_PCT",
            "FG3_PCT",
            "FT_PCT",
            "EFG_PCT",
            "TS_PCT",
            "PTS_PER48"
        ],
        "LeagueMax": [
            "PTS",
            "FG_PCT",
            "FG3_PCT",
            "FT_PCT",
            "EFG_PCT",
            "TS_PCT",
            "PTS_PER48"
        ]
    },
    "endpoint": "HomePageLeaders",
    "last_validated_date": "2018-10-08",
    "nullable_parameters": [],
    "parameter_patterns": {
        "GameScope": "^(Season)|(Last 10)|(Yesterday)|(Finals)$",
        "LeagueID": "^\\d{2}$",
        "PlayerOrTeam": "^(Player)|(Team)$",
        "PlayerScope": "^(All Players)|(Rookies)$",
        "Season": "^\\d{4}-\\d{2}$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)$",
        "StatCategory": "^(Points)|(Rebounds)|(Assists)|(Defense)|(Clutch)|(Playmaking)|(Efficiency)|(Fast Break)|(Scoring Breakdown)$"
    },
    "parameters": [
        "GameScope",
        "LeagueID",
        "PlayerOrTeam",
        "PlayerScope",
        "Season",
        "SeasonType",
        "StatCategory"
    ],
    "required_parameters": [
        "GameScope",
        "LeagueID",
        "PlayerOrTeam",
        "PlayerScope",
        "Season",
        "SeasonType",
        "StatCategory"
    ],
    "status": "success"
}
```

Last validated 2018-10-08