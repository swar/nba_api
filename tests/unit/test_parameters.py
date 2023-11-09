from nba_api.stats.library.parameters import Season
import re


def test_season():
    assert re.search(r"^\d{4}-\d{2}$", Season.default) is not None
