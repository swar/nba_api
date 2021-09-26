# PlayerIndex
##### [nba_api/stats/endpoints/playerindex.py](https://github.com/swar/nba_api/blob/master/nba_api/stats/endpoints/playerindex.py)

##### Endpoint URL
>[https://stats.nba.com/stats/playerindex](https://stats.nba.com/stats/playerindex)

##### Valid URL
>[https://stats.nba.com/stats/playerindex?Active=&AllStar=&College=&Country=&DraftPick=&DraftYear=&Height=&Historical=&LeagueID=00&PlayerPosition=&Season=2020-21&TeamID=&Weight=](https://stats.nba.com/stats/playerindex?Active=&AllStar=&College=&Country=&DraftPick=&DraftYear=&Height=&Historical=&LeagueID=00&PlayerPosition=&Season=2020-21&TeamID=&Weight=)

## Parameters
API Parameter Name | Python Parameter Variable | Pattern | Required | Nullable
------------ | ------------ | :-----------: | :---: | :---:
[_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id |  | `Y` |  | 
[_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season) | season |  | `Y` |  | 
[_**Weight**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Weight) | weight_nullable |  |  | `Y` | 
[_**TeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TeamID) | team_id_nullable |  |  | `Y` | 
[_**PlayerPosition**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#PlayerPosition) | player_position_nullable |  |  | `Y` | 
[_**Historical**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Historical) | historical_nullable |  |  | `Y` | 
[_**Height**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Height) | height_nullable |  |  | `Y` | 
[_**DraftYear**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DraftYear) | draft_year_nullable |  |  | `Y` | 
[_**DraftPick**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#DraftPick) | draft_pick_nullable |  |  | `Y` | 
[_**Country**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Country) | country_nullable |  |  | `Y` | 
[_**College**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#College) | college_nullable |  |  | `Y` | 
[_**AllStar**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#AllStar) | all_star_nullable |  |  | `Y` | 
[_**Active**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Active) | active_nullable |  |  | `Y` | 

## Data Sets
#### PlayerIndex `player_index`
```text
['PERSON_ID', 'PLAYER_LAST_NAME', 'PLAYER_FIRST_NAME', 'PLAYER_SLUG', 'TEAM_ID', 'TEAM_SLUG', 'IS_DEFUNCT', 'TEAM_CITY', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'JERSEY_NUMBER', 'POSITION', 'HEIGHT', 'WEIGHT', 'COLLEGE', 'COUNTRY', 'DRAFT_YEAR', 'DRAFT_ROUND', 'DRAFT_NUMBER', 'ROSTER_STATUS', 'FROM_YEAR', 'TO_YEAR', 'PTS', 'REB', 'AST', 'STATS_TIMEFRAME']
```


## JSON
```json
{
    "data_sets": {
        "PlayerIndex": [
            "PERSON_ID",
            "PLAYER_LAST_NAME",
            "PLAYER_FIRST_NAME",
            "PLAYER_SLUG",
            "TEAM_ID",
            "TEAM_SLUG",
            "IS_DEFUNCT",
            "TEAM_CITY",
            "TEAM_NAME",
            "TEAM_ABBREVIATION",
            "JERSEY_NUMBER",
            "POSITION",
            "HEIGHT",
            "WEIGHT",
            "COLLEGE",
            "COUNTRY",
            "DRAFT_YEAR",
            "DRAFT_ROUND",
            "DRAFT_NUMBER",
            "ROSTER_STATUS",
            "FROM_YEAR",
            "TO_YEAR",
            "PTS",
            "REB",
            "AST",
            "STATS_TIMEFRAME"
        ]
    },
    "endpoint": "PlayerIndex",
    "last_validated_date": "2021-09-26",
    "nullable_parameters": [
        "Active",
        "AllStar",
        "College",
        "Country",
        "DraftPick",
        "DraftYear",
        "Height",
        "Historical",
        "PlayerPosition",
        "TeamID",
        "Weight"
    ],
    "parameter_patterns": {
        "Active": null,
        "AllStar": null,
        "College": null,
        "Country": null,
        "DraftPick": null,
        "DraftYear": null,
        "Height": null,
        "Historical": null,
        "LeagueID": null,
        "PlayerPosition": null,
        "Season": null,
        "TeamID": null,
        "Weight": null
    },
    "parameters": [
        "Active",
        "AllStar",
        "College",
        "Country",
        "DraftPick",
        "DraftYear",
        "Height",
        "Historical",
        "LeagueID",
        "PlayerPosition",
        "Season",
        "TeamID",
        "Weight"
    ],
    "required_parameters": [
        "LeagueID",
        "Season"
    ],
    "status": "success"
}
```

Last validated 2021-09-26