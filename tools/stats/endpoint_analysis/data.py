from nba_api.stats.library.parameters import *

# OLD REGEX FOR MISSING PARAMS
#missing_parameter_regex = r"^\s*?(?:The value '[^']+' is not valid for |The )?([A-z0-9]+( Scope| Category)?)(?: Year)?\s*(?:property (?:is|are) required\.?| (?:is|are) required\.?(?:,? pass 0 for (?:default|all teams))?|\.)$"
# Season Year -> Season     This only occurs in LeagueDashPtStats

#NEW REGEX FOR MISSING PARAMS (Includes Capture Groups + Unit Tests)
missing_parameter_regex = r"(The value '(?P<invalid_value>[^']+)' is not valid for (?P<invalid_parameter>[A-z0-9]+))|(The (?P<required_parameter>[A-z0-9]+) property (is|are) required.)"

parameter_pattern_regex  = r"\s*The field ([A-z]+) must match the regular expression '([^']+)'\.(?:;|$)"

missing_required_parameters = {
    'AllTimeLeadersGrids': {
        'TopX': '10',
        'LeagueID': LeagueID.default,
        'PerMode': PerModeSimple.default,
        'SeasonType': SeasonType.default,
    },
    'BoxScoreSimilarityScore': {
        'Person1Id': '2544',
        'Person2Id': '2544',
        'Person1LeagueId': LeagueID.default,
        'Person1Season': SeasonYear.default,
        'Person1SeasonType': SeasonType.default,
        'Person2LeagueId': LeagueID.default,
        'Person2Season': SeasonYear.default,
        'Person2SeasonType': SeasonType.default,
    },
    'CumeStatsTeamGames': {'Season': Season.default},
    'DefenseHub': {'Season': '2017-18'},
    'DraftBoard': {'Season': SeasonYear.default},
    'GLAlumBoxScoreSimilarityScore': {
        'Person1Id': '2544',
        'Person2Id': '2544',
        'Person1LeagueId': LeagueID.default,
        'Person1Season': SeasonYear.default,
        'Person1SeasonType': SeasonType.default,
        'Person2LeagueId': LeagueID.default,
        'Person2Season': SeasonYear.default,
        'Person2SeasonType': SeasonType.default,
    },
    'LeagueDashLineups': {'Season': Season.default},
    'LeagueDashPlayerClutch': {'Season': Season.default},
    'LeagueDashPlayerStats': {'Season': Season.default},
    'LeagueDashTeamClutch': {'Season': Season.default},
    'LeagueDashTeamShotLocations': {'Season': Season.default},
    'LeagueDashTeamStats': {'Season': Season.default},
    'LeagueGameLog': {'Counter': 0, 'Season': Season.default},
    'LeagueHustleStatsPlayer': {'Season': Season.default},
    'LeagueHustleStatsPlayerLeaders': {'Season': Season.default},
    'LeagueHustleStatsTeam': {'Season': Season.default},
    'LeagueHustleStatsTeamLeaders': {'Season': Season.default},
    'LeagueLeaders': {'Season': Season.default},
    'LeagueLineupViz': {'Season': Season.default},
    'LeaguePlayerOnDetails': {'Season': Season.default, 'TeamID': '1610612739'},  # Cleveland Cavaliers
    'LeagueStandings': {'Season': Season.default},
    'LeagueStandingsV3': {'Season': Season.default},
    'PlayerCareerByCollege': {'College': 'Ohio State'},
    'PlayerCompare': {'Season': Season.default},
    'PlayerDashboardByClutch': {'Season': Season.default},
    'PlayerDashboardByGameSplits': {'Season': Season.default},
    'PlayerDashboardByGeneralSplits': {'Season': Season.default},
    'PlayerDashboardByLastNGames': {'Season': Season.default},
    'PlayerDashboardByOpponent': {'Season': Season.default},
    'PlayerDashboardByShootingSplits': {'Season': Season.default},
    'PlayerDashboardByTeamPerformance': {'Season': Season.default},
    'PlayerDashboardByYearOverYear': {'Season': Season.default},
    'PlayerDashPtPass': {'LeagueID': LeagueID.default},
    'PlayerDashPtReb': {'LeagueID': LeagueID.default},
    'PlayerDashPtShotDefend': {'LeagueID': LeagueID.default},
    'PlayerDashPtShots': {'LeagueID': LeagueID.default},
    'PlayerEstimatedMetrics': {'LeagueID': LeagueID.default, 'Season': Season.default, 'SeasonType': SeasonType.default},
    'PlayerFantasyProfile': {'Season': Season.default},
    'PlayerFantasyProfileBarGraph': {'Season': Season.default},
    'PlayerVsPlayer': {'Season': Season.default},
    'ShotChartDetail': {'ContextMeasure': ContextMeasureSimple.default, 'LeagueID': LeagueID.default, 'PlayerPosition': ''},
    'ShotChartLeagueWide': {'LeagueID': LeagueID.default},
    'ShotChartLineupDetail': {'GameID': '', 'TeamID': ''},
    'TeamAndPlayersVsPlayers': {'Season': Season.default},
    'TeamDashboardByClutch': {'Season': Season.default},
    'TeamDashboardByGameSplits': {'Season': Season.default},
    'TeamDashboardByGeneralSplits': {'Season': Season.default},
    'TeamDashboardByLastNGames': {'Season': Season.default},
    'TeamDashboardByOpponent': {'Season': Season.default},
    'TeamDashboardByShootingSplits': {'Season': Season.default},
    'TeamDashboardByTeamPerformance': {'Season': Season.default},
    'TeamDashboardByYearOverYear': {'Season': Season.default},
    'TeamDashLineups': {'Season': Season.default},
    'TeamDashPtPass': {'LeagueID': LeagueID.default},
    'TeamDashPtReb': {'LeagueID': LeagueID.default},
    'TeamDashPtShots': {'LeagueID': LeagueID.default},
    'TeamEstimatedMetrics': {'LeagueID': LeagueID.default, 'Season': Season.default, 'SeasonType': SeasonType.default},
    'TeamPlayerDashboard': {'Season': Season.default},
    'TeamPlayerOnOffDetails': {'Season': Season.default},
    'TeamPlayerOnOffSummary': {'Season': Season.default},
    'TeamVsPlayer': {'Season': Season.default, 'TeamID': '1610612739'},  # Cleveland Cavaliers
    'VideoDetails': {'Season': Season.default},  # Cleveland Cavaliers
}


parameter_override = {
    'PlayerCareerByCollege': {'School': 'College'},
    'PlayerGameLogs': {'SeasonYear': 'Season'},
    'TeamGameLogs': {'SeasonYear': 'Season'},
}

remove_nullable_parameters = {
    'PlayerCareerByCollege': ['School']
}
