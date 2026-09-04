# NBA Stats Endpoints & Parameters Reference

An exhaustive index of prominent `nba_api.stats.endpoints` classes, parameter types, string enums, and returned dataset schemas for advanced analytics.

---

## 1. `SynergyPlayTypes` (Play-Type Efficiency)

Measures team and player performance across specific offensive and defensive basketball actions (Play Types).

- **Module**: `nba_api.stats.endpoints.synergyplaytypes`
- **Key Parameters**:
  - `player_or_team_abbreviation`: `'P'` for individual players, `'T'` for team totals.
  - `type_grouping_nullable`: `'offensive'` (default) or `'defensive'`.
  - `season`: e.g. `'2024-25'`, `'2023-24'`.
  - `season_type_all_star`: `'Regular Season'` (default), `'Playoffs'`.
  - `play_type_nullable`: **Required** (an empty string returns 0 rows).
- **Valid `play_type_nullable` Values**:
  | Play Type | Description |
  | :--- | :--- |
  | `PRBallHandler` | Pick & Roll: Ball Handler creating out of the screen |
  | `PRRollman` | Pick & Roll: Screener rolling, popping, or slipping |
  | `Isolation` | 1-on-1 isolation plays from stationary starts |
  | `Spotup` | Catch-and-shoot or straight-line drive off a kickout |
  | `Postup` | Back-to-the-basket or face-up post possessions |
  | `Handoff` | Dribble handoffs (DHO) |
  | `OffScreen` | Shooters curling, flaring, or fading off off-ball screens |
  | `Cut` | Backdoor, flash, and basket cuts |
  | `Transition` | Fast-break possessions |
  | `OffRebound` | Putbacks and second-chance scoring attempts |
  | `Misc` | Broken plays, end-of-clock heaves |
- **Key Columns**:
  - `POSS`: Total possessions logged for this play type.
  - `PTS`: Total points scored.
  - `PPP`: Points Per Possession (primary efficiency metric).
  - `PERCENTILE`: Percentile rank across the league (0.000 to 1.000).
  - `FG_PCT` / `EFG_PCT`: Raw and effective field goal percentage.
  - `TOV_POSS_PCT`: Turnover frequency per possession.
  - `SCORE_POSS_PCT`: Percentage of possessions resulting in at least 1 point.

---

## 2. `PlayerDashPtShots` (Second Spectrum Player Tracking)

Detailed tracking splits for an individual player broken down by shot type, touch time, dribbles, defender distance, and shot clock.

- **Module**: `nba_api.stats.endpoints.playerdashptshots`
- **Parameters**: `player_id` (int), `team_id=0`, `season='2024-25'`
- **Returned Datasets (`get_data_frames()`)**:
  - `[0] Overall`: Overall season shot totals.
  - `[1] General`: Shot type splits (`Catch and Shoot`, `Pullups`, `Less than 10ft`).
  - `[2] Shot Clock`: Shot clock bins (`24-22`, `22-18 Very Early`, `18-15 Early`, `15-7 Average`, `7-4 Late`, `4-0 Very Late`).
  - `[3] Dribble Range`: Dribble bins (`0 Dribbles`, `1 Dribble`, `2 Dribbles`, `3-6 Dribbles`, `7+ Dribbles`).
  - `[4] Closest Defender`: Defender distance (`0-2 Feet - Very Tight`, `2-4 Feet - Tight`, `4-6 Feet - Open`, `6+ Feet - Wide Open`).
  - `[5] Closest Defender 10ft+`: Defender distance for shots beyond 10 feet.
  - `[6] Touch Time`: Touch length (`Touch < 2 Seconds`, `Touch 2-6 Seconds`, `Touch 6+ Seconds`).
- **Key Columns**: `FGA_FREQUENCY`, `FGA`, `FGM`, `FG_PCT`, `EFG_PCT`, `FG2A`, `FG2_PCT`, `FG3A`, `FG3_PCT`.

---

## 3. `LeagueDashPlayerPtShot` (Second Spectrum League Tracking)

League-wide tracking leaderboards with customizable filters.

- **Module**: `nba_api.stats.endpoints.leaguedashplayerptshot`
- **Key Filter Parameters**:
  - `general_range_nullable`: `'Pullups'`, `'Catch and Shoot'`, `'Less than 10ft'`
  - `dribble_range_nullable`: `'0 Dribbles'`, `'1 Dribble'`, `'2 Dribbles'`, `'3-6 Dribbles'`, `'7+ Dribbles'`
  - `close_def_dist_range_nullable`: `'0-2 Feet - Very Tight'`, `'2-4 Feet - Tight'`, `'4-6 Feet - Open'`, `'6+ Feet - Wide Open'`
  - `touch_time_range_nullable`: `'Touch < 2 Seconds'`, `'Touch 2-6 Seconds'`, `'Touch 6+ Seconds'`
  - `shot_dist_range_nullable`: `'>=10.0'`, `'>=15.0'`, etc.
