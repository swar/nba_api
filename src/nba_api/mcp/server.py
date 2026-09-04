"""Model Context Protocol (MCP) server for nba_api.

Exposes NBA stats, player profiles, game logs, scoreboards, Synergy play types,
Second Spectrum tracking, shot charts, advanced analytics, and hustle stats as
callable tools for LLMs and AI agents (Cursor, Claude Desktop, Antigravity, Factory Droid).
"""

import datetime
import importlib
import inspect
import json
import time
import unicodedata
from collections.abc import Callable
from typing import Any

import requests

from nba_api.stats.static import players, teams

try:
    try:
        from mcp.server.mcpserver import MCPServer as _ServerClass
    except ImportError:
        from mcp.server.fastmcp import FastMCP as _ServerClass
except ImportError:
    _ServerClass = None

if _ServerClass is None:
    raise ImportError(
        "The MCP server requires the 'mcp' extra. Install it with: pip install 'nba-api[mcp]'"
    )

_description = (
    "Official NBA API Model Context Protocol server for player statistics, "
    "game logs, scoreboards, Synergy play types, Second Spectrum shot tracking, "
    "shot mechanics, and advanced analytics."
)
try:
    mcp = _ServerClass("nba-api", description=_description)
except TypeError:
    try:
        mcp = _ServerClass("nba-api", instructions=_description)
    except TypeError:
        mcp = _ServerClass("nba-api")

DEFAULT_TIMEOUT = 45


def _get_default_season() -> str:
    """Calculate the current active or most recently completed NBA season string."""
    today = datetime.date.today()
    if today.month >= 10:
        return f"{today.year}-{str(today.year + 1)[-2:]}"
    return f"{today.year - 1}-{str(today.year)[-2:]}"


PLAY_TYPE_MAP: dict[str, str] = {
    "prballhandler": "PRBallHandler",
    "pr_ball_handler": "PRBallHandler",
    "pnr_handler": "PRBallHandler",
    "pnr": "PRBallHandler",
    "isolation": "Isolation",
    "iso": "Isolation",
    "spotup": "Spotup",
    "spot_up": "Spotup",
    "postup": "Postup",
    "post_up": "Postup",
    "post": "Postup",
    "transition": "Transition",
    "offscreen": "OffScreen",
    "off_screen": "OffScreen",
    "handoff": "Handoff",
    "hand_off": "Handoff",
    "cut": "Cut",
    "prrollman": "PRRollman",
    "pr_roll_man": "PRRollman",
    "roll_man": "PRRollman",
    "roller": "PRRollman",
    "offrebound": "OffRebound",
    "putback": "OffRebound",
    "misc": "Misc",
}


def _call_with_retry(
    func: Callable[..., Any], max_retries: int = 2, *args: Any, **kwargs: Any
) -> Any:
    """Execute an nba_api call with automatic retry on read timeouts or connection issues."""
    last_err = None
    for attempt in range(1, max_retries + 1):
        try:
            return func(*args, **kwargs)
        except (
            requests.exceptions.ReadTimeout,
            requests.exceptions.ConnectionError,
        ) as err:
            last_err = err
            if attempt < max_retries:
                time.sleep(1.5)
                continue
            raise
        except Exception:
            raise
    raise last_err if last_err else RuntimeError("Failed after retries")


def _strip_accents(text: str) -> str:
    """Normalize and strip diacritics/accents from text for reliable searching."""
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c)).lower().strip()


def _find_player(name_query: str) -> dict[str, Any]:
    """Find a player by name (accent-insensitive, exact or fuzzy)."""
    all_players = players.get_players()
    q_norm = _strip_accents(name_query)

    exact = [p for p in all_players if _strip_accents(p["full_name"]) == q_norm]
    if exact:
        return exact[0]

    matches = [p for p in all_players if q_norm in _strip_accents(p["full_name"])]
    if matches:
        active = [p for p in matches if p.get("is_active")]
        return active[0] if active else matches[0]

    word_matches = [
        p
        for p in all_players
        if any(q_norm == _strip_accents(part) for part in p["full_name"].split())
    ]
    if word_matches:
        active = [p for p in word_matches if p.get("is_active")]
        return active[0] if active else word_matches[0]

    raise ValueError(f"Player '{name_query}' not found in NBA records.")


