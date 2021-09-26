# Endpoint Parameters


## _Active_
No available information.


## _ActiveFlag_
No available information.


## _ActivePlayers_

#### Class `ActivePlayers`
##### Patterns 
 - `^(Y)|(N)$`

Variable Name | Value
------------ | -------------
_**no**_ `default` | `N`
_**yes**_ | `Y`

## _ActiveStreaksOnly_
No available information.


## _ActiveTeamsOnly_
No available information.


## _AheadBehind_

#### Class `AheadBehind`
##### Patterns 
 - `^((Ahead or Behind)|(Behind or Tied)|(Ahead or Tied))?$`

Variable Name | Value
------------ | -------------
_**ahead_or_behind**_ `default` | `Ahead or Behind`
_**ahead_or_tied**_ | `Ahead or Tied`
_**behind_or_tied**_ | `Behind or Tied`

#### Class `AheadBehindNullable`
##### Patterns 
 - `^((Ahead or Behind)|(Ahead or Tied)|(Behind or Tied))?$`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**ahead_or_behind**_ | `Ahead or Behind`
_**ahead_or_tied**_ | `Ahead or Tied`
_**behind_or_tied**_ | `Behind or Tied`

## _AllStar_
No available information.


## _BtrOPPAST_
No available information.


## _BtrOPPBLK_
No available information.


## _BtrOPPDREB_
No available information.


## _BtrOPPFG3A_
No available information.


## _BtrOPPFG3M_
No available information.


## _BtrOPPFG3PCT_
No available information.


## _BtrOPPFGA_
No available information.


## _BtrOPPFGM_
No available information.


## _BtrOPPFG_PCT_
No available information.


## _BtrOPPFTA_
No available information.


## _BtrOPPFTM_
No available information.


## _BtrOPPFT_PCT_
No available information.


## _BtrOPPOREB_
No available information.


## _BtrOPPPF_
No available information.


## _BtrOPPPTS_
No available information.


## _BtrOPPPTS2NDCHANCE_
No available information.


## _BtrOPPPTSFB_
No available information.


## _BtrOPPPTSOFFTOV_
No available information.


## _BtrOPPPTSPAINT_
No available information.


## _BtrOPPREB_
No available information.


## _BtrOPPSTL_
No available information.


## _BtrOPPTOV_
No available information.


## _CloseDefDistRange_
No available information.


## _ClutchTime_

#### Class `ClutchTime`
##### Patterns 
 - `^((Last 5 Minutes)|(Last 4 Minutes)|(Last 3 Minutes)|(Last 2 Minutes)|(Last 1 Minute)|(Last 30 Seconds)|(Last 10 Seconds))?$`

Variable Name | Value
------------ | -------------
_**last_5_minutes**_ `default` | `Last 5 Minutes`
_**last_10_seconds**_ | `Last 10 Seconds`
_**last_1_minute**_ | `Last 1 Minute`
_**last_2_minutes**_ | `Last 2 Minutes`
_**last_30_seconds**_ | `Last 30 Seconds`
_**last_3_minutes**_ | `Last 3 Minutes`
_**last_4_minutes**_ | `Last 4 Minutes`

#### Class `ClutchTimeNullable`
##### Patterns 
 - `^((Last 5 Minutes)|(Last 4 Minutes)|(Last 3 Minutes)|(Last 2 Minutes)|(Last 1 Minute)|(Last 30 Seconds)|(Last 10 Seconds))?$`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**last_10_seconds**_ | `Last 10 Seconds`
_**last_1_minute**_ | `Last 1 Minute`
_**last_2_minutes**_ | `Last 2 Minutes`
_**last_30_seconds**_ | `Last 30 Seconds`
_**last_3_minutes**_ | `Last 3 Minutes`
_**last_4_minutes**_ | `Last 4 Minutes`
_**last_5_minutes**_ | `Last 5 Minutes`

## _College_
No available information.


## _Conference_

#### Class `ConferenceNullable`
##### Patterns 
 - `((East)|(West))?`
 - `^((East)|(West))?$`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**east**_ | `East`
_**west**_ | `West`

## _ContextFilter_
No available information.


## _ContextMeasure_

#### Class `ContextMeasureDetailed`
##### Patterns 
 - `^((PTS)|(FGM)|(FGA)|(FG_PCT)|(FG3M)|(FG3A)|(FG3_PCT)|(FTM)|(FTA)|(OREB)|(DREB)|(AST)|(FGM_AST)|(FG3_AST)|(STL)|(BLK)|(BLKA)|(TOV)|(POSS_END_FT)|(PTS_PAINT)|(PTS_FB)|(PTS_OFF_TOV)|(PTS_2ND_CHANCE)|(REB)|(TM_FGM)|(TM_FGA)|(TM_FG3M)|(TM_FG3A)|(TM_FTM)|(TM_FTA)|(TM_OREB)|(TM_DREB)|(TM_REB)|(TM_TEAM_REB)|(TM_AST)|(TM_STL)|(TM_BLK)|(TM_BLKA)|(TM_TOV)|(TM_TEAM_TOV)|(TM_PF)|(TM_PFD)|(TM_PTS)|(TM_PTS_PAINT)|(TM_PTS_FB)|(TM_PTS_OFF_TOV)|(TM_PTS_2ND_CHANCE)|(TM_FGM_AST)|(TM_FG3_AST)|(TM_POSS_END_FT)|(OPP_FTM)|(OPP_FTA)|(OPP_OREB)|(OPP_DREB)|(OPP_REB)|(OPP_TEAM_REB)|(OPP_AST)|(OPP_STL)|(OPP_BLK)|(OPP_BLKA)|(OPP_TOV)|(OPP_TEAM_TOV)|(OPP_PF)|(OPP_PFD)|(OPP_PTS)|(OPP_PTS_PAINT)|(OPP_PTS_FB)|(OPP_PTS_OFF_TOV)|(OPP_PTS_2ND_CHANCE)|(OPP_FGM_AST)|(OPP_FG3_AST)|(OPP_POSS_END_FT)|(PTS))$`
 - `^((FGM)|(FGA)|(FG_PCT)|(FG3M)|(FG3A)|(FG3_PCT)|(FTM)|(FTA)|(OREB)|(DREB)|(AST)|(FGM_AST)|(FG3_AST)|(STL)|(BLK)|(BLKA)|(TOV)|(PF)|(PFD)|(POSS_END_FT)|(PTS_PAINT)|(PTS_FB)|(PTS_OFF_TOV)|(PTS_2ND_CHANCE)|(REB)|(TM_FGM)|(TM_FGA)|(TM_FG3M)|(TM_FG3A)|(TM_FTM)|(TM_FTA)|(TM_OREB)|(TM_DREB)|(TM_REB)|(TM_TEAM_REB)|(TM_AST)|(TM_STL)|(TM_BLK)|(TM_BLKA)|(TM_TOV)|(TM_TEAM_TOV)|(TM_PF)|(TM_PFD)|(TM_PTS)|(TM_PTS_PAINT)|(TM_PTS_FB)|(TM_PTS_OFF_TOV)|(TM_PTS_2ND_CHANCE)|(TM_FGM_AST)|(TM_FG3_AST)|(TM_POSS_END_FT)|(OPP_FGM)|(OPP_FGA)|(OPP_FG3M)|(OPP_FG3A)|(OPP_FTM)|(OPP_FTA)|(OPP_OREB)|(OPP_DREB)|(OPP_REB)|(OPP_TEAM_REB)|(OPP_AST)|(OPP_STL)|(OPP_BLK)|(OPP_BLKA)|(OPP_TOV)|(OPP_TEAM_TOV)|(OPP_PF)|(OPP_PFD)|(OPP_PTS)|(OPP_PTS_PAINT)|(OPP_PTS_FB)|(OPP_PTS_OFF_TOV)|(OPP_PTS_2ND_CHANCE)|(OPP_FGM_AST)|(OPP_FG3_AST)|(OPP_POSS_END_FT)|(PTS))$`

