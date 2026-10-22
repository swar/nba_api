"""Endpoints the NBA API no longer serves warn when constructed."""

import pytest

from nba_api.stats import endpoints

REMOVED = [
    ("LeagueLeaders", {}),
    ("AssistLeaders", {}),
    ("AssistTracker", {}),
    ("PlayoffPicture", {}),
    ("BoxScoreAdvancedV2", {"game_id": "0022500001"}),
    ("BoxScoreFourFactorsV2", {"game_id": "0022500001"}),
    ("BoxScoreMiscV2", {"game_id": "0022500001"}),
    ("BoxScoreScoringV2", {"game_id": "0022500001"}),
    ("BoxScoreUsageV2", {"game_id": "0022500001"}),
    ("PlayByPlay", {"game_id": "0022500001"}),
]


@pytest.mark.parametrize(("name", "kwargs"), REMOVED)
def test_removed_endpoint_warns(name, kwargs):
    with pytest.warns(DeprecationWarning, match=f"^{name} is deprecated"):
        getattr(endpoints, name)(get_request=False, **kwargs)
