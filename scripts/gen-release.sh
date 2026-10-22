#!/usr/bin/env bash
#
# Prepare an nba_api release.
#
# Computes the next version from the Conventional Commits since the last tag,
# bumps pyproject.toml, and turns the "## Unreleased" section of CHANGELOG.MD
# into "## vX.Y.Z", all in one commit on a new release/vX.Y.Z branch.
# Nothing is pushed, tagged, or published. The full process is in
# RELEASING.md.

set -euo pipefail

usage() {
    cat <<'EOF'
Usage: scripts/gen-release.sh [--dry-run] [--yes] [--remote NAME]

  --dry-run      Run every check and print the plan; change nothing.
  -y, --yes      Skip the confirmation prompt.
  --remote NAME  Remote for swar/nba_api (default: origin).
EOF
}

DRY_RUN=false
ASSUME_YES=false
REMOTE=origin
BASE_BRANCH=master
CHANGELOG=CHANGELOG.MD
# Matches the heading with or without a trailing \r (the file has mixed line endings).
UNRELEASED_RE='^## Unreleased[[:space:]]*$'

die() {
    echo "error: $*" >&2
    exit 1
}

info() {
    echo "==> $*"
}

while [ $# -gt 0 ]; do
    case "$1" in
        --dry-run) DRY_RUN=true ;;
        -y | --yes) ASSUME_YES=true ;;
        --remote)
            [ $# -ge 2 ] || die "--remote needs a value"
            REMOTE=$2
            shift
            ;;
        -h | --help)
            usage
            exit 0
            ;;
        *) die "unknown argument '$1' (see --help)" ;;
    esac
    shift
done

cd "$(git rev-parse --show-toplevel)"

# --- Preconditions -----------------------------------------------------------

command -v poetry >/dev/null || die "poetry is not installed"
git remote get-url "$REMOTE" >/dev/null 2>&1 ||
    die "no git remote named '$REMOTE' (pass --remote)"

branch=$(git branch --show-current)
[ "$branch" = "$BASE_BRANCH" ] ||
    die "run this from '$BASE_BRANCH' (currently on '${branch:-detached HEAD}')"

[ -z "$(git status --porcelain --untracked-files=no)" ] ||
    die "you have uncommitted changes; commit or stash them first"

info "Fetching $REMOTE/$BASE_BRANCH and tags"
git fetch --quiet --tags --force "$REMOTE" "$BASE_BRANCH"
[ "$(git rev-parse HEAD)" = "$(git rev-parse "$REMOTE/$BASE_BRANCH")" ] ||
    die "local $BASE_BRANCH differs from $REMOTE/$BASE_BRANCH; run: git pull --ff-only $REMOTE $BASE_BRANCH"

current=$(poetry version --short)
last_tag=$(git describe --tags --abbrev=0 --match 'v[0-9]*' 2>/dev/null) ||
    die "no vX.Y.Z tags found"
[ "v$current" = "$last_tag" ] ||
    die "pyproject.toml is at $current but the latest tag is $last_tag. Tag and publish the previous release first."

# --- Next version ------------------------------------------------------------

psr_log=$(mktemp)
trap 'rm -f "$psr_log"' EXIT

# --strict makes "nothing to release" exit 2 instead of reprinting the current version.
set +e
next=$(poetry run semantic-release --strict version --print 2>"$psr_log")
status=$?
set -e
if [ "$status" -ne 0 ]; then
    if grep -q "No release will be made" "$psr_log"; then
        die "nothing to release: no feat/fix/perf or breaking commits since $last_tag"
    fi
    cat "$psr_log" >&2
    die "semantic-release failed (exit $status); its output is above"
fi
next=$(printf '%s\n' "$next" | tail -n 1)
printf '%s\n' "$next" | grep -Eq '^[0-9]+\.[0-9]+\.[0-9]+$' ||
    die "unexpected version from semantic-release: '$next'"

release_branch="release/v$next"
if git show-ref --verify --quiet "refs/heads/$release_branch"; then
    die "branch $release_branch already exists locally; delete it or finish that release"
