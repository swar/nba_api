from nba_api.stats.library.http import NBAStatsResponse
nba_stats_response =  NBAStatsResponse

nba_stats_response_400 = nba_stats_response('The LeagueID property is required.; The Season property is required.', 400, 'https://stats.nba.com/stats/PlayerIndex')
nba_stats_response_200 = nba_stats_response('{"resource":"playerindex","parameters":{"LeagueID":"00","Season":"2020-21", \
    "Historical":null,"TeamID":null,"Country":null,"College":null,"DraftYear":null,"DraftPick":null,"PlayerPosition":null, \
    "Height":null,"Weight":null,"Active":null,"AllStar":null},"resultSets":[{"name":"PlayerIndex","headers": \
    ["PERSON_ID","PLAYER_LAST_NAME","PLAYER_FIRST_NAME","PLAYER_SLUG","TEAM_ID","TEAM_SLUG","IS_DEFUNCT","TEAM_CITY","TEAM_NAME", \
    "TEAM_ABBREVIATION","JERSEY_NUMBER","POSITION","HEIGHT","WEIGHT","COLLEGE","COUNTRY","DRAFT_YEAR","DRAFT_ROUND","DRAFT_NUMBER", \
    "ROSTER_STATUS","FROM_YEAR","TO_YEAR","PTS","REB","AST","STATS_TIMEFRAME"],"rowSet":[[1630173,"Achiuwa","Precious","precious-achiuwa", \
    1610612748,"heat",0,"Miami","Heat","MIA","5","F","6-8","225","Memphis","Nigeria",2020,1,20,1.0,"2020","2021",5.000,3.400,0.500,"Season"], \
    [1629121,"Adams","Jaylen","jaylen-adams",0,null,0,null,null,null,null,"G","6-0","225","St. Bonaventure","USA",null,null,null,null, \
    "2018","2020",0.300,0.400,0.300,"Season"],[203500,"Adams","Steven","steven-adams",1610612740,"pelicans",0,"New Orleans","Pelicans","NOP", \
    "12","C","6-11","265","Pittsburgh","New Zealand",2013,1,12,1.0,"2013","2021",7.600,8.900,1.900,"Season"]]}]}', 200, \
    'https://stats.nba.com/stats/PlayerIndex?LeagueID=00&Season=2020-21')