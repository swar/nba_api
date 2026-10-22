#`/scripts/`

## `analyze_endpoints_and_create_files.py`

This is a script to analyze all endpoints and create the .py files, endpoint documentation, and parameter documentation. Please note that this file might break dependent on major changes to the NBA API.

It will be beneficial to enable `DEBUG` and `DEBUG_STORAGE` to help in the debugging process.


## `static_players_update/generate_static_data_file.py`

Regenerates the `players` and `wnba_players` lists from the `CommonAllPlayers` endpoint and writes a complete `data.py` (using `template.py`) to `./static_files/data.py` in the directory it is run from. Run it from `scripts/static_players_update/` and copy the result to `src/nba_api/stats/library/data.py`.

The `teams` and `wnba_teams` lists in `template.py` are written into `data.py` as-is, so team changes belong in the template (see below).

## `static_teams_update/generate_static_teams.py`

Refreshes the `teams` and `wnba_teams` lists from the `CommonTeamYears` and `TeamDetails` endpoints. Existing rows are the base, so hand-curated fields such as state, city and abbreviation are kept.

- Championship years are refreshed from the API.
- Teams the API reports as active that are missing from the data are added. The API has no state field, so add new teams' states to `team_states` in the script.
- Differences in abbreviation, nickname, city or year founded, and teams that are no longer active, are logged as warnings and left unchanged for manual review.

The lists are rewritten in both `scripts/static_players_update/template.py` and `src/nba_api/stats/library/data.py`, so a later players refresh does not revert them.

```bash
# Report what would change, exit 1 if the data is out of date (writes nothing)
poetry run python scripts/static_teams_update/generate_static_teams.py --check

# Apply the changes
poetry run python scripts/static_teams_update/generate_static_teams.py
```
