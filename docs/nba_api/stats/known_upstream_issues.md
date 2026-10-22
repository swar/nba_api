# Known upstream issues

Endpoints that stats.nba.com is not serving correctly. The `nba_api` classes are kept, so
existing code keeps importing. The server is the problem, and there is nothing to fix on your
side. Each section gives the date the behaviour was last checked. Rerun
[`endpoint_scope`](../tools/stats/endpoint_scope/scope.md) to recheck.

## Failing upstream

**Last checked: 2026-10-21.** These endpoints answer HTTP 500 with an empty body for every
parameter combination tried. A 500 can also mean a required parameter or value nobody has found
yet, so treat these as likely broken rather than removed. They are not deprecated.

| Endpoint | Parameters tried |
|---|---|
| [DraftBoard](endpoints/draftboard.md) | `Season` 2024 and 2025 |
| [PlayerCareerByCollege](endpoints/playercareerbycollege.md) | `College=Ohio State`, with `Season` blank and 2025-26 |
| [TeamGameStreakFinder](endpoints/teamgamestreakfinder.md) | Library defaults; `Season=2025-26`, with and without `SeasonType=Regular Season` (only a few of its 200+ filters) |
| [TeamHistoricalLeaders](endpoints/teamhistoricalleaders.md) | `TeamID=1610612739`, `SeasonID` 22024 and 22025 |
| [WinProbabilityPBP](endpoints/winprobabilitypbp.md) | `RunType=each second`, games `0022200552` (2022-23) and `0022500001` (2025-26) |

If you find parameters that make one of these work, please open an issue.

## Removed upstream

**Last checked: 2026-10-21.** These return no data at all. Requests are redirected to the
NBA.com homepage (HTTP 200 with HTML), or answered with an empty `{}`. Constructing them emits
a `DeprecationWarning` that names a replacement where one exists.

| Endpoint | Response | Use instead |
|---|---|---|
| [AssistLeaders](endpoints/assistleaders.md) | Homepage redirect | LeagueDashPlayerStats or LeagueDashTeamStats |
| [AssistTracker](endpoints/assisttracker.md) | Homepage redirect | — |
| [LeagueLeaders](endpoints/leagueleaders.md) | Homepage redirect | LeagueDashPlayerStats |
| [PlayoffPicture](endpoints/playoffpicture.md) | Homepage redirect | LeagueStandingsV3 |
| [BoxScoreAdvancedV2](endpoints/boxscoreadvancedv2.md) | Empty `{}` | BoxScoreAdvancedV3 |
| [BoxScoreFourFactorsV2](endpoints/boxscorefourfactorsv2.md) | Empty `{}` | BoxScoreFourFactorsV3 |
| [BoxScoreMiscV2](endpoints/boxscoremiscv2.md) | Empty `{}` | BoxScoreMiscV3 |
| [BoxScoreScoringV2](endpoints/boxscorescoringv2.md) | Empty `{}` | BoxScoreScoringV3 |
| [BoxScoreUsageV2](endpoints/boxscoreusagev2.md) | Empty `{}` | BoxScoreUsageV3 |
| [PlayByPlay](endpoints/playbyplay.md) | Empty `{}` | PlayByPlayV3 |
| [PlayByPlayV2](endpoints/playbyplayv2.md) | Empty `{}` | PlayByPlayV3 |
