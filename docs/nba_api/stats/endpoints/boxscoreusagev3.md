# BoxScoreUsageV3
##### [nba_apiv3/stats/endpoints/boxscoreusagev3.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/boxscoreusagev3.py)

##### Endpoint URL
>[https://stats.nba.com/stats/boxscoreusagev3](https://stats.nba.com/stats/boxscoreusagev3)

##### Valid URL
>[https://stats.nba.com/stats/boxscoreusagev3?EndPeriod=1&EndRange=0&GameID=0021700807&RangeType=0&StartPeriod=1&StartRange=0](https://stats.nba.com/stats/boxscoreusagev3?EndPeriod=1&EndRange=0&GameID=0021700807&RangeType=0&StartPeriod=1&StartRange=0)

## Parameters
| API Parameter Name                                                                                                            | Python Parameter Variable |  Pattern   | Required | Nullable |
|-------------------------------------------------------------------------------------------------------------------------------|---------------------------|:----------:|:--------:|:--------:|
| [_**EndPeriod**_](https://github.com/shufinskiy/nba_apiv3/blob/master/docs/nba_api/stats/library/parameters.md#EndPeriod)     | end_period                |            |   `Y`    |          | 
| [_**EndRange**_](https://github.com/shufinskiy/nba_apiv3/blob/master/docs/nba_api/stats/library/parameters.md#EndRange)       | end_range                 |            |   `Y`    |          | 
| [_**GameID**_](https://github.com/shufinskiy/nba_apiv3/blob/master/docs/nba_api/stats/library/parameters.md#GameID)           | game_id                   | `^\d{10}$` |   `Y`    |          | 
| [_**RangeType**_](https://github.com/shufinskiy/nba_apiv3/blob/master/docs/nba_api/stats/library/parameters.md#RangeType)     | range_type                |            |   `Y`    |          | 
| [_**StartPeriod**_](https://github.com/shufinskiy/nba_apiv3/blob/master/docs/nba_api/stats/library/parameters.md#StartPeriod) | start_period              |            |   `Y`    |          | 
| [_**StartRange**_](https://github.com/shufinskiy/nba_apiv3/blob/master/docs/nba_api/stats/library/parameters.md#StartRange)   | start_range               |            |   `Y`    |          | 

## Data Sets
#### PlayerStats `player_stats`
```text
['gameId', 'teamId', 'teamCity', 'teamName', 'teamTricode', 'teamSlug', 'personId', 'firstName', 'familyName', 'nameI', 'playerSlug', 'position', 'comment', 'jerseyNum', 'minutes', 'usagePercentage', 'percentageFieldGoalsMade', 'percentageFieldGoalsAttempted', 'percentageThreePointersMade', 'percentageThreePointersAttempted', 'percentageFreeThrowsMade', 'percentageFreeThrowsAttempted', 'percentageReboundsOffensive', 'percentageReboundsDefensive', 'percentageReboundsTotal', 'percentageAssists', 'percentageTurnovers', 'percentageSteals', 'percentageBlocks', 'percentageBlocksAllowed', 'percentagePersonalFouls', 'percentagePersonalFoulsDrawn', 'percentagePoints']
```

#### TeamStats `team_stats`
```text
['gameId', 'teamId', 'teamCity', 'teamName', 'teamTricode', 'teamSlug', 'minutes', 'usagePercentage', 'percentageFieldGoalsMade', 'percentageFieldGoalsAttempted', 'percentageThreePointersMade', 'percentageThreePointersAttempted', 'percentageFreeThrowsMade', 'percentageFreeThrowsAttempted', 'percentageReboundsOffensive', 'percentageReboundsDefensive', 'percentageReboundsTotal', 'percentageAssists', 'percentageTurnovers', 'percentageSteals', 'percentageBlocks', 'percentageBlocksAllowed', 'percentagePersonalFouls', 'percentagePersonalFoulsDrawn', 'percentagePoints']
```


## JSON
```json
{
    "data_sets": {
        "PlayerStats": [
            "gameId", 
            "teamId",
            "teamCity",
            "teamName",
            "teamTricode",
            "teamSlug",
            "personId",
            "firstName",
            "familyName",
            "nameI",
            "playerSlug",
            "position",
            "comment",
            "jerseyNum",
            "minutes",
            "usagePercentage",
            "percentageFieldGoalsMade",
            "percentageFieldGoalsAttempted",
            "percentageThreePointersMade",
            "percentageThreePointersAttempted",
            "percentageFreeThrowsMade",
            "percentageFreeThrowsAttempted",
            "percentageReboundsOffensive",
            "percentageReboundsDefensive",
            "percentageReboundsTotal",
            "percentageAssists",
            "percentageTurnovers",
            "percentageSteals",
            "percentageBlocks",
            "percentageBlocksAllowed",
            "percentagePersonalFouls",
            "percentagePersonalFoulsDrawn",
            "percentagePoints"
        ],
        "TeamStats": [
            "gameId", 
            "teamId", 
            "teamCity",
            "teamName",
            "teamTricode",
            "teamSlug",
            "minutes",
            "usagePercentage", 
            "percentageFieldGoalsMade", 
            "percentageFieldGoalsAttempted", 
            "percentageThreePointersMade", 
            "percentageThreePointersAttempted", 
            "percentageFreeThrowsMade", 
            "percentageFreeThrowsAttempted", 
            "percentageReboundsOffensive", 
            "percentageReboundsDefensive", 
            "percentageReboundsTotal", 
            "percentageAssists", 
            "percentageTurnovers", 
            "percentageSteals", 
            "percentageBlocks", 
            "percentageBlocksAllowed",
            "percentagePersonalFouls",
            "percentagePersonalFoulsDrawn",
            "percentagePoints"
        ]
    },
    "endpoint": "BoxScoreUsageV3",
    "last_validated_date": "2023-09-14",
    "nullable_parameters": [],
    "parameter_patterns": {
        "EndPeriod": null,
        "EndRange": null,
        "GameID": "^\\d{10}$",
        "RangeType": null,
        "StartPeriod": null,
        "StartRange": null
    },
    "parameters": [
        "EndPeriod",
        "EndRange",
        "GameID",
        "RangeType",
        "StartPeriod",
        "StartRange"
    ],
    "required_parameters": [
        "EndPeriod",
        "EndRange",
        "GameID",
        "RangeType",
        "StartPeriod",
        "StartRange"
    ],
    "status": "success"
}
```

Last validated 2023-09-14