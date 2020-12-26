# PlayByPlay
##### [nba_api/stats/endpoints/playbyplay.py](https://github.com/swar/nba_api/blob/master/nba_api/stats/endpoints/playbyplay.py)

##### Endpoint URL
>[https://stats.nba.com/stats/playbyplay](https://stats.nba.com/stats/playbyplay)

##### Valid URL
>[https://stats.nba.com/stats/playbyplay?EndPeriod=1&GameID=0021700807&StartPeriod=1](https://stats.nba.com/stats/playbyplay?EndPeriod=1&GameID=0021700807&StartPeriod=1)

## Parameters
API Parameter Name | Python Parameter Variable | Pattern | Required | Nullable
------------ | ------------ | :-----------: | :---: | :---:
[_**EndPeriod**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#EndPeriod) | end_period |  | `Y` |  | 
[_**GameID**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#GameID) | game_id | `^\d{10}$` | `Y` |  | 
[_**StartPeriod**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#StartPeriod) | start_period |  | `Y` |  | 

## Data Sets
#### AvailableVideo `available_video`
```text
['VIDEO_AVAILABLE_FLAG']
```

#### PlayByPlay `play_by_play`
```text
['GAME_ID', 'EVENTNUM', 'EVENTMSGTYPE', 'EVENTMSGACTIONTYPE', 'PERIOD', 'WCTIMESTRING', 'PCTIMESTRING', 'HOMEDESCRIPTION', 'NEUTRALDESCRIPTION', 'VISITORDESCRIPTION', 'SCORE', 'SCOREMARGIN']
```


## JSON
```json
{
    "meta": {
        "version": 1,
        "code":200,
        "request":"http://nba.cloud/games/0022000011/playbyplay?Format=json",
        "time":"2020-12-23 23:28:42.239540"
    },
    "game":{
        "gameId":"0022000011",
        "actions":[{
            "actionNumber":2,
            "clock":"PT12M00.00S",
            "timeActual":"2020-12-24T00:13:22.7Z",
            "period":1,
            "periodType":"REGULAR",
            "actionType":"period",
            "subType":"start",
            "qualifiers":[],
            "personId":0,
            "x":"None",
            "y":"None",
            "possession":0,
            "scoreHome":"0",
            "scoreAway":"0",
            "edited":"2020-12-24T00:13:22Z",
            "orderNumber":20000,
            "xLegacy":"None",
            "yLegacy":"None",
            "isFieldGoal":0,
            "side":"None",
            "description":"Period Start",
            "personIdsFilter":[]
         }]}}
```

Last validated 2020-08-16