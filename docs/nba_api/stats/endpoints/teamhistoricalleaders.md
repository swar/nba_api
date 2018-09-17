# TeamHistoricalLeaders

##### Endpoint URL
>[https://stats.nba.com/stats/teamhistoricalleaders](https://stats.nba.com/stats/teamhistoricalleaders)

##### Valid URL
>[https://stats.nba.com/stats/teamhistoricalleaders?LeagueID=00&SeasonID=22017&TeamID=1610612739](https://stats.nba.com/stats/teamhistoricalleaders?LeagueID=00&SeasonID=22017&TeamID=1610612739)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**LeagueID**_ | `^\d{2}$` | `Y` |  | 
_**SeasonID**_ | `^\d{5}$` | `Y` |  | 
_**TeamID**_ |  | `Y` |  | 

## Data Sets
#### CareerLeadersByTeam `career_leaders_by_team`
```text
['TEAM_ID', 'PTS', 'PTS_PERSON_ID', 'PTS_PLAYER', 'AST', 'AST_PERSON_ID', 'AST_PLAYER', 'REB', 'REB_PERSON_ID', 'REB_PLAYER', 'BLK', 'BLK_PERSON_ID', 'BLK_PLAYER', 'STL', 'STL_PERSON_ID', 'STL_PLAYER', 'SEASON_YEAR']
```


## JSON
```json
{
    "data_sets": {
        "CareerLeadersByTeam": [
            "TEAM_ID",
            "PTS",
            "PTS_PERSON_ID",
            "PTS_PLAYER",
            "AST",
            "AST_PERSON_ID",
            "AST_PLAYER",
            "REB",
            "REB_PERSON_ID",
            "REB_PLAYER",
            "BLK",
            "BLK_PERSON_ID",
            "BLK_PLAYER",
            "STL",
            "STL_PERSON_ID",
            "STL_PLAYER",
            "SEASON_YEAR"
        ]
    },
    "endpoint": "TeamHistoricalLeaders",
    "nullable_parameters": [],
    "parameter_patterns": {
        "LeagueID": "^\\d{2}$",
        "SeasonID": "^\\d{5}$",
        "TeamID": null
    },
    "parameters": [
        "LeagueID",
        "SeasonID",
        "TeamID"
    ],
    "required_parameters": [
        "LeagueID",
        "SeasonID",
        "TeamID"
    ],
    "status": "success"
}
```

Last validated 2018-09-16