fi
if git ls-remote --exit-code --heads "$REMOTE" "$release_branch" >/dev/null 2>&1; then
    die "branch $release_branch already exists on $REMOTE"
fi

# --- Changelog ---------------------------------------------------------------

found=$(grep -cE "$UNRELEASED_RE" "$CHANGELOG" || true)
[ "$found" -eq 1 ] ||
    die "$CHANGELOG needs exactly one '## Unreleased' heading (found $found)"

unreleased=$(awk -v re="$UNRELEASED_RE" '
    $0 ~ re      { on = 1; next }
    on && /^## / { exit }
    on           { print }
' "$CHANGELOG" | tr -d '\r')
printf '%s\n' "$unreleased" | grep -q '[^[:space:]]' ||
    die "the '## Unreleased' section of $CHANGELOG is empty; write the release notes there first"

# User-facing commits whose PR number never appears in the Unreleased notes.
unmentioned=$(git log --first-parent --format='%s' "$last_tag..HEAD" | while IFS= read -r subject; do
    printf '%s\n' "$subject" | grep -Eq '^(feat|fix|perf)(\([^)]*\))?!?: ' || continue
    pr=$(printf '%s\n' "$subject" | sed -nE 's/.*\(#([0-9]+)\)$/\1/p')
    if [ -z "$pr" ] || ! printf '%s\n' "$unreleased" | grep -Eq "#$pr([^0-9]|$)"; then
        printf '    %s\n' "$subject"
    fi
done)

# --- Plan --------------------------------------------------------------------

today=$(date +%F)
echo
echo "Release plan"
echo "  version:   $current -> $next"
echo "  branch:    $release_branch (from $BASE_BRANCH @ $(git rev-parse --short HEAD))"
echo "  changelog: '## Unreleased' -> '## v$next' (Date: $today); a new empty '## Unreleased' goes above it"
echo
echo "Commits since $last_tag:"
git log --first-parent --format='    %h %s' "$last_tag..HEAD"
if [ -n "$unmentioned" ]; then
    echo
    echo "warning: these feat/fix/perf commits aren't mentioned in the Unreleased notes:"
    echo "$unmentioned"
fi
echo

if $DRY_RUN; then
    info "Dry run: nothing changed."
    exit 0
fi

if ! $ASSUME_YES; then
    [ -t 0 ] || die "not running interactively; pass --yes to skip the prompt"
    printf 'Create %s with this release commit? [y/N] ' "$release_branch"
    read -r reply
    case "$reply" in
        y | Y | yes) ;;
        *) die "aborted; nothing changed" ;;
    esac
fi

# --- Apply -------------------------------------------------------------------

git switch --quiet -c "$release_branch"
poetry version "$next" >/dev/null

tmp=$(mktemp)
awk -v re="$UNRELEASED_RE" -v heading="## v$next" -v date="Date: $today" '
    $0 ~ re { print "## Unreleased"; print ""; print heading; print date; next }
            { print }
' "$CHANGELOG" >"$tmp"
cat "$tmp" >"$CHANGELOG"
rm -f "$tmp"

git add pyproject.toml "$CHANGELOG"
git commit --quiet -m "chore: release v$next"

cat <<EOF

Committed "chore: release v$next" on $release_branch.

Next steps:
  1. Review the commit, and edit $CHANGELOG if needed (amend the commit):
       git show
  2. Push and open the release PR:
       git push -u $REMOTE $release_branch
       gh pr create --base $BASE_BRANCH --title "chore: release v$next" --body "Release v$next. See $CHANGELOG."
  3. After it is squash-merged, tag the merge commit and create the GitHub release:
       git switch $BASE_BRANCH && git pull --ff-only $REMOTE $BASE_BRANCH
       git tag v$next && git push $REMOTE v$next
       awk '/^## v$next\$/ {on=1; next} on && /^## / {exit} on' $CHANGELOG | gh release create v$next --title v$next --notes-file -
  4. Publish: GitHub -> Actions -> Release -> Run workflow, tag v$next, target pypi.
  5. Clean up: git branch -D $release_branch
EOF
