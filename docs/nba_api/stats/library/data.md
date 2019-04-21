# data.py
>/nba_api/stats/library/data.py

This module contains static data to be used with that `nba_api/stats/static` directory.

### list `players`

```text
player_id, last_name, first_name, full_name
```

This is a list of lists of player information.

`player_index_id` = `0`

`player_index_last_name` = `1`

`player_index_first_name` = `2`

`player_index_full_name` = `3`

`player_index_is_active` = `4`



### list `teams`

```text
team_id = abbreviation, nickname, year_founded, city, full_name, state
```

This is a list of lists of team information.

`team_index_id` = `0`

`team_index_abbreviation` = `1`

`team_index_nickname` = `2`

`team_index_year_founded` = `3`

`team_index_city` = `4`

`team_index_full_name` = `5`

`team_index_state` = `6`