Variable Name | Value
------------ | -------------
_**pts**_ `default` | `PTS`
_**ast**_ | `AST`
_**blk**_ | `BLK`
_**blka**_ | `BLKA`
_**dreb**_ | `DREB`
_**fg3_ast**_ | `FG3_AST`
_**fg3_pct**_ | `FG3_PCT`
_**fg3a**_ | `FG3A`
_**fg3m**_ | `FG3M`
_**fg_pct**_ | `FG_PCT`
_**fga**_ | `FGA`
_**fgm**_ | `FGM`
_**fgm_ast**_ | `FGM_AST`
_**fta**_ | `FTA`
_**ftm**_ | `FTM`
_**opp_ast**_ | `OPP_AST`
_**opp_blk**_ | `OPP_BLK`
_**opp_blka**_ | `OPP_BLKA`
_**opp_dreb**_ | `OPP_DREB`
_**opp_fg3_ast**_ | `OPP_FG3_AST`
_**opp_fgm_ast**_ | `OPP_FGM_AST`
_**opp_fta**_ | `OPP_FTA`
_**opp_ftm**_ | `OPP_FTM`
_**opp_oreb**_ | `OPP_OREB`
_**opp_pf**_ | `OPP_PF`
_**opp_pfd**_ | `OPP_PFD`
_**opp_poss_end_ft**_ | `OPP_POSS_END_FT`
_**opp_pts**_ | `OPP_PTS`
_**opp_pts_2nd_chance**_ | `OPP_PTS_2ND_CHANCE`
_**opp_pts_fb**_ | `OPP_PTS_FB`
_**opp_pts_off_tov**_ | `OPP_PTS_OFF_TOV`
_**opp_pts_paint**_ | `OPP_PTS_PAINT`
_**opp_reb**_ | `OPP_REB`
_**opp_stl**_ | `OPP_STL`
_**opp_team_reb**_ | `OPP_TEAM_REB`
_**opp_team_tov**_ | `OPP_TEAM_TOV`
_**opp_tov**_ | `OPP_TOV`
_**oreb**_ | `OREB`
_**poss_end_ft**_ | `POSS_END_FT`
_**pts_2nd_chance**_ | `PTS_2ND_CHANCE`
_**pts_fb**_ | `PTS_FB`
_**pts_off_tov**_ | `PTS_OFF_TOV`
_**pts_paint**_ | `PTS_PAINT`
_**reb**_ | `REB`
_**stl**_ | `STL`
_**tm_ast**_ | `TM_AST`
_**tm_blk**_ | `TM_BLK`
_**tm_blka**_ | `TM_BLKA`
_**tm_dreb**_ | `TM_DREB`
_**tm_fg3_ast**_ | `TM_FG3_AST`
_**tm_fg3a**_ | `TM_FG3A`
_**tm_fg3m**_ | `TM_FG3M`
_**tm_fga**_ | `TM_FGA`
_**tm_fgm**_ | `TM_FGM`
_**tm_fgm_ast**_ | `TM_FGM_AST`
_**tm_fta**_ | `TM_FTA`
_**tm_ftm**_ | `TM_FTM`
_**tm_oreb**_ | `TM_OREB`
_**tm_pf**_ | `TM_PF`
_**tm_pfd**_ | `TM_PFD`
_**tm_poss_end_ft**_ | `TM_POSS_END_FT`
_**tm_pts**_ | `TM_PTS`
_**tm_pts_2nd_chance**_ | `TM_PTS_2ND_CHANCE`
_**tm_pts_fb**_ | `TM_PTS_FB`
_**tm_pts_off_tov**_ | `TM_PTS_OFF_TOV`
_**tm_pts_paint**_ | `TM_PTS_PAINT`
_**tm_reb**_ | `TM_REB`
_**tm_stl**_ | `TM_STL`
_**tm_team_reb**_ | `TM_TEAM_REB`
_**tm_team_tov**_ | `TM_TEAM_TOV`
_**tm_tov**_ | `TM_TOV`
_**tov**_ | `TOV`

#### Class `ContextMeasureSimple`
##### Patterns 
 - `^((PTS)|(FGM)|(FGA)|(FG_PCT)|(FG3M)|(FG3A)|(FG3_PCT)|(PF)|(EFG_PCT)|(TS_PCT)|(PTS_FB)|(PTS_OFF_TOV)|(PTS_2ND_CHANCE)|(PF))?$`

Variable Name | Value
------------ | -------------
_**pts**_ `default` | `PTS`
_**efg_pct**_ | `EFG_PCT`
_**fg3_pct**_ | `FG3_PCT`
_**fg3a**_ | `FG3A`
_**fg3m**_ | `FG3M`
_**fg_pct**_ | `FG_PCT`
_**fga**_ | `FGA`
_**fgm**_ | `FGM`
_**pf**_ | `PF`
_**pts_2nd_chance**_ | `PTS_2ND_CHANCE`
_**pts_fb**_ | `PTS_FB`
_**pts_off_tov**_ | `PTS_OFF_TOV`
_**ts_pct**_ | `TS_PCT`

