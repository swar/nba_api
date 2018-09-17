# TeamDetails

##### Endpoint URL
>[https://stats.nba.com/stats/teamdetails](https://stats.nba.com/stats/teamdetails)

##### Valid URL
>[https://stats.nba.com/stats/teamdetails?TeamID=1610612739](https://stats.nba.com/stats/teamdetails?TeamID=1610612739)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**TeamID**_ |  | `Y` |  | 

## Data Sets
#### TeamAwardsChampionships `team_awards_championships`
```text
['YEARAWARDED', 'OPPOSITETEAM']
```

#### TeamAwardsConf `team_awards_conf`
```text
['YEARAWARDED', 'OPPOSITETEAM']
```

#### TeamAwardsDiv `team_awards_div`
```text
['YEARAWARDED', 'OPPOSITETEAM']
```

#### TeamBackground `team_background`
```text
['TEAM_ID', 'ABBREVIATION', 'NICKNAME', 'YEARFOUNDED', 'CITY', 'ARENA', 'ARENACAPACITY', 'OWNER', 'GENERALMANAGER', 'HEADCOACH', 'DLEAGUEAFFILIATION']
```

#### TeamHistory `team_history`
```text
['TEAM_ID', 'CITY', 'NICKNAME', 'YEARFOUNDED', 'YEARACTIVETILL']
```

#### TeamHof `team_hof`
```text
['PLAYERID', 'PLAYER', 'POSITION', 'JERSEY', 'SEASONSWITHTEAM', 'YEAR']
```

#### TeamRetired `team_retired`
```text
['PLAYERID', 'PLAYER', 'POSITION', 'JERSEY', 'SEASONSWITHTEAM', 'YEAR']
```

#### TeamSocialSites `team_social_sites`
```text
['ACCOUNTTYPE', 'WEBSITE_LINK']
```


## JSON
```json
{
    "data_sets": {
        "TeamAwardsChampionships": [
            "YEARAWARDED",
            "OPPOSITETEAM"
        ],
        "TeamAwardsConf": [
            "YEARAWARDED",
            "OPPOSITETEAM"
        ],
        "TeamAwardsDiv": [
            "YEARAWARDED",
            "OPPOSITETEAM"
        ],
        "TeamBackground": [
            "TEAM_ID",
            "ABBREVIATION",
            "NICKNAME",
            "YEARFOUNDED",
            "CITY",
            "ARENA",
            "ARENACAPACITY",
            "OWNER",
            "GENERALMANAGER",
            "HEADCOACH",
            "DLEAGUEAFFILIATION"
        ],
        "TeamHistory": [
            "TEAM_ID",
            "CITY",
            "NICKNAME",
            "YEARFOUNDED",
            "YEARACTIVETILL"
        ],
        "TeamHof": [
            "PLAYERID",
            "PLAYER",
            "POSITION",
            "JERSEY",
            "SEASONSWITHTEAM",
            "YEAR"
        ],
        "TeamRetired": [
            "PLAYERID",
            "PLAYER",
            "POSITION",
            "JERSEY",
            "SEASONSWITHTEAM",
            "YEAR"
        ],
        "TeamSocialSites": [
            "ACCOUNTTYPE",
            "WEBSITE_LINK"
        ]
    },
    "endpoint": "TeamDetails",
    "nullable_parameters": [],
    "parameter_patterns": {
        "TeamID": null
    },
    "parameters": [
        "TeamID"
    ],
    "required_parameters": [
        "TeamID"
    ],
    "status": "success"
}
```

Last validated 2018-09-16