def _find_team(team_query: str) -> dict[str, Any]:
    """Find an NBA team by name, city, nickname, or abbreviation."""
    all_teams = teams.get_teams()
    q = team_query.strip().lower()

    abbr_match = [t for t in all_teams if t["abbreviation"].lower() == q]
    if abbr_match:
        return abbr_match[0]

    matches = [
        t
        for t in all_teams
        if q in t["full_name"].lower()
        or q in t["nickname"].lower()
        or q in t["city"].lower()
    ]
    if matches:
        return matches[0]

    raise ValueError(f"Team '{team_query}' not found.")


@mcp.tool()
def get_player_stats(
    player: str, season: str | None = None, per_game: bool = True
) -> str:
    """Get NBA regular season or career statistics for a player.

    Args:
        player: Player name (e.g., 'LeBron James', 'Stephen Curry', 'Luka Doncic')
        season: Season ID (e.g., '2025-26'), 'career' for all seasons, or None for current season
        per_game: Whether to return per-game averages (True) or season totals (False)
    """
    from nba_api.stats.endpoints import playercareerstats

    p = _find_player(player)
    per_mode = "PerGame" if per_game else "Totals"
    call = _call_with_retry(
        playercareerstats.PlayerCareerStats,
        player_id=p["id"],
        per_mode36=per_mode,
        timeout=DEFAULT_TIMEOUT,
    )
    df = call.get_data_frames()[0]
    if season and season.strip().lower() in ["career", "all"]:
        pass
    else:
        target_season = season.strip() if season else _get_default_season()
        df = df[df["SEASON_ID"] == target_season]

    cols = [
        "SEASON_ID",
        "TEAM_ABBREVIATION",
        "PLAYER_AGE",
        "GP",
        "GS",
        "MIN",
        "PTS",
        "REB",
        "AST",
        "STL",
        "BLK",
        "FG_PCT",
        "FG3_PCT",
        "FT_PCT",
    ]
    avail = [c for c in cols if c in df.columns]
    return df[avail].to_json(orient="records", indent=2)


@mcp.tool()
def get_player_gamelog(player: str, season: str | None = None, last_n: int = 10) -> str:
    """Get recent game-by-game box scores for a player.

    Args:
        player: Player name
        season: Season ID (default: current season, e.g. '2025-26')
        last_n: Number of recent games to return (default: 10)
    """
    from nba_api.stats.endpoints import playergamelog

    season = season or _get_default_season()
    p = _find_player(player)
    log = _call_with_retry(
        playergamelog.PlayerGameLog,
        player_id=p["id"],
        season=season,
        timeout=DEFAULT_TIMEOUT,
    )
    df = log.get_data_frames()[0]
    if last_n > 0:
        df = df.head(last_n)

    cols = [
        "GAME_DATE",
        "MATCHUP",
        "WL",
        "MIN",
        "PTS",
        "REB",
        "AST",
        "STL",
        "BLK",
        "FGM",
        "FGA",
        "FG_PCT",
        "FG3M",
        "FG3A",
        "FTM",
        "PLUS_MINUS",
    ]
    avail = [c for c in cols if c in df.columns]
    return df[avail].to_json(orient="records", indent=2)


