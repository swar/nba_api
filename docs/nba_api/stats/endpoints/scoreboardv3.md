# ScoreboardV2
##### [nba_api/stats/endpoints/scoreboardv3.py](https://github.com/swar/nba_api/blob/master/nba_api/stats/endpoints/scoreboardv3.py)

##### Endpoint URL
>[https://stats.nba.com/stats/scoreboardv3](https://stats.nba.com/stats/scoreboardv3)

##### Valid URL
>[https://stats.nba.com/stats/scoreboardv3?GameDate=2020-08-16&LeagueID=00](https://stats.nba.com/stats/scoreboardv3?GameDate=2020-08-16&LeagueID=00)

## Parameters
API Parameter Name | Python Parameter Variable | Pattern | Required | Nullable
------------ | ------------ | :-----------: | :---: | :---:
[_**GameDate**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameDate) | game_date |  | `Y` |  | 
[_**LeagueID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#LeagueID) | league_id | `^\d{2}$` | `Y` |  | 

## Properties
#### ScoreBoardDate `score_board_date`
```text
#returns a string
scoreboardv3.ScoreboardV3().score_board_date
```

#### Games `games`
```text
#returns all games as dictionary
scoreboardv3.ScoreboardV3().games.get_dict()

#returns all games as json
scoreboardv3.ScoreboardV3().games.get_json()
```

## JSON
```json
{
    "meta":{
        "version":1,
        "request":"http://nba.cloud/league/00/2022/10/14/scoreboard?Format=json",
        "time":"2022-10-15T00:32:46.3246Z"
    },
    "scoreboard":{
        "gameDate":"2022-10-14",
        "leagueId":"00",
        "leagueName":"National Basketball Association",
        "games":[
            {
                "gameId":"0012200062",
                "gameCode":"20221014/HOUIND",
                "gameStatus":3,
                "gameStatusText":"Final",
                "period":4,
                "gameClock":"",
                "gameTimeUTC":"2022-10-14T23:00:00Z",
                "gameEt":"2022-10-14T19:00:00Z",
                "regulationPeriods":4,
                "seriesGameNumber":"",
                "seriesText":"",
                "ifNecessary":false,
                "gameLeaders":{
                    "homeLeaders":{
                        "personId":1631097,
                        "name":"Bennedict Mathurin",
                        "playerSlug":"bennedict-mathurin",
                        "jerseyNum":"00",
                        "position":"G-F",
                        "teamTricode":"IND",
                        "points":18,
                        "rebounds":5,
                        "assists":3
                    },
                    "awayLeaders":{
                        "personId":1630224,
                        "name":"Jalen Green",
                        "playerSlug":"jalen-green",
                        "jerseyNum":"0",
                        "position":"G",
                        "teamTricode":"HOU",
                        "points":33,
                        "rebounds":1,
                        "assists":3
                    }
                },
                "teamLeaders":{
                    "homeLeaders":{
                        "personId":1631097,
                        "name":"Bennedict Mathurin",
                        "playerSlug":"bennedict-mathurin",
                        "jerseyNum":"00",
                        "position":"G-F",
                        "teamTricode":"IND",
                        "points":19.8,
                        "rebounds":3.8,
                        "assists":1.3
                    },
                    "awayLeaders":{
                        "personId":1630224,
                        "name":"Jalen Green",
                        "playerSlug":"jalen-green",
                        "jerseyNum":"0",
                        "position":"G",
                        "teamTricode":"HOU",
                        "points":22.0,
                        "rebounds":3.0,
                        "assists":3.3
                    },
                    "seasonLeadersFlag":0
                },
                "broadcasters":{
                    "nationalBroadcasters":[
                        
                    ],
                    "homeTvBroadcasters":[
                        {
                            "broadcasterId":1000341,
                            "broadcastDisplay":"BSIN"
                        }
                    ],
                    "homeRadioBroadcasters":[
                        
                    ],
                    "awayTvBroadcasters":[
                        {
                            "broadcasterId":1000208,
                            "broadcastDisplay":"Rockets.com"
                        }
                    ],
                    "awayRadioBroadcasters":[
                        {
                            "broadcasterId":1000704,
                            "broadcastDisplay":"KBME/KAMA-HD2"
                        }
                    ]
                },
                "homeTeam":{
                    "teamId":1610612754,
                    "teamName":"Pacers",
                    "teamCity":"Indiana",
                    "teamTricode":"IND",
                    "teamSlug":"pacers",
                    "wins":2,
                    "losses":2,
                    "score":114,
                    "seed":0,
                    "inBonus":null,
                    "timeoutsRemaining":0,
                    "periods":[
                        {
                            "period":1,
                            "periodType":"REGULAR",
                            "score":29
                        }
                    ]
                },
                "awayTeam":{
                    "teamId":1610612745,
                    "teamName":"Rockets",
                    "teamCity":"Houston",
                    "teamTricode":"HOU",
                    "teamSlug":"rockets",
                    "wins":3,
                    "losses":1,
                    "score":122,
                    "seed":0,
                    "inBonus":null,
                    "timeoutsRemaining":1,
                    "periods":[
                        {
                            "period":1,
                            "periodType":"REGULAR",
                            "score":39
                        }
                    ]
                }
            }
        ]
    }
}
```

Last validated 2022-10-15
