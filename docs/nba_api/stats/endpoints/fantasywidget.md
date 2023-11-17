# FantasyWidget
##### [nba_api/stats/endpoints/fantasywidget.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/fantasywidget.py)

##### Endpoint URL
>[https://stats.nba.com/stats/fantasywidget](https://stats.nba.com/stats/fantasywidget)

##### Valid URL
>[https://stats.nba.com/stats/fantasywidget?ActivePlayers=N&DateFrom=&DateTo=&LastNGames=0&LeagueID=00&Location=&Month=&OpponentTeamID=&PORound=&PlayerID=&Position=&Season=2019-20&SeasonSegment=&SeasonType=Regular+Season&TeamID=&TodaysOpponent=0&TodaysPlayers=N&VsConference=&VsDivision=](https://stats.nba.com/stats/fantasywidget?ActivePlayers=N&DateFrom=&DateTo=&LastNGames=0&LeagueID=00&Location=&Month=&OpponentTeamID=&PORound=&PlayerID=&Position=&Season=2019-20&SeasonSegment=&SeasonType=Regular+Season&TeamID=&TodaysOpponent=0&TodaysPlayers=N&VsConference=&VsDivision=)

## Parameters
| API Parameter Name                                                                                                          | Python Parameter Variable |                                            Pattern                                             | Required | Nullable |
|-----------------------------------------------------------------------------------------------------------------------------|---------------------------|:----------------------------------------------------------------------------------------------:|:--------:|:--------:|
| [_**ActivePlayers**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#ActivePlayers)   | active_players            |                                          `^(Y)\|(N)$`                                          |   `Y`    |          | 
| [_**LastNGames**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LastNGames)         | last_n_games              |                                                                                                |   `Y`    |          | 
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)             | league_id                 |                                           `^\d{2}$`                                            |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)                 | season                    |                                                                                                |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType)         | season_type_all_star      |                   `^(Regular Season)\|(Pre Season)\|(Playoffs)\|(All Star)$`                   |   `Y`    |          | 
| [_**TodaysOpponent**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TodaysOpponent) | todays_opponent           |                                                                                                |   `Y`    |          | 
| [_**TodaysPlayers**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TodaysPlayers)   | todays_players            |                                          `^(Y)\|(N)$`                                          |   `Y`    |          | 
| [_**VsDivision**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsDivision)         | vs_division_nullable      | `^((Atlantic)\|(Central)\|(Northwest)\|(Pacific)\|(Southeast)\|(Southwest)\|(East)\|(West))?$` |          |   `Y`    | 
| [_**VsConference**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#VsConference)     | vs_conference_nullable    |                                     `^((East)\|(West))?$`                                      |          |   `Y`    | 
| [_**TeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TeamID)                 | team_id_nullable          |                                                                                                |          |   `Y`    | 
| [_**SeasonSegment**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonSegment)   | season_segment_nullable   |                             `^((Post All-Star)\|(Pre All-Star))?$`                             |          |   `Y`    | 
| [_**Position**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Position)             | position_nullable         |                                 `^(Guard\|Forward\|Center)?$`                                  |          |   `Y`    | 
| [_**PlayerID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerID)             | player_id_nullable        |                                                                                                |          |   `Y`    | 
| [_**PORound**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PORound)               | po_round_nullable         |                                                                                                |          |   `Y`    | 
| [_**OpponentTeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#OpponentTeamID) | opponent_team_id_nullable |                                                                                                |          |   `Y`    | 
| [_**Month**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Month)                   | month_nullable            |                                                                                                |          |   `Y`    | 
| [_**Location**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Location)             | location_nullable         |                                     `^((Home)\|(Road))?$`                                      |          |   `Y`    | 
| [_**DateTo**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateTo)                 | date_to_nullable          |                                                                                                |          |   `Y`    | 
| [_**DateFrom**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DateFrom)             | date_from_nullable        |                                                                                                |          |   `Y`    | 

## Data Sets
#### FantasyWidgetResult `fantasy_widget_result`
```text
['PLAYER_ID', 'PLAYER_NAME', 'PLAYER_POSITION', 'TEAM_ID', 'TEAM_ABBREVIATION', 'GP', 'MIN', 'FAN_DUEL_PTS', 'NBA_FANTASY_PTS', 'PTS', 'REB', 'AST', 'BLK', 'STL', 'TOV', 'FG3M', 'FGA', 'FG_PCT', 'FTA', 'FT_PCT']
```


## JSON
```json
{
    "data_sets": {
        "FantasyWidgetResult": [
            "PLAYER_ID",
            "PLAYER_NAME",
            "PLAYER_POSITION",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "GP",
            "MIN",
            "FAN_DUEL_PTS",
            "NBA_FANTASY_PTS",
            "PTS",
            "REB",
            "AST",
            "BLK",
            "STL",
            "TOV",
            "FG3M",
            "FGA",
            "FG_PCT",
            "FTA",
            "FT_PCT"
        ]
    },
    "endpoint": "FantasyWidget",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [
        "DateFrom",
        "DateTo",
        "Location",
        "Month",
        "OpponentTeamID",
        "PORound",
        "PlayerID",
        "Position",
        "SeasonSegment",
        "TeamID",
        "VsConference",
        "VsDivision"
    ],
    "parameter_patterns": {
        "ActivePlayers": "^(Y)|(N)$",
        "DateFrom": null,
        "DateTo": null,
        "LastNGames": null,
        "LeagueID": "^\\d{2}$",
        "Location": "^((Home)|(Road))?$",
        "Month": null,
        "OpponentTeamID": null,
        "PORound": null,
        "PlayerID": null,
        "Position": "^(Guard|Forward|Center)?$",
        "Season": null,
        "SeasonSegment": "^((Post All-Star)|(Pre All-Star))?$",
        "SeasonType": "^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$",
        "TeamID": null,
        "TodaysOpponent": null,
        "TodaysPlayers": "^(Y)|(N)$",
        "VsConference": "^((East)|(West))?$",
        "VsDivision": "^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$"
    },
    "parameters": [
        "ActivePlayers",
        "DateFrom",
        "DateTo",
        "LastNGames",
        "LeagueID",
        "Location",
        "Month",
        "OpponentTeamID",
        "PORound",
        "PlayerID",
        "Position",
        "Season",
        "SeasonSegment",
        "SeasonType",
        "TeamID",
        "TodaysOpponent",
        "TodaysPlayers",
        "VsConference",
        "VsDivision"
    ],
    "required_parameters": [
        "ActivePlayers",
        "LastNGames",
        "LeagueID",
        "Season",
        "SeasonType",
        "TodaysOpponent",
        "TodaysPlayers"
    ],
    "status": "success"
}
```

Last validated 2020-08-16