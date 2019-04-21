# players.py
>/nba_api/stats/static/players.py

The purpose of this module is to access player information without having to submit requests.

## `_find_players`(_`regex_pattern`_, _`row_id`_)

This is a protected function used to help search regex patterns through the players list.

## `_get_player_dict`(_`player_row`_)
```python
player = {
    'id': player_id,
    'full_name': full_name,
    'first_name': first_name,
    'last_name': last_name,
    'is_active': True or False
}
```
This a protected function that will parse a player list row into a friendly `dictionary`.

## `find_players_by_full_name`(_`regex_pattern`_)

Returns a list of players where full names match the provided `regex pattern`. 

## `find_players_by_first_name`(_`regex_pattern`_)

Returns a list of players where first names match the provided `regex pattern`. 

## `find_players_by_last_name`(_`regex_pattern`_)

Returns a list of players where last names match the provided `regex pattern`.

## `find_player_by_id`(_`player_id`_)

Returns a player that matches the player id provided. Function will fail on any multiple matches. This means our player list has a duplicate or there's an error in the function. No matches will return a `null` value.

## `get_players`()

Returns a list of all players.

## `get_active_players`()

Returns a list of all active players.

## `get_inactive_players`()

Returns a list of all inactive players.
