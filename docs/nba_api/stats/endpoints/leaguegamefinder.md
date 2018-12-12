# LeagueGameFinder
##### [nba_api/stats/endpoints/leaguegamefinder.py](https://github.com/swar/nba_api/blob/master/nba_api/stats/endpoints/leaguegamefinder.py)

##### Endpoint URL
>[https://stats.nba.com/stats/leaguegamefinder](https://stats.nba.com/stats/leaguegamefinder)

##### Valid URL
>[https://stats.nba.com/stats/leaguegamefinder?Conference=&DateFrom=&DateTo=&Division=&DraftNumber=&DraftRound=&DraftTeamID=&DraftYear=&EqAST=&EqBLK=&EqDD=&EqDREB=&EqFG3A=&EqFG3M=&EqFG3_PCT=&EqFGA=&EqFGM=&EqFG_PCT=&EqFTA=&EqFTM=&EqFT_PCT=&EqMINUTES=&EqOREB=&EqPF=&EqPTS=&EqREB=&EqSTL=&EqTD=&EqTOV=&GameID=&GtAST=&GtBLK=&GtDD=&GtDREB=&GtFG3A=&GtFG3M=&GtFG3_PCT=&GtFGA=&GtFGM=&GtFG_PCT=&GtFTA=&GtFTM=&GtFT_PCT=&GtMINUTES=&GtOREB=&GtPF=&GtPTS=&GtREB=&GtSTL=&GtTD=&GtTOV=&LeagueID=&Location=&LtAST=&LtBLK=&LtDD=&LtDREB=&LtFG3A=&LtFG3M=&LtFG3_PCT=&LtFGA=&LtFGM=&LtFG_PCT=&LtFTA=&LtFTM=&LtFT_PCT=&LtMINUTES=&LtOREB=&LtPF=&LtPTS=&LtREB=&LtSTL=&LtTD=&LtTOV=&Outcome=&PORound=&PlayerID=&PlayerOrTeam=T&RookieYear=&Season=&SeasonSegment=&SeasonType=&StarterBench=&TeamID=&VsConference=&VsDivision=&VsTeamID=&YearsExperience=](https://stats.nba.com/stats/leaguegamefinder?Conference=&DateFrom=&DateTo=&Division=&DraftNumber=&DraftRound=&DraftTeamID=&DraftYear=&EqAST=&EqBLK=&EqDD=&EqDREB=&EqFG3A=&EqFG3M=&EqFG3_PCT=&EqFGA=&EqFGM=&EqFG_PCT=&EqFTA=&EqFTM=&EqFT_PCT=&EqMINUTES=&EqOREB=&EqPF=&EqPTS=&EqREB=&EqSTL=&EqTD=&EqTOV=&GameID=&GtAST=&GtBLK=&GtDD=&GtDREB=&GtFG3A=&GtFG3M=&GtFG3_PCT=&GtFGA=&GtFGM=&GtFG_PCT=&GtFTA=&GtFTM=&GtFT_PCT=&GtMINUTES=&GtOREB=&GtPF=&GtPTS=&GtREB=&GtSTL=&GtTD=&GtTOV=&LeagueID=&Location=&LtAST=&LtBLK=&LtDD=&LtDREB=&LtFG3A=&LtFG3M=&LtFG3_PCT=&LtFGA=&LtFGM=&LtFG_PCT=&LtFTA=&LtFTM=&LtFT_PCT=&LtMINUTES=&LtOREB=&LtPF=&LtPTS=&LtREB=&LtSTL=&LtTD=&LtTOV=&Outcome=&PORound=&PlayerID=&PlayerOrTeam=T&RookieYear=&Season=&SeasonSegment=&SeasonType=&StarterBench=&TeamID=&VsConference=&VsDivision=&VsTeamID=&YearsExperience=)

## Parameters
API Parameter Name | Python Parameter Class | Python Parameter Variable | Pattern | Required | Nullable
------------ | ------------ | ------------ | :-----------: | :---: | :---:
_**PlayerOrTeam**_ | [PlayerOrTeamAbbreviation](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerOrTeam) | player_or_team_abbreviation | `^(P)\|(T)$` | `Y` |  | 
_**YearsExperience**_ | [YearsExperienceNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#YearsExperience) | years_experience_nullable |  |  | `Y` | 
_**VsTeamID**_ | [VsTeamIDNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsTeamID) | vs_team_id_nullable |  |  | `Y` | 
_**VsDivision**_ | [VsDivisionNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsDivision) | vs_division_nullable |  |  | `Y` | 
_**VsConference**_ | [VsConferenceNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsConference) | vs_conference_nullable |  |  | `Y` | 
_**TeamID**_ | [TeamIDNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TeamID) | team_id_nullable |  |  | `Y` | 
_**StarterBench**_ | [StarterBenchNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#StarterBench) | starter_bench_nullable |  |  | `Y` | 
_**SeasonType**_ | [SeasonTypeNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType) | season_type_nullable |  |  | `Y` | 
_**SeasonSegment**_ | [SeasonSegmentNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonSegment) | season_segment_nullable |  |  | `Y` | 
_**Season**_ | [SeasonNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season) | season_nullable |  |  | `Y` | 
_**RookieYear**_ | [RookieYearNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#RookieYear) | rookie_year_nullable |  |  | `Y` | 
_**PlayerID**_ | [PlayerIDNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerID) | player_id_nullable |  |  | `Y` | 
_**PORound**_ | [PORoundNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PORound) | po_round_nullable |  |  | `Y` | 
_**Outcome**_ | [OutcomeNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Outcome) | outcome_nullable |  |  | `Y` | 
_**LtTOV**_ | [LtTOVNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtTOV) | lt_tov_nullable |  |  | `Y` | 
_**LtTD**_ | [LtTDNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtTD) | lt_td_nullable |  |  | `Y` | 
_**LtSTL**_ | [LtSTLNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtSTL) | lt_stl_nullable |  |  | `Y` | 
_**LtREB**_ | [LtREBNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtREB) | lt_reb_nullable |  |  | `Y` | 
_**LtPTS**_ | [LtPTSNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtPTS) | lt_pts_nullable |  |  | `Y` | 
_**LtPF**_ | [LtPFNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtPF) | lt_pf_nullable |  |  | `Y` | 
_**LtOREB**_ | [LtOREBNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtOREB) | lt_oreb_nullable |  |  | `Y` | 
_**LtMINUTES**_ | [LtMINUTESNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtMINUTES) | lt_minutes_nullable |  |  | `Y` | 
_**LtFT_PCT**_ | [LtFT_PCTNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtFT_PCT) | lt_ft_pct_nullable |  |  | `Y` | 
_**LtFTM**_ | [LtFTMNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtFTM) | lt_ftm_nullable |  |  | `Y` | 
_**LtFTA**_ | [LtFTANullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtFTA) | lt_fta_nullable |  |  | `Y` | 
_**LtFG_PCT**_ | [LtFG_PCTNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtFG_PCT) | lt_fg_pct_nullable |  |  | `Y` | 
_**LtFGM**_ | [LtFGMNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtFGM) | lt_fgm_nullable |  |  | `Y` | 
_**LtFGA**_ | [LtFGANullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtFGA) | lt_fga_nullable |  |  | `Y` | 
_**LtFG3_PCT**_ | [LtFG3_PCTNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtFG3_PCT) | lt_fg3_pct_nullable |  |  | `Y` | 
_**LtFG3M**_ | [LtFG3MNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtFG3M) | lt_fg3m_nullable |  |  | `Y` | 
_**LtFG3A**_ | [LtFG3ANullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtFG3A) | lt_fg3a_nullable |  |  | `Y` | 
_**LtDREB**_ | [LtDREBNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtDREB) | lt_dreb_nullable |  |  | `Y` | 
_**LtDD**_ | [LtDDNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtDD) | lt_dd_nullable |  |  | `Y` | 
_**LtBLK**_ | [LtBLKNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtBLK) | lt_blk_nullable |  |  | `Y` | 
_**LtAST**_ | [LtASTNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtAST) | lt_ast_nullable |  |  | `Y` | 
_**Location**_ | [LocationNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Location) | location_nullable |  |  | `Y` | 
_**LeagueID**_ | [LeagueIDNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id_nullable |  |  | `Y` | 
_**GtTOV**_ | [GtTOVNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtTOV) | gt_tov_nullable |  |  | `Y` | 
_**GtTD**_ | [GtTDNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtTD) | gt_td_nullable |  |  | `Y` | 
_**GtSTL**_ | [GtSTLNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtSTL) | gt_stl_nullable |  |  | `Y` | 
_**GtREB**_ | [GtREBNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtREB) | gt_reb_nullable |  |  | `Y` | 
_**GtPTS**_ | [GtPTSNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtPTS) | gt_pts_nullable |  |  | `Y` | 
_**GtPF**_ | [GtPFNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtPF) | gt_pf_nullable |  |  | `Y` | 
_**GtOREB**_ | [GtOREBNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtOREB) | gt_oreb_nullable |  |  | `Y` | 
_**GtMINUTES**_ | [GtMINUTESNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtMINUTES) | gt_minutes_nullable |  |  | `Y` | 
_**GtFT_PCT**_ | [GtFT_PCTNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtFT_PCT) | gt_ft_pct_nullable |  |  | `Y` | 
_**GtFTM**_ | [GtFTMNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtFTM) | gt_ftm_nullable |  |  | `Y` | 
_**GtFTA**_ | [GtFTANullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtFTA) | gt_fta_nullable |  |  | `Y` | 
_**GtFG_PCT**_ | [GtFG_PCTNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtFG_PCT) | gt_fg_pct_nullable |  |  | `Y` | 
_**GtFGM**_ | [GtFGMNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtFGM) | gt_fgm_nullable |  |  | `Y` | 
_**GtFGA**_ | [GtFGANullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtFGA) | gt_fga_nullable |  |  | `Y` | 
_**GtFG3_PCT**_ | [GtFG3_PCTNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtFG3_PCT) | gt_fg3_pct_nullable |  |  | `Y` | 
_**GtFG3M**_ | [GtFG3MNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtFG3M) | gt_fg3m_nullable |  |  | `Y` | 
_**GtFG3A**_ | [GtFG3ANullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtFG3A) | gt_fg3a_nullable |  |  | `Y` | 
_**GtDREB**_ | [GtDREBNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtDREB) | gt_dreb_nullable |  |  | `Y` | 
_**GtDD**_ | [GtDDNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtDD) | gt_dd_nullable |  |  | `Y` | 
_**GtBLK**_ | [GtBLKNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtBLK) | gt_blk_nullable |  |  | `Y` | 
_**GtAST**_ | [GtASTNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtAST) | gt_ast_nullable |  |  | `Y` | 
_**GameID**_ | [GameIDNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameID) | game_id_nullable |  |  | `Y` | 
_**EqTOV**_ | [EqTOVNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqTOV) | eq_tov_nullable |  |  | `Y` | 
_**EqTD**_ | [EqTDNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqTD) | eq_td_nullable |  |  | `Y` | 
_**EqSTL**_ | [EqSTLNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqSTL) | eq_stl_nullable |  |  | `Y` | 
_**EqREB**_ | [EqREBNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqREB) | eq_reb_nullable |  |  | `Y` | 
_**EqPTS**_ | [EqPTSNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqPTS) | eq_pts_nullable |  |  | `Y` | 
_**EqPF**_ | [EqPFNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqPF) | eq_pf_nullable |  |  | `Y` | 
_**EqOREB**_ | [EqOREBNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqOREB) | eq_oreb_nullable |  |  | `Y` | 
_**EqMINUTES**_ | [EqMINUTESNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqMINUTES) | eq_minutes_nullable |  |  | `Y` | 
_**EqFT_PCT**_ | [EqFT_PCTNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqFT_PCT) | eq_ft_pct_nullable |  |  | `Y` | 
_**EqFTM**_ | [EqFTMNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqFTM) | eq_ftm_nullable |  |  | `Y` | 
_**EqFTA**_ | [EqFTANullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqFTA) | eq_fta_nullable |  |  | `Y` | 
_**EqFG_PCT**_ | [EqFG_PCTNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqFG_PCT) | eq_fg_pct_nullable |  |  | `Y` | 
_**EqFGM**_ | [EqFGMNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqFGM) | eq_fgm_nullable |  |  | `Y` | 
_**EqFGA**_ | [EqFGANullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqFGA) | eq_fga_nullable |  |  | `Y` | 
_**EqFG3_PCT**_ | [EqFG3_PCTNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqFG3_PCT) | eq_fg3_pct_nullable |  |  | `Y` | 
_**EqFG3M**_ | [EqFG3MNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqFG3M) | eq_fg3m_nullable |  |  | `Y` | 
_**EqFG3A**_ | [EqFG3ANullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqFG3A) | eq_fg3a_nullable |  |  | `Y` | 
_**EqDREB**_ | [EqDREBNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqDREB) | eq_dreb_nullable |  |  | `Y` | 
_**EqDD**_ | [EqDDNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqDD) | eq_dd_nullable |  |  | `Y` | 
_**EqBLK**_ | [EqBLKNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqBLK) | eq_blk_nullable |  |  | `Y` | 
_**EqAST**_ | [EqASTNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqAST) | eq_ast_nullable |  |  | `Y` | 
_**DraftYear**_ | [DraftYearNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DraftYear) | draft_year_nullable |  |  | `Y` | 
_**DraftTeamID**_ | [DraftTeamIDNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DraftTeamID) | draft_team_id_nullable |  |  | `Y` | 
_**DraftRound**_ | [DraftRoundNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DraftRound) | draft_round_nullable |  |  | `Y` | 
_**DraftNumber**_ | [DraftNumberNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DraftNumber) | draft_number_nullable |  |  | `Y` | 
_**Division**_ | [DivisionSimpleNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Division) | division_simple_nullable |  |  | `Y` | 
_**DateTo**_ | [DateToNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateTo) | date_to_nullable |  |  | `Y` | 
_**DateFrom**_ | [DateFromNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateFrom) | date_from_nullable |  |  | `Y` | 
_**Conference**_ | [ConferenceNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Conference) | conference_nullable |  |  | `Y` | 

## Data Sets
#### LeagueGameFinderResults `league_game_finder_results`
```text
['SEASON_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'GAME_ID', 'GAME_DATE', 'MATCHUP', 'WL', 'MIN', 'PTS', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PLUS_MINUS']
```


## JSON
```json
{
    "data_sets": {
        "LeagueGameFinderResults": [
            "SEASON_ID",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "GAME_ID",
            "GAME_DATE",
            "MATCHUP",
            "WL",
            "MIN",
            "PTS",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "STL",
            "BLK",
            "TOV",
            "PF",
            "PLUS_MINUS"
        ]
    },
    "endpoint": "LeagueGameFinder",
    "last_validated_date": "2018-12-11",
    "nullable_parameters": [
        "Conference",
        "DateFrom",
        "DateTo",
        "Division",
        "DraftNumber",
        "DraftRound",
        "DraftTeamID",
        "DraftYear",
        "EqAST",
        "EqBLK",
        "EqDD",
        "EqDREB",
        "EqFG3A",
        "EqFG3M",
        "EqFG3_PCT",
        "EqFGA",
        "EqFGM",
        "EqFG_PCT",
        "EqFTA",
        "EqFTM",
        "EqFT_PCT",
        "EqMINUTES",
        "EqOREB",
        "EqPF",
        "EqPTS",
        "EqREB",
        "EqSTL",
        "EqTD",
        "EqTOV",
        "GameID",
        "GtAST",
        "GtBLK",
        "GtDD",
        "GtDREB",
        "GtFG3A",
        "GtFG3M",
        "GtFG3_PCT",
        "GtFGA",
        "GtFGM",
        "GtFG_PCT",
        "GtFTA",
        "GtFTM",
        "GtFT_PCT",
        "GtMINUTES",
        "GtOREB",
        "GtPF",
        "GtPTS",
        "GtREB",
        "GtSTL",
        "GtTD",
        "GtTOV",
        "LeagueID",
        "Location",
        "LtAST",
        "LtBLK",
        "LtDD",
        "LtDREB",
        "LtFG3A",
        "LtFG3M",
        "LtFG3_PCT",
        "LtFGA",
        "LtFGM",
        "LtFG_PCT",
        "LtFTA",
        "LtFTM",
        "LtFT_PCT",
        "LtMINUTES",
        "LtOREB",
        "LtPF",
        "LtPTS",
        "LtREB",
        "LtSTL",
        "LtTD",
        "LtTOV",
        "Outcome",
        "PORound",
        "PlayerID",
        "RookieYear",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "StarterBench",
        "TeamID",
        "VsConference",
        "VsDivision",
        "VsTeamID",
        "YearsExperience"
    ],
    "parameter_patterns": {
        "Conference": null,
        "DateFrom": null,
        "DateTo": null,
        "Division": null,
        "DraftNumber": null,
        "DraftRound": null,
        "DraftTeamID": null,
        "DraftYear": null,
        "EqAST": null,
        "EqBLK": null,
        "EqDD": null,
        "EqDREB": null,
        "EqFG3A": null,
        "EqFG3M": null,
        "EqFG3_PCT": null,
        "EqFGA": null,
        "EqFGM": null,
        "EqFG_PCT": null,
        "EqFTA": null,
        "EqFTM": null,
        "EqFT_PCT": null,
        "EqMINUTES": null,
        "EqOREB": null,
        "EqPF": null,
        "EqPTS": null,
        "EqREB": null,
        "EqSTL": null,
        "EqTD": null,
        "EqTOV": null,
        "GameID": null,
        "GtAST": null,
        "GtBLK": null,
        "GtDD": null,
        "GtDREB": null,
        "GtFG3A": null,
        "GtFG3M": null,
        "GtFG3_PCT": null,
        "GtFGA": null,
        "GtFGM": null,
        "GtFG_PCT": null,
        "GtFTA": null,
        "GtFTM": null,
        "GtFT_PCT": null,
        "GtMINUTES": null,
        "GtOREB": null,
        "GtPF": null,
        "GtPTS": null,
        "GtREB": null,
        "GtSTL": null,
        "GtTD": null,
        "GtTOV": null,
        "LeagueID": null,
        "Location": null,
        "LtAST": null,
        "LtBLK": null,
        "LtDD": null,
        "LtDREB": null,
        "LtFG3A": null,
        "LtFG3M": null,
        "LtFG3_PCT": null,
        "LtFGA": null,
        "LtFGM": null,
        "LtFG_PCT": null,
        "LtFTA": null,
        "LtFTM": null,
        "LtFT_PCT": null,
        "LtMINUTES": null,
        "LtOREB": null,
        "LtPF": null,
        "LtPTS": null,
        "LtREB": null,
        "LtSTL": null,
        "LtTD": null,
        "LtTOV": null,
        "Outcome": null,
        "PORound": null,
        "PlayerID": null,
        "PlayerOrTeam": "^(P)|(T)$",
        "RookieYear": null,
        "Season": null,
        "SeasonSegment": null,
        "SeasonType": null,
        "StarterBench": null,
        "TeamID": null,
        "VsConference": null,
        "VsDivision": null,
        "VsTeamID": null,
        "YearsExperience": null
    },
    "parameters": [
        "Conference",
        "DateFrom",
        "DateTo",
        "Division",
        "DraftNumber",
        "DraftRound",
        "DraftTeamID",
        "DraftYear",
        "EqAST",
        "EqBLK",
        "EqDD",
        "EqDREB",
        "EqFG3A",
        "EqFG3M",
        "EqFG3_PCT",
        "EqFGA",
        "EqFGM",
        "EqFG_PCT",
        "EqFTA",
        "EqFTM",
        "EqFT_PCT",
        "EqMINUTES",
        "EqOREB",
        "EqPF",
        "EqPTS",
        "EqREB",
        "EqSTL",
        "EqTD",
        "EqTOV",
        "GameID",
        "GtAST",
        "GtBLK",
        "GtDD",
        "GtDREB",
        "GtFG3A",
        "GtFG3M",
        "GtFG3_PCT",
        "GtFGA",
        "GtFGM",
        "GtFG_PCT",
        "GtFTA",
        "GtFTM",
        "GtFT_PCT",
        "GtMINUTES",
        "GtOREB",
        "GtPF",
        "GtPTS",
        "GtREB",
        "GtSTL",
        "GtTD",
        "GtTOV",
        "LeagueID",
        "Location",
        "LtAST",
        "LtBLK",
        "LtDD",
        "LtDREB",
        "LtFG3A",
        "LtFG3M",
        "LtFG3_PCT",
        "LtFGA",
        "LtFGM",
        "LtFG_PCT",
        "LtFTA",
        "LtFTM",
        "LtFT_PCT",
        "LtMINUTES",
        "LtOREB",
        "LtPF",
        "LtPTS",
        "LtREB",
        "LtSTL",
        "LtTD",
        "LtTOV",
        "Outcome",
        "PORound",
        "PlayerID",
        "PlayerOrTeam",
        "RookieYear",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "StarterBench",
        "TeamID",
        "VsConference",
        "VsDivision",
        "VsTeamID",
        "YearsExperience"
    ],
    "required_parameters": [
        "PlayerOrTeam"
    ],
    "status": "success"
}
```

Last validated 2018-12-11