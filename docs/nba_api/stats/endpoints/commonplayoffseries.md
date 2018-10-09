# CommonPlayoffSeries

##### Endpoint URL
>[https://stats.nba.com/stats/commonplayoffseries](https://stats.nba.com/stats/commonplayoffseries)

##### Valid URL
>[https://stats.nba.com/stats/commonplayoffseries?LeagueID=&Season=2017-18&SeriesID=](https://stats.nba.com/stats/commonplayoffseries?LeagueID=&Season=2017-18&SeriesID=)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**Season**_ | `^\d{4}-\d{2}$` | `Y` |  | 
_**SeriesID**_ |  |  | `Y` | 
_**LeagueID**_ | `(00)\|(20)\|(10)` | `Y` | `Y` | 

## Data Sets
#### PlayoffSeries `playoff_series`
```text
['GAME_ID', 'HOME_TEAM_ID', 'VISITOR_TEAM_ID', 'SERIES_ID', 'GAME_NUM']
```


## JSON
```json
{
    "data_sets": {
        "PlayoffSeries": [
            "GAME_ID",
            "HOME_TEAM_ID",
            "VISITOR_TEAM_ID",
            "SERIES_ID",
            "GAME_NUM"
        ]
    },
    "endpoint": "CommonPlayoffSeries",
    "last_validated_date": "2018-10-08",
    "nullable_parameters": [
        "LeagueID",
        "SeriesID"
    ],
    "parameter_patterns": {
        "LeagueID": "(00)|(20)|(10)",
        "Season": "^\\d{4}-\\d{2}$",
        "SeriesID": null
    },
    "parameters": [
        "LeagueID",
        "Season",
        "SeriesID"
    ],
    "required_parameters": [
        "LeagueID",
        "Season"
    ],
    "status": "success"
}
```

Last validated 2018-10-08