@mcp.tool()
def get_scoreboard(date: str | None = None) -> str:
    """Get NBA game scoreboard, live/final scores, series notes, and game status.

    Args:
        date: Date in YYYY-MM-DD format (default: today)
    """
    from nba_api.stats.endpoints import scoreboardv3

    game_date = date or datetime.datetime.now().strftime("%Y-%m-%d")
    sb = _call_with_retry(
        scoreboardv3.ScoreboardV3,
        game_date=game_date,
        timeout=DEFAULT_TIMEOUT,
    )
    frames = sb.get_data_frames()
    if len(frames) < 3 or frames[1].empty:
        return json.dumps([])

    game_summary = frames[1]
    team_scores = frames[2]

    summary_rows = []
    for _, game in game_summary.iterrows():
        gid = game["gameId"]
        status = str(game.get("gameStatusText", "")).strip()
        teams_match = team_scores[team_scores["gameId"] == gid]
        if len(teams_match) >= 2:
            t1, t2 = teams_match.iloc[0], teams_match.iloc[1]
            summary_rows.append(
                {
                    "game_id": gid,
                    "status": status,
                    "away_team": t2["teamTricode"],
                    "away_pts": int(t2["score"]),
                    "home_team": t1["teamTricode"],
                    "home_pts": int(t1["score"]),
                    "series_note": game.get("seriesText", "")
                    or game.get("gameSubLabel", ""),
                }
            )
    return json.dumps(summary_rows, indent=2)


@mcp.tool()
def get_team_roster(team: str, season: str | None = None) -> str:
    """Get active team roster, player positions, numbers, and person IDs.

    Args:
        team: Team name, city, or abbreviation (e.g. 'Celtics', 'BOS', 'Warriors')
        season: Season ID (default: current season, e.g. '2025-26')
    """
    from nba_api.stats.endpoints import commonteamroster

    season = season or _get_default_season()
    t = _find_team(team)
    roster = _call_with_retry(
        commonteamroster.CommonTeamRoster,
        team_id=t["id"],
        season=season,
        timeout=DEFAULT_TIMEOUT,
    )
    df = roster.get_data_frames()[0]
    cols = [
        "PLAYER",
        "NUM",
        "POSITION",
        "HEIGHT",
        "WEIGHT",
        "AGE",
        "EXP",
        "PLAYER_ID",
    ]
    avail = [c for c in cols if c in df.columns]
    return df[avail].to_json(orient="records", indent=2)


@mcp.tool()
def get_synergy_play_types(
    play_type: str = "PRBallHandler",
    player: str | None = None,
    team: str | None = None,
    grouping: str = "offensive",
    season: str | None = None,
    min_poss: int = 20,
    top_n: int = 15,
) -> str:
    """Query Synergy play types (P&R, Isolation, Postup, Spotup, Transition, etc.).

    Args:
        play_type: One of PRBallHandler, Isolation, Spotup, Postup, Transition,
                   OffScreen, Handoff, Cut, PRRollman, OffRebound
        player: Filter by player name (optional)
        team: Filter by team name or abbreviation (optional)
        grouping: 'offensive' or 'defensive'
        season: Season ID (default: current season, e.g. '2025-26')
        min_poss: Minimum possessions threshold (default: 20)
        top_n: Number of top entries to return (default: 15)
    """
    from nba_api.stats.endpoints import synergyplaytypes

    season = season or _get_default_season()

    pt = PLAY_TYPE_MAP.get(play_type.lower(), play_type)
    player_or_team = "T" if (team and not player) else "P"

    s = _call_with_retry(
        synergyplaytypes.SynergyPlayTypes,
        player_or_team_abbreviation=player_or_team,
        play_type_nullable=pt,
        type_grouping_nullable=grouping.lower(),
        season=season,
        timeout=DEFAULT_TIMEOUT,
    )
    df = s.get_data_frames()[0]

    if player:
        p_norm = _strip_accents(_find_player(player)["full_name"])
        df = df[df["PLAYER_NAME"].apply(lambda n: _strip_accents(str(n)) == p_norm)]
    elif team:
        t = _find_team(team)
        df = df[
            (df["TEAM_ID"] == t["id"]) | (df["TEAM_ABBREVIATION"] == t["abbreviation"])
        ]

    if "POSS" in df.columns:
        df = df[df["POSS"] >= min_poss]

    sort_col = "PPP" if "PPP" in df.columns else "POSS"
    df = df.sort_values(by=sort_col, ascending=False)
    if top_n > 0:
        df = df.head(top_n)

    cols = [
        "PLAYER_NAME" if player_or_team == "P" else "TEAM_NAME",
        "TEAM_ABBREVIATION",
        "PLAY_TYPE",
        "GP",
        "POSS",
        "PTS",
        "PPP",
        "PERCENTILE",
        "FG_PCT",
        "EFG_PCT",
        "TOV_POSS_PCT",
        "SCORE_POSS_PCT",
    ]
    avail = [c for c in cols if c in df.columns]
    return df[avail].to_json(orient="records", indent=2)