#### Class `ContextMeasureSimpleNullable`
##### Patterns 
 - `^((PTS)|(FGM)|(FGA)|(FG_PCT)|(FG3M)|(FG3A)|(FG3_PCT)|(PF)|(EFG_PCT)|(TS_PCT)|(PTS_FB)|(PTS_OFF_TOV)|(PTS_2ND_CHANCE)|(PF))?$`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**efg_pct**_ | `EFG_PCT`
_**fg3_pct**_ | `FG3_PCT`
_**fg3a**_ | `FG3A`
_**fg3m**_ | `FG3M`
_**fg_pct**_ | `FG_PCT`
_**fga**_ | `FGA`
_**fgm**_ | `FGM`
_**pf**_ | `PF`
_**pts**_ | `PTS`
_**pts_2nd_chance**_ | `PTS_2ND_CHANCE`
_**pts_fb**_ | `PTS_FB`
_**pts_off_tov**_ | `PTS_OFF_TOV`
_**ts_pct**_ | `TS_PCT`

## _Counter_
No available information.


## _Country_
No available information.


## _DLeagueTeamID_
No available information.


## _DateFrom_
No available information.


## _DateTo_
No available information.


## _DayOffset_

#### Class `DayOffset`
##### Patterns 
 - `^-{0,1}\d+$`

Variable Name | Value
------------ | -------------
_**days**_ | `days()`

## _DefPlayerID_
No available information.


## _DefTeamID_
No available information.


## _DefenseCategory_

#### Class `DefenseCategory`
##### Patterns 
 - `^((Overall)|(3 Pointers)|(2 Pointers)|(Less Than 6Ft)|(Less Than 10Ft)|(Greater Than 15Ft))?$`

Variable Name | Value
------------ | -------------
_**overall**_ `default` | `Overall`
_**greater_than_15ft**_ | `Greater Than 15Ft`
_**less_than_10ft**_ | `Less Than 10Ft`
_**less_than_6ft**_ | `Less Than 6Ft`
_**threes**_ | `3 Pointers`
_**twos**_ | `2 Pointers`

#### Class `DefenseCategoryNullable`
##### Patterns 
 - `^((Overall)|(3 Pointers)|(2 Pointers)|(Less Than 6Ft)|(Less Than 10Ft)|(Greater Than 15Ft))?$`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**greater_than_15ft**_ | `Greater Than 15Ft`
_**less_than_10ft**_ | `Less Than 10Ft`
_**less_than_6ft**_ | `Less Than 6Ft`
_**overall**_ | `Overall`
_**threes**_ | `3 Pointers`
_**twos**_ | `2 Pointers`

## _Direction_

#### Class `Direction`
##### Patterns 
 - `^(ASC)|(DESC)$`

Variable Name | Value
------------ | -------------
_**asc**_ `default` | `ASC`
_**desc**_ | `DESC`

## _DistanceRange_

#### Class `DistanceRange`
##### Patterns 
 - `^(5ft Range)|(8ft Range)|(By Zone)$`

Variable Name | Value
------------ | -------------
_**by_zone**_ `default` | `By Zone`
_**range_5ft**_ | `5ft Range`
_**range_8ft**_ | `8ft Range`

## _Division_

