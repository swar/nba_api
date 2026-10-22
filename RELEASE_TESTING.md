# Releases

This guide is for maintainers. It covers how a release is cut and how to preview a release safely without publishing anything.

Versioning and changelog generation use [python-semantic-release](https://python-semantic-release.readthedocs.io/) (configured under `[tool.semantic_release]` in `pyproject.toml`). The next version is computed from the [Conventional Commits](https://www.conventionalcommits.org/) merged since the last `vX.Y.Z` tag.

## How commits map to versions

| Commit | Example | Version bump |
|---|---|---|
| `fix:`, `perf:` | `fix: resolve timeout in HTTP requests` | patch (1.11.4 → 1.11.5) |
| `feat:` | `feat: add player stats endpoint` | minor (1.11.4 → 1.12.0) |
| `feat!:` or a `BREAKING CHANGE:` footer | `feat!: remove deprecated endpoints` | major (1.11.4 → 2.0.0) |
| `docs:`, `test:`, `chore:`, `refactor:`, `style:`, `build:`, `ci:` | `docs: update examples` | none |

Commits matching `Bump ...`, `Update ...`, or `Merge pull request ...` are excluded from the changelog.

## Cutting a release

1. **Prepare.** From an up-to-date `master`, run the release script:

   ```bash
   git checkout master && git pull
   ./scripts/gen-release.sh
   ```

   The script switches to a `release` branch (offering to create it), shows the computed next version, and asks for confirmation. It then runs `semantic-release version --no-tag --no-push --no-vcs-release`, which updates the version in `pyproject.toml` and `CHANGELOG.MD` in a single local commit. Nothing is tagged or pushed.

2. **Review.** Check the changes with `git show` and edit the changelog wording if needed.

3. **Open a PR.** Push the branch and open a PR titled `chore: release vX.Y.Z` against `master`.

4. **Tag.** After the PR is merged, tag the merge commit `vX.Y.Z`, push the tag, and create the GitHub release for it.

5. **Publish.** In GitHub → *Actions* → **Release** → *Run workflow*, enter the tag and pick `pypi`. The workflow checks that the tag matches the version in `pyproject.toml`, builds once, publishes to PyPI via [Trusted Publishing](https://docs.pypi.org/trusted-publishers/), and attaches the built files to the GitHub release. The manual alternative is still `poetry build && poetry publish` from a clean checkout of the tag.

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