@mcp.tool()
def get_shot_tracking(
    player: str | None = None,
    split: str = "general",
    general_range: str = "Pullups",
    dribbles: str | None = None,
    defender_dist: str | None = None,
    min_fga: int = 30,
    sort_by: str = "FGA",
    season: str | None = None,
    top_n: int = 15,
) -> str:
    """Query Second Spectrum tracking (Pullups, Catch & Shoot, Dribble counts, Defender proximity).

    Use this tool for official, full-season Second Spectrum league-wide tracking leaderboards
    (Pullups, Catch and Shoot, Defender distance) which cover the entire season without truncation.

    Args:
        player: Player name for individual tracking breakdown (optional)
        split: When player is specified: 'general', 'dribbles', 'defense', 'touch', 'shotclock'
        general_range: When league-wide: 'Pullups', 'Catch and Shoot', 'Less than 10ft'
        dribbles: '0 Dribbles', '1 Dribble', '2 Dribbles', '3-6 Dribbles', '7+ Dribbles'
        defender_dist: '0-2 Feet - Very Tight', '2-4 Feet - Tight', '4-6 Feet - Open', '6+ Feet - Wide Open'
        min_fga: Minimum field goal attempts threshold (default: 30)
        sort_by: Metric column to sort by when league-wide, e.g. 'FGA', 'FG3_PCT', 'EFG_PCT' (default: 'FGA')
        season: Season ID (default: current season, e.g. '2025-26')
        top_n: Number of top entries to return (default: 15)
    """
    season = season or _get_default_season()
    if player:
        from nba_api.stats.endpoints import playerdashptshots

        p = _find_player(player)
        pt = _call_with_retry(
            playerdashptshots.PlayerDashPtShots,
            team_id=0,
            player_id=p["id"],
            season=season,
            timeout=DEFAULT_TIMEOUT,
        )
        frames = pt.get_data_frames()
        dataset_map = {
            "general": 1,
            "shotclock": 2,
            "dribbles": 3,
            "defense": 4,
            "touch": 6,
        }
        idx = dataset_map.get(split.lower(), 1)
        df = frames[idx]
        first_cols = [
            c
            for c in [
                "SHOT_TYPE",
                "SHOT_CLOCK_RANGE",
                "DRIBBLE_RANGE",
                "CLOSE_DEF_DIST_RANGE",
                "TOUCH_TIME_RANGE",
            ]
            if c in df.columns
        ]
        other_cols = [
            "FGA_FREQUENCY",
            "FGM",
            "FGA",
            "FG_PCT",
            "EFG_PCT",
            "FG2A",
            "FG2_PCT",
            "FG3A",
            "FG3_PCT",
        ]
        ordered = first_cols + [c for c in other_cols if c in df.columns]
        return df[ordered].to_json(orient="records", indent=2)

    from nba_api.stats.endpoints import leaguedashplayerptshot

    league_pt = _call_with_retry(
        leaguedashplayerptshot.LeagueDashPlayerPtShot,
        season=season,
        general_range_nullable=general_range or "",
        dribble_range_nullable=dribbles or "",
        close_def_dist_range_nullable=defender_dist or "",
        timeout=DEFAULT_TIMEOUT,
    )
    df = league_pt.get_data_frames()[0]
    if "FGA" in df.columns:
        df = df[df["FGA"] >= min_fga]
    sort_col = sort_by if sort_by in df.columns else "FGA"
    df = df.sort_values(by=sort_col, ascending=False)
    if top_n > 0:
        df = df.head(top_n)

    cols = [
        "PLAYER_NAME",
        "PLAYER_LAST_TEAM_ABBREVIATION",
        "GP",
        "FGA",
        "FGM",
        "FG_PCT",
        "EFG_PCT",
        "FG2A",
        "FG2_PCT",
        "FG3A",
        "FG3_PCT",
        "FGA_FREQUENCY",
    ]
    avail = [c for c in cols if c in df.columns]
    return df[avail].to_json(orient="records", indent=2)


