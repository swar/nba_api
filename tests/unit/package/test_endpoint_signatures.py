"""Pin the public constructor contract of every exported endpoint class.

Downstream code depends on endpoint class names, ``__init__`` parameter names,
order, kinds and defaults, and on the class attributes pre-set to ``None``.
``endpoint_signatures.json`` records all of that (plus ``endpoint`` /
``endpoint_url`` and the ``expected_data`` dataset names) for every class
exported from ``nba_api.stats.endpoints`` and ``nba_api.live.nba.endpoints``.

Date-derived defaults such as ``Season.default`` are stored by name, not value,
so the snapshot does not roll over in October (see ``endpoint_signatures.py``).

If a change to the snapshot is intentional, regenerate it and commit the diff::

    NBA_API_UPDATE_SNAPSHOTS=1 poetry run pytest tests/unit/package/test_endpoint_signatures.py
"""

import difflib
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).parent
SNAPSHOT_PATH = HERE / "endpoint_signatures.json"
UPDATE_COMMAND = (
    "NBA_API_UPDATE_SNAPSHOTS=1 poetry run pytest "
    "tests/unit/package/test_endpoint_signatures.py"
)


def _current_snapshot_text():
    # A fresh interpreter, so the builder can freeze datetime.now() before
    # nba_api.stats.library.parameters is imported.
    result = subprocess.run(
        [sys.executable, str(HERE / "endpoint_signatures.py")],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    return result.stdout


def _diff(expected, actual):
    lines = []
    for name in sorted(expected.keys() - actual.keys()):
        lines.append(f"removed class: {name}")
    for name in sorted(actual.keys() - expected.keys()):
        lines.append(f"added class: {name}")
    for name in sorted(expected.keys() & actual.keys()):
        if expected[name] != actual[name]:
            lines.extend(
                difflib.unified_diff(
                    json.dumps(expected[name], indent=2).splitlines(),
                    json.dumps(actual[name], indent=2).splitlines(),
                    fromfile=f"snapshot {name}",
                    tofile=f"current {name}",
                    lineterm="",
                )
            )
    return "\n".join(lines)


def test_endpoint_signatures_match_snapshot():
    current_text = _current_snapshot_text()
    if os.environ.get("NBA_API_UPDATE_SNAPSHOTS") == "1":
        SNAPSHOT_PATH.write_text(current_text)

    expected = json.loads(SNAPSHOT_PATH.read_text())
    actual = json.loads(current_text)
    if actual != expected:
        pytest.fail(
            "Public endpoint signatures changed:\n\n"
            f"{_diff(expected, actual)}\n\n"
            "Endpoint class, parameter and attribute names are a compatibility "
            "contract (see AGENTS.md). If this change is intentional, regenerate "
            f"the snapshot with\n    {UPDATE_COMMAND}\n"
            "and commit endpoint_signatures.json.",
            pytrace=False,
        )
    # Byte-for-byte too, so the committed file stays in canonical form.
    assert SNAPSHOT_PATH.read_text() == current_text, (
        f"endpoint_signatures.json is not canonically formatted; run {UPDATE_COMMAND}"
    )
