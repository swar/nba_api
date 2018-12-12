# ShotChartDetail
##### [nba_api/stats/endpoints/shotchartdetail.py](https://github.com/swar/nba_api/blob/master/nba_api/stats/endpoints/shotchartdetail.py)

##### Endpoint URL
>[https://stats.nba.com/stats/shotchartdetail](https://stats.nba.com/stats/shotchartdetail)

##### Valid URL
>[https://stats.nba.com/stats/shotchartdetail?AheadBehind=&ClutchTime=&ContextFilter=&ContextMeasure=PTS&DateFrom=&DateTo=&EndPeriod=&EndRange=&GameID=&GameSegment=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&Period=0&PlayerID=2544&PlayerPosition=&PointDiff=&Position=&RangeType=&RookieYear=&Season=&SeasonSegment=&SeasonType=Regular+Season&StartPeriod=&StartRange=&TeamID=1610612739&VsConference=&VsDivision=](https://stats.nba.com/stats/shotchartdetail?AheadBehind=&ClutchTime=&ContextFilter=&ContextMeasure=PTS&DateFrom=&DateTo=&EndPeriod=&EndRange=&GameID=&GameSegment=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&Period=0&PlayerID=2544&PlayerPosition=&PointDiff=&Position=&RangeType=&RookieYear=&Season=&SeasonSegment=&SeasonType=Regular+Season&StartPeriod=&StartRange=&TeamID=1610612739&VsConference=&VsDivision=)

## Parameters
API Parameter Name | Python Parameter Class | Python Parameter Variable | Pattern | Required | Nullable
------------ | ------------ | ------------ | :-----------: | :---: | :---:
_**ContextMeasure**_ | [ContextMeasureSimple](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#ContextMeasure) | context_measure_simple | `^((PTS)\|(FGM)\|(FGA)\|(FG_PCT)\|(FG3M)\|(FG3A)\|(FG3_PCT)\|(PF)\|(EFG_PCT)\|(TS_PCT)\|(PTS_FB)\|(PTS_OFF_TOV)\|(PTS_2ND_CHANCE)\|(PF))?$` | `Y` |  | 
_**LastNGames**_ | [LastNGames](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LastNGames) | last_n_games |  | `Y` |  | 
_**LeagueID**_ | [LeagueID](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id | `(00)\|(20)\|(10)` |  |  | 
_**Month**_ | [Month](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Month) | month |  | `Y` |  | 
_**OpponentTeamID**_ | [OpponentTeamID](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#OpponentTeamID) | opponent_team_id |  | `Y` |  | 
_**Period**_ | [Period](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Period) | period |  | `Y` |  | 
_**PlayerID**_ | [PlayerID](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerID) | player_id |  | `Y` |  | 
_**SeasonType**_ | [SeasonTypeAllStar](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType) | season_type_all_star | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$` | `Y` |  | 
_**TeamID**_ | [TeamID](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TeamID) | team_id |  | `Y` |  | 
_**VsDivision**_ | [VsDivisionNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsDivision) | vs_division_nullable | `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$` | `Y` | `Y` | 
_**VsConference**_ | [VsConferenceNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsConference) | vs_conference_nullable | `^((East)\|(West))?$` | `Y` | `Y` | 
_**StartRange**_ | [StartRangeNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#StartRange) | start_range_nullable |  |  | `Y` | 
_**StartPeriod**_ | [StartPeriodNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#StartPeriod) | start_period_nullable |  |  | `Y` | 
_**SeasonSegment**_ | [SeasonSegmentNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonSegment) | season_segment_nullable | `^((Post All-Star)\|(Pre All-Star))?$` | `Y` | `Y` | 
_**Season**_ | [SeasonNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season) | season_nullable | `^(\d{4}-\d{2})?$` |  | `Y` | 
_**RookieYear**_ | [RookieYearNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#RookieYear) | rookie_year_nullable | `^(\d{4}-\d{2})?$` | `Y` | `Y` | 
_**RangeType**_ | [RangeTypeNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#RangeType) | range_type_nullable |  |  | `Y` | 
_**Position**_ | [PositionNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Position) | position_nullable |  |  | `Y` | 
_**PointDiff**_ | [PointDiffNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PointDiff) | point_diff_nullable |  |  | `Y` | 
_**PlayerPosition**_ | [PlayerPositionNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerPosition) | player_position_nullable | `^((Guard)\|(Center)\|(Forward))?$` | `Y` | `Y` | 
_**Outcome**_ | [OutcomeNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Outcome) | outcome_nullable | `^((W)\|(L))?$` | `Y` | `Y` | 
_**Location**_ | [LocationNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Location) | location_nullable | `^((Home)\|(Road))?$` | `Y` | `Y` | 
_**GameSegment**_ | [GameSegmentNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameSegment) | game_segment_nullable | `^((First Half)\|(Overtime)\|(Second Half))?$` | `Y` | `Y` | 
_**GameID**_ | [GameIDNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameID) | game_id_nullable | `^(\d{10})?$` | `Y` | `Y` | 
_**EndRange**_ | [EndRangeNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EndRange) | end_range_nullable |  |  | `Y` | 
_**EndPeriod**_ | [EndPeriodNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EndPeriod) | end_period_nullable |  |  | `Y` | 
_**DateTo**_ | [DateToNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateTo) | date_to_nullable |  | `Y` | `Y` | 
_**DateFrom**_ | [DateFromNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateFrom) | date_from_nullable |  | `Y` | `Y` | 
_**ContextFilter**_ | [ContextFilterNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#ContextFilter) | context_filter_nullable |  |  | `Y` | 
_**ClutchTime**_ | [ClutchTimeNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#ClutchTime) | clutch_time_nullable | `^((Last 5 Minutes)\|(Last 4 Minutes)\|(Last 3 Minutes)\|(Last 2 Minutes)\|(Last 1 Minute)\|(Last 30 Seconds)\|(Last 10 Seconds))?$` |  | `Y` | 
_**AheadBehind**_ | [AheadBehindNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#AheadBehind) | ahead_behind_nullable | `^((Ahead or Behind)\|(Ahead or Tied)\|(Behind or Tied))?$` |  | `Y` | 

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
    "last_validated_date": "2018-12-11",
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

Last validated 2018-12-11