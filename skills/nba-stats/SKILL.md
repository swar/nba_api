---
name: nba-stats
description: >-
  Query NBA statistics, player profiles, career/season splits, game logs, scoreboards,
  team rosters, league leaders, Synergy play types, Second Spectrum shot tracking,
  shot chart mechanics (step-backs, fadeaways, floaters), advanced metrics (TS%, USG%, NetRTG),
  and hustle stats using swar/nba_api. Use whenever asked about NBA players,
  teams, game results, statistical comparisons, shot diet, or advanced basketball analytics.
---

# NBA Stats Agent Skill

This skill guides AI agents and LLMs in querying and analyzing official NBA statistics via `nba_api` using either the **Model Context Protocol (MCP)** server or direct Python API endpoints.

---

## 1. Execution via Model Context Protocol (MCP)

When configured with the `nba-api` MCP server (`nba-mcp`), call the following tools directly:

| Tool | Purpose | Example Parameters |
| :--- | :--- | :--- |
| `get_player_stats` | Career and season stats (per game or totals) | `player_name="Nikola Jokic", season="2024-25", per_game=True` |
| `get_player_gamelog` | Recent game-by-game log for a player | `player_name="Luka Doncic", last_n=5` |
| `get_scoreboard` | Live/final scores, linescores, game status | `date="2026-03-01"` |
| `get_team_roster` | Active or historical roster with player bio | `team_name="BOS", season="2024-25"` |
| `get_synergy_play_types` | Synergy offensive/defensive play type PPP efficiency | `play_type="PRBallHandler", min_poss=200, sort_by="PPP", top_n=10` |
| `get_shot_tracking` | Second Spectrum tracking (Pullups, Catch & Shoot, dribbles) | `player_name="Stephen Curry", split="general"` |
| `get_shot_chart_actions` | Physical shot mechanics (Step Back, Fadeaway, Floater) | `action_type="Step Back", shot_type="3pt", min_fga=50, top_n=10` |
| `get_advanced_stats` | TS%, USG%, Net Rating, PIE, AST%, REB% | `min_minutes=1000, sort_by="TS_PCT", top_n=10` |
| `get_hustle_stats` | Deflections, Screen Assists, Charges Drawn, Loose Balls | `min_minutes=20, sort_by="DEFLECTIONS", top_n=10` |
| `query_raw_endpoint` | General-purpose bridge for any `nba_api.stats.endpoints` class | `endpoint_name="CommonPlayerInfo", params={"player_id": 2544}` |

---

## 2. Execution via Direct Python API

Agents writing custom Python scripts or notebooks can use the underlying `nba_api` classes:

### Synergy Play Types
```python
from nba_api.stats.endpoints import synergyplaytypes

synergy = synergyplaytypes.SynergyPlayTypes(
    player_or_team_abbreviation="P",
    play_type_nullable="PRBallHandler",
    type_grouping_nullable="offensive",
    season="2024-25",
    timeout=45,
)
df = synergy.get_data_frames()[0]
# Filter qualification: df[df["POSS"] >= 150].sort_values(by="PPP", ascending=False)
```

### Second Spectrum Shot Tracking
```python
from nba_api.stats.endpoints import leaguedashplayerptshot, playerdashptshots

# League-wide pull-ups:
pullups = leaguedashplayerptshot.LeagueDashPlayerPtShot(
    general_range_nullable="Pullups",
    timeout=45,
)
df_pullups = pullups.get_data_frames()[0]

# Player tracking splits (Catch & Shoot vs Pullups vs Rim):
player_shots = playerdashptshots.PlayerDashPtShots(player_id=201939, timeout=45)
df_splits = player_shots.get_data_frames()[1]  # General splits
```

### Shot Chart Details & Mechanics
```python
from nba_api.stats.endpoints import shotchartdetail

# Note: context_measure_simple must be 'FGA' to include both makes and misses
shots = shotchartdetail.ShotChartDetail(
    player_id=0,
    team_id=0,
    context_measure_simple="FGA",
    season_nullable="2024-25",
    timeout=60,
)
df_shots = shots.get_data_frames()[0]
# Filter by action: df_shots[df_shots["ACTION_TYPE"].str.contains("Step Back", case=False)]
```

### Advanced Metrics (TS%, USG%, NetRTG)
```python
from nba_api.stats.endpoints import leaguedashplayerstats

adv = leaguedashplayerstats.LeagueDashPlayerStats(
    measure_type_detailed_defense="Advanced",
    timeout=45,
)
df_adv = adv.get_data_frames()[0]
```

### Hustle & Extra-Effort Stats
```python
from nba_api.stats.endpoints import leaguehustlestatsplayer

hustle = leaguehustlestatsplayer.LeagueHustleStatsPlayer(timeout=45)
df_hustle = hustle.get_data_frames()[0]
```

---

## 3. Reference Guides

- [Endpoints & Parameters Guide](./references/endpoints.md): Full documentation of classes, parameter enums, and dataset indexes.
- [Analytical Recipes & Workflows](./references/recipes.md): Pre-built query patterns for common scouting and analytics questions.
- [Gotchas & Best Practices](./references/gotchas.md): Rate limits, timeouts, header spoofing, and diacritic handling.