#### Class `DivisionNullable`
##### Patterns 
 - `^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**east**_ | `East`
_**west**_ | `West`

#### Class `DivisionSimpleNullable`
##### Patterns 
 - `((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest))?`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**atlantic**_ | `Atlantic`
_**central**_ | `Central`
_**northwest**_ | `Northwest`
_**pacific**_ | `Pacific`
_**southeast**_ | `Southeast`
_**southwest**_ | `Southwest`

## _DraftNumber_
No available information.


## _DraftPick_
No available information.


## _DraftRound_
No available information.


## _DraftTeamID_
No available information.


## _DraftYear_
No available information.


## _DribbleRange_
No available information.


## _EastPlayer1_
No available information.


## _EastPlayer2_
No available information.


## _EastPlayer3_
No available information.


## _EastPlayer4_
No available information.


## _EastPlayer5_
No available information.


## _EndPeriod_

Variable Name | Value
------------ | -------------
_**all**_ `default` | `0`
_**first**_ | `1`
_**fourth**_ | `4`
_**overtime**_ | `overtime()`
_**quarter**_ | `quarter()`
_**second**_ | `2`
_**third**_ | `3`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**all**_ | `0`
_**first**_ | `1`
_**fourth**_ | `4`
_**overtime**_ | `overtime()`
_**quarter**_ | `quarter()`
_**second**_ | `2`
_**third**_ | `3`

## _EndRange_

Variable Name | Value
------------ | -------------


Variable Name | Value
------------ | -------------
_**none**_ `default` | 

## _EqAST_
No available information.


## _EqBLK_
No available information.


## _EqDD_
No available information.


## _EqDREB_
No available information.


## _EqFG3A_
No available information.


## _EqFG3M_
No available information.


## _EqFG3_PCT_
No available information.


## _EqFGA_
No available information.


## _EqFGM_
No available information.


## _EqFG_PCT_
No available information.


## _EqFTA_
No available information.


## _EqFTM_
No available information.


## _EqFT_PCT_
No available information.


## _EqMINUTES_
No available information.


## _EqOPPPTS2NDCHANCE_
No available information.


## _EqOPPPTSFB_
No available information.


## _EqOPPPTSOFFTOV_
No available information.


## _EqOPPPTSPAINT_
No available information.


## _EqOREB_
No available information.


## _EqPF_
No available information.


## _EqPTS_
No available information.


## _EqPTS2NDCHANCE_
No available information.


## _EqPTSFB_
No available information.


## _EqPTSOFFTOV_
No available information.


## _EqPTSPAINT_
No available information.


## _EqREB_
No available information.


## _EqSTL_
No available information.


## _EqTD_
No available information.


## _EqTOV_
No available information.


## _GROUP_ID_
No available information.


## _GameDate_

Variable Name | Value
------------ | -------------
_**get_date**_ | `get_date()`
_**get_date_format**_ | `get_date_format()`

## _GameEventID_
No available information.


## _GameID_
No available information.


## _GameIDs_
No available information.


## _GameScope_

#### Class `GameScopeDetailed`
##### Patterns 
 - `^(Season)|(Last 10)|(Yesterday)|(Finals)$`

Variable Name | Value
------------ | -------------
_**season**_ `default` | `Season`
_**finals**_ | `Finals`
_**last_10**_ | `Last 10`
_**yesterday**_ | `Yesterday`

#### Class `GameScopeSimpleNullable`
##### Patterns 
 - `((Yesterday)|(Last 10))?`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**last_10**_ | `Last 10`
_**yesterday**_ | `Yesterday`

## _GameSegment_

#### Class `GameSegmentNullable`
##### Patterns 
 - `^((First Half)|(Overtime)|(Second Half))?$`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**first_half**_ | `First Half`
_**overtime**_ | `Overtime`
_**second_half**_ | `Second Half`

## _GeneralRange_
No available information.


## _GraphEndSeason_

#### Class `SeasonNullable`
##### Patterns 
 - `^(\d{4}-\d{2})?$`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**current_datetime**_ | `2021-09-26 16:21:20.725385`
_**current_season**_ | `2020-21`
_**current_season_year**_ | `2020`

## _GraphStartSeason_

#### Class `SeasonNullable`
##### Patterns 
 - `^(\d{4}-\d{2})?$`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**current_datetime**_ | `2021-09-26 16:21:20.725385`
_**current_season**_ | `2020-21`
_**current_season_year**_ | `2020`

## _GraphStat_
No available information.


## _GroupQuantity_

Variable Name | Value
------------ | -------------
_**players**_ | `players()`

## _GtAST_
No available information.


## _GtBLK_
No available information.


## _GtDD_
No available information.


## _GtDREB_
No available information.


## _GtFG3A_
No available information.


## _GtFG3M_
No available information.


## _GtFG3_PCT_
No available information.


## _GtFGA_
No available information.


## _GtFGM_
No available information.


## _GtFG_PCT_
No available information.


## _GtFTA_
No available information.


## _GtFTM_
No available information.


## _GtFT_PCT_
No available information.


## _GtMINUTES_
No available information.


## _GtOPPAST_
No available information.


## _GtOPPBLK_
No available information.


## _GtOPPDREB_
No available information.


## _GtOPPFG3A_
No available information.


## _GtOPPFG3M_
No available information.


## _GtOPPFG3PCT_
No available information.


## _GtOPPFGA_
No available information.


## _GtOPPFGM_
No available information.


## _GtOPPFG_PCT_
No available information.


## _GtOPPFTA_
No available information.


## _GtOPPFTM_
No available information.


## _GtOPPFT_PCT_
No available information.


## _GtOPPOREB_
No available information.


## _GtOPPPF_
No available information.


## _GtOPPPTS_
No available information.


## _GtOPPPTS2NDCHANCE_
No available information.


## _GtOPPPTSFB_
No available information.


## _GtOPPPTSOFFTOV_
No available information.


## _GtOPPPTSPAINT_
No available information.


## _GtOPPREB_
No available information.


## _GtOPPSTL_
No available information.


## _GtOPPTOV_
No available information.


## _GtOREB_
No available information.


## _GtPF_
No available information.


## _GtPTS_
No available information.


## _GtPTS2NDCHANCE_
No available information.


## _GtPTSFB_
No available information.


## _GtPTSOFFTOV_
No available information.


## _GtPTSPAINT_
No available information.


## _GtREB_
No available information.


## _GtSTL_
No available information.


## _GtTD_
No available information.


## _GtTOV_
No available information.


## _Height_
No available information.


## _Historical_
No available information.


## _IsOnlyCurrentSeason_
No available information.


## _LStreak_
No available information.


## _LastNGames_

Variable Name | Value
------------ | -------------
_**games**_ | `games()`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**games**_ | `games()`

## _LeagueID_

#### Class `LeagueID`
##### Patterns 
 - `^\d{2}$`
 - `^(00)|(10)|(20)$`
 - `(00)|(20)|(10)`
 - `^(00)|(20)$`
 - `^((00)|(20))?$`
 - `^(00)|(20)|(10)$`

Variable Name | Value
------------ | -------------
_**nba**_ `default` | `00`
_**aba**_ | `01`
_**g_league**_ | `20`
_**wnba**_ | `10`

#### Class `LeagueIDNullable`
##### Patterns 
 - `(00)|(20)|(10)`
 - `^((00)|(20))?$`
 - `^\d{2}$`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**aba**_ | `01`
_**g_league**_ | `20`
_**nba**_ | `00`
_**wnba**_ | `10`

## _Location_

#### Class `LocationNullable`
##### Patterns 
 - `^((Home)|(Road))?$`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**home**_ | `Home`
_**road**_ | `Road`

## _LtAST_
No available information.


## _LtBLK_
No available information.


## _LtDD_
No available information.


## _LtDREB_
No available information.


## _LtFG3A_
No available information.


## _LtFG3M_
No available information.


## _LtFG3_PCT_
No available information.


## _LtFGA_
No available information.


## _LtFGM_
No available information.


## _LtFG_PCT_
No available information.


## _LtFTA_
No available information.


## _LtFTM_
No available information.


## _LtFT_PCT_
No available information.


## _LtMINUTES_
No available information.


## _LtOPPAST_
No available information.


## _LtOPPBLK_
No available information.


## _LtOPPDREB_
No available information.


## _LtOPPFG3A_
No available information.


## _LtOPPFG3M_
No available information.


## _LtOPPFG3PCT_
No available information.


## _LtOPPFGA_
No available information.


## _LtOPPFGM_
No available information.


## _LtOPPFG_PCT_
No available information.


## _LtOPPFTA_
No available information.


## _LtOPPFTM_
No available information.


## _LtOPPFT_PCT_
No available information.


## _LtOPPOREB_
No available information.


## _LtOPPPF_
No available information.


## _LtOPPPTS_
No available information.


## _LtOPPPTS2NDCHANCE_
No available information.


## _LtOPPPTSFB_
No available information.


## _LtOPPPTSOFFTOV_
No available information.


## _LtOPPPTSPAINT_
No available information.


## _LtOPPREB_
No available information.


## _LtOPPSTL_
No available information.


## _LtOPPTOV_
No available information.


## _LtOREB_
No available information.


## _LtPF_
No available information.


## _LtPTS_
No available information.


## _LtPTS2NDCHANCE_
No available information.


## _LtPTSFB_
No available information.


## _LtPTSOFFTOV_
No available information.


## _LtPTSPAINT_
No available information.


## _LtREB_
No available information.


## _LtSTL_
No available information.


## _LtTD_
No available information.


## _LtTOV_
No available information.


## _MeasureType_

#### Class `MeasureTypeBase`
##### Patterns 
 - `^(Base)$`

Variable Name | Value
------------ | -------------
_**base**_ `default` | `Base`

#### Class `MeasureTypeDetailed`
##### Patterns 
 - `^(Base)|(Advanced)|(Misc)|(Four Factors)|(Scoring)|(Opponent)|(Usage)$`

Variable Name | Value
------------ | -------------
_**base**_ `default` | `Base`
_**advanced**_ | `Advanced`
_**four_factors**_ | `Four Factors`
_**misc**_ | `Misc`
_**opponent**_ | `Opponent`
_**scoring**_ | `Scoring`
_**usage**_ | `Usage`

#### Class `MeasureTypeDetailedDefense`
##### Patterns 
 - `^(Base)|(Advanced)|(Misc)|(Four Factors)|(Scoring)|(Opponent)|(Usage)|(Defense)$`

Variable Name | Value
------------ | -------------
_**base**_ `default` | `Base`
_**advanced**_ | `Advanced`
_**defense**_ | `Defense`
_**four_factors**_ | `Four Factors`
_**misc**_ | `Misc`
_**opponent**_ | `Opponent`
_**scoring**_ | `Scoring`
_**usage**_ | `Usage`

#### Class `MeasureTypeSimple`
##### Patterns 
 - `^(Base)|(Opponent)$`

Variable Name | Value
------------ | -------------
_**base**_ `default` | `Base`
_**opponent**_ | `Opponent`
No available information.


## _MinGames_
No available information.


## _MinutesMin_
No available information.


## _Month_

Variable Name | Value
------------ | -------------
_**month**_ | `month()`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**month**_ | `month()`

## _NBATeamID_
No available information.


## _NumberOfGames_

Variable Name | Value
------------ | -------------
_**games**_ | `games()`

## _OffPlayerID_
No available information.


## _OffTeamID_
No available information.


## _OppTeamID_
No available information.


## _OpponentTeamID_
No available information.


## _Outcome_

#### Class `OutcomeNullable`
##### Patterns 
 - `^((W)|(L))?$`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**loss**_ | `L`
_**win**_ | `W`

## _OverallPick_
No available information.


## _PORound_
No available information.


## _PaceAdjust_

#### Class `PaceAdjust`
##### Patterns 
 - `^(Y)|(N)$`

Variable Name | Value
------------ | -------------
_**no**_ `default` | `N`
_**yes**_ | `Y`

#### Class `PaceAdjustNo`
##### Patterns 
 - `^(N)$`

Variable Name | Value
------------ | -------------
_**no**_ `default` | `N`

## _PerMode_

#### Class `PerMode36`
##### Patterns 
 - `^(Totals)|(PerGame)|(Per36)$`

Variable Name | Value
------------ | -------------
_**totals**_ `default` | `Totals`
_**per_36**_ | `Per36`
_**per_game**_ | `PerGame`

#### Class `PerMode48`
##### Patterns 
 - `^(Totals)|(PerGame)|(Per48)$`

Variable Name | Value
------------ | -------------
_**totals**_ `default` | `Totals`
_**per_48**_ | `Per48`
_**per_game**_ | `PerGame`

#### Class `PerModeDetailed`
##### Patterns 
 - `^(Totals)|(PerGame)|(MinutesPer)|(Per48)|(Per40)|(Per36)|(PerMinute)|(PerPossession)|(PerPlay)|(Per100Possessions)|(Per100Plays)$`

Variable Name | Value
------------ | -------------
_**totals**_ `default` | `Totals`
_**minutes_per**_ | `MinutesPer`
_**per_100_plays**_ | `Per100Plays`
_**per_100_possessions**_ | `Per100Possessions`
_**per_36**_ | `Per36`
_**per_40**_ | `Per40`
_**per_48**_ | `Per48`
_**per_game**_ | `PerGame`
_**per_minute**_ | `PerMinute`
_**per_play**_ | `PerPlay`
_**per_possession**_ | `PerPossession`

#### Class `PerModeSimple`
##### Patterns 
 - `^(Totals)|(PerGame)$`

Variable Name | Value
------------ | -------------
_**totals**_ `default` | `Totals`
_**per_game**_ | `PerGame`

#### Class `PerModeSimpleNullable`
##### Patterns 
 - `^(Totals)|(PerGame)$`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**per_game**_ | `PerGame`
_**totals**_ | `Totals`

#### Class `PerModeTime`
##### Patterns 
 - `^(Totals)|(PerGame)|(Per48)|(Per40)|(Per36)|(PerMinute)$`

Variable Name | Value
------------ | -------------
_**totals**_ `default` | `Totals`
_**minutes_per**_ | `MinutesPer`
_**per_36**_ | `Per36`
_**per_40**_ | `Per40`
_**per_48**_ | `Per48`
_**per_game**_ | `PerGame`

## _Period_

Variable Name | Value
------------ | -------------
_**all**_ `default` | `0`
_**first**_ | `1`
_**fourth**_ | `4`
_**overtime**_ | `overtime()`
_**quarter**_ | `quarter()`
_**second**_ | `2`
_**third**_ | `3`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**all**_ | `0`
_**first**_ | `1`
_**fourth**_ | `4`
_**overtime**_ | `overtime()`
_**quarter**_ | `quarter()`
_**second**_ | `2`
_**third**_ | `3`

## _Person1Id_
No available information.


## _Person1LeagueId_

Variable Name | Value
------------ | -------------
_**nba**_ `default` | `00`
_**aba**_ | `01`
_**g_league**_ | `20`
_**wnba**_ | `10`

## _Person1Season_

Variable Name | Value
------------ | -------------
_**current_season_year**_ `default` | `2020`
_**current_datetime**_ | `2021-09-26 16:21:20.725385`

## _Person1SeasonType_

Variable Name | Value
------------ | -------------
_**regular**_ `default` | `Regular Season`
_**preseason**_ | `Pre Season`

## _Person2Id_
No available information.


## _Person2LeagueId_

Variable Name | Value
------------ | -------------
_**nba**_ `default` | `00`
_**aba**_ | `01`
_**g_league**_ | `20`
_**wnba**_ | `10`

## _Person2Season_

Variable Name | Value
------------ | -------------
_**current_season_year**_ `default` | `2020`
_**current_datetime**_ | `2021-09-26 16:21:20.725385`

## _Person2SeasonType_

Variable Name | Value
------------ | -------------
_**regular**_ `default` | `Regular Season`
_**preseason**_ | `Pre Season`

## _PlayType_

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**cut**_ | `Cut`
_**handoff**_ | `Handoff`
_**isolation**_ | `Isolation`
_**misc**_ | `Misc`
_**off_screen**_ | `OffScreen`
_**post_up**_ | `Postup`
_**pr_ball_handler**_ | `PRBallHandler`
_**pr_roll_man**_ | `PRRollman`
_**putbacks**_ | `OffRebound`
_**spot_up**_ | `Spotup`
_**transition**_ | `Transition`

## _PlayerExperience_

#### Class `PlayerExperienceNullable`
##### Patterns 
 - `((Rookie)|(Sophomore)|(Veteran))?`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**rookie**_ | `Rookie`
_**sophomore**_ | `Sophomore`
_**veteran**_ | `Veteran`

## _PlayerID_
No available information.


## _PlayerID1_
No available information.


## _PlayerID2_
No available information.


## _PlayerID3_
No available information.


## _PlayerID4_
No available information.


## _PlayerID5_
No available information.


## _PlayerIDList_
No available information.


## _PlayerOrTeam_

#### Class `PlayerOrTeam`
##### Patterns 
 - `^(Player)|(Team)$`

Variable Name | Value
------------ | -------------
_**team**_ `default` | `Team`
_**player**_ | `Player`

#### Class `PlayerOrTeamAbbreviation`
##### Patterns 
 - `^(P)|(T)$`

Variable Name | Value
------------ | -------------
_**team**_ `default` | `T`
_**player**_ | `P`

## _PlayerPosition_

#### Class `PlayerPositionAbbreviationNullable`
##### Patterns 
 - `((F)|(C)|(G)|(C-F)|(F-C)|(F-G)|(G-F))?`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**center**_ | `C`
_**center_forward**_ | `C-F`
_**forward**_ | `F`
_**forward_center**_ | `F-C`
_**forward_guard**_ | `F-G`
_**guard**_ | `G`
_**guard_forward**_ | `G-F`

#### Class `PlayerPositionNullable`
##### Patterns 
 - `^((Guard)|(Center)|(Forward))?$`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**center**_ | `Center`
_**forward**_ | `Forward`
_**guard**_ | `Guard`

## _PlayerScope_

#### Class `PlayerScope`
##### Patterns 
 - `^(All Players)|(Rookies)$`

Variable Name | Value
------------ | -------------
_**all_players**_ `default` | `All Players`
_**rookies**_ | `Rookies`

## _PlayerTeamID_
No available information.


## _PlusMinus_

#### Class `PlusMinus`
##### Patterns 
 - `^(Y)|(N)$`

Variable Name | Value
------------ | -------------
_**no**_ `default` | `N`
_**yes**_ | `Y`

#### Class `PlusMinusNo`
##### Patterns 
 - `^(N)$`

Variable Name | Value
------------ | -------------
_**no**_ `default` | `N`

## _PointDiff_

Variable Name | Value
------------ | -------------
_**points**_ | `points()`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**points**_ | `points()`

## _Position_

#### Class `PositionNullable`
##### Patterns 
 - `^(Guard|Forward|Center)?$`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**center**_ | `Center`
_**forward**_ | `Forward`
_**guard**_ | `Guard`

## _PtMeasureType_

#### Class `PtMeasureType`
##### Patterns 
 - `^(SpeedDistance)|(Rebounding)|(Possessions)|(CatchShoot)|(PullUpShot)|(Defense)|(Drives)|(Passing)|(ElbowTouch)|(PostTouch)|(PaintTouch)|(Efficiency)$`

Variable Name | Value
------------ | -------------
_**speed_distance**_ `default` | `SpeedDistance`
_**catch_shoot**_ | `CatchShoot`
_**defense**_ | `Defense`
_**drives**_ | `Drives`
_**efficiency**_ | `Efficiency`
_**elbowTouch**_ | `ElbowTouch`
_**paintTouch**_ | `PaintTouch`
_**passing**_ | `Passing`
_**possessions**_ | `Possessions`
_**postTouch**_ | `PostTouch`
_**pull_up_shot**_ | `PullUpShot`
_**rebounding**_ | `Rebounding`

## _RangeType_

Variable Name | Value
------------ | -------------


Variable Name | Value
------------ | -------------
_**none**_ `default` | 

## _Rank_

#### Class `Rank`
##### Patterns 
 - `^(Y)|(N)$`

Variable Name | Value
------------ | -------------
_**no**_ `default` | `N`
_**yes**_ | `Y`

#### Class `RankNo`
##### Patterns 
 - `^(N)$`

Variable Name | Value
------------ | -------------
_**no**_ `default` | `N`

## _RookieYear_

#### Class `SeasonNullable`
##### Patterns 
 - `^(\d{4}-\d{2})?$`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**current_datetime**_ | `2021-09-26 16:21:20.725385`
_**current_season**_ | `2020-21`
_**current_season_year**_ | `2020`

## _RoundNum_
No available information.


## _RoundPick_
No available information.


## _RunType_

Variable Name | Value
------------ | -------------


## _Runtype_

Variable Name | Value
------------ | -------------


## _School_
No available information.


## _Scope_

#### Class `Scope`
##### Patterns 
 - `^(RS)|(S)|(Rookies)$`

Variable Name | Value
------------ | -------------
_**s**_ `default` | `S`
_**rookies**_ | `Rookies`
_**rs**_ | `RS`

## _Season_

#### Class `Season`
##### Patterns 
 - `^(\d{4}-\d{2})$`
 - `^\d{4}-\d{2}$`
 - `^(\d{4}-\d{2})?$`

Variable Name | Value
------------ | -------------
_**current_season**_ `default` | `2020-21`
_**current_datetime**_ | `2021-09-26 16:21:20.725385`
_**current_season_year**_ | `2020`

#### Class `SeasonAll`
##### Patterns 
 - `^(\d{4}-\d{2})|(ALL)$`

Variable Name | Value
------------ | -------------
_**current_season**_ `default` | `2020-21`
_**all**_ | `ALL`
_**current_datetime**_ | `2021-09-26 16:21:20.725385`
_**current_season_year**_ | `2020`

#### Class `SeasonAllNullable`
##### Patterns 
 - `^(\d{4}-\d{2})|(ALL)$`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**all**_ | `ALL`
_**current_datetime**_ | `2021-09-26 16:21:20.725385`
_**current_season**_ | `2020-21`
_**current_season_year**_ | `2020`

#### Class `SeasonAllTime`
##### Patterns 
 - `^(\d{4}-\d{2})|(ALLTIME)$`

Variable Name | Value
------------ | -------------
_**current_season**_ `default` | `2020-21`
_**alltime**_ | `ALLTIME`
_**current_datetime**_ | `2021-09-26 16:21:20.725385`
_**current_season_year**_ | `2020`

#### Class `SeasonAll_Time`
##### Patterns 
 - `^(\d{4}-\d{2})|(All Time)$`

Variable Name | Value
------------ | -------------
_**current_season**_ `default` | `2020-21`
_**all_time**_ | `All Time`
_**current_datetime**_ | `2021-09-26 16:21:20.725385`
_**current_season_year**_ | `2020`

#### Class `SeasonNullable`
##### Patterns 
 - `^(\d{4}-\d{2})?$`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**current_datetime**_ | `2021-09-26 16:21:20.725385`
_**current_season**_ | `2020-21`
_**current_season_year**_ | `2020`

#### Class `SeasonYear`
##### Patterns 
 - `^\d{4}$`

Variable Name | Value
------------ | -------------
_**current_season_year**_ `default` | `2020`
_**current_datetime**_ | `2021-09-26 16:21:20.725385`

#### Class `SeasonYearNullable`
##### Patterns 
 - `^\d{4}$`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**current_datetime**_ | `2021-09-26 16:21:20.725385`
_**current_season_year**_ | `2020`

## _SeasonID_

#### Class `SeasonID`
##### Patterns 
 - `^\d{5}$`

Variable Name | Value
------------ | -------------
_**current_season_year**_ `default` | `22020`
_**current_datetime**_ | `2021-09-26 16:21:20.725385`
_**get_season_id**_ | `get_season_id()`
No available information.


## _SeasonSegment_

#### Class `SeasonSegmentNullable`
##### Patterns 
 - `^((Post All-Star)|(Pre All-Star))?$`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**post_all_star**_ | `Post All-Star`
_**pre_all_star**_ | `Pre All-Star`

## _SeasonType_

#### Class `SeasonType`
##### Patterns 
 - `^(Regular Season)|(Pre Season)$`

Variable Name | Value
------------ | -------------
_**regular**_ `default` | `Regular Season`
_**preseason**_ | `Pre Season`

#### Class `SeasonTypeAllStar`
##### Patterns 
 - `^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$`
 - `^((Regular Season)|(Pre Season)|(Playoffs)|(All Star))?$`
 - `^(Regular Season)|(Playoffs)|(All Star)|(Pre Season)$`
 - `^(Regular Season)|(Pre Season)|(Playoffs)|(All-Star)|(All Star)|(Preseason)$`
 - `^(Regular Season)|(Pre Season)|(Playoffs)|(All-Star)|(All Star)$`
 - `^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)|(All-Star)$`

Variable Name | Value
------------ | -------------
_**regular**_ `default` | `Regular Season`
_**all_star**_ | `All Star`
_**playoffs**_ | `Playoffs`
_**preseason**_ | `Pre Season`

#### Class `SeasonTypeAllStarNullable`
##### Patterns 
 - `^(Regular Season)|(Pre Season)|(Playoffs)|(All-Star)|(All Star)|(Preseason)$`
 - `^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**playoffs**_ | `Playoffs`
