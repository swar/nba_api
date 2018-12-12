# PlayoffPicture
##### [nba_api/stats/endpoints/playoffpicture.py](https://github.com/swar/nba_api/blob/master/nba_api/stats/endpoints/playoffpicture.py)

##### Endpoint URL
>[https://stats.nba.com/stats/playoffpicture](https://stats.nba.com/stats/playoffpicture)

##### Valid URL
>[https://stats.nba.com/stats/playoffpicture?LeagueID=00&SeasonID=22018](https://stats.nba.com/stats/playoffpicture?LeagueID=00&SeasonID=22018)

## Parameters
API Parameter Name | Python Parameter Variable | Parameter Mapping Class | Pattern | Required | Nullable
------------ | ------------ | ------------ | :-----------: | :---: | :---:
[_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id | LeagueID | `^\d{2}$` | `Y` |  | 
[_**SeasonID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonID) | season_id | SeasonID |  | `Y` |  | 

## Data Sets
#### EastConfPlayoffPicture `east_conf_playoff_picture`
```text
['CONFERENCE', 'HIGH_SEED_RANK', 'HIGH_SEED_TEAM', 'HIGH_SEED_TEAM_ID', 'LOW_SEED_RANK', 'LOW_SEED_TEAM', 'LOW_SEED_TEAM_ID', 'HIGH_SEED_SERIES_W', 'HIGH_SEED_SERIES_L', 'HIGH_SEED_SERIES_REMAINING_G', 'HIGH_SEED_SERIES_REMAINING_HOME_G', 'HIGH_SEED_SERIES_REMAINING_AWAY_G']
```

#### EastConfRemainingGames `east_conf_remaining_games`
```text
['TEAM', 'TEAM_ID', 'REMAINING_G', 'REMAINING_HOME_G', 'REMAINING_AWAY_G']
```

#### EastConfStandings `east_conf_standings`
```text
['CONFERENCE', 'RANK', 'TEAM', 'TEAM_ID', 'WINS', 'LOSSES', 'PCT', 'DIV', 'CONF', 'HOME', 'AWAY', 'GB', 'GR_OVER_500', 'GR_OVER_500_HOME', 'GR_OVER_500_AWAY', 'GR_UNDER_500', 'GR_UNDER_500_HOME', 'GR_UNDER_500_AWAY', 'RANKING_CRITERIA', 'CLINCHED_PLAYOFFS', 'CLINCHED_CONFERENCE', 'CLINCHED_DIVISION', 'ELIMINATED_PLAYOFFS', 'SOSA_REMAINING']
```

#### WestConfPlayoffPicture `west_conf_playoff_picture`
```text
['CONFERENCE', 'HIGH_SEED_RANK', 'HIGH_SEED_TEAM', 'HIGH_SEED_TEAM_ID', 'LOW_SEED_RANK', 'LOW_SEED_TEAM', 'LOW_SEED_TEAM_ID', 'HIGH_SEED_SERIES_W', 'HIGH_SEED_SERIES_L', 'HIGH_SEED_SERIES_REMAINING_G', 'HIGH_SEED_SERIES_REMAINING_HOME_G', 'HIGH_SEED_SERIES_REMAINING_AWAY_G']
```

#### WestConfRemainingGames `west_conf_remaining_games`
```text
['TEAM', 'TEAM_ID', 'REMAINING_G', 'REMAINING_HOME_G', 'REMAINING_AWAY_G']
```

#### WestConfStandings `west_conf_standings`
```text
['CONFERENCE', 'RANK', 'TEAM', 'TEAM_ID', 'WINS', 'LOSSES', 'PCT', 'DIV', 'CONF', 'HOME', 'AWAY', 'GB', 'GR_OVER_500', 'GR_OVER_500_HOME', 'GR_OVER_500_AWAY', 'GR_UNDER_500', 'GR_UNDER_500_HOME', 'GR_UNDER_500_AWAY', 'RANKING_CRITERIA', 'CLINCHED_PLAYOFFS', 'CLINCHED_CONFERENCE', 'CLINCHED_DIVISION', 'ELIMINATED_PLAYOFFS', 'SOSA_REMAINING']
```


## JSON
```json
{
    "data_sets": {
        "EastConfPlayoffPicture": [
            "CONFERENCE",
            "HIGH_SEED_RANK",
            "HIGH_SEED_TEAM",
            "HIGH_SEED_TEAM_ID",
            "LOW_SEED_RANK",
            "LOW_SEED_TEAM",
            "LOW_SEED_TEAM_ID",
            "HIGH_SEED_SERIES_W",
            "HIGH_SEED_SERIES_L",
            "HIGH_SEED_SERIES_REMAINING_G",
            "HIGH_SEED_SERIES_REMAINING_HOME_G",
            "HIGH_SEED_SERIES_REMAINING_AWAY_G"
        ],
        "EastConfRemainingGames": [
            "TEAM",
            "TEAM_ID",
            "REMAINING_G",
            "REMAINING_HOME_G",
            "REMAINING_AWAY_G"
        ],
        "EastConfStandings": [
            "CONFERENCE",
            "RANK",
            "TEAM",
            "TEAM_ID",
            "WINS",
            "LOSSES",
            "PCT",
            "DIV",
            "CONF",
            "HOME",
            "AWAY",
            "GB",
            "GR_OVER_500",
            "GR_OVER_500_HOME",
            "GR_OVER_500_AWAY",
            "GR_UNDER_500",
            "GR_UNDER_500_HOME",
            "GR_UNDER_500_AWAY",
            "RANKING_CRITERIA",
            "CLINCHED_PLAYOFFS",
            "CLINCHED_CONFERENCE",
            "CLINCHED_DIVISION",
            "ELIMINATED_PLAYOFFS",
            "SOSA_REMAINING"
        ],
        "WestConfPlayoffPicture": [
            "CONFERENCE",
            "HIGH_SEED_RANK",
            "HIGH_SEED_TEAM",
            "HIGH_SEED_TEAM_ID",
            "LOW_SEED_RANK",
            "LOW_SEED_TEAM",
            "LOW_SEED_TEAM_ID",
            "HIGH_SEED_SERIES_W",
            "HIGH_SEED_SERIES_L",
            "HIGH_SEED_SERIES_REMAINING_G",
            "HIGH_SEED_SERIES_REMAINING_HOME_G",
            "HIGH_SEED_SERIES_REMAINING_AWAY_G"
        ],
        "WestConfRemainingGames": [
            "TEAM",
            "TEAM_ID",
            "REMAINING_G",
            "REMAINING_HOME_G",
            "REMAINING_AWAY_G"
        ],
        "WestConfStandings": [
            "CONFERENCE",
            "RANK",
            "TEAM",
            "TEAM_ID",
            "WINS",
            "LOSSES",
            "PCT",
            "DIV",
            "CONF",
            "HOME",
            "AWAY",
            "GB",
            "GR_OVER_500",
            "GR_OVER_500_HOME",
            "GR_OVER_500_AWAY",
            "GR_UNDER_500",
            "GR_UNDER_500_HOME",
            "GR_UNDER_500_AWAY",
            "RANKING_CRITERIA",
            "CLINCHED_PLAYOFFS",
            "CLINCHED_CONFERENCE",
            "CLINCHED_DIVISION",
            "ELIMINATED_PLAYOFFS",
            "SOSA_REMAINING"
        ]
    },
    "endpoint": "PlayoffPicture",
    "last_validated_date": "2018-12-11",
    "nullable_parameters": [],
    "parameter_patterns": {
        "LeagueID": "^\\d{2}$",
        "SeasonID": null
    },
    "parameters": [
        "LeagueID",
        "SeasonID"
    ],
    "required_parameters": [
        "LeagueID",
        "SeasonID"
    ],
    "status": "success"
}
```

Last validated 2018-12-11