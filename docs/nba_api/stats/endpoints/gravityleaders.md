# GravityLeaders
##### [nba_api/stats/endpoints/gravityleaders.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/gravityleaders.py)

##### Endpoint URL
>[https://stats.nba.com/stats/gravityleaders](https://stats.nba.com/stats/gravityleaders)

## Parameters
API Parameter Name | Python Parameter Variable | Pattern | Required | Nullable
------------ | ------------ | :-----------: | :---: | :---:
[_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id | | `N` | 
[_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season) | season | | `N` | 
[_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType) | season_type_all_star | | `N` | 

## Data Sets
#### leaders `leaders`
```text
["PLAYERID", "FIRSTNAME", "LASTNAME", "TEAMID", "TEAMABBREVIATION", "TEAMNAME", "TEAMCITY", "FRAMES", "GRAVITYSCORE", "AVGGRAVITYSCORE", "ONBALLPERIMETERFRAMES", "ONBALLPERIMETERGRAVITYSCORE", "AVGONBALLPERIMETERGRAVITYSCORE", "OFFBALLPERIMETERFRAMES", "OFFBALLPERIMETERGRAVITYSCORE", "AVGOFFBALLPERIMETERGRAVITYSCORE", "ONBALLINTERIORFRAMES", "ONBALLINTERIORGRAVITYSCORE", "AVGONBALLINTERIORGRAVITYSCORE", "OFFBALLINTERIORFRAMES", "OFFBALLINTERIORGRAVITYSCORE", "AVGOFFBALLINTERIORGRAVITYSCORE", "GAMESPLAYED", "MINUTES", "PTS", "REB", "AST"]
```

_Generated from the endpoint source; parameter patterns have not been validated against the live API._
