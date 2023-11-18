# MatchupsRollup
##### [nba_api/stats/endpoints/matchupsrollup.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/matchupsrollup.py)

##### Endpoint URL
>[https://stats.nba.com/stats/matchupsrollup](https://stats.nba.com/stats/matchupsrollup)

##### Valid URL
>[https://stats.nba.com/stats/matchupsrollup?DefPlayerID=&DefTeamID=&LeagueID=00&OffPlayerID=&OffTeamID=&PerMode=Totals&Season=2019-20&SeasonType=Regular+Season](https://stats.nba.com/stats/matchupsrollup?DefPlayerID=&DefTeamID=&LeagueID=00&OffPlayerID=&OffTeamID=&PerMode=Totals&Season=2019-20&SeasonType=Regular+Season)

## Parameters
| API Parameter Name                                                                                                    | Python Parameter Variable |                           Pattern                            | Required | Nullable |
|-----------------------------------------------------------------------------------------------------------------------|---------------------------|:------------------------------------------------------------:|:--------:|:--------:|
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)       | league_id                 |                          `^\d{2}$`                           |   `Y`    |          | 
| [_**PerMode**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PerMode)         | per_mode_simple           |                                                              |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)           | season                    |                      `^(\d{4}-\d{2})$`                       |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType)   | season_type_playoffs      | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(Pre-Season)$` |   `Y`    |          | 
| [_**OffTeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#OffTeamID)     | off_team_id_nullable      |                                                              |          |   `Y`    | 
| [_**OffPlayerID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#OffPlayerID) | off_player_id_nullable    |                                                              |          |   `Y`    | 
| [_**DefTeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DefTeamID)     | def_team_id_nullable      |                                                              |          |   `Y`    | 
| [_**DefPlayerID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DefPlayerID) | def_player_id_nullable    |                                                              |          |   `Y`    | 

## Data Sets
#### MatchupsRollup `matchups_rollup`
```text
['SEASON_ID', 'POSITION', 'PERCENT_OF_TIME', 'DEF_PLAYER_ID', 'DEF_PLAYER_NAME', 'GP', 'MATCHUP_MIN', 'PARTIAL_POSS', 'PLAYER_PTS', 'TEAM_PTS', 'MATCHUP_AST', 'MATCHUP_TOV', 'MATCHUP_BLK', 'MATCHUP_FGM', 'MATCHUP_FGA', 'MATCHUP_FG_PCT', 'MATCHUP_FG3M', 'MATCHUP_FG3A', 'MATCHUP_FG3_PCT', 'MATCHUP_FTM', 'MATCHUP_FTA', 'SFL']
```


## JSON
```json
{
    "data_sets": {
        "MatchupsRollup": [
            "SEASON_ID",
            "POSITION",
            "PERCENT_OF_TIME",
            "DEF_PLAYER_ID",
            "DEF_PLAYER_NAME",
            "GP",
            "MATCHUP_MIN",
            "PARTIAL_POSS",
            "PLAYER_PTS",
            "TEAM_PTS",
            "MATCHUP_AST",
            "MATCHUP_TOV",
            "MATCHUP_BLK",
            "MATCHUP_FGM",
            "MATCHUP_FGA",
            "MATCHUP_FG_PCT",
            "MATCHUP_FG3M",
            "MATCHUP_FG3A",
            "MATCHUP_FG3_PCT",
            "MATCHUP_FTM",
            "MATCHUP_FTA",
            "SFL"
        ]
    },
    "endpoint": "MatchupsRollup",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [
        "DefPlayerID",
        "DefTeamID",
        "OffPlayerID",
        "OffTeamID"
    ],
    "parameter_patterns": {
        "DefPlayerID": null,
        "DefTeamID": null,
        "LeagueID": "^\\d{2}$",
        "OffPlayerID": null,
        "OffTeamID": null,
        "PerMode": null,
        "Season": "^(\\d{4}-\\d{2})$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(Pre-Season)$"
    },
    "parameters": [
        "DefPlayerID",
        "DefTeamID",
        "LeagueID",
        "OffPlayerID",
        "OffTeamID",
        "PerMode",
        "Season",
        "SeasonType"
    ],
    "required_parameters": [
        "LeagueID",
        "PerMode",
        "Season",
        "SeasonType"
    ],
    "status": "success"
}
```

Last validated 2020-08-16