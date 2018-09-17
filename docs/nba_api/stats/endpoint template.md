# BoxScoreScoringV2

##### Endpoint URL
>[https://stats.nba.com/stats/boxscorescoringv2](https://stats.nba.com/stats/boxscorescoringv2)

##### Valid URL
>[https://stats.nba.com/stats/boxscorescoringv2?GameID=0021701218&StartPeriod=&EndPeriod=&StartRange=&EndRange=&RangeType=](https://stats.nba.com/stats/boxscorescoringv2?GameID=0021701218&StartPeriod=&EndPeriod=&StartRange=&EndRange=&RangeType=)

## Parameters
Parameter Name | Pattern | Required | Nullable
------------ | :-----------: | :---: | :---:
_**GameID**_ | `^\\d{10}$` | Y | 
_**StartPeriod**_ |  | Y | 
_**EndPeriod**_ |  | Y | 
_**StartRange**_ |  | Y | 
_**EndRange**_ |  | Y | 
_**RangeType**_ |  | Y | 

## Data Sets
#### LeagueDashPlayerBioStats `league_dash_player_bio_stats`
```text
"PLAYER_ID","PLAYER_NAME","TEAM_ID","TEAM_ABBREVIATION","AGE","PLAYER_HEIGHT","PLAYER_HEIGHT_INCHES","PLAYER_WEIGHT","COLLEGE","COUNTRY","DRAFT_YEAR","DRAFT_ROUND","DRAFT_NUMBER","GP","PTS","REB","AST","NET_RATING","OREB_PCT","DREB_PCT","USG_PCT","TS_PCT","AST_PCT"
```

## JSON
```json
{
    "BoxScoreScoringV2": {
        "status": "success",
        "endpoint": "BoxScoreScoringV2",
        "data_sets": [
            "sqlPlayersScoring",
            "sqlTeamsScoring"
        ],
        "parameters": [
            "GameID",
            "StartPeriod",
            "EndPeriod",
            "StartRange",
            "EndRange",
            "RangeType"
        ],
        "required_parameters": [
            "GameID",
            "StartPeriod",
            "EndPeriod",
            "StartRange",
            "EndRange",
            "RangeType"
        ],
        "nullable_parameters": [],
        "parameter_patterns": {
            "GameID": "^\\d{10}$",
            "StartPeriod": null,
            "EndPeriod": null,
            "StartRange": null,
            "EndRange": null,
            "RangeType": null
        }
    }
}
```