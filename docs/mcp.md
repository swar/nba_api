# NBA API Model Context Protocol (MCP) Server

The `nba_api` package includes an official Model Context Protocol (MCP) server that exposes NBA statistics, player profiles, game logs, live scoreboards, Synergy play types, Second Spectrum shot tracking, shot chart mechanics, and advanced analytics as callable tools for AI agents and LLMs (Claude Desktop, Cursor, Antigravity, Factory Droid, Windsurf, etc.).

---

## 1. Installation

The MCP server is provided as an optional extra in `nba_api` so existing library users incur zero additional dependencies:

```bash
# Using pip
pip install "nba-api[mcp]"

# Using uv
uv pip install "nba-api[mcp]"
```

---

## 2. Running the Server

Once installed, the server can be launched directly via the console script entrypoint:

```bash
nba-mcp
```

Or via Python module execution:

```bash
python -m nba_api.mcp.server
```

The server communicates using JSON-RPC over `stdio`, adhering to the Model Context Protocol standard.

---

## 3. Client Configuration

### Claude Desktop

Add the following to your `claude_desktop_config.json` (located at `%APPDATA%\Claude\claude_desktop_config.json` on Windows or `~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

```json
{
  "mcpServers": {
    "nba-api": {
      "command": "nba-mcp"
    }
  }
}
```

If running in a specific virtual environment:

```json
{
  "mcpServers": {
    "nba-api": {
      "command": "python",
      "args": ["-m", "nba_api.mcp.server"]
    }
  }
}
```

### Cursor

In Cursor, open **Settings -> Features -> MCP Servers -> Add New MCP Server**:
- **Name**: `nba-api`
- **Type**: `command`
- **Command**: `nba-mcp`

Or in your project's `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "nba-api": {
      "command": "nba-mcp"
    }
  }
}
```

### Gemini CLI / Antigravity / Factory Droid

Add to your MCP settings file (e.g., `~/.gemini/antigravity/mcp_config.json` or `.factory/mcp.json`):

```json
{
  "mcpServers": {
    "nba-api": {
      "command": "nba-mcp"
    }
  }
}
```

---

## 4. Exposed Tools

The server registers 10 specialized, high-performance tools designed with clean JSON schemas and input sanitization (including diacritic/accent normalization for player names like "Dončić" and "Jokić", and fuzzy team lookups):

| Tool | Description | Key Parameters |
| :--- | :--- | :--- |
| `get_player_stats` | Career and season per-game or totals for any player. | `player_name`, `season`, `per_game` |
| `get_player_gamelog` | Recent individual game logs for a player. | `player_name`, `season`, `last_n` |
| `get_scoreboard` | Today's or specific date's scores, game status, and live linescores. | `game_date` (YYYY-MM-DD) |
| `get_team_roster` | Active or historical team roster with player positions, numbers, and ages. | `team_name`, `season` |
| `get_synergy_play_types` | Synergy offensive/defensive play-type efficiency (P&R Ball Handler, Isolation, Post Up, Spot Up, Transition, etc.). | `play_type`, `player_name`, `team_name`, `grouping`, `season`, `min_poss`, `sort_by`, `top_n` |
| `get_shot_tracking` | Second Spectrum tracking splits (Catch & Shoot, Pullups, dribble counts, defender distance). | `player_name`, `split_type`, `stat_category`, `min_fga`, `sort_by`, `top_n` |
| `get_shot_chart_actions` | Physical shot mechanics (Step Back, Fadeaway, Pullup, Floater, Hook Shot) across players or league-wide. | `action_type`, `player_name`, `shot_type`, `season`, `min_fga`, `sort_by`, `top_n` |
| `get_advanced_stats` | Advanced metrics (TS%, USG%, Net Rating, PIE, AST%, REB%). | `player_name`, `season`, `min_minutes`, `sort_by`, `top_n` |
| `get_hustle_stats` | Hustle and effort metrics (Deflections, Screen Assists, Charges Drawn, Loose Balls Recovered, Box Outs). | `player_name`, `season`, `min_minutes`, `sort_by`, `top_n` |
| `query_raw_endpoint` | General-purpose bridge to query any of the 130+ `nba_api.stats.endpoints` by name. | `endpoint_name`, `params`, `dataset_index` |

---

## 5. Agent Skill Integration

For LLMs and agents supporting the [Agent Skills standard](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo) or file-based workflows, an `nba-stats` skill definition is provided in `skills/nba-stats/SKILL.md` along with reference guides in `skills/nba-stats/references/`.
