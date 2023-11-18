# LeagueDashPlayerBioStats
##### [nba_api/stats/endpoints/leaguedashplayerbiostats.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/leaguedashplayerbiostats.py)

##### Endpoint URL
>[https://stats.nba.com/stats/leaguedashplayerbiostats](https://stats.nba.com/stats/leaguedashplayerbiostats)

##### Valid URL
>[https://stats.nba.com/stats/leaguedashplayerbiostats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=&LeagueID=00&Location=&Month=&OpponentTeamID=&Outcome=&PORound=&PerMode=Totals&Period=&PlayerExperience=&PlayerPosition=&Season=2019-20&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=&VsConference=&VsDivision=&Weight=](https://stats.nba.com/stats/leaguedashplayerbiostats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=&LeagueID=00&Location=&Month=&OpponentTeamID=&Outcome=&PORound=&PerMode=Totals&Period=&PlayerExperience=&PlayerPosition=&Season=2019-20&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=&VsConference=&VsDivision=&Weight=)

## Parameters
| API Parameter Name                                                                                                              | Python Parameter Variable             |                                                    Pattern                                                    | Required | Nullable |
|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|:-------------------------------------------------------------------------------------------------------------:|:--------:|:--------:|
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)                 | league_id                             |                                                                                                               |   `Y`    |          | 
| [_**PerMode**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PerMode)                   | per_mode_simple                       |                                            `^(Totals)\|(PerGame)$`                                            |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)                     | season                                |                                                                                                               |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType)             | season_type_all_star                  |                          `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$`                           |   `Y`    |          | 
| [_**Weight**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Weight)                     | weight_nullable                       |                                                                                                               |          |   `Y`    | 
| [_**VsDivision**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsDivision)             | vs_division_nullable                  |        `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$`         |          |   `Y`    | 
| [_**VsConference**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsConference)         | vs_conference_nullable                |                                             `^((East)\|(West))?$`                                             |          |   `Y`    | 
| [_**TeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TeamID)                     | team_id_nullable                      |                                                                                                               |          |   `Y`    | 
| [_**StarterBench**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#StarterBench)         | starter_bench_nullable                |                                           `((Starters)\|(Bench))?`                                            |          |   `Y`    | 
| [_**ShotClockRange**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#ShotClockRange)     | shot_clock_range_nullable             | `((24-22)\|(22-18 Very Early)\|(18-15 Early)\|(15-7 Average)\|(7-4 Late)\|(4-0 Very Late)\|(ShotClock Off))?` |          |   `Y`    | 
| [_**SeasonSegment**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonSegment)       | season_segment_nullable               |                                    `^((Post All-Star)\|(Pre All-Star))?$`                                     |          |   `Y`    | 
| [_**PlayerPosition**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerPosition)     | player_position_abbreviation_nullable |                                `((F)\|(C)\|(G)\|(C-F)\|(F-C)\|(F-G)\|(G-F))?`                                 |          |   `Y`    | 
| [_**PlayerExperience**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerExperience) | player_experience_nullable            |                                     `((Rookie)\|(Sophomore)\|(Veteran))?`                                     |          |   `Y`    | 
| [_**Period**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Period)                     | period_nullable                       |                                                                                                               |          |   `Y`    | 
| [_**PORound**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PORound)                   | po_round_nullable                     |                                                                                                               |          |   `Y`    | 
| [_**Outcome**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Outcome)                   | outcome_nullable                      |                                                `^((W)\|(L))?$`                                                |          |   `Y`    | 
| [_**OpponentTeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#OpponentTeamID)     | opponent_team_id_nullable             |                                                                                                               |          |   `Y`    | 
| [_**Month**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Month)                       | month_nullable                        |                                                                                                               |          |   `Y`    | 
| [_**Location**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Location)                 | location_nullable                     |                                             `^((Home)\|(Road))?$`                                             |          |   `Y`    | 
| [_**LastNGames**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LastNGames)             | last_n_games_nullable                 |                                                                                                               |          |   `Y`    | 
| [_**Height**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Height)                     | height_nullable                       |                                                                                                               |          |   `Y`    | 
| [_**GameSegment**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameSegment)           | game_segment_nullable                 |                                `^((First Half)\|(Overtime)\|(Second Half))?$`                                 |          |   `Y`    | 
| [_**GameScope**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameScope)               | game_scope_simple_nullable            |                                          `((Yesterday)\|(Last 10))?`                                          |          |   `Y`    | 
| [_**DraftYear**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DraftYear)               | draft_year_nullable                   |                                                                                                               |          |   `Y`    | 
| [_**DraftPick**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DraftPick)               | draft_pick_nullable                   |                                                                                                               |          |   `Y`    | 
| [_**Division**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Division)                 | division_simple_nullable              |                 `((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest))?`                  |          |   `Y`    | 
| [_**DateTo**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateTo)                     | date_to_nullable                      |                                                                                                               |          |   `Y`    | 
| [_**DateFrom**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateFrom)                 | date_from_nullable                    |                                                                                                               |          |   `Y`    | 
| [_**Country**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Country)                   | country_nullable                      |                                                                                                               |          |   `Y`    | 
| [_**Conference**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Conference)             | conference_nullable                   |                                              `((East)\|(West))?`                                              |          |   `Y`    | 
| [_**College**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#College)                   | college_nullable                      |                                                                                                               |          |   `Y`    | 

## Data Sets
#### LeagueDashPlayerBioStats `league_dash_player_bio_stats`
```text
['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ID', 'TEAM_ABBREVIATION', 'AGE', 'PLAYER_HEIGHT', 'PLAYER_HEIGHT_INCHES', 'PLAYER_WEIGHT', 'COLLEGE', 'COUNTRY', 'DRAFT_YEAR', 'DRAFT_ROUND', 'DRAFT_NUMBER', 'GP', 'PTS', 'REB', 'AST', 'NET_RATING', 'OREB_PCT', 'DREB_PCT', 'USG_PCT', 'TS_PCT', 'AST_PCT']
```


## JSON
```json
{
    "data_sets": {
        "LeagueDashPlayerBioStats": [
            "PLAYER_ID",
            "PLAYER_NAME",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "AGE",
            "PLAYER_HEIGHT",
            "PLAYER_HEIGHT_INCHES",
            "PLAYER_WEIGHT",
            "COLLEGE",
            "COUNTRY",
            "DRAFT_YEAR",
            "DRAFT_ROUND",
            "DRAFT_NUMBER",
            "GP",
            "PTS",
            "REB",
            "AST",
            "NET_RATING",
            "OREB_PCT",
            "DREB_PCT",
            "USG_PCT",
            "TS_PCT",
            "AST_PCT"
        ]
    },
    "endpoint": "LeagueDashPlayerBioStats",
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
        "PlayerPosition",
        "SeasonSegment",
        "ShotClockRange",
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
        "GameSegment": "^((First Half)|(Overtime)|(Second Half))?$",
        "Height": null,
        "LastNGames": null,
        "LeagueID": null,
        "Location": "^((Home)|(Road))?$",
        "Month": null,
        "OpponentTeamID": null,
        "Outcome": "^((W)|(L))?$",
        "PORound": null,
        "PerMode": "^(Totals)|(PerGame)$",
        "Period": null,
        "PlayerExperience": "((Rookie)|(Sophomore)|(Veteran))?",
        "PlayerPosition": "((F)|(C)|(G)|(C-F)|(F-C)|(F-G)|(G-F))?",
        "Season": null,
        "SeasonSegment": "^((Post All-Star)|(Pre All-Star))?$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$",
        "ShotClockRange": "((24-22)|(22-18 Very Early)|(18-15 Early)|(15-7 Average)|(7-4 Late)|(4-0 Very Late)|(ShotClock Off))?",
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
        "PlayerPosition",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "ShotClockRange",
        "StarterBench",
        "TeamID",
        "VsConference",
        "VsDivision",
        "Weight"
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