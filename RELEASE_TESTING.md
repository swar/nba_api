# Releases

This guide is for maintainers. It covers how a release is cut and how to preview a release safely without publishing anything.

The next version is computed by [python-semantic-release](https://python-semantic-release.readthedocs.io/) (configured under `[tool.semantic_release]` in `pyproject.toml`) from the [Conventional Commits](https://www.conventionalcommits.org/) merged since the last `vX.Y.Z` tag. semantic-release does nothing else here: `CHANGELOG.MD` is written by hand, and publishing is done by the **Release** GitHub Actions workflow.

## How commits map to versions

| Commit | Example | Version bump |
|---|---|---|
| `fix:`, `perf:` | `fix: resolve timeout in HTTP requests` | patch (1.11.4 → 1.11.5) |
| `feat:` | `feat: add player stats endpoint` | minor (1.11.4 → 1.12.0) |
| `feat!:` or a `BREAKING CHANGE:` footer | `feat!: remove deprecated endpoints` | major (1.11.4 → 2.0.0) |
| `docs:`, `test:`, `chore:`, `refactor:`, `style:`, `build:`, `ci:` | `docs: update examples` | none |

## Cutting a release

1. **Write the notes.** Make sure the `## Unreleased` section of `CHANGELOG.MD` describes everything user-facing since the last release. A dry run lists any `feat:`/`fix:`/`perf:` commits whose PR number isn't mentioned there:

   ```bash
   git checkout master && git pull --ff-only
   ./scripts/gen-release.sh --dry-run
   ```

2. **Prepare.** Run the script for real:

   ```bash
   ./scripts/gen-release.sh
   ```

   First it checks that you're on `master`, the working tree is clean, `master` matches the remote (after fetching tags), and `pyproject.toml` matches the latest tag. Then it shows the next version and asks for confirmation. On a yes, it creates a `release/vX.Y.Z` branch with one commit, `chore: release vX.Y.Z`. That commit bumps `pyproject.toml` and renames `## Unreleased` to `## vX.Y.Z` with today's date, leaving a new empty `## Unreleased` above it. Nothing is tagged, pushed, or built. It stops with an error, changing nothing, if there's nothing to release or the Unreleased section is empty. Run `--help` for options.

3. **Review and open a PR.** Check the commit with `git show` (amend it to reword the changelog), then push the branch and open a PR titled `chore: release vX.Y.Z`. The script prints the exact commands.

4. **Tag.** After the PR is squash-merged, tag the merge commit `vX.Y.Z`, push the tag, and create the GitHub release from that version's changelog section. The script prints these commands too.

5. **Publish.** In GitHub → *Actions* → **Release** → *Run workflow*, enter the tag and pick `pypi`. The workflow checks that the tag matches the version in `pyproject.toml`, builds once, publishes to PyPI via [Trusted Publishing](https://docs.pypi.org/trusted-publishers/), and attaches the built files to the GitHub release. The manual alternative is still `poetry build && poetry publish` from a clean checkout of the tag.

6. **Clean up.** `git branch -D release/vX.Y.Z`.

> [!WARNING]
> Don't run `semantic-release version` directly. The script only uses it to compute the version. The config uses changelog `mode = "update"` with a marker that `CHANGELOG.MD` never contains, so a stray run can't regenerate (and wipe) the hand-written changelog. It would still bump the version, commit, tag, and (by default) push.

The CircleCI `release` job (`.circleci/config.yml`) runs `semantic-release publish` on every `master` build. With python-semantic-release v9 that only uploads `dist/*` to the latest GitHub release, and `dist/` is never built there, so it doesn't publish anything. It goes away when CircleCI is retired.

### One-time setup for the Release workflow

1. On [PyPI](https://pypi.org/manage/project/nba_api/settings/publishing/), add a trusted publisher: owner `swar`, repository `nba_api`, workflow `release.yml`, environment `pypi`. To rehearse, do the same on [TestPyPI](https://test.pypi.org/) with environment `testpypi`.
2. In GitHub → *Settings* → *Environments*, create `pypi` and `testpypi`. On `pypi`, add yourself as a required reviewer and limit deployments to the `master` branch (the branch the workflow is run from; the tag is an input).
3. Rehearse with target `testpypi` before the first real run. Each version can only be uploaded once per index.

## Previewing a release safely

All of these run locally and publish nothing.

**See which commits will count toward the next release:**

```bash
git log --oneline $(git describe --tags --abbrev=0)..HEAD
```

**Compute the next version the way the release script does:**

```bash
poetry run semantic-release version --print
```

This only works on branches matched in `[tool.semantic_release.branches]` (`master`/`main`, `release`/`release/*`, or `test-release` for `-rc` prereleases). The patterns match the start of the branch name, so `release-preview` below also counts. On any other branch it reports that no release will be made.

**Preview the result of merging your branch,** in a throwaway worktree so your checkout is untouched:

```bash
git fetch origin --tags
git worktree add -b release-preview ../nba_api-release-preview origin/master
cd ../nba_api-release-preview
git merge --no-edit <your-branch>
poetry install
poetry run semantic-release version --print
cd - && git worktree remove --force ../nba_api-release-preview
git branch -D release-preview
```

**Check commit message format** for recent commits. Lines that don't match need rewording before merge:

```bash
git log --format=%s -20 | grep -vE '^(feat|fix|perf|docs|style|refactor|test|chore|build|ci)(\(.+\))?!?: '
```

> [!CAUTION]
> Don't test the release pipeline by merging test commits into `swar/nba_api:master`. Any merged `feat:` or `fix:` commit will be included in the next real release and its changelog. To exercise the full pipeline end to end, run the **Release** workflow with target `testpypi`, or use your own fork.

## Troubleshooting

**"No release will be made"**

- No `feat:`, `fix:`, `perf:`, or breaking commits since the last tag.
- The current branch isn't listed in `[tool.semantic_release.branches]`.
- Tags are missing locally. Run `git fetch --tags`.

**The computed version is unexpected**

Make sure your local tags match the remote (`git fetch --tags --force`), then list the commits since the last tag with the command above. A single mislabeled commit, such as `feat:` that should have been `fix:`, changes the bump.