_**preseason**_ | `Pre Season`
_**regular**_ | `Regular Season`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**playoffs**_ | `Playoffs`
_**preseason**_ | `Pre Season`
_**regular**_ | `Regular Season`

#### Class `SeasonType`
##### Patterns 
 - `^(Regular Season)|(Pre Season)|(Playoffs)$`
 - `^(Regular Season)|(Pre Season)|(Playoffs)|(Pre-Season)$`

Variable Name | Value
------------ | -------------
_**regular**_ `default` | `Regular Season`
_**preseason**_ | `Pre Season`

## _SeasonYear_

#### Class `Season`
##### Patterns 
 - `^\d{4}-\d{2}$`
 - `^(\d{4}-\d{2})|(\d{4})$`

Variable Name | Value
------------ | -------------
_**current_season**_ `default` | `2020-21`
_**current_datetime**_ | `2021-09-26 16:21:20.725385`
_**current_season_year**_ | `2020`

#### Class `SeasonAll_Time`
##### Patterns 
 - `^(\d{4}-\d{2})|(All Time)$`

Variable Name | Value
------------ | -------------
_**current_season**_ `default` | `2020-21`
_**all_time**_ | `All Time`
_**current_datetime**_ | `2021-09-26 16:21:20.725385`
_**current_season_year**_ | `2020`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**current_datetime**_ | `2021-09-26 16:21:20.725385`
_**current_season**_ | `2020-21`
_**current_season_year**_ | `2020`

