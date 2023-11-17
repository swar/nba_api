# BoxScoreDefensiveV2
##### [nba_apiv3/stats/endpoints/boxscoredefensivev2.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/boxscoredefensivev2.py)

##### Endpoint URL
>[https://stats.nba.com/stats/boxscoredefensivev2](https://stats.nba.com/stats/boxscoredefensivev2)

##### Valid URL
>[https://stats.nba.com/stats/boxscoredefensivev2?GameID=0021700807](https://stats.nba.com/stats/boxscoredefensivev2?GameID=0021700807)

## Parameters
| API Parameter Name                                                                                                  | Python Parameter Variable |  Pattern   | Required | Nullable |
|---------------------------------------------------------------------------------------------------------------------|---------------------------|:----------:|:--------:|:--------:|
| [_**GameID**_](https://github.com/shufinskiy/nba_apiv3/blob/master/docs/nba_api/stats/library/parameters.md#GameID) | game_id                   | `^\d{10}$` |   `Y`    |          | 

## Data Sets
#### PlayerStats `player_stats`
```text
['gameId', 'teamId', 'teamCity', 'teamName', 'teamTricode', 'teamSlug', 'personId', 'firstName', 'familyName', 'nameI', 'playerSlug', 'position', 'comment', 'jerseyNum', 'matchupMinutes', 'partialPossessions', 'switchesOn', 'playerPoints', 'defensiveRebounds', 'matchupAssists', 'matchupTurnovers', 'steals', 'blocks', 'matchupFieldGoalsMade', 'matchupFieldGoalsAttempted', 'matchupFieldGoalPercentage', 'matchupThreePointersMade', 'matchupThreePointersAttempted', 'matchupThreePointerPercentage']
```

#### TeamStats `team_stats`
```text
['gameId', 'teamId', 'teamCity', 'teamName', 'teamTricode', 'teamSlug', 'minutes']
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
            "matchupMinutes", 
            "partialPossessions", 
            "switchesOn", 
            "playerPoints", 
            "defensiveRebounds", 
            "matchupAssists", 
            "matchupTurnovers", 
            "steals", 
            "blocks", 
            "matchupFieldGoalsMade", 
            "matchupFieldGoalsAttempted", 
            "matchupFieldGoalPercentage", 
            "matchupThreePointersMade", 
            "matchupThreePointersAttempted", 
            "matchupThreePointerPercentage"
        ],
        "TeamStats": [
            "gameId", 
            "teamId", 
            "teamCity", 
            "teamName", 
            "teamTricode", 
            "teamSlug", 
            "minutes"
        ]
    },
    "endpoint": "BoxScoreDefensiveV2",
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