"""Endpoints that accept the NBA Cup ISTRound filter."""

import inspect

import pytest

from nba_api.stats import endpoints
from nba_api.stats.library.parameters import ISTRound

IST_ROUND_ENDPOINTS = [
    "LeagueDashLineups",
    "LeagueDashPlayerBioStats",
    "LeagueDashPlayerClutch",
    "LeagueDashPlayerPtShot",
    "LeagueDashPlayerShotLocations",
    "LeagueDashPlayerStats",
    "LeagueDashPtDefend",
    "LeagueDashPtStats",
    "LeagueDashPtTeamDefend",
    "LeagueDashTeamClutch",
    "LeagueDashTeamPtShot",
    "LeagueDashTeamShotLocations",
    "LeagueDashTeamStats",
    "LeagueHustleStatsPlayer",
    "LeagueHustleStatsTeam",
    "LeaguePlayerOnDetails",
    "PlayerDashboardByClutch",
    "PlayerDashboardByGameSplits",
    "PlayerDashboardByGeneralSplits",
    "PlayerDashboardByLastNGames",
    "PlayerDashboardByShootingSplits",
    "PlayerDashboardByTeamPerformance",
    "PlayerDashPtPass",
    "PlayerDashPtReb",
    "PlayerDashPtShotDefend",
    "ShotChartDetail",
    "TeamDashboardByGeneralSplits",
    "TeamDashboardByShootingSplits",
    "TeamDashLineups",
    "TeamDashPtReb",
    "TeamPlayerDashboard",
    "TeamPlayerOnOffDetails",
    "TeamPlayerOnOffSummary",
    "VideoDetailsAsset",
]


def _build(name, **kwargs):
    cls = getattr(endpoints, name)
    required = {
        p.name: "0"
        for p in inspect.signature(cls).parameters.values()
        if p.default is inspect.Parameter.empty
    }
    return cls(**required, **kwargs, get_request=False)


@pytest.mark.parametrize("name", IST_ROUND_ENDPOINTS)
def test_ist_round_is_omitted_by_default(name):
    # None keeps ISTRound out of the query string, so existing requests are unchanged.
    assert _build(name).parameters["ISTRound"] is None


@pytest.mark.parametrize("name", IST_ROUND_ENDPOINTS)
def test_ist_round_is_sent_when_set(name):
    endpoint = _build(name, ist_round_nullable=ISTRound.knockout)
    assert endpoint.parameters["ISTRound"] == "Knockout"