Variable Name | Value
------------ | -------------
_**current_season_year**_ `default` | `2020`
_**current_datetime**_ | `2021-09-26 16:21:20.725385`

## _SeriesID_
No available information.


## _ShotClockRange_

#### Class `ShotClockRangeNullable`
##### Patterns 
 - `((24-22)|(22-18 Very Early)|(18-15 Early)|(15-7 Average)|(7-4 Late)|(4-0 Very Late)|(ShotClock Off))?`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**calculate_range**_ | `calculate_range()`
_**range_0_4**_ | `4-0 Very Late`
_**range_15_18**_ | `18-15 Early`
_**range_18_22**_ | `22-18 Very Early`
_**range_22_24**_ | `24-22`
_**range_4_7**_ | `7-4 Late`
_**range_7_15**_ | `15-7 Average`
_**shot_clock_off**_ | `ShotClock Off`

## _ShotDistRange_
No available information.


## _Sorter_

#### Class `Sorter`
##### Patterns 
 - `^((FGM)|(FGA)|(FG_PCT)|(FG3M)|(FG3A)|(FG3_PCT)|(FTM)|(FTA)|(FT_PCT)|(OREB)|(DREB)|(AST)|(STL)|(BLK)|(TOV)|(REB)|(PTS)|(DATE))$`

