---
name: release
description: Prepare an nba_api release - gather the commits since the last tag, write the CHANGELOG.MD notes, and create the release/vX.Y.Z commit with scripts/gen-release.sh. Use when the maintainer asks to prepare, cut, or start a release, or to write release notes.
---

Prepare the next nba_api release. `RELEASING.md` is the source of truth; read its
"Writing the release notes" section first and follow it exactly.

1. Confirm you're on an up-to-date `master` with a clean working tree. If not, stop and say why.
2. Run `./scripts/gen-release.sh --context` and read the whole output.
3. Write the notes to a file in your scratchpad (not in the repo), following the rules and
   format in `RELEASING.md`.
4. Run `./scripts/gen-release.sh --notes <file> --yes`. If it warns that PRs are missing from
   the notes, decide whether each belongs, then `git switch master`, delete the
   `release/vX.Y.Z` branch, fix the notes, and re-run.
5. Show the maintainer the result (`git show --stat` plus the new CHANGELOG.MD section), and
   list the next steps the script printed.

Stop there. Don't push, open the PR, tag, or run the Release workflow unless the maintainer
asks you to in this conversation.
