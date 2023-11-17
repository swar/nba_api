# FranchisePlayers
##### [nba_api/stats/endpoints/franchiseplayers.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/franchiseplayers.py)

##### Endpoint URL
>[https://stats.nba.com/stats/franchiseplayers](https://stats.nba.com/stats/franchiseplayers)

##### Valid URL
>[https://stats.nba.com/stats/franchiseplayers?LeagueID=00&PerMode=Totals&SeasonType=Regular+Season&TeamID=1610612739](https://stats.nba.com/stats/franchiseplayers?LeagueID=00&PerMode=Totals&SeasonType=Regular+Season&TeamID=1610612739)

## Parameters
| API Parameter Name                                                                                                  | Python Parameter Variable |                                                                    Pattern                                                                    | Required | Nullable |
|---------------------------------------------------------------------------------------------------------------------|---------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------:|:--------:|:--------:|
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)     | league_id                 |                                                                                                                                               |   `Y`    |          | 
| [_**PerMode**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PerMode)       | per_mode_detailed         | `^(Totals)\|(PerGame)\|(MinutesPer)\|(Per48)\|(Per40)\|(Per36)\|(PerMinute)\|(PerPossession)\|(PerPlay)\|(Per100Possessions)\|(Per100Plays)$` |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType) | season_type_all_star      |                                          `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$`                                           |   `Y`    |          | 
| [_**TeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TeamID)         | team_id                   |                                                                                                                                               |   `Y`    |          | 

## Data Sets
#### FranchisePlayers `franchise_players`
```text
['LEAGUE_ID', 'TEAM_ID', 'TEAM', 'PERSON_ID', 'PLAYER', 'SEASON_TYPE', 'ACTIVE_WITH_TEAM', 'GP', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'PF', 'STL', 'TOV', 'BLK', 'PTS']
```


## JSON
```json
{
    "data_sets": {
        "FranchisePlayers": [
            "LEAGUE_ID",
            "TEAM_ID",
            "TEAM",
            "PERSON_ID",
            "PLAYER",
            "SEASON_TYPE",
            "ACTIVE_WITH_TEAM",
            "GP",
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
            "PTS"
        ]
    },
    "endpoint": "FranchisePlayers",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [],
    "parameter_patterns": {
        "LeagueID": null,
        "PerMode": "^(Totals)|(PerGame)|(MinutesPer)|(Per48)|(Per40)|(Per36)|(PerMinute)|(PerPossession)|(PerPlay)|(Per100Possessions)|(Per100Plays)$",
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