# Endpoint guide

`nba_api` wraps about 140 stats.nba.com endpoints, and their names rarely say what is in them.
This page groups every endpoint by what its data is about. For each one it says what you get,
what you have to pass, and which data set attributes to read. Each endpoint's own page has the
full parameter and column lists.

Status notes come from a live check of every endpoint on 2026-10-21 and from fixes on `master`
since then. If an endpoint misbehaves, also check
[Known upstream issues](known_upstream_issues.md).

- [Reading endpoint names](#reading-endpoint-names)
- [Parameters that change what you get](#parameters-that-change-what-you-get)
- [Quick finder](#quick-finder)
- Endpoints by topic: [Players](#players) · [Teams](#teams) · [League-wide stats](#league-wide-stats) ·
  [Leaders](#leaders) · [Standings and schedule](#standings-and-schedule) · [Games](#games) ·
  [Shots](#shots) · [Draft](#draft) · [Video](#video) · [Live data](#live-data)

## Reading endpoint names

| Name | What it holds |
|---|---|
| `Common*` | Reference data: player bios, rosters, franchise years, playoff series. |
| `Player*`, `Team*` | One player or one team. Pass `player_id` or `team_id`. |
| `PlayerDashboardBy*`, `TeamDashboardBy*` | One player's or team's season, split by context (home and away, month, clutch, shot type, and so on). Each split is its own data set. In each row, `GROUP_SET` names the split and `GROUP_VALUE` the bucket, such as `Location` and `Home`. |
| `LeagueDash*` | One row per player, team, or lineup across the league, with dozens of filters. Use these for "who leads the league in X". |
| `*Pt*` | Player tracking: speed and distance, touches, passes, drives, catch-and-shoot, rebound chances, and shots defended. |
| `*Hustle*` | Deflections, contested shots, charges drawn, screen assists, loose balls, and box outs. |
| `BoxScore*` | One game. Pass `game_id`. The word after `BoxScore` names the stat family. |
| `CumeStats*` | Totals over a list of games that you choose. |
| `*GameFinder`, `*StreakFinder` | Search for games or streaks that match stat thresholds. |
| `V2`, `V3` | Newer versions of the same data. Use the highest version: several V2 endpoints were removed upstream. V3 columns are camelCase (`personId`, `points`) where V2 used `PLAYER_ID` and `PTS`. |

Tracking, hustle, matchup, and play type data only exist for recent seasons. An empty result for
an older season usually means the data was never collected.

## Parameters that change what you get

Several endpoints return different columns, or different rows, depending on one parameter. The
names below are the NBA's. The Python name is in the endpoint's signature, for example
`measure_type_detailed_defense`. All values are in [parameters](library/parameters.md).

| Parameter | Values | Used by |
|---|---|---|
| `MeasureType` | `Base` (box score stats, the default), `Advanced` (ratings, usage, pace), `Misc` (points off turnovers, second chance, fast break, paint), `Four Factors`, `Scoring` (shot mix and assisted rates), `Opponent`, `Usage`, `Defense` | `LeagueDash*Stats`, `*Clutch`, `*DashboardBy*`, lineups, on/off, and versus endpoints. Not every endpoint takes every value: LeagueDashTeamStats rejects `Usage`, TeamDashboardByGeneralSplits rejects `Defense` and `Usage`, and PlayerDashboardByGeneralSplits rejects `Four Factors` and `Opponent`. |
| `PerMode` | `Totals` (the default), `PerGame`, `Per36`, `Per48`, `Per100Possessions`, and others | Most season stats endpoints. |
| `PtMeasureType` | `SpeedDistance`, `Rebounding`, `Possessions`, `CatchShoot`, `PullUpShot`, `Defense`, `Drives`, `Passing`, `ElbowTouch`, `PostTouch`, `PaintTouch`, `Efficiency` | LeagueDashPtStats |
| `PlayerOrTeam` | `Player` or `Team`; `P` or `T` on LeagueGameFinder, LeagueGameLog, and SynergyPlayTypes | Endpoints that can return either. |
| `DefenseCategory` | `Overall`, `3 Pointers`, `2 Pointers`, `Less Than 6Ft`, `Less Than 10Ft`, `Greater Than 15Ft` | LeagueDashPtDefend, LeagueDashPtTeamDefend |
| `PlayType`, `TypeGrouping` | `Transition`, `Isolation`, `PRBallHandler`, `PRRollman`, `Postup`, `Spotup`, `Handoff`, `Cut`, `OffScreen`, `OffRebound`, `Misc`; `offensive` or `defensive` | SynergyPlayTypes |
| `ContextMeasure` | `PTS` (the default, which returns made shots only), `FGA` (every attempt), and other stats | ShotChartDetail, ShotChartLineupDetail, VideoDetailsAsset |
| `GroupQuantity` | Number of players in a lineup (default 5) | LeagueDashLineups, LeagueLineupViz, TeamDashLineups |
| `SeasonType` | `Regular Season`, `Playoffs`, `PlayIn`, `Pre Season`, `All Star` | Nearly every endpoint. The Python name varies, see [IDs, seasons, and dates](../../ai_agents.md#ids-seasons-and-dates). |

## Quick finder

| To get | Use |
|---|---|
| Player or team IDs | [`nba_api.stats.static`](static/players.md) (offline, no request) |
| Every player, past and present | [CommonAllPlayers](#players) or [PlayerIndex](#players) |
| A player's height, weight, birthdate, school, draft position | [CommonPlayerInfo](#players), or [LeagueDashPlayerBioStats](#league-wide-stats) for all players at once |
| A player's season-by-season and career totals | [PlayerCareerStats](#players) |
| A player's career and season highs | [PlayerProfileV2](#players) |
| A player's awards | [PlayerAwards](#players) |
| A player's game log | [PlayerGameLog](#players), or [PlayerGameLogs](#players) for advanced columns or many players |
| A player's home and away, monthly, or clutch splits | [PlayerDashboardBy*](#players) |
| Who a player passes to | [PlayerDashPtPass](#players) |
| How a player does against one opponent | [PlayerVsPlayer](#players), or [LeagueSeasonMatchups](#league-wide-stats) for direct defensive matchups |
| A roster and coaching staff | [CommonTeamRoster](#teams) |
| Arena, owner, GM, titles, retired numbers | [TeamDetails](#teams) |
| A franchise's history, season by season | [TeamYearByYearStats](#teams) |
| A team's game log | [TeamGameLog](#teams) |
| Lineup stats | [TeamDashLineups](#teams) for one team, [LeagueDashLineups](#league-wide-stats) for the league |
| How a team does with a player on or off the court | [TeamPlayerOnOffSummary](#teams) |
| Season stats for every player or team | [LeagueDashPlayerStats, LeagueDashTeamStats](#league-wide-stats) |
| Advanced ratings (offensive, defensive, net, pace) | `MeasureType="Advanced"` on the above, or [PlayerEstimatedMetrics](#league-wide-stats) |
| Speed, distance, touches, drives, catch-and-shoot | [LeagueDashPtStats](#league-wide-stats) |
| Hustle stats | [LeagueHustleStatsPlayer, LeagueHustleStatsTeam](#league-wide-stats) |
| Opponent shooting when a player defends | [LeagueDashPtDefend](#league-wide-stats) |
| Shooting by court zone | [LeagueDashPlayerShotLocations](#league-wide-stats) |
| Play types (isolation, pick and roll, spot up) | [SynergyPlayTypes](#league-wide-stats) |
| All-time leaders | [AllTimeLeadersGrids](#leaders) |
| Standings | [LeagueStandingsV3](#standings-and-schedule) |
| NBA Cup standings | [ISTStandings](#standings-and-schedule) |
| The season schedule | [ScheduleLeagueV2](#standings-and-schedule) |
| Games on a date | [ScoreboardV3](#games) |
| Game IDs that match filters | [LeagueGameFinder](#games) |
| A box score | [BoxScoreTraditionalV3](#games) and the other `BoxScore*V3` |
| Play-by-play | [PlayByPlayV3](#games) |
| Officials, attendance, inactive players | [BoxScoreSummaryV3](#games) |
| When each player subbed in and out | [GameRotation](#games) |
| Shot locations (x, y) | [ShotChartDetail](#shots) |
| Draft picks | [DraftHistory](#draft) |
| Draft combine measurements | [DraftCombinePlayerAnthro](#draft) |
| Live scores and box scores | [Live data](#live-data) |

## Players

### Reference and career

| Endpoint | What you get | You pass | Data sets |
|---|---|---|---|
| [CommonAllPlayers](endpoints/commonallplayers.md) | Every player in league history, with first and last season and current team. Set `is_only_current_season=1` for this season only. | `season` | `common_all_players` |
| [PlayerIndex](endpoints/playerindex.md) | One row per player for a season: bio, draft, team, and season PTS, REB, and AST. Filters for team, college, country, draft year, height, and weight. | `season` | `player_index` |
| [CommonPlayerInfo](endpoints/commonplayerinfo.md) | One player's bio: birthdate, height, weight, school, country, draft, jersey, position, team, and years active. Also headline stats and the seasons played. | `player_id` | `common_player_info`, `player_headline_stats`, `available_seasons` |
| [PlayerAwards](endpoints/playerawards.md) | Every award: All-NBA, All-Star, MVP, Player of the Week and Month, and championships. | `player_id` | `player_awards` |
| [PlayerCareerStats](endpoints/playercareerstats.md) | Season-by-season and career totals for the regular season, playoffs, All-Star, and college, plus season rankings. Career highs, season highs, and the Showcase (NBA Cup final) totals are only in `.data_sets`. | `player_id` | `season_totals_regular_season`, `career_totals_regular_season`, `season_totals_post_season`, ... |
| [PlayerProfileV2](endpoints/playerprofilev2.md) | Everything in PlayerCareerStats, plus preseason, career and season highs, and the next game. | `player_id` | `season_totals_regular_season`, `career_highs`, `season_highs`, `next_game`, ... |
| [PlayerNextNGames](endpoints/playernextngames.md) | A player's upcoming games. Set how many with `number_of_games`. | `player_id` | `next_n_games` |
| [PlayerFantasyProfileBarGraph](endpoints/playerfantasyprofilebargraph.md) | Fantasy points and key stats: season average and last five games. | `player_id`, `season` | `season_avg`, `last_five_games_avg` |
| [PlayerCareerByCollegeRollup](endpoints/playercareerbycollegerollup.md) | NBA career totals by college, seeded as a tournament bracket by region. | | `east`, `midwest`, `south`, `west` |
| [PlayerCareerByCollege](endpoints/playercareerbycollege.md) | **Failing upstream** (HTTP 500). NBA totals for the players from one college. | `college` | `player_career_by_college` |

### Game logs and search

| Endpoint | What you get | You pass | Data sets |
|---|---|---|---|
| [PlayerGameLog](endpoints/playergamelog.md) | One row per game for one player and season: the box score line, matchup, and result. | `player_id`, `season` | `player_game_log` |
| [PlayerGameLogs](endpoints/playergamelogs.md) | Game logs for one or many players, with ranks, other `MeasureType`s, and filters. | `player_id_nullable` or `team_id_nullable`, `season_nullable` | `player_game_logs` |
| [PlayerGameStreakFinder](endpoints/playergamestreakfinder.md) | Streaks of games that meet stat thresholds, such as 20 or more points. | Thresholds such as `gt_pts_nullable` | `player_game_streak_finder_results` |
| [CumeStatsPlayer](endpoints/cumestatsplayer.md) | A player's totals, averages, and maximums over the games you list, plus each game's line. | `player_id`, `game_ids`, `season` | `total_player_stats`, `game_by_game_stats` |
| [CumeStatsPlayerGames](endpoints/cumestatsplayergames.md) | A player's games for a season (game ID and matchup), to pick IDs for CumeStatsPlayer. | `player_id`, `season` | `cume_stats_player_games` |

### Splits, tracking, and comparisons

| Endpoint | What you get | You pass | Data sets |
|---|---|---|---|
| [PlayerDashboardByGeneralSplits](endpoints/playerdashboardbygeneralsplits.md) | Season stats split by home and away, wins and losses, month, before and after the All-Star break, starting or bench, and days of rest. | `player_id`, `season` | `overall_player_dashboard`, `location_player_dashboard`, `month_player_dashboard`, ... |
| [PlayerDashboardByClutch](endpoints/playerdashboardbyclutch.md) | Stats in clutch windows, such as the last 5, 3, or 1 minutes within 5 points, or the last 30 or 10 seconds within 3. | `player_id`, `season` | `overall_player_dashboard`, `last5_min5_point_player_dashboard`, ... |
| [PlayerDashboardByGameSplits](endpoints/playerdashboardbygamesplits.md) | Stats by half, period, score margin, and final margin. | `player_id`, `season` | `by_half_player_dashboard`, `by_period_player_dashboard`, ... |
| [PlayerDashboardByLastNGames](endpoints/playerdashboardbylastngames.md) | Stats over the last 5, 10, 15, and 20 games, and by game number. | `player_id`, `season` | `last5_player_dashboard`, `last10_player_dashboard`, ... |
| [PlayerDashboardByShootingSplits](endpoints/playerdashboardbyshootingsplits.md) | Shooting by distance, court area, and shot type, assisted or not, and by who made the assist. | `player_id`, `season` | `shot_area_player_dashboard`, `shot_type_player_dashboard`, `assisted_by`, ... |
| [PlayerDashboardByTeamPerformance](endpoints/playerdashboardbyteamperformance.md) | Stats by how many points the team scored and allowed, and by final margin. | `player_id`, `season` | `points_scored_player_dashboard`, `ponts_against_player_dashboard` (sic), ... |
| [PlayerDashboardByYearOverYear](endpoints/playerdashboardbyyearoveryear.md) | One row per season of the player's career. | `player_id` | `by_year_player_dashboard` |
| [PlayerDashPtPass](endpoints/playerdashptpass.md) | Passes made to and received from each teammate, with the assists and shooting that followed. | `team_id`, `player_id`, `season` | `passes_made`, `passes_received` |
| [PlayerDashPtReb](endpoints/playerdashptreb.md) | Rebounds, contested and uncontested, by shot type, shot distance, rebound distance, and number of players contesting. | `team_id`, `player_id`, `season` | `overall_rebounding`, `shot_distance_rebounding`, ... |
| [PlayerDashPtShotDefend](endpoints/playerdashptshotdefend.md) | Opponents' shooting when this player defended the shot, against their usual FG%. | `team_id`, `player_id`, `season` | `defending_shots` |
| [PlayerDashPtShots](endpoints/playerdashptshots.md) | Shooting by shot type, shot clock, dribbles, touch time, and closest defender distance. **Intermittent**: HTTP 500 on 2026-10-21. | `team_id`, `player_id`, `season` | `general_shooting`, `closest_defender_shooting`, ... |
| [PlayerCompare](endpoints/playercompare.md) | Stats for one group of players next to another. IDs are comma-separated strings. | `player_id_list`, `vs_player_id_list`, `season` | `overall_compare`, `individual` |
| [PlayerVsPlayer](endpoints/playervsplayer.md) | A player's stats with another player on and off the court, and shooting by area and distance. | `player_id`, `vs_player_id`, `season` | `overall`, `on_off_court`, `shot_area_on_court`, ... |
| [GLAlumBoxScoreSimilarityScore](endpoints/glalumboxscoresimilarityscore.md) | **Not working** (HTTP 500 with every parameter set tried). Similarity scores for G League alumni. | `person1_id`, `person2_id` | `g_league_alum_box_score_similarity_scores` |

## Teams

### Reference and history

| Endpoint | What you get | You pass | Data sets |
|---|---|---|---|
| [CommonTeamYears](endpoints/commonteamyears.md) | Every franchise with its first and last season. | | `team_years` |
| [TeamInfoCommon](endpoints/teaminfocommon.md) | A team's conference, division, record, and ranks for a season, plus per-game PTS, REB, AST, and opponent PTS ranks. | `team_id`, `season_nullable` | `team_info_common`, `team_season_ranks`, `available_seasons` |
| [TeamDetails](endpoints/teamdetails.md) | Arena and capacity, owner, GM, head coach, G League affiliate, name history, championships, conference and division titles, Hall of Famers, retired jerseys, and social accounts. NBA Cup titles (`TeamAwardsCommCup`) are only in `.data_sets`. | `team_id` | `team_background`, `team_history`, `team_awards_championships`, `team_hof`, `team_retired`, ... |
| [CommonTeamRoster](endpoints/commonteamroster.md) | Players (number, position, height, weight, age, experience, school, how acquired) and coaches. | `team_id`, `season` | `common_team_roster`, `coaches` |
| [TeamYearByYearStats](endpoints/teamyearbyyearstats.md) | One row per season: record, conference and division rank, playoff results, and totals. | `team_id` | `team_stats` |
| [FranchiseHistory](endpoints/franchisehistory.md) | Every franchise's all-time record, playoff appearances, and titles. Defunct teams are listed separately. | | `franchise_history`, `defunct_teams` |
| [FranchiseLeaders](endpoints/franchiseleaders.md) | A franchise's all-time leader in PTS, AST, REB, BLK, and STL. | `team_id` | `franchise_leaders` |
| [FranchisePlayers](endpoints/franchiseplayers.md) | Every player who played for a franchise, with totals for their time there. | `team_id` | `franchise_players` |
| [TeamHistoricalLeaders](endpoints/teamhistoricalleaders.md) | **Failing upstream** (HTTP 500). | `team_id` | `career_leaders_by_team` |

### Game logs, splits, lineups, and on/off

| Endpoint | What you get | You pass | Data sets |
|---|---|---|---|
| [TeamGameLog](endpoints/teamgamelog.md) | One row per game for a team and season, with the running record. | `team_id`, `season` | `team_game_log` |
| [TeamGameLogs](endpoints/teamgamelogs.md) | Game logs for one or many teams, with ranks, other `MeasureType`s, and filters. | `team_id_nullable`, `season_nullable` | `team_game_logs` |
| [TeamGameStreakFinder](endpoints/teamgamestreakfinder.md) | **Failing upstream** (HTTP 500). Team streaks that meet stat thresholds. | Thresholds | `team_game_streak_finder_parameters_results` |
| [CumeStatsTeam](endpoints/cumestatsteam.md) | Team and per-player totals over the games you list. | `team_id`, `game_ids`, `season` | `total_team_stats`, `game_by_game_stats` |
| [CumeStatsTeamGames](endpoints/cumestatsteamgames.md) | A team's games for a season (game ID and matchup), to pick IDs for CumeStatsTeam. | `team_id`, `season` | `cume_stats_team_games` |
| [TeamDashboardByGeneralSplits](endpoints/teamdashboardbygeneralsplits.md) | Team stats split by home and away, wins and losses, month, before and after the All-Star break, and days of rest. | `team_id`, `season` | `overall_team_dashboard`, `location_team_dashboard`, ... |
| [TeamDashboardByShootingSplits](endpoints/teamdashboardbyshootingsplits.md) | Team shooting by distance, area, and shot type, assisted or not, and by who made the assist. | `team_id`, `season` | `shot_area_team_dashboard`, `assisted_by`, ... |
| [TeamPlayerDashboard](endpoints/teamplayerdashboard.md) | Every player's stats for one team, plus the team's totals. | `team_id`, `season` | `players_season_totals`, `team_overall` |
| [TeamDashLineups](endpoints/teamdashlineups.md) | A team's lineups and their stats. | `team_id`, `season` | `lineups`, `overall` |
| [TeamPlayerOnOffSummary](endpoints/teamplayeronoffsummary.md) | For each player: minutes, plus-minus, and offensive, defensive, and net rating with them on and off the court. | `team_id`, `season` | `players_on_court_team_player_on_off_summary`, `players_off_court_team_player_on_off_summary`, ... |
| [TeamPlayerOnOffDetails](endpoints/teamplayeronoffdetails.md) | The same on and off split, with full box score stats. | `team_id`, `season` | `players_on_court_team_player_on_off_details`, `players_off_court_team_player_on_off_details`, ... |
| [TeamVsPlayer](endpoints/teamvsplayer.md) | A team's stats with an opposing player on and off the court. | `team_id`, `vs_player_id`, `season` | `overall`, `on_off_court`, `vs_player_overall`, ... |
| [TeamDashPtPass](endpoints/teamdashptpass.md) | Team passing by passer and receiver. **Intermittent**: HTTP 500 on 2026-10-21. | `team_id`, `season` | `passes_made`, `passes_received` |
| [TeamDashPtReb](endpoints/teamdashptreb.md) | Team rebounding, contested and uncontested, by shot type and distance. | `team_id`, `season` | `overall_rebounding`, `shot_distance_rebounding`, ... |
| [TeamDashPtShots](endpoints/teamdashptshots.md) | Team shooting by shot clock, dribbles, touch time, and closest defender distance. **Intermittent**: HTTP 500 on 2026-10-21. | `team_id`, `season` | `general_shooting`, `closest_defender_shooting`, ... |
| [TeamAndPlayersVsPlayers](endpoints/teamandplayersvsplayers.md) | **Not working** (HTTP 500 with every parameter set tried). Five players against five. | `team_id`, `vs_team_id`, `player_id1` to `player_id5`, `vs_player_id1` to `vs_player_id5` | `players_vs_players`, ... |

## League-wide stats

One row per player, team, or lineup.

| Endpoint | What you get | You pass | Data sets |
|---|---|---|---|
| [LeagueDashPlayerStats](endpoints/leaguedashplayerstats.md) | Every player's season stats. `MeasureType` picks the column family. Filters for team, position, college, draft, height, dates, opponent, and more. | `season` | `league_dash_player_stats` |
| [LeagueDashTeamStats](endpoints/leaguedashteamstats.md) | Every team's season stats, with the same options. | `season` | `league_dash_team_stats` |
| [LeagueDashPlayerClutch](endpoints/leaguedashplayerclutch.md) | Every player's stats in clutch time. Set the window with `clutch_time`, `ahead_behind`, and `point_diff`. | `season` | `league_dash_player_clutch` |
| [LeagueDashTeamClutch](endpoints/leaguedashteamclutch.md) | The same for teams. | `season` | `league_dash_team_clutch` |
| [LeagueDashPlayerBioStats](endpoints/leaguedashplayerbiostats.md) | Every player's age, height, weight, college, country, and draft, with PTS, REB, AST, net rating, usage, and TS%. | `season` | `league_dash_player_bio_stats` |
| [LeagueDashPlayerShotLocations](endpoints/leaguedashplayershotlocations.md) | Every player's FGM, FGA, and FG% by zone (restricted area, paint, mid-range, corner 3s, above the break 3, backcourt) or by distance range. | `season` | `shot_locations` |
| [LeagueDashTeamShotLocations](endpoints/leaguedashteamshotlocations.md) | The same for teams. | `season` | `shot_locations` |
| [LeagueDashPlayerPtShot](endpoints/leaguedashplayerptshot.md) | Every player's shooting (FG, 2PT, 3PT, eFG%, frequency) under shot filters: closest defender distance, dribbles, touch time, shot clock, and shot distance. | `season` | `league_dash_ptshots` |
| [LeagueDashTeamPtShot](endpoints/leaguedashteamptshot.md) | The same for teams. | `season` | `league_dash_ptshots` |
| [LeagueDashOppPtShot](endpoints/leaguedashoppptshot.md) | The same, for the shots each team allowed. | `season` | `league_dash_ptshots` |
| [LeagueDashPtStats](endpoints/leaguedashptstats.md) | Tracking stats for every player or team. `pt_measure_type` picks the family: speed and distance, touches, drives, passing, catch-and-shoot, and so on. | `season`, `player_or_team`, `pt_measure_type` | `league_dash_pt_stats` |
| [LeagueDashPtDefend](endpoints/leaguedashptdefend.md) | For every defender: opponents' FG% on shots they defended, against those shooters' usual FG%. | `season`, `defense_category` | `league_dash_p_tdefend` (sic) |
| [LeagueDashPtTeamDefend](endpoints/leaguedashptteamdefend.md) | The same for teams. | `season`, `defense_category` | `league_dash_pt_team_defend` |
| [LeagueHustleStatsPlayer](endpoints/leaguehustlestatsplayer.md) | Every player's hustle stats. | `season` | `hustle_stats_player` |
| [LeagueHustleStatsTeam](endpoints/leaguehustlestatsteam.md) | Every team's hustle stats. | `season` | `hustle_stats_team` |
| [LeagueDashLineups](endpoints/leaguedashlineups.md) | Every lineup in the league with its stats. Filter by team with `team_id_nullable`. | `season` | `lineups` |
| [LeagueLineupViz](endpoints/leaguelineupviz.md) | Lineups that played at least `minutes_min` minutes, with ratings, pace, and shot mix. | `minutes_min`, `season` | `league_lineup_viz` |
| [LeaguePlayerOnDetails](endpoints/leagueplayerondetails.md) | A team's stats with each of its players on the court. | `team_id`, `season` | `players_on_court_league_player_details` |
| [LeagueSeasonMatchups](endpoints/leagueseasonmatchups.md) | Defensive matchups over a season: when one player guarded another, the minutes, possessions, points, and shooting. | `season`, and optionally `off_player_id_nullable`, `def_player_id_nullable` | `season_matchups` |
| [MatchupsRollup](endpoints/matchupsrollup.md) | The same matchups summed per defender, with the share of time at each position. | `season` | `matchups_rollup` |
| [SynergyPlayTypes](endpoints/synergyplaytypes.md) | Points per possession, frequency, and percentile by play type for players or teams. The default request returned no rows on 2026-10-21, so pass a play type and grouping. | `season`, `play_type_nullable`, `type_grouping_nullable` | `synergy_play_type` |
| [PlayerEstimatedMetrics](endpoints/playerestimatedmetrics.md) | Every player's estimated offensive, defensive, and net rating, pace, usage, and rebound and turnover rates. | `season` | `player_estimated_metrics` |
| [TeamEstimatedMetrics](endpoints/teamestimatedmetrics.md) | The same for teams. | `season` | `team_estimated_metrics` |
| [GravityLeaders](endpoints/gravityleaders.md) | Gravity scores (how much a player draws the defense), on and off the ball, on the perimeter and inside. | `season` | `leaders` |
| [DunkScoreLeaders](endpoints/dunkscoreleaders.md) | Every dunk of a season, scored on jump, power, style, and defensive contest, with ball speed, vertical, and hang time. | `season` | `dunks` |

## Leaders

| Endpoint | What you get | You pass | Data sets |
|---|---|---|---|
| [AllTimeLeadersGrids](endpoints/alltimeleadersgrids.md) | The all-time top players in 19 stats. `topx` sets how many. | | `pts_leaders`, `ast_leaders`, `reb_leaders`, ... |
| [HomePageLeaders](endpoints/homepageleaders.md) | Leading players or teams in one `stat_category`, with the league average and maximum. | `season` | `home_page_leaders`, `league_average`, `league_max` |
| [HomePageV2](endpoints/homepagev2.md) | Leaders in eight stats: PTS, REB, AST, STL, FG%, FT%, 3P%, and BLK. | `season` | `home_page_stat1` to `home_page_stat8` |
| [LeadersTiles](endpoints/leaderstiles.md) | The leaders in one stat, with the all-time and last season highs. | `season` | `leaders_tiles`, `all_time_season_high`, ... |
| [FantasyWidget](endpoints/fantasywidget.md) | FanDuel and NBA fantasy points with averages, filterable by dates, opponent, and position. | `season` | `fantasy_widget_result` |
| [LeagueLeaders](endpoints/leagueleaders.md) | **Removed upstream.** Use LeagueDashPlayerStats. | | `league_leaders` |
| [AssistLeaders](endpoints/assistleaders.md) | **Removed upstream.** Use LeagueDashPlayerStats or LeagueDashTeamStats. | | `assist_leaders` |
| [AssistTracker](endpoints/assisttracker.md) | **Removed upstream.** | | `assist_tracker` |
| [DefenseHub](endpoints/defensehub.md) | **Not working** (HTTP 500 with every parameter set tried). | | `defense_hub_stat1`, ... |

## Standings and schedule

| Endpoint | What you get | You pass | Data sets |
|---|---|---|---|
| [LeagueStandingsV3](endpoints/leaguestandingsv3.md) | Standings with home, road, conference, division, and last-10 records, streaks, clinch flags, and month-by-month records. | `season` | `standings` |
| [LeagueStandings](endpoints/leaguestandings.md) | The older version of LeagueStandingsV3. | `season` | `standings` |
| [ISTStandings](endpoints/iststandings.md) | NBA Cup group standings and knockout status, with each team's Cup games. | `season` | `standings` |
| [CommonPlayoffSeries](endpoints/commonplayoffseries.md) | Every playoff game with its series ID and game number. | `season` | `playoff_series` |
| [ScheduleLeagueV2](endpoints/scheduleleaguev2.md) | The full season schedule: dates and times, arenas, teams, scores, broadcasters, and points leaders. | `season` | `season_games`, `season_weeks` |
| [ScheduleLeagueV2Int](endpoints/scheduleleaguev2int.md) | A variant of ScheduleLeagueV2. Not checked live. | `season` | `season_games`, `season_weeks` |
| [PlayoffPicture](endpoints/playoffpicture.md) | **Removed upstream.** Use LeagueStandingsV3. | | `east_conf_standings`, ... |

## Games

### Finding games

| Endpoint | What you get | You pass | Data sets |
|---|---|---|---|
| [ScoreboardV3](endpoints/scoreboardv3.md) | Every game on a date: status, line scores, game and team leaders, broadcasters, and series info. | `game_date` as `YYYY-MM-DD` | `game_header`, `line_score`, `game_leaders`, `team_leaders`, `broadcasters` |
| [ScoreboardV2](endpoints/scoreboardv2.md) | The older scoreboard. Line scores are wrong for some 2025-26 games, and it emits a `DeprecationWarning`. Use ScoreboardV3. | `game_date` | `game_header`, `line_score`, ... |
| [LeagueGameFinder](endpoints/leaguegamefinder.md) | Games matching team, player, date, and stat thresholds, as box score lines with game IDs. | `player_or_team_abbreviation`, plus filters such as `team_id_nullable` and `season_nullable` | `league_game_finder_results` |
| [LeagueGameLog](endpoints/leaguegamelog.md) | Every team's (or player's) line for every game of a season. | `season` | `league_game_log` |

### One game

All of these take `game_id`, a 10-character string.

| Endpoint | What you get | Data sets |
|---|---|---|
| [BoxScoreSummaryV3](endpoints/boxscoresummaryv3.md) | Arena, attendance, duration, officials, inactive players, line score by period, team totals (biggest lead, lead changes, bench points), and the last five meetings. | `game_summary`, `game_info`, `arena_info`, `officials`, `inactive_players`, `line_score`, `other_stats`, `last_five_meetings` |
| [BoxScoreTraditionalV3](endpoints/boxscoretraditionalv3.md) | Points, rebounds, assists, shooting, and plus-minus, with starters and bench totals. | `player_stats`, `team_stats`, `team_starter_bench_stats` |
| [BoxScoreAdvancedV3](endpoints/boxscoreadvancedv3.md) | Offensive, defensive, and net rating, usage, pace, PIE, and AST%, REB%, and TS%. | `player_stats`, `team_stats` |
| [BoxScoreFourFactorsV3](endpoints/boxscorefourfactorsv3.md) | eFG%, free throw rate, turnover rate, and offensive rebound rate, for each side. | `player_stats`, `team_stats` |
| [BoxScoreMiscV3](endpoints/boxscoremiscv3.md) | Points off turnovers, second chance, fast break, and paint points, blocks against, and fouls drawn. | `player_stats`, `team_stats` |
| [BoxScoreScoringV3](endpoints/boxscorescoringv3.md) | Share of shots and points by type (2PT, 3PT, mid-range, paint, fast break), assisted and unassisted. | `player_stats`, `team_stats` |
| [BoxScoreUsageV3](endpoints/boxscoreusagev3.md) | Each player's share of the team's shots, rebounds, assists, turnovers, and so on while on the court. | `player_stats`, `team_stats` |
| [BoxScorePlayerTrackV3](endpoints/boxscoreplayertrackv3.md) | Speed, distance, touches, passes, secondary assists, contested shooting, and rim defense. | `player_stats`, `team_stats` |
| [BoxScoreHustleV2](endpoints/boxscorehustlev2.md) | Hustle stats for the game. | `player_stats`, `team_stats` |
| [HustleStatsBoxScore](endpoints/hustlestatsboxscore.md) | The same hustle stats, with uppercase column names. | `player_stats`, `team_stats`, `hustle_stats_available` |
| [BoxScoreDefensiveV2](endpoints/boxscoredefensivev2.md) | For each defender: matchup minutes, points and shots allowed, and switches. | `player_stats`, `team_stats` |
| [BoxScoreMatchupsV3](endpoints/boxscorematchupsv3.md) | Every offensive and defensive player pairing: minutes, points, shooting, assists, and help blocks. | `player_stats` |
| [PlayByPlayV3](endpoints/playbyplayv3.md) | Every event: period, clock, score, player, description, action type, and for shots the result, distance, and x and y. | `play_by_play` |
| [GameRotation](endpoints/gamerotation.md) | Each player's stints, with in and out times, points, and plus-minus. **Intermittent**: HTTP 500 on 2026-10-21. | `home_team`, `away_team` |
| [InfographicFanDuelPlayer](endpoints/infographicfanduelplayer.md) | Each player's fantasy points and box score line. | `fan_duel_player` |
| [BoxScoreSummaryV2](endpoints/boxscoresummaryv2.md) | The older summary. Use BoxScoreSummaryV3. | `game_summary`, `line_score`, `officials`, ... |
| [BoxScoreTraditionalV2](endpoints/boxscoretraditionalv2.md) | The older traditional box score. No data for 2025-26 or later games. Use BoxScoreTraditionalV3. | `player_stats`, `team_stats`, `team_starter_bench_stats` |
| [WinProbabilityPBP](endpoints/winprobabilitypbp.md) | **Failing upstream** (HTTP 500). | `win_prob_p_bp`, `game_info` |

**Removed upstream** (no data, use the V3 in brackets): [BoxScoreAdvancedV2](endpoints/boxscoreadvancedv2.md)
(BoxScoreAdvancedV3), [BoxScoreFourFactorsV2](endpoints/boxscorefourfactorsv2.md)
(BoxScoreFourFactorsV3), [BoxScoreMiscV2](endpoints/boxscoremiscv2.md) (BoxScoreMiscV3),
[BoxScoreScoringV2](endpoints/boxscorescoringv2.md) (BoxScoreScoringV3),
[BoxScoreUsageV2](endpoints/boxscoreusagev2.md) (BoxScoreUsageV3),
[PlayByPlay](endpoints/playbyplay.md) and [PlayByPlayV2](endpoints/playbyplayv2.md) (PlayByPlayV3).

## Shots

| Endpoint | What you get | You pass | Data sets |
|---|---|---|---|
| [ShotChartDetail](endpoints/shotchartdetail.md) | Every shot with x and y, zone, distance, shot type, made or missed, period, and time left, plus league averages by zone. Pass `context_measure_simple="FGA"` for misses too. | `team_id` (0 for all), `player_id`, `season_nullable` | `shot_chart_detail`, `league_averages` |
| [ShotChartLeagueWide](endpoints/shotchartleaguewide.md) | League FG% by zone for a season. | `season` | `league_wide` |
| [ShotChartLineupDetail](endpoints/shotchartlineupdetail.md) | Every shot taken while a lineup was on the floor. `group_id` lists player IDs, as in `"-202689-203493-203501-1626174-1627827-"`. | `group_id`, `season` | `shot_chart_lineup_detail`, `shot_chart_lineup_league_average` |

Shot zones for every player or team are in
[LeagueDashPlayerShotLocations](#league-wide-stats). Its DataFrame has two column levels, so
read a zone with `df[("Restricted Area", "FGA")]`.

## Draft

| Endpoint | What you get | You pass | Data sets |
|---|---|---|---|
| [DraftHistory](endpoints/drafthistory.md) | Every pick: year, round, pick, team, and school or club. Filters for year, team, round, and college. | | `draft_history` |
| [DraftCombineStats](endpoints/draftcombinestats.md) | All combine measurements and drills for a year. | `season_all_time` | `draft_combine_stats` |
| [DraftCombinePlayerAnthro](endpoints/draftcombineplayeranthro.md) | Height with and without shoes, weight, wingspan, standing reach, body fat, and hand size. | `season_year` | `results` |
| [DraftCombineDrillResults](endpoints/draftcombinedrillresults.md) | Standing and max vertical, lane agility, three-quarter sprint, and bench press. | `season_year` | `results` |
| [DraftCombineSpotShooting](endpoints/draftcombinespotshooting.md) | Spot shooting from 15 feet, college 3, and NBA 3, at each spot. | `season_year` | `results` |
| [DraftCombineNonStationaryShooting](endpoints/draftcombinenonstationaryshooting.md) | Shooting off the dribble and on the move. | `season_year` | `results` |
| [DraftBoard](endpoints/draftboard.md) | **Failing upstream** (HTTP 500). | | `draft_board` |

## Video

These return video URLs. Except VideoStatus, they have no named data sets, so read them with
`get_dict()`.

| Endpoint | What you get | You pass |
|---|---|---|
| [VideoStatus](endpoints/videostatus.md) | Which games on a date have video and tracking data. Data set: `video_status`. | `game_date` |
| [VideoEvents](endpoints/videoevents.md) | Video for one play. | `game_id`, `game_event_id` |
| [VideoEventsAsset](endpoints/videoeventsasset.md) | Video for one play. | `game_id`, `game_event_id` |
| [VideoDetailsAsset](endpoints/videodetailsasset.md) | Clips of a player's plays that match a `context_measure_detailed`, such as every FGA. | `team_id`, `player_id`, `season` |
| [VideoDetails](endpoints/videodetails.md) | **Not working** (HTTP 500 with every parameter set tried). | `team_id`, `player_id` |

## Live data

`nba_api.live.nba.endpoints` reads the NBA's live CDN instead of stats.nba.com, and returns
dicts. ScoreBoard and Odds cover today's games.

| Endpoint | What you get | You pass |
|---|---|---|
| [ScoreBoard](../live/endpoints/scoreboard.md) | Today's games with live scores and status. | |
| [BoxScore](../live/endpoints/boxscore.md) | A live box score. | `game_id` |
| [PlayByPlay](../live/endpoints/playbyplay.md) | Live play-by-play. | `game_id` |
| [Odds](../live/endpoints/odds.md) | Betting odds for today's games. | |
