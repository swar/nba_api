# LeagueDashPtStats
##### [nba_api/stats/endpoints/leaguedashptstats.py](https://github.com/swar/nba_api/blob/master/nba_api/stats/endpoints/leaguedashptstats.py)

##### Endpoint URL
>[https://stats.nba.com/stats/leaguedashptstats](https://stats.nba.com/stats/leaguedashptstats)

##### Valid URL
>[https://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=&PerMode=Totals&PlayerExperience=&PlayerOrTeam=Team&PlayerPosition=&PtMeasureType=SpeedDistance&Season=2018-19&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=&VsConference=&VsDivision=&Weight=](https://stats.nba.com/stats/leaguedashptstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&Height=&LastNGames=0&LeagueID=&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=&PerMode=Totals&PlayerExperience=&PlayerOrTeam=Team&PlayerPosition=&PtMeasureType=SpeedDistance&Season=2018-19&SeasonSegment=&SeasonType=Regular+Season&StarterBench=&TeamID=&VsConference=&VsDivision=&Weight=)

## Parameters
API Parameter Name | Python Parameter Class | Python Parameter Variable | Pattern | Required | Nullable
------------ | ------------ | ------------ | :-----------: | :---: | :---:
_**LastNGames**_ | [LastNGames](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LastNGames) | last_n_games |  | `Y` |  | 
_**Month**_ | [Month](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Month) | month |  | `Y` |  | 
_**OpponentTeamID**_ | [OpponentTeamID](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#OpponentTeamID) | opponent_team_id |  | `Y` |  | 
_**PerMode**_ | [PerModeSimple](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PerMode) | per_mode_simple | `^(Totals)\|(PerGame)$` | `Y` |  | 
_**PlayerOrTeam**_ | [PlayerOrTeam](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerOrTeam) | player_or_team | `^(Player)\|(Team)$` | `Y` |  | 
_**PtMeasureType**_ | [PtMeasureType](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PtMeasureType) | pt_measure_type | `^(SpeedDistance)\|(Rebounding)\|(Possessions)\|(CatchShoot)\|(PullUpShot)\|(Defense)\|(Drives)\|(Passing)\|(ElbowTouch)\|(PostTouch)\|(PaintTouch)\|(Efficiency)$` | `Y` |  | 
_**Season**_ | [Season](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season) | season | `^\d{4}-\d{2}$` | `Y` |  | 
_**SeasonType**_ | [SeasonTypeAllStar](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType) | season_type_all_star | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$` | `Y` |  | 
_**Weight**_ | [WeightNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Weight) | weight_nullable |  |  | `Y` | 
_**VsDivision**_ | [VsDivisionNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsDivision) | vs_division_nullable | `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$` | `Y` | `Y` | 
_**VsConference**_ | [VsConferenceNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsConference) | vs_conference_nullable | `^((East)\|(West))?$` | `Y` | `Y` | 
_**TeamID**_ | [TeamIDNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TeamID) | team_id_nullable |  |  | `Y` | 
_**StarterBench**_ | [StarterBenchNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#StarterBench) | starter_bench_nullable | `((Starters)\|(Bench))?` | `Y` | `Y` | 
_**SeasonSegment**_ | [SeasonSegmentNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonSegment) | season_segment_nullable | `^((Post All-Star)\|(Pre All-Star))?$` | `Y` | `Y` | 
_**PlayerPosition**_ | [PlayerPositionAbbreviationNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerPosition) | player_position_abbreviation_nullable | `((F)\|(C)\|(G)\|(C-F)\|(F-C)\|(F-G)\|(G-F))?` | `Y` | `Y` | 
_**PlayerExperience**_ | [PlayerExperienceNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerExperience) | player_experience_nullable | `((Rookie)\|(Sophomore)\|(Veteran))?` | `Y` | `Y` | 
_**PORound**_ | [PORoundNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PORound) | po_round_nullable |  |  | `Y` | 
_**Outcome**_ | [OutcomeNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Outcome) | outcome_nullable | `^((W)\|(L))?$` | `Y` | `Y` | 
_**Location**_ | [LocationNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Location) | location_nullable | `^((Home)\|(Road))?$` | `Y` | `Y` | 
_**LeagueID**_ | [LeagueIDNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id_nullable | `(00)\|(20)\|(10)` |  | `Y` | 
_**Height**_ | [HeightNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Height) | height_nullable |  |  | `Y` | 
_**GameScope**_ | [GameScopeSimpleNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameScope) | game_scope_simple_nullable | `((Yesterday)\|(Last 10))?` | `Y` | `Y` | 
_**DraftYear**_ | [DraftYearNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DraftYear) | draft_year_nullable |  |  | `Y` | 
_**DraftPick**_ | [DraftPickNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DraftPick) | draft_pick_nullable |  |  | `Y` | 
_**Division**_ | [DivisionSimpleNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Division) | division_simple_nullable | `((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest))?` |  | `Y` | 
_**DateTo**_ | [DateToNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateTo) | date_to_nullable |  | `Y` | `Y` | 
_**DateFrom**_ | [DateFromNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateFrom) | date_from_nullable |  | `Y` | `Y` | 
_**Country**_ | [CountryNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Country) | country_nullable |  |  | `Y` | 
_**Conference**_ | [ConferenceNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Conference) | conference_nullable | `((East)\|(West))?` |  | `Y` | 
_**College**_ | [CollegeNullable](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#College) | college_nullable |  |  | `Y` | 

## Data Sets
#### LeagueDashPtStats `league_dash_pt_stats`
```text
['TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'GP', 'W', 'L', 'MIN', 'DIST_FEET', 'DIST_MILES', 'DIST_MILES_OFF', 'DIST_MILES_DEF', 'AVG_SPEED', 'AVG_SPEED_OFF', 'AVG_SPEED_DEF']
```


## JSON
```json
{
    "data_sets": {
        "LeagueDashPtStats": [
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "TEAM_NAME",
            "GP",
            "W",
            "L",
            "MIN",
            "DIST_FEET",
            "DIST_MILES",
            "DIST_MILES_OFF",
            "DIST_MILES_DEF",
            "AVG_SPEED",
            "AVG_SPEED_OFF",
            "AVG_SPEED_DEF"
        ]
    },
    "endpoint": "LeagueDashPtStats",
    "last_validated_date": "2018-12-11",
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
        "LeagueID",
        "Location",
        "Outcome",
        "PORound",
        "PlayerExperience",
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
        "LeagueID": "(00)|(20)|(10)",
        "Location": "^((Home)|(Road))?$",
        "Month": null,
        "OpponentTeamID": null,
        "Outcome": "^((W)|(L))?$",
        "PORound": null,
        "PerMode": "^(Totals)|(PerGame)$",
        "PlayerExperience": "((Rookie)|(Sophomore)|(Veteran))?",
        "PlayerOrTeam": "^(Player)|(Team)$",
        "PlayerPosition": "((F)|(C)|(G)|(C-F)|(F-C)|(F-G)|(G-F))?",
        "PtMeasureType": "^(SpeedDistance)|(Rebounding)|(Possessions)|(CatchShoot)|(PullUpShot)|(Defense)|(Drives)|(Passing)|(ElbowTouch)|(PostTouch)|(PaintTouch)|(Efficiency)$",
        "Season": "^\\d{4}-\\d{2}$",
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
        "PlayerOrTeam",
        "PlayerPosition",
        "PtMeasureType",
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
        "DateFrom",
        "DateTo",
        "GameScope",
        "LastNGames",
        "Location",
        "Month",
        "OpponentTeamID",
        "Outcome",
        "PerMode",
        "PlayerExperience",
        "PlayerOrTeam",
        "PlayerPosition",
        "PtMeasureType",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "StarterBench",
        "VsConference",
        "VsDivision"
    ],
    "status": "success"
}
```

Last validated 2018-12-11