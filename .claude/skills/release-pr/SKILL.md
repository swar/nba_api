---
name: release-pr
description: Open the nba_api release PR - write the CHANGELOG.MD notes from the commits since the last tag, create the release/vX.Y.Z commit with scripts/gen-release.sh, push it, and open the "chore: release vX.Y.Z" PR. Use when the maintainer asks to prepare or start a release, open a release PR, or write release notes. Does not merge, tag, or publish.
---

Open the release PR for the next nba_api version. `RELEASING.md` is the source of truth;
read its "Writing the release notes" section first and follow it exactly.

1. Confirm you're on an up-to-date `master` with a clean working tree. If not, stop and say why.
2. Run `./scripts/gen-release.sh --context` and read the whole output.
3. Write the notes to a file in your scratchpad (not in the repo), following the rules and
   format in `RELEASING.md`.
4. Run `./scripts/gen-release.sh --notes <file> --yes`. If it warns that PRs are missing from
   the notes, decide whether each belongs, then `git switch master`, delete the
   `release/vX.Y.Z` branch, fix the notes, and re-run.
5. Push the branch and open the PR:
   `git push -u origin release/vX.Y.Z`, then
   `gh pr create --base master --title "chore: release vX.Y.Z" --body-file <file>`.
   The body is the new CHANGELOG.MD section, followed by a "After merging" checklist with the
   tag, GitHub release, and Release workflow (`target: pypi`) commands the script printed.
6. Reply with the PR link and the new changelog section.

Stop there. Never merge the PR, push tags, create the GitHub release, or run the Release
workflow. Those are the maintainer's steps after reviewing the PR.
