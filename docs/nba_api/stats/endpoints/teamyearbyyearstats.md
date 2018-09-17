# TeamYearByYearStats

##### Endpoint URL
>[https://stats.nba.com/stats/teamyearbyyearstats](https://stats.nba.com/stats/teamyearbyyearstats)

##### Valid URL
>[https://stats.nba.com/stats/teamyearbyyearstats?LeagueID=00&PerMode=Totals&SeasonType=Regular+Season&TeamID=1610612739](https://stats.nba.com/stats/teamyearbyyearstats?LeagueID=00&PerMode=Totals&SeasonType=Regular+Season&TeamID=1610612739)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**LeagueID**_ | `^\d{2}$` | `Y` |  | 
_**PerMode**_ | `^(Totals)\|(PerGame)$` | `Y` |  | 
_**SeasonType**_ | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$` | `Y` |  | 
_**TeamID**_ |  | `Y` |  | 

## Data Sets
#### TeamStats `team_stats`
```text
['TEAM_ID', 'TEAM_CITY', 'TEAM_NAME', 'YEAR', 'GP', 'WINS', 'LOSSES', 'WIN_PCT', 'CONF_RANK', 'DIV_RANK', 'PO_WINS', 'PO_LOSSES', 'CONF_COUNT', 'DIV_COUNT', 'NBA_FINALS_APPEARANCE', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'PF', 'STL', 'TOV', 'BLK', 'PTS', 'PTS_RANK']
```


## JSON
```json
{
    "data_sets": {
        "TeamStats": [
            "TEAM_ID",
            "TEAM_CITY",
            "TEAM_NAME",
            "YEAR",
            "GP",
            "WINS",
            "LOSSES",
            "WIN_PCT",
            "CONF_RANK",
            "DIV_RANK",
            "PO_WINS",
            "PO_LOSSES",
            "CONF_COUNT",
            "DIV_COUNT",
            "NBA_FINALS_APPEARANCE",
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
            "PF",
            "STL",
            "TOV",
            "BLK",
            "PTS",
            "PTS_RANK"
        ]
    },
    "endpoint": "TeamYearByYearStats",
    "nullable_parameters": [],
    "parameter_patterns": {
        "LeagueID": "^\\d{2}$",
        "PerMode": "^(Totals)|(PerGame)$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$",
        "TeamID": null
    },
    "parameters": [
        "LeagueID",
        "PerMode",
        "SeasonType",
        "TeamID"
    ],
    "required_parameters": [
        "LeagueID",
        "PerMode",
        "SeasonType",
        "TeamID"
    ],
    "status": "success"
}
```

Last validated 2018-09-16