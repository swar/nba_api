# BoxScoreSummaryV3
##### [nba_api/stats/endpoints/boxscoresummaryv3.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/boxscoresummaryv3.py)

##### Endpoint URL
>[https://stats.nba.com/stats/boxscoresummaryv3](https://stats.nba.com/stats/boxscoresummaryv3)

##### Valid URL
>[https://stats.nba.com/stats/boxscoresummaryv3?GameID=0021700807](https://stats.nba.com/stats/boxscoresummaryv3?GameID=0021700807)

## Parameters
API Parameter Name | Python Parameter Variable | Pattern | Required | Nullable
------------ | ------------ | :-----------: | :---: | :---:
[_**GameID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameID) | game_id |  |  |  | 

## Data Sets
#### GameSummary `game_summary`
```text
['gameId', 'gameCode', 'gameStatus', 'gameStatusText', 'period', 'gameClock', 'gameTimeUTC', 'gameEt', 'awayTeamId', 'homeTeamId', 'duration', 'attendance', 'sellout']
```

#### GameInfo `game_info`
```text
['gameId', 'gameDate', 'attendance', 'gameDuration']
```

#### ArenaInfo `arena_info`
```text
['gameId', 'arenaId', 'arenaName', 'arenaCity', 'arenaState', 'arenaCountry', 'arenaTimezone']
```

#### Officials `officials`
```text
['gameId', 'personId', 'name', 'nameI', 'firstName', 'familyName', 'jerseyNum']
```

#### LineScore `line_score`
```text
['gameId', 'teamId', 'teamCity', 'teamName', 'teamTricode', 'teamSlug', 'teamWins', 'teamLosses', 'period1Score', 'period2Score', 'period3Score', 'period4Score', 'score']
```

#### InactivePlayers `inactive_players`
```text
['gameId', 'teamId', 'personId', 'firstName', 'familyName', 'jerseyNum']
```

#### LastFiveMeetings `last_five_meetings`
```text
['recencyOrder', 'gameId', 'gameTimeUTC', 'gameEt', 'gameStatus', 'gameStatusText', 'awayTeamId', 'awayTeamCity', 'awayTeamName', 'awayTeamTricode', 'awayTeamScore', 'awayTeamWins', 'awayTeamLosses', 'homeTeamId', 'homeTeamCity', 'homeTeamName', 'homeTeamTricode', 'homeTeamScore', 'homeTeamWins', 'homeTeamLosses']
```

#### OtherStats `other_stats`
```text
['gameId', 'teamId', 'teamCity', 'teamName', 'teamTricode', 'points', 'reboundsTotal', 'assists', 'steals', 'blocks', 'turnovers', 'fieldGoalsPercentage', 'threePointersPercentage', 'freeThrowsPercentage', 'pointsInThePaint', 'pointsSecondChance', 'pointsFastBreak', 'biggestLead', 'leadChanges', 'timesTied', 'biggestScoringRun', 'turnoversTeam', 'turnoversTotal', 'reboundsTeam', 'pointsFromTurnovers', 'benchPoints']
```

#### AvailableVideo `available_video`
```text
['gameId', 'videoAvailableFlag', 'ptAvailable', 'ptXYZAvailable', 'whStatus', 'hustleStatus', 'historicalStatus']
```


## JSON
```json
{
    "data_sets": {
        "ArenaInfo": [
            "gameId",
            "arenaId",
            "arenaName",
            "arenaCity",
            "arenaState",
            "arenaCountry",
            "arenaTimezone"
        ],
        "AvailableVideo": [
            "gameId",
            "videoAvailableFlag",
            "ptAvailable",
            "ptXYZAvailable",
            "whStatus",
            "hustleStatus",
            "historicalStatus"
        ],
        "GameInfo": [
            "gameId",
            "gameDate",
            "attendance",
            "gameDuration"
        ],
        "GameSummary": [
            "gameId",
            "gameCode",
            "gameStatus",
            "gameStatusText",
            "period",
            "gameClock",
            "gameTimeUTC",
            "gameEt",
            "awayTeamId",
            "homeTeamId",
            "duration",
            "attendance",
            "sellout"
        ],
        "InactivePlayers": [
            "gameId",
            "teamId",
            "personId",
            "firstName",
            "familyName",
            "jerseyNum"
        ],
        "LastFiveMeetings": [
            "recencyOrder",
            "gameId",
            "gameTimeUTC",
            "gameEt",
            "gameStatus",
            "gameStatusText",
            "awayTeamId",
            "awayTeamCity",
            "awayTeamName",
            "awayTeamTricode",
            "awayTeamScore",
            "awayTeamWins",
            "awayTeamLosses",
            "homeTeamId",
            "homeTeamCity",
            "homeTeamName",
            "homeTeamTricode",
            "homeTeamScore",
            "homeTeamWins",
            "homeTeamLosses"
        ],
        "LineScore": [
            "gameId",
            "teamId",
            "teamCity",
            "teamName",
            "teamTricode",
            "teamSlug",
            "teamWins",
            "teamLosses",
            "period1Score",
            "period2Score",
            "period3Score",
            "period4Score",
            "score"
        ],
        "Officials": [
            "gameId",
            "personId",
            "name",
            "nameI",
            "firstName",
            "familyName",
            "jerseyNum"
        ],
        "OtherStats": [
            "gameId",
            "teamId",
            "teamCity",
            "teamName",
            "teamTricode",
            "points",
            "reboundsTotal",
            "assists",
            "steals",
            "blocks",
            "turnovers",
            "fieldGoalsPercentage",
            "threePointersPercentage",
            "freeThrowsPercentage",
            "pointsInThePaint",
            "pointsSecondChance",
            "pointsFastBreak",
            "biggestLead",
            "leadChanges",
            "timesTied",
            "biggestScoringRun",
            "turnoversTeam",
            "turnoversTotal",
            "reboundsTeam",
            "pointsFromTurnovers",
            "benchPoints"
        ]
    },
    "nullable_parameters": [],
    "parameter_patterns": {
        "GameID": null
    },
    "parameters": [
        "GameID"
    ],
    "required_parameters": [],
    "status": "success"
}
```

Last validated 2025-11-03