@mcp.tool()
def get_shot_chart_actions(
    player: str | None = None,
    action_type: str | None = None,
    shot_type: str | None = None,
    min_fga: int = 10,
    season: str | None = None,
    top_n: int = 15,
) -> str:
    """Analyze shooting mechanics and action types (Step Back, Fadeaway, Pullup, Floater, etc.).

    NOTE: NBA.com's ShotChartDetail endpoint truncates league-wide queries (player=None)
    at 102,400 shots (~mid-season). For exact full-season stats of a specific player, always
    specify player='<Name>'. For un-truncated full-season league-wide pullup and catch-and-shoot
    leaderboards, use get_shot_tracking.

    Args:
        player: Player name (optional, recommended for complete full-season player stats)
        action_type: Action mechanic filter (e.g. 'Step Back', 'Fadeaway', 'Pullup', 'Floating')
        shot_type: '2pt', '3pt', or None
        min_fga: Minimum attempts threshold (default: 10)
        season: Season ID (default: current season, e.g. '2025-26')
        top_n: Number of top entries to return (default: 15)
    """
    from nba_api.stats.endpoints import shotchartdetail

    season = season or _get_default_season()
    player_id = _find_player(player)["id"] if player else 0

    sc = _call_with_retry(
        shotchartdetail.ShotChartDetail,
        team_id=0,
        player_id=player_id,
        context_measure_simple="FGA",
        season_nullable=season,
        timeout=DEFAULT_TIMEOUT,
    )
    df = sc.get_data_frames()[0]
    if df.empty:
        return json.dumps([])

    raw_count = len(df)
    is_truncated = raw_count >= 100000 and not player

    if shot_type:
        st = shot_type.strip().lower()
        if st in ["2pt", "2", "2p"]:
            df = df[df["SHOT_TYPE"] == "2PT Field Goal"]
        elif st in ["3pt", "3", "3p"]:
            df = df[df["SHOT_TYPE"] == "3PT Field Goal"]

    if action_type:
        term = action_type.strip().lower()
        df = df[df["ACTION_TYPE"].str.lower().str.contains(term, na=False)]

    if df.empty:
        return json.dumps([])

    if player and not action_type:
        # Full action repertoire for player
        grouped = (
            df.groupby("ACTION_TYPE")
            .agg(
                FGA=("SHOT_ATTEMPTED_FLAG", "count"),
                FGM=("SHOT_MADE_FLAG", "sum"),
                FG3A=("SHOT_TYPE", lambda s: (s == "3PT Field Goal").sum()),
                FG3M=(
                    "SHOT_TYPE",
                    lambda s: (
                        (s == "3PT Field Goal")
                        & (df.loc[s.index, "SHOT_MADE_FLAG"] == 1)
                    ).sum(),
                ),
                AVG_DIST=("SHOT_DISTANCE", "mean"),
            )
            .reset_index()
        )
        grouped["FG2A"] = grouped["FGA"] - grouped["FG3A"]
        grouped["FG2M"] = grouped["FGM"] - grouped["FG3M"]
        grouped["FG_PCT"] = (grouped["FGM"] / grouped["FGA"]).round(3)
        grouped["FG2_PCT"] = (
            grouped["FG2M"] / grouped["FG2A"].replace(0, float("nan"))
        ).round(3)
        grouped["FG3_PCT"] = (
            grouped["FG3M"] / grouped["FG3A"].replace(0, float("nan"))
        ).round(3)
        grouped["EFG_PCT"] = (
            (grouped["FGM"] + 0.5 * grouped["FG3M"]) / grouped["FGA"]
        ).round(3)
        grouped["AVG_DIST"] = grouped["AVG_DIST"].round(1)
        grouped = grouped[grouped["FGA"] >= min_fga].sort_values(
            by="FGA", ascending=False
        )
        if top_n > 0:
            grouped = grouped.head(top_n)
        return grouped.to_json(orient="records", indent=2)

    # League or player-filtered leaderboard
    grouped = (
        df.groupby(["PLAYER_NAME", "TEAM_NAME"])
        .agg(
            FGA=("SHOT_ATTEMPTED_FLAG", "count"),
            FGM=("SHOT_MADE_FLAG", "sum"),
            FG3A=("SHOT_TYPE", lambda s: (s == "3PT Field Goal").sum()),
            FG3M=(
                "SHOT_TYPE",
                lambda s: (
                    (s == "3PT Field Goal") & (df.loc[s.index, "SHOT_MADE_FLAG"] == 1)
                ).sum(),
            ),
            AVG_DIST=("SHOT_DISTANCE", "mean"),
        )
        .reset_index()
    )
    grouped["FG2A"] = grouped["FGA"] - grouped["FG3A"]
    grouped["FG2M"] = grouped["FGM"] - grouped["FG3M"]
    grouped["FG_PCT"] = (grouped["FGM"] / grouped["FGA"]).round(3)
    grouped["FG2_PCT"] = (
        grouped["FG2M"] / grouped["FG2A"].replace(0, float("nan"))
    ).round(3)
    grouped["FG3_PCT"] = (
        grouped["FG3M"] / grouped["FG3A"].replace(0, float("nan"))
    ).round(3)
    grouped["EFG_PCT"] = (
        (grouped["FGM"] + 0.5 * grouped["FG3M"]) / grouped["FGA"]
    ).round(3)
    grouped["AVG_DIST"] = grouped["AVG_DIST"].round(1)
    grouped = grouped[grouped["FGA"] >= min_fga].sort_values(by="FGA", ascending=False)
    if top_n > 0:
        grouped = grouped.head(top_n)

    records = json.loads(grouped.to_json(orient="records"))
    if is_truncated:
        return json.dumps(
            {
                "notice": (
                    f"NBA.com ShotChartDetail response reached maximum API payload limit "
                    f"({raw_count} shots) and cuts off around mid-season for league-wide queries. "
                    f"To obtain 100% complete full-season shot chart data for a specific player, "
                    f"re-run with player='<Player Name>'. For un-truncated full-season pull-up "
                    f"or catch-and-shoot leaderboards across the entire league, use get_shot_tracking."
                ),
                "data": records,
            },
            indent=2,
        )
    return json.dumps(records, indent=2)


