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
["actionNumber", "actionType", "assistPersonId", "assistPlayerNameInitial", "assistTotal", "blockPersonId", "blockPlayerName", "clock", "description", "descriptor", "edited", "foulDrawnPersonId", "foulDrawnPlayerName", "foulPersonalTotal", "foulTechnicalTotal", "isFieldGoal", "jumpBallLostPersonId", "jumpBallLostPlayerName", "jumpBallRecoverdPersonId", "jumpBallRecoveredName", "jumpBallWonPersonId", "jumpBallWonPlayerName", "officialId", "orderNumber", "period", "periodType", "personId", "personIdsFilter"[], "playerName", "playerNameI", "pointsTotal", "possession", "qualifiers"[], "reboundDefensiveTotal", "reboundOffensiveTotal", "reboundTotal", "scoreAway", "scoreHome", "shotActionNumber", "shotDistance", "shotResult", "side", "stealPersonId", "stealPlayerName", "subType", "teamId", "teamTricode", "timeActual", "turnoverTotal", "value", "x", "xLegacy", "y", "yLegacy"]
```
## About `Actions` Data Set
This is intended to be a comprehensive list of all possible `actions` available. Note that not all keys appear on every `action` as it depends on the `actionType`
Key | Class | Sample | Description | AlwaysPresent |
------------ | ------------ | :-----------: | :------------------: | :---------:
`actionNumber`|`<class 'int'>`| `4` | `actionNumber is guaranteed to be sequential but not consectutive ([2, 5, 6, 7, 9, 10])` | `Yes` |
`actionType`|`<class 'str'>`| `"period"` | `-` | `Yes` |
`assistPersonId`|`<class 'int'>`| `1627759` | `-` | `No` |
`assistPlayerNameInitial`|`<class 'str'>`| `J. Brown` | `-` | `No` |
`assistTotal`|`<class 'int'>`| `3` | `-` | `No` |
`blockPersonId`|`<class 'int'>`| `1627759` | `-` | `No` |
`blockPlayerName`|`<class 'str'>`| `J. Brown` | `-` | `No` |
`clock`|`<class 'str'>`| `PT03M59.00S` | `clock is the Period Time in which the play occurred` | `Yes` |
`description`|`<class 'str'>`| `J. Brown 14' pullup Jump Shot (2 PTS)` | `description of the action` | `No` |
`descriptor`|`<class 'str'>`| `pullup` | `a key phrase with regards to the play. Examples: ("heldball","technical","pullup","bad pass","driving finger roll"` )  | `No` |
`edited`|`<class 'str'>`| `2021-01-16T02:01:02Z` | `The time in which the play was edited` | `No` |
`foulDrawnPersonId`|`<class 'int'>`| `1627759` | `-` | `No` |
`foulDrawnPlayerName`|`<class 'str'>`| `Brown` | `-` | `No` |
`foulPersonalTotal`|`<class 'int'>`| `1` | `-` | `No` |
`foulTechnicalTotal`|`<class 'int'>`| `0` | `-` | `No` |
`isFieldGoal`|`<class 'int'>`| `0` | `0 | 1` | `Yes` |
`jumpBallLostPersonId`|`<class 'int'>`| `203935` | `-` | `No` |
`jumpBallLostPlayerName`|`<class 'str'>`| `Smart` | `-` | `No` |
`jumpBallRecoverdPersonId`|`<class 'int'>`| `203932` | `-` | `No` |
`jumpBallRecoveredName`|`<class 'str'>`| `A. Gordon` | `-` | `No` |
`jumpBallWonPersonId`|`<class 'int'>`| `203920` | `-` | `No` |
`jumpBallWonPlayerName`|`<class 'str'>`| `Birch` | `-` | `No` |
`officialId`|`<class 'int'>`| `-` | `-` | `No` |
`orderNumber`|`<class 'int'>`| `4560000` | `unknown consecutive number` | `Yes` |
`period`|`<class 'int'>`| `3` | `-` | `Yes` |
`periodType`|`<class 'str'>`| `-` | `-` | `Yes` |
`personId`|`<class 'int'>`| `1629109` | `-` | `Yes` |
`personIdsFilter`|`<class 'list'>`| `[203932, 203920, 203935]` | `players involved in the play. In this case ti was a jump ball (recovered, won, lost)` | `Yes` |
`playerName`|`<class 'str'>`| `Clark` | `-` | `No` |
`playerNameI`|`<class 'str'>`| `G. Clark` | `-` | `No` |
`pointsTotal`|`<class 'int'>`| `6` | `-` | `No` |
`possession`|`<class 'int'>`| `1610612753` | `The teamId who has possession` | `Yes` |
`qualifiers`|`<class 'list'>`| `["pointsinthepaint"]` | `-` | `yes` |
`reboundDefensiveTotal`|`<class 'int'>`| `6` | `-` | `No` |
`reboundOffensiveTotal`|`<class 'int'>`| `2` | `-` | `No` |
`reboundTotal`|`<class 'int'>`| `8` | `-` | `No` |
`scoreAway`|`<class 'str'>`| `68` | `-` | `Yes` |
`scoreHome`|`<class 'str'>`| `83` | `-` | `Yes` |
`shotActionNumber`|`<class 'int'>`| `10` | `shotActionNumber is guaranteed to be sequential but not consectutive ([10, 14, 18, 38])` |
`shotDistance`|`<class 'float'>`| `4.44` | `-` | `No` |
`shotResult`|`<class 'str'>`| `"Made" | "Missed"` | `-` | `No` |
`side`|`<class 'str'>`| `null | "left" | "right"` | `-` | `Yes` |
`stealPersonId`|`<class 'int'>`| `1629750` | `-` | `No` |
`stealPlayerName`|`<class 'str'>`| `Green` | `-` | `No` |
`subType`|`<class 'str'>`| `"request` | `subType of the actonType` | `No` |
`teamId`|`<class 'int'>`| `1610612738` | `-` | `No` |
`teamTricode`|`<class 'str'>`| `BOS` | `-` | `No` |
`timeActual`|`<class 'str'>`| `2021-01-16T02:14:17.3Z` | `The time in which the play occurred` | `Yes` |
`turnoverTotal`|`<class 'int'>`| `1` | `-` | `No` |
`value`|`<class 'str'>`| `"Corrected to Offensive Foul on C. Anthony"` | `Was found to be present on an actionType of "instantreplay" and subType of "challenge" with a descriptor of "overturned"` | `No` |
`x`|`<class 'float'>`| `90.22667542706965` | `-` | `Yes` |
`xLegacy`|`<class 'int'>`| `-20` | `-` | `Yes`  |
`y`|`<class 'float'>`| `45.90226715686275` | `-` | `Yes`  |
`yLegacy`|`<class 'int'>`| `39` | `-` | `Yes` |


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
            "actionNumber":2,
            "actionType":"period",
            "assistPersonId":1627759,
            "assistPlayerNameInitial":"J. Brown",
            "assistTotal":1,
            "blockPersonId":1630202,
            "blockPlayerName":"Pritchard",
            "clock":"PT10M53.00S",
            "description":"N. Vucevic 14' turnaround Hook (2 PTS) (A. Gordon 1 AST)",
            "descriptor":"turnaround",
            "edited":"2021-01-16T00:42:13Z",
            "foulDrawnPersonId":201952,
            "foulDrawnPlayerName":"Teague",
            "foulPersonalTotal":1,
            "foulTechnicalTotal":0,
            "isFieldGoal":1,
            "jumpBallLostPersonId":1628407,
            "jumpBallLostPlayerName":"Bacon",
            "jumpBallRecoverdPersonId":1630202,
            "jumpBallRecoveredName":"P. Pritchard",
            "jumpBallWonPersonId":202684,
            "jumpBallWonPlayerName":"Thompson",
            "officialId":202041,
            "orderNumber":20000,
            "period":1,
            "periodType":"REGULAR",
            "personId":202696,
            "personIdsFilter":[
               1630175,
               201952
            ],
            "playerName":"Williams",
            "playerNameI":"G. Williams",
            "pointsTotal":8,
            "possession":1610612753,
            "qualifiers":[
               "pointsinthepaint"
            ],
            "reboundDefensiveTotal":4,
            "reboundOffensiveTotal":3,
            "reboundTotal":7,
            "scoreAway":"68",
            "scoreHome":"72",
            "shotActionNumber":40,
            "shotDistance":10.64,
            "shotResult":"Missed",
            "side":"right",
            "stealPersonId":"202696",
            "stealPlayerName":"Vucevic",
            "subType":"out",
            "teamId":1610612738,
            "teamTricode":"BOS",
            "timeActual":"2021-01-16T01:16:36.7Z",
            "turnoverTotal":2,
            "value":"Corrected to Offensive Foul on C. Anthony",
            "x":80.81471747700394,
            "xLegacy":-63,
            "y":37.31234681372549,
            "yLegacy":128
         }
      ]
   }
}
```

Last validated 2020-08-16