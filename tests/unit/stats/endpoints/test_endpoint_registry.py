"""Every stats endpoint module is exported and documented.

Catches an endpoint added to one place but not the others listed under
"Adding an endpoint touches" in AGENTS.md.
"""

import re
from pathlib import Path

import pytest

import nba_api.stats.endpoints as endpoints
from nba_api.stats.endpoints._base import Endpoint

REPO_ROOT = Path(__file__).resolve().parents[4]
ENDPOINTS_DIR = REPO_ROOT / "src" / "nba_api" / "stats" / "endpoints"
DOCS_DIR = REPO_ROOT / "docs" / "nba_api" / "stats" / "endpoints"
TABLE_OF_CONTENTS = REPO_ROOT / "docs" / "table_of_contents.md"
ENDPOINT_GUIDE = REPO_ROOT / "docs" / "nba_api" / "stats" / "endpoint_guide.md"

MODULES = sorted(
    path.stem for path in ENDPOINTS_DIR.glob("*.py") if not path.stem.startswith("_")
)
EXPORTED_CLASSES = {
    obj
    for name, obj in vars(endpoints).items()
    if isinstance(obj, type) and issubclass(obj, Endpoint) and obj is not Endpoint
}


@pytest.mark.parametrize("module", MODULES)
def test_module_is_in_all(module):
    assert module in endpoints.__all__


@pytest.mark.parametrize("module", MODULES)
def test_module_class_is_exported(module):
    assert any(cls.__module__.endswith(f".{module}") for cls in EXPORTED_CLASSES)


@pytest.mark.parametrize("module", MODULES)
def test_module_has_doc(module):
    assert (DOCS_DIR / f"{module}.md").is_file()


def test_table_of_contents_lists_every_endpoint():
    toc = TABLE_OF_CONTENTS.read_text(encoding="utf-8")
    linked = set(re.findall(r"\(nba_api/stats/endpoints/(\w+)\.md\)", toc))
    assert linked == set(MODULES)

    count = re.search(r"Endpoints \((\d+)\)", toc)
    assert count is not None
    assert int(count.group(1)) == len(MODULES)


def test_endpoint_guide_lists_every_endpoint():
    guide = ENDPOINT_GUIDE.read_text(encoding="utf-8")
    linked = set(re.findall(r"\(endpoints/(\w+)\.md\)", guide))
    assert linked == set(MODULES)
