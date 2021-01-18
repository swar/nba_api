# PlayByPlay
##### [nba_api/live/nba/endpoints/playbyplay.py](https://github.com/swar/nba_api/blob/master/nba_api/live/nba/endpoints/playbyplay.py)

##### Endpoint URL
>>[https://cdn.nba.com/static/json/liveData/playbyplay/playbyplay_{game_id}.json](playbyplay/playbyplay_{game_id}.json)

##### Valid URL
>>[https://cdn.nba.com/static/json/liveData/playbyplay/playbyplay_0022000180.json](https://cdn.nba.com/static/json/liveData/playbyplay/playbyplay_0022000180.json)

## Parameters
API Parameter Name | Python Parameter Variable | Pattern | Required | Nullable
------------ | ------------ | :-----------: | :---: | :---:
[_**GameID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameID) | game_id | `^\d{10}$` | `Y` |  | 

## Data Sets
#### Actions `actions`
```text
['VIDEO_AVAILABLE_FLAG']
```

## JSON
```json
{
   "meta":{
      "version":1,
      "code":200,
      "request":"http://nba.cloud/games/0022000180/playbyplay?Format=json",
      "time":"2021-01-15 23:48:58.906160"
   },
   "game":{
      "gameId":"0022000180",
      "actions":[
         {
            "actionNumber":4,
            "clock":"PT11M58.00S",
            "timeActual":"2021-01-16T00:40:31.3Z",
            "period":1,
            "periodType":"REGULAR",
            "teamId":1610612738,
            "teamTricode":"BOS",
            "actionType":"jumpball",
            "subType":"recovered",
            "descriptor":"startperiod",
            "qualifiers":[
               
            ],
            "personId":1629684,
            "x":"None",
            "y":"None",
            "possession":1610612738,
            "scoreHome":"0",
            "scoreAway":"0",
            "edited":"2021-01-16T00:40:31Z",
            "orderNumber":40000,
            "xLegacy":"None",
            "yLegacy":"None",
            "isFieldGoal":0,
            "jumpBallRecoveredName":"G. Williams",
            "jumpBallRecoverdPersonId":1629684,
            "side":"None",
            "playerName":"Williams",
            "playerNameI":"G. Williams",
            "personIdsFilter":[
               1629684,
               202684,
               202696
            ],
            "jumpBallWonPlayerName":"Thompson",
            "jumpBallWonPersonId":202684,
            "description":"Jump Ball T. Thompson vs. N. Vucevic: Tip to G. Williams",
            "jumpBallLostPlayerName":"Vucevic",
            "jumpBallLostPersonId":202696
         }
      ]
   }
}
```

Last validated 2020-08-16