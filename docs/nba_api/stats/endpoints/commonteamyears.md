# CommonTeamYears
##### [nba_api/stats/endpoints/commonteamyears.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/commonteamyears.py)

##### Endpoint URL
>[https://stats.nba.com/stats/commonteamyears](https://stats.nba.com/stats/commonteamyears)

##### Valid URL
>[https://stats.nba.com/stats/commonteamyears?LeagueID=00](https://stats.nba.com/stats/commonteamyears?LeagueID=00)

## Parameters
| API Parameter Name                                                                                              | Python Parameter Variable |  Pattern  | Required | Nullable |
|-----------------------------------------------------------------------------------------------------------------|---------------------------|:---------:|:--------:|:--------:|
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id                 | `^\d{2}$` |   `Y`    |          | 

## Data Sets
#### TeamYears `team_years`
```text
['LEAGUE_ID', 'TEAM_ID', 'MIN_YEAR', 'MAX_YEAR', 'ABBREVIATION']
```


## JSON
```json
{
    "data_sets": {
        "TeamYears": [
            "LEAGUE_ID",
            "TEAM_ID",
            "MIN_YEAR",
            "MAX_YEAR",
            "ABBREVIATION"
        ]
    },
    "endpoint": "CommonTeamYears",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [],
    "parameter_patterns": {
        "LeagueID": "^\\d{2}$"
    },
    "parameters": [
        "LeagueID"
    ],
    "required_parameters": [
        "LeagueID"
    ],
    "status": "success"
}
```

Last validated 2020-08-16