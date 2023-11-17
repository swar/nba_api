# CommonPlayoffSeries
##### [nba_api/stats/endpoints/commonplayoffseries.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/commonplayoffseries.py)

##### Endpoint URL
>[https://stats.nba.com/stats/commonplayoffseries](https://stats.nba.com/stats/commonplayoffseries)

##### Valid URL
>[https://stats.nba.com/stats/commonplayoffseries?LeagueID=00&Season=2019-20&SeriesID=](https://stats.nba.com/stats/commonplayoffseries?LeagueID=00&Season=2019-20&SeriesID=)

## Parameters
| API Parameter Name                                                                                              | Python Parameter Variable | Pattern | Required | Nullable |
|-----------------------------------------------------------------------------------------------------------------|---------------------------|:-------:|:--------:|:--------:|
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id                 |         |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)     | season                    |         |   `Y`    |          | 
| [_**SeriesID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeriesID) | series_id_nullable        |         |          |   `Y`    | 

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
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [
        "SeriesID"
    ],
    "parameter_patterns": {
        "LeagueID": null,
        "Season": null,
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

Last validated 2020-08-16