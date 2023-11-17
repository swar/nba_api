# GLAlumBoxScoreSimilarityScore
##### [nba_api/stats/endpoints/glalumboxscoresimilarityscore.py](https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/glalumboxscoresimilarityscore.py)

##### Endpoint URL
>[https://stats.nba.com/stats/glalumboxscoresimilarityscore](https://stats.nba.com/stats/glalumboxscoresimilarityscore)

##### Valid URL
>[https://stats.nba.com/stats/glalumboxscoresimilarityscore?Person1Id=202681&Person1LeagueId=00&Person1Season=2019&Person1SeasonType=Regular+Season&Person2Id=203078&Person2LeagueId=00&Person2Season=2019&Person2SeasonType=Regular+Season](https://stats.nba.com/stats/glalumboxscoresimilarityscore?Person1Id=202681&Person1LeagueId=00&Person1Season=2019&Person1SeasonType=Regular+Season&Person2Id=203078&Person2LeagueId=00&Person2Season=2019&Person2SeasonType=Regular+Season)

## Parameters
| API Parameter Name                                                                                                                | Python Parameter Variable | Pattern | Required | Nullable |
|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------|:-------:|:--------:|:--------:|
| [_**Person1Id**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Person1Id)                 | person1_id                |         |   `Y`    |          | 
| [_**Person1LeagueId**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Person1LeagueId)     | person1_league_id         |         |   `Y`    |          | 
| [_**Person1Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Person1Season)         | person1_season_year       |         |   `Y`    |          | 
| [_**Person1SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Person1SeasonType) | person1_season_type       |         |   `Y`    |          | 
| [_**Person2Id**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Person2Id)                 | person2_id                |         |   `Y`    |          | 
| [_**Person2LeagueId**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Person2LeagueId)     | person2_league_id         |         |   `Y`    |          | 
| [_**Person2Season**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Person2Season)         | person2_season_year       |         |   `Y`    |          | 
| [_**Person2SeasonType**_](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md#Person2SeasonType) | person2_season_type       |         |   `Y`    |          | 

## Data Sets
#### GLeagueAlumBoxScoreSimilarityScores `g_league_alum_box_score_similarity_scores`
```text
['PERSON_2_ID', 'PERSON_2', 'TEAM_ID', 'SIMILARITY_SCORE']
```


## JSON
```json
{
    "data_sets": {
        "GLeagueAlumBoxScoreSimilarityScores": [
            "PERSON_2_ID",
            "PERSON_2",
            "TEAM_ID",
            "SIMILARITY_SCORE"
        ]
    },
    "endpoint": "GLAlumBoxScoreSimilarityScore",
    "last_validated_date": "2020-08-15",
    "nullable_parameters": [],
    "parameter_patterns": {
        "Person1Id": null,
        "Person1LeagueId": null,
        "Person1Season": null,
        "Person1SeasonType": null,
        "Person2Id": null,
        "Person2LeagueId": null,
        "Person2Season": null,
        "Person2SeasonType": null
    },
    "parameters": [
        "Person1Id",
        "Person1LeagueId",
        "Person1Season",
        "Person1SeasonType",
        "Person2Id",
        "Person2LeagueId",
        "Person2Season",
        "Person2SeasonType"
    ],
    "required_parameters": [
        "Person1Id",
        "Person1LeagueId",
        "Person1Season",
        "Person1SeasonType",
        "Person2Id",
        "Person2LeagueId",
        "Person2Season",
        "Person2SeasonType"
    ],
    "status": "success"
}
```

Last validated 2020-08-16