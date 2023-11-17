# BoxScorePlayerTrackV3
##### [nba_apiv3/stats/endpoints/boxscoreplayertrackv3.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/boxscoreplayertrackv3.py)

##### Endpoint URL
>[https://stats.nba.com/stats/boxscoreplayertrackv3](https://stats.nba.com/stats/boxscoreplayertrackv3)

##### Valid URL
>[https://stats.nba.com/stats/boxscoreplayertrackv3?GameID=0021700807](https://stats.nba.com/stats/boxscoreplayertrackv3?GameID=0021700807)

## Parameters
| API Parameter Name                                                                                                  | Python Parameter Variable |  Pattern   | Required | Nullable |
|---------------------------------------------------------------------------------------------------------------------|---------------------------|:----------:|:--------:|:--------:|
| [_**GameID**_](https://github.com/shufinskiy/nba_apiv3/blob/master/docs/nba_api/stats/library/parameters.md#GameID) | game_id                   | `^\d{10}$` |   `Y`    |          | 

## Data Sets
#### PlayerStats `player_stats`
```text
['gameId', 'teamId', 'teamCity', 'teamName', 'teamTricode', 'teamSlug', 'personId', 'firstName', 'familyName', 'nameI', 'playerSlug', 'position', 'comment', 'jerseyNum', 'minutes', 'speed', 'distance', 'reboundChancesOffensive', 'reboundChancesDefensive', 'reboundChancesTotal', 'touches', 'secondaryAssists', 'freeThrowAssists', 'passes', 'assists', 'contestedFieldGoalsMade', 'contestedFieldGoalsAttempted', 'contestedFieldGoalPercentage', 'uncontestedFieldGoalsMade', 'uncontestedFieldGoalsAttempted', 'uncontestedFieldGoalsPercentage', 'fieldGoalPercentage', 'defendedAtRimFieldGoalsMade', 'defendedAtRimFieldGoalsAttempted', 'defendedAtRimFieldGoalPercentage']
```

#### TeamStats `team_stats`
```text
['gameId', 'teamId', 'teamCity', 'teamName', 'teamTricode', 'teamSlug', 'minutes', 'distance', 'reboundChancesOffensive', 'reboundChancesDefensive', 'reboundChancesTotal', 'touches', 'secondaryAssists', 'freeThrowAssists', 'passes', 'assists', 'contestedFieldGoalsMade', 'contestedFieldGoalsAttempted', 'contestedFieldGoalPercentage', 'uncontestedFieldGoalsMade', 'uncontestedFieldGoalsAttempted', 'uncontestedFieldGoalsPercentage', 'fieldGoalPercentage', 'defendedAtRimFieldGoalsMade', 'defendedAtRimFieldGoalsAttempted', 'defendedAtRimFieldGoalPercentage']
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
            "speed",
            "distance",
            "reboundChancesOffensive",
            "reboundChancesDefensive",
            "reboundChancesTotal",
            "touches",
            "secondaryAssists",
            "freeThrowAssists",
            "passes",
            "assists",
            "contestedFieldGoalsMade",
            "contestedFieldGoalsAttempted",
            "contestedFieldGoalPercentage",
            "uncontestedFieldGoalsMade",
            "uncontestedFieldGoalsAttempted",
            "uncontestedFieldGoalsPercentage",
            "fieldGoalPercentage",
            "defendedAtRimFieldGoalsMade",
            "defendedAtRimFieldGoalsAttempted",
            "defendedAtRimFieldGoalPercentage"
        ],
        "TeamStats": [
            "gameId",
            "teamId",
            "teamCity",
            "teamName",
            "teamTricode",
            "teamSlug",
            "minutes",
            "distance",
            "reboundChancesOffensive",
            "reboundChancesDefensive",
            "reboundChancesTotal",
            "touches",
            "secondaryAssists",
            "freeThrowAssists",
            "passes",
            "assists",
            "contestedFieldGoalsMade",
            "contestedFieldGoalsAttempted",
            "contestedFieldGoalPercentage",
            "uncontestedFieldGoalsMade",
            "uncontestedFieldGoalsAttempted",
            "uncontestedFieldGoalsPercentage",
            "fieldGoalPercentage",
            "defendedAtRimFieldGoalsMade",
            "defendedAtRimFieldGoalsAttempted",
            "defendedAtRimFieldGoalPercentage"
        ]
    },
    "endpoint": "BoxScorePlayerTrackV3",
    "last_validated_date": "2023-09-14",
    "nullable_parameters": [],
    "parameter_patterns": {
        "GameID": "^\\d{10}$"
    },
    "parameters": [
        "GameID"
    ],
    "required_parameters": [
        "GameID"
    ],
    "status": "success"
}
```

Last validated 2023-09-14