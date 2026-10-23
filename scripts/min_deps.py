"""Print the lowest versions pyproject.toml allows for the running Python.

One pin per runtime dependency whose marker matches this interpreter, taken from
its ">=" (or "==" / "~=") bound, e.g. "numpy==1.26.0". CI installs these over
the locked versions to test the floors the package promises.

Usage: poetry run python scripts/min_deps.py
"""

import sys
from pathlib import Path

from packaging.requirements import Requirement

if sys.version_info >= (3, 11):
    import tomllib
else:
    import tomli as tomllib

PYPROJECT = Path(__file__).resolve().parents[1] / "pyproject.toml"


def floors():
    project = tomllib.loads(PYPROJECT.read_text())["project"]
    for dependency in project["dependencies"]:
        requirement = Requirement(dependency)
        if requirement.marker and not requirement.marker.evaluate():
            continue
        lower = [
            spec.version
            for spec in requirement.specifier
            if spec.operator in (">=", "==", "~=")
        ]
        if not lower:
            sys.exit(f"{dependency!r} has no lower bound")
        yield f"{requirement.name}=={lower[0]}"


if __name__ == "__main__":
    print("\n".join(floors()))
