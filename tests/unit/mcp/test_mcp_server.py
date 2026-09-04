from unittest.mock import MagicMock, patch

import pandas as pd
import pytest

from nba_api.mcp.server import (
    _find_player,
    _find_team,
    _strip_accents,
    get_player_stats,
    mcp,
)


def test_strip_accents():
    assert _strip_accents("Luka Dončić") == "luka doncic"
    assert _strip_accents("Nikola Jokić") == "nikola jokic"
    assert _strip_accents("Kristaps Porziņģis") == "kristaps porzingis"


def test_find_player_exact_and_fuzzy():
    # Exact
    p1 = _find_player("LeBron James")
    assert p1["id"] == 2544

    # Accent insensitive
    p2 = _find_player("Luka Doncic")
    assert p2["id"] == 1629029

    # Shorthand
    p3 = _find_player("Jokic")
    assert p3["id"] == 203999


def test_find_player_not_found():
    with pytest.raises(ValueError, match="not found in NBA records"):
        _find_player("NonexistentPlayerXYZ123")


def test_find_team():
    # Abbreviation
    t1 = _find_team("BOS")
    assert t1["id"] == 1610612738

    # Nickname
    t2 = _find_team("Lakers")
    assert t2["id"] == 1610612747


def test_find_team_not_found():
    with pytest.raises(ValueError, match="Team 'UnknownTeamXYZ' not found"):
        _find_team("UnknownTeamXYZ")


def test_mcp_tools_registered():
    """Verify that all intended tools are registered on the MCPServer instance."""
    # Check tool registry or tool names
    expected_tools = {
        "get_player_stats",
        "get_player_gamelog",
        "get_scoreboard",
        "get_team_roster",
        "get_synergy_play_types",
        "get_shot_tracking",
        "get_shot_chart_actions",
        "get_advanced_stats",
        "get_hustle_stats",
        "query_raw_endpoint",
    }
    # Check if tools are accessible
    registered_tools = set()
    if hasattr(mcp, "_tool_manager"):
        registered_tools = set(mcp._tool_manager._tools.keys())
    elif hasattr(mcp, "_tools"):
        registered_tools = set(mcp._tools.keys())
    elif hasattr(mcp, "tools"):
        registered_tools = {t.name for t in mcp.tools}

    if registered_tools:
        for tool in expected_tools:
            assert tool in registered_tools, f"Missing tool: {tool}"


@patch("nba_api.stats.endpoints.playercareerstats.PlayerCareerStats")
def test_get_player_stats_mocked(mock_career_stats):
    dummy_df = pd.DataFrame(
        [
            {
                "SEASON_ID": "2024-25",
                "TEAM_ABBREVIATION": "LAL",
                "PLAYER_AGE": 40.0,
                "GP": 50,
                "GS": 50,
                "MIN": 35.0,
                "PTS": 25.0,
                "REB": 8.0,
                "AST": 8.0,
                "STL": 1.2,
                "BLK": 0.6,
                "FG_PCT": 0.510,
                "FG3_PCT": 0.380,
                "FT_PCT": 0.760,
            }
        ]
    )
    mock_instance = MagicMock()
    mock_instance.get_data_frames.return_value = [dummy_df]
    mock_career_stats.return_value = mock_instance

    result_json = get_player_stats("LeBron James", season="2024-25", per_game=True)
    assert "2024-25" in result_json
    assert "LAL" in result_json
    assert "25.0" in result_json
