# PlayerGameStreakFinder
##### [nba_api/stats/endpoints/playergamestreakfinder.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/playergamestreakfinder.py)

##### Endpoint URL
>[https://stats.nba.com/stats/playergamestreakfinder](https://stats.nba.com/stats/playergamestreakfinder)

##### Valid URL
>[https://stats.nba.com/stats/playergamestreakfinder?ActiveStreaksOnly=&Conference=&DateFrom=&DateTo=&Division=&DraftNumber=&DraftRound=&DraftTeamID=&DraftYear=&EqAST=&EqBLK=&EqDD=&EqDREB=&EqFG3A=&EqFG3M=&EqFG3_PCT=&EqFGA=&EqFGM=&EqFG_PCT=&EqFTA=&EqFTM=&EqFT_PCT=&EqMINUTES=&EqOREB=&EqPF=&EqPTS=&EqREB=&EqSTL=&EqTD=&EqTOV=&GameID=&GtAST=&GtBLK=&GtDD=&GtDREB=&GtFG3A=&GtFG3M=&GtFG3_PCT=&GtFGA=&GtFGM=&GtFG_PCT=&GtFTA=&GtFTM=&GtFT_PCT=&GtMINUTES=&GtOREB=&GtPF=&GtPTS=&GtREB=&GtSTL=&GtTD=&GtTOV=&LeagueID=&Location=&LtAST=&LtBLK=&LtDD=&LtDREB=&LtFG3A=&LtFG3M=&LtFG3_PCT=&LtFGA=&LtFGM=&LtFG_PCT=&LtFTA=&LtFTM=&LtFT_PCT=&LtMINUTES=&LtOREB=&LtPF=&LtPTS=&LtREB=&LtSTL=&LtTD=&LtTOV=&MinGames=&Outcome=&PORound=&PlayerID=&RookieYear=&Season=&SeasonSegment=&SeasonType=&StarterBench=&TeamID=&VsConference=&VsDivision=&VsTeamID=&YearsExperience=](https://stats.nba.com/stats/playergamestreakfinder?ActiveStreaksOnly=&Conference=&DateFrom=&DateTo=&Division=&DraftNumber=&DraftRound=&DraftTeamID=&DraftYear=&EqAST=&EqBLK=&EqDD=&EqDREB=&EqFG3A=&EqFG3M=&EqFG3_PCT=&EqFGA=&EqFGM=&EqFG_PCT=&EqFTA=&EqFTM=&EqFT_PCT=&EqMINUTES=&EqOREB=&EqPF=&EqPTS=&EqREB=&EqSTL=&EqTD=&EqTOV=&GameID=&GtAST=&GtBLK=&GtDD=&GtDREB=&GtFG3A=&GtFG3M=&GtFG3_PCT=&GtFGA=&GtFGM=&GtFG_PCT=&GtFTA=&GtFTM=&GtFT_PCT=&GtMINUTES=&GtOREB=&GtPF=&GtPTS=&GtREB=&GtSTL=&GtTD=&GtTOV=&LeagueID=&Location=&LtAST=&LtBLK=&LtDD=&LtDREB=&LtFG3A=&LtFG3M=&LtFG3_PCT=&LtFGA=&LtFGM=&LtFG_PCT=&LtFTA=&LtFTM=&LtFT_PCT=&LtMINUTES=&LtOREB=&LtPF=&LtPTS=&LtREB=&LtSTL=&LtTD=&LtTOV=&MinGames=&Outcome=&PORound=&PlayerID=&RookieYear=&Season=&SeasonSegment=&SeasonType=&StarterBench=&TeamID=&VsConference=&VsDivision=&VsTeamID=&YearsExperience=)

## Parameters
| API Parameter Name                                                                                                                | Python Parameter Variable    | Pattern | Required | Nullable |
|-----------------------------------------------------------------------------------------------------------------------------------|------------------------------|:-------:|:--------:|:--------:|
| [_**YearsExperience**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#YearsExperience)     | years_experience_nullable    |         |          |   `Y`    | 
| [_**VsTeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsTeamID)                   | vs_team_id_nullable          |         |          |   `Y`    | 
| [_**VsDivision**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsDivision)               | vs_division_nullable         |         |          |   `Y`    | 
| [_**VsConference**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsConference)           | vs_conference_nullable       |         |          |   `Y`    | 
| [_**TeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TeamID)                       | team_id_nullable             |         |          |   `Y`    | 
| [_**StarterBench**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#StarterBench)           | starter_bench_nullable       |         |          |   `Y`    | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType)               | season_type_nullable         |         |          |   `Y`    | 
| [_**SeasonSegment**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonSegment)         | season_segment_nullable      |         |          |   `Y`    | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)                       | season_nullable              |         |          |   `Y`    | 
| [_**RookieYear**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#RookieYear)               | rookie_year_nullable         |         |          |   `Y`    | 
| [_**PlayerID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerID)                   | player_id_nullable           |         |          |   `Y`    | 
| [_**PORound**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PORound)                     | po_round_nullable            |         |          |   `Y`    | 
| [_**Outcome**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Outcome)                     | outcome_nullable             |         |          |   `Y`    | 
| [_**MinGames**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#MinGames)                   | min_games_nullable           |         |          |   `Y`    | 
| [_**LtTOV**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtTOV)                         | lt_tov_nullable              |         |          |   `Y`    | 
| [_**LtTD**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtTD)                           | lt_td_nullable               |         |          |   `Y`    | 
| [_**LtSTL**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtSTL)                         | lt_stl_nullable              |         |          |   `Y`    | 
| [_**LtREB**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtREB)                         | lt_reb_nullable              |         |          |   `Y`    | 
| [_**LtPTS**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtPTS)                         | lt_pts_nullable              |         |          |   `Y`    | 
| [_**LtPF**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtPF)                           | lt_pf_nullable               |         |          |   `Y`    | 
| [_**LtOREB**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtOREB)                       | lt_oreb_nullable             |         |          |   `Y`    | 
| [_**LtMINUTES**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtMINUTES)                 | lt_minutes_nullable          |         |          |   `Y`    | 
| [_**LtFT_PCT**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtFT_PCT)                   | lt_ft_pct_nullable           |         |          |   `Y`    | 
| [_**LtFTM**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtFTM)                         | lt_ftm_nullable              |         |          |   `Y`    | 
| [_**LtFTA**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtFTA)                         | lt_fta_nullable              |         |          |   `Y`    | 
| [_**LtFG_PCT**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtFG_PCT)                   | lt_fg_pct_nullable           |         |          |   `Y`    | 
| [_**LtFGM**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtFGM)                         | lt_fgm_nullable              |         |          |   `Y`    | 
| [_**LtFGA**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtFGA)                         | lt_fga_nullable              |         |          |   `Y`    | 
| [_**LtFG3_PCT**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtFG3_PCT)                 | lt_fg3_pct_nullable          |         |          |   `Y`    | 
| [_**LtFG3M**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtFG3M)                       | lt_fg3m_nullable             |         |          |   `Y`    | 
| [_**LtFG3A**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtFG3A)                       | lt_fg3a_nullable             |         |          |   `Y`    | 
| [_**LtDREB**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtDREB)                       | lt_dreb_nullable             |         |          |   `Y`    | 
| [_**LtDD**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtDD)                           | lt_dd_nullable               |         |          |   `Y`    | 
| [_**LtBLK**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtBLK)                         | lt_blk_nullable              |         |          |   `Y`    | 
| [_**LtAST**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LtAST)                         | lt_ast_nullable              |         |          |   `Y`    | 
| [_**Location**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Location)                   | location_nullable            |         |          |   `Y`    | 
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)                   | league_id_nullable           |         |          |   `Y`    | 
| [_**GtTOV**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtTOV)                         | gt_tov_nullable              |         |          |   `Y`    | 
| [_**GtTD**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtTD)                           | gt_td_nullable               |         |          |   `Y`    | 
| [_**GtSTL**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtSTL)                         | gt_stl_nullable              |         |          |   `Y`    | 
| [_**GtREB**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtREB)                         | gt_reb_nullable              |         |          |   `Y`    | 
| [_**GtPTS**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtPTS)                         | gt_pts_nullable              |         |          |   `Y`    | 
| [_**GtPF**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtPF)                           | gt_pf_nullable               |         |          |   `Y`    | 
| [_**GtOREB**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtOREB)                       | gt_oreb_nullable             |         |          |   `Y`    | 
| [_**GtMINUTES**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtMINUTES)                 | gt_minutes_nullable          |         |          |   `Y`    | 
| [_**GtFT_PCT**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtFT_PCT)                   | gt_ft_pct_nullable           |         |          |   `Y`    | 
| [_**GtFTM**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtFTM)                         | gt_ftm_nullable              |         |          |   `Y`    | 
| [_**GtFTA**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtFTA)                         | gt_fta_nullable              |         |          |   `Y`    | 
| [_**GtFG_PCT**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtFG_PCT)                   | gt_fg_pct_nullable           |         |          |   `Y`    | 
| [_**GtFGM**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtFGM)                         | gt_fgm_nullable              |         |          |   `Y`    | 
| [_**GtFGA**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtFGA)                         | gt_fga_nullable              |         |          |   `Y`    | 
| [_**GtFG3_PCT**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtFG3_PCT)                 | gt_fg3_pct_nullable          |         |          |   `Y`    | 
| [_**GtFG3M**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtFG3M)                       | gt_fg3m_nullable             |         |          |   `Y`    | 
| [_**GtFG3A**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtFG3A)                       | gt_fg3a_nullable             |         |          |   `Y`    | 
| [_**GtDREB**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtDREB)                       | gt_dreb_nullable             |         |          |   `Y`    | 
| [_**GtDD**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtDD)                           | gt_dd_nullable               |         |          |   `Y`    | 
| [_**GtBLK**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtBLK)                         | gt_blk_nullable              |         |          |   `Y`    | 
| [_**GtAST**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GtAST)                         | gt_ast_nullable              |         |          |   `Y`    | 
| [_**GameID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameID)                       | game_id_nullable             |         |          |   `Y`    | 
| [_**EqTOV**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqTOV)                         | eq_tov_nullable              |         |          |   `Y`    | 
| [_**EqTD**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqTD)                           | eq_td_nullable               |         |          |   `Y`    | 
| [_**EqSTL**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqSTL)                         | eq_stl_nullable              |         |          |   `Y`    | 
| [_**EqREB**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqREB)                         | eq_reb_nullable              |         |          |   `Y`    | 
| [_**EqPTS**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqPTS)                         | eq_pts_nullable              |         |          |   `Y`    | 
| [_**EqPF**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqPF)                           | eq_pf_nullable               |         |          |   `Y`    | 
| [_**EqOREB**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqOREB)                       | eq_oreb_nullable             |         |          |   `Y`    | 
| [_**EqMINUTES**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqMINUTES)                 | eq_minutes_nullable          |         |          |   `Y`    | 
| [_**EqFT_PCT**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqFT_PCT)                   | eq_ft_pct_nullable           |         |          |   `Y`    | 
| [_**EqFTM**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqFTM)                         | eq_ftm_nullable              |         |          |   `Y`    | 
| [_**EqFTA**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqFTA)                         | eq_fta_nullable              |         |          |   `Y`    | 
| [_**EqFG_PCT**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqFG_PCT)                   | eq_fg_pct_nullable           |         |          |   `Y`    | 
| [_**EqFGM**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqFGM)                         | eq_fgm_nullable              |         |          |   `Y`    | 
| [_**EqFGA**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqFGA)                         | eq_fga_nullable              |         |          |   `Y`    | 
| [_**EqFG3_PCT**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqFG3_PCT)                 | eq_fg3_pct_nullable          |         |          |   `Y`    | 
| [_**EqFG3M**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqFG3M)                       | eq_fg3m_nullable             |         |          |   `Y`    | 
| [_**EqFG3A**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqFG3A)                       | eq_fg3a_nullable             |         |          |   `Y`    | 
| [_**EqDREB**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqDREB)                       | eq_dreb_nullable             |         |          |   `Y`    | 
| [_**EqDD**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqDD)                           | eq_dd_nullable               |         |          |   `Y`    | 
| [_**EqBLK**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqBLK)                         | eq_blk_nullable              |         |          |   `Y`    | 
| [_**EqAST**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EqAST)                         | eq_ast_nullable              |         |          |   `Y`    | 
| [_**DraftYear**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DraftYear)                 | draft_year_nullable          |         |          |   `Y`    | 
| [_**DraftTeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DraftTeamID)             | draft_team_id_nullable       |         |          |   `Y`    | 
| [_**DraftRound**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DraftRound)               | draft_round_nullable         |         |          |   `Y`    | 
| [_**DraftNumber**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DraftNumber)             | draft_number_nullable        |         |          |   `Y`    | 
| [_**Division**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Division)                   | division_simple_nullable     |         |          |   `Y`    | 
| [_**DateTo**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateTo)                       | date_to_nullable             |         |          |   `Y`    | 
| [_**DateFrom**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateFrom)                   | date_from_nullable           |         |          |   `Y`    | 
| [_**Conference**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Conference)               | conference_nullable          |         |          |   `Y`    | 
| [_**ActiveStreaksOnly**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#ActiveStreaksOnly) | active_streaks_only_nullable |         |          |   `Y`    | 

## Data Sets
#### PlayerGameStreakFinderResults `player_game_streak_finder_results`
```text
['PLAYER_NAME_LAST_FIRST', 'PLAYER_ID', 'GAMESTREAK', 'STARTDATE', 'ENDDATE', 'ACTIVESTREAK', 'NUMSEASONS', 'LASTSEASON', 'FIRSTSEASON']
```


## JSON
```json
{
    "data_sets": {
        "PlayerGameStreakFinderResults": [
            "PLAYER_NAME_LAST_FIRST",
            "PLAYER_ID",
            "GAMESTREAK",
            "STARTDATE",
            "ENDDATE",
            "ACTIVESTREAK",
            "NUMSEASONS",
            "LASTSEASON",
            "FIRSTSEASON"
        ]
    },
    "endpoint": "PlayerGameStreakFinder",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [
        "ActiveStreaksOnly",
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
        "MinGames",
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
        "ActiveStreaksOnly": null,
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
        "MinGames": null,
        "Outcome": null,
        "PORound": null,
        "PlayerID": null,
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
        "ActiveStreaksOnly",
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
        "MinGames",
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
    "required_parameters": [],
    "status": "success"
}
```

Last validated 2020-08-16