# ISTStandings
##### [nba_api/stats/endpoints/iststandings.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/idststandings.py)

##### Endpoint URL
>[https://stats.nba.com/stats/iststandings](https://stats.nba.com/stats/iststandings)

##### Valid URL
>[https://stats.nba.com/stats/iststandings?LeagueID=00&Season=2023-24&Section=group](https://stats.nba.com/stats/iststandings?LeagueID=00&Season=2023-24&Section=group)

## Parameters
| API Parameter Name                                                                                              | Python Parameter Variable |         Pattern         |  Required   | Nullable |
|-----------------------------------------------------------------------------------------------------------------|---------------------------|:-----------------------:|:-----------:|:--------:|
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id                 |        `^\d{2}$`        |     `Y`     |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)     | season                    |                         |     `Y`     |          |
| [_**Section**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Section)   | section                   | `^(group)\|(wildcard)$` |     `Y`     |          |

## Data Sets
#### Standings `standings`
```text
["leagueId", "seasonYear", "teamId", "teamCity", "teamName", "teamAbbreviation", "teamSlug", "conference", "istGroup", "clinchIndicator", "clinchedIstKnockout", "clinchedIstGroup", "clinchedIstWildcard", "istWildcardRank", "istGroupRank", "istKnockoutRank", "wins", "losses", "pct", "istGroupGb", "istWildcardGb", "diff", "pts", "oppPts", "gameId1", "opponentTeamAbbreviation1", "location1", "gameStatus1", "gameStatusText1", "outcome1", "gameId2", "opponentTeamAbbreviation2", "location2", "gameStatus2", "gameStatusText2", "outcome2", "gameId3", "opponentTeamAbbreviation3", "location3", "gameStatus3", "gameStatusText3", "outcome3", "gameId4", "opponentTeamAbbreviation4", "location4", "gameStatus4", "gameStatusText4", "outcome4"]
```


## JSON
```json
{
    "data_sets": {
        "Standings": [
            "leagueId",
            "seasonYear",
            "teamId",
            "teamCity",
            "teamName",
            "teamAbbreviation",
            "teamSlug",
            "conference",
            "istGroup",
            "clinchIndicator",
            "clinchedIstKnockout",
            "clinchedIstGroup",
            "clinchedIstWildcard",
            "istWildcardRank",
            "istGroupRank",
            "istKnockoutRank",
            "wins",
            "losses",
            "pct",
            "istGroupGb",
            "istWildcardGb",
            "diff",
            "pts",
            "oppPts",
            "gameId1",
            "opponentTeamAbbreviation1",
            "location1",
            "gameStatus1",
            "gameStatusText1",
            "outcome1",
            "gameId2",
            "opponentTeamAbbreviation2",
            "location2",
            "gameStatus2",
            "gameStatusText2",
            "outcome2",
            "gameId3",
            "opponentTeamAbbreviation3",
            "location3",
            "gameStatus3",
            "gameStatusText3",
            "outcome3",
            "gameId4",
            "opponentTeamAbbreviation4",
            "location4",
            "gameStatus4",
            "gameStatusText4",
            "outcome4"
        ]
    },
    "endpoint": "ISTStandings",
    "last_validated_date": "2023-11-08",
    "nullable_parameters": [
    ],
    "parameter_patterns": {
        "LeagueID": "^\\d{2}$",
        "Season": "^\\d{4}-\\d{2}$",
        "Section": "^(group)|(wildcard)$"
    },
    "parameters": [
        "LeagueID",
        "Season",
        "Section"
    ],
    "required_parameters": [
        "LeagueID",
        "Season",
        "Section"
    ],
    "status": "success"
}
```

Last validated 2023-11-08