# AGENTS.md

Guidance for AI coding agents (Claude Code, Codex, Cursor, Copilot, etc.) working in this repo.
Human contributors: see [CONTRIBUTING.md](CONTRIBUTING.md). Keep this file short and factual — if a
rule here goes stale, fix it in the same PR that made it stale.

## What this is

`nba_api` is a widely used PyPI client for the NBA.com APIs (stats.nba.com and the live CDN).
Python 3.10–3.15, `src/` layout, managed with Poetry, linted/formatted with Ruff.
**Downstream users depend on the public API** — endpoint class names, constructor parameter
names, and dataset attribute names are a compatibility contract. Don't rename or remove them;
add new things alongside old ones.

## Commands

Run everything through Poetry. These mirror CI (`.github/workflows/ci.yml`):

```bash
poetry install                                   # set up env
poetry run pytest tests/unit                     # unit tests (no network, ~5s)
NBA_API_PROXY= poetry run pytest tests/integration -m vcr   # cassette replay tests (no network)
poetry run ruff check --fix && poetry run ruff format       # lint + format
make ci                                          # all of the above in check mode
```

Single test: `poetry run pytest tests/unit/stats/endpoints/test_teamgamelog.py -k initialization`

After editing Python, run `poetry run ruff check --fix <files> && poetry run ruff format <files>`.

**Definition of done:** unit tests, VCR tests, `ruff check`, and `ruff format --check` all pass.

## Layout

```
src/nba_api/
  library/http.py            # NBAHTTP / NBAResponse base: sessions, proxy, headers
  library/proxy.py           # resolve_proxy(): per-request proxy lookup, NBA_API_REQUIRE_PROXY, redact()
  library/debug/debug.py     # DEBUG flags (read at import time) + deprecated legacy PROXY
  stats/endpoints/<name>.py  # one class per stats.nba.com endpoint (~140 of them)
  stats/endpoints/_parsers/  # parsers for nested-JSON (V3-style) endpoints + _PARSER_REGISTRY
  stats/library/parameters.py # parameter enums/defaults (Season, SeasonType, LeagueID, ...)
  stats/library/data.py      # GENERATED static players/teams data — do not hand-edit
  stats/static/              # players.py / teams.py lookup helpers over data.py
  live/nba/endpoints/        # live CDN endpoints (scoreboard, boxscore, playbyplay, odds)
tests/unit/                  # fast, offline; HTTP is mocked
tests/integration/           # smoke + scenario tests; replay VCR cassettes or hit the live API
tools/stats/endpoint_scope/  # scope a new endpoint from a URL; `--all --offline` audits expected_data vs cassettes
tools/stats/ (others)        # old generators; endpoint_analysis no longer works upstream, so don't rely on them
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
`docs/nba_api/stats/endpoints/<name>.md` plus entries in `docs/table_of_contents.md` and
`docs/nba_api/stats/endpoint_guide.md`.

## Testing rules

- Unit tests must never touch the network. Mock the HTTP layer (see `tests/unit/http/`).
- `http.py` reads `DEBUG`/`DEBUG_STORAGE` from `debug.py` **at import time**. Tests that change those
  must patch and reload the modules — follow `tests/unit/http/test_legacy_debug_usage.py`. The proxy
  is resolved per request in `library/proxy.py`: just `monkeypatch.setenv("NBA_API_PROXY", ...)`.
- Integration markers: `vcr` = replays a cassette (offline, runs in CI); `live` = real HTTP;
  `canary` = the few live requests in `tests/integration/canary`, which force
  `NBA_API_REQUIRE_PROXY=1` and skip without `NBA_API_PROXY` (`make test-canary`).
  Do not record or re-record cassettes, or run `live`/`canary` tests, unless asked — they hit
  stats.nba.com, which rate-limits and blocks aggressively.
- stats.nba.com does not answer most cloud IPs, so live requests from hosted agent sandboxes hang
  until they time out. Work offline with cassettes and `get_request=False`. A hang there is not a
  bug: don't "fix" it by raising timeouts or adding retries.
- `Season.default` and friends are date-derived and roll over every October. Cassette tests pin
  them via `RECORDED_SEASON_YEAR` in `tests/integration/helpers/seasons.py`; bump it only when
  cassettes are re-recorded. Never hardcode "current season" assumptions in tests.

## Gotchas

- **Proxy credentials.** `NBA_API_PROXY` may hold real credentials. The library does not read `.env`,
  but a shell-exported `NBA_API_PROXY` still reaches tests, so run cassette tests with
  `NBA_API_PROXY=` (as above). Request errors have the proxy URL masked, but still never read,
  print, or commit `.env`, and never paste proxy URLs into commits, PRs, or issues.
- The version in `pyproject.toml` and each release's `CHANGELOG.MD` section are written by
  `scripts/gen-release.sh` in a `chore: release vX.Y.Z` PR. Don't bump the version or edit
  `CHANGELOG.MD` in ordinary PRs. When asked to open a release PR, follow "Writing the release
  notes" in `RELEASING.md`: run `--context`, write the notes to a file, run `--notes <file> --yes`,
  push the `release/vX.Y.Z` branch, open the PR, and stop. Never merge, tag, or publish.
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
- Adding runtime dependencies (keep the dependency list minimal: requests, pandas).
- Touching release config (`[tool.semantic_release]`, `.github/workflows/`, `scripts/gen-release.sh`).
- Anything that publishes: `semantic-release`, `poetry publish`, pushing tags.

## Further reading

`REFACTORING.md` (known tech debt, e.g. decoupling parsers from `http.py`),
`docs/open_api_findings.md` (audit findings about stats.nba.com not yet handled: bad enum
values, stale `expected_data`, unsent params, coverage gaps),
`docs/nba_api/stats/known_upstream_issues.md` (endpoints stats.nba.com broke or removed),
`docs/ai_agents.md` (for agents writing code that *uses* nba_api), `RELEASING.md`,
`docs/table_of_contents.md`.
