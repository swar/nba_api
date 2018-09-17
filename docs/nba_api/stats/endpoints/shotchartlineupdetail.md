# ShotChartLineupDetail

##### Endpoint URL
>[https://stats.nba.com/stats/shotchartlineupdetail](https://stats.nba.com/stats/shotchartlineupdetail)

##### Valid URL
>[https://stats.nba.com/stats/shotchartlineupdetail?ContextFilter=&ContextMeasure=PTS&DateFrom=&DateTo=&GROUP_ID=0&GameID=&GameSegment=&LastNGames=&LeagueID=00&Location=&Month=&OpponentTeamID=&Outcome=&Period=1&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&TeamID=&VsConference=&VsDivision=](https://stats.nba.com/stats/shotchartlineupdetail?ContextFilter=&ContextMeasure=PTS&DateFrom=&DateTo=&GROUP_ID=0&GameID=&GameSegment=&LastNGames=&LeagueID=00&Location=&Month=&OpponentTeamID=&Outcome=&Period=1&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&TeamID=&VsConference=&VsDivision=)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**ContextMeasure**_ | `^((PTS)\|(FGM)\|(FGA)\|(FG_PCT)\|(FG3M)\|(FG3A)\|(FG3_PCT)\|(FTM)\|(FTA)\|(OREB)\|(DREB)\|(AST)\|(FGM_AST)\|(FG3_AST)\|(STL)\|(BLK)\|(BLKA)\|(TOV)\|(POSS_END_FT)\|(PTS_PAINT)\|(PTS_FB)\|(PTS_OFF_TOV)\|(PTS_2ND_CHANCE)\|(REB)\|(TM_FGM)\|(TM_FGA)\|(TM_FG3M)\|(TM_FG3A)\|(TM_FTM)\|(TM_FTA)\|(TM_OREB)\|(TM_DREB)\|(TM_REB)\|(TM_TEAM_REB)\|(TM_AST)\|(TM_STL)\|(TM_BLK)\|(TM_BLKA)\|(TM_TOV)\|(TM_TEAM_TOV)\|(TM_PF)\|(TM_PFD)\|(TM_PTS)\|(TM_PTS_PAINT)\|(TM_PTS_FB)\|(TM_PTS_OFF_TOV)\|(TM_PTS_2ND_CHANCE)\|(TM_FGM_AST)\|(TM_FG3_AST)\|(TM_POSS_END_FT)\|(OPP_FTM)\|(OPP_FTA)\|(OPP_OREB)\|(OPP_DREB)\|(OPP_REB)\|(OPP_TEAM_REB)\|(OPP_AST)\|(OPP_STL)\|(OPP_BLK)\|(OPP_BLKA)\|(OPP_TOV)\|(OPP_TEAM_TOV)\|(OPP_PF)\|(OPP_PFD)\|(OPP_PTS)\|(OPP_PTS_PAINT)\|(OPP_PTS_FB)\|(OPP_PTS_OFF_TOV)\|(OPP_PTS_2ND_CHANCE)\|(OPP_FGM_AST)\|(OPP_FG3_AST)\|(OPP_POSS_END_FT)\|(PTS))$` | `Y` |  | 
_**GROUP_ID**_ | `^\d+(( - \d+){2,4})?$` | `Y` |  | 
_**LeagueID**_ | `^(00)\|(20)$` | `Y` |  | 
_**Period**_ |  | `Y` |  | 
_**Season**_ | `^\d{4}-\d{2}$` | `Y` |  | 
_**SeasonType**_ | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$` | `Y` |  | 
_**VsDivision**_ | `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$` | `Y` | `Y` | 
_**VsConference**_ | `^((East)\|(West))?$` | `Y` | `Y` | 
_**TeamID**_ |  | `Y` | `Y` | 
_**SeasonSegment**_ | `^((Post All-Star)\|(Pre All-Star))?$` | `Y` | `Y` | 
_**Outcome**_ | `^((W)\|(L))?$` | `Y` | `Y` | 
_**OpponentTeamID**_ |  | `Y` | `Y` | 
_**Month**_ |  | `Y` | `Y` | 
_**Location**_ | `^((Home)\|(Road))?$` | `Y` | `Y` | 
_**LastNGames**_ |  | `Y` | `Y` | 
_**GameSegment**_ | `^((First Half)\|(Overtime)\|(Second Half))?$` | `Y` | `Y` | 
_**GameID**_ | `^(\d{10})?$` | `Y` | `Y` | 
_**DateTo**_ |  | `Y` | `Y` | 
_**DateFrom**_ |  | `Y` | `Y` | 
_**ContextFilter**_ |  | `Y` | `Y` | 

## Data Sets
#### ShotChartLineupDetail `shot_chart_lineup_detail`
```text
['GRID_TYPE', 'GAME_ID', 'GAME_EVENT_ID', 'GROUP_ID', 'GROUP_NAME', 'PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_NAME', 'PERIOD', 'MINUTES_REMAINING', 'SECONDS_REMAINING', 'EVENT_TYPE', 'ACTION_TYPE', 'SHOT_TYPE', 'SHOT_ZONE_BASIC', 'SHOT_ZONE_AREA', 'SHOT_ZONE_RANGE', 'SHOT_DISTANCE', 'LOC_X', 'LOC_Y', 'SHOT_ATTEMPTED_FLAG', 'SHOT_MADE_FLAG', 'GAME_DATE', 'HTM', 'VTM']
```

#### ShotChartLineupLeagueAverage `shot_chart_lineup_league_average`
```text
['GRID_TYPE', 'SHOT_ZONE_BASIC', 'SHOT_ZONE_AREA', 'SHOT_ZONE_RANGE', 'FGA', 'FGM', 'FG_PCT']
```


## JSON
```json
{
    "data_sets": {
        "ShotChartLineupDetail": [
            "GRID_TYPE",
            "GAME_ID",
            "GAME_EVENT_ID",
            "GROUP_ID",
            "GROUP_NAME",
            "PLAYER_ID",
            "PLAYER_NAME",
            "TEAM_ID",
            "TEAM_NAME",
            "PERIOD",
            "MINUTES_REMAINING",
            "SECONDS_REMAINING",
            "EVENT_TYPE",
            "ACTION_TYPE",
            "SHOT_TYPE",
            "SHOT_ZONE_BASIC",
            "SHOT_ZONE_AREA",
            "SHOT_ZONE_RANGE",
            "SHOT_DISTANCE",
            "LOC_X",
            "LOC_Y",
            "SHOT_ATTEMPTED_FLAG",
            "SHOT_MADE_FLAG",
            "GAME_DATE",
            "HTM",
            "VTM"
        ],
        "ShotChartLineupLeagueAverage": [
            "GRID_TYPE",
            "SHOT_ZONE_BASIC",
            "SHOT_ZONE_AREA",
            "SHOT_ZONE_RANGE",
            "FGA",
            "FGM",
            "FG_PCT"
        ]
    },
    "endpoint": "ShotChartLineupDetail",
    "nullable_parameters": [
        "ContextFilter",
        "DateFrom",
        "DateTo",
        "GameID",
        "GameSegment",
        "LastNGames",
        "Location",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "SeasonSegment",
        "TeamID",
        "VsConference",
        "VsDivision"
    ],
    "parameter_patterns": {
        "ContextFilter": null,
        "ContextMeasure": "^((PTS)|(FGM)|(FGA)|(FG_PCT)|(FG3M)|(FG3A)|(FG3_PCT)|(FTM)|(FTA)|(OREB)|(DREB)|(AST)|(FGM_AST)|(FG3_AST)|(STL)|(BLK)|(BLKA)|(TOV)|(POSS_END_FT)|(PTS_PAINT)|(PTS_FB)|(PTS_OFF_TOV)|(PTS_2ND_CHANCE)|(REB)|(TM_FGM)|(TM_FGA)|(TM_FG3M)|(TM_FG3A)|(TM_FTM)|(TM_FTA)|(TM_OREB)|(TM_DREB)|(TM_REB)|(TM_TEAM_REB)|(TM_AST)|(TM_STL)|(TM_BLK)|(TM_BLKA)|(TM_TOV)|(TM_TEAM_TOV)|(TM_PF)|(TM_PFD)|(TM_PTS)|(TM_PTS_PAINT)|(TM_PTS_FB)|(TM_PTS_OFF_TOV)|(TM_PTS_2ND_CHANCE)|(TM_FGM_AST)|(TM_FG3_AST)|(TM_POSS_END_FT)|(OPP_FTM)|(OPP_FTA)|(OPP_OREB)|(OPP_DREB)|(OPP_REB)|(OPP_TEAM_REB)|(OPP_AST)|(OPP_STL)|(OPP_BLK)|(OPP_BLKA)|(OPP_TOV)|(OPP_TEAM_TOV)|(OPP_PF)|(OPP_PFD)|(OPP_PTS)|(OPP_PTS_PAINT)|(OPP_PTS_FB)|(OPP_PTS_OFF_TOV)|(OPP_PTS_2ND_CHANCE)|(OPP_FGM_AST)|(OPP_FG3_AST)|(OPP_POSS_END_FT)|(PTS))$",
        "DateFrom": null,
        "DateTo": null,
        "GROUP_ID": "^\\d+(( - \\d+){2,4})?$",
        "GameID": "^(\\d{10})?$",
        "GameSegment": "^((First Half)|(Overtime)|(Second Half))?$",
        "LastNGames": null,
        "LeagueID": "^(00)|(20)$",
        "Location": "^((Home)|(Road))?$",
        "Month": null,
        "OpponentTeamID": null,
        "Outcome": "^((W)|(L))?$",
        "Period": null,
        "Season": "^\\d{4}-\\d{2}$",
        "SeasonSegment": "^((Post All-Star)|(Pre All-Star))?$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$",
        "TeamID": null,
        "VsConference": "^((East)|(West))?$",
        "VsDivision": "^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$"
    },
    "parameters": [
        "ContextFilter",
        "ContextMeasure",
        "DateFrom",
        "DateTo",
        "GROUP_ID",
        "GameID",
        "GameSegment",
        "LastNGames",
        "LeagueID",
        "Location",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "Period",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "TeamID",
        "VsConference",
        "VsDivision"
    ],
    "required_parameters": [
        "ContextFilter",
        "ContextMeasure",
        "DateFrom",
        "DateTo",
        "GROUP_ID",
        "GameID",
        "GameSegment",
        "LastNGames",
        "LeagueID",
        "Location",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "Period",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "TeamID",
        "VsConference",
        "VsDivision"
    ],
    "status": "success"
}
```

Last validated 2018-09-16