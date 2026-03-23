from importlib.metadata import version

import nba_api


def test_version_exists():
    assert hasattr(nba_api, "__version__")


def test_version_format():
    assert isinstance(nba_api.__version__, str)
    parts = nba_api.__version__.split(".")
    assert len(parts) >= 2
    for part in parts:
        assert part.isdigit()


def test_version_matches_metadata():
    assert nba_api.__version__ == version("nba_api")
