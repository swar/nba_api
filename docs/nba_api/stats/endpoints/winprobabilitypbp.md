# WinProbabilityPBP
##### [nba_api/stats/endpoints/winprobabilitypbp.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/winprobabilitypbp.py)

##### Endpoint URL
>[https://stats.nba.com/stats/winprobabilitypbp](https://stats.nba.com/stats/winprobabilitypbp)

##### Valid URL
>[https://stats.nba.com/stats/winprobabilitypbp?GameID=0021700807&RunType=each+second](https://stats.nba.com/stats/winprobabilitypbp?GameID=0021700807&RunType=each+second)

## Parameters
| API Parameter Name                                                                                            | Python Parameter Variable | Pattern | Required | Nullable |
|---------------------------------------------------------------------------------------------------------------|---------------------------|:-------:|:--------:|:--------:|
| [_**GameID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameID)   | game_id                   |         |   `Y`    |          | 
| [_**RunType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#RunType) | run_type                  |         |   `Y`    |          | 

## Data Sets
#### GameInfo `game_info`
```text
['GAME_ID', 'GAME_DATE', 'HOME_TEAM_ID', 'HOME_TEAM_ABR', 'HOME_TEAM_PTS', 'VISITOR_TEAM_ID', 'VISITOR_TEAM_ABR', 'VISITOR_TEAM_PTS']
```

#### WinProbPBP `win_prob_p_bp`
```text
['GAME_ID', 'EVENT_NUM', 'HOME_PCT', 'VISITOR_PCT', 'HOME_PTS', 'VISITOR_PTS', 'HOME_SCORE_MARGIN', 'PERIOD', 'SECONDS_REMAINING', 'HOME_POSS_IND', 'HOME_G', 'DESCRIPTION', 'LOCATION', 'PCTIMESTRING', 'ISVISIBLE']
```


## JSON
```json
{
    "data_sets": {
        "GameInfo": [
            "GAME_ID",
            "GAME_DATE",
            "HOME_TEAM_ID",
            "HOME_TEAM_ABR",
            "HOME_TEAM_PTS",
            "VISITOR_TEAM_ID",
            "VISITOR_TEAM_ABR",
            "VISITOR_TEAM_PTS"
        ],
        "WinProbPBP": [
            "GAME_ID",
            "EVENT_NUM",
            "HOME_PCT",
            "VISITOR_PCT",
            "HOME_PTS",
            "VISITOR_PTS",
            "HOME_SCORE_MARGIN",
            "PERIOD",
            "SECONDS_REMAINING",
            "HOME_POSS_IND",
            "HOME_G",
            "DESCRIPTION",
            "LOCATION",
            "PCTIMESTRING",
            "ISVISIBLE"
        ]
    },
    "endpoint": "WinProbabilityPBP",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [],
    "parameter_patterns": {
        "GameID": null,
        "RunType": null
    },
    "parameters": [
        "GameID",
        "RunType"
    ],
    "required_parameters": [
        "GameID",
        "RunType"
    ],
    "status": "success"
}
```

Last validated 2020-08-16