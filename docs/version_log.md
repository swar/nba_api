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