Variable Name | Value
------------ | -------------
_**date**_ `default` | `DATE`
_**ast**_ | `AST`
_**blk**_ | `BLK`
_**dreb**_ | `DREB`
_**fg3_pct**_ | `FG3_PCT`
_**fg3a**_ | `FG3A`
_**fg3m**_ | `FG3M`
_**fg_pct**_ | `FG_PCT`
_**fga**_ | `FGA`
_**fgm**_ | `FGM`
_**ft_pct**_ | `FT_PCT`
_**fta**_ | `FTA`
_**ftm**_ | `FTM`
_**oreb**_ | `OREB`
_**pts**_ | `PTS`
_**reb**_ | `REB`
_**stl**_ | `STL`
_**tov**_ | `TOV`

## _StartPeriod_

Variable Name | Value
------------ | -------------
_**all**_ `default` | `0`
_**first**_ | `1`
_**fourth**_ | `4`
_**overtime**_ | `overtime()`
_**quarter**_ | `quarter()`
_**second**_ | `2`
_**third**_ | `3`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**all**_ | `0`
_**first**_ | `1`
_**fourth**_ | `4`
_**overtime**_ | `overtime()`
_**quarter**_ | `quarter()`
_**second**_ | `2`
_**third**_ | `3`

## _StartRange_