@mcp.tool()
def get_advanced_stats(
    player: str | None = None,
    team: str | None = None,
    min_minutes: int = 500,
    sort_by: str = "TS_PCT",
    season: str | None = None,
    top_n: int = 15,
) -> str:
    """Query advanced metrics: True Shooting % (TS%), Usage Rate (USG%), Net Rating, PIE.

    Args:
        player: Filter by player name (optional)
        team: Filter by team name or abbreviation (optional)
        min_minutes: Minimum total minutes (if > 50) or minutes per game (if <= 50)
        sort_by: Column to sort by (e.g. 'TS_PCT', 'USG_PCT', 'NET_RATING', 'PIE')
        season: Season ID (default: current season, e.g. '2025-26')
        top_n: Number of top entries to return (default: 15)
    """
    from nba_api.stats.endpoints import leaguedashplayerstats

    season = season or _get_default_season()
    adv = _call_with_retry(
        leaguedashplayerstats.LeagueDashPlayerStats,
        measure_type_detailed_defense="Advanced",
        per_mode_detailed="PerGame",
        season=season,
        timeout=DEFAULT_TIMEOUT,
    )
    df = adv.get_data_frames()[0]

    if player:
        p_norm = _strip_accents(_find_player(player)["full_name"])
        df = df[df["PLAYER_NAME"].apply(lambda n: _strip_accents(str(n)) == p_norm)]
    elif team:
        t = _find_team(team)
        df = df[
            (df["TEAM_ID"] == t["id"]) | (df["TEAM_ABBREVIATION"] == t["abbreviation"])
        ]

    if "MIN" in df.columns:
        if min_minutes > 50:
            gp = df["GP"] if "GP" in df.columns else 1
            df = df[(df["MIN"] * gp) >= min_minutes]
        else:
            df = df[df["MIN"] >= min_minutes]

    sort_col = sort_by if sort_by in df.columns else "TS_PCT"
    df = df.sort_values(by=sort_col, ascending=False)
    if top_n > 0:
        df = df.head(top_n)

    cols = [
        "PLAYER_NAME",
        "TEAM_ABBREVIATION",
        "GP",
        "MIN",
        "OFF_RATING",
        "DEF_RATING",
        "NET_RATING",
        "AST_PCT",
        "REB_PCT",
        "TS_PCT",
        "EFG_PCT",
        "USG_PCT",
        "PACE",
        "PIE",
    ]
    avail = [c for c in cols if c in df.columns]
    return df[avail].to_json(orient="records", indent=2)


