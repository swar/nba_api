# ShotChartDetail

##### Endpoint URL
>[https://stats.nba.com/stats/shotchartdetail](https://stats.nba.com/stats/shotchartdetail)

##### Valid URL
>[https://stats.nba.com/stats/shotchartdetail?AheadBehind=&ClutchTime=&ContextFilter=&ContextMeasure=PTS&DateFrom=&DateTo=&EndPeriod=&EndRange=&GameID=&GameSegment=&LastNGames=10&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&Period=1&PlayerID=2544&PlayerPosition=&PointDiff=&Position=&RangeType=&RookieYear=&Season=&SeasonSegment=&SeasonType=Regular+Season&StartPeriod=&StartRange=&TeamID=1610612739&VsConference=&VsDivision=](https://stats.nba.com/stats/shotchartdetail?AheadBehind=&ClutchTime=&ContextFilter=&ContextMeasure=PTS&DateFrom=&DateTo=&EndPeriod=&EndRange=&GameID=&GameSegment=&LastNGames=10&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&Period=1&PlayerID=2544&PlayerPosition=&PointDiff=&Position=&RangeType=&RookieYear=&Season=&SeasonSegment=&SeasonType=Regular+Season&StartPeriod=&StartRange=&TeamID=1610612739&VsConference=&VsDivision=)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**ContextMeasure**_ | `^((PTS)|(FGM)|(FGA)|(FG_PCT)|(FG3M)|(FG3A)|(FG3_PCT)|(PF)|(EFG_PCT)|(TS_PCT)|(PTS_FB)|(PTS_OFF_TOV)|(PTS_2ND_CHANCE)|(PF))?$` | `Y` |  | 
_**LastNGames**_ |  | `Y` |  | 
_**LeagueID**_ | `(00)|(20)|(10)` |  |  | 
_**Month**_ |  | `Y` |  | 
_**OpponentTeamID**_ |  | `Y` |  | 
_**Period**_ |  | `Y` |  | 
_**PlayerID**_ |  | `Y` |  | 
_**SeasonType**_ | `^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$` | `Y` |  | 
_**TeamID**_ |  | `Y` |  | 
_**VsDivision**_ | `^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$` | `Y` | `Y` | 
_**VsConference**_ | `^((East)|(West))?$` | `Y` | `Y` | 
_**StartRange**_ |  |  | `Y` | 
_**StartPeriod**_ |  |  | `Y` | 
_**SeasonSegment**_ | `^((Post All-Star)|(Pre All-Star))?$` | `Y` | `Y` | 
_**Season**_ | `^(\d{4}-\d{2})?$` |  | `Y` | 
_**RookieYear**_ | `^(\d{4}-\d{2})?$` | `Y` | `Y` | 
_**RangeType**_ |  |  | `Y` | 
_**Position**_ |  |  | `Y` | 
_**PointDiff**_ |  |  | `Y` | 
_**PlayerPosition**_ | `^((Guard)|(Center)|(Forward))?$` | `Y` | `Y` | 
_**Outcome**_ | `^((W)|(L))?$` | `Y` | `Y` | 
_**Location**_ | `^((Home)|(Road))?$` | `Y` | `Y` | 
_**GameSegment**_ | `^((First Half)|(Overtime)|(Second Half))?$` | `Y` | `Y` | 
_**GameID**_ | `^(\d{10})?$` | `Y` | `Y` | 
_**EndRange**_ |  |  | `Y` | 
_**EndPeriod**_ |  |  | `Y` | 
_**DateTo**_ |  | `Y` | `Y` | 
_**DateFrom**_ |  | `Y` | `Y` | 
_**ContextFilter**_ |  |  | `Y` | 
_**ClutchTime**_ | `^((Last 5 Minutes)|(Last 4 Minutes)|(Last 3 Minutes)|(Last 2 Minutes)|(Last 1 Minute)|(Last 30 Seconds)|(Last 10 Seconds))?$` |  | `Y` | 
_**AheadBehind**_ | `^((Ahead or Behind)|(Ahead or Tied)|(Behind or Tied))?$` |  | `Y` | 

## Data Sets
#### LeagueAverages `league_averages`
```text
['GRID_TYPE', 'SHOT_ZONE_BASIC', 'SHOT_ZONE_AREA', 'SHOT_ZONE_RANGE', 'FGA', 'FGM', 'FG_PCT']
```

#### Shot_Chart_Detail `shot_chart_detail`
```text
['GRID_TYPE', 'GAME_ID', 'GAME_EVENT_ID', 'PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_NAME', 'PERIOD', 'MINUTES_REMAINING', 'SECONDS_REMAINING', 'EVENT_TYPE', 'ACTION_TYPE', 'SHOT_TYPE', 'SHOT_ZONE_BASIC', 'SHOT_ZONE_AREA', 'SHOT_ZONE_RANGE', 'SHOT_DISTANCE', 'LOC_X', 'LOC_Y', 'SHOT_ATTEMPTED_FLAG', 'SHOT_MADE_FLAG', 'GAME_DATE', 'HTM', 'VTM']
```


## JSON
```json
{
    "data_sets": {
        "LeagueAverages": [
            "GRID_TYPE",
            "SHOT_ZONE_BASIC",
            "SHOT_ZONE_AREA",
            "SHOT_ZONE_RANGE",
            "FGA",
            "FGM",
            "FG_PCT"
        ],
        "Shot_Chart_Detail": [
            "GRID_TYPE",
            "GAME_ID",
            "GAME_EVENT_ID",
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
        ]
    },
    "endpoint": "ShotChartDetail",
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
        "Location",
        "Outcome",
        "PlayerPosition",
        "PointDiff",
        "Position",
        "RangeType",
        "RookieYear",
        "Season",
        "SeasonSegment",
        "StartPeriod",
        "StartRange",
        "VsConference",
        "VsDivision"
    ],
    "parameter_patterns": {
        "AheadBehind": "^((Ahead or Behind)|(Ahead or Tied)|(Behind or Tied))?$",
        "ClutchTime": "^((Last 5 Minutes)|(Last 4 Minutes)|(Last 3 Minutes)|(Last 2 Minutes)|(Last 1 Minute)|(Last 30 Seconds)|(Last 10 Seconds))?$",
        "ContextFilter": null,
        "ContextMeasure": "^((PTS)|(FGM)|(FGA)|(FG_PCT)|(FG3M)|(FG3A)|(FG3_PCT)|(PF)|(EFG_PCT)|(TS_PCT)|(PTS_FB)|(PTS_OFF_TOV)|(PTS_2ND_CHANCE)|(PF))?$",
        "DateFrom": null,
        "DateTo": null,
        "EndPeriod": null,
        "EndRange": null,
        "GameID": "^(\\d{10})?$",
        "GameSegment": "^((First Half)|(Overtime)|(Second Half))?$",
        "LastNGames": null,
        "LeagueID": "(00)|(20)|(10)",
        "Location": "^((Home)|(Road))?$",
        "Month": null,
        "OpponentTeamID": null,
        "Outcome": "^((W)|(L))?$",
        "Period": null,
        "PlayerID": null,
        "PlayerPosition": "^((Guard)|(Center)|(Forward))?$",
        "PointDiff": null,
        "Position": null,
        "RangeType": null,
        "RookieYear": "^(\\d{4}-\\d{2})?$",
        "Season": "^(\\d{4}-\\d{2})?$",
        "SeasonSegment": "^((Post All-Star)|(Pre All-Star))?$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$",
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
        "PlayerPosition",
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
        "GameID",
        "GameSegment",
        "LastNGames",
        "Location",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "Period",
        "PlayerID",
        "PlayerPosition",
        "RookieYear",
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