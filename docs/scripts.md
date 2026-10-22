# Scripts

Maintenance scripts live in [`/scripts`](../scripts). They are run by maintainers and are not part of the installed package. All of them except `gen-release.sh` send requests to `stats.nba.com`.

## `static_players_update/generate_static_data_file.py`

Regenerates [`src/nba_api/stats/library/data.py`](nba_api/stats/library/data.md), the bundled player and team data behind `nba_api.stats.static`.

- **Players** (NBA and WNBA) are fetched live from the `CommonAllPlayers` endpoint. Manual name corrections, such as family-name-first ordering or nicknames, go in `player_adjustments` / `wnba_player_adjustments` at the top of the script.
- **Teams** are not fetched. They are copied from the hand-maintained `teams` and `wnba_teams` lists in `static_players_update/template.py`. To add a team or a championship year, edit `template.py`, then regenerate, or make the same edit in `data.py` directly.

```bash
cd scripts/static_players_update
poetry run python generate_static_data_file.py   # writes ./static_files/data.py (gitignored)
cp static_files/data.py ../../src/nba_api/stats/library/data.py
cd ../..
poetry run ruff format src/nba_api/stats/library/data.py
poetry run pytest tests/unit/stats/static
```

Commit the result as `chore: refresh static player data`.

## `analyze_endpoints_and_create_files.py`

Analyzes every endpoint in the analyzer's endpoint list by probing `stats.nba.com` with valid, missing, and invalid parameters. It then generates endpoint `.py` files, endpoint documentation, and parameter documentation from the results. See the [endpoint tooling docs](table_of_contents.md#contributing-and-maintenance) and the [analysis format](endpoint_analysis_format.md).

```bash
PYTHONPATH=. poetry run python scripts/analyze_endpoints_and_create_files.py   # run from the repo root so `tools` is importable
```

> [!WARNING]
> This script sends a large number of requests and depends on the exact wording of the API's error messages, so it tends to break when NBA.com changes. Its output is a starting point to review and merge by hand, not a drop-in replacement for the files in `src/` and `docs/`. For a single endpoint, writing the class by hand and generating its docs with `generate_boilerplate_endpoint_documentation()` is usually easier.

Enabling `DEBUG` and `DEBUG_STORAGE` in [`debug.py`](nba_api/debug.md) caches responses between runs, which helps while debugging the analyzer.

## `gen-release.sh`

Prepares a release locally: it computes the next version from the Conventional Commits since the last tag, then updates `pyproject.toml` and `CHANGELOG.MD` in a local commit. It doesn't tag or push. See [RELEASE_TESTING.md](../RELEASE_TESTING.md).

```bash
./scripts/gen-release.sh
```
