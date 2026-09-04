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

pytest.importorskip("mcp", reason="mcp extra not installed")


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


def test_get_default_season():
    from nba_api.mcp.server import _get_default_season

    season = _get_default_season()
    assert len(season) == 7
    assert "-" in season
    assert season[:4].isdigit()
    assert season[5:].isdigit()


@patch("nba_api.stats.endpoints.shotchartdetail.ShotChartDetail")
def test_get_shot_chart_actions_breakdown(mock_sc):
    import json

    from nba_api.mcp.server import get_shot_chart_actions

    df = pd.DataFrame(
        [
            {
                "PLAYER_NAME": "Ryan Rollins",
                "TEAM_NAME": "Milwaukee Bucks",
                "ACTION_TYPE": "Step Back Jump shot",
                "SHOT_TYPE": "3PT Field Goal",
                "SHOT_ATTEMPTED_FLAG": 1,
                "SHOT_MADE_FLAG": 1,
                "SHOT_DISTANCE": 26.0,
            },
            {
                "PLAYER_NAME": "Ryan Rollins",
                "TEAM_NAME": "Milwaukee Bucks",
                "ACTION_TYPE": "Step Back Jump shot",
                "SHOT_TYPE": "3PT Field Goal",
                "SHOT_ATTEMPTED_FLAG": 1,
                "SHOT_MADE_FLAG": 0,
                "SHOT_DISTANCE": 25.0,
            },
            {
                "PLAYER_NAME": "Ryan Rollins",
                "TEAM_NAME": "Milwaukee Bucks",
                "ACTION_TYPE": "Step Back Jump shot",
                "SHOT_TYPE": "2PT Field Goal",
                "SHOT_ATTEMPTED_FLAG": 1,
                "SHOT_MADE_FLAG": 1,
                "SHOT_DISTANCE": 18.0,
            },
        ]
    )
    mock_instance = MagicMock()
    mock_instance.get_data_frames.return_value = [df]
    mock_sc.return_value = mock_instance

    res = get_shot_chart_actions(
        player="Ryan Rollins", action_type="Step Back", min_fga=1
    )
    parsed = json.loads(res)
    assert len(parsed) == 1
    item = parsed[0]
    assert item["PLAYER_NAME"] == "Ryan Rollins"
    assert item["FGA"] == 3
    assert item["FGM"] == 2
    assert item["FG3A"] == 2
    assert item["FG3M"] == 1
    assert item["FG2A"] == 1
    assert item["FG2M"] == 1
    assert item["FG3_PCT"] == 0.5
    assert item["FG2_PCT"] == 1.0


@patch("nba_api.stats.endpoints.shotchartdetail.ShotChartDetail")
def test_get_shot_chart_actions_truncation_notice(mock_sc):
    import json

    from nba_api.mcp.server import get_shot_chart_actions

    # Simulate 100,000 row truncation for league-wide query
    dummy_row = {
        "PLAYER_NAME": "Player A",
        "TEAM_NAME": "Team A",
        "ACTION_TYPE": "Step Back Jump shot",
        "SHOT_TYPE": "3PT Field Goal",
        "SHOT_ATTEMPTED_FLAG": 1,
        "SHOT_MADE_FLAG": 1,
        "SHOT_DISTANCE": 26.0,
    }
    df = pd.DataFrame([dummy_row] * 100000)
    mock_instance = MagicMock()
    mock_instance.get_data_frames.return_value = [df]
    mock_sc.return_value = mock_instance

    res = get_shot_chart_actions(action_type="Step Back", min_fga=10)
    parsed = json.loads(res)
    assert "notice" in parsed
    assert "data" in parsed
    assert (
        "ShotChartDetail response reached maximum API payload limit" in parsed["notice"]
    )


def test_query_raw_endpoint_json_string_and_defaults():
    import json

    from nba_api.mcp.server import query_raw_endpoint

    # Nonexistent endpoint returns error json
    err_res = json.loads(query_raw_endpoint("NonExistentEndpoint123"))
    assert "error" in err_res

    # Test invalid json string params
    err_json = json.loads(query_raw_endpoint("CommonPlayerInfo", params="{bad-json"))
    assert "error" in err_json
