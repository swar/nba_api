# `v1.1.0`
#### `2019-04-07`
`stats.nba.com`
* Adding proxy, header, and timeout support for every request. [#49] [Example](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/examples.md)
* Fixing auto-complete tabs for IDEs on endpoints. [#45]
* Laid out foundation for future url generation without requesting.
* Adding endpoints [#54]
  * AssistLeaders
  * AssistTracker
  * BoxScoreDefensive
  * BoxScoreMatchups
  * FantasyWidget
  * FranchiseLeaders
  * FranchisePlayers
  * LeaguePlayerOnDetails
  * LeagueSeasonMatchups
  * TeamAndPlayersVsPlayers
  * WinProbabilityPBP

`Tools`
* Updating analysis for site updates

# `v1.0.7`
#### 2018-12-11
`stats.nba.com`
* PlayersVsPlayers no longer valid.
* Adding TwoWay to parameters

`Documentation`
* Updating Endpoint docs with Python variables for [#19](https://github.com/swar/nba_api/issues/19).

`Endpoint Documentation Generator`
* Updating Endpoint docs with Python variables for [#19](https://github.com/swar/nba_api/issues/19).

# `v1.0.6`
#### 2018-10-11
* Accidentally distributed with DEBUG Mode enabled in `v1.0.5`.

# `v1.0.5`
#### 2018-10-10
* Adding `last_validated_date` to analysis json.

`stats.nba.com`
* Adding _LeagueDashPtStats_ endpoint
* Adding PtMeasureType to parameters
* Updating `missing_parameter_regex` for `Season Year` bug.
* Switching default values in `parameters.py`
  * `LastNGames` from `10` -> `0`
  * `Period` from `1` -> `0`
  * `StartPeriod` from `1` -> `0`
  * `EndPeriod` from `1` -> `0`

# `v1.0.4`
#### 2018-09-25
* Updating description on PyPi 

# `v1.0.3`
#### 2018-09-25
`stats.nba.com`
* Fixed a bug in `find_team_name_by_id()` in static/teams. 

# `v1.0.2`
#### 2018-09-17
`stats.nba.com`
* Added `__all__` to the following file: `nba_api/nba_api/stats/static/__init__.py`

# `v1.0.1`
#### 2018-09-17
`stats.nba.com`
* Added `__init__.py` to the following directory: `nba_api/nba_api/stats/static`

# `v1.0.0`
#### 2018-09-16
* The initial release of `nba_api`.
