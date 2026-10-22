# Open API findings

Things a live audit of stats.nba.com found that the library doesn't handle yet. This is a
work list for contributors and coding agents, not user documentation. For what users should
know, see [Known upstream issues](nba_api/stats/known_upstream_issues.md).

**Source:** an `endpoint_scope` run on 2026-10-21 over all 137 stats endpoint classes
(the tool is in #703, not yet merged; the full report is not committed). Each item was
checked against `master` on 2026-10-22.

**Before acting on an item:**

- The server changes. Recheck live first (one request with `NBA_API_PROXY=` is usually
  enough), and only when you've been asked to touch the network (see AGENTS.md).
- The report can be wrong about *why* something fails. It blamed a missing `MeasureType`
  for the PlayerGameLogs/TeamGameLogs 500s; the real cause was a blank `Season` (#709).
  Test the cause, not just the symptom.
- Public names are a compatibility contract. Fix a bad enum value by adding the right
  one alongside it, not by renaming or removing the old one, unless the maintainer agrees.
- When you fix an item, delete it here in the same PR.

## Already addressed

ISTRound filter (#719), `homeTeamId`/`awayTeamId` on V3 box scores (#717), deprecation
warnings for the 10 dead endpoints (#712), DunkScoreLeaders blank IDs (#708), GameLogs
blank `Season` (#709), and the user-facing list of failing endpoints (#715).

## Parameter values the server rejects

Each was rejected (non-200) with every other parameter at its baseline value, so a few
may only be invalid in combination.

| Endpoint | Parameter | Library class | Rejected values | Server accepts instead |
|---|---|---|---|---|
| LeagueDashPlayerStats, LeagueDashTeamStats, LeagueDashPtStats | `PlayerPosition` | `PlayerPositionAbbreviationNullable` | `C-F`, `F-C`, `F-G`, `G-F` | `F`, `C`, `G` |
| LeagueDashTeamStats | `MeasureType` | `MeasureTypeDetailedDefense` | `Usage` | |
| TeamDashboardByGeneralSplits | `MeasureType` | `MeasureTypeDetailedDefense` | `Defense`, `Usage` | |
| PlayerDashboardByGeneralSplits | `MeasureType` | `MeasureTypeDetailed` | `Four Factors`, `Opponent` | |
| LeagueHustleStatsPlayer | `PerMode` | `PerModeTime` | `MinutesPer` | `PerMinute` (in `PerModeDetailed`, not `PerModeTime`) |
| LeagueHustleStatsPlayer | `PlayerPosition` | `PlayerPositionNullable` | `Center`, `Forward`, `Guard` | |
| LeagueGameFinder | `RookieYear` | `SeasonNullable` | `2025-26`, `2026-27` (the `YYYY-YY` form) | a single year (`2025`), as in `SeasonYear` |

Accepted by the server but missing from the class the endpoint uses:

- PlayerDashboardByGeneralSplits: the argument is named `season_type_playoffs` but
  defaults from `SeasonType`, which has no `Playoffs` or `All Star`. Both are accepted.
- LeagueGameFinder `SeasonType` (`SeasonTypeNullable`): `All Star`.

## Stale `expected_data`

The DataSet columns come from the response, not `expected_data`, so these mostly affect
docs and anyone relying on `expected_data`. Renames do break users who look columns up by
name.

- **Renamed columns:**
  - PlayerCareerStats CareerTotals{RegularSeason,PostSeason,AllStarSeason}: `Team_ID` →
    `TEAM_ID`.
  - ScoreboardV2 LastMeeting: `LAST_GAME_VISITOR_TEAM_CITY1` →
    `LAST_GAME_VISITOR_TEAM_ABBREVIATION`.
  - PlayerDashPtShotDefend DefendingShots: `CLOSE_DEF_PERSON_ID` removed, `MATCHUPID`
    added.
  - BoxScoreMatchupsV3 PlayerStats: `expected_data` lists `positionDef`/`commentDef`, but
    the parser emits `positionOff`/`commentOff`. `expected_data` is the one that's wrong.
- **Removed columns:** `CFID` and `CFPARAMS` are gone from 77 datasets across 15 dashboard
  endpoints (LeagueDash{Player,Team}{Stats,Clutch}, all 7 PlayerDashboardBy*, both
  TeamDashboardBy*, PlayerVsPlayer, TeamVsPlayer). LeagueStandingsV3 lost 35
  `ReturnToPlay_*`/`Seeding_Game_*` columns from the 2019-20 restart.
- **Added columns** (safe for users): `WNBA_FANTASY_PTS*`, `TEAM_COUNT`, `NICKNAME`,
  `FP_HIGH_SCORE*` on player dashboards; `IS_ACTIVE_FLAG` on AllTimeLeadersGrids;
  `SUM_TIME_PLAYED` on lineups; a `Corner 3` shot category on both
  LeagueDash*ShotLocations (code that slices the multi-level header by position is off by
  one); and others.
- **DunkScoreLeaders:** `_expected_data/dunkscoreleaders.py` uses the key `dunks`, but the
  parser returns a dataset named `DunkScoreLeaders`.

## Datasets with no named attribute

Present in `.data_sets` only:

- PlayerCareerStats: `CareerHighs`, `SeasonHighs`, `CareerTotalsShowcaseSeason`,
  `SeasonTotalsShowcaseSeason` (the "Showcase" ones are probably the NBA Cup final).
- TeamDetails: `TeamAwardsCommCup`.

## Parameters the server accepts that the library never sends

The server echoes these back, so it knows them. What each one does is untested.

| Parameter | Endpoints |
|---|---|
| `ActiveRoster` | LeagueDashPlayerStats, LeagueDashPlayerClutch |
| `TwoWay` | LeagueDashPlayerClutch |
| `GameSubtype` | LeagueDashPlayerStats, LeagueDashPlayerClutch, LeagueDashTeamStats |
| `ActivePlayersOnly` | LeagueGameFinder |
| `PORound` | LeagueSeasonMatchups |
| `OppPlayerID` | VideoDetailsAsset |
| `LastNGames` | LeagueHustleStatsPlayer, LeagueHustleStatsTeam |

`SeasonType=IST` (NBA Cup games only) works on LeagueDashTeamStats but isn't in any
`SeasonType` class. #625 proposes constants for it; check which endpoints accept it first.

## Fields the nested (V3) parsers drop

Found by a loose name match, so treat as leads.

- **BoxScoreSummaryV3** drops about 45 fields, the largest gap: game labels and series
  info (`gameLabel`, `seriesText`, `ifNecessary`, `isNeutral`), arena address, team
  `seed`/`inBonus`/`timeoutsRemaining`, officials' `assignment`, OTT and international
  broadcasters, and the pre/postgame stat leaders.
- **ScheduleLeagueV2, ScoreboardV3:** `nationalOttBroadcasters`, `homeOttBroadcasters`,
  `awayOttBroadcasters`. ScoreboardV3 also drops `periods[].periodType`.
- **ISTStandings:** `teams[].games[].gameNumber`, `timeStampUtc`, `unixTimeStamp`.

## Failing endpoints left alone on purpose

These failed in the audit but are not in the user-facing list, because they are
intermittent: GameRotation 500'd on an old game but worked on recent ones, and the
tracking dashboards flipped between 500 and 200 (#715).

- GameRotation: 500 or a 30 s timeout on game `0022200552`.
- PlayerDashPtShots: 500 after about 30 s.
- TeamDashPtPass, TeamDashPtShots: an immediate 500.

All four still have active `EndpointSpec`s. CI replays their recorded cassettes, so it
won't notice if they stay broken.

## Test coverage gaps

- **Working, but no `EndpointSpec` or cassette:** BoxScoreSummaryV3, GravityLeaders,
  ScheduleLeagueV2, ScoreboardV3, TeamGameLog, and now DunkScoreLeaders and TeamGameLogs
  (fixed by #708/#709). None is regression-tested in CI.
- **PlayerGameLogs** is still marked `skip`. It works since #709 and could get a spec and
  cassette.
- **SynergyPlayTypes:** its spec returns 0 rows, so its cassette proves little. Pin a
  season and play type that return data.
- **TeamGameStreakFinder:** 500 with all 200+ parameters blank. It's in the failing list,
  but it probably just needs some required values nobody has found.

Recording cassettes hits the live API, so it needs the maintainer's go-ahead.

## Server quirks worth knowing

- **Echoed names differ from sent names.** The server echoes some parameters under other
  names (`Month` → `MonthNum`, `OpponentTeamID` → `OppTeamID`, `Season` → `SeasonYear`,
  `VsConference` → `vsConfernce`, `DraftTeamID` → `DraftTeam`). That doesn't mean the
  filter is ignored: on LeagueHustleStatsPlayer, `Month=1` cut the rows from 581 to 409,
  while `MonthNum=1` changed nothing. Only that pair was checked.
- **Garbage values accepted** (no validation): AllTimeLeadersGrids `TopX`,
  CommonPlayoffSeries `SeriesID`, CumeStatsTeamGames `SeasonID`, ISTStandings `Section`,
  LeagueStandings/LeagueStandingsV3 `SeasonYear`, ShotChartDetail and VideoDetailsAsset
  `ContextFilter`/`Position`, ShotChartLineupDetail `ContextFilter`, TeamVsPlayer
  `PlayerID`.
- **Values accepted with no visible effect** (data byte-identical to the baseline):
  `GameScope` `Last 10`/`Yesterday` on LeagueDashPlayerStats and LeagueDashPtStats (maybe
  current-season only), `Rank=Y` on four dashboards, `PlusMinus=Y`/`PaceAdjust=Y` with
  `MeasureType=Base`, and `LeagueID=01` on PlayerCareerStats.
- **A blank value and a missing parameter are different.** For example, DunkScoreLeaders
  rejects `PlayerID=` but accepts the parameter being left out (#708). Defaulting an
  optional argument to `None` leaves it out of the query string.