@mcp.tool()
def get_hustle_stats(
    player: str | None = None,
    team: str | None = None,
    min_minutes: int = 15,
    sort_by: str = "DEFLECTIONS",
    season: str | None = None,
    top_n: int = 15,
) -> str:
    """Query NBA Hustle stats (Deflections, Charges Drawn, Screen Assists, Contested Shots).

    Args:
        player: Filter by player name (optional)
        team: Filter by team name or abbreviation (optional)
        min_minutes: Minimum minutes per game (if <= 50) or total minutes (if > 50)
        sort_by: Column to sort by (e.g. 'DEFLECTIONS', 'CHARGES_DRAWN', 'SCREEN_ASSISTS')
        season: Season ID (default: current season, e.g. '2025-26')
        top_n: Number of top entries to return (default: 15)
    """
    from nba_api.stats.endpoints import leaguehustlestatsplayer

    season = season or _get_default_season()
    hustle = _call_with_retry(
        leaguehustlestatsplayer.LeagueHustleStatsPlayer,
        per_mode_time="PerGame",
        season=season,
        timeout=DEFAULT_TIMEOUT,
    )
    df = hustle.get_data_frames()[0]

    if player:
        p_norm = _strip_accents(_find_player(player)["full_name"])
        df = df[df["PLAYER_NAME"].apply(lambda n: _strip_accents(str(n)) == p_norm)]
    elif team:
        t = _find_team(team)
        df = df[
            (df["TEAM_ID"] == t["id"]) | (df["TEAM_ABBREVIATION"] == t["abbreviation"])
        ]

    if "MIN" in df.columns:
        if min_minutes > 50:
            gp = df["G"] if "G" in df.columns else 1
            df = df[(df["MIN"] * gp) >= min_minutes]
        else:
            df = df[df["MIN"] >= min_minutes]

    sort_col = sort_by if sort_by in df.columns else "DEFLECTIONS"
    df = df.sort_values(by=sort_col, ascending=False)
    if top_n > 0:
        df = df.head(top_n)

    cols = [
        "PLAYER_NAME",
        "TEAM_ABBREVIATION",
        "MIN",
        "CONTESTED_SHOTS",
        "DEFLECTIONS",
        "CHARGES_DRAWN",
        "SCREEN_ASSISTS",
        "SCREEN_AST_PTS",
        "LOOSE_BALLS_RECOVERED",
    ]
    avail = [c for c in cols if c in df.columns]
    return df[avail].to_json(orient="records", indent=2)


