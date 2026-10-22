# Contributing to nba_api

Thank you for your interest in contributing! There are many ways to help beyond writing code: reporting bugs, flagging endpoints that NBA.com has changed, improving documentation, and answering questions.

## Asking questions

Rather than opening an issue for a question, join the [Slack](https://join.slack.com/t/nbaapi/shared_invite/zt-3dc2qtnh0-udQJoSYrQVWaXOF3owVaAw) or ask on [Stack Overflow](https://stackoverflow.com/questions/tagged/nba-api) with the `nba-api` tag.

## Reporting issues

1. **Search first.** Check [open issues](https://github.com/swar/nba_api/issues) for an existing report. If one exists, add details or a 👍 [reaction](https://github.blog/news-insights/product-news/add-reactions-to-pull-requests-issues-and-comments/) instead of a "+1" comment.
2. **One problem per issue.** Don't combine several bugs or requests in one issue, and don't add to an existing issue unless the cause is identical.
3. **Use the bug report template** and include:
   - your `nba_api` version (`python -c "import nba_api; print(nba_api.__version__)"`)
   - numbered steps to reproduce
   - what you expected versus what happened
   - a minimal, copy-pasteable code snippet (not a screenshot)

For significant changes, open an issue titled `PROPOSAL: ...` to discuss the design before writing code.

## Development setup

### Prerequisites

- **Python** — a version listed under `requires-python` and the classifiers in [`pyproject.toml`](pyproject.toml) (currently 3.10–3.13; CI tests all of them).
- **[Poetry](https://python-poetry.org/docs/#installation) 2.x** — manages the virtual environment, dependencies, and builds.
- **[pyenv](https://github.com/pyenv/pyenv)** (optional) — for switching between Python versions. Poetry uses whichever Python is active.

A [dev container](.devcontainer/devcontainer.json) is also provided if you prefer VS Code or Codespaces.

### Setup

```bash
# 1. Fork the repository on GitHub, then clone your fork
git clone https://github.com/<your-username>/nba_api.git
cd nba_api

# 2. Install the package and all development dependencies
poetry install

# 3. Install the pre-commit hooks (runs Ruff on every commit)
poetry run pre-commit install

# 4. Verify everything passes
make ci
```

Run commands with `poetry run <command>`, or activate the environment with `eval $(poetry env activate)`.

## Running checks

`make ci` runs the same checks as CI. The individual commands:

| Check | Command |
|---|---|
| Unit tests (offline, fast) | `poetry run pytest tests/unit` |
| Integration tests (replay recorded responses, offline) | `make test-vcr` |
| Live canary tests (real requests, needs a proxy; see below) | `make test-canary` |
| Lint | `poetry run ruff check` |
| Format check | `poetry run ruff format --check` |
| Auto-fix lint and format | `make format` |
| Coverage report | `make test-cov` |

> [!WARNING]
> Running bare `pytest` also collects integration tests that send real requests to `stats.nba.com`. Those requests are slow and easily throttled. Run `tests/unit` and the `vcr`-marked tests, as above, unless you specifically need live requests.

> [!NOTE]
> If you export `NBA_API_PROXY` in your shell, use `make test-vcr` instead of calling pytest directly. It clears the proxy so recorded responses are replayed rather than sent through the proxy.

### Live canary tests

`tests/integration/canary` makes a handful of real requests to stats.nba.com and cdn.nba.com to confirm the library still works against the live APIs. It is meant for maintainers before a release, not for everyday development, and it is not part of `make ci`.

- Every request goes through the proxy in `NBA_API_PROXY` (export it in your shell). The tests set `NBA_API_REQUIRE_PROXY=1`, so they can never fall back to a direct connection.
- Without `NBA_API_PROXY` the tests skip locally. On GitHub Actions they fail instead, so a missing secret can't pass silently.
- SOCKS proxies (`socks5://...`) work because `requests[socks]` is a dev dependency.
- Don't combine them with `--block-network`, and don't use `pytest -l`/`--showlocals`, which prints local variables including the proxy URL.

### Test conventions

- **Unit tests** (`tests/unit/`) must never make network requests. Construct endpoints with `get_request=False` and mock the HTTP layer.
- **Integration tests** (`tests/integration/`) replay responses recorded as [VCR](https://github.com/kiwicom/pytest-recording) cassettes. The `vcr` marker means a test replays a cassette; `live` means it sends real requests.
- Season defaults such as `Season.default` change every October. Integration tests pin them to the season the cassettes were recorded in (`RECORDED_SEASON_YEAR` in `tests/integration/helpers/seasons.py`). Don't hardcode the current season in tests.

## Making changes

### Style

- Ruff enforces linting and formatting (configured in `pyproject.toml`). The pre-commit hook fixes most issues automatically. If it modifies files, stage them and commit again.
- Follow the patterns of the surrounding code. Endpoints in particular share one structure; copy a similar existing endpoint rather than starting from scratch.
- Don't break the public API. Endpoint class names, constructor parameter names, and data set attribute names are relied on by many downstream projects. Add new names alongside old ones rather than renaming.

### Adding or updating a stats endpoint

1. Add `src/nba_api/stats/endpoints/<name>.py`, following an existing endpoint with a similar response shape.
2. If the endpoint returns nested JSON instead of the tabular `resultSets` format, add a parser in `src/nba_api/stats/endpoints/_parsers/` and register it in `_PARSER_REGISTRY`.
3. Export it from `src/nba_api/stats/endpoints/__init__.py`: add the module name to `__all__` and import the class.
4. Add unit tests in `tests/unit/stats/endpoints/` (and parser tests, if applicable).
5. Add an `EndpointSpec` entry in `tests/integration/helpers/endpoint_specs.py`.
6. Document it in `docs/nba_api/stats/endpoints/<name>.md` and add it to [`docs/table_of_contents.md`](docs/table_of_contents.md).

### Updating static player and team data

`src/nba_api/stats/library/data.py` is generated by `scripts/static_players_update/` (see [docs/scripts.md](docs/scripts.md)). Player rows come from the API. Name corrections go in the script's `player_adjustments`, and team rows (including championship years) go in its `template.py`. If you also edit `data.py` directly, make the same change in the script or template so it survives the next refresh.

### Commit messages

This project uses [Conventional Commits](https://www.conventionalcommits.org/). The commit type determines the next version number and the changelog entry, so it matters:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

| Type | Use for | Version bump |
|---|---|---|
| `feat` | a new feature or endpoint | minor |
| `fix` | a bug fix | patch |
| `perf` | a performance improvement | patch |
| `docs` | documentation only | none |
| `test` | adding or fixing tests | none |
| `refactor` | code changes that neither fix a bug nor add a feature | none |
| `style` | formatting only | none |
| `build` | build system or dependencies | none |
| `ci` | CI configuration | none |
| `chore` | anything else that doesn't touch `src/` or tests | none |

A breaking change, marked with `!` after the type (`feat!: ...`) or a `BREAKING CHANGE:` footer, triggers a major bump.

### Pull requests

1. Create a branch from `master` in your fork.
2. Keep each PR to one logical change, and tidy up your commits before requesting review.
3. Make sure `make ci` passes.
4. Open the PR against `swar/nba_api:master`. Open it as a draft for early feedback on larger changes.

Don't edit `CHANGELOG.MD` or the version in `pyproject.toml`. Both are updated during the release process.

## Releases

Maintainers cut releases with [python-semantic-release](https://python-semantic-release.readthedocs.io/). `scripts/gen-release.sh` computes the next version from the commit history, bumps `pyproject.toml`, and dates the `## Unreleased` section of `CHANGELOG.MD`. The result is merged as a `chore: release vX.Y.Z` PR. Contributors only need to write correct commit messages. See [RELEASING.md](RELEASING.md) for the full process.

## AI coding agents

If you use an AI coding assistant, it should read [AGENTS.md](AGENTS.md), which summarizes these conventions for agents. Claude Code loads it automatically through `CLAUDE.md`.
