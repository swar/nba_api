# CommonPlayoffSeries
##### [nba_api/stats/endpoints/commonplayoffseries.py](https://github.com/swar/nba_api/blob/master/nba_api/stats/endpoints/commonplayoffseries.py)

##### Endpoint URL
>[https://stats.nba.com/stats/commonplayoffseries](https://stats.nba.com/stats/commonplayoffseries)

##### Valid URL
>[https://stats.nba.com/stats/commonplayoffseries?LeagueID=&Season=2018-19&SeriesID=](https://stats.nba.com/stats/commonplayoffseries?LeagueID=&Season=2018-19&SeriesID=)

## Parameters
API Parameter Name | Python Parameter Class | Python Parameter Variable | Pattern | Required | Nullable
------------ | ------------ | ------------ | :-----------: | :---: | :---:
_**Season**_ | [Season](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season) | season | `^\d{4}-\d{2}$` | `Y` |  | 
_**SeriesID**_ | [SeriesIDNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeriesID) | series_id_nullable |  |  | `Y` | 
_**LeagueID**_ | [LeagueIDNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id_nullable | `(00)\|(20)\|(10)` | `Y` | `Y` | 

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
    "last_validated_date": "2018-12-11",
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

Last validated 2018-12-11