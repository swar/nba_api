# Releases

This guide is for maintainers. It covers how a release is cut and how to preview a release safely without publishing anything.

The next version is computed by [python-semantic-release](https://python-semantic-release.readthedocs.io/) (configured under `[tool.semantic_release]` in `pyproject.toml`) from the [Conventional Commits](https://www.conventionalcommits.org/) merged since the last `vX.Y.Z` tag. semantic-release does nothing else here. The release notes in `CHANGELOG.MD` are written per release (usually by an AI agent, from the commits), and publishing is done by the **Release** GitHub Actions workflow.

## Quick checklist

Details for each step are in [Cutting a release](#cutting-a-release). Replace `X.Y.Z` with the version the script prints.

```bash
# 1-3. Have an agent open the release PR: in Claude Code run /release-pr
#      (other agents: "Open the nba_api release PR following RELEASING.md").
#      It writes the notes, runs the script, pushes, and opens the PR. Or by hand:
git checkout master && git pull --ff-only
./scripts/gen-release.sh --context > /tmp/release-context.md   # read this, write /tmp/notes.md
./scripts/gen-release.sh --notes /tmp/notes.md                 # creates release/vX.Y.Z with one commit
git push -u origin release/vX.Y.Z
gh pr create --base master --title "chore: release vX.Y.Z"

# Review the PR (especially the CHANGELOG.MD section), then squash-merge it

# 4. Tag the merge commit and create the GitHub release
git switch master && git pull --ff-only
git tag vX.Y.Z && git push origin vX.Y.Z
awk '/^## vX.Y.Z$/ {on=1; next} on && /^## / {exit} on' CHANGELOG.MD | gh release create vX.Y.Z --title vX.Y.Z --notes-file -

# 5. Publish to PyPI, then approve the run when it pauses for the pypi environment
gh workflow run release.yml -f tag=vX.Y.Z -f target=pypi
gh run watch

# 6. Clean up
git branch -D release/vX.Y.Z
```

## How commits map to versions

| Commit | Example | Version bump |
|---|---|---|
| `fix:`, `perf:` | `fix: resolve timeout in HTTP requests` | patch (1.11.4 → 1.11.5) |
| `feat:` | `feat: add player stats endpoint` | minor (1.11.4 → 1.12.0) |
| `feat!:` or a `BREAKING CHANGE:` footer | `feat!: remove deprecated endpoints` | major (1.11.4 → 2.0.0) |
| `docs:`, `test:`, `chore:`, `refactor:`, `style:`, `build:`, `ci:` | `docs: update examples` | none |

## Cutting a release

1. **Write the notes.** Get the release context, then write this release's notes to a file outside the repo, following [Writing the release notes](#writing-the-release-notes):

   ```bash
   git checkout master && git pull --ff-only
   ./scripts/gen-release.sh --context > /tmp/release-context.md
   ```

   The context covers every commit since the last tag (first-parent, so one entry per merged PR), with its PR link, changed files and commit body, plus any notes already under `## Unreleased`. It changes nothing.

2. **Prepare.** Run the script with the notes:

   ```bash
   ./scripts/gen-release.sh --notes /tmp/notes.md --dry-run   # optional: check the plan first
   ./scripts/gen-release.sh --notes /tmp/notes.md
   ```

   First it checks that you're on `master`, the working tree is clean, `master` matches the remote (after fetching tags), and `pyproject.toml` matches the latest tag. Then it shows the next version, warns about any `feat:`/`fix:`/`perf:` PR missing from the notes, and asks for confirmation (`--yes` skips the prompt). On a yes, it creates a `release/vX.Y.Z` branch with one commit, `chore: release vX.Y.Z`. That commit:
   - bumps `pyproject.toml`;
   - adds a `## vX.Y.Z` section with today's date and the notes;
   - replaces anything under `## Unreleased`, leaving the heading empty.

   Nothing is tagged, pushed, or built. It stops with an error, changing nothing, if there's nothing to release or the notes are empty or contain `#`/`##` headings. Without `--notes`, the existing `## Unreleased` section is used as the notes. Run `--help` for options.

3. **Review and open a PR.** Check the commit with `git show` (amend it to reword the changelog), then push the branch and open a PR titled `chore: release vX.Y.Z`. The script prints the exact commands.

4. **Tag.** After the PR is squash-merged, tag the merge commit `vX.Y.Z`, push the tag, and create the GitHub release from that version's changelog section. The script prints these commands too.

5. **Publish.** In GitHub → *Actions* → **Release** → *Run workflow*, enter the tag and pick `pypi`. The workflow checks that the tag matches the version in `pyproject.toml`, builds once, publishes to PyPI via [Trusted Publishing](https://docs.pypi.org/trusted-publishers/), and attaches the built files to the GitHub release. The manual alternative is still `poetry build && poetry publish` from a clean checkout of the tag.

6. **Clean up.** `git branch -D release/vX.Y.Z`.

> [!WARNING]
> Don't run `semantic-release version` directly. The script only uses it to compute the version. The config uses changelog `mode = "update"` with a marker that `CHANGELOG.MD` never contains, so a stray run can't regenerate (and wipe) the hand-written changelog. It would still bump the version, commit, tag, and (by default) push.

## Writing the release notes

These rules are for whoever writes the notes, usually an AI agent working from the `--context` output.

**Procedure for agents**

1. On an up-to-date `master` with a clean tree, run `./scripts/gen-release.sh --context` and read all of it.
2. Write the notes to a file outside the repo (agents can't edit `CHANGELOG.MD` directly; `.claude/settings.json` denies it).
3. Run `./scripts/gen-release.sh --notes <file> --yes`. Fix the notes and re-run if it warns about missing PRs; delete the `release/vX.Y.Z` branch first (`git switch master && git branch -D release/vX.Y.Z`).
4. Push the branch (`git push -u origin release/vX.Y.Z`) and open the PR with `gh pr create --base master --title "chore: release vX.Y.Z"`. In the body, put the new changelog section, then the post-merge steps the script printed (tag, GitHub release, Release workflow) as a checklist.
5. Give the maintainer the PR link and stop. Merging, tagging, and publishing are the maintainer's job; never do them.

**What to include**

- Every `feat:`, `fix:`, and `perf:` PR, plus anything else a user of the package would notice: new or removed endpoints, parameters, or datasets; behavior changes; deprecations; dependency floor changes; static data updates. A `fix:` that only touches tests goes under `Infrastructure`.
- Carry over still-relevant entries from the existing `## Unreleased` notes. `--notes` replaces them.
- Skip pure noise: release commits, formatting-only changes, merge-branch commits. Group related internal changes (CI, tooling, test refactors) into a few `Infrastructure` entries instead of one per commit.
- Read the commit bodies and changed files, not just subjects. Describe the user-visible effect, not the implementation. If a PR fixes an issue, say so (`fixes #602`).
- Breaking changes (`!` or `BREAKING CHANGE:`) go first, in a `### Breaking Changes` section that says what users must change.

**Format** (match the `v1.11.4` section of `CHANGELOG.MD`)

- Sections, in this order and only when non-empty: `### Breaking Changes`, `### Added`, `### Changed`, `### Deprecated`, `### Removed`, `### Fixed`, `### Security`, `### Infrastructure`, `### Contributor`. Use `###` and deeper only.
- One bullet per change: ``* **Name** - What changed, in one or two sentences (PR [#123](https://github.com/swar/nba_api/pull/123))``. `Name` is the endpoint, class, or feature (`**LeagueGameFinder**`, `**Static Teams Data**`). Put code identifiers in backticks.
- Several PRs for one change: `(PR [#1](...), PR [#2](...))`.

Example:

```markdown
### Added
* **Static Teams Data** - Added the Portland Fire and Toronto Tempo WNBA expansion teams (PR [#693](https://github.com/swar/nba_api/pull/693))

### Fixed
* **ScheduleLeagueV2** - League schedules now parse regardless of the order of keys in the NBA.com response (PR [#692](https://github.com/swar/nba_api/pull/692))
```

## One-time setup for the Release workflow

Already done for `swar/nba_api`; kept for reference.

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
