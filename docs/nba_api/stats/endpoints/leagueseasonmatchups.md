# LeagueSeasonMatchups
##### [nba_api/stats/endpoints/leagueseasonmatchups.py](https://github.com/swar/nba_api/blob/master/nba_api/stats/endpoints/leagueseasonmatchups.py)

##### Endpoint URL
>[https://stats.nba.com/stats/leagueseasonmatchups](https://stats.nba.com/stats/leagueseasonmatchups)

##### Valid URL
>[https://stats.nba.com/stats/leagueseasonmatchups?DateFrom=&DateTo=&DefPlayerID=&DefTeamID=&LeagueID=00&OffPlayerID=&OffTeamID=&Outcome=&PORound=&PerMode=&Season=2018-19&SeasonType=Regular+Season](https://stats.nba.com/stats/leagueseasonmatchups?DateFrom=&DateTo=&DefPlayerID=&DefTeamID=&LeagueID=00&OffPlayerID=&OffTeamID=&Outcome=&PORound=&PerMode=&Season=2018-19&SeasonType=Regular+Season)

## Parameters
API Parameter Name | Python Parameter Variable | Pattern | Required | Nullable
------------ | ------------ | :-----------: | :---: | :---:
[_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id | `^\d{2}$` | `Y` |  | 
[_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season) | season | `^(\d{4}-\d{2})$` | `Y` |  | 
[_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType) | season_type_playoffs | `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(Pre-Season)$` | `Y` |  | 
[_**PerMode**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PerMode) | per_mode_simple_nullable |  |  | `Y` | 
[_**PORound**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PORound) | po_round_nullable |  |  | `Y` | 
[_**Outcome**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Outcome) | outcome_nullable |  |  | `Y` | 
[_**OffTeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#OffTeamID) | off_team_id_nullable |  |  | `Y` | 
[_**OffPlayerID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#OffPlayerID) | off_player_id_nullable |  |  | `Y` | 
[_**DefTeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DefTeamID) | def_team_id_nullable |  |  | `Y` | 
[_**DefPlayerID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DefPlayerID) | def_player_id_nullable |  |  | `Y` | 
[_**DateTo**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateTo) | date_to_nullable |  |  | `Y` | 
[_**DateFrom**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateFrom) | date_from_nullable |  |  | `Y` | 

## Data Sets
#### SeasonMatchups `season_matchups`
```text
['OFF_TEAM_ID', 'OFF_TEAM_ABBREVIATION', 'OFF_TEAM_CITY', 'OFF_TEAM_NICKNAME', 'OFF_PLAYER_ID', 'OFF_PLAYER_NAME', 'DEF_TEAM_ID', 'DEF_TEAM_ABBREVIATION', 'DEF_TEAM_CITY', 'DEF_TEAM_NICKNAME', 'DEF_PLAYER_ID', 'DEF_PLAYER_NAME', 'GP', 'POSS', 'OFF_MATCHUP_PCT', 'PLAYER_PTS', 'PLAYER_PTS_DIFF', 'TEAM_PTS', 'TEAM_PTS_DIFF', 'AST', 'TOV', 'BLK', 'HELP_BLK', 'HELP_BLK_REC', 'FGM', 'FGA', 'FGA_DIFF', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'SFL', 'DEF_FOULS', 'OFF_FOULS']
```


## JSON
```json
{
    "data_sets": {
        "SeasonMatchups": [
            "OFF_TEAM_ID",
            "OFF_TEAM_ABBREVIATION",
            "OFF_TEAM_CITY",
            "OFF_TEAM_NICKNAME",
            "OFF_PLAYER_ID",
            "OFF_PLAYER_NAME",
            "DEF_TEAM_ID",
            "DEF_TEAM_ABBREVIATION",
            "DEF_TEAM_CITY",
            "DEF_TEAM_NICKNAME",
            "DEF_PLAYER_ID",
            "DEF_PLAYER_NAME",
            "GP",
            "POSS",
            "OFF_MATCHUP_PCT",
            "PLAYER_PTS",
            "PLAYER_PTS_DIFF",
            "TEAM_PTS",
            "TEAM_PTS_DIFF",
            "AST",
            "TOV",
            "BLK",
            "HELP_BLK",
            "HELP_BLK_REC",
            "FGM",
            "FGA",
            "FGA_DIFF",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "SFL",
            "DEF_FOULS",
            "OFF_FOULS"
        ]
    },
    "endpoint": "LeagueSeasonMatchups",
    "last_validated_date": "2019-04-15",
    "nullable_parameters": [
        "DateFrom",
        "DateTo",
        "DefPlayerID",
        "DefTeamID",
        "OffPlayerID",
        "OffTeamID",
        "Outcome",
        "PORound",
        "PerMode"
    ],
    "parameter_patterns": {
        "DateFrom": null,
        "DateTo": null,
        "DefPlayerID": null,
        "DefTeamID": null,
        "LeagueID": "^\\d{2}$",
        "OffPlayerID": null,
        "OffTeamID": null,
        "Outcome": null,
        "PORound": null,
        "PerMode": null,
        "Season": "^(\\d{4}-\\d{2})$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(Pre-Season)$"
    },
    "parameters": [
        "DateFrom",
        "DateTo",
        "DefPlayerID",
        "DefTeamID",
        "LeagueID",
        "OffPlayerID",
        "OffTeamID",
        "Outcome",
        "PORound",
        "PerMode",
        "Season",
        "SeasonType"
    ],
    "required_parameters": [
        "LeagueID",
        "Season",
        "SeasonType"
    ],
    "status": "success"
}
```

Last validated 2019-04-15