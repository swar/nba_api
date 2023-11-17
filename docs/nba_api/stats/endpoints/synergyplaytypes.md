# SynergyPlayTypes
##### [nba_api/stats/endpoints/synergyplaytypes.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/synergyplaytypes.py)

##### Endpoint URL
>[https://stats.nba.com/stats/synergyplaytypes](https://stats.nba.com/stats/synergyplaytypes)

##### Valid URL
>[https://stats.nba.com/stats/synergyplaytypes?LeagueID=00&PerMode=Totals&PlayType=&PlayerOrTeam=T&SeasonType=Regular+Season&SeasonYear=2019-20&TypeGrouping=](https://stats.nba.com/stats/synergyplaytypes?LeagueID=00&PerMode=Totals&PlayType=&PlayerOrTeam=T&SeasonType=Regular+Season&SeasonYear=2019-20&TypeGrouping=)

## Parameters
| API Parameter Name                                                                                                      | Python Parameter Variable   |                                Pattern                                 | Required | Nullable |
|-------------------------------------------------------------------------------------------------------------------------|-----------------------------|:----------------------------------------------------------------------:|:--------:|:--------:|
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)         | league_id                   |                               `^\d{2}$`                                |   `Y`    |          | 
| [_**PerMode**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PerMode)           | per_mode_simple             |                        `^(Totals)\|(PerGame)$`                         |   `Y`    |          | 
| [_**PlayerOrTeam**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerOrTeam) | player_or_team_abbreviation |                              `^(P)\|(T)$`                              |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType)     | season_type_all_star        | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)\|(All-Star)$` |   `Y`    |          | 
| [_**SeasonYear**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonYear)     | season                      |                       `^(\d{4}-\d{2})\|(\d{4})$`                       |   `Y`    |          | 
| [_**TypeGrouping**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TypeGrouping) | type_grouping_nullable      |                                                                        |          |   `Y`    | 
| [_**PlayType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayType)         | play_type_nullable          |                                                                        |          |   `Y`    | 

## Data Sets
#### SynergyPlayType `synergy_play_type`
```text
['SEASON_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'PLAY_TYPE', 'TYPE_GROUPING', 'PERCENTILE', 'GP', 'POSS_PCT', 'PPP', 'FG_PCT', 'FT_POSS_PCT', 'TOV_POSS_PCT', 'SF_POSS_PCT', 'PLUSONE_POSS_PCT', 'SCORE_POSS_PCT', 'EFG_PCT', 'POSS', 'PTS', 'FGM', 'FGA', 'FGMX']
```


## JSON
```json
{
    "data_sets": {
        "SynergyPlayType": [
            "SEASON_ID",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "PLAY_TYPE",
            "TYPE_GROUPING",
            "PERCENTILE",
            "GP",
            "POSS_PCT",
            "PPP",
            "FG_PCT",
            "FT_POSS_PCT",
            "TOV_POSS_PCT",
            "SF_POSS_PCT",
            "PLUSONE_POSS_PCT",
            "SCORE_POSS_PCT",
            "EFG_PCT",
            "POSS",
            "PTS",
            "FGM",
            "FGA",
            "FGMX"
        ]
    },
    "endpoint": "SynergyPlayTypes",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [
        "PlayType",
        "TypeGrouping"
    ],
    "parameter_patterns": {
        "LeagueID": "^\\d{2}$",
        "PerMode": "^(Totals)|(PerGame)$",
        "PlayType": null,
        "PlayerOrTeam": "^(P)|(T)$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)|(All-Star)$",
        "SeasonYear": "^(\\d{4}-\\d{2})|(\\d{4})$",
        "TypeGrouping": null
    },
    "parameters": [
        "LeagueID",
        "PerMode",
        "PlayType",
        "PlayerOrTeam",
        "SeasonType",
        "SeasonYear",
        "TypeGrouping"
    ],
    "required_parameters": [
        "LeagueID",
        "PerMode",
        "PlayerOrTeam",
        "SeasonType",
        "SeasonYear"
    ],
    "status": "success"
}
```

Last validated 2020-08-16