# DraftHistory
##### [nba_api/stats/endpoints/drafthistory.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/drafthistory.py)

##### Endpoint URL
>[https://stats.nba.com/stats/drafthistory](https://stats.nba.com/stats/drafthistory)

##### Valid URL
>[https://stats.nba.com/stats/drafthistory?College=&LeagueID=00&OverallPick=&RoundNum=&RoundPick=&Season=&TeamID=&TopX=](https://stats.nba.com/stats/drafthistory?College=&LeagueID=00&OverallPick=&RoundNum=&RoundPick=&Season=&TeamID=&TopX=)

## Parameters
| API Parameter Name                                                                                                    | Python Parameter Variable |  Pattern  | Required | Nullable |
|-----------------------------------------------------------------------------------------------------------------------|---------------------------|:---------:|:--------:|:--------:|
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)       | league_id                 | `^\d{2}$` |   `Y`    |          | 
| [_**TopX**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TopX)               | topx_nullable             |           |          |   `Y`    | 
| [_**TeamID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#TeamID)           | team_id_nullable          |           |          |   `Y`    | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)           | season_year_nullable      | `^\d{4}$` |          |   `Y`    | 
| [_**RoundPick**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#RoundPick)     | round_pick_nullable       |           |          |   `Y`    | 
| [_**RoundNum**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#RoundNum)       | round_num_nullable        |           |          |   `Y`    | 
| [_**OverallPick**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#OverallPick) | overall_pick_nullable     |           |          |   `Y`    | 
| [_**College**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#College)         | college_nullable          |           |          |   `Y`    | 

## Data Sets
#### DraftHistory `draft_history`
```text
['PERSON_ID', 'PLAYER_NAME', 'SEASON', 'ROUND_NUMBER', 'ROUND_PICK', 'OVERALL_PICK', 'DRAFT_TYPE', 'TEAM_ID', 'TEAM_CITY', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'ORGANIZATION', 'ORGANIZATION_TYPE']
```


## JSON
```json
{
    "data_sets": {
        "DraftHistory": [
            "PERSON_ID",
            "PLAYER_NAME",
            "SEASON",
            "ROUND_NUMBER",
            "ROUND_PICK",
            "OVERALL_PICK",
            "DRAFT_TYPE",
            "TEAM_ID",
            "TEAM_CITY",
            "TEAM_NAME",
            "TEAM_ABBREVIATION",
            "ORGANIZATION",
            "ORGANIZATION_TYPE"
        ]
    },
    "endpoint": "DraftHistory",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [
        "College",
        "OverallPick",
        "RoundNum",
        "RoundPick",
        "Season",
        "TeamID",
        "TopX"
    ],
    "parameter_patterns": {
        "College": null,
        "LeagueID": "^\\d{2}$",
        "OverallPick": null,
        "RoundNum": null,
        "RoundPick": null,
        "Season": "^\\d{4}$",
        "TeamID": null,
        "TopX": null
    },
    "parameters": [
        "College",
        "LeagueID",
        "OverallPick",
        "RoundNum",
        "RoundPick",
        "Season",
        "TeamID",
        "TopX"
    ],
    "required_parameters": [
        "LeagueID"
    ],
    "status": "success"
}
```

Last validated 2020-08-16