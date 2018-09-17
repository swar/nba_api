# VideoDetails

##### Endpoint URL
>[https://stats.nba.com/stats/videodetails](https://stats.nba.com/stats/videodetails)

##### Valid URL
>[https://stats.nba.com/stats/videodetails?AheadBehind=&ClutchTime=&ContextFilter=&ContextMeasure=PTS&DateFrom=&DateTo=&EndPeriod=&EndRange=&GameID=&GameSegment=&LastNGames=10&LeagueID=&Location=&Month=0&OpponentTeamID=0&Outcome=&Period=1&PlayerID=2544&PointDiff=&Position=&RangeType=&RookieYear=&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&StartPeriod=&StartRange=&TeamID=1610612739&VsConference=&VsDivision=](https://stats.nba.com/stats/videodetails?AheadBehind=&ClutchTime=&ContextFilter=&ContextMeasure=PTS&DateFrom=&DateTo=&EndPeriod=&EndRange=&GameID=&GameSegment=&LastNGames=10&LeagueID=&Location=&Month=0&OpponentTeamID=0&Outcome=&Period=1&PlayerID=2544&PointDiff=&Position=&RangeType=&RookieYear=&Season=2017-18&SeasonSegment=&SeasonType=Regular+Season&StartPeriod=&StartRange=&TeamID=1610612739&VsConference=&VsDivision=)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**ContextMeasure**_ | `^((FGM)|(FGA)|(FG_PCT)|(FG3M)|(FG3A)|(FG3_PCT)|(FTM)|(FTA)|(OREB)|(DREB)|(AST)|(FGM_AST)|(FG3_AST)|(STL)|(BLK)|(BLKA)|(TOV)|(PF)|(PFD)|(POSS_END_FT)|(PTS_PAINT)|(PTS_FB)|(PTS_OFF_TOV)|(PTS_2ND_CHANCE)|(REB)|(TM_FGM)|(TM_FGA)|(TM_FG3M)|(TM_FG3A)|(TM_FTM)|(TM_FTA)|(TM_OREB)|(TM_DREB)|(TM_REB)|(TM_TEAM_REB)|(TM_AST)|(TM_STL)|(TM_BLK)|(TM_BLKA)|(TM_TOV)|(TM_TEAM_TOV)|(TM_PF)|(TM_PFD)|(TM_PTS)|(TM_PTS_PAINT)|(TM_PTS_FB)|(TM_PTS_OFF_TOV)|(TM_PTS_2ND_CHANCE)|(TM_FGM_AST)|(TM_FG3_AST)|(TM_POSS_END_FT)|(OPP_FGM)|(OPP_FGA)|(OPP_FG3M)|(OPP_FG3A)|(OPP_FTM)|(OPP_FTA)|(OPP_OREB)|(OPP_DREB)|(OPP_REB)|(OPP_TEAM_REB)|(OPP_AST)|(OPP_STL)|(OPP_BLK)|(OPP_BLKA)|(OPP_TOV)|(OPP_TEAM_TOV)|(OPP_PF)|(OPP_PFD)|(OPP_PTS)|(OPP_PTS_PAINT)|(OPP_PTS_FB)|(OPP_PTS_OFF_TOV)|(OPP_PTS_2ND_CHANCE)|(OPP_FGM_AST)|(OPP_FG3_AST)|(OPP_POSS_END_FT)|(PTS))$` | `Y` |  | 
_**LastNGames**_ |  | `Y` |  | 
_**Month**_ |  | `Y` |  | 
_**OpponentTeamID**_ |  | `Y` |  | 
_**Period**_ |  | `Y` |  | 
_**PlayerID**_ |  | `Y` |  | 
_**Season**_ | `^(\d{4}-\d{2})?$` | `Y` |  | 
_**SeasonType**_ | `^((Regular Season)|(Pre Season)|(Playoffs)|(All Star))?$` | `Y` |  | 
_**TeamID**_ |  | `Y` |  | 
_**VsDivision**_ | `^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$` | `Y` | `Y` | 
_**VsConference**_ | `^((East)|(West))?$` | `Y` | `Y` | 
_**StartRange**_ |  | `Y` | `Y` | 
_**StartPeriod**_ |  | `Y` | `Y` | 
_**SeasonSegment**_ | `^((Post All-Star)|(Pre All-Star))?$` | `Y` | `Y` | 
_**RookieYear**_ |  |  | `Y` | 
_**RangeType**_ |  | `Y` | `Y` | 
_**Position**_ |  |  | `Y` | 
_**PointDiff**_ |  |  | `Y` | 
_**Outcome**_ | `^((W)|(L))?$` | `Y` | `Y` | 
_**Location**_ | `^((Home)|(Road))?$` | `Y` | `Y` | 
_**LeagueID**_ | `^((00)|(20))?$` | `Y` | `Y` | 
_**GameSegment**_ |  |  | `Y` | 
_**GameID**_ | `^(\d{10})?$` | `Y` | `Y` | 
_**EndRange**_ |  | `Y` | `Y` | 
_**EndPeriod**_ |  | `Y` | `Y` | 
_**DateTo**_ |  | `Y` | `Y` | 
_**DateFrom**_ |  | `Y` | `Y` | 
_**ContextFilter**_ |  |  | `Y` | 
_**ClutchTime**_ |  |  | `Y` | 
_**AheadBehind**_ |  |  | `Y` | 

## Data Sets


## JSON
```json
{
    "data_sets": {},
    "endpoint": "VideoDetails",
    "nullable_parameters": [
        "AheadBehind",
        "ClutchTime",
        "ContextFilter",
        "DateFrom",
        "DateTo",
        "EndPeriod",
        "EndRange",
        "GameID",
        "GameSegment",
        "LeagueID",
        "Location",
        "Outcome",
        "PointDiff",
        "Position",
        "RangeType",
        "RookieYear",
        "SeasonSegment",
        "StartPeriod",
        "StartRange",
        "VsConference",
        "VsDivision"
    ],
    "parameter_patterns": {
        "AheadBehind": null,
        "ClutchTime": null,
        "ContextFilter": null,
        "ContextMeasure": "^((FGM)|(FGA)|(FG_PCT)|(FG3M)|(FG3A)|(FG3_PCT)|(FTM)|(FTA)|(OREB)|(DREB)|(AST)|(FGM_AST)|(FG3_AST)|(STL)|(BLK)|(BLKA)|(TOV)|(PF)|(PFD)|(POSS_END_FT)|(PTS_PAINT)|(PTS_FB)|(PTS_OFF_TOV)|(PTS_2ND_CHANCE)|(REB)|(TM_FGM)|(TM_FGA)|(TM_FG3M)|(TM_FG3A)|(TM_FTM)|(TM_FTA)|(TM_OREB)|(TM_DREB)|(TM_REB)|(TM_TEAM_REB)|(TM_AST)|(TM_STL)|(TM_BLK)|(TM_BLKA)|(TM_TOV)|(TM_TEAM_TOV)|(TM_PF)|(TM_PFD)|(TM_PTS)|(TM_PTS_PAINT)|(TM_PTS_FB)|(TM_PTS_OFF_TOV)|(TM_PTS_2ND_CHANCE)|(TM_FGM_AST)|(TM_FG3_AST)|(TM_POSS_END_FT)|(OPP_FGM)|(OPP_FGA)|(OPP_FG3M)|(OPP_FG3A)|(OPP_FTM)|(OPP_FTA)|(OPP_OREB)|(OPP_DREB)|(OPP_REB)|(OPP_TEAM_REB)|(OPP_AST)|(OPP_STL)|(OPP_BLK)|(OPP_BLKA)|(OPP_TOV)|(OPP_TEAM_TOV)|(OPP_PF)|(OPP_PFD)|(OPP_PTS)|(OPP_PTS_PAINT)|(OPP_PTS_FB)|(OPP_PTS_OFF_TOV)|(OPP_PTS_2ND_CHANCE)|(OPP_FGM_AST)|(OPP_FG3_AST)|(OPP_POSS_END_FT)|(PTS))$",
        "DateFrom": null,
        "DateTo": null,
        "EndPeriod": null,
        "EndRange": null,
        "GameID": "^(\\d{10})?$",
        "GameSegment": null,
        "LastNGames": null,
        "LeagueID": "^((00)|(20))?$",
        "Location": "^((Home)|(Road))?$",
        "Month": null,
        "OpponentTeamID": null,
        "Outcome": "^((W)|(L))?$",
        "Period": null,
        "PlayerID": null,
        "PointDiff": null,
        "Position": null,
        "RangeType": null,
        "RookieYear": null,
        "Season": "^(\\d{4}-\\d{2})?$",
        "SeasonSegment": "^((Post All-Star)|(Pre All-Star))?$",
        "SeasonType": "^((Regular Season)|(Pre Season)|(Playoffs)|(All Star))?$",
        "StartPeriod": null,
        "StartRange": null,
        "TeamID": null,
        "VsConference": "^((East)|(West))?$",
        "VsDivision": "^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$"
    },
    "parameters": [
        "AheadBehind",
        "ClutchTime",
        "ContextFilter",
        "ContextMeasure",
        "DateFrom",
        "DateTo",
        "EndPeriod",
        "EndRange",
        "GameID",
        "GameSegment",
        "LastNGames",
        "LeagueID",
        "Location",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "Period",
        "PlayerID",
        "PointDiff",
        "Position",
        "RangeType",
        "RookieYear",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "StartPeriod",
        "StartRange",
        "TeamID",
        "VsConference",
        "VsDivision"
    ],
    "required_parameters": [
        "ContextMeasure",
        "DateFrom",
        "DateTo",
        "EndPeriod",
        "EndRange",
        "GameID",
        "LastNGames",
        "LeagueID",
        "Location",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "Period",
        "PlayerID",
        "RangeType",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "StartPeriod",
        "StartRange",
        "TeamID",
        "VsConference",
        "VsDivision"
    ],
    "status": "success"
}
```

Last validated 2018-09-16