- **Key Columns**:
  - `PLAYER_NAME`, `PLAYER_LAST_TEAM_ABBREVIATION`, `GP`, `FGA`, `FGM`, `FG_PCT`, `EFG_PCT`, `FG2A`, `FG2_PCT`, `FG3A`, `FG3_PCT`, `FGA_FREQUENCY`.

---

## 4. `ShotChartDetail` (Shot Mechanics & Coordinates)

Pitch-level shot tracking data, containing exact physical court coordinates (`LOC_X`, `LOC_Y`) and granular shot mechanics (`ACTION_TYPE`).

- **Module**: `nba_api.stats.endpoints.shotchartdetail`
- **Key Parameters**:
  - `player_id`: Specific player ID or `0` for all players.
  - `team_id`: Specific team ID or `0` for all teams.
  - `context_measure_simple`: **Must be `'FGA'`** (if set to `'PTS'`, only made shots are returned, omitting misses).
  - `season_nullable`: e.g. `'2024-25'`.
- **Common `ACTION_TYPE` Strings**:
  - **Step-backs**: `'Step Back Jump shot'`, `'Step Back Bank Jump Shot'`, `'Turnaround Step Back Jump Shot'`
  - **Fadeaways**: `'Fadeaway Jump Shot'`, `'Turnaround Fadeaway shot'`, `'Turnaround Fadeaway Bank Jump Shot'`
  - **Pull-ups**: `'Pullup Jump shot'`, `'Running Pull-Up Jump Shot'`, `'Pullup Bank Jump Shot'`
  - **Floaters**: `'Floating Jump Shot'`, `'Driving Floating Jump Shot'`, `'Driving Floating Bank Jump Shot'`
  - **Hooks**: `'Hook Shot'`, `'Turnaround Hook Shot'`, `'Driving Hook Shot'`
  - **Layups & Dunks**: `'Driving Layup Shot'`, `'Cutting Dunk Shot'`, `'Alley Oop Dunk Shot'`, `'Running Dunk Shot'`
- **Key Columns**:
  - `LOC_X`, `LOC_Y`: Court coordinates in tenths of a foot (hoop centered at `0, 0`).
  - `SHOT_DISTANCE`: Shot distance in feet.
  - `SHOT_ZONE_BASIC`: Restricted Area, In The Paint (Non-RA), Mid-Range, Left Corner 3, Right Corner 3, Above the Break 3.
  - `SHOT_TYPE`: `'2PT Field Goal'` or `'3PT Field Goal'`.
  - `SHOT_ATTEMPTED_FLAG`: Always `1`.
  - `SHOT_MADE_FLAG`: `1` if made, `0` if missed.

---

## 5. `LeagueDashPlayerStats` (Advanced Metrics)

Comprehensive player leaderboard including four factors, possession ratings, and adjusted efficiencies.

- **Module**: `nba_api.stats.endpoints.leaguedashplayerstats`
- **Key Parameters**:
  - `measure_type_detailed_defense`: `'Advanced'` (default for advanced analytics), `'Base'`, `'Usage'`, `'Defense'`.
  - `per_mode_detailed`: `'PerGame'`, `'Totals'`.
- **Key Advanced Columns**:
  - `TS_PCT`: True Shooting Percentage ($\frac{\text{PTS}}{2 \times (\text{FGA} + 0.44 \times \text{FTA})}$).
  - `USG_PCT`: Usage Rate (percentage of team plays used while on floor).
  - `OFF_RATING` / `DEF_RATING` / `NET_RATING`: Offensive, Defensive, and Net points per 100 possessions.
  - `AST_PCT`: Assist Percentage (% of teammate field goals assisted while on floor).
  - `REB_PCT`: Rebound Percentage (% of available rebounds grabbed).
  - `PACE`: Team possessions per 48 minutes while on floor.
  - `PIE`: Player Impact Estimate (NBA's all-in-one box score metric).

---

## 6. `LeagueHustleStatsPlayer` (Hustle & Non-Box Score Metrics)

Tracks energy plays and defensive actions not reflected in traditional box scores.

- **Module**: `nba_api.stats.endpoints.leaguehustlestatsplayer`
- **Key Parameters**: `per_mode_time`: `'PerGame'`, `'Totals'`.
- **Key Columns**:
  - `DEFLECTIONS`: Passes deflected by a defender.
  - `CHARGES_DRAWN`: Offensive fouls drawn.
  - `CONTESTED_SHOTS`: Total shots closed out on by defender (`2PT` + `3PT`).
  - `SCREEN_ASSISTS` / `SCREEN_AST_PTS`: Direct points produced off off-ball and on-ball screens.
  - `LOOSE_BALLS_RECOVERED`: Loose ball diving/recovering on offense and defense.
