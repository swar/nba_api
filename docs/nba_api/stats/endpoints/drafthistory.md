# DraftHistory

##### Endpoint URL
>[https://stats.nba.com/stats/drafthistory](https://stats.nba.com/stats/drafthistory)

##### Valid URL
>[https://stats.nba.com/stats/drafthistory?College=&LeagueID=00&OverallPick=&RoundNum=&RoundPick=&Season=&TeamID=&TopX=](https://stats.nba.com/stats/drafthistory?College=&LeagueID=00&OverallPick=&RoundNum=&RoundPick=&Season=&TeamID=&TopX=)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**LeagueID**_ | `^\d{2}$` | `Y` |  | 
_**TopX**_ |  |  | `Y` | 
_**TeamID**_ |  |  | `Y` | 
_**Season**_ | `^\d{4}$` |  | `Y` | 
_**RoundPick**_ |  |  | `Y` | 
_**RoundNum**_ |  |  | `Y` | 
_**OverallPick**_ |  |  | `Y` | 
_**College**_ |  |  | `Y` | 

## Data Sets
#### DraftHistory `draft_history`
```text
['PERSON_ID', 'PLAYER_NAME', 'SEASON', 'ROUND_NUMBER', 'ROUND_PICK', 'OVERALL_PICK', 'TEAM_ID', 'TEAM_CITY', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'ORGANIZATION', 'ORGANIZATION_TYPE']
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
            "TEAM_ID",
            "TEAM_CITY",
            "TEAM_NAME",
            "TEAM_ABBREVIATION",
            "ORGANIZATION",
            "ORGANIZATION_TYPE"
        ]
    },
    "endpoint": "DraftHistory",
    "last_validated_date": "2018-10-08",
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

Last validated 2018-10-08