# CumeStatsTeamGames
##### [nba_api/stats/endpoints/cumestatsteamgames.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/cumestatsteamgames.py)

##### Endpoint URL
>[https://stats.nba.com/stats/cumestatsteamgames](https://stats.nba.com/stats/cumestatsteamgames)

##### Valid URL
>[https://stats.nba.com/stats/cumestatsteamgames?LeagueID=00&Location=&Outcome=&Season=2019-20&SeasonID=&SeasonType=Regular+Season&TeamID=1610612739&VsConference=&VsDivision=&VsTeamID=](https://stats.nba.com/stats/cumestatsteamgames?LeagueID=00&Location=&Outcome=&Season=2019-20&SeasonID=&SeasonType=Regular+Season&TeamID=1610612739&VsConference=&VsDivision=&VsTeamID=)

## Parameters
| API Parameter Name                                                                                                      | Python Parameter Variable |                          Pattern                           | Required | Nullable |
|-------------------------------------------------------------------------------------------------------------------------|---------------------------|:----------------------------------------------------------:|:--------:|:--------:|
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)         | league_id                 |                                                            |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)             | season                    |                                                            |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType)     | season_type_all_star      | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$` |   `Y`    |          | 
| [_**TeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TeamID)             | team_id                   |                                                            |   `Y`    |          | 
| [_**VsTeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsTeamID)         | vs_team_id_nullable       |                                                            |          |   `Y`    | 
| [_**VsDivision**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsDivision)     | vs_division_nullable      |                                                            |          |   `Y`    | 
| [_**VsConference**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsConference) | vs_conference_nullable    |                                                            |          |   `Y`    | 
| [_**SeasonID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonID)         | season_id_nullable        |                                                            |          |   `Y`    | 
| [_**Outcome**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Outcome)           | outcome_nullable          |                                                            |          |   `Y`    | 
| [_**Location**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Location)         | location_nullable         |                                                            |          |   `Y`    | 

## Data Sets
#### CumeStatsTeamGames `cume_stats_team_games`
```text
['MATCHUP', 'GAME_ID']
```


## JSON
```json
{
    "data_sets": {
        "CumeStatsTeamGames": [
            "MATCHUP",
            "GAME_ID"
        ]
    },
    "endpoint": "CumeStatsTeamGames",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [
        "Location",
        "Outcome",
        "SeasonID",
        "VsConference",
        "VsDivision",
        "VsTeamID"
    ],
    "parameter_patterns": {
        "LeagueID": null,
        "Location": null,
        "Outcome": null,
        "Season": null,
        "SeasonID": null,
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$",
        "TeamID": null,
        "VsConference": null,
        "VsDivision": null,
        "VsTeamID": null
    },
    "parameters": [
        "LeagueID",
        "Location",
        "Outcome",
        "Season",
        "SeasonID",
        "SeasonType",
        "TeamID",
        "VsConference",
        "VsDivision",
        "VsTeamID"
    ],
    "required_parameters": [
        "LeagueID",
        "Season",
        "SeasonType",
        "TeamID"
    ],
    "status": "success"
}
```

Last validated 2020-08-16