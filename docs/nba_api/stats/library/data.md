# data.py
>/src/nba_api/stats/library/data.py

This module holds the player and team reference data used by [`stats/static`](../static/players.md). It is **generated** by `scripts/static_players_update/` (see [Scripts](../../../scripts.md)). Player rows come from the API, and team rows are copied from that script's `template.py`. Any hand edit here must also be made in the script or template, or the next refresh will overwrite it.

Each list holds one row (a `list`) per player or team. Use the index constants to read a column rather than hardcoding positions.

## Players

### `players`, `wnba_players`

```text
[player_id, last_name, first_name, full_name, is_active]
```

```python
[1628378, "Mitchell", "Donovan", "Donovan Mitchell", True]
```

| Constant | Value |
|---|---|
| `player_index_id` | `0` |
| `player_index_last_name` | `1` |
| `player_index_first_name` | `2` |
| `player_index_full_name` | `3` |
| `player_index_is_active` | `4` |

## Teams

### `teams`, `wnba_teams`

```text
[team_id, abbreviation, nickname, year_founded, city, full_name, state, championship_years]
```

```python
[1610612739, "CLE", "Cavaliers", 1970, "Cleveland", "Cleveland Cavaliers", "Ohio", [2016]]
```

| Constant | Value |
|---|---|
| `team_index_id` | `0` |
| `team_index_abbreviation` | `1` |
| `team_index_nickname` | `2` |
| `team_index_year_founded` | `3` |
| `team_index_city` | `4` |
| `team_index_full_name` | `5` |
| `team_index_state` | `6` |
| `team_index_championship_year` | `7` |
