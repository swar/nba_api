# Using nba_api with AI agents

Read this before writing code that uses `nba_api`. It is written for AI coding agents, but it
doubles as a checklist of the library's gotchas for people. It links to the full reference
rather than repeating it.

## Rules

1. **Don't write `nba_api` calls from memory.** Python parameter names differ from the NBA's
   query-string names and often carry suffixes (`season_type_all_star`, `per_mode36`,
   `league_id_nullable`, `measure_type_detailed_defense`). Check the endpoint's constructor in
   the installed package, for example `inspect.signature(PlayerGameLog.__init__)`, and its
   `expected_data` for the data sets and columns. Each [endpoint page](table_of_contents.md#reference)
   lists the same information under "Python Parameter Variable", but some pages are older than
   the code. When they disagree, the code wins.
2. **Constructing an endpoint sends the request.** Pass `get_request=False` to build it without
   sending, then call `.get_request()`.
3. **Look up IDs offline** with `nba_api.stats.static` (see [IDs](#ids-seasons-and-dates)).
   Never guess a player, team, or game ID.
4. **Pass game IDs as strings**, such as `"0022400061"`. An int drops the leading zeros and the
   request fails or returns nothing. Player and team IDs can be ints.
5. **Always pass `season` explicitly**, as `"2024-25"`. Defaults are derived from today's date
   and roll over to the new season every October, when there is little or no data yet.
6. **Check [known upstream issues](nba_api/stats/known_upstream_issues.md) before using a V2,
   `PlayByPlay`, or `*Leaders` endpoint.** Several were removed by stats.nba.com and return no
   data. Prefer the V3 versions. Removed endpoints emit a `DeprecationWarning` that names the
   replacement.
7. **Be gentle with stats.nba.com.** Send one request at a time, pause about a second between
   requests in a loop, and cache results. It throttles rapid requests and does not answer many
   cloud IP ranges, including the sandboxes many coding agents run in. If requests hang, raising
   `timeout` or adding retries will not help: use a `proxy` (or the `NBA_API_PROXY` environment
   variable) or run the code locally.

## Which endpoint?

All stats endpoints import from `nba_api.stats.endpoints`. The last column is the data set
attribute to call `.get_data_frame()` on.

| To get | Endpoint and key parameters | Data set |
|---|---|---|
| A player's career totals by season | `PlayerCareerStats(player_id)` | `season_totals_regular_season` |
| A player's game log | `PlayerGameLog(player_id, season, season_type_all_star)` | `player_game_log` |
| A team's game log | `TeamGameLog(team_id, season, season_type_all_star)` | `team_game_log` |
| Games and game IDs matching filters | `LeagueGameFinder(player_or_team_abbreviation="T", team_id_nullable, season_nullable)` | `league_game_finder_results` |
| Season stats for every player (leaders) | `LeagueDashPlayerStats(season, per_mode_detailed="PerGame")` | `league_dash_player_stats` |
| Season stats for every team | `LeagueDashTeamStats(season, per_mode_detailed="PerGame")` | `league_dash_team_stats` |
| Standings | `LeagueStandingsV3(season)` | `standings` |
| A season's schedule | `ScheduleLeagueV2(season)` | `season_games` |
| Games on a date | `ScoreboardV3(game_date="2025-01-15")` | `game_header`, `line_score` |
| Box score for a finished game | `BoxScoreTraditionalV3(game_id)` (also `BoxScoreAdvancedV3`, ...) | `player_stats`, `team_stats` |
| Play-by-play for a finished game | `PlayByPlayV3(game_id)` | `play_by_play` |
| Shot locations | `ShotChartDetail(team_id=0, player_id, season_nullable, context_measure_simple="FGA")` | `shot_chart_detail` |
| A team's roster | `CommonTeamRoster(team_id, season)` | `common_team_roster` |
| A player's bio | `CommonPlayerInfo(player_id)` | `common_player_info` |
| Tonight's games, live | `nba_api.live.nba.endpoints.scoreboard.ScoreBoard()` | `games` (use `.get_dict()`) |

`ShotChartDetail` defaults to `context_measure_simple="PTS"`, which returns made shots only.
Pass `"FGA"` for every attempt. `team_id=0` means all teams.

For anything else, browse the [endpoint list](table_of_contents.md#reference).

## IDs, seasons, and dates

```python
from nba_api.stats.static import players, teams

player_id = players.find_players_by_full_name("donovan mitchell")[0]["id"]  # 1628378
team_id = teams.find_team_by_abbreviation("cle")["id"]                      # 1610612739
```

Name searches take a case-insensitive regular expression and return a list, so check its
length. See [stats examples](nba_api/stats/examples.md#static-data) for every lookup.

- **Game IDs** are 10-character strings: `"002"` for the regular season or `"004"` for the
  playoffs, then the season's start year and a game number (`"0022400061"`). Get them from
  `LeagueGameFinder`, `ScoreboardV3`, or `ScheduleLeagueV2` rather than building them.
- **Seasons** are `"YYYY-YY"` strings, such as `"2024-25"`.
- **Season type** values are `"Regular Season"`, `"Playoffs"`, `"PlayIn"`, `"Pre Season"`, and
  `"All Star"`. The parameter name varies by endpoint: most use `season_type_all_star`, some
  `season_type_playoffs`, `season_type_nullable`, or plain `season_type`.
- **Dates**: `ScoreboardV3(game_date=...)` takes `"YYYY-MM-DD"`. The `date_from_nullable` and
  `date_to_nullable` filters take `"MM/DD/YYYY"`.
- **Other leagues**: many endpoints accept `league_id` (or `league_id_nullable`): `"00"` NBA,
  `"10"` WNBA, `"20"` G League.

Valid values for every parameter are in [parameters](nba_api/stats/library/parameters.md), and
as classes in `nba_api.stats.library.parameters` (for example `SeasonTypeAllStar.playoffs`).

## Reading results

```python
from nba_api.stats.endpoints import PlayerGameLog

log = PlayerGameLog(player_id=1628378, season="2024-25", season_type_all_star="Regular Season")
df = log.player_game_log.get_data_frame()
```

- Each data set is an attribute with `get_data_frame()`, `get_dict()`, and `get_json()`.
  `get_data_frames()` returns all of them as a list. See
  [endpoint data structure](nba_api/stats/endpoints_data_structure.md).
- An **empty DataFrame usually means a valid request with no matching data**: a season that
  hasn't started, the wrong season type, or the wrong league. It is not an error.
- Live endpoints (`nba_api.live.nba.endpoints`) return dicts. Use `.get_dict()` on their data
  sets.

## When something goes wrong

| Symptom | Likely cause |
|---|---|
| Request hangs, then `ReadTimeout` or `ConnectTimeout` | Throttled, or a blocked cloud IP. Slow down, or use a proxy. |
| `TypeError: ... unexpected keyword argument` | A guessed parameter name. Check the constructor signature. |
| `JSONDecodeError` | stats.nba.com sent something other than JSON: a block page, the NBA.com homepage (for a removed endpoint), or an empty body. |
| `KeyError: 'resultSet'` | The response was `{}` (a removed endpoint) or an error object, often for an invalid parameter value. |
| `DeprecationWarning` | The endpoint was removed upstream. Use the replacement it names. |
| Empty DataFrame | See [Reading results](#reading-results). |

To see what the server actually sent, build the endpoint without sending it, then inspect the
response after a failure:

```python
ep = PlayerGameLog(player_id=1628378, season="2024-25", get_request=False)
try:
    ep.get_request()
except Exception:
    print(ep.get_request_url())
    print(ep.nba_response.get_response()[:500])
    raise
```

## More

- [README](../README.md): installation, quick start, and request options
- [Stats examples](nba_api/stats/examples.md): request options, return formats, and static data
- [Known upstream issues](nba_api/stats/known_upstream_issues.md): broken and removed endpoints
- [Table of contents](table_of_contents.md): every endpoint's parameters and data sets
