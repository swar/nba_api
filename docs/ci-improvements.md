# CI: moving to GitHub Actions, and what comes next

Status: **draft / working doc.** The GitHub Actions workflows run alongside CircleCI until
cutover. Nothing below changes how releases are published until a maintainer does the
setup steps.

## 1. What was ported

| CircleCI (`.circleci/config.yml`) | GitHub Actions | Notes |
|---|---|---|
| `main` job: `poetry install`, matrix `cimg/python:3.10–3.13` | `ci.yml` → `test` (matrix 3.10–3.13, `fail-fast: false`) | Poetry pinned to 2.3.2, the version that generated `poetry.lock`. Virtualenv cached by `setup-python`, keyed on `poetry.lock`. |
| `pytest tests/unit` | `test` → *Unit tests* | |
| `pytest tests/integration -m "vcr"` | `test` → *Integration tests (VCR cassette replay)* | `NBA_API_PROXY=""` set explicitly. |
| `ruff check && ruff format --check` (ran 4×, once per Python) | `ci.yml` → `lint` (once, on 3.13) | Uses `--output-format=github` so problems show up as inline PR annotations. |
| `snyk/scan` orb, non-PR builds only | `ci.yml` → `snyk` (non-PR events only) | Runs `snyk test`, plus `snyk monitor` on master. **Needs a `SNYK_TOKEN` repo secret.** Skipped with a notice until one is added. |
| `release` job (`semantic-release publish` on master) | `release.yml` (manual trigger) | See §2. This is a behavior fix, not a 1:1 port. |

Also new in the port:

- `permissions: contents: read` by default. Write and OIDC permissions are granted only to
  the release jobs that need them.
- Every action is pinned to a full commit SHA, with the version in a comment.
- `concurrency` cancels superseded PR runs but never a run on master.
- `persist-credentials: false` on checkout, so the token isn't left in `.git/config`.
- Timeouts on every job (the default is 6 hours).
- Clearly named steps. CircleCI had two steps both called "run tests".

## 2. Finding: the CircleCI release job doesn't publish anything

`release` runs `poetry run semantic-release publish` on every master build. The locked
version is python-semantic-release **9.21.1**. In v8 and later, `publish` only uploads
files matching `dist/*` to the **latest existing tag's** GitHub release
(`semantic_release/cli/commands/publish.py`). It doesn't version, tag, build, or upload
to PyPI. The job never runs `poetry build`, so `dist/` is empty and nothing is uploaded.

Related dead config:

- `[tool.semantic_release] upload_to_pypi` and `upload_to_release` are v7 settings that v9
  ignores.
- `poetry config pypi-token.pypi $PYPI_TOKEN` and the `REPOSITORY_*` exports in that job
  are never used.
- The real PyPI publish is the manual `poetry publish` step printed by
  `scripts/gen-release.sh`. That matches the GitHub release history: tags and releases are
  created by hand.

`RELEASE_TESTING.md` describes the CircleCI job as part of the pipeline, so it should be
corrected at cutover.

`release.yml` replaces the manual `poetry build && poetry publish`. Given an existing tag,
it:

1. checks out the tag and fails if `v<pyproject version>` ≠ tag,
2. builds the sdist and wheel once and stores them as an artifact,
3. publishes to PyPI with **Trusted Publishing** (OIDC, no API token). This also produces
   PEP 740 attestations,
4. attaches the same files to the GitHub release.

It's `workflow_dispatch` only, so nothing publishes automatically.

## 3. Cutover checklist

Each step needs maintainer access. AGENTS.md lists `.circleci/` and release config as
ask-first.

- [ ] Merge the PR that adds `.github/workflows/`. Run both CIs on the next few PRs and
      compare results.
- [ ] (Optional) Add `SNYK_TOKEN` as a repo secret, or drop Snyk in favor of §4.3.
- [ ] On PyPI → nba_api → *Publishing*, add a trusted publisher: owner `swar`, repo
      `nba_api`, workflow `release.yml`, environment `pypi`.
