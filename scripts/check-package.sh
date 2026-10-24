#!/usr/bin/env bash
#
# Build the sdist and wheel, check their metadata with twine, then install the
# wheel into a clean virtualenv and import it from there. The test suite runs
# against the source tree, so this is the only check of what actually ships.
#
# Usage: scripts/check-package.sh [PYTHON]
#
# PYTHON is the interpreter for the throwaway virtualenv (default: whatever uv
# finds). It must satisfy requires-python. Nothing is written inside the repo.

set -euo pipefail

TWINE_VERSION="7.0.0"
PYTHON="${1:-}"

work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT

uv build --quiet --out-dir "$work/dist"

uv venv --quiet ${PYTHON:+--python "$PYTHON"} "$work/venv"
uv pip install --quiet --python "$work/venv/bin/python" \
    "twine==${TWINE_VERSION}" "$work"/dist/*.whl

"$work/venv/bin/twine" check --strict "$work"/dist/*

# -I and a cwd outside the repo, so nothing can be imported from src/.
cd "$work"
"$work/venv/bin/python" -I - <<'EOF'
import nba_api
from nba_api.live.nba.endpoints import boxscore, odds, playbyplay, scoreboard  # noqa: F401
from nba_api.stats import endpoints
from nba_api.stats.static import players, teams

assert "site-packages" in nba_api.__file__, nba_api.__file__

missing = [name for name in endpoints.__all__ if not hasattr(endpoints, name)]
assert not missing, f"in __all__ but not importable: {missing}"

assert players.find_players_by_full_name("LeBron James"), "static players data"
assert teams.find_team_by_abbreviation("BOS"), "static teams data"

endpoints.CommonPlayerInfo(player_id=2544, get_request=False)

print(f"nba_api {nba_api.__version__}: {len(endpoints.__all__)} endpoint modules OK")
EOF
