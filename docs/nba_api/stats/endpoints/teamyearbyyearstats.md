# TeamYearByYearStats
##### [nba_api/stats/endpoints/teamyearbyyearstats.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/teamyearbyyearstats.py)

##### Endpoint URL
>[https://stats.nba.com/stats/teamyearbyyearstats](https://stats.nba.com/stats/teamyearbyyearstats)

##### Valid URL
>[https://stats.nba.com/stats/teamyearbyyearstats?LeagueID=00&PerMode=Totals&SeasonType=Regular+Season&TeamID=1610612739](https://stats.nba.com/stats/teamyearbyyearstats?LeagueID=00&PerMode=Totals&SeasonType=Regular+Season&TeamID=1610612739)

## Parameters
| API Parameter Name                                                                                                  | Python Parameter Variable |                          Pattern                           | Required | Nullable |
|---------------------------------------------------------------------------------------------------------------------|---------------------------|:----------------------------------------------------------:|:--------:|:--------:|
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)     | league_id                 |                         `^\d{2}$`                          |   `Y`    |          | 
| [_**PerMode**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PerMode)       | per_mode_simple           |                  `^(Totals)\|(PerGame)$`                   |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType) | season_type_all_star      | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$` |   `Y`    |          | 
| [_**TeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TeamID)         | team_id                   |                                                            |   `Y`    |          | 

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
    "last_validated_date": "2020-08-15",
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

Last validated 2020-08-16