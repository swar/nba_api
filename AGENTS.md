# AGENTS.md

Guidance for AI coding agents (Claude Code, Codex, Cursor, Copilot, etc.) working in this repo.
Human contributors: see [CONTRIBUTING.md](CONTRIBUTING.md). Keep this file short and factual — if a
rule here goes stale, fix it in the same PR that made it stale.

## What this is

`nba_api` is a widely used PyPI client for the NBA.com APIs (stats.nba.com and the live CDN).
Python 3.10–3.13, `src/` layout, managed with Poetry, linted/formatted with Ruff.
**Downstream users depend on the public API** — endpoint class names, constructor parameter
names, and dataset attribute names are a compatibility contract. Don't rename or remove them;
add new things alongside old ones.

## Commands

Run everything through Poetry. These mirror CI (`.circleci/config.yml`):

```bash
poetry install                                   # set up env
poetry run pytest tests/unit                     # unit tests (no network, ~5s)
NBA_API_PROXY= poetry run pytest tests/integration -m vcr   # cassette replay tests (no network)
poetry run ruff check --fix && poetry run ruff format       # lint + format
make ci                                          # all of the above in check mode
```

Single test: `poetry run pytest tests/unit/stats/endpoints/test_teamgamelog.py -k initialization`

**Definition of done:** unit tests, VCR tests, `ruff check`, and `ruff format --check` all pass.

## Layout

```
src/nba_api/
  library/http.py            # NBAHTTP / NBAResponse base: sessions, proxy, headers
  library/debug/debug.py     # DEBUG flags + PROXY, loaded from env / local .env at import time
  stats/endpoints/<name>.py  # one class per stats.nba.com endpoint (~140 of them)
  stats/endpoints/_parsers/  # parsers for nested-JSON (V3-style) endpoints + _PARSER_REGISTRY
  stats/library/parameters.py # parameter enums/defaults (Season, SeasonType, LeagueID, ...)
  stats/library/data.py      # GENERATED static players/teams data — do not hand-edit
  stats/static/              # players.py / teams.py lookup helpers over data.py
  live/nba/endpoints/        # live CDN endpoints (scoreboard, boxscore, playbyplay, odds)
tests/unit/                  # fast, offline; HTTP is mocked
tests/integration/           # smoke + scenario tests; replay VCR cassettes or hit the live API
tools/                       # code/doc generators used by scripts/analyze_endpoints_and_create_files.py
scripts/static_players_update/  # regenerate data.py from the live API
docs/nba_api/                # per-endpoint markdown docs
```

## Endpoint conventions

Stats endpoints share one shape — copy a neighbor (e.g. `commonplayerinfo.py`) rather than inventing:

- Class attrs `endpoint = "<lowercase name>"` and `expected_data = {dataset: [columns]}`.
- `__init__(..., proxy=None, headers=None, timeout=30, get_request=True)`; builds
  `self.parameters` keyed by the **NBA query-string names** (`"PlayerID"`, `"Season"`), with
  defaults from `stats/library/parameters.py`.
- `load_response()` populates `self.data_sets` plus one `Endpoint.DataSet` attribute per dataset.
- Tabular endpoints use `nba_response.get_data_sets()`. Nested-JSON endpoints call
  `get_data_sets(self.endpoint)` and need a parser in `_parsers/` registered in `_PARSER_REGISTRY`.

Adding an endpoint touches: the endpoint file, `stats/endpoints/__init__.py` (both the `__all__`
module name and the class import), a unit test using `get_request=False` (plus a parser test if
applicable), an `EndpointSpec` in `tests/integration/helpers/endpoint_specs.py`, and
`docs/nba_api/stats/endpoints/<name>.md` plus an entry in `docs/table_of_contents.md`.

## Testing rules

- Unit tests must never touch the network. Mock the HTTP layer (see `tests/unit/http/`).
- `http.py` reads `DEBUG`/`PROXY` from `debug.py` **at import time**. Tests that change those must
  patch and reload the modules — follow `tests/unit/http/test_legacy_debug_usage.py`.
- Integration markers: `vcr` = replays a cassette (offline, runs in CI); `live` = real HTTP.
  Do not record or re-record cassettes, or run `live` tests, unless asked — they hit
  stats.nba.com, which rate-limits and blocks aggressively.
- `Season.default` and friends are date-derived and roll over every October. Cassette tests pin
  them via `RECORDED_SEASON_YEAR` in `tests/integration/helpers/seasons.py`; bump it only when
  cassettes are re-recorded. Never hardcode "current season" assumptions in tests.

## Gotchas

- **`.env` contains real proxy credentials.** `debug.py` auto-loads `.env` from the CWD, so a
  local `NBA_API_PROXY` leaks into tests. VCR tests then fail with SOCKS errors **and the
  traceback prints the credentials**. Always run integration tests with `NBA_API_PROXY=`
  (as above). Never read, print, or commit `.env`, and never paste tracebacks containing proxy
  URLs into commits, PRs, or issues.
- The version in `pyproject.toml` and the release headings in `CHANGELOG.MD` are written by
  `scripts/gen-release.sh` in a maintainer's `chore: release vX.Y.Z` PR. Don't bump the version
  by hand. Changelog entries are hand-written under `## Unreleased`.
- `stats/library/data.py` is generated by `scripts/static_players_update/`: players come from the
  API (fixes go in `player_adjustments`), teams from that script's `template.py`. Any direct edit
  to `data.py` must be mirrored there or the next refresh drops it. See `docs/scripts.md`.
- Endpoints marked deprecated/skip in `endpoint_specs.py` are known-flaky upstream; leave them.

## Commits & PRs

- [Conventional Commits](https://www.conventionalcommits.org/) are **required** — they drive
  releases. `feat:` → minor, `fix:`/`perf:` → patch, `!`/`BREAKING CHANGE:` → major. Use
  `test:`, `docs:`, `chore:`, `refactor:`, `ci:`, `build:` for everything else.
- Branch off `master`; one logical change per PR; don't commit directly to `master`.
- Pre-commit runs Ruff (`poetry run pre-commit install` once per clone).

## Ask before

- Changing public endpoint/parameter/dataset names or signatures.
- Adding runtime dependencies (keep the dependency list minimal: requests, numpy, pandas).
- Touching release config (`[tool.semantic_release]`, `.circleci/`, `scripts/gen-release.sh`).
- Anything that publishes: `semantic-release`, `poetry publish`, pushing tags.

## Further reading

`REFACTORING.md` (known tech debt, e.g. decoupling parsers from `http.py`),
`RELEASING.md`, `docs/table_of_contents.md`.
