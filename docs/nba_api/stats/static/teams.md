# teams.py
>/src/nba_api/stats/static/teams.py

This module looks up NBA and WNBA teams from the data bundled in [`data.py`](../library/data.md), without sending any requests.

Text searches take a regular expression and match case-insensitively. Use anchors for exact matches, for example `"^cleveland"`. Year arguments must be `int`s.

Each team is returned as a `dict`:

```python
{
    'id': 1610612739,
    'full_name': 'Cleveland Cavaliers',
    'abbreviation': 'CLE',
    'nickname': 'Cavaliers',
    'city': 'Cleveland',
    'state': 'Ohio',
    'year_founded': 1970,
}
```

## Public functions

### `get_teams`( )

Returns a list of all NBA teams.

### `find_teams_by_full_name`(_`regex_pattern`_)

Returns a list of teams whose full name matches `regex_pattern`.

### `find_teams_by_state`(_`regex_pattern`_)

Returns a list of teams whose state matches `regex_pattern`.

### `find_teams_by_city`(_`regex_pattern`_)

Returns a list of teams whose city matches `regex_pattern`.

### `find_teams_by_nickname`(_`regex_pattern`_)

Returns a list of teams whose nickname matches `regex_pattern`.

### `find_teams_by_year_founded`(_`year`_)

Returns a list of teams founded in `year`.

### `find_team_by_abbreviation`(_`abbreviation`_)

Returns the team with this abbreviation (case-insensitive), or `None` if there is no match.

### `find_team_name_by_id`(_`team_id`_)

Returns the team **dict** with this ID, despite the function's name, or `None` if there is no match.

### `find_teams_by_championship_year`(_`year`_)

Returns the **full name** (a `str`, not a team dict) of the team that won the championship in `year`, for example `"Cleveland Cavaliers"` for `2016`.

> [!WARNING]
> If no team won a championship in `year` (a future season, for example), this function raises `UnboundLocalError` instead of returning `None`.

### WNBA equivalents

Each function above has a WNBA counterpart that behaves the same way over the WNBA team list:

`get_wnba_teams`, `find_wnba_teams_by_full_name`, `find_wnba_teams_by_state`, `find_wnba_teams_by_city`, `find_wnba_teams_by_nickname`, `find_wnba_teams_by_year_founded`, `find_wnba_team_by_abbreviation`, `find_wnba_team_name_by_id`, `find_wnba_teams_by_championship_year`.

## Internal helpers

These functions are prefixed with `_` and are not part of the public API. Each takes an optional `teams` argument that defaults to the NBA list; the WNBA functions pass `wnba_teams`.

- `_find_teams`(_`regex_pattern`_, _`row_id`_, _`teams=teams`_) — regex search on one column of the team rows.
- `_find_team_name_by_id`(_`team_id`_, _`teams=teams`_)
- `_find_team_by_abbreviation`(_`abbreviation`_, _`teams=teams`_)
- `_find_teams_by_championship_year`(_`year`_, _`teams=teams`_)
- `_find_teams_by_year_founded`(_`year`_, _`teams=teams`_)
- `_get_teams`(_`teams=teams`_)
- `_get_team_dict`(_`team_row`_) — converts a raw team row into the dict shown above.
