# ScoreBoard
##### [nba_api/live/nba/endpoints/scoreboard.py](https://github.com/swar/nba_api/blob/master/nba_api/live/nba/endpoints/scoreboard.py)

##### Endpoint URL
>[https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json](https://cdn.nba.com/static/json/liveData/scoreboard/todaysScoreboard_00.json)

## Parameters
`None`

## Properties
#### GameDate `score_board_date`
```text
#returns a string
scoreboard.ScoreBoard().score_board_date
```

#### Games `games`
```text
#returns all games as dictionary
scoreboard.ScoreBoard().games.get_dict()

#returns all games as json
scoreboard.ScoreBoard().games.get_json()
```


## JSON
```json
{
   "meta":{
      "version":1,
      "request":"https://nba-prod-us-east-1-mediaops-stats.s3.amazonaws.com/NBA/liveData/scoreboard/todaysScoreboard_00.json",
      "time":"2021-01-16 11:11:39.1139",
      "code":200
   },
   "scoreboard":{
      "gameDate":"2021-01-15",
      "leagueId":"00",
      "leagueName":"National Basketball Association",
      "games":[
         {
            "gameId":"0022000181",
            "gameCode":"20210115/NYKCLE",
            "gameStatus":3,
            "gameStatusText":"Final",
            "period":4,
            "gameClock":"",
            "gameTimeUTC":"2021-01-16T00:30:00Z",
            "gameEt":"2021-01-15T19:30:00Z",
            "regulationPeriods":4,
            "seriesGameNumber":"",
            "seriesText":"",
            "homeTeam":{
               "teamId":1610612739,
               "teamName":"Cavaliers",
               "teamCity":"Cleveland",
               "teamTricode":"CLE",
               "wins":6,
               "losses":7,
               "score":106,
               "inBonus":"None",
               "timeoutsRemaining":1,
               "periods":[
                  {
                     "period":1,
                     "periodType":"REGULAR",
                     "score":28
                  }
               ]
            },
            "awayTeam":{
               "teamId":1610612752,
               "teamName":"Knicks",
               "teamCity":"New York",
               "teamTricode":"NYK",
               "wins":5,
               "losses":8,
               "score":103,
               "inBonus":"None",
               "timeoutsRemaining":0,
               "periods":[
                  {
                     "period":1,
                     "periodType":"REGULAR",
                     "score":25
                  }
               ]
            },
            "gameLeaders":{
               "homeLeaders":{
                  "personId":203083,
                  "name":"Andre Drummond",
                  "jerseyNum":"3",
                  "position":"C",
                  "teamTricode":"CLE",
                  "playerSlug":"None",
                  "points":33,
                  "rebounds":23,
                  "assists":3
               },
               "awayLeaders":{
                  "personId":203944,
                  "name":"Julius Randle",
                  "jerseyNum":"30",
                  "position":"F-C",
                  "teamTricode":"NYK",
                  "playerSlug":"None",
                  "points":28,
                  "rebounds":6,
                  "assists":6
               }
            },
            "pbOdds":{
               "team":"None",
               "odds":0.0,
               "suspended":1
            }
         }
      ]
   }
}
```

Last validated 2020-08-16