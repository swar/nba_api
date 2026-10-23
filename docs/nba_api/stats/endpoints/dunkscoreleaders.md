# DunkScoreLeaders
##### [nba_api/stats/endpoints/dunkscoreleaders.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/dunkscoreleaders.py)

##### Endpoint URL
>[https://stats.nba.com/stats/dunkscoreleaders](https://stats.nba.com/stats/dunkscoreleaders)

## Parameters
API Parameter Name | Python Parameter Variable | Pattern | Required | Nullable
------------ | ------------ | :-----------: | :---: | :---:
[_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id_nullable | | `N` | `Y`
[_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season) | season | | `N` | 
[_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType) | season_type_all_star | | `N` | 
[_**PlayerID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerID) | player_id_nullable | | `N` | `Y`
[_**TeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TeamID) | team_id_nullable | | `N` | `Y`
[_**GameID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameID) | game_id_nullable | | `N` | `Y`

## Data Sets
#### DunkScoreLeaders `dunks`
```text
["gameId", "gameDate", "matchup", "period", "gameClockTime", "eventNum", "playerId", "playerName", "firstName", "lastName", "teamId", "teamName", "teamCity", "teamAbbreviation", "dunkScore", "jumpSubscore", "powerSubscore", "styleSubscore", "defensiveContestSubscore", "maxBallHeight", "ballSpeedThroughRim", "playerVertical", "hangTime", "takeoffDistance", "reverseDunk", "dunk360", "throughTheLegs", "alleyOop", "tipIn", "selfOop", "playerRotation", "playerLateralSpeed", "ballDistanceTraveled", "ballReachBack", "totalBallAcceleration", "dunkingHand", "jumpingFoot", "passLength", "catchingHand", "catchDistance", "lateralCatchDistance", "passerId", "passerName", "passerFirstName", "passerLastName", "passReleasePoint", "shooterId", "shooterName", "shooterFirstName", "shooterLastName", "shotReleasePoint", "shotLength", "defensiveContestLevel", "possibleAttemptedCharge", "videoAvailable"]
```

_Generated from the endpoint source; parameter patterns have not been validated against the live API._
