# LeagueStandings
##### [nba_api/stats/endpoints/leaguestandings.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/leaguestandings.py)

##### Endpoint URL
>[https://stats.nba.com/stats/leaguestandings](https://stats.nba.com/stats/leaguestandings)

##### Valid URL
>[https://stats.nba.com/stats/leaguestandings?LeagueID=00&Season=2019-20&SeasonType=Regular+Season&SeasonYear=](https://stats.nba.com/stats/leaguestandings?LeagueID=00&Season=2019-20&SeasonType=Regular+Season&SeasonYear=)

## Parameters
| API Parameter Name                                                                                                  | Python Parameter Variable |              Pattern               | Required | Nullable |
|---------------------------------------------------------------------------------------------------------------------|---------------------------|:----------------------------------:|:--------:|:--------:|
| [_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID)     | league_id                 |             `^\d{2}$`              |   `Y`    |          | 
| [_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season)         | season                    |                                    |   `Y`    |          | 
| [_**SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonType) | season_type               | `^(Regular Season)\|(Pre Season)$` |   `Y`    |          | 
| [_**SeasonYear**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#SeasonYear) | season_nullable           |                                    |          |   `Y`    | 

## Data Sets
#### Standings `standings`
```text
['LeagueID', 'SeasonID', 'TeamID', 'TeamCity', 'TeamName', 'Conference', 'ConferenceRecord', 'PlayoffRank', 'ClinchIndicator', 'Division', 'DivisionRecord', 'DivisionRank', 'WINS', 'LOSSES', 'WinPCT', 'LeagueRank', 'Record', 'HOME', 'ROAD', 'L10', 'Last10Home', 'Last10Road', 'OT', 'ThreePTSOrLess', 'TenPTSOrMore', 'LongHomeStreak', 'strLongHomeStreak', 'LongRoadStreak', 'strLongRoadStreak', 'LongWinStreak', 'LongLossStreak', 'CurrentHomeStreak', 'strCurrentHomeStreak', 'CurrentRoadStreak', 'strCurrentRoadStreak', 'CurrentStreak', 'strCurrentStreak', 'ConferenceGamesBack', 'DivisionGamesBack', 'ClinchedConferenceTitle', 'ClinchedDivisionTitle', 'ClinchedPlayoffBirth', 'EliminatedConference', 'EliminatedDivision', 'AheadAtHalf', 'BehindAtHalf', 'TiedAtHalf', 'AheadAtThird', 'BehindAtThird', 'TiedAtThird', 'Score100PTS', 'OppScore100PTS', 'OppOver500', 'LeadInFGPCT', 'LeadInReb', 'FewerTurnovers', 'PointsPG', 'OppPointsPG', 'DiffPointsPG', 'vsEast', 'vsAtlantic', 'vsCentral', 'vsSoutheast', 'vsWest', 'vsNorthwest', 'vsPacific', 'vsSouthwest', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'PreAS', 'PostAS']
```


## JSON
```json
{
    "data_sets": {
        "Standings": [
            "LeagueID",
            "SeasonID",
            "TeamID",
            "TeamCity",
            "TeamName",
            "Conference",
            "ConferenceRecord",
            "PlayoffRank",
            "ClinchIndicator",
            "Division",
            "DivisionRecord",
            "DivisionRank",
            "WINS",
            "LOSSES",
            "WinPCT",
            "LeagueRank",
            "Record",
            "HOME",
            "ROAD",
            "L10",
            "Last10Home",
            "Last10Road",
            "OT",
            "ThreePTSOrLess",
            "TenPTSOrMore",
            "LongHomeStreak",
            "strLongHomeStreak",
            "LongRoadStreak",
            "strLongRoadStreak",
            "LongWinStreak",
            "LongLossStreak",
            "CurrentHomeStreak",
            "strCurrentHomeStreak",
            "CurrentRoadStreak",
            "strCurrentRoadStreak",
            "CurrentStreak",
            "strCurrentStreak",
            "ConferenceGamesBack",
            "DivisionGamesBack",
            "ClinchedConferenceTitle",
            "ClinchedDivisionTitle",
            "ClinchedPlayoffBirth",
            "EliminatedConference",
            "EliminatedDivision",
            "AheadAtHalf",
            "BehindAtHalf",
            "TiedAtHalf",
            "AheadAtThird",
            "BehindAtThird",
            "TiedAtThird",
            "Score100PTS",
            "OppScore100PTS",
            "OppOver500",
            "LeadInFGPCT",
            "LeadInReb",
            "FewerTurnovers",
            "PointsPG",
            "OppPointsPG",
            "DiffPointsPG",
            "vsEast",
            "vsAtlantic",
            "vsCentral",
            "vsSoutheast",
            "vsWest",
            "vsNorthwest",
            "vsPacific",
            "vsSouthwest",
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
            "PreAS",
            "PostAS"
        ]
    },
    "endpoint": "LeagueStandings",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [
        "SeasonYear"
    ],
    "parameter_patterns": {
        "LeagueID": "^\\d{2}$",
        "Season": null,
        "SeasonType": "^(Regular Season)|(Pre Season)$",
        "SeasonYear": null
    },
    "parameters": [
        "LeagueID",
        "Season",
        "SeasonType",
        "SeasonYear"
    ],
    "required_parameters": [
        "LeagueID",
        "Season",
        "SeasonType"
    ],
    "status": "success"
}
```

Last validated 2020-08-16