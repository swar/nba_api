## What does this change?

<!-- A short description, and the issue it fixes if there is one (for example "Fixes #123"). -->

## Checklist

- [ ] The PR title follows [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `docs:`, ...); it drives the release notes.
- [ ] Unit tests pass: `uv run pytest tests/unit`
- [ ] Cassette tests pass: `NBA_API_PROXY= uv run pytest tests/integration -m vcr`
- [ ] Lint and format pass: `uv run ruff check && uv run ruff format --check`
- [ ] New or changed endpoints include tests and docs (see [CONTRIBUTING.md](https://github.com/swar/nba_api/blob/master/CONTRIBUTING.md)).
- [ ] No public endpoint, parameter, or data set names were renamed or removed.
