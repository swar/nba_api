# ScoreboardV3
##### [nba_api/stats/endpoints/scoreboardv3.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/scoreboardv3.py)

##### Endpoint URL
>[https://stats.nba.com/stats/scoreboardv3](https://stats.nba.com/stats/scoreboardv3)

## Parameters
API Parameter Name | Python Parameter Variable | Pattern | Required | Nullable
------------ | ------------ | :-----------: | :---: | :---:
[_**GameDate**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameDate) | game_date | | `Y` | 
[_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id | | `N` | 

## Data Sets
#### ScoreboardInfo `scoreboard_info`
```text
["gameDate", "leagueId", "leagueName"]
```

#### GameHeader `game_header`
```text
["gameId", "gameCode", "gameStatus", "gameStatusText", "period", "gameClock", "gameTimeUTC", "gameEt", "regulationPeriods", "seriesGameNumber", "gameLabel", "gameSubLabel", "seriesText", "ifNecessary", "seriesConference", "poRoundDesc", "gameSubtype", "isNeutral"]
```

#### LineScore `line_score`
```text
["gameId", "teamId", "teamCity", "teamName", "teamTricode", "teamSlug", "wins", "losses", "score", "seed", "inBonus", "timeoutsRemaining"]
```

#### GameLeaders `game_leaders`
```text
["gameId", "teamId", "leaderType", "personId", "name", "playerSlug", "jerseyNum", "position", "teamTricode", "points", "rebounds", "assists"]
```

#### TeamLeaders `team_leaders`
```text
["gameId", "teamId", "leaderType", "personId", "name", "playerSlug", "jerseyNum", "position", "teamTricode", "points", "rebounds", "assists", "seasonLeadersFlag"]
```

#### Broadcasters `broadcasters`
```text
["gameId", "broadcasterType", "broadcasterId", "broadcastDisplay", "broadcasterTeamId", "broadcasterDescription"]
```

_Generated from the endpoint source; parameter patterns have not been validated against the live API._
