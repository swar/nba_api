# AssistTracker
##### [nba_api/stats/endpoints/assisttracker.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/assisttracker.py)

##### Endpoint URL
>[https://stats.nba.com/stats/assisttracker](https://stats.nba.com/stats/assisttracker)

##### Valid URL
>[https://stats.nba.com/stats/assisttracker?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=&LeagueID=&Location=&Month=&OpponentTeamID=&Outcome=&PORound=&PerMode=&PlayerExperience=&PlayerPosition=&Season=&SeasonSegment=&SeasonType=&StarterBench=&TeamID=&VsConference=&VsDivision=&Weight=](https://stats.nba.com/stats/assisttracker?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=&LeagueID=&Location=&Month=&OpponentTeamID=&Outcome=&PORound=&PerMode=&PlayerExperience=&PlayerPosition=&Season=&SeasonSegment=&SeasonType=&StarterBench=&TeamID=&VsConference=&VsDivision=&Weight=)

## Parameters
| API Parameter Name                                                                                                              | Python Parameter Variable             |                                            Pattern                                             | Required | Nullable |
|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|:----------------------------------------------------------------------------------------------:|:--------:|:--------:|
| [_**Weight**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Weight)                     | weight_nullable                       |                                                                                                |          |   `Y`    | 
| [_**VsDivision**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsDivision)             | vs_division_nullable                  | `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$` |          |   `Y`    | 
| [_**VsConference**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsConference)         | vs_conference_nullable                |                                     `^((East)\|(West))?$`                                      |          |   `Y`    | 
| [_**TeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TeamID)                     | team_id_nullable                      |                                                                                                |          |   `Y`    | 
| [_**StarterBench**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#StarterBench)         | starter_bench_nullable                |                                    `((Starters)\|(Bench))?`                                    |          |   `Y`    | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType)             | season_type_all_star_nullable         |                   `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$`                   |          |   `Y`    | 
| [_**SeasonSegment**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonSegment)       | season_segment_nullable               |                             `^((Post All-Star)\|(Pre All-Star))?$`                             |          |   `Y`    | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)                     | season_nullable                       |                                                                                                |          |   `Y`    | 
| [_**PlayerPosition**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerPosition)     | player_position_abbreviation_nullable |                         `((F)\|(C)\|(G)\|(C-F)\|(F-C)\|(F-G)\|(G-F))?`                         |          |   `Y`    | 
| [_**PlayerExperience**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerExperience) | player_experience_nullable            |                             `((Rookie)\|(Sophomore)\|(Veteran))?`                              |          |   `Y`    | 
| [_**PerMode**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PerMode)                   | per_mode_simple_nullable              |                                    `^(Totals)\|(PerGame)$`                                     |          |   `Y`    | 
| [_**PORound**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PORound)                   | po_round_nullable                     |                                                                                                |          |   `Y`    | 
| [_**Outcome**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Outcome)                   | outcome_nullable                      |                                        `^((W)\|(L))?$`                                         |          |   `Y`    | 
| [_**OpponentTeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#OpponentTeamID)     | opponent_team_id_nullable             |                                                                                                |          |   `Y`    | 
| [_**Month**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Month)                       | month_nullable                        |                                                                                                |          |   `Y`    | 
| [_**Location**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Location)                 | location_nullable                     |                                     `^((Home)\|(Road))?$`                                      |          |   `Y`    | 
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)                 | league_id_nullable                    |                                                                                                |          |   `Y`    | 
| [_**LastNGames**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LastNGames)             | last_n_games_nullable                 |                                                                                                |          |   `Y`    | 
| [_**Height**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Height)                     | height_nullable                       |                                                                                                |          |   `Y`    | 
| [_**GameScope**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameScope)               | game_scope_simple_nullable            |                                  `((Yesterday)\|(Last 10))?`                                   |          |   `Y`    | 
| [_**DraftYear**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DraftYear)               | draft_year_nullable                   |                                                                                                |          |   `Y`    | 
| [_**DraftPick**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DraftPick)               | draft_pick_nullable                   |                                                                                                |          |   `Y`    | 
| [_**Division**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Division)                 | division_simple_nullable              |          `((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest))?`          |          |   `Y`    | 
| [_**DateTo**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateTo)                     | date_to_nullable                      |                                                                                                |          |   `Y`    | 
| [_**DateFrom**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateFrom)                 | date_from_nullable                    |                                                                                                |          |   `Y`    | 
| [_**Country**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Country)                   | country_nullable                      |                                                                                                |          |   `Y`    | 
| [_**Conference**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Conference)             | conference_nullable                   |                                      `((East)\|(West))?`                                       |          |   `Y`    | 
| [_**College**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#College)                   | college_nullable                      |                                                                                                |          |   `Y`    | 

## Data Sets
#### AssistTracker `assist_tracker`
```text
['ASSISTS']
```


## JSON
```json
{
    "data_sets": {
        "AssistTracker": [
            "ASSISTS"
        ]
    },
    "endpoint": "AssistTracker",
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
        "GameScope",
        "Height",
        "LastNGames",
        "LeagueID",
        "Location",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "PORound",
        "PerMode",
        "PlayerExperience",
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
    "parameter_patterns": {
        "College": null,
        "Conference": "((East)|(West))?",
        "Country": null,
        "DateFrom": null,
        "DateTo": null,
        "Division": "((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest))?",
        "DraftPick": null,
        "DraftYear": null,
        "GameScope": "((Yesterday)|(Last 10))?",
        "Height": null,
        "LastNGames": null,
        "LeagueID": null,
        "Location": "^((Home)|(Road))?$",
        "Month": null,
        "OpponentTeamID": null,
        "Outcome": "^((W)|(L))?$",
        "PORound": null,
        "PerMode": "^(Totals)|(PerGame)$",
        "PlayerExperience": "((Rookie)|(Sophomore)|(Veteran))?",
        "PlayerPosition": "((F)|(C)|(G)|(C-F)|(F-C)|(F-G)|(G-F))?",
        "Season": null,
        "SeasonSegment": "^((Post All-Star)|(Pre All-Star))?$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$",
        "StarterBench": "((Starters)|(Bench))?",
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
        "Division",
        "DraftPick",
        "DraftYear",
        "GameScope",
        "Height",
        "LastNGames",
        "LeagueID",
        "Location",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "PORound",
        "PerMode",
        "PlayerExperience",
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
    "required_parameters": [],
    "status": "success"
}
```

Last validated 2020-08-16