- [ ] In GitHub → *Settings → Environments*, create `pypi`. Add yourself as a required
      reviewer and restrict it to tags `v*`.
- [ ] Dry run: run `release.yml` against TestPyPI from a fork, or do the next real release
      with it instead of `poetry publish`.
- [ ] In branch protection (or a ruleset) for `master`, require `Lint (ruff)` and the four
      `Tests (Python 3.x)` checks, or the single aggregate check from §4.1.
- [ ] Delete `.circleci/`, disconnect the CircleCI project, and revoke the CircleCI
      `PYPI_TOKEN` / `GITHUB_TOKEN`.
- [ ] Remove `upload_to_pypi` / `upload_to_release` from `[tool.semantic_release]`.
- [ ] Update the references: README badge, `AGENTS.md` ("These mirror CI
      (`.circleci/config.yml`)", and the ask-before list), `RELEASE_TESTING.md`,
      `CONTRIBUTING.md`, and the "next steps" in `scripts/gen-release.sh`.

## 4. Improvements

Ordered by value for effort. Each item can be its own small PR.

### 4.1 Quick wins (≤ 1 hour each)

- **One required check.** Add an `all-green` job with `needs: [lint, test]` and
  `if: always()` that fails if any dependency failed. Branch protection then requires only
  that job, so adding Python versions or jobs never means editing protection rules. It
  also makes path filtering (4.4) safe.
- **Lint PR titles as Conventional Commits.** Releases depend on commit messages, and with
  squash merges the PR title *becomes* the commit message. Today nothing checks it.
  `amannn/action-semantic-pull-request` with the `allowed_tags` from pyproject closes the
  gap. This is probably the most valuable item on the list.
- **Enforce "unit tests never touch the network."** AGENTS.md states this rule, but CI
  doesn't enforce it. pytest-recording (already a dependency) has `--block-network`. Add
  it, plus `--record-mode=none`, to both test steps. Then a test that would have quietly
  called stats.nba.com fails loudly instead.
- **`poetry check --lock`** in `lint`, so CI catches a `pyproject.toml` change committed
  without re-locking.
- **Dependabot for GitHub Actions.** Add a `github-actions` ecosystem entry to
  `.github/dependabot.yml` so the SHA pins get updated. Also use `groups:` to batch
  minor/patch pip updates into one weekly PR instead of up to ten.
- **Keep the pre-commit Ruff version in sync.** `.pre-commit-config.yaml` pins
  `rev: v0.15.2` separately from the locked Ruff. They match today but will drift. Either
  let Dependabot/pre-commit.ci bump it, or add a CI check that compares the two.
- **Test reporting.** Add `--junitxml` plus a step-summary or test-reporter action so
  failures show up in the PR checks UI rather than in raw logs. Add `pytest -n auto`
  (pytest-xdist) if the suite grows.

### 4.2 Release pipeline: from manual to boring

- **Auto-tag on the release PR.** Today a maintainer merges `chore: release vX.Y.Z`, then
  tags, creates the GitHub release, and publishes by hand. A workflow on push to master
  can detect a `chore: release v*` head commit and do all of that. It would create the tag
  and release from `CHANGELOG.MD`, then call the `release.yml` jobs as a reusable
  workflow. The `pypi` environment's required-reviewer gate is the human approval step.
- **Package smoke test before publishing.** Tests run against the source tree, never the
  built wheel. Add a `build` job to `ci.yml` that runs `poetry build`, `twine check
  --strict dist/*`, installs the wheel into a clean venv, and runs
  `python -c "from nba_api.stats.endpoints import playercareerstats; from nba_api.stats.static import players; players.get_players()"`.
  That catches missing package data or a broken `src/` layout before users do.
- **TestPyPI rehearsal.** Add a `target` input (`testpypi` / `pypi`) to `release.yml` so
  the full path can be tested without touching real PyPI.

### 4.3 Supply chain and security

- **Dependency review on PRs.** Snyk only ran on non-PR builds, so PRs that add or bump a
  dependency were never scanned. `actions/dependency-review-action` needs no token and
  comments on the PR.
- **CodeQL** for `python` and `actions` (default setup is one click in repo settings).
- **zizmor** (workflow security linter) and **actionlint** as a lint step for
  `.github/workflows/`. They catch template injection, over-broad permissions, and
  unpinned actions.
- **pip-audit** as a tokenless alternative to Snyk. Decide whether to keep Snyk at all.
  Running two scanners is noise.
- **OpenSSF Scorecard** workflow plus badge. With 700+ forks and many downstream users,
  it's a cheap trust signal.
- **Fork PR policy.** Under *Settings → Actions*, require approval to run workflows for
  first-time contributors.

### 4.4 Test coverage of what we actually promise

- **Python 3.14** (released Oct 2025) as a matrix entry. Start with `continue-on-error`,
  then make it required and add the classifier.
- **Minimum-dependency job.** pyproject promises `numpy>=1.26`, `pandas>=2.1`,
  `requests>=2.32.3`, but CI only tests whatever the lockfile resolves to. Add one job on
  3.10 that installs the declared floors and runs the unit tests.
- **macOS and Windows** on one Python version. The package claims "OS Independent", and
  path handling and line endings in cassettes are typical places where that breaks.
- **Coverage.** pytest-cov is already a dependency. Publish the report (Codecov or a
  step-summary comment) and set a floor that only goes up.
- **Path filters.** Skip the test matrix on docs-only PRs (`docs/**`, `*.md`). Only do
  this together with the aggregate check from 4.1, or required checks will hang.

### 4.5 Scheduled jobs that watch the upstream API

This is where CI could make the project much better. nba_api's main failure mode is
stats.nba.com changing under us, and right now users are the ones who find out.

- **Nightly live canary.** A `canary` pytest marker is registered in pyproject but no test
  uses it. Tag a few cheap smoke specs as `canary` and run `-m "live and canary"` on a
  `schedule`. On failure, open or update a single tracking issue. Caveats:
  stats.nba.com blocks many cloud IP ranges, including GitHub-hosted runners, so this
  probably needs a proxy secret (`NBA_API_PROXY`) or a self-hosted runner. Make it
  non-blocking, and ask the maintainer first (AGENTS.md: no `live` runs unless asked).
- **Endpoint drift report.** Once `tools/stats/endpoint_scope` lands (branch
  `chore/endpoint-scope-tool`), run it weekly and open an issue when upstream endpoints or
  parameters change.
- **Static data refresh.** Run `scripts/static_players_update` monthly and open a PR with
  the regenerated `stats/library/data.py` (e.g. `peter-evans/create-pull-request`). That
  turns roster changes into a reviewable diff instead of a chore.
- **Season rollover reminder.** `Season.default` rolls over in October and
  `RECORDED_SEASON_YEAR` pins cassettes. A scheduled job each October can open an issue to
  re-record cassettes and bump the constant.

### 4.6 Repo hygiene enforced by CI

- **Endpoint checklist check.** AGENTS.md lists six places a new endpoint must touch:
  module, `__init__` `__all__` and import, unit test, `EndpointSpec`, doc page, and TOC
  entry. A small script or unit test can check that every module in `stats/endpoints/`
  appears in all of them. Contributors get a precise error instead of a review comment.
- **Docs link check** with `lychee` over `docs/` and `README.md`, on a weekly schedule so
  it doesn't flake PRs.
- **Composite action** `.github/actions/setup-poetry` to remove the repeated
  checkout → poetry → setup-python → install steps across workflows.
- **Single source for CI commands.** Workflows and `make ci` drift independently. Either
  have the workflow call `make` targets, or treat the workflow as the source of truth and
  generate the AGENTS.md command block from it.

## 5. Open questions for the maintainer

1. Keep Snyk (add `SNYK_TOKEN`) or replace it with dependency-review + pip-audit?
2. Automate releases fully (4.2), or keep the human tag step and only automate the publish?
3. Is a proxy secret for live canaries acceptable, given the credential-leak gotcha in
   AGENTS.md? The workflow would have to mask it and keep tracebacks out of issue bodies.
