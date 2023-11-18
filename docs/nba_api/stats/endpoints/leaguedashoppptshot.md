# LeagueDashOppPtShot
##### [nba_api/stats/endpoints/leaguedashoppptshot.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/leaguedashoppptshot.py)

##### Endpoint URL
>[https://stats.nba.com/stats/leaguedashoppptshot](https://stats.nba.com/stats/leaguedashoppptshot)

##### Valid URL
>[https://stats.nba.com/stats/leaguedashoppptshot?CloseDefDistRange=&Conference=&DateFrom=&DateTo=&Division=&DribbleRange=&GameSegment=&GeneralRange=&LastNGames=&LeagueID=00&Location=&Month=&OpponentTeamID=&Outcome=&PORound=&PerMode=Totals&Period=&Season=2019-20&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&ShotDistRange=&TeamID=&TouchTimeRange=&VsConference=&VsDivision=](https://stats.nba.com/stats/leaguedashoppptshot?CloseDefDistRange=&Conference=&DateFrom=&DateTo=&Division=&DribbleRange=&GameSegment=&GeneralRange=&LastNGames=&LeagueID=00&Location=&Month=&OpponentTeamID=&Outcome=&PORound=&PerMode=Totals&Period=&Season=2019-20&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&ShotDistRange=&TeamID=&TouchTimeRange=&VsConference=&VsDivision=)

## Parameters
| API Parameter Name                                                                                                                | Python Parameter Variable     |                                            Pattern                                             | Required | Nullable |
|-----------------------------------------------------------------------------------------------------------------------------------|-------------------------------|:----------------------------------------------------------------------------------------------:|:--------:|:--------:|
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)                   | league_id                     |                                           `^\d{2}$`                                            |   `Y`    |          | 
| [_**PerMode**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PerMode)                     | per_mode_simple               |                                    `^(Totals)\|(PerGame)$`                                     |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)                       | season                        |                                                                                                |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType)               | season_type_all_star          |                   `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$`                   |   `Y`    |          | 
| [_**VsDivision**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsDivision)               | vs_division_nullable          | `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$` |          |   `Y`    | 
| [_**VsConference**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsConference)           | vs_conference_nullable        |                                     `^((East)\|(West))?$`                                      |          |   `Y`    | 
| [_**TouchTimeRange**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TouchTimeRange)       | touch_time_range_nullable     |                                                                                                |          |   `Y`    | 
| [_**TeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TeamID)                       | team_id_nullable              |                                                                                                |          |   `Y`    | 
| [_**ShotDistRange**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#ShotDistRange)         | shot_dist_range_nullable      |                                                                                                |          |   `Y`    | 
| [_**ShotClockRange**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#ShotClockRange)       | shot_clock_range_nullable     |                                                                                                |          |   `Y`    | 
| [_**SeasonSegment**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonSegment)         | season_segment_nullable       |                             `^((Post All-Star)\|(Pre All-Star))?$`                             |          |   `Y`    | 
| [_**Period**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Period)                       | period_nullable               |                                                                                                |          |   `Y`    | 
| [_**PORound**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PORound)                     | po_round_nullable             |                                                                                                |          |   `Y`    | 
| [_**Outcome**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Outcome)                     | outcome_nullable              |                                        `^((W)\|(L))?$`                                         |          |   `Y`    | 
| [_**OpponentTeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#OpponentTeamID)       | opponent_team_id_nullable     |                                                                                                |          |   `Y`    | 
| [_**Month**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Month)                         | month_nullable                |                                                                                                |          |   `Y`    | 
| [_**Location**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Location)                   | location_nullable             |                                     `^((Home)\|(Road))?$`                                      |          |   `Y`    | 
| [_**LastNGames**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LastNGames)               | last_n_games_nullable         |                                                                                                |          |   `Y`    | 
| [_**GeneralRange**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GeneralRange)           | general_range_nullable        |                                                                                                |          |   `Y`    | 
| [_**GameSegment**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameSegment)             | game_segment_nullable         |                         `^((First Half)\|(Overtime)\|(Second Half))?$`                         |          |   `Y`    | 
| [_**DribbleRange**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DribbleRange)           | dribble_range_nullable        |                                                                                                |          |   `Y`    | 
| [_**Division**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Division)                   | division_nullable             | `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$` |          |   `Y`    | 
| [_**DateTo**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateTo)                       | date_to_nullable              |                                                                                                |          |   `Y`    | 
| [_**DateFrom**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateFrom)                   | date_from_nullable            |                                                                                                |          |   `Y`    | 
| [_**Conference**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Conference)               | conference_nullable           |                                     `^((East)\|(West))?$`                                      |          |   `Y`    | 
| [_**CloseDefDistRange**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#CloseDefDistRange) | close_def_dist_range_nullable |                                                                                                |          |   `Y`    | 

## Data Sets
#### LeagueDashPTShots `league_dash_ptshots`
```text
['TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'GP', 'G', 'FGA_FREQUENCY', 'FGM', 'FGA', 'FG_PCT', 'EFG_PCT', 'FG2A_FREQUENCY', 'FG2M', 'FG2A', 'FG2_PCT', 'FG3A_FREQUENCY', 'FG3M', 'FG3A', 'FG3_PCT']
```


## JSON
```json
{
    "data_sets": {
        "LeagueDashPTShots": [
            "TEAM_ID",
            "TEAM_NAME",
            "TEAM_ABBREVIATION",
            "GP",
            "G",
            "FGA_FREQUENCY",
            "FGM",
            "FGA",
            "FG_PCT",
            "EFG_PCT",
            "FG2A_FREQUENCY",
            "FG2M",
            "FG2A",
            "FG2_PCT",
            "FG3A_FREQUENCY",
            "FG3M",
            "FG3A",
            "FG3_PCT"
        ]
    },
    "endpoint": "LeagueDashOppPtShot",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [
        "CloseDefDistRange",
        "Conference",
        "DateFrom",
        "DateTo",
        "Division",
        "DribbleRange",
        "GameSegment",
        "GeneralRange",
        "LastNGames",
        "Location",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "PORound",
        "Period",
        "SeasonSegment",
        "ShotClockRange",
        "ShotDistRange",
        "TeamID",
        "TouchTimeRange",
        "VsConference",
        "VsDivision"
    ],
    "parameter_patterns": {
        "CloseDefDistRange": null,
        "Conference": "^((East)|(West))?$",
        "DateFrom": null,
        "DateTo": null,
        "Division": "^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$",
        "DribbleRange": null,
        "GameSegment": "^((First Half)|(Overtime)|(Second Half))?$",
        "GeneralRange": null,
        "LastNGames": null,
        "LeagueID": "^\\d{2}$",
        "Location": "^((Home)|(Road))?$",
        "Month": null,
        "OpponentTeamID": null,
        "Outcome": "^((W)|(L))?$",
        "PORound": null,
        "PerMode": "^(Totals)|(PerGame)$",
        "Period": null,
        "Season": null,
        "SeasonSegment": "^((Post All-Star)|(Pre All-Star))?$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$",
        "ShotClockRange": null,
        "ShotDistRange": null,
        "TeamID": null,
        "TouchTimeRange": null,
        "VsConference": "^((East)|(West))?$",
        "VsDivision": "^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$"
    },
    "parameters": [
        "CloseDefDistRange",
        "Conference",
        "DateFrom",
        "DateTo",
        "Division",
        "DribbleRange",
        "GameSegment",
        "GeneralRange",
        "LastNGames",
        "LeagueID",
        "Location",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "PORound",
        "PerMode",
        "Period",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "ShotClockRange",
        "ShotDistRange",
        "TeamID",
        "TouchTimeRange",
        "VsConference",
        "VsDivision"
    ],
    "required_parameters": [
        "LeagueID",
        "PerMode",
        "Season",
        "SeasonType"
    ],
    "status": "success"
}
```

Last validated 2020-08-16