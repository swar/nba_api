# players.py
>/src/nba_api/stats/static/players.py

This module looks up NBA and WNBA players from the data bundled in [`data.py`](../library/data.md), without sending any requests.

Name searches take a regular expression, match case-insensitively, and ignore accents in both the pattern and the name, so `"jokic"` matches `"Nikola Jokić"`. Use anchors for exact matches, for example `"^james$"`.

Each player is returned as a `dict`:

```python
{'id': 203999, 'full_name': 'Nikola Jokić', 'first_name': 'Nikola', 'last_name': 'Jokić', 'is_active': True}
```

## Public functions

### `find_players_by_full_name`(_`regex_pattern`_)

Returns a list of players where full names match the provided `regex pattern`. 

### `find_players_by_first_name`(_`regex_pattern`_)

Returns a list of players where first names match the provided `regex pattern`. 

### `find_players_by_last_name`(_`regex_pattern`_)

Returns a list of players where last names match the provided `regex pattern`.

### `find_player_by_id`(_`player_id`_)

Returns a player that matches the player id provided. Raises an `Exception` if more than one player matches, which would indicate a duplicate in the bundled data. Returns `None` if there is no match.

### `get_players`()

Returns a list of all players.

### `get_active_players`()

Returns a list of all active players.

### `get_inactive_players`()

Returns a list of all inactive players.

### `find_wnba_players_by_full_name`(_`regex_pattern`_)

Returns a list of WNBA players where full names match the provided `regex pattern`. 

### `find_wnba_players_by_first_name`(_`regex_pattern`_)

Returns a list of WNBA players where first names match the provided `regex pattern`. 

### `find_wnba_players_by_last_name`(_`regex_pattern`_)

Returns a list of WNBA players where last names match the provided `regex pattern`.

### `find_wnba_player_by_id`(_`player_id`_)

Returns a WNBA player that matches the player id provided. Raises an `Exception` if more than one player matches, which would indicate a duplicate in the bundled data. Returns `None` if there is no match.

### `get_wnba_players`()

Returns a list of all WNBA players.

### `get_wnba_active_players`()

Returns a list of all active WNBA players.

### `get_wnba_inactive_players`()

Returns a list of all inactive WNBA players.

## Internal helpers

These functions are prefixed with `_` and are not part of the public API.

### `_find_players`(_`regex_pattern`_, _`row_id`_, _`players=players`_)

This is a protected function used to help search regex patterns through the players list. The
`players` parameter defaults to NBA players, but `wnba_players` can be passed in.

### `_find_player_by_id`(_`player_id`_, _`players=players`_)

This is a protected function used to help search for players by ID. The `players` parameter defaults
to NBA players, but `wnba_players` can be passed in.

### `_get_players`(_`players=players`_)

This is a protected function used to get all players. The `players` parameter defaults
to NBA players, but `wnba_players` can be passed in.

### `_get_active_players`(_`players=players`_)

This is a protected function used to get active players. The `players` parameter defaults
to NBA players, but `wnba_players` can be passed in.

### `_get_inactive_players`(_`players=players`_)

This is a protected function used to get inactive players. The `players` parameter defaults
to NBA players, but `wnba_players` can be passed in.

### `_get_player_dict`(_`player_row`_)
```python
player = {
    'id': player_id,
    'full_name': full_name,
    'first_name': first_name,
    'last_name': last_name,
    'is_active': True or False
}
```
This is a protected function that will parse a player list row into a friendly `dictionary`.
