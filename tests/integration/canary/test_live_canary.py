"""Pre-release canary: a few real requests to stats.nba.com and cdn.nba.com.

Every test here goes through the proxy in ``NBA_API_PROXY`` and fails closed:
``NBA_API_REQUIRE_PROXY`` is forced on, so a missing proxy raises before any
socket opens instead of falling back to a direct connection. Locally the tests
skip when no proxy is configured; on GitHub Actions they fail instead, so a
missing secret can't pass silently.

Run with: ``uv run pytest tests/integration/canary -m canary``
Never combine with ``--block-network`` (these are real requests).
"""

import os

import pytest

import nba_api.live.nba.endpoints as live_ep
import nba_api.stats.endpoints as stats_ep

from ..helpers.constants import PLAYER_ID

pytestmark = [pytest.mark.live, pytest.mark.canary]


@pytest.fixture(autouse=True)
def require_proxy(monkeypatch):
    if not os.environ.get("NBA_API_PROXY") and not os.environ.get("GITHUB_ACTIONS"):
        pytest.skip("NBA_API_PROXY is not set; canary tests always go through a proxy")
    monkeypatch.setenv("NBA_API_REQUIRE_PROXY", "1")


def assert_valid(endpoint):
    assert endpoint.nba_response.valid_json()
    return endpoint


def test_stats_common_player_info():
    endpoint = assert_valid(stats_ep.CommonPlayerInfo(player_id=PLAYER_ID))
    assert endpoint.common_player_info.get_dict()["data"]


def test_stats_common_team_years():
    endpoint = assert_valid(stats_ep.CommonTeamYears())
    assert endpoint.team_years.get_dict()["data"]


def test_stats_league_standings_v3():
    endpoint = assert_valid(stats_ep.LeagueStandingsV3())
    assert endpoint.get_available_data()


def test_live_scoreboard():
    endpoint = assert_valid(live_ep.scoreboard.ScoreBoard())
    assert endpoint.score_board_date


def test_live_odds():
    # Valid JSON only: the odds feed can legitimately be empty on off days.
    assert_valid(live_ep.odds.Odds())
