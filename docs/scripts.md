# Scripts

Maintenance scripts live in [`/scripts`](../scripts). They are run by maintainers and are not part of the installed package. All of them except `gen-release.sh` send requests to `stats.nba.com`.

## `static_players_update/generate_static_data_file.py`

Regenerates [`src/nba_api/stats/library/data.py`](nba_api/stats/library/data.md), the bundled player and team data behind `nba_api.stats.static`.

- **Players** (NBA and WNBA) are fetched live from the `CommonAllPlayers` endpoint. Manual name corrections, such as family-name-first ordering or nicknames, go in `player_adjustments` / `wnba_player_adjustments` at the top of the script.
- **Teams** are not fetched. They are copied from the hand-maintained `teams` and `wnba_teams` lists in `static_players_update/template.py`. To add a team or a championship year, edit `template.py`, then regenerate, or make the same edit in `data.py` directly.

```bash
cd scripts/static_players_update
uv run python generate_static_data_file.py   # writes ./static_files/data.py (gitignored)
cp static_files/data.py ../../src/nba_api/stats/library/data.py
cd ../..
uv run ruff format src/nba_api/stats/library/data.py
uv run pytest tests/unit/stats/static
```

Commit the result as `chore: refresh static player data`.

## `static_teams_update/generate_static_teams.py`

Refreshes the `teams` and `wnba_teams` lists from the `CommonTeamYears` and `TeamDetails` endpoints. Existing rows are the base, so hand-curated fields such as state, city and abbreviation are kept.

- Championship years are refreshed from the API.
- Teams the API reports as active that are missing from the data are added. The API has no state field, so add new teams' states to `team_states` in the script.
- Differences in abbreviation, nickname, city or year founded, and teams that are no longer active, are logged as warnings and left unchanged for manual review.

The lists are rewritten in both `scripts/static_players_update/template.py` and `src/nba_api/stats/library/data.py`, so a later players refresh does not revert them.

```bash
# Report what would change, exit 1 if the data is out of date (writes nothing)
uv run python scripts/static_teams_update/generate_static_teams.py --check

# Apply the changes
uv run python scripts/static_teams_update/generate_static_teams.py
```

## `gen-release.sh`

Prepares a release locally. It computes the next version from the Conventional Commits since the last tag, bumps `pyproject.toml`, and renames the hand-written `## Unreleased` section of `CHANGELOG.MD` to `## vX.Y.Z`, in one commit on a new `release/vX.Y.Z` branch. It doesn't tag, push, or build. See [RELEASING.md](../RELEASING.md).

```bash
./scripts/gen-release.sh --dry-run   # checks + plan, changes nothing
./scripts/gen-release.sh             # asks before committing
```
