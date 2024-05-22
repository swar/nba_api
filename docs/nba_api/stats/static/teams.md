# teams.py
>/nba_api/stats/static/teams.py

The purpose of this module is to access team information without having to submit requests.

## `_find_teams`(_`regex_pattern`_, _`row_id`_, _`teams=teams`_)

This is a protected function used to help search regex patterns through the teams list. The `teams` parameter defaults to NBA teams, but `wnba_teams` can be passed in.

## `_find_team_name_by_id`(_`team_id`_, _`teams=teams`_)

This is a protected function used to find a team by ID. The `teams` parameter defaults to NBA teams, but `wnba_teams` can be passed in.

## `_find_team_by_abbreviation`(_`abbreviation`_, _`teams=teams`_)

This is a protected function used to find a team by abbreviation. The `teams` parameter defaults to NBA teams, but `wnba_teams` can be passed in.

## `_find_teams_by_championship_year`(_`year`_, _`teams=teams`_)

This is a protected function used to find a team by championship year. The `teams` parameter defaults to NBA teams, but `wnba_teams` can be passed in.

## `_find_teams_by_year_founded`(_`year`_, _`teams=teams`_)

This is a protected function used to find a team by year founded. The `teams` parameter defaults to NBA teams, but `wnba_teams` can be passed in.

## `_get_teams`(_`teams=teams`_)

This is a protected function used to get all teams. The `teams` parameter defaults to NBA teams, but `wnba_teams` can be passed in.

## `_get_team_dict`(_`team_row`_)
```python
team = {
    'id': team_id,
    'full_name': full_name,
    'abbreviation': abbreviation,
    'nickname': nickname,
    'city': city,
    'state': state,
    'year_founded': year_founded,
}
```
This a protected function that will parse a team list row into a friendly `dictionary`.

## `find_teams_by_full_name`(_`regex_pattern`_)

Returns a list of teams where full team name matches the provided `regex pattern`. 

## `find_teams_by_state`(_`regex_pattern`_)

Returns a list of teams where the state matches the provided `regex pattern`. 

## `find_teams_by_city`(_`regex_pattern`_)

Returns a list of teams where the city matches the provided `regex pattern`.

## `find_teams_by_nickname`(_`regex_pattern`_)

Returns a list of teams where the nickname matches the provided `regex pattern`.

## `find_teams_by_year_founded`(_`year`_)

Returns a list of teams that matches the year provided.

## `find_teams_by_championship_year`(_`year`_)

Returns a list of teams that matches the championship year provided.

## `find_team_by_abbreviation`(_`abbreviation`_)

Returns a team that matches the abbreviation provided. Function will fail on any multiple matches. This means our team list has a duplicate or there's an error in the function. No matches will return a `null` value.

## `find_team_name_by_id`(_`team_id`_)

Returns a team that matches the team id provided. Function will fail on any multiple matches. This means our team list has a duplicate or there's an error in the function. No matches will return a `null` value.

## `get_teams`(_`regex_pattern`_, _`row_id`_)

Returns a list of all teams.

## `find_wnba_teams_by_full_name`(_`regex_pattern`_)

Returns a list of WNBA teams where full team name matches the provided `regex pattern`. 
## `find_wnba_teams_by_state`(_`regex_pattern`_)

Returns a list of WNBA teams where the state matches the provided `regex pattern`. 

## `find_wnba_teams_by_city`(_`regex_pattern`_)

Returns a list of WNBA teams where the city matches the provided `regex pattern`.

## `find_wnba_teams_by_nickname`(_`regex_pattern`_)

Returns a list of WNBA teams where the nickname matches the provided `regex pattern`.

## `find_wnba_teams_by_year_founded`(_`year`_)

Returns a list of WNBA teams that matches the year provided.

## `find_wnba_teams_by_championship_year`(_`year`_)

Returns a list of WNBA teams that matches the championship year provided.

## `find_wnba_team_by_abbreviation`(_`abbreviation`_)

Returns a WNBA team that matches the abbreviation provided. Function will fail on any multiple matches. This means our team list has a duplicate or there's an error in the function. No matches will return a `null` value.

## `find_wnba_team_name_by_id`(_`team_id`_)

Returns a WNBA team that matches the team id provided. Function will fail on any multiple matches. This means our team list has a duplicate or there's an error in the function. No matches will return a `null` value.

## `get_wnba_teams`()

Returns a list of all WNBA teams.