Variable Name | Value
------------ | -------------


Variable Name | Value
------------ | -------------
_**none**_ `default` | 

## _StarterBench_

#### Class `StarterBenchNullable`
##### Patterns 
 - `((Starters)|(Bench))?`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**bench**_ | `Bench`
_**starters**_ | `Starters`

## _Stat_

#### Class `Stat`
##### Patterns 
 - `^(PTS)|(REB)|(AST)|(FG_PCT)|(FT_PCT)|(FG3_PCT)|(STL)|(BLK)$`

Variable Name | Value
------------ | -------------
_**points**_ `default` | `PTS`
_**assists**_ | `AST`
_**blocks**_ | `BLK`
_**field_goal_percent**_ | `FG_PCT`
_**free_throw_percent**_ | `FT_PCT`
_**rebounds**_ | `REB`
_**steals**_ | `STL`
_**threes_percent**_ | `FG3_PCT`

## _StatCategory_

#### Class `StatCategory`
##### Patterns 
 - `^(Points)|(Rebounds)|(Assists)|(Defense)|(Clutch)|(Playmaking)|(Efficiency)|(Fast Break)|(Scoring Breakdown)$`

Variable Name | Value
------------ | -------------
_**points**_ `default` | `Points`
_**assists**_ | `Assists`
_**clutch**_ | `Clutch`
_**defense**_ | `Defense`
_**efficiency**_ | `Efficiency`
_**fast_break**_ | `Fast Break`
_**playmaking**_ | `Playmaking`
_**rebounds**_ | `Rebounds`
_**scoring_breakdown**_ | `Scoring Breakdown`

Variable Name | Value
------------ | -------------
_**pts**_ `default` | `PTS`
_**ast**_ | `AST`
_**blk**_ | `BLK`
_**dreb**_ | `DREB`
_**fg3_pct**_ | `FG3_PCT`
_**fg3a**_ | `FG3A`
_**fg3m**_ | `FG3M`
_**fg_pct**_ | `FG_PCT`
_**fga**_ | `FGA`
_**fgm**_ | `FGM`
_**fta**_ | `FTA`
_**ftm**_ | `FTM`
_**oreb**_ | `OREB`
_**reb**_ | `REB`
_**stl**_ | `STL`
_**tov**_ | `TOV`

## _StatType_

#### Class `StatType`
##### Patterns 
 - `^(Traditional)|(Advanced)|(Tracking)$`

Variable Name | Value
------------ | -------------
_**traditional**_ `default` | `Traditional`
_**advanced**_ | `Advanced`
_**tracking**_ | `Tracking`

## _TeamID_
No available information.


## _TodaysOpponent_
No available information.


## _TodaysPlayers_

#### Class `TodaysPlayers`
##### Patterns 
 - `^(Y)|(N)$`

Variable Name | Value
------------ | -------------
_**no**_ `default` | `N`
_**yes**_ | `Y`

## _TopX_
No available information.


## _TouchTimeRange_
No available information.


## _TwoWay_
No available information.


## _TypeGrouping_

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**defensive**_ | `defensive`
_**offensive**_ | `offensive`

## _VsConference_

#### Class `ConferenceNullable`
##### Patterns 
 - `^((East)|(West))?$`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**east**_ | `East`
_**west**_ | `West`

## _VsDivision_

#### Class `DivisionNullable`
##### Patterns 
 - `^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$`

Variable Name | Value
------------ | -------------
_**none**_ `default` | 
_**east**_ | `East`
_**west**_ | `West`

## _VsPlayerID_
No available information.


## _VsPlayerID1_
No available information.


## _VsPlayerID2_
No available information.


## _VsPlayerID3_
No available information.


## _VsPlayerID4_
No available information.


## _VsPlayerID5_
No available information.


## _VsPlayerIDList_
No available information.


## _VsTeamID_
No available information.


## _WStreak_
No available information.


## _Weight_
No available information.


## _WestPlayer1_
No available information.


## _WestPlayer2_
No available information.


## _WestPlayer3_
No available information.


## _WestPlayer4_
No available information.


## _WestPlayer5_
No available information.


## _WrsOPPAST_
No available information.


## _WrsOPPBLK_
No available information.


## _WrsOPPDREB_
No available information.


## _WrsOPPFG3A_
No available information.


## _WrsOPPFG3M_
No available information.


## _WrsOPPFG3PCT_
No available information.


## _WrsOPPFGA_
No available information.


## _WrsOPPFGM_
No available information.


## _WrsOPPFG_PCT_
No available information.


## _WrsOPPFTA_
No available information.


## _WrsOPPFTM_
No available information.


## _WrsOPPFT_PCT_
No available information.


## _WrsOPPOREB_
No available information.


## _WrsOPPPF_
No available information.


## _WrsOPPPTS_
No available information.


## _WrsOPPPTS2NDCHANCE_
No available information.


## _WrsOPPPTSFB_
No available information.


## _WrsOPPPTSOFFTOV_
No available information.


## _WrsOPPPTSPAINT_
No available information.


## _WrsOPPREB_
No available information.


## _WrsOPPSTL_
No available information.


## _WrsOPPTOV_
No available information.


## _YearsExperience_
No available information.

