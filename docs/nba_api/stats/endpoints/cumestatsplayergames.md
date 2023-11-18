# CumeStatsPlayerGames
##### [nba_api/stats/endpoints/cumestatsplayergames.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/cumestatsplayergames.py)

##### Endpoint URL
>[https://stats.nba.com/stats/cumestatsplayergames](https://stats.nba.com/stats/cumestatsplayergames)

##### Valid URL
>[https://stats.nba.com/stats/cumestatsplayergames?LeagueID=00&Location=&Outcome=&PlayerID=2544&Season=2019-20&SeasonType=Regular+Season&VsConference=&VsDivision=&VsTeamID=](https://stats.nba.com/stats/cumestatsplayergames?LeagueID=00&Location=&Outcome=&PlayerID=2544&Season=2019-20&SeasonType=Regular+Season&VsConference=&VsDivision=&VsTeamID=)

## Parameters
| API Parameter Name                                                                                                      | Python Parameter Variable |                          Pattern                           | Required | Nullable |
|-------------------------------------------------------------------------------------------------------------------------|---------------------------|:----------------------------------------------------------:|:--------:|:--------:|
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)         | league_id                 |                                                            |   `Y`    |          | 
| [_**PlayerID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerID)         | player_id                 |                                                            |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)             | season                    |                                                            |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType)     | season_type_all_star      | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$` |   `Y`    |          | 
| [_**VsTeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsTeamID)         | vs_team_id_nullable       |                                                            |          |   `Y`    | 
| [_**VsDivision**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsDivision)     | vs_division_nullable      |                                                            |          |   `Y`    | 
| [_**VsConference**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsConference) | vs_conference_nullable    |                                                            |          |   `Y`    | 
| [_**Outcome**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Outcome)           | outcome_nullable          |                                                            |          |   `Y`    | 
| [_**Location**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Location)         | location_nullable         |                                                            |          |   `Y`    | 

## Data Sets
#### CumeStatsPlayerGames `cume_stats_player_games`
```text
['MATCHUP', 'GAME_ID']
```


## JSON
```json
{
    "data_sets": {
        "CumeStatsPlayerGames": [
            "MATCHUP",
            "GAME_ID"
        ]
    },
    "endpoint": "CumeStatsPlayerGames",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [
        "Location",
        "Outcome",
        "VsConference",
        "VsDivision",
        "VsTeamID"
    ],
    "parameter_patterns": {
        "LeagueID": null,
        "Location": null,
        "Outcome": null,
        "PlayerID": null,
        "Season": null,
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$",
        "VsConference": null,
        "VsDivision": null,
        "VsTeamID": null
    },
    "parameters": [
        "LeagueID",
        "Location",
        "Outcome",
        "PlayerID",
        "Season",
        "SeasonType",
        "VsConference",
        "VsDivision",
        "VsTeamID"
    ],
    "required_parameters": [
        "LeagueID",
        "PlayerID",
        "Season",
        "SeasonType"
    ],
    "status": "success"
}
```

Last validated 2020-08-16