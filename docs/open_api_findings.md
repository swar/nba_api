# Open API findings

Problems a live audit of stats.nba.com found that the library doesn't handle yet. A work
list for contributors and coding agents. The audit was an `endpoint_scope` run (#703) on
2026-10-21, and each item was checked against `master` on 2026-10-22.

The audit can be wrong about *why* something fails. It blamed a missing `MeasureType` for
the PlayerGameLogs/TeamGameLogs 500s, but the cause was a blank `Season` (#709). Test the
cause before fixing. When you fix an item, delete it here in the same PR.

## Parameter values the server rejects

| Endpoint | Parameter | Library class | Rejected | Accepted instead |
|---|---|---|---|---|
| LeagueDashPlayerStats, LeagueDashTeamStats, LeagueDashPtStats | `PlayerPosition` | `PlayerPositionAbbreviationNullable` | `C-F`, `F-C`, `F-G`, `G-F` | `F`, `C`, `G` |
| LeagueDashTeamStats | `MeasureType` | `MeasureTypeDetailedDefense` | `Usage` | |
| TeamDashboardByGeneralSplits | `MeasureType` | `MeasureTypeDetailedDefense` | `Defense`, `Usage` | |
| PlayerDashboardByGeneralSplits | `MeasureType` | `MeasureTypeDetailed` | `Four Factors`, `Opponent` | |
| LeagueHustleStatsPlayer | `PerMode` | `PerModeTime` | `MinutesPer` | `PerMinute` (in `PerModeDetailed`) |
| LeagueHustleStatsPlayer | `PlayerPosition` | `PlayerPositionNullable` | `Center`, `Forward`, `Guard` | |
| LeagueGameFinder | `RookieYear` | `SeasonNullable` | `2025-26` form | a single year (`2025`) |

Missing from the class an endpoint uses: PlayerDashboardByGeneralSplits'
`season_type_playoffs` defaults from `SeasonType`, which has no `Playoffs` or `All Star`;
LeagueGameFinder's `SeasonTypeNullable` has no `All Star`. The server accepts all three.

## Columns that break lookups by name

- PlayerCareerStats CareerTotals{RegularSeason,PostSeason,AllStarSeason}: `Team_ID` →
  `TEAM_ID`.
- ScoreboardV2 LastMeeting: `LAST_GAME_VISITOR_TEAM_CITY1` →
  `LAST_GAME_VISITOR_TEAM_ABBREVIATION`.
- PlayerDashPtShotDefend DefendingShots: `CLOSE_DEF_PERSON_ID` → `MATCHUPID`.
- `CFID` and `CFPARAMS` are gone from 77 datasets across 15 dashboard endpoints
  (LeagueDash*, PlayerDashboardBy*, TeamDashboardBy*, PlayerVsPlayer, TeamVsPlayer), and
  still listed in their `expected_data`.
- DunkScoreLeaders: `expected_data` uses the key `dunks`, but the parser returns
  `DunkScoreLeaders`.

## Data the library doesn't expose

- **Datasets with no named attribute** (only in `.data_sets`): PlayerCareerStats
  `CareerHighs`, `SeasonHighs`, `CareerTotalsShowcaseSeason`, `SeasonTotalsShowcaseSeason`;
  TeamDetails `TeamAwardsCommCup`.
- **Parameters the server accepts but the library never sends:** `ActiveRoster` and
  `GameSubtype` (LeagueDashPlayerStats/Clutch; `GameSubtype` also LeagueDashTeamStats),
  `TwoWay` (LeagueDashPlayerClutch), `ActivePlayersOnly` (LeagueGameFinder), `PORound`
  (LeagueSeasonMatchups), `OppPlayerID` (VideoDetailsAsset), `LastNGames`
  (LeagueHustleStats*). What each one does is untested.
- **`SeasonType=IST`** (NBA Cup games only) works on LeagueDashTeamStats but isn't in any
  `SeasonType` class. #625 proposes it; check which endpoints accept it first.
- **Fields the V3 parsers drop:** BoxScoreSummaryV3 drops about 45, including game and
  series labels, team seeds and the stat leaders. ScheduleLeagueV2 and ScoreboardV3 drop
  the OTT broadcaster groups.

## Tests that don't catch breakage

- **Intermittently failing endpoints:** GameRotation, PlayerDashPtShots, TeamDashPtPass and
  TeamDashPtShots gave 500s or timeouts, but have worked at other times, so they're not in
  [Known upstream issues](nba_api/stats/known_upstream_issues.md). Their `EndpointSpec`s
  replay old cassettes, so CI won't notice if they stay broken.
- **Working endpoints with no `EndpointSpec`:** BoxScoreSummaryV3, GravityLeaders,
  ScheduleLeagueV2, ScoreboardV3, TeamGameLog, DunkScoreLeaders, TeamGameLogs.
- **PlayerGameLogs** is still marked `skip`, though it works since #709.
- **SynergyPlayTypes:** its spec returns 0 rows, so its cassette proves little.

Adding a spec means recording a cassette against the live API, so ask the maintainer first.

## Blank and missing are different

The server can reject a blank value but accept the parameter being left out:
DunkScoreLeaders rejects `PlayerID=` (#708), and the GameLogs endpoints 500 on `Season=`
(#709). Defaulting an optional argument to `None` leaves it out of the query string.
