# LeagueStandingsV3
##### [nba_api/stats/endpoints/leaguestandingsv3.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/leaguestandingsv3.py)

##### Endpoint URL
>[https://stats.nba.com/stats/leaguestandingsv3](https://stats.nba.com/stats/leaguestandingsv3)

##### Valid URL
>[https://stats.nba.com/stats/leaguestandingsv3?LeagueID=00&Season=2019-20&SeasonType=Regular+Season&SeasonYear=](https://stats.nba.com/stats/leaguestandingsv3?LeagueID=00&Season=2019-20&SeasonType=Regular+Season&SeasonYear=)

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
['LeagueID', 'SeasonID', 'TeamID', 'TeamCity', 'TeamName', 'TeamSlug', 'Conference', 'ConferenceRecord', 'PlayoffRank', 'ClinchIndicator', 'Division', 'DivisionRecord', 'DivisionRank', 'WINS', 'LOSSES', 'WinPCT', 'LeagueRank', 'Record', 'HOME', 'ROAD', 'L10', 'Last10Home', 'Last10Road', 'OT', 'ThreePTSOrLess', 'TenPTSOrMore', 'LongHomeStreak', 'strLongHomeStreak', 'LongRoadStreak', 'strLongRoadStreak', 'LongWinStreak', 'LongLossStreak', 'CurrentHomeStreak', 'strCurrentHomeStreak', 'CurrentRoadStreak', 'strCurrentRoadStreak', 'CurrentStreak', 'strCurrentStreak', 'ConferenceGamesBack', 'DivisionGamesBack', 'ClinchedConferenceTitle', 'ClinchedDivisionTitle', 'ClinchedPlayoffBirth', 'EliminatedConference', 'EliminatedDivision', 'AheadAtHalf', 'BehindAtHalf', 'TiedAtHalf', 'AheadAtThird', 'BehindAtThird', 'TiedAtThird', 'Score100PTS', 'OppScore100PTS', 'OppOver500', 'LeadInFGPCT', 'LeadInReb', 'FewerTurnovers', 'PointsPG', 'OppPointsPG', 'DiffPointsPG', 'vsEast', 'vsAtlantic', 'vsCentral', 'vsSoutheast', 'vsWest', 'vsNorthwest', 'vsPacific', 'vsSouthwest', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'ReturnToPlay_East_PI_Flag', 'ReturnToPlay_West_PI_Flag', 'ReturnToPlay_Already_Eliminated', 'Seeding_Game_1_Outcome', 'Seeding_Game_2_Outcome', 'Seeding_Game_3_Outcome', 'Seeding_Game_4_Outcome', 'Seeding_Game_5_Outcome', 'Seeding_Game_6_Outcome', 'Seeding_Game_7_Outcome', 'Seeding_Game_8_Outcome', 'Seeding_Game_1_ID', 'Seeding_Game_2_ID', 'Seeding_Game_3_ID', 'Seeding_Game_4_ID', 'Seeding_Game_5_ID', 'Seeding_Game_6_ID', 'Seeding_Game_7_ID', 'Seeding_Game_8_ID', 'Seeding_Game_1_Opponent', 'Seeding_Game_2_Opponent', 'Seeding_Game_3_Opponent', 'Seeding_Game_4_Opponent', 'Seeding_Game_5_Opponent', 'Seeding_Game_6_Opponent', 'Seeding_Game_7_Opponent', 'Seeding_Game_8_Opponent', 'Seeding_Game_1_Label', 'Seeding_Game_2_Label', 'Seeding_Game_3_Label', 'Seeding_Game_4_Label', 'Seeding_Game_5_Label', 'Seeding_Game_6_Label', 'Seeding_Game_7_Label', 'Seeding_Game_8_Label']
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
            "TeamSlug",
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
            "ReturnToPlay_East_PI_Flag",
            "ReturnToPlay_West_PI_Flag",
            "ReturnToPlay_Already_Eliminated",
            "Seeding_Game_1_Outcome",
            "Seeding_Game_2_Outcome",
            "Seeding_Game_3_Outcome",
            "Seeding_Game_4_Outcome",
            "Seeding_Game_5_Outcome",
            "Seeding_Game_6_Outcome",
            "Seeding_Game_7_Outcome",
            "Seeding_Game_8_Outcome",
            "Seeding_Game_1_ID",
            "Seeding_Game_2_ID",
            "Seeding_Game_3_ID",
            "Seeding_Game_4_ID",
            "Seeding_Game_5_ID",
            "Seeding_Game_6_ID",
            "Seeding_Game_7_ID",
            "Seeding_Game_8_ID",
            "Seeding_Game_1_Opponent",
            "Seeding_Game_2_Opponent",
            "Seeding_Game_3_Opponent",
            "Seeding_Game_4_Opponent",
            "Seeding_Game_5_Opponent",
            "Seeding_Game_6_Opponent",
            "Seeding_Game_7_Opponent",
            "Seeding_Game_8_Opponent",
            "Seeding_Game_1_Label",
            "Seeding_Game_2_Label",
            "Seeding_Game_3_Label",
            "Seeding_Game_4_Label",
            "Seeding_Game_5_Label",
            "Seeding_Game_6_Label",
            "Seeding_Game_7_Label",
            "Seeding_Game_8_Label"
        ]
    },
    "endpoint": "LeagueStandingsV3",
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