from importlib.metadata import version

import pytest

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


def test_version_can_be_imported_by_name():
    from nba_api import __version__

    assert __version__ == version("nba_api")


def test_unknown_attribute_raises_attribute_error():
    with pytest.raises(AttributeError, match="no attribute 'not_a_thing'"):
        nba_api.not_a_thing  # noqa: B018
