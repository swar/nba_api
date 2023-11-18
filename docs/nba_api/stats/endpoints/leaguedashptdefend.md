# LeagueDashPtDefend
##### [nba_api/stats/endpoints/leaguedashptdefend.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/leaguedashptdefend.py)

##### Endpoint URL
>[https://stats.nba.com/stats/leaguedashptdefend](https://stats.nba.com/stats/leaguedashptdefend)

##### Valid URL
>[https://stats.nba.com/stats/leaguedashptdefend?College=&Conference=&Country=&DateFrom=&DateTo=&DefenseCategory=Overall&Division=&DraftPick=&DraftYear=&GameSegment=&Height=&LastNGames=&LeagueID=00&Location=&Month=&OpponentTeamID=&Outcome=&PORound=&PerMode=Totals&Period=&PlayerExperience=&PlayerID=&PlayerPosition=&Season=2019-20&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=&VsConference=&VsDivision=&Weight=](https://stats.nba.com/stats/leaguedashptdefend?College=&Conference=&Country=&DateFrom=&DateTo=&DefenseCategory=Overall&Division=&DraftPick=&DraftYear=&GameSegment=&Height=&LastNGames=&LeagueID=00&Location=&Month=&OpponentTeamID=&Outcome=&PORound=&PerMode=Totals&Period=&PlayerExperience=&PlayerID=&PlayerPosition=&Season=2019-20&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=&VsConference=&VsDivision=&Weight=)

## Parameters
| API Parameter Name                                                                                                              | Python Parameter Variable  |                                               Pattern                                                | Required | Nullable |
|---------------------------------------------------------------------------------------------------------------------------------|----------------------------|:----------------------------------------------------------------------------------------------------:|:--------:|:--------:|
| [_**DefenseCategory**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DefenseCategory)   | defense_category           | `^((Overall)\|(3 Pointers)\|(2 Pointers)\|(Less Than 6Ft)\|(Less Than 10Ft)\|(Greater Than 15Ft))?$` |   `Y`    |          | 
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)                 | league_id                  |                                              `^\d{2}$`                                               |   `Y`    |          | 
| [_**PerMode**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PerMode)                   | per_mode_simple            |                                       `^(Totals)\|(PerGame)$`                                        |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)                     | season                     |                                                                                                      |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType)             | season_type_all_star       |                      `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$`                      |   `Y`    |          | 
| [_**Weight**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Weight)                     | weight_nullable            |                                                                                                      |          |   `Y`    | 
| [_**VsDivision**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsDivision)             | vs_division_nullable       |    `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$`    |          |   `Y`    | 
| [_**VsConference**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsConference)         | vs_conference_nullable     |                                        `^((East)\|(West))?$`                                         |          |   `Y`    | 
| [_**TeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TeamID)                     | team_id_nullable           |                                                                                                      |          |   `Y`    | 
| [_**StarterBench**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#StarterBench)         | starter_bench_nullable     |                                                                                                      |          |   `Y`    | 
| [_**SeasonSegment**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonSegment)       | season_segment_nullable    |                                `^((Post All-Star)\|(Pre All-Star))?$`                                |          |   `Y`    | 
| [_**PlayerPosition**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerPosition)     | player_position_nullable   |                                                                                                      |          |   `Y`    | 
| [_**PlayerID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerID)                 | player_id_nullable         |                                                                                                      |          |   `Y`    | 
| [_**PlayerExperience**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerExperience) | player_experience_nullable |                                                                                                      |          |   `Y`    | 
| [_**Period**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Period)                     | period_nullable            |                                                                                                      |          |   `Y`    | 
| [_**PORound**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PORound)                   | po_round_nullable          |                                                                                                      |          |   `Y`    | 
| [_**Outcome**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Outcome)                   | outcome_nullable           |                                           `^((W)\|(L))?$`                                            |          |   `Y`    | 
| [_**OpponentTeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#OpponentTeamID)     | opponent_team_id_nullable  |                                                                                                      |          |   `Y`    | 
| [_**Month**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Month)                       | month_nullable             |                                                                                                      |          |   `Y`    | 
| [_**Location**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Location)                 | location_nullable          |                                        `^((Home)\|(Road))?$`                                         |          |   `Y`    | 
| [_**LastNGames**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LastNGames)             | last_n_games_nullable      |                                                                                                      |          |   `Y`    | 
| [_**Height**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Height)                     | height_nullable            |                                                                                                      |          |   `Y`    | 
| [_**GameSegment**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameSegment)           | game_segment_nullable      |                            `^((First Half)\|(Overtime)\|(Second Half))?$`                            |          |   `Y`    | 
| [_**DraftYear**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DraftYear)               | draft_year_nullable        |                                                                                                      |          |   `Y`    | 
| [_**DraftPick**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DraftPick)               | draft_pick_nullable        |                                                                                                      |          |   `Y`    | 
| [_**Division**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Division)                 | division_nullable          |    `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$`    |          |   `Y`    | 
| [_**DateTo**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateTo)                     | date_to_nullable           |                                                                                                      |          |   `Y`    | 
| [_**DateFrom**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateFrom)                 | date_from_nullable         |                                                                                                      |          |   `Y`    | 
| [_**Country**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Country)                   | country_nullable           |                                                                                                      |          |   `Y`    | 
| [_**Conference**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Conference)             | conference_nullable        |                                        `^((East)\|(West))?$`                                         |          |   `Y`    | 
| [_**College**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#College)                   | college_nullable           |                                                                                                      |          |   `Y`    | 

## Data Sets
#### LeagueDashPTDefend `league_dash_p_tdefend`
```text
['CLOSE_DEF_PERSON_ID', 'PLAYER_NAME', 'PLAYER_LAST_TEAM_ID', 'PLAYER_LAST_TEAM_ABBREVIATION', 'PLAYER_POSITION', 'AGE', 'GP', 'G', 'FREQ', 'D_FGM', 'D_FGA', 'D_FG_PCT', 'NORMAL_FG_PCT', 'PCT_PLUSMINUS']
```


## JSON
```json
{
    "data_sets": {
        "LeagueDashPTDefend": [
            "CLOSE_DEF_PERSON_ID",
            "PLAYER_NAME",
            "PLAYER_LAST_TEAM_ID",
            "PLAYER_LAST_TEAM_ABBREVIATION",
            "PLAYER_POSITION",
            "AGE",
            "GP",
            "G",
            "FREQ",
            "D_FGM",
            "D_FGA",
            "D_FG_PCT",
            "NORMAL_FG_PCT",
            "PCT_PLUSMINUS"
        ]
    },
    "endpoint": "LeagueDashPtDefend",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [
        "College",
        "Conference",
        "Country",
        "DateFrom",
        "DateTo",
        "Division",
        "DraftPick",
        "DraftYear",
        "GameSegment",
        "Height",
        "LastNGames",
        "Location",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "PORound",
        "Period",
        "PlayerExperience",
        "PlayerID",
        "PlayerPosition",
        "SeasonSegment",
        "StarterBench",
        "TeamID",
        "VsConference",
        "VsDivision",
        "Weight"
    ],
    "parameter_patterns": {
        "College": null,
        "Conference": "^((East)|(West))?$",
        "Country": null,
        "DateFrom": null,
        "DateTo": null,
        "DefenseCategory": "^((Overall)|(3 Pointers)|(2 Pointers)|(Less Than 6Ft)|(Less Than 10Ft)|(Greater Than 15Ft))?$",
        "Division": "^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$",
        "DraftPick": null,
        "DraftYear": null,
        "GameSegment": "^((First Half)|(Overtime)|(Second Half))?$",
        "Height": null,
        "LastNGames": null,
        "LeagueID": "^\\d{2}$",
        "Location": "^((Home)|(Road))?$",
        "Month": null,
        "OpponentTeamID": null,
        "Outcome": "^((W)|(L))?$",
        "PORound": null,
        "PerMode": "^(Totals)|(PerGame)$",
        "Period": null,
        "PlayerExperience": null,
        "PlayerID": null,
        "PlayerPosition": null,
        "Season": null,
        "SeasonSegment": "^((Post All-Star)|(Pre All-Star))?$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$",
        "StarterBench": null,
        "TeamID": null,
        "VsConference": "^((East)|(West))?$",
        "VsDivision": "^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$",
        "Weight": null
    },
    "parameters": [
        "College",
        "Conference",
        "Country",
        "DateFrom",
        "DateTo",
        "DefenseCategory",
        "Division",
        "DraftPick",
        "DraftYear",
        "GameSegment",
        "Height",
        "LastNGames",
        "LeagueID",
        "Location",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "PORound",
        "PerMode",
        "Period",
        "PlayerExperience",
        "PlayerID",
        "PlayerPosition",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "StarterBench",
        "TeamID",
        "VsConference",
        "VsDivision",
        "Weight"
    ],
    "required_parameters": [
        "DefenseCategory",
        "LeagueID",
        "PerMode",
        "Season",
        "SeasonType"
    ],
    "status": "success"
}
```

Last validated 2020-08-16