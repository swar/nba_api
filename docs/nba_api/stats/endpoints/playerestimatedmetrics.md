# PlayerEstimatedMetrics
##### [nba_api/stats/endpoints/playerestimatedmetrics.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/playerestimatedmetrics.py)

##### Endpoint URL
>[https://stats.nba.com/stats/playerestimatedmetrics](https://stats.nba.com/stats/playerestimatedmetrics)

##### Valid URL
>[https://stats.nba.com/stats/playerestimatedmetrics?LeagueID=00&Season=2019-20&SeasonType=Regular+Season](https://stats.nba.com/stats/playerestimatedmetrics?LeagueID=00&Season=2019-20&SeasonType=Regular+Season)

## Parameters
| API Parameter Name                                                                                                  | Python Parameter Variable | Pattern | Required | Nullable |
|---------------------------------------------------------------------------------------------------------------------|---------------------------|:-------:|:--------:|:--------:|
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)     | league_id                 |         |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)         | season                    |         |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType) | season_type               |         |   `Y`    |          | 

## Data Sets
#### PlayerEstimatedMetrics `player_estimated_metrics`
```text
['PLAYER_ID', 'PLAYER_NAME', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'E_OFF_RATING', 'E_DEF_RATING', 'E_NET_RATING', 'E_AST_RATIO', 'E_OREB_PCT', 'E_DREB_PCT', 'E_REB_PCT', 'E_TOV_PCT', 'E_USG_PCT', 'E_PACE', 'GP_RANK', 'W_RANK', 'L_RANK', 'W_PCT_RANK', 'MIN_RANK', 'E_OFF_RATING_RANK', 'E_DEF_RATING_RANK', 'E_NET_RATING_RANK', 'E_AST_RATIO_RANK', 'E_OREB_PCT_RANK', 'E_DREB_PCT_RANK', 'E_REB_PCT_RANK', 'E_TOV_PCT_RANK', 'E_USG_PCT_RANK', 'E_PACE_RANK']
```


## JSON
```json
{
    "data_sets": {
        "PlayerEstimatedMetrics": [
            "PLAYER_ID",
            "PLAYER_NAME",
            "GP",
            "W",
            "L",
            "W_PCT",
            "MIN",
            "E_OFF_RATING",
            "E_DEF_RATING",
            "E_NET_RATING",
            "E_AST_RATIO",
            "E_OREB_PCT",
            "E_DREB_PCT",
            "E_REB_PCT",
            "E_TOV_PCT",
            "E_USG_PCT",
            "E_PACE",
            "GP_RANK",
            "W_RANK",
            "L_RANK",
            "W_PCT_RANK",
            "MIN_RANK",
            "E_OFF_RATING_RANK",
            "E_DEF_RATING_RANK",
            "E_NET_RATING_RANK",
            "E_AST_RATIO_RANK",
            "E_OREB_PCT_RANK",
            "E_DREB_PCT_RANK",
            "E_REB_PCT_RANK",
            "E_TOV_PCT_RANK",
            "E_USG_PCT_RANK",
            "E_PACE_RANK"
        ]
    },
    "endpoint": "PlayerEstimatedMetrics",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [],
    "parameter_patterns": {
        "LeagueID": null,
        "Season": null,
        "SeasonType": null
    },
    "parameters": [
        "LeagueID",
        "Season",
        "SeasonType"
    ],
    "required_parameters": [
        "LeagueID",
        "Season",
        "SeasonType"
    ],
    "status": "success"
}
```

Last validated 2020-08-16