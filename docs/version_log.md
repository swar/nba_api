# `v1.1.11`
#### `2021-11-08`
`Live NBA Stats`
- Adding missing live functionality [#231](https://github.com/swar/nba_api/pull/231)

# `v1.1.10`
#### `2021-10-31`
`stats.nba.com`
- Added handling of multiple level column names [#212](https://github.com/swar/nba_api/pull/212)
- Finding team by championship years [#219](https://github.com/swar/nba_api/pull/219)
- Updated Static Player and Team Data [#225](https://github.com/swar/nba_api/pull/225)
- Added `previous_season` attribute for Season Parameter [#226](https://github.com/swar/nba_api/pull/226)

`Live NBA Stats`
- Randy added some Live NBA endpoints [#184](https://github.com/swar/nba_api/pull/184/files)

Endpoints were unable to be tested due to outdated analyzer.

# `v1.1.9`
#### `2020-08-18`
`stats.nba.com`
* Fixed bug where LeagueDashOppPtShot was missing in tests and __init__.py [#152](https://github.com/swar/nba_api/pull/152)
* Adding endpoints [#102](https://github.com/swar/nba_api/issues/102)
  * AllTimeLeadersGrids
  * BoxScoreSimilarityScore
  * CumeStatsPlayer
  * CumeStatsPlayerGames
  * CumeStatsTeam
  * CumeStatsTeamGames
  * DraftBoard
  * GameRotation
  * GLAlumBoxScoreSimilarityScore
  * LeagueHustleStatsPlayer [#144](https://github.com/swar/nba_api/issues/144)
  * LeagueHustleStatsPlayerLeaders [#144](https://github.com/swar/nba_api/issues/144)
  * LeagueHustleStatsTeam [#144](https://github.com/swar/nba_api/issues/144), [#147](https://github.com/swar/nba_api/issues/147)
  * LeagueHustleStatsTeamLeaders [#144](https://github.com/swar/nba_api/issues/144)
  * LeagueLineupViz
  * LeagueStandingsV3
  * MatchupsRollup
  * PlayerCareerByCollege
  * PlayerCareerByCollegeRollup
  * PlayerEstimatedMetrics
  * ShotChartLeagueWide
  * TeamEstimatedMetrics

`Tools`
* Various Changes for New Endpoints including Threading


# `v1.1.8`
#### `2020-01-27`
`stats.nba.com`
* Updating Headers for New Requirements [#126](https://github.com/swar/nba_api/pull/126)
* Updates to Static Players Data 
* Added Proxy List Support
* Adding endpoint [#102](https://github.com/swar/nba_api/issues/102)
  * TeamGameLogs

`Tools`
* Added Parameter Overrides for Bad Parameter Analysis [#99](https://github.com/swar/nba_api/issues/99)


# `v1.1.7`
#### `2020-01-27`
##### SCRAPPED


# `v1.1.6`
#### `2020-01-27`
##### SCRAPPED

# `v1.1.5`
#### `2019-11-09`
`stats.nba.com`
* Bug fix to PlayByPlay Regex [#89](https://github.com/swar/nba_api/pull/89)
* Updates to Static Players Data with 2019 Draft [#91](https://github.com/swar/nba_api/issues/91)
* Updating Headers to Include Referer [#94](https://github.com/swar/nba_api/issues/94)
* Adding endpoint [#79](https://github.com/swar/nba_api/issues/79)
  * PlayerGameLogs


# `v1.1.4`
#### `2019-04-28`
`stats.nba.com`
* Updates to PlayByPlay Regex [#70](https://github.com/swar/nba_api/pull/70)

`Scripts`
* Added Script for Static Player Updater

`Tests`
* Updates to PlayByPlay Tests with Yesterday's Games [#70](https://github.com/swar/nba_api/pull/70)

`Tools`
* Added Static Player Data Updater Tool [#67](https://github.com/swar/nba_api/pull/67) 


# `v1.1.3`
#### `2019-04-21`
`stats.nba.com`
* Added PlayByPlay Regex for Ejections [#64](https://github.com/swar/nba_api/pull/64)
* Adding Active Status to Static Player List [#66](https://github.com/swar/nba_api/pull/66)
* Removing `tools` from the PyPi upload


# `v1.1.2`
#### `2019-04-15`
`stats.nba.com`
* Updating PlayByPlay Regex. [#59](https://github.com/swar/nba_api/pull/59)
* Adding endpoint [#60](https://github.com/swar/nba_api/pull/60)
  * SynergyPlayTypes


# `v1.1.1`
#### `2019-04-07`
`stats.nba.com`
* Adding proxy, header, and timeout support for every request. [#49](https://github.com/swar/nba_api/issues/49)
  * [Example](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/examples.md)
* Fixing auto-complete tabs for IDEs on endpoints. [#45](https://github.com/swar/nba_api/pull/45)
* Laid out foundation for future url generation without requesting.
* Adding endpoints [#54](https://github.com/swar/nba_api/issues/54)
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