@mcp.tool()
def query_raw_endpoint(
    endpoint_name: str,
    params: dict[str, Any] | str | None = None,
    dataset_index: int = 0,
) -> str:
    """Execute any endpoint in nba_api.stats.endpoints dynamically.

    Args:
        endpoint_name: Class name in nba_api.stats.endpoints (e.g. 'CommonPlayerInfo', 'ShotChartDetail')
        params: Dictionary or JSON string of kwargs to pass to endpoint constructor
        dataset_index: Index of dataset returned by get_data_frames() (default: 0)
    """
    module_name = endpoint_name.lower()
    try:
        mod = importlib.import_module(f"nba_api.stats.endpoints.{module_name}")
        endpoint_cls = getattr(mod, endpoint_name)
    except (ImportError, AttributeError):
        import nba_api.stats.endpoints as ep_pkg

        if hasattr(ep_pkg, endpoint_name):
            endpoint_cls = getattr(ep_pkg, endpoint_name)
        else:
            return json.dumps(
                {
                    "error": f"Endpoint '{endpoint_name}' could not be located in nba_api.stats.endpoints."
                }
            )

    if isinstance(params, str):
        try:
            call_params = json.loads(params)
        except json.JSONDecodeError as err:
            return json.dumps({"error": f"Invalid JSON string passed in params: {err}"})
    elif isinstance(params, dict):
        call_params = dict(params)
    else:
        call_params = {}

    if "timeout" not in call_params:
        call_params["timeout"] = DEFAULT_TIMEOUT

    # Inspect endpoint constructor signature to supply sensible defaults for common required positional args
    # and map common alias parameters (e.g. season -> season_nullable)
    try:
        sig = inspect.signature(endpoint_cls.__init__)
        sig_params = sig.parameters

        alias_pairs = [
            ("season", "season_nullable"),
            ("team_id", "team_id_nullable"),
            ("player_id", "player_id_nullable"),
            ("league_id", "league_id_nullable"),
        ]
        for standard_key, nullable_key in alias_pairs:
            if (
                standard_key in call_params
                and standard_key not in sig_params
                and nullable_key in sig_params
            ):
                call_params[nullable_key] = call_params.pop(standard_key)
            elif (
                nullable_key in call_params
                and nullable_key not in sig_params
                and standard_key in sig_params
            ):
                call_params[standard_key] = call_params.pop(nullable_key)

        for param_name, param in sig_params.items():
            if param_name in ("self", "args", "kwargs"):
                continue
            if (
                param.default is inspect.Parameter.empty
                and param_name not in call_params
            ):
                if param_name in (
                    "team_id",
                    "player_id",
                    "team_id_nullable",
                    "player_id_nullable",
                ):
                    call_params[param_name] = 0
                elif param_name in ("league_id", "league_id_nullable"):
                    call_params[param_name] = "00"
                elif param_name in ("season", "season_nullable"):
                    call_params[param_name] = _get_default_season()
    except Exception:
        pass

    try:
        instance = _call_with_retry(endpoint_cls, **call_params)
        data_frames = instance.get_data_frames()
        if dataset_index >= len(data_frames):
            return json.dumps(
                {
                    "error": f"Dataset index {dataset_index} out of range (returned {len(data_frames)} datasets)"
                }
            )
        return data_frames[dataset_index].to_json(orient="records", indent=2)
    except Exception as err:
        return json.dumps({"error": str(err)})


def main() -> None:
    """Entrypoint for the nba-mcp console script."""
    mcp.run()


if __name__ == "__main__":
    main()
