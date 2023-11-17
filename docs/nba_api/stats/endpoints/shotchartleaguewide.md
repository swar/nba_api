# ShotChartLeagueWide
##### [nba_api/stats/endpoints/shotchartleaguewide.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/shotchartleaguewide.py)

##### Endpoint URL
>[https://stats.nba.com/stats/shotchartleaguewide](https://stats.nba.com/stats/shotchartleaguewide)

##### Valid URL
>[https://stats.nba.com/stats/shotchartleaguewide?LeagueID=00&Season=2019-20](https://stats.nba.com/stats/shotchartleaguewide?LeagueID=00&Season=2019-20)

## Parameters
| API Parameter Name                                                                                              | Python Parameter Variable | Pattern | Required | Nullable |
|-----------------------------------------------------------------------------------------------------------------|---------------------------|:-------:|:--------:|:--------:|
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id                 |         |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)     | season                    |         |   `Y`    |          | 

## Data Sets
#### League_Wide `league_wide`
```text
['GRID_TYPE', 'SHOT_ZONE_BASIC', 'SHOT_ZONE_AREA', 'SHOT_ZONE_RANGE', 'FGA', 'FGM', 'FG_PCT']
```


## JSON
```json
{
    "data_sets": {
        "League_Wide": [
            "GRID_TYPE",
            "SHOT_ZONE_BASIC",
            "SHOT_ZONE_AREA",
            "SHOT_ZONE_RANGE",
            "FGA",
            "FGM",
            "FG_PCT"
        ]
    },
    "endpoint": "ShotChartLeagueWide",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [],
    "parameter_patterns": {
        "LeagueID": null,
        "Season": null
    },
    "parameters": [
        "LeagueID",
        "Season"
    ],
    "required_parameters": [
        "LeagueID",
        "Season"
    ],
    "status": "success"
}
```

Last validated 2020-08-16