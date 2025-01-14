# ScheduleLeagueV2
##### [nba_api/stats/endpoints/scheduleleaguev2.py](https://github.com/swar/nba_api/blob/master/nba_api/stats/endpoints/scheduleleaguev2.py)

##### Endpoint URL
>[https://stats.nba.com/stats/scheduleleaguev2](https://stats.nba.com/stats/scheduleleaguev2)

##### Valid URL
>[https://stats.nba.com/stats/scheduleleaguev2?LeagueID=00&Season=2024-25](https://stats.nba.com/stats/scheduleleaguev2?LeagueID=00&Season=2024-25)

## Parameters
API Parameter Name | Python Parameter Variable | Pattern | Required | Nullable
------------ | ------------ | :-----------: | :---: | :---:
[_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id |  |  |  | 
[_**Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Season) | season |  |  |  | 

## Data Sets
#### SeasonGames `season_games`
```text
['leagueId', 'seasonYear', 'gameDate', 'gameId', 'gameCode', 'gameStatus', 'gameStatusText', 'gameSequence', 'gameDateEst', 'gameTimeEst', 'gameDateTimeEst', 'gameDateUTC', 'gameTimeUTC', 'gameDateTimeUTC', 'awayTeamTime', 'homeTeamTime', 'day', 'monthNum', 'weekNumber', 'weekName', 'ifNecessary', 'seriesGameNumber', 'gameLabel', 'gameSubLabel', 'seriesText', 'arenaName', 'arenaState', 'arenaCity', 'postponedStatus', 'branchLink', 'gameSubtype', 'isNeutral', 'homeTeam_teamId', 'homeTeam_teamName', 'homeTeam_teamCity', 'homeTeam_teamTricode', 'homeTeam_teamSlug', 'homeTeam_wins', 'homeTeam_losses', 'homeTeam_score', 'homeTeam_seed', 'awayTeam_teamId', 'awayTeam_teamName', 'awayTeam_teamCity', 'awayTeam_teamTricode', 'awayTeam_teamSlug', 'awayTeam_wins', 'awayTeam_losses', 'awayTeam_score', 'awayTeam_seed', 'pointsLeaders_personId', 'pointsLeaders_firstName', 'pointsLeaders_lastName', 'pointsLeaders_teamId', 'pointsLeaders_teamCity', 'pointsLeaders_teamName', 'pointsLeaders_teamTricode', 'pointsLeaders_points', 'nationalBroadcasters_broadcasterScope', 'nationalBroadcasters_broadcasterMedia', 'nationalBroadcasters_broadcasterId', 'nationalBroadcasters_broadcasterDisplay', 'nationalBroadcasters_broadcasterAbbreviation', 'nationalBroadcasters_tapeDelayComments', 'nationalBroadcasters_broadcasterVideoLink', 'nationalBroadcasters_broadcasterDescription', 'nationalBroadcasters_broadcasterTeamId', 'nationalRadioBroadcasters_broadcasterScope', 'nationalRadioBroadcasters_broadcasterMedia', 'nationalRadioBroadcasters_broadcasterId', 'nationalRadioBroadcasters_broadcasterDisplay', 'nationalRadioBroadcasters_broadcasterAbbreviation', 'nationalRadioBroadcasters_tapeDelayComments', 'nationalRadioBroadcasters_broadcasterVideoLink', 'nationalRadioBroadcasters_broadcasterDescription', 'nationalRadioBroadcasters_broadcasterTeamId', 'nationalOttBroadcasters_broadcasterScope', 'nationalOttBroadcasters_broadcasterMedia', 'nationalOttBroadcasters_broadcasterId', 'nationalOttBroadcasters_broadcasterDisplay', 'nationalOttBroadcasters_broadcasterAbbreviation', 'nationalOttBroadcasters_tapeDelayComments', 'nationalOttBroadcasters_broadcasterVideoLink', 'nationalOttBroadcasters_broadcasterDescription', 'nationalOttBroadcasters_broadcasterTeamId', 'homeTvBroadcasters_broadcasterScope', 'homeTvBroadcasters_broadcasterMedia', 'homeTvBroadcasters_broadcasterId', 'homeTvBroadcasters_broadcasterDisplay', 'homeTvBroadcasters_broadcasterAbbreviation', 'homeTvBroadcasters_tapeDelayComments', 'homeTvBroadcasters_broadcasterVideoLink', 'homeTvBroadcasters_broadcasterDescription', 'homeTvBroadcasters_broadcasterTeamId', 'homeRadioBroadcasters_broadcasterScope', 'homeRadioBroadcasters_broadcasterMedia', 'homeRadioBroadcasters_broadcasterId', 'homeRadioBroadcasters_broadcasterDisplay', 'homeRadioBroadcasters_broadcasterAbbreviation', 'homeRadioBroadcasters_tapeDelayComments', 'homeRadioBroadcasters_broadcasterVideoLink', 'homeRadioBroadcasters_broadcasterDescription', 'homeRadioBroadcasters_broadcasterTeamId', 'homeOttBroadcasters_broadcasterScope', 'homeOttBroadcasters_broadcasterMedia', 'homeOttBroadcasters_broadcasterId', 'homeOttBroadcasters_broadcasterDisplay', 'homeOttBroadcasters_broadcasterAbbreviation', 'homeOttBroadcasters_tapeDelayComments', 'homeOttBroadcasters_broadcasterVideoLink', 'homeOttBroadcasters_broadcasterDescription', 'homeOttBroadcasters_broadcasterTeamId', 'awayTvBroadcasters_broadcasterScope', 'awayTvBroadcasters_broadcasterMedia', 'awayTvBroadcasters_broadcasterId', 'awayTvBroadcasters_broadcasterDisplay', 'awayTvBroadcasters_broadcasterAbbreviation', 'awayTvBroadcasters_tapeDelayComments', 'awayTvBroadcasters_broadcasterVideoLink', 'awayTvBroadcasters_broadcasterDescription', 'awayTvBroadcasters_broadcasterTeamId', 'awayRadioBroadcasters_broadcasterScope', 'awayRadioBroadcasters_broadcasterMedia', 'awayRadioBroadcasters_broadcasterId', 'awayRadioBroadcasters_broadcasterDisplay', 'awayRadioBroadcasters_broadcasterAbbreviation', 'awayRadioBroadcasters_tapeDelayComments', 'awayRadioBroadcasters_broadcasterVideoLink', 'awayRadioBroadcasters_broadcasterDescription', 'awayRadioBroadcasters_broadcasterTeamId', 'awayOttBroadcasters_broadcasterScope', 'awayOttBroadcasters_broadcasterMedia', 'awayOttBroadcasters_broadcasterId', 'awayOttBroadcasters_broadcasterDisplay', 'awayOttBroadcasters_broadcasterAbbreviation', 'awayOttBroadcasters_tapeDelayComments', 'awayOttBroadcasters_broadcasterVideoLink', 'awayOttBroadcasters_broadcasterDescription', 'awayOttBroadcasters_broadcasterTeamId']
```

#### SeasonWeeks `season_weeks`
```text
['leagueId', 'seasonYear', 'weekNumber', 'weekName', 'startDate', 'endDate']
```


## JSON
```json
{
    "data_sets": {
        "SeasonGames": [
            "leagueId",
            "seasonYear",
            "gameDate",
            "gameId",
            "gameCode",
            "gameStatus",
            "gameStatusText",
            "gameSequence",
            "gameDateEst",
            "gameTimeEst",
            "gameDateTimeEst",
            "gameDateUTC",
            "gameTimeUTC",
            "gameDateTimeUTC",
            "awayTeamTime",
            "homeTeamTime",
            "day",
            "monthNum",
            "weekNumber",
            "weekName",
            "ifNecessary",
            "seriesGameNumber",
            "gameLabel",
            "gameSubLabel",
            "seriesText",
            "arenaName",
            "arenaState",
            "arenaCity",
            "postponedStatus",
            "branchLink",
            "gameSubtype",
            "isNeutral",
            "homeTeam_teamId",
            "homeTeam_teamName",
            "homeTeam_teamCity",
            "homeTeam_teamTricode",
            "homeTeam_teamSlug",
            "homeTeam_wins",
            "homeTeam_losses",
            "homeTeam_score",
            "homeTeam_seed",
            "awayTeam_teamId",
            "awayTeam_teamName",
            "awayTeam_teamCity",
            "awayTeam_teamTricode",
            "awayTeam_teamSlug",
            "awayTeam_wins",
            "awayTeam_losses",
            "awayTeam_score",
            "awayTeam_seed",
            "pointsLeaders_personId",
            "pointsLeaders_firstName",
            "pointsLeaders_lastName",
            "pointsLeaders_teamId",
            "pointsLeaders_teamCity",
            "pointsLeaders_teamName",
            "pointsLeaders_teamTricode",
            "pointsLeaders_points",
            "nationalBroadcasters_broadcasterScope",
            "nationalBroadcasters_broadcasterMedia",
            "nationalBroadcasters_broadcasterId",
            "nationalBroadcasters_broadcasterDisplay",
            "nationalBroadcasters_broadcasterAbbreviation",
            "nationalBroadcasters_tapeDelayComments",
            "nationalBroadcasters_broadcasterVideoLink",
            "nationalBroadcasters_broadcasterDescription",
            "nationalBroadcasters_broadcasterTeamId",
            "nationalRadioBroadcasters_broadcasterScope",
            "nationalRadioBroadcasters_broadcasterMedia",
            "nationalRadioBroadcasters_broadcasterId",
            "nationalRadioBroadcasters_broadcasterDisplay",
            "nationalRadioBroadcasters_broadcasterAbbreviation",
            "nationalRadioBroadcasters_tapeDelayComments",
            "nationalRadioBroadcasters_broadcasterVideoLink",
            "nationalRadioBroadcasters_broadcasterDescription",
            "nationalRadioBroadcasters_broadcasterTeamId",
            "nationalOttBroadcasters_broadcasterScope",
            "nationalOttBroadcasters_broadcasterMedia",
            "nationalOttBroadcasters_broadcasterId",
            "nationalOttBroadcasters_broadcasterDisplay",
            "nationalOttBroadcasters_broadcasterAbbreviation",
            "nationalOttBroadcasters_tapeDelayComments",
            "nationalOttBroadcasters_broadcasterVideoLink",
            "nationalOttBroadcasters_broadcasterDescription",
            "nationalOttBroadcasters_broadcasterTeamId",
            "homeTvBroadcasters_broadcasterScope",
            "homeTvBroadcasters_broadcasterMedia",
            "homeTvBroadcasters_broadcasterId",
            "homeTvBroadcasters_broadcasterDisplay",
            "homeTvBroadcasters_broadcasterAbbreviation",
            "homeTvBroadcasters_tapeDelayComments",
            "homeTvBroadcasters_broadcasterVideoLink",
            "homeTvBroadcasters_broadcasterDescription",
            "homeTvBroadcasters_broadcasterTeamId",
            "homeRadioBroadcasters_broadcasterScope",
            "homeRadioBroadcasters_broadcasterMedia",
            "homeRadioBroadcasters_broadcasterId",
            "homeRadioBroadcasters_broadcasterDisplay",
            "homeRadioBroadcasters_broadcasterAbbreviation",
            "homeRadioBroadcasters_tapeDelayComments",
            "homeRadioBroadcasters_broadcasterVideoLink",
            "homeRadioBroadcasters_broadcasterDescription",
            "homeRadioBroadcasters_broadcasterTeamId",
            "homeOttBroadcasters_broadcasterScope",
            "homeOttBroadcasters_broadcasterMedia",
            "homeOttBroadcasters_broadcasterId",
            "homeOttBroadcasters_broadcasterDisplay",
            "homeOttBroadcasters_broadcasterAbbreviation",
            "homeOttBroadcasters_tapeDelayComments",
            "homeOttBroadcasters_broadcasterVideoLink",
            "homeOttBroadcasters_broadcasterDescription",
            "homeOttBroadcasters_broadcasterTeamId",
            "awayTvBroadcasters_broadcasterScope",
            "awayTvBroadcasters_broadcasterMedia",
            "awayTvBroadcasters_broadcasterId",
            "awayTvBroadcasters_broadcasterDisplay",
            "awayTvBroadcasters_broadcasterAbbreviation",
            "awayTvBroadcasters_tapeDelayComments",
            "awayTvBroadcasters_broadcasterVideoLink",
            "awayTvBroadcasters_broadcasterDescription",
            "awayTvBroadcasters_broadcasterTeamId",
            "awayRadioBroadcasters_broadcasterScope",
            "awayRadioBroadcasters_broadcasterMedia",
            "awayRadioBroadcasters_broadcasterId",
            "awayRadioBroadcasters_broadcasterDisplay",
            "awayRadioBroadcasters_broadcasterAbbreviation",
            "awayRadioBroadcasters_tapeDelayComments",
            "awayRadioBroadcasters_broadcasterVideoLink",
            "awayRadioBroadcasters_broadcasterDescription",
            "awayRadioBroadcasters_broadcasterTeamId",
            "awayOttBroadcasters_broadcasterScope",
            "awayOttBroadcasters_broadcasterMedia",
            "awayOttBroadcasters_broadcasterId",
            "awayOttBroadcasters_broadcasterDisplay",
            "awayOttBroadcasters_broadcasterAbbreviation",
            "awayOttBroadcasters_tapeDelayComments",
            "awayOttBroadcasters_broadcasterVideoLink",
            "awayOttBroadcasters_broadcasterDescription",
            "awayOttBroadcasters_broadcasterTeamId"
        ],
        "SeasonWeeks": [
            "leagueId",
            "seasonYear",
            "weekNumber",
            "weekName",
            "startDate",
            "endDate"
        ]
    },
    "nullable_parameters": [],
    "parameter_patterns": {
        "LeagueID": null,
        "Season": null
    },
    "parameters": [
        "LeagueID",
        "Season"
    ],
    "required_parameters": [],
    "status": "success"
}
```

Last validated 2025-01-14