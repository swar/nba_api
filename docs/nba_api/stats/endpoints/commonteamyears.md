# CommonTeamYears

##### Endpoint URL
>[https://stats.nba.com/stats/commonteamyears](https://stats.nba.com/stats/commonteamyears)

##### Valid URL
>[https://stats.nba.com/stats/commonteamyears?LeagueID=00](https://stats.nba.com/stats/commonteamyears?LeagueID=00)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**LeagueID**_ | `^\d{2}$` | `Y` |  | 

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

Last validated 2018-09-16