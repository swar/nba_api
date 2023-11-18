# PlayerProfileV2
##### [nba_api/stats/endpoints/playerprofilev2.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/playerprofilev2.py)

##### Endpoint URL
>[https://stats.nba.com/stats/playerprofilev2](https://stats.nba.com/stats/playerprofilev2)

##### Valid URL
>[https://stats.nba.com/stats/playerprofilev2?LeagueID=&PerMode=Totals&PlayerID=2544](https://stats.nba.com/stats/playerprofilev2?LeagueID=&PerMode=Totals&PlayerID=2544)

## Parameters
| API Parameter Name                                                                                              | Python Parameter Variable |             Pattern              | Required | Nullable |
|-----------------------------------------------------------------------------------------------------------------|---------------------------|:--------------------------------:|:--------:|:--------:|
| [_**PerMode**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PerMode)   | per_mode36                | `^(Totals)\|(PerGame)\|(Per36)$` |   `Y`    |          | 
| [_**PlayerID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerID) | player_id                 |                                  |   `Y`    |          | 
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id_nullable        |                                  |          |   `Y`    | 

## Data Sets
#### CareerHighs `career_highs`
```text
['PLAYER_ID', 'GAME_DATE', 'VS_TEAM_ID', 'VS_TEAM_CITY', 'VS_TEAM_NAME', 'VS_TEAM_ABBREVIATION', 'STAT', 'STATS_VALUE', 'STAT_ORDER', 'DATE_EST']
```

#### CareerTotalsAllStarSeason `career_totals_all_star_season`
```text
['PLAYER_ID', 'LEAGUE_ID', 'TEAM_ID', 'GP', 'GS', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```

#### CareerTotalsCollegeSeason `career_totals_college_season`
```text
['PLAYER_ID', 'LEAGUE_ID', 'ORGANIZATION_ID', 'GP', 'GS', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```

#### CareerTotalsPostSeason `career_totals_post_season`
```text
['PLAYER_ID', 'LEAGUE_ID', 'TEAM_ID', 'GP', 'GS', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```

#### CareerTotalsPreseason `career_totals_preseason`
```text
['PLAYER_ID', 'LEAGUE_ID', 'TEAM_ID', 'GP', 'GS', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```

#### CareerTotalsRegularSeason `career_totals_regular_season`
```text
['PLAYER_ID', 'LEAGUE_ID', 'TEAM_ID', 'GP', 'GS', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```

#### NextGame `next_game`
```text
['GAME_ID', 'GAME_DATE', 'GAME_TIME', 'LOCATION', 'PLAYER_TEAM_ID', 'PLAYER_TEAM_CITY', 'PLAYER_TEAM_NICKNAME', 'PLAYER_TEAM_ABBREVIATION', 'VS_TEAM_ID', 'VS_TEAM_CITY', 'VS_TEAM_NICKNAME', 'VS_TEAM_ABBREVIATION']
```

#### SeasonHighs `season_highs`
```text
['PLAYER_ID', 'GAME_DATE', 'VS_TEAM_ID', 'VS_TEAM_CITY', 'VS_TEAM_NAME', 'VS_TEAM_ABBREVIATION', 'STAT', 'STATS_VALUE', 'STAT_ORDER', 'DATE_EST']
```

#### SeasonRankingsPostSeason `season_rankings_post_season`
```text
['PLAYER_ID', 'SEASON_ID', 'LEAGUE_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'PLAYER_AGE', 'GP', 'GS', 'RANK_MIN', 'RANK_FGM', 'RANK_FGA', 'RANK_FG_PCT', 'RANK_FG3M', 'RANK_FG3A', 'RANK_FG3_PCT', 'RANK_FTM', 'RANK_FTA', 'RANK_FT_PCT', 'RANK_OREB', 'RANK_DREB', 'RANK_REB', 'RANK_AST', 'RANK_STL', 'RANK_BLK', 'RANK_TOV', 'RANK_PTS', 'RANK_EFF']
```

#### SeasonRankingsRegularSeason `season_rankings_regular_season`
```text
['PLAYER_ID', 'SEASON_ID', 'LEAGUE_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'PLAYER_AGE', 'GP', 'GS', 'RANK_MIN', 'RANK_FGM', 'RANK_FGA', 'RANK_FG_PCT', 'RANK_FG3M', 'RANK_FG3A', 'RANK_FG3_PCT', 'RANK_FTM', 'RANK_FTA', 'RANK_FT_PCT', 'RANK_OREB', 'RANK_DREB', 'RANK_REB', 'RANK_AST', 'RANK_STL', 'RANK_BLK', 'RANK_TOV', 'RANK_PTS', 'RANK_EFF']
```

#### SeasonTotalsAllStarSeason `season_totals_all_star_season`
```text
['PLAYER_ID', 'SEASON_ID', 'LEAGUE_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'PLAYER_AGE', 'GP', 'GS', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```

#### SeasonTotalsCollegeSeason `season_totals_college_season`
```text
['PLAYER_ID', 'SEASON_ID', 'LEAGUE_ID', 'ORGANIZATION_ID', 'SCHOOL_NAME', 'PLAYER_AGE', 'GP', 'GS', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```

#### SeasonTotalsPostSeason `season_totals_post_season`
```text
['PLAYER_ID', 'SEASON_ID', 'LEAGUE_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'PLAYER_AGE', 'GP', 'GS', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```

#### SeasonTotalsPreseason `season_totals_preseason`
```text
['PLAYER_ID', 'SEASON_ID', 'LEAGUE_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'PLAYER_AGE', 'GP', 'GS', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```

#### SeasonTotalsRegularSeason `season_totals_regular_season`
```text
['PLAYER_ID', 'SEASON_ID', 'LEAGUE_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'PLAYER_AGE', 'GP', 'GS', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
```


## JSON
```json
{
    "data_sets": {
        "CareerHighs": [
            "PLAYER_ID",
            "GAME_DATE",
            "VS_TEAM_ID",
            "VS_TEAM_CITY",
            "VS_TEAM_NAME",
            "VS_TEAM_ABBREVIATION",
            "STAT",
            "STATS_VALUE",
            "STAT_ORDER",
            "DATE_EST"
        ],
        "CareerTotalsAllStarSeason": [
            "PLAYER_ID",
            "LEAGUE_ID",
            "TEAM_ID",
            "GP",
            "GS",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "STL",
            "BLK",
            "TOV",
            "PF",
            "PTS"
        ],
        "CareerTotalsCollegeSeason": [
            "PLAYER_ID",
            "LEAGUE_ID",
            "ORGANIZATION_ID",
            "GP",
            "GS",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "STL",
            "BLK",
            "TOV",
            "PF",
            "PTS"
        ],
        "CareerTotalsPostSeason": [
            "PLAYER_ID",
            "LEAGUE_ID",
            "TEAM_ID",
            "GP",
            "GS",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "STL",
            "BLK",
            "TOV",
            "PF",
            "PTS"
        ],
        "CareerTotalsPreseason": [
            "PLAYER_ID",
            "LEAGUE_ID",
            "TEAM_ID",
            "GP",
            "GS",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "STL",
            "BLK",
            "TOV",
            "PF",
            "PTS"
        ],
        "CareerTotalsRegularSeason": [
            "PLAYER_ID",
            "LEAGUE_ID",
            "TEAM_ID",
            "GP",
            "GS",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "STL",
            "BLK",
            "TOV",
            "PF",
            "PTS"
        ],
        "NextGame": [
            "GAME_ID",
            "GAME_DATE",
            "GAME_TIME",
            "LOCATION",
            "PLAYER_TEAM_ID",
            "PLAYER_TEAM_CITY",
            "PLAYER_TEAM_NICKNAME",
            "PLAYER_TEAM_ABBREVIATION",
            "VS_TEAM_ID",
            "VS_TEAM_CITY",
            "VS_TEAM_NICKNAME",
            "VS_TEAM_ABBREVIATION"
        ],
        "SeasonHighs": [
            "PLAYER_ID",
            "GAME_DATE",
            "VS_TEAM_ID",
            "VS_TEAM_CITY",
            "VS_TEAM_NAME",
            "VS_TEAM_ABBREVIATION",
            "STAT",
            "STATS_VALUE",
            "STAT_ORDER",
            "DATE_EST"
        ],
        "SeasonRankingsPostSeason": [
            "PLAYER_ID",
            "SEASON_ID",
            "LEAGUE_ID",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "PLAYER_AGE",
            "GP",
            "GS",
            "RANK_MIN",
            "RANK_FGM",
            "RANK_FGA",
            "RANK_FG_PCT",
            "RANK_FG3M",
            "RANK_FG3A",
            "RANK_FG3_PCT",
            "RANK_FTM",
            "RANK_FTA",
            "RANK_FT_PCT",
            "RANK_OREB",
            "RANK_DREB",
            "RANK_REB",
            "RANK_AST",
            "RANK_STL",
            "RANK_BLK",
            "RANK_TOV",
            "RANK_PTS",
            "RANK_EFF"
        ],
        "SeasonRankingsRegularSeason": [
            "PLAYER_ID",
            "SEASON_ID",
            "LEAGUE_ID",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "PLAYER_AGE",
            "GP",
            "GS",
            "RANK_MIN",
            "RANK_FGM",
            "RANK_FGA",
            "RANK_FG_PCT",
            "RANK_FG3M",
            "RANK_FG3A",
            "RANK_FG3_PCT",
            "RANK_FTM",
            "RANK_FTA",
            "RANK_FT_PCT",
            "RANK_OREB",
            "RANK_DREB",
            "RANK_REB",
            "RANK_AST",
            "RANK_STL",
            "RANK_BLK",
            "RANK_TOV",
            "RANK_PTS",
            "RANK_EFF"
        ],
        "SeasonTotalsAllStarSeason": [
            "PLAYER_ID",
            "SEASON_ID",
            "LEAGUE_ID",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "PLAYER_AGE",
            "GP",
            "GS",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "STL",
            "BLK",
            "TOV",
            "PF",
            "PTS"
        ],
        "SeasonTotalsCollegeSeason": [
            "PLAYER_ID",
            "SEASON_ID",
            "LEAGUE_ID",
            "ORGANIZATION_ID",
            "SCHOOL_NAME",
            "PLAYER_AGE",
            "GP",
            "GS",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "STL",
            "BLK",
            "TOV",
            "PF",
            "PTS"
        ],
        "SeasonTotalsPostSeason": [
            "PLAYER_ID",
            "SEASON_ID",
            "LEAGUE_ID",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "PLAYER_AGE",
            "GP",
            "GS",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "STL",
            "BLK",
            "TOV",
            "PF",
            "PTS"
        ],
        "SeasonTotalsPreseason": [
            "PLAYER_ID",
            "SEASON_ID",
            "LEAGUE_ID",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "PLAYER_AGE",
            "GP",
            "GS",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "STL",
            "BLK",
            "TOV",
            "PF",
            "PTS"
        ],
        "SeasonTotalsRegularSeason": [
            "PLAYER_ID",
            "SEASON_ID",
            "LEAGUE_ID",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "PLAYER_AGE",
            "GP",
            "GS",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "STL",
            "BLK",
            "TOV",
            "PF",
            "PTS"
        ]
    },
    "endpoint": "PlayerProfileV2",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [
        "LeagueID"
    ],
    "parameter_patterns": {
        "LeagueID": null,
        "PerMode": "^(Totals)|(PerGame)|(Per36)$",
        "PlayerID": null
    },
    "parameters": [
        "LeagueID",
        "PerMode",
        "PlayerID"
    ],
    "required_parameters": [
        "PerMode",
        "PlayerID"
    ],
    "status": "success"
}
```

Last validated 2020-08-16