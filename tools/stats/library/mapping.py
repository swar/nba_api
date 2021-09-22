from nba_api.stats.library.parameters import *

endpoint_list = [
    # '2AssistTracker',
    # 'AllPlayers',
    # 'AllStarBallotPredictor',
    # 'AllTimeLeadersGrids',
    # 'AssistLeaders',
    # 'AssistTracker',
    # 'AssistTrackerStats',
    # 'BoxScoreAdvanced',
    # 'BoxScoreAdvancedV2',
    # 'BoxScoreDefensive',
    # 'BoxScoreFourFactors',
    # 'BoxScoreFourFactorsV2',
    # 'BoxScoreMatchups',
    # 'BoxScoreMisc',
    # 'BoxScoreMiscV2',
    # 'BoxScorePlayerTracking',
    # 'BoxScorePlayerTrackV2',
    # 'BoxScoreScoring',
    # 'BoxScoreScoringV2',
    # 'BoxScoreSimilarityScore',
    # 'BoxScoreSummary',
    # 'BoxScoreSummaryV2',
    # 'BoxScoreTraditional',
    # 'BoxScoreTraditionalV2',
    # 'BoxScoreUsage',
    # 'BoxScoreUsageV2',
    # 'CommonAllPlayers',
    # 'CommonPlayerInfo',
    # 'CommonPlayoffSeries',
    # 'CommonTeamRoster',
    # 'CommonTeamYears',
    # 'CumeStatsPlayer',
    # 'CumeStatsPlayerGames',
    # 'CumeStatsTeam',
    # 'CumeStatsTeamGames',
    # 'DefenseHub',
    # 'DLeaguePredictor',
    # 'DraftBoard',
    # 'DraftCombineDrillResults',
    # 'DraftCombineNonStationaryShooting',
    # 'DraftCombinePlayerAnthro',
    # 'DraftCombinePlayerMeasurements',
    # 'DraftCombineSpotShooting',
    # 'DraftCombineStats',
    # 'DraftHistory',
    # 'FantasyWidget',
    # 'FranchiseHistory',
    # 'FranchiseLeaders',
    # 'FranchisePlayers',
    # 'GameRotation',
    # 'GLAlumBoxScoreSimilarityScore',
    # 'GLeaguePredictor',
    # 'HomePage',
    # 'HomePageLeaders',
    # 'HomePageV2',
    # 'HustleStatsBoxScore',
    # 'InfographicFanDuelPlayer',
    # 'LeadersTiles',
    # 'LeagueDashLineups',
    # 'LeagueDashOppPtShot',
    # 'LeagueDashPlayerBioStats',
    # 'LeagueDashPlayerClutch',
    # 'LeagueDashPlayerPtShot',
    # 'LeagueDashPlayerShotLocations',
    # 'LeagueDashPlayerStats',
    # 'LeagueDashPtDefend',
    # 'LeagueDashPtStats',
    # 'LeagueDashPtTeamDefend',
    # 'LeagueDashTeamClutch',
    # 'LeagueDashTeamPtShot',
    # 'LeagueDashTeamShotLocations',
    # 'LeagueDashTeamStats',
    # 'LeagueGameFinder',
    # 'LeagueGameLog',
    # 'LeagueHustleStatsPlayer',
    # 'LeagueHustleStatsPlayerLeaders',
    # 'LeagueHustleStatsTeam',
    # 'LeagueHustleStatsTeamLeaders',
    # 'LeagueLeaders',
    # 'LeagueLineupViz',
    # 'LeaguePlayerOnDetails',
    # 'LeagueSeasonMatchups',
    # 'LeagueStandings',
    # 'LeagueStandingsV3',
    # 'LineupStats',
    # 'MatchupsRollup',
    'PlayByPlay',
    # 'PlayByPlayMini',
    # 'PlayByPlayV2',
    # 'PlayerAwards',
    # 'PlayerBioStats',
    # 'PlayerCareerByCollege',
    # 'PlayerCareerByCollegeRollup',
    # 'PlayerCareerStats',
    # 'PlayerClutchStats',
    # 'PlayerCompare',
    # 'PlayerCompareStats',
    # 'PlayerDashboardByClutch',
    # 'PlayerDashboardByGameSplits',
    # 'PlayerDashboardByGeneralSplits',
    # 'PlayerDashboardByLastNGames',
    # 'PlayerDashboardByOpponent',
    # 'PlayerDashboardByShootingSplits',
    # 'PlayerDashboardByTeamPerformance',
    # 'PlayerDashboardByYearOverYear',
    # 'PlayerDashPtPass',
    # 'PlayerDashPtReb',
    # 'PlayerDashPtReboundLogs',
    # 'PlayerDashPtShotDefend',
    # 'PlayerDashPtShotlog',
    # 'PlayerDashPtShots',
    # 'PlayerDefenseStats',
    # 'PlayerEstimatedMetrics',
    # 'PlayerFantasyProfile',
    # 'PlayerFantasyProfileBarGraph',
    # 'PlayerGameLog',
    # 'PlayerGameLogs',
    # 'PlayerGameLogsStats',
    # 'PlayerGameSplitsStats',
    # 'PlayerGameStreakFinder',
    # 'PlayerGeneralSplitsStats',
    # 'PlayerInfo',
    # 'PlayerLastNGamesStats',
    # 'PlayerNextNGames',
    # 'PlayerOnDetails',
    # 'PlayerOpponentStats',
    # 'PlayerPassesStats',
    # 'PlayerProfile',
    # 'PlayerProfileV2',
    # 'PlayerReboundsStats',
    # 'PlayersCareerStats',
    # 'PlayersClutchStats',
    # 'PlayersDefenseStats',
    # 'PlayersGeneralStats',
    # 'PlayerShotChartDetail',
    # 'PlayerShotsStats',
    # 'PlayersHustleLeaders',
    # 'PlayersHustleStats',
    # 'PlayersShotLocationStats',
    # 'PlayersShotStats',
    # 'PlayersTrackingStats',
    # 'PlayersVsPlayers',
    # 'PlayerTeamPerformanceStats',
    # 'PlayerTrackBucketSimilarityScore',
    # 'PlayerTrackRankSimilarityComp',
    # 'PlayerTrackSimilarityScore',
    # 'PlayerTrackSimilarityUniqueness',
    # 'PlayerVsPlayer',
    # 'PlayerYearOverYearStats',
    # 'PlayoffPicture',
    # 'PlayoffSeries',
    # 'Scoreboard',
    # 'ScoreboardMini',
    # 'ScoreboardV2',
    # 'ShotChartDetail',
    # 'ShotChartLeagueWide',
    # 'ShotChartLineupDetail',
    # 'SynergyBucketSimilarityScore',
    # 'SynergyPlayTypes',
    # 'SynergySimilarityScore',
    # 'TeamAndPlayerVsPlayers',
    # 'TeamAndPlayersVsPlayers',
    # 'TeamClutchStats',
    # 'TeamDashboardByClutch',
    # 'TeamDashboardByGameSplits',
    # 'TeamDashboardByGeneralSplits',
    # 'TeamDashboardByLastNGames',
    # 'TeamDashboardByOpponent',
    # 'TeamDashboardByShootingSplits',
    # 'TeamDashboardByTeamPerformance',
    # 'TeamDashboardByYearOverYear',
    # 'TeamDashLineups',
    # 'TeamDashPtPass',
    # 'TeamDashPtReb',
    # 'TeamDashPtShots',
    # 'TeamDetails',
    # 'TeamEstimatedMetrics',
    # 'TeamFranchiseLeaders',
    # 'TeamFranchiseLeadersRank',
    # 'TeamGameLog',
    # 'TeamGameLogs',
    # 'TeamGameSplitsStats',
    # 'TeamGameStreakFinder',
    # 'TeamGeneralSplitsStats',
    # 'TeamHistoricalLeaders',
    # 'TeamInfo',
    # 'TeamInfoCommon',
    # 'TeamLastNGamesStats',
    # 'TeamLineupStats',
    # 'TeamOpponentStats',
    # 'TeamPassesStats',
    # 'TeamPerformanceStats',
    # 'TeamPlayerDashboard',
    # 'TeamPlayerOnOffDetails',
    # 'TeamPlayerOnOffSummary',
    # 'TeamPlayerStats',
    # 'TeamReboundsStats',
    # 'TeamRoster',
    # 'TeamsClutchStats',
    # 'TeamsDefenseStats',
    # 'TeamsGeneralStats',
    # 'TeamShootingSplitsStats',
    # 'TeamShotChartLineupDetail',
    # 'TeamShotsStats',
    # 'TeamsHustleLeaders',
    # 'TeamsHustleStats',
    # 'TeamsShotLocationStats',
    # 'TeamsShotStats',
    # 'TeamsYearByYearStats',
    # 'TeamVsPlayer',
    # 'TeamYearByYearStats',
    # 'TeamYearOverYearStats',
    # 'TeamYears',
    # 'VideoDetails',
    # 'VideoEvents',
    # 'VideoStatus',
    # 'WinProbabilityPlayByPlay',
    # 'WinProbabilityPBP',
]

parameter_variations = {
    'GameEventID': {
        'default_py_value': '0',
        'parameter_value': '0',
        'parameter_error_value': 'a',
    },
    'GameID': {
        'default_py_value': None,
        'parameter_value': '0021700807',  # CLE vs MIN - 2018-02-07
        'parameter_error_value': 'a',
    },
    'GameIDs': {
        'default_py_value': None,
        'parameter_value': '0021700807',  # CLE vs MIN - 2018-02-07
        'parameter_error_value': 'a',
    },
    'GameIDNullable': {
        'default_py_value': "''",
        'parameter_value': None,
        'parameter_error_value': 'a',
    },
    'Person1LeagueID': {
        'default_py_value': 'LeagueID.default',
        'parameter_value': LeagueID.default,
        'parameter_error_value': 'a',
    },
    'Person2LeagueID': {
        'default_py_value': 'LeagueID.default',
        'parameter_value': LeagueID.default,
        'parameter_error_value': 'a',
    },
    'LeagueID': {
        'default_py_value': 'LeagueID.default',
        'parameter_value': LeagueID.default,
        'parameter_error_value': 'a',
    },
    'LeagueIDNullable': {
        'default_py_value': 'LeagueIDNullable.default',
        'parameter_value': LeagueIDNullable.default,
        'parameter_error_value': 'a',
    },
    'ActiveFlagNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'AheadBehind': {
        'default_py_value': 'AheadBehind.default',
        'parameter_value': AheadBehind.default,
        'parameter_error_value': 0,
    },
    'AheadBehindNullable': {
        'default_py_value': 'AheadBehindNullable.default',
        'parameter_value': AheadBehindNullable.default,
        'parameter_error_value': 0,
    },
    'CloseDefDistRangeNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'ClutchTime': {
        'default_py_value': 'ClutchTime.default',
        'parameter_value': ClutchTime.default,
        'parameter_error_value': 0,
    },
    'ClutchTimeNullable': {
        'default_py_value': 'ClutchTimeNullable.default',
        'parameter_value': ClutchTimeNullable.default,
        'parameter_error_value': 0,
    },
    'College': {
        'default_py_value': None,
        'parameter_value': 'Ohio State',
        'parameter_error_value': 1,
    },
    'CollegeNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'Conference': {
        'default_py_value': 'Conference.default',
        'parameter_value': Conference.default,
        'parameter_error_value': 0,
    },
    'ConferenceNullable': {
        'default_py_value': 'ConferenceNullable.default',
        'parameter_value': ConferenceNullable.default,
        'parameter_error_value': 0,
    },
    'VsConference': {
        'default_py_value': 'Conference.default',
        'parameter_value': Conference.default,
        'parameter_error_value': 0,
    },
    'VsConferenceNullable': {
        'default_py_value': 'ConferenceNullable.default',
        'parameter_value': ConferenceNullable.default,
        'parameter_error_value': 0,
    },
    'ContextFilterNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'ContextMeasureSimple': {
        'default_py_value': 'ContextMeasureSimple.default',
        'parameter_value': ContextMeasureSimple.default,
        'parameter_error_value': 0,
    },
    'ContextMeasureSimpleNullable': {
        'default_py_value': 'ContextMeasureSimpleNullable.default',
        'parameter_value': ContextMeasureSimpleNullable.default,
        'parameter_error_value': 0,
    },
    'ContextMeasureDetailed': {
        'default_py_value': 'ContextMeasureDetailed.default',
        'parameter_value': ContextMeasureDetailed.default,
        'parameter_error_value': 0,
    },
    'Counter': {
        'default_py_value': '0',
        'parameter_value': '0',
        'parameter_error_value': 'a',
    },
    'CounterNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'CountryNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'DateFromNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'DateToNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'DayOffset': {
        'default_py_value': 'DayOffset.default',
        'parameter_value': DayOffset.default,
        'parameter_error_value': 'a',
    },
    'DefenseCategory': {
        'default_py_value': 'DefenseCategory.default',
        'parameter_value': DefenseCategory.default,
        'parameter_error_value': 0,
    },
    'DefenseCategoryNullable': {
        'default_py_value': 'DefenseCategoryNullable.default',
        'parameter_value': DefenseCategoryNullable.default,
        'parameter_error_value': 0,
    },
    'Direction': {
        'default_py_value': 'Direction.default',
        'parameter_value': Direction.default,
        'parameter_error_value': 0,
    },
    'DistanceRange': {
        'default_py_value': 'DistanceRange.default',
        'parameter_value': DistanceRange.default,
        'parameter_error_value': 0,
    },
    'DivisionSimple': {
        'default_py_value': 'DivisionSimple.default',
        'parameter_value': DivisionSimple.default,
        'parameter_error_value': 0,
    },
    'DivisionSimpleNullable': {
        'default_py_value': 'DivisionSimpleNullable.default',
        'parameter_value': DivisionSimpleNullable.default,
        'parameter_error_value': 0,
    },
    'Division': {
        'default_py_value': 'Division.default',
        'parameter_value': Division.default,
        'parameter_error_value': 0,
    },
    'DivisionNullable': {
        'default_py_value': 'DivisionNullable.default',
        'parameter_value': DivisionNullable.default,
        'parameter_error_value': 0,
    },
    'VsDivision': {
        'default_py_value': 'Division.default',
        'parameter_value': Division.default,
        'parameter_error_value': 0,
    },
    'VsDivisionNullable': {
        'default_py_value': 'DivisionNullable.default',
        'parameter_value': DivisionNullable.default,
        'parameter_error_value': 0,
    },
    'DraftPickNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'DraftYearNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'DribbleRangeNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GameDate': {
        'default_py_value': 'GameDate.default',
        'parameter_value': GameDate.default,
        'parameter_error_value': 'a',
    },
    'GameScopeSimple': {
        'default_py_value': 'GameScopeSimple.default',
        'parameter_value': GameScopeSimple.default,
        'parameter_error_value': 0,
    },
    'GameScopeSimpleNullable': {
        'default_py_value': 'GameScopeSimpleNullable.default',
        'parameter_value': GameScopeSimpleNullable.default,
        'parameter_error_value': 0,
    },
    'GameScopeDetailed': {
        'default_py_value': 'GameScopeDetailed.default',
        'parameter_value': GameScopeDetailed.default,
        'parameter_error_value': 0,
    },
    'GameSegment': {
        'default_py_value': 'GameSegment.default',
        'parameter_value': GameSegment.default,
        'parameter_error_value': '234',
    },
    'GameSegmentNullable': {
        'default_py_value': 'GameSegmentNullable.default',
        'parameter_value': GameSegmentNullable.default,
        'parameter_error_value': '234',
    },
    'GeneralRangeNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GraphStatNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GroupQuantity': {
        'default_py_value': 'GroupQuantity.default',
        'parameter_value': GroupQuantity.default,
        'parameter_error_value': 'a',
    },
    'GroupID': {
        'default_py_value': '0',
        'parameter_value': 0,
        'parameter_error_value': 'a',
    },
    'HeightNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LastNGames': {
        'default_py_value': 'LastNGames.default',
        'parameter_value': LastNGames.default,
        'parameter_error_value': 'a',
    },
    'LastNGamesNullable': {
        'default_py_value': 'LastNGamesNullable.default',
        'parameter_value': LastNGamesNullable.default,
        'parameter_error_value': 'a',
    },
    'Location': {
        'default_py_value': 'Location.default',
        'parameter_value': Location.default,
        'parameter_error_value': 0,
    },
    'LocationNullable': {
        'default_py_value': 'LocationNullable.default',
        'parameter_value': LocationNullable.default,
        'parameter_error_value': 0,
    },
    'Month': {
        'default_py_value': 'Month.default',
        'parameter_value': Month.default,
        'parameter_error_value': 'a',
    },
    'MonthNullable': {
        'default_py_value': 'MonthNullable.default',
        'parameter_value': MonthNullable.default,
        'parameter_error_value': 'a',
    },
    'MeasureTypeBase': {
        'default_py_value': 'MeasureTypeBase.default',
        'parameter_value': MeasureTypeBase.default,
        'parameter_error_value': 0,
    },
    'MeasureTypeSimple': {
        'default_py_value': 'MeasureTypeSimple.default',
        'parameter_value': MeasureTypeSimple.default,
        'parameter_error_value': 0,
    },
    'MeasureTypeDetailed': {
        'default_py_value': 'MeasureTypeDetailed.default',
        'parameter_value': MeasureTypeDetailed.default,
        'parameter_error_value': 0,
    },
    'MeasureTypeDetailedDefense': {
        'default_py_value': 'MeasureTypeDetailedDefense.default',
        'parameter_value': MeasureTypeDetailedDefense.default,
        'parameter_error_value': 0,
    },
    'MeasureTypePlayerGameLogsNullable': {
        'default_py_value': None,
        'parameter_value': '',
        'parameter_error_value': 0,
    },
    'NumberOfGames': {
        'default_py_value': 'NumberOfGames.default',
        'parameter_value': NumberOfGames.default,
        'parameter_error_value': 0,
    },
    'Outcome': {
        'default_py_value': 'Outcome.default',
        'parameter_value': Outcome.default,
        'parameter_error_value': 0,
    },
    'OutcomeNullable': {
        'default_py_value': 'OutcomeNullable.default',
        'parameter_value': OutcomeNullable.default,
        'parameter_error_value': 0,
    },
    'OverallPickNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'PaceAdjust': {
        'default_py_value': 'PaceAdjust.default',
        'parameter_value': PaceAdjust.default,
        'parameter_error_value': 0,
    },
    'PaceAdjustNo': {
        'default_py_value': 'PaceAdjustNo.default',
        'parameter_value': PaceAdjustNo.default,
        'parameter_error_value': 0,
    },
    'PlusMinus': {
        'default_py_value': 'PlusMinus.default',
        'parameter_value': PlusMinus.default,
        'parameter_error_value': 0,
    },
    'PlusMinusNo': {
        'default_py_value': 'PlusMinusNo.default',
        'parameter_value': PlusMinusNo.default,
        'parameter_error_value': 0,
    },
    'Period': {
        'default_py_value': 'Period.default',
        'parameter_value': Period.default,
        'parameter_error_value': 'a',
    },
    'PeriodNullable': {
        'default_py_value': 'PeriodNullable.default',
        'parameter_value': PeriodNullable.default,
        'parameter_error_value': 'a',
    },
    'StartPeriod': {
        'default_py_value': 'StartPeriod.default',
        'parameter_value': '1',
        'parameter_error_value': 'a',
    },
    'StartPeriodNullable': {
        'default_py_value': 'StartPeriodNullable.default',
        'parameter_value': StartPeriodNullable.default,
        'parameter_error_value': 'a',
    },
    'EndPeriod': {
        'default_py_value': 'EndPeriod.default',
        'parameter_value': '1',
        'parameter_error_value': 'a',
    },
    'EndPeriodNullable': {
        'default_py_value': 'EndPeriodNullable.default',
        'parameter_value': EndPeriodNullable.default,
        'parameter_error_value': 'a',
    },
    'PerModeSimple': {
        'default_py_value': 'PerModeSimple.default',
        'parameter_value': PerModeSimple.default,
        'parameter_error_value': 0,
    },
    'PerModeSimpleNullable': {
        'default_py_value': 'PerModeSimpleNullable.default',
        'parameter_value': PerModeSimpleNullable.default,
        'parameter_error_value': 0,
    },
    'PerMode36': {
        'default_py_value': 'PerMode36.default',
        'parameter_value': PerMode36.default,
        'parameter_error_value': 0,
    },
    'PerMode48': {
        'default_py_value': 'PerMode48.default',
        'parameter_value': PerMode48.default,
        'parameter_error_value': 0,
    },
    'PerModeTime': {
        'default_py_value': 'PerModeTime.default',
        'parameter_value': PerModeTime.default,
        'parameter_error_value': 0,
    },
    'PerModeDetailed': {
        'default_py_value': 'PerModeDetailed.default',
        'parameter_value': PerModeDetailed.default,
        'parameter_error_value': 0,
    },
    'PlayerExperience': {
        'default_py_value': 'PlayerExperience.default',
        'parameter_value': PlayerExperience.default,
        'parameter_error_value': 0,
    },
    'PlayerExperienceNullable': {
        'default_py_value': 'PlayerExperienceNullable.default',
        'parameter_value': PlayerExperienceNullable.default,
        'parameter_error_value': 0,
    },
    'ActivePlayers': {
        'default_py_value': 'ActivePlayers.default',
        'parameter_value': ActivePlayers.default,
        'parameter_error_value': 'a',
    },
    'TodaysPlayers': {
        'default_py_value': 'TodaysPlayers.default',
        'parameter_value': TodaysPlayers.default,
        'parameter_error_value': 'a',
    },
    'PlayerID': {
        'default_py_value': None,
        'parameter_value': '2544',  # Lebron James
        'parameter_error_value': 'a',
    },
    'PlayerIDNullable': {
        'default_py_value': "''",
        'parameter_value': '',  # Lebron James
        'parameter_error_value': 'a',
    },
    'DefPlayerIDNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'OffPlayerIDNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'VsPlayerID': {
        'default_py_value': None,
        'parameter_value': '2544',  # Lebron James
        'parameter_error_value': 'a',
    },
    'Person1ID': {
        'default_py_value': None,
        'parameter_value': '202681',  # Kyrie Irving
        'parameter_error_value': 'a',
    },
    'Person2ID': {
        'default_py_value': None,
        'parameter_value': '203078',  # Bradley Beal
        'parameter_error_value': 'a',
    },
    'PlayerID1': {
        'default_py_value': None,
        'parameter_value': '202681',  # Kyrie Irving
        'parameter_error_value': 'a',
    },
    'PlayerID2': {
        'default_py_value': None,
        'parameter_value': '203078',  # Bradley Beal
        'parameter_error_value': 'a',
    },
    'PlayerID3': {
        'default_py_value': None,
        'parameter_value': '203507',  # Giannis Antetokounmpo
        'parameter_error_value': 'a',
    },
    'PlayerID4': {
        'default_py_value': None,
        'parameter_value': '201567',  # Kevin Love
        'parameter_error_value': 'a',
    },
    'PlayerID5': {
        'default_py_value': None,
        'parameter_value': '203954',  # Joel Embiid
        'parameter_error_value': 'a',
    },
    'VsPlayerID1': {
        'default_py_value': None,
        'parameter_value': '201566',  # Russel Westbrook
        'parameter_error_value': 'a',
    },
    'VsPlayerID2': {
        'default_py_value': None,
        'parameter_value': '201939',  # Stephen Curry
        'parameter_error_value': 'a',
    },
    'VsPlayerID3': {
        'default_py_value': None,
        'parameter_value': '201935',  # James Harden
        'parameter_error_value': 'a',
    },
    'VsPlayerID4': {
        'default_py_value': None,
        'parameter_value': '201142',  # Kevin Durant
        'parameter_error_value': 'a',
    },
    'VsPlayerID5': {
        'default_py_value': None,
        'parameter_value': '203076',  # Anthony Davis
        'parameter_error_value': 'a',
    },
    'EastPlayer1': {
        'default_py_value': None,
        'parameter_value': '202681',  # Kyrie Irving
        'parameter_error_value': 'a',
    },
    'EastPlayer2': {
        'default_py_value': None,
        'parameter_value': '203078',  # Bradley Beal
        'parameter_error_value': 'a',
    },
    'EastPlayer3': {
        'default_py_value': None,
        'parameter_value': '2544',  # Lebron James
        'parameter_error_value': 'a',
    },
    'EastPlayer4': {
        'default_py_value': None,
        'parameter_value': '201567',  # Kevin Love
        'parameter_error_value': 'a',
    },
    'EastPlayer5': {
        'default_py_value': None,
        'parameter_value': '203954',  # Joel Embiid
        'parameter_error_value': 'a',
    },
    'WestPlayer1': {
        'default_py_value': None,
        'parameter_value': '201566',  # Russel Westbrook
        'parameter_error_value': 'a',
    },
    'WestPlayer2': {
        'default_py_value': None,
        'parameter_value': '201939',  # Stephen Curry
        'parameter_error_value': 'a',
    },
    'WestPlayer3': {
        'default_py_value': None,
        'parameter_value': '201935',  # James Harden
        'parameter_error_value': 'a',
    },
    'WestPlayer4': {
        'default_py_value': None,
        'parameter_value': '201142',  # Kevin Durant
        'parameter_error_value': 'a',
    },
    'WestPlayer5': {
        'default_py_value': None,
        'parameter_value': '203076',  # Anthony Davis
        'parameter_error_value': 'a',
    },
    'PlayerIDList': {
        'default_py_value': None,
        'parameter_value': '202681,203078,2544,201567,203954',  # Kyrie Irving & Bradley Beal & Lebron James & Kevin Love & Joel Embiid
        'parameter_error_value': 'a',
    },
    'VsPlayerIDList': {
        'default_py_value': None,
        'parameter_value': '201566,201939,201935,201142,203076',  # Russel Westbrook & Stephen Curry & James Harden & Kevin Durant & Anthony Davis
        'parameter_error_value': 'a',
    },
    'PlayerOrTeam': {
        'default_py_value': 'PlayerOrTeam.default',
        'parameter_value': PlayerOrTeam.default,
        'parameter_error_value': 0,
    },
    'PlayerOrTeamAbbreviation': {
        'default_py_value': 'PlayerOrTeamAbbreviation.default',
        'parameter_value': PlayerOrTeamAbbreviation.default,
        'parameter_error_value': 0,
    },
    'PlayerPosition': {
        'default_py_value': 'PlayerPosition.default',
        'parameter_value': PlayerPosition.default,
        'parameter_error_value': 0,
    },
    'PlayerPositionNullable': {
        'default_py_value': 'PlayerPositionNullable.default',
        'parameter_value': PlayerPositionNullable.default,
        'parameter_error_value': 0,
    },
    'PlayerPositionAbbreviation': {
        'default_py_value': 'PlayerPositionAbbreviation.default',
        'parameter_value': PlayerPositionAbbreviation.default,
        'parameter_error_value': 0,
    },
    'PlayerPositionAbbreviationNullable': {
        'default_py_value': 'PlayerPositionAbbreviationNullable.default',
        'parameter_value': PlayerPositionAbbreviationNullable.default,
        'parameter_error_value': 0,
    },
    'PlayerScope': {
        'default_py_value': 'PlayerScope.default',
        'parameter_value': PlayerScope.default,
        'parameter_error_value': 0,
    },
    'PlayerTeamID': {
        'default_py_value': None,
        'parameter_value': '1610612739',  # Cleveland Cavaliers
        'parameter_error_value': 'a',
    },
    'VsTeamID': {
        'default_py_value': None,
        'parameter_value': '1610612765',  # Detroit Pistons
        'parameter_error_value': 'a',
    },
    'VsTeamIDNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'TeamID': {
        'default_py_value': None,
        'parameter_value': '1610612739',  # Cleveland Cavaliers
        'parameter_error_value': 'a',
    },
    'TeamIDNullable': {
        'default_py_value': "''",
        'parameter_value': '0',  # Cleveland Cavaliers: 1610612739
        'parameter_error_value': 'a',
    },
    'DLeagueTeamIDNullable': {
        'default_py_value': "0",
        'parameter_value': '0',  # Cleveland Cavaliers: 1610612739
        'parameter_error_value': 'a',
    },
    'TodaysOpponent': {
        'default_py_value': 0,
        'parameter_value': '0',
        'parameter_error_value': 'a',
    },
    'OppTeamIDNullable': {
        'default_py_value': None,
        'parameter_value': '0',
        'parameter_error_value': 'a',
    },
    'OpponentTeamID': {
        'default_py_value': '0',
        'parameter_value': '0',
        'parameter_error_value': 'a',
    },
    'OpponentTeamIDNullable': {
        'default_py_value': "''",
        'parameter_value': '0',  # Dallas Mavericks: 1610612742
        'parameter_error_value': 'a',
    },
    'DefTeamID': {
        'default_py_value': None,
        'parameter_value': '1610612742',  # Dallas Mavericks
        'parameter_error_value': 'a',
    },
    'DefTeamIDNullable': {
        'default_py_value': None,
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'OffTeamID': {
        'default_py_value': None,
        'parameter_value': '1610612739',  # Cleveland Cavaliers
        'parameter_error_value': 'a',
    },
    'OffTeamIDNullable': {
        'default_py_value': None,
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'PlayType': {
        'default_py_value': 'PlayType.default',
        'parameter_value': PlayType.default,
        'parameter_error_value': 0,
    },
    'PlayTypeNullable': {
        'default_py_value': 'PlayTypeNullable.default',
        'parameter_value': PlayTypeNullable.default,
        'parameter_error_value': 0,
    },
    'PointDiff': {
        'default_py_value': 'PointDiff.default',
        'parameter_value': PointDiff.default,
        'parameter_error_value': 0,
    },
    'PointDiffNullable': {
        'default_py_value': 'PointDiffNullable.default',
        'parameter_value': PointDiffNullable.default,
        'parameter_error_value': 0,
    },
    'PORoundNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'PositionNullable': {
        'default_py_value': "PositionNullable.default",
        'parameter_value': PositionNullable.default,
        'parameter_error_value': 'a',
    },
    'PtMeasureType': {
        'default_py_value': 'PtMeasureType.default',
        'parameter_value': PtMeasureType.default,
        'parameter_error_value': 0,
    },
    'RangeType': {
        'default_py_value': 'RangeType.default',
        'parameter_value': RangeType.default,
        'parameter_error_value': 'a',
    },
    'RangeTypeNullable': {
        'default_py_value': 'RangeTypeNullable.default',
        'parameter_value': RangeTypeNullable.default,
        'parameter_error_value': 'a',
    },
    'Sorter': {
        'default_py_value': 'Sorter.default',
        'parameter_value': Sorter.default,
        'parameter_error_value': 'a',
    },
    'StartRange': {
        'default_py_value': 'StartRange.default',
        'parameter_value': StartRange.default,
        'parameter_error_value': 'a',
    },
    'StartRangeNullable': {
        'default_py_value': 'StartRangeNullable.default',
        'parameter_value': StartRangeNullable.default,
        'parameter_error_value': 'a',
    },
    'EndRange': {
        'default_py_value': 'EndRange.default',
        'parameter_value': EndRange.default,
        'parameter_error_value': 'a',
    },
    'EndRangeNullable': {
        'default_py_value': 'EndRangeNullable.default',
        'parameter_value': EndRangeNullable.default,
        'parameter_error_value': 'a',
    },
    'Rank': {
        'default_py_value': 'Rank.default',
        'parameter_value': Rank.default,
        'parameter_error_value': 0,
    },
    'RankNo': {
        'default_py_value': 'RankNo.default',
        'parameter_value': RankNo.default,
        'parameter_error_value': 0,
    },
    'RoundNumNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'RoundPickNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'Scope': {
        'default_py_value': 'Scope.default',
        'parameter_value': Scope.default,
        'parameter_error_value': 'a',
    },
    'RunType': {
        'default_py_value': 'RunType.default',
        'parameter_value': RunType.default,
        'parameter_error_value': 'a',
    },
    'Person1SeasonYear': {
        'default_py_value': 'SeasonYear.default',
        'parameter_value': SeasonYear.default,
        'parameter_error_value': 'a',
    },
    'Person2SeasonYear': {
        'default_py_value': 'SeasonYear.default',
        'parameter_value': SeasonYear.default,
        'parameter_error_value': 'a',
    },
    'SeasonYear': {
        'default_py_value': 'SeasonYear.default',
        'parameter_value': SeasonYear.default,
        'parameter_error_value': 'a',
    },
    'SeasonYearNullable': {
        'default_py_value': 'SeasonYearNullable.default',
        'parameter_value': SeasonYearNullable.default,
        'parameter_error_value': 'a',
    },
    'Season': {
        'default_py_value': 'Season.default',
        'parameter_value': Season.default,
        'parameter_error_value': 'a',
    },
    'SeasonNullable': {
        'default_py_value': 'SeasonNullable.default',
        'parameter_value': SeasonNullable.default,
        'parameter_error_value': 'a',
    },
    'SeasonAll': {
        'default_py_value': 'SeasonAll.default',
        'parameter_value': SeasonAll.default,
        'parameter_error_value': 'a',
    },
    'SeasonAllNullable': {
        'default_py_value': 'SeasonAllNullable.default',
        'parameter_value': SeasonAllNullable.default,
        'parameter_error_value': 'a',
    },
    'SeasonAll_Time': {
        'default_py_value': 'SeasonAll_Time.default',
        'parameter_value': SeasonAll_Time.default,
        'parameter_error_value': 'a',
    },
    'SeasonAllTime': {
        'default_py_value': 'SeasonAllTime.default',
        'parameter_value': SeasonAllTime.default,
        'parameter_error_value': 'a',
    },
    'GraphStartSeason': {
        'default_py_value': 'Season.default',
        'parameter_value': Season.default,
        'parameter_error_value': 'a',
    },
    'GraphStartSeasonNullable': {
        'default_py_value': 'SeasonNullable.default',
        'parameter_value': SeasonNullable.default,
        'parameter_error_value': 'a',
    },
    'GraphEndSeason': {
        'default_py_value': 'Season.default',
        'parameter_value': Season.default,
        'parameter_error_value': 'a',
    },
    'GraphEndSeasonNullable': {
        'default_py_value': 'SeasonNullable.default',
        'parameter_value': SeasonNullable.default,
        'parameter_error_value': 'a',
    },
    'RookieYear': {
        'default_py_value': 'Season.default',
        'parameter_value': Season.default,
        'parameter_error_value': 'a',
    },
    'RookieYearNullable': {
        'default_py_value': 'SeasonNullable.default',
        'parameter_value': SeasonNullable.default,
        'parameter_error_value': 'a',
    },
    'SeasonID': {
        'default_py_value': 'SeasonID.default',
        'parameter_value': SeasonID.default,
        'parameter_error_value': 'a',
    },
    'SeasonIDNullable': {
        'default_py_value': "''",
        'parameter_value': SeasonID.default,
        'parameter_error_value': 'a',
    },
    'Person1SeasonType': {
        'default_py_value': 'SeasonType.default',
        'parameter_value': SeasonType.default,
        'parameter_error_value': 'a',
    },
    'Person2SeasonType': {
        'default_py_value': 'SeasonType.default',
        'parameter_value': SeasonType.default,
        'parameter_error_value': 'a',
    },
    'SeasonType': {
        'default_py_value': 'SeasonType.default',
        'parameter_value': SeasonType.default,
        'parameter_error_value': 'a',
    },
    'SeasonTypePlayoffs': {
        'default_py_value': 'SeasonType.default',
        'parameter_value': SeasonType.default,
        'parameter_error_value': 'a',
    },
    'SeasonTypeNullable': {
        'default_py_value': 'SeasonTypeNullable.default',
        'parameter_value': SeasonTypeNullable.default,
        'parameter_error_value': 'a',
    },
    'SeasonTypeAllStar': {
        'default_py_value': 'SeasonTypeAllStar.default',
        'parameter_value': SeasonTypeAllStar.default,
        'parameter_error_value': 'a',
    },
    'SeasonTypeAllStarNullable': {
        'default_py_value': 'SeasonTypeAllStarNullable.default',
        'parameter_value': SeasonTypeAllStarNullable.default,
        'parameter_error_value': 'a',
    },
    'SeasonSegment': {
        'default_py_value': 'SeasonSegment.default',
        'parameter_value': SeasonSegment.default,
        'parameter_error_value': 'a',
    },
    'SeasonSegmentNullable': {
        'default_py_value': 'SeasonSegmentNullable.default',
        'parameter_value': SeasonSegmentNullable.default,
        'parameter_error_value': 'a',
    },
    'IsOnlyCurrentSeason': {
        'default_py_value': 0,
        'parameter_value': '0',
        'parameter_error_value': 'a',
    },
    'SeriesIDNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'ShotClockRangeNullable': {
        'default_py_value': 'ShotClockRangeNullable.default',
        'parameter_value': ShotClockRangeNullable.default,
        'parameter_error_value': 'a',
    },
    'ShotDistRangeNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'StarterBench': {
        'default_py_value': 'StarterBench.default',
        'parameter_value': StarterBench.default,
        'parameter_error_value': 0,
    },
    'StarterBenchNullable': {
        'default_py_value': 'StarterBenchNullable.default',
        'parameter_value': StarterBenchNullable.default,
        'parameter_error_value': 0,
    },
    'Stat': {
        'default_py_value': 'Stat.default',
        'parameter_value': Stat.default,
        'parameter_error_value': 0,
    },
    'StatCategory': {
        'default_py_value': 'StatCategory.default',
        'parameter_value': StatCategory.default,
        'parameter_error_value': 0,
    },
    'StatCategoryAbbreviation': {
        'default_py_value': 'StatCategoryAbbreviation.default',
        'parameter_value': StatCategoryAbbreviation.default,
        'parameter_error_value': 0,
    },
    'StatType': {
        'default_py_value': 'StatType.default',
        'parameter_value': StatType.default,
        'parameter_error_value': 0,
    },
    'TopX': {
        'default_py_value': '10',
        'parameter_value': 10,
        'parameter_error_value': 'a',
    },
    'TopXNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'TouchTimeRangeNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'TypeGrouping': {
        'default_py_value': 'TypeGrouping.default',
        'parameter_value': TypeGrouping.default,
        'parameter_error_value': 0,
    },
    'TypeGroupingNullable': {
        'default_py_value': 'TypeGroupingNullable.default',
        'parameter_value': TypeGroupingNullable.default,
        'parameter_error_value': 0,
    },
    'WeightNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtPTSNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtREBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtASTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtSTLNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtBLKNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtOREBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtDREBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtDDNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtTDNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtMINUTESNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtTOVNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtPFNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtFGMNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtFGANullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtFG_PCTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtFTMNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtFTANullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtFT_PCTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtFG3MNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtFG3ANullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtFG3_PCTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtPTSNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtREBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtASTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtSTLNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtBLKNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtOREBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtDREBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtDDNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtTDNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtMINUTESNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtTOVNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtPFNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtFGMNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtFGANullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtFG_PCTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtFTMNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtFTANullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtFT_PCTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtFG3MNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtFG3ANullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtFG3_PCTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqPTSNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqREBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqASTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqSTLNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqBLKNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqOREBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqDREBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqDDNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqTDNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqMINUTESNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqTOVNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqPFNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqFGMNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqFGANullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqFG_PCTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqFTMNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqFTANullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqFT_PCTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqFG3MNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqFG3ANullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqFG3_PCTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },'GtOPPPTSOFFTOVNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtOPPTOVNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqOPPPTS2NDCHANCENullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtOPPPTSPAINTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'ActiveStreaksOnlyNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtOPPFG3ANullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'WrsOPPBLKNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtPTS2NDCHANCENullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtOPPSTLNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtOPPFTANullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtOPPFG_PCTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtPTS2NDCHANCENullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'BtrOPPDREBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'BtrOPPPTSPAINTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtOPPPTS2NDCHANCENullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtOPPASTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtOPPOREBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'BtrOPPBLKNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtPTSOFFTOVNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtOPPFGMNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'WrsOPPPTS2NDCHANCENullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'BtrOPPFG3MNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'WrsOPPPTSOFFTOVNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'BtrOPPOREBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtOPPFT_PCTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'BtrOPPSTLNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtOPPASTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'BtrOPPREBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtOPPPTSNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'WrsOPPASTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'WrsOPPOREBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'BtrOPPPTSFBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'WrsOPPFG3PCTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtOPPFG_PCTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'WrsOPPPFNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtOPPFTANullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'BtrOPPFGANullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'WrsOPPPTSPAINTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtPTSOFFTOVNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtOPPPTS2NDCHANCENullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'BtrOPPFG3PCTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtPTSFBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtOPPREBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtOPPPFNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtOPPDREBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'WrsOPPFGMNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtOPPBLKNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtOPPFGANullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'WrsOPPFG_PCTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'WrsOPPFG3MNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'BtrOPPTOVNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'BtrOPPFTANullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqPTSPAINTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtOPPBLKNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'BtrOPPFT_PCTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtOPPPTSFBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtOPPSTLNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtOPPDREBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'ActiveTeamsOnlyNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'BtrOPPPTSNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'WrsOPPDREBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtOPPPTSPAINTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtOPPFTMNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'WrsOPPFTMNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqPTSOFFTOVNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqOPPPTSFBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'BtrOPPASTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'MinGamesNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'MinutesMin': {
        'default_py_value': None,
        'parameter_value': '10',
        'parameter_error_value': 'a',
    },
    'LtOPPFG3MNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'WrsOPPPTSNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'WrsOPPREBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'WrsOPPSTLNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtPTSPAINTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'BtrOPPFG3ANullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'WrsOPPFT_PCTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'WrsOPPPTSFBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqOPPPTSPAINTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtOPPFTMNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtOPPPTSFBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtOPPFT_PCTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtOPPFG3ANullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtPTSPAINTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'WrsOPPTOVNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'BtrOPPPFNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'BtrOPPPTS2NDCHANCENullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtOPPPFNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'WrsOPPFTANullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtOPPFGMNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtOPPFG3PCTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtOPPREBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'WStreakNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'BtrOPPFTMNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtOPPFGANullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtOPPPTSOFFTOVNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqPTS2NDCHANCENullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'WrsOPPFG3ANullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'BtrOPPFGMNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtOPPOREBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtOPPPTSNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LtOPPTOVNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'WrsOPPFGANullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtPTSFBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'BtrOPPFG_PCTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqOPPPTSOFFTOVNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtOPPFG3PCTNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'EqPTSFBNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'BtrOPPPTSOFFTOVNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'LStreakNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'GtOPPFG3MNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'DraftNumberNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'YearsExperienceNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'DraftTeamIDNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'DraftRoundNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
    'TwoWayNullable': {
        'default_py_value': "''",
        'parameter_value': '',
        'parameter_error_value': 'a',
    },
}

parameter_map = {
    'ActiveFlag': {
        'nullable': {
            None: 'ActiveFlagNullable'
        },
        'non-nullable': {

        }
    },
    'AheadBehind': {
        'nullable': {
            '^((Ahead or Behind)|(Ahead or Tied)|(Behind or Tied))?$': 'AheadBehindNullable',
            None: 'AheadBehindNullable'
        },
        'non-nullable': {
            '^((Ahead or Behind)|(Behind or Tied)|(Ahead or Tied))?$': 'AheadBehind'
        }
    },
    'CloseDefDistRange': {
        'nullable': {
            None: 'CloseDefDistRangeNullable'
        },
        'non-nullable': {

        }
    },
    'ClutchTime': {
        'nullable': {
            '^((Last 5 Minutes)|(Last 4 Minutes)|(Last 3 Minutes)|(Last 2 Minutes)|(Last 1 Minute)|(Last 30 Seconds)|(Last 10 Seconds))?$': 'ClutchTimeNullable',
            None: 'ClutchTimeNullable'
        },
        'non-nullable': {
            '^((Last 5 Minutes)|(Last 4 Minutes)|(Last 3 Minutes)|(Last 2 Minutes)|(Last 1 Minute)|(Last 30 Seconds)|(Last 10 Seconds))?$': 'ClutchTime'
        }
    },
    'College': {
        'nullable': {
            None: 'CollegeNullable'
        },
        'non-nullable': {
            None: 'College'
        }
    },
    'School': {
        'nullable': {

        },
        'non-nullable': {
            None: 'College'
        }
    },
    'Conference': {
        'nullable': {
            '((East)|(West))?': 'ConferenceNullable',
            '^((East)|(West))?$': 'ConferenceNullable',
            None: 'ConferenceNullable'
        },
        'non-nullable': {

        }
    },
    'ContextFilter': {
        'nullable': {
            None: 'ContextFilterNullable'
        },
        'non-nullable': {

        }
    },
    'ContextMeasure': {
        'nullable': {
            '^((PTS)|(FGM)|(FGA)|(FG_PCT)|(FG3M)|(FG3A)|(FG3_PCT)|(PF)|(EFG_PCT)|(TS_PCT)|(PTS_FB)|(PTS_OFF_TOV)|(PTS_2ND_CHANCE)|(PF))?$': 'ContextMeasureSimpleNullable'
        },
        'non-nullable': {
            '^((PTS)|(FGM)|(FGA)|(FG_PCT)|(FG3M)|(FG3A)|(FG3_PCT)|(PF)|(EFG_PCT)|(TS_PCT)|(PTS_FB)|(PTS_OFF_TOV)|(PTS_2ND_CHANCE)|(PF))?$': 'ContextMeasureSimple',
            '^((PTS)|(FGM)|(FGA)|(FG_PCT)|(FG3M)|(FG3A)|(FG3_PCT)|(FTM)|(FTA)|(OREB)|(DREB)|(AST)|(FGM_AST)|(FG3_AST)|(STL)|(BLK)|(BLKA)|(TOV)|(POSS_END_FT)|(PTS_PAINT)|(PTS_FB)|(PTS_OFF_TOV)|(PTS_2ND_CHANCE)|(REB)|(TM_FGM)|(TM_FGA)|(TM_FG3M)|(TM_FG3A)|(TM_FTM)|(TM_FTA)|(TM_OREB)|(TM_DREB)|(TM_REB)|(TM_TEAM_REB)|(TM_AST)|(TM_STL)|(TM_BLK)|(TM_BLKA)|(TM_TOV)|(TM_TEAM_TOV)|(TM_PF)|(TM_PFD)|(TM_PTS)|(TM_PTS_PAINT)|(TM_PTS_FB)|(TM_PTS_OFF_TOV)|(TM_PTS_2ND_CHANCE)|(TM_FGM_AST)|(TM_FG3_AST)|(TM_POSS_END_FT)|(OPP_FTM)|(OPP_FTA)|(OPP_OREB)|(OPP_DREB)|(OPP_REB)|(OPP_TEAM_REB)|(OPP_AST)|(OPP_STL)|(OPP_BLK)|(OPP_BLKA)|(OPP_TOV)|(OPP_TEAM_TOV)|(OPP_PF)|(OPP_PFD)|(OPP_PTS)|(OPP_PTS_PAINT)|(OPP_PTS_FB)|(OPP_PTS_OFF_TOV)|(OPP_PTS_2ND_CHANCE)|(OPP_FGM_AST)|(OPP_FG3_AST)|(OPP_POSS_END_FT)|(PTS))$': 'ContextMeasureDetailed',
            '^((FGM)|(FGA)|(FG_PCT)|(FG3M)|(FG3A)|(FG3_PCT)|(FTM)|(FTA)|(OREB)|(DREB)|(AST)|(FGM_AST)|(FG3_AST)|(STL)|(BLK)|(BLKA)|(TOV)|(PF)|(PFD)|(POSS_END_FT)|(PTS_PAINT)|(PTS_FB)|(PTS_OFF_TOV)|(PTS_2ND_CHANCE)|(REB)|(TM_FGM)|(TM_FGA)|(TM_FG3M)|(TM_FG3A)|(TM_FTM)|(TM_FTA)|(TM_OREB)|(TM_DREB)|(TM_REB)|(TM_TEAM_REB)|(TM_AST)|(TM_STL)|(TM_BLK)|(TM_BLKA)|(TM_TOV)|(TM_TEAM_TOV)|(TM_PF)|(TM_PFD)|(TM_PTS)|(TM_PTS_PAINT)|(TM_PTS_FB)|(TM_PTS_OFF_TOV)|(TM_PTS_2ND_CHANCE)|(TM_FGM_AST)|(TM_FG3_AST)|(TM_POSS_END_FT)|(OPP_FGM)|(OPP_FGA)|(OPP_FG3M)|(OPP_FG3A)|(OPP_FTM)|(OPP_FTA)|(OPP_OREB)|(OPP_DREB)|(OPP_REB)|(OPP_TEAM_REB)|(OPP_AST)|(OPP_STL)|(OPP_BLK)|(OPP_BLKA)|(OPP_TOV)|(OPP_TEAM_TOV)|(OPP_PF)|(OPP_PFD)|(OPP_PTS)|(OPP_PTS_PAINT)|(OPP_PTS_FB)|(OPP_PTS_OFF_TOV)|(OPP_PTS_2ND_CHANCE)|(OPP_FGM_AST)|(OPP_FG3_AST)|(OPP_POSS_END_FT)|(PTS))$': 'ContextMeasureDetailed'
        }
    },
    'Counter': {
        'nullable': {
            None: 'CounterNullable',
        },
        'non-nullable': {
            None: 'Counter'
        }
    },
    'Country': {
        'nullable': {
            None: 'CountryNullable'
        },
        'non-nullable': {

        }
    },
    'DateFrom': {
        'nullable': {
            None: 'DateFromNullable'
        },
        'non-nullable': {

        }
    },
    'DateTo': {
        'nullable': {
            None: 'DateToNullable'
        },
        'non-nullable': {

        }
    },
    'DayOffset': {
        'nullable': {

        },
        'non-nullable': {
            '^-{0,1}\\d+$': 'DayOffset'
        }
    },
    'DefenseCategory': {
        'nullable': {
            '^((Overall)|(3 Pointers)|(2 Pointers)|(Less Than 6Ft)|(Less Than 10Ft)|(Greater Than 15Ft))?$': 'DefenseCategoryNullable'
        },
        'non-nullable': {
            '^((Overall)|(3 Pointers)|(2 Pointers)|(Less Than 6Ft)|(Less Than 10Ft)|(Greater Than 15Ft))?$': 'DefenseCategory'
        }
    },
    'Direction': {
        'nullable': {

        },
        'non-nullable': {
            '^(ASC)|(DESC)$': 'Direction'
        }
    },
    'DistanceRange': {
        'nullable': {

        },
        'non-nullable': {
            '^(5ft Range)|(8ft Range)|(By Zone)$': 'DistanceRange'
        }
    },
    'Division': {
        'nullable': {
            None: 'DivisionSimpleNullable',
            '((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest))?': 'DivisionSimpleNullable',
            '^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$': 'DivisionNullable'
        },
        'non-nullable': {

        }
    },
    'DraftPick': {
        'nullable': {
            None: 'DraftPickNullable'
        },
        'non-nullable': {

        }
    },
    'DraftYear': {
        'nullable': {
            None: 'DraftYearNullable'
        },
        'non-nullable': {

        }
    },
    'DribbleRange': {
        'nullable': {
            None: 'DribbleRangeNullable'
        },
        'non-nullable': {

        }
    },
    'EastPlayer1': {
        'nullable': {

        },
        'non-nullable': {
            None: 'EastPlayer1'
        }
    },
    'EastPlayer2': {
        'nullable': {

        },
        'non-nullable': {
            None: 'EastPlayer2'
        }
    },
    'EastPlayer3': {
        'nullable': {

        },
        'non-nullable': {
            None: 'EastPlayer3'
        }
    },
    'EastPlayer4': {
        'nullable': {

        },
        'non-nullable': {
            None: 'EastPlayer4'
        }
    },
    'EastPlayer5': {
        'nullable': {

        },
        'non-nullable': {
            None: 'EastPlayer5'
        }
    },
    'EndPeriod': {
        'nullable': {
            None: 'EndPeriodNullable'
        },
        'non-nullable': {
            None: 'EndPeriod'
        }
    },
    'EndRange': {
        'nullable': {
            None: 'EndRangeNullable'
        },
        'non-nullable': {
            None: 'EndRange'
        }
    },
    'GROUP_ID': {
        'nullable': {

        },
        'non-nullable': {
            '^\\d+(( - \\d+){2,4})?$': 'GroupID'
        }
    },
    'GameDate': {
        'nullable': {

        },
        'non-nullable': {
            None: 'GameDate'
        }
    },
    'GameEventID': {
        'nullable': {

        },
        'non-nullable': {
            None: 'GameEventID'
        }
    },
    'GameID': {
        'nullable': {
            '^(\\d{10})?$': 'GameIDNullable',
            None: 'GameIDNullable'
        },
        'non-nullable': {
            '^(\\d{10})?$': 'GameID',
            '^\\d{10}$': 'GameID',
            None: 'GameID'
        }
    },
    'GameIDs': {
        'nullable': {

        },
        'non-nullable': {
            None: 'GameIDs'
        }
    },
    'GameScope': {
        'nullable': {
            '((Yesterday)|(Last 10))?': 'GameScopeSimpleNullable'
        },
        'non-nullable': {
            '^(Season)|(Last 10)|(Yesterday)|(Finals)$': 'GameScopeDetailed'
        }
    },
    'GameSegment': {
        'nullable': {
            '^((First Half)|(Overtime)|(Second Half))?$': 'GameSegmentNullable',
            None: 'GameSegmentNullable'
        },
        'non-nullable': {

        }
    },
    'GeneralRange': {
        'nullable': {
            None: 'GeneralRangeNullable'
        },
        'non-nullable': {

        }
    },
    'GraphEndSeason': {
        'nullable': {
            '^(\\d{4}-\\d{2})?$': 'GraphEndSeasonNullable'
        },
        'non-nullable': {

        }
    },
    'GraphStartSeason': {
        'nullable': {
            '^(\\d{4}-\\d{2})?$': 'GraphStartSeasonNullable'
        },
        'non-nullable': {

        }
    },
    'GraphStat': {
        'nullable': {
            None: 'GraphStatNullable'
        },
        'non-nullable': {

        }
    },
    'GroupQuantity': {
        'nullable': {

        },
        'non-nullable': {
            None: 'GroupQuantity'
        }
    },
    'Height': {
        'nullable': {
            None: 'HeightNullable'
        },
        'non-nullable': {

        }
    },
    'IsOnlyCurrentSeason': {
        'nullable': {
            None: 'IsOnlyCurrentSeason'
        },
        'non-nullable': {
            None: 'IsOnlyCurrentSeason'
        }
    },
    'LastNGames': {
        'nullable': {
            None: 'LastNGamesNullable'
        },
        'non-nullable': {
            None: 'LastNGames'
        }
    },
    'Person1LeagueId': {
        'nullable': {

        },
        'non-nullable': {
            None: 'Person1LeagueID'
        }
    },
    'Person2LeagueId': {
        'nullable': {

        },
        'non-nullable': {
            None: 'Person2LeagueID'
        }
    },
    'LeagueID': {
        'nullable': {
            '(00)|(20)|(10)': 'LeagueIDNullable',
            '^((00)|(20))?$': 'LeagueIDNullable',
            '^\\d{2}$': 'LeagueIDNullable',
            None: 'LeagueIDNullable'
        },
        'non-nullable': {
            '^\\d{2}$': 'LeagueID',
            '^(00)|(10)|(20)$': 'LeagueID',
            '(00)|(20)|(10)': 'LeagueID',
            '^(00)|(20)$': 'LeagueID',
            '^((00)|(20))?$': 'LeagueID',
            '^(00)|(20)|(10)$': 'LeagueID',
            None: 'LeagueID'
        }
    },
    'Location': {
        'nullable': {
            '^((Home)|(Road))?$': 'LocationNullable',
            None: 'LocationNullable'
        },
        'non-nullable': {

        }
    },
    'MeasureType': {
        'nullable': {
            None: 'MeasureTypePlayerGameLogsNullable',
        },
        'non-nullable': {
            '^(Base)$': 'MeasureTypeBase',
            '^(Base)|(Opponent)$': 'MeasureTypeSimple',
            '^(Base)|(Advanced)|(Misc)|(Four Factors)|(Scoring)|(Opponent)|(Usage)$': 'MeasureTypeDetailed',
            '^(Base)|(Advanced)|(Misc)|(Four Factors)|(Scoring)|(Opponent)|(Usage)|(Defense)$': 'MeasureTypeDetailedDefense'
        }
    },
    'Month': {
        'nullable': {
            None: 'MonthNullable'
        },
        'non-nullable': {
            None: 'Month'
        }
    },
    'NumberOfGames': {
        'nullable': {

        },
        'non-nullable': {
            None: 'NumberOfGames'
        }
    },
    'OppTeamID': {
        'nullable': {
            None: 'OppTeamIDNullable'
        },
        'non-nullable': {
        }
    },
    'OpponentTeamID': {
        'nullable': {
            None: 'OpponentTeamIDNullable'
        },
        'non-nullable': {
            None: 'OpponentTeamID'
        }
    },
    'Outcome': {
        'nullable': {
            '^((W)|(L))?$': 'OutcomeNullable',
            None: 'OutcomeNullable'
        },
        'non-nullable': {

        }
    },
    'OverallPick': {
        'nullable': {
            None: 'OverallPickNullable'
        },
        'non-nullable': {

        }
    },
    'PORound': {
        'nullable': {
            None: 'PORoundNullable'
        },
        'non-nullable': {

        }
    },
    'PaceAdjust': {
        'nullable': {

        },
        'non-nullable': {
            '^(N)$': 'PaceAdjustNo',
            '^(Y)|(N)$': 'PaceAdjust'
        }
    },
    'PerMode': {
        'nullable': {
            '^(Totals)|(PerGame)$': 'PerModeSimpleNullable',
            None: 'PerModeSimpleNullable'
        },
        'non-nullable': {
            None: 'PerModeSimple',
            '^(Totals)|(PerGame)$': 'PerModeSimple',
            '^(Totals)|(PerGame)|(Per36)$': 'PerMode36',
            '^(Totals)|(PerGame)|(Per48)$': 'PerMode48',
            '^(Totals)|(PerGame)|(Per48)|(Per40)|(Per36)|(PerMinute)$': 'PerModeTime',
            '^(Totals)|(PerGame)|(MinutesPer)|(Per48)|(Per40)|(Per36)|(PerMinute)|(PerPossession)|(PerPlay)|(Per100Possessions)|(Per100Plays)$': 'PerModeDetailed'
        }
    },
    'Period': {
        'nullable': {
            None: 'PeriodNullable'
        },
        'non-nullable': {
            None: 'Period'
        }
    },
    'PlayerExperience': {
        'nullable': {
            '((Rookie)|(Sophomore)|(Veteran))?': 'PlayerExperienceNullable',
            None: 'PlayerExperienceNullable'
        },
        'non-nullable': {

        }
    },
    'ActivePlayers': {
        'nullable': {

        },
        'non-nullable': {
            '^(Y)|(N)$': 'ActivePlayers'
        }
    },
    'TodaysPlayers': {
        'nullable': {

        },
        'non-nullable': {
            '^(Y)|(N)$': 'TodaysPlayers'
        }
    },
    'PlayerID': {
        'nullable': {
            None: 'PlayerIDNullable'
        },
        'non-nullable': {
            None: 'PlayerID'
        }
    },
    'Person1Id': {
        'nullable': {

        },
        'non-nullable': {
            None: 'Person1ID'
        }
    },
    'Person2Id': {
        'nullable': {

        },
        'non-nullable': {
            None: 'Person2ID'
        }
    },
    'PlayerID1': {
        'nullable': {

        },
        'non-nullable': {
            None: 'PlayerID1'
        }
    },
    'PlayerID2': {
        'nullable': {

        },
        'non-nullable': {
            None: 'PlayerID2'
        }
    },
    'PlayerID3': {
        'nullable': {

        },
        'non-nullable': {
            None: 'PlayerID3'
        }
    },
    'PlayerID4': {
        'nullable': {

        },
        'non-nullable': {
            None: 'PlayerID4'
        }
    },
    'PlayerID5': {
        'nullable': {

        },
        'non-nullable': {
            None: 'PlayerID5'
        }
    },
    'DefPlayerID': {
        'nullable': {
            None: 'DefPlayerIDNullable'
        },
        'non-nullable': {

        }
    },
    'OffPlayerID': {
        'nullable': {
            None: 'OffPlayerIDNullable'
        },
        'non-nullable': {

        }
    },
    'PlayerIDList': {
        'nullable': {

        },
        'non-nullable': {
            None: 'PlayerIDList'
        }
    },
    'PlayerOrTeam': {
        'nullable': {

        },
        'non-nullable': {
            '^(Player)|(Team)$': 'PlayerOrTeam',
            '^(P)|(T)$': 'PlayerOrTeamAbbreviation'
        }
    },
    'PlayerPosition': {
        'nullable': {
            '((F)|(C)|(G)|(C-F)|(F-C)|(F-G)|(G-F))?': 'PlayerPositionAbbreviationNullable',
            '^((Guard)|(Center)|(Forward))?$': 'PlayerPositionNullable',
            None: 'PlayerPositionNullable'
        },
        'non-nullable': {

        }
    },
    'PlayerScope': {
        'nullable': {

        },
        'non-nullable': {
            '^(All Players)|(Rookies)$': 'PlayerScope'
        }
    },
    'PlayerTeamID': {
        'nullable': {

        },
        'non-nullable': {
            None: 'PlayerTeamID'
        }
    },
    'PlayType': {
        'nullable': {
            None: 'PlayTypeNullable',
        },
        'non-nullable': {

        }
    },
    'PlusMinus': {
        'nullable': {

        },
        'non-nullable': {
            '^(N)$': 'PlusMinusNo',
            '^(Y)|(N)$': 'PlusMinus'
        }
    },
    'PointDiff': {
        'nullable': {
            None: 'PointDiffNullable'
        },
        'non-nullable': {
            None: 'PointDiff'
        }
    },
    'Position': {
        'nullable': {
            None: 'PositionNullable',
            '^(Guard|Forward|Center)?$': 'PositionNullable'
        },
        'non-nullable': {

        }
    },
    'PtMeasureType': {
        'nullable': {
        },
        'non-nullable': {
            '^(SpeedDistance)|(Rebounding)|(Possessions)|(CatchShoot)|(PullUpShot)|(Defense)|(Drives)|(Passing)|(ElbowTouch)|(PostTouch)|(PaintTouch)|(Efficiency)$': 'PtMeasureType'
        }
    },
    'RangeType': {
        'nullable': {
            None: 'RangeTypeNullable'
        },
        'non-nullable': {
            None: 'RangeType'
        }
    },
    'Rank': {
        'nullable': {

        },
        'non-nullable': {
            '^(N)$': 'RankNo',
            '^(Y)|(N)$': 'Rank'
        }
    },
    'RookieYear': {
        'nullable': {
            '^(\\d{4}-\\d{2})?$': 'RookieYearNullable',
            None: 'RookieYearNullable'
        },
        'non-nullable': {

        }
    },
    'RoundNum': {
        'nullable': {
            None: 'RoundNumNullable'
        },
        'non-nullable': {

        }
    },
    'RoundPick': {
        'nullable': {
            None: 'RoundPickNullable'
        },
        'non-nullable': {

        }
    },
    'RunType': {
        'nullable': {

        },
        'non-nullable': {
            None: 'RunType'
        }
    },
    'Runtype': {
        'nullable': {

        },
        'non-nullable': {
            None: 'RunType'
        }
    },
    'Scope': {
        'nullable': {

        },
        'non-nullable': {
            '^(RS)|(S)|(Rookies)$': 'Scope'
        }
    },
    'Person1Season': {
        'nullable': {

        },
        'non-nullable': {
            None: 'Person1SeasonYear',
        }
    },
    'Person2Season': {
        'nullable': {

        },
        'non-nullable': {
            None: 'Person2SeasonYear',
        }
    },
    'Season': {
        'nullable': {
            '^\\d{4}$': 'SeasonYearNullable',
            '^(\\d{4}-\\d{2})?$': 'SeasonNullable',
            '^(\\d{4}-\\d{2})|(ALL)$': 'SeasonAllNullable',
            None: 'SeasonNullable'
        },
        'non-nullable': {
            None: 'Season',
            '^\\d{4}$': 'SeasonYear',
            '^(\\d{4}-\\d{2})$': 'Season',
            '^\\d{4}-\\d{2}$': 'Season',
            '^(\\d{4}-\\d{2})?$': 'Season',
            '^(\\d{4}-\\d{2})|(All Time)$': 'SeasonAll_Time',
            '^(\\d{4}-\\d{2})|(ALLTIME)$': 'SeasonAllTime',
            '^(\\d{4}-\\d{2})|(ALL)$': 'SeasonAll'
        }
    },
    'SeasonID': {
        'nullable': {
            None: 'SeasonIDNullable',
        },
        'non-nullable': {
            None: 'SeasonID',
            '^\\d{5}$': 'SeasonID'
        }
    },
    'SeasonSegment': {
        'nullable': {
            '^((Post All-Star)|(Pre All-Star))?$': 'SeasonSegmentNullable',
            None: 'SeasonSegmentNullable'
        },
        'non-nullable': {

        }
    },
    'Person1SeasonType': {
        'nullable': {

        },
        'non-nullable': {
            None: 'Person1SeasonType',
        }
    },
    'Person2SeasonType': {
        'nullable': {

        },
        'non-nullable': {
            None: 'Person2SeasonType',
        }
    },
    'SeasonType': {
        'nullable': {
            None: 'SeasonTypeNullable',
            '^(Regular Season)|(Pre Season)|(Playoffs)|(All-Star)|(All Star)|(Preseason)$': 'SeasonTypeAllStarNullable',
            '^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$': 'SeasonTypeAllStarNullable'
        },
        'non-nullable': {
            None: 'SeasonType',
            '^(Regular Season)|(Pre Season)$': 'SeasonType',
            '^(Regular Season)|(Pre Season)|(Playoffs)$': 'SeasonTypePlayoffs',
            '^(Regular Season)|(Pre Season)|(Playoffs)|(Pre-Season)$': 'SeasonTypePlayoffs',
            '^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)$': 'SeasonTypeAllStar',
            '^((Regular Season)|(Pre Season)|(Playoffs)|(All Star))?$': 'SeasonTypeAllStar',
            '^(Regular Season)|(Playoffs)|(All Star)|(Pre Season)$': 'SeasonTypeAllStar',
            '^(Regular Season)|(Pre Season)|(Playoffs)|(All-Star)|(All Star)|(Preseason)$': 'SeasonTypeAllStar',
            '^(Regular Season)|(Pre Season)|(Playoffs)|(All-Star)|(All Star)$': 'SeasonTypeAllStar',
            '^(Regular Season)|(Pre Season)|(Playoffs)|(All Star)|(All-Star)$': 'SeasonTypeAllStar'
        }
    },
    'SeasonYear': {
        'nullable': {
            None: 'SeasonNullable',
        },
        'non-nullable': {
            '^\\d{4}-\\d{2}$': 'Season',
            None: 'SeasonYear',
            '^(\\d{4}-\\d{2})|(All Time)$': 'SeasonAll_Time',
            '^(\\d{4}-\\d{2})|(\\d{4})$': 'Season'
        }
    },
    'SeriesID': {
        'nullable': {
            None: 'SeriesIDNullable'
        },
        'non-nullable': {

        }
    },
    'ShotClockRange': {
        'nullable': {
            '((24-22)|(22-18 Very Early)|(18-15 Early)|(15-7 Average)|(7-4 Late)|(4-0 Very Late)|(ShotClock Off))?': 'ShotClockRangeNullable',
            None: 'ShotClockRangeNullable'
        },
        'non-nullable': {

        }
    },
    'ShotDistRange': {
        'nullable': {
            None: 'ShotDistRangeNullable'
        },
        'non-nullable': {

        }
    },
    'Sorter': {
        'nullable': {

        },
        'non-nullable': {
            '^((FGM)|(FGA)|(FG_PCT)|(FG3M)|(FG3A)|(FG3_PCT)|(FTM)|(FTA)|(FT_PCT)|(OREB)|(DREB)|(AST)|(STL)|(BLK)|(TOV)|(REB)|(PTS)|(DATE))$': 'Sorter'
        }
    },
    'StartPeriod': {
        'nullable': {
            None: 'StartPeriodNullable'
        },
        'non-nullable': {
            None: 'StartPeriod'
        }
    },
    'StartRange': {
        'nullable': {
            None: 'StartRangeNullable'
        },
        'non-nullable': {
            None: 'StartRange'
        }
    },
    'StarterBench': {
        'nullable': {
            '((Starters)|(Bench))?': 'StarterBenchNullable',
            None: 'StarterBenchNullable'
        },
        'non-nullable': {

        }
    },
    'Stat': {
        'nullable': {

        },
        'non-nullable': {
            '^(PTS)|(REB)|(AST)|(FG_PCT)|(FT_PCT)|(FG3_PCT)|(STL)|(BLK)$': 'Stat'
        }
    },
    'StatCategory': {
        'nullable': {

        },
        'non-nullable': {
            None: 'StatCategoryAbbreviation',
            '^(Points)|(Rebounds)|(Assists)|(Defense)|(Clutch)|(Playmaking)|(Efficiency)|(Fast Break)|(Scoring Breakdown)$': 'StatCategory'
        }
    },
    'StatType': {
        'nullable': {

        },
        'non-nullable': {
            '^(Traditional)|(Advanced)|(Tracking)$': 'StatType'
        }
    },
    'DLeagueTeamID': {
        'nullable': {
            None: 'DLeagueTeamIDNullable'
        },
        'non-nullable': {

        }
    },
    'NBATeamID': {
        'nullable': {

        },
        'non-nullable': {
            None: 'TeamID'
        }
    },
    'TeamID': {
        'nullable': {
            None: 'TeamIDNullable'
        },
        'non-nullable': {
            None: 'TeamID'
        }
    },
    'TodaysOpponent': {
        'nullable': {

        },
        'non-nullable': {
            None: 'TodaysOpponent'
        }
    },
    'DefTeamID': {
        'nullable': {
            None: 'DefTeamIDNullable'
        },
        'non-nullable': {
            None: 'DefTeamID'
        }
    },
    'OffTeamID': {
        'nullable': {
            None: 'OffTeamIDNullable'
        },
        'non-nullable': {
            None: 'OffTeamID'
        }
    },
    'TopX': {
        'nullable': {
            None: 'TopXNullable'
        },
        'non-nullable': {
            None: 'TopX'
        }
    },
    'TouchTimeRange': {
        'nullable': {
            None: 'TouchTimeRangeNullable'
        },
        'non-nullable': {

        }
    },
    'TypeGrouping': {
        'nullable': {
            None: 'TypeGroupingNullable',
        },
        'non-nullable': {

        }
    },
    'VsConference': {
        'nullable': {
            '^((East)|(West))?$': 'VsConferenceNullable',
            None: 'VsConferenceNullable'
        },
        'non-nullable': {

        }
    },
    'VsDivision': {
        'nullable': {
            '^((Atlantic)|(Central)|(Northwest)|(Pacific)|(Southeast)|(Southwest)|(East)|(West))?$': 'VsDivisionNullable',
            None: 'VsDivisionNullable'
        },
        'non-nullable': {

        }
    },
    'VsPlayerID': {
        'nullable': {

        },
        'non-nullable': {
            None: 'VsPlayerID'
        }
    },
    'VsPlayerID1': {
        'nullable': {

        },
        'non-nullable': {
            None: 'VsPlayerID1'
        }
    },
    'VsPlayerID2': {
        'nullable': {

        },
        'non-nullable': {
            None: 'VsPlayerID2'
        }
    },
    'VsPlayerID3': {
        'nullable': {

        },
        'non-nullable': {
            None: 'VsPlayerID3'
        }
    },
    'VsPlayerID4': {
        'nullable': {

        },
        'non-nullable': {
            None: 'VsPlayerID4'
        }
    },
    'VsPlayerID5': {
        'nullable': {

        },
        'non-nullable': {
            None: 'VsPlayerID5'
        }
    },
    'VsPlayerIDList': {
        'nullable': {

        },
        'non-nullable': {
            None: 'VsPlayerIDList'
        }
    },
    'VsTeamID': {
        'nullable': {
            None: 'VsTeamIDNullable'
        },
        'non-nullable': {
            None: 'VsTeamID'
        }
    },
    'Weight': {
        'nullable': {
            None: 'WeightNullable'
        },
        'non-nullable': {

        }
    },
    'WestPlayer1': {
        'nullable': {

        },
        'non-nullable': {
            None: 'WestPlayer1'
        }
    },
    'WestPlayer2': {
        'nullable': {

        },
        'non-nullable': {
            None: 'WestPlayer2'
        }
    },
    'WestPlayer3': {
        'nullable': {

        },
        'non-nullable': {
            None: 'WestPlayer3'
        }
    },
    'WestPlayer4': {
        'nullable': {

        },
        'non-nullable': {
            None: 'WestPlayer4'
        }
    },
    'WestPlayer5': {
        'nullable': {

        },
        'non-nullable': {
            None: 'WestPlayer5'
        }
    },
    'GtPTS': {
        'nullable': {
            None: 'GtPTSNullable'
        },
        'non-nullable': {

        }
    },
    'GtREB': {
        'nullable': {
            None: 'GtREBNullable'
        },
        'non-nullable': {

        }
    },
    'GtAST': {
        'nullable': {
            None: 'GtASTNullable'
        },
        'non-nullable': {

        }
    },
    'GtSTL': {
        'nullable': {
            None: 'GtSTLNullable'
        },
        'non-nullable': {

        }
    },
    'GtBLK': {
        'nullable': {
            None: 'GtBLKNullable'
        },
        'non-nullable': {

        }
    },
    'GtOREB': {
        'nullable': {
            None: 'GtOREBNullable'
        },
        'non-nullable': {

        }
    },
    'GtDREB': {
        'nullable': {
            None: 'GtDREBNullable'
        },
        'non-nullable': {

        }
    },
    'GtDD': {
        'nullable': {
            None: 'GtDDNullable'
        },
        'non-nullable': {

        }
    },
    'GtTD': {
        'nullable': {
            None: 'GtTDNullable'
        },
        'non-nullable': {

        }
    },
    'GtMINUTES': {
        'nullable': {
            None: 'GtMINUTESNullable'
        },
        'non-nullable': {

        }
    },
    'GtTOV': {
        'nullable': {
            None: 'GtTOVNullable'
        },
        'non-nullable': {

        }
    },
    'GtPF': {
        'nullable': {
            None: 'GtPFNullable'
        },
        'non-nullable': {

        }
    },
    'GtFGM': {
        'nullable': {
            None: 'GtFGMNullable'
        },
        'non-nullable': {

        }
    },
    'GtFGA': {
        'nullable': {
            None: 'GtFGANullable'
        },
        'non-nullable': {

        }
    },
    'GtFG_PCT': {
        'nullable': {
            None: 'GtFG_PCTNullable'
        },
        'non-nullable': {

        }
    },
    'GtFTM': {
        'nullable': {
            None: 'GtFTMNullable'
        },
        'non-nullable': {

        }
    },
    'GtFTA': {
        'nullable': {
            None: 'GtFTANullable'
        },
        'non-nullable': {

        }
    },
    'GtFT_PCT': {
        'nullable': {
            None: 'GtFT_PCTNullable'
        },
        'non-nullable': {

        }
    },
    'GtFG3M': {
        'nullable': {
            None: 'GtFG3MNullable'
        },
        'non-nullable': {

        }
    },
    'GtFG3A': {
        'nullable': {
            None: 'GtFG3ANullable'
        },
        'non-nullable': {

        }
    },
    'GtFG3_PCT': {
        'nullable': {
            None: 'GtFG3_PCTNullable'
        },
        'non-nullable': {

        }
    },
    'LtPTS': {
        'nullable': {
            None: 'LtPTSNullable'
        },
        'non-nullable': {

        }
    },
    'LtREB': {
        'nullable': {
            None: 'LtREBNullable'
        },
        'non-nullable': {

        }
    },
    'LtAST': {
        'nullable': {
            None: 'LtASTNullable'
        },
        'non-nullable': {

        }
    },
    'LtSTL': {
        'nullable': {
            None: 'LtSTLNullable'
        },
        'non-nullable': {

        }
    },
    'LtBLK': {
        'nullable': {
            None: 'LtBLKNullable'
        },
        'non-nullable': {

        }
    },
    'LtOREB': {
        'nullable': {
            None: 'LtOREBNullable'
        },
        'non-nullable': {

        }
    },
    'LtDREB': {
        'nullable': {
            None: 'LtDREBNullable'
        },
        'non-nullable': {

        }
    },
    'LtDD': {
        'nullable': {
            None: 'LtDDNullable'
        },
        'non-nullable': {

        }
    },
    'LtTD': {
        'nullable': {
            None: 'LtTDNullable'
        },
        'non-nullable': {

        }
    },
    'LtMINUTES': {
        'nullable': {
            None: 'LtMINUTESNullable'
        },
        'non-nullable': {

        }
    },
    'LtTOV': {
        'nullable': {
            None: 'LtTOVNullable'
        },
        'non-nullable': {

        }
    },
    'LtPF': {
        'nullable': {
            None: 'LtPFNullable'
        },
        'non-nullable': {

        }
    },
    'LtFGM': {
        'nullable': {
            None: 'LtFGMNullable'
        },
        'non-nullable': {

        }
    },
    'LtFGA': {
        'nullable': {
            None: 'LtFGANullable'
        },
        'non-nullable': {

        }
    },
    'LtFG_PCT': {
        'nullable': {
            None: 'LtFG_PCTNullable'
        },
        'non-nullable': {

        }
    },
    'LtFTM': {
        'nullable': {
            None: 'LtFTMNullable'
        },
        'non-nullable': {

        }
    },
    'LtFTA': {
        'nullable': {
            None: 'LtFTANullable'
        },
        'non-nullable': {

        }
    },
    'LtFT_PCT': {
        'nullable': {
            None: 'LtFT_PCTNullable'
        },
        'non-nullable': {

        }
    },
    'LtFG3M': {
        'nullable': {
            None: 'LtFG3MNullable'
        },
        'non-nullable': {

        }
    },
    'LtFG3A': {
        'nullable': {
            None: 'LtFG3ANullable'
        },
        'non-nullable': {

        }
    },
    'LtFG3_PCT': {
        'nullable': {
            None: 'LtFG3_PCTNullable'
        },
        'non-nullable': {

        }
    },
    'EqPTS': {
        'nullable': {
            None: 'EqPTSNullable'
        },
        'non-nullable': {

        }
    },
    'EqREB': {
        'nullable': {
            None: 'EqREBNullable'
        },
        'non-nullable': {

        }
    },
    'EqAST': {
        'nullable': {
            None: 'EqASTNullable'
        },
        'non-nullable': {

        }
    },
    'EqSTL': {
        'nullable': {
            None: 'EqSTLNullable'
        },
        'non-nullable': {

        }
    },
    'EqBLK': {
        'nullable': {
            None: 'EqBLKNullable'
        },
        'non-nullable': {

        }
    },
    'EqOREB': {
        'nullable': {
            None: 'EqOREBNullable'
        },
        'non-nullable': {

        }
    },
    'EqDREB': {
        'nullable': {
            None: 'EqDREBNullable'
        },
        'non-nullable': {

        }
    },
    'EqDD': {
        'nullable': {
            None: 'EqDDNullable'
        },
        'non-nullable': {

        }
    },
    'EqTD': {
        'nullable': {
            None: 'EqTDNullable'
        },
        'non-nullable': {

        }
    },
    'EqMINUTES': {
        'nullable': {
            None: 'EqMINUTESNullable'
        },
        'non-nullable': {

        }
    },
    'EqTOV': {
        'nullable': {
            None: 'EqTOVNullable'
        },
        'non-nullable': {

        }
    },
    'EqPF': {
        'nullable': {
            None: 'EqPFNullable'
        },
        'non-nullable': {

        }
    },
    'EqFGM': {
        'nullable': {
            None: 'EqFGMNullable'
        },
        'non-nullable': {

        }
    },
    'EqFGA': {
        'nullable': {
            None: 'EqFGANullable'
        },
        'non-nullable': {

        }
    },
    'EqFG_PCT': {
        'nullable': {
            None: 'EqFG_PCTNullable'
        },
        'non-nullable': {

        }
    },
    'EqFTM': {
        'nullable': {
            None: 'EqFTMNullable'
        },
        'non-nullable': {

        }
    },
    'EqFTA': {
        'nullable': {
            None: 'EqFTANullable'
        },
        'non-nullable': {

        }
    },
    'EqFT_PCT': {
        'nullable': {
            None: 'EqFT_PCTNullable'
        },
        'non-nullable': {

        }
    },
    'EqFG3M': {
        'nullable': {
            None: 'EqFG3MNullable'
        },
        'non-nullable': {

        }
    },
    'EqFG3A': {
        'nullable': {
            None: 'EqFG3ANullable'
        },
        'non-nullable': {

        }
    },
    'EqFG3_PCT': {
        'nullable': {
            None: 'EqFG3_PCTNullable'
        },
        'non-nullable': {

        }
    },
    'GtOPPPTSOFFTOV': {
        'nullable': {
            None: 'GtOPPPTSOFFTOVNullable'
        },
        'non-nullable': {

        }
    },
    'GtOPPTOV': {
        'nullable': {
            None: 'GtOPPTOVNullable'
        },
        'non-nullable': {

        }
    },
    'EqOPPPTS2NDCHANCE': {
        'nullable': {
            None: 'EqOPPPTS2NDCHANCENullable'
        },
        'non-nullable': {

        }
    },
    'GtOPPPTSPAINT': {
        'nullable': {
            None: 'GtOPPPTSPAINTNullable'
        },
        'non-nullable': {

        }
    },
    'ActiveStreaksOnly': {
        'nullable': {
            None: 'ActiveStreaksOnlyNullable'
        },
        'non-nullable': {

        }
    },
    'GtOPPFG3A': {
        'nullable': {
            None: 'GtOPPFG3ANullable'
        },
        'non-nullable': {

        }
    },
    'WrsOPPBLK': {
        'nullable': {
            None: 'WrsOPPBLKNullable'
        },
        'non-nullable': {

        }
    },
    'LtPTS2NDCHANCE': {
        'nullable': {
            None: 'LtPTS2NDCHANCENullable'
        },
        'non-nullable': {

        }
    },
    'LtOPPSTL': {
        'nullable': {
            None: 'LtOPPSTLNullable'
        },
        'non-nullable': {

        }
    },
    'GtOPPFTA': {
        'nullable': {
            None: 'GtOPPFTANullable'
        },
        'non-nullable': {

        }
    },
    'GtOPPFG_PCT': {
        'nullable': {
            None: 'GtOPPFG_PCTNullable'
        },
        'non-nullable': {

        }
    },
    'GtPTS2NDCHANCE': {
        'nullable': {
            None: 'GtPTS2NDCHANCENullable'
        },
        'non-nullable': {

        }
    },
    'BtrOPPDREB': {
        'nullable': {
            None: 'BtrOPPDREBNullable'
        },
        'non-nullable': {

        }
    },
    'BtrOPPPTSPAINT': {
        'nullable': {
            None: 'BtrOPPPTSPAINTNullable'
        },
        'non-nullable': {

        }
    },
    'LtOPPPTS2NDCHANCE': {
        'nullable': {
            None: 'LtOPPPTS2NDCHANCENullable'
        },
        'non-nullable': {

        }
    },
    'GtOPPAST': {
        'nullable': {
            None: 'GtOPPASTNullable'
        },
        'non-nullable': {

        }
    },
    'GtOPPOREB': {
        'nullable': {
            None: 'GtOPPOREBNullable'
        },
        'non-nullable': {

        }
    },
    'BtrOPPBLK': {
        'nullable': {
            None: 'BtrOPPBLKNullable'
        },
        'non-nullable': {

        }
    },
    'LtPTSOFFTOV': {
        'nullable': {
            None: 'LtPTSOFFTOVNullable'
        },
        'non-nullable': {

        }
    },
    'LtOPPFGM': {
        'nullable': {
            None: 'LtOPPFGMNullable'
        },
        'non-nullable': {

        }
    },
    'WrsOPPPTS2NDCHANCE': {
        'nullable': {
            None: 'WrsOPPPTS2NDCHANCENullable'
        },
        'non-nullable': {

        }
    },
    'BtrOPPFG3M': {
        'nullable': {
            None: 'BtrOPPFG3MNullable'
        },
        'non-nullable': {

        }
    },
    'WrsOPPPTSOFFTOV': {
        'nullable': {
            None: 'WrsOPPPTSOFFTOVNullable'
        },
        'non-nullable': {

        }
    },
    'BtrOPPOREB': {
        'nullable': {
            None: 'BtrOPPOREBNullable'
        },
        'non-nullable': {

        }
    },
    'LtOPPFT_PCT': {
        'nullable': {
            None: 'LtOPPFT_PCTNullable'
        },
        'non-nullable': {

        }
    },
    'BtrOPPSTL': {
        'nullable': {
            None: 'BtrOPPSTLNullable'
        },
        'non-nullable': {

        }
    },
    'LtOPPAST': {
        'nullable': {
            None: 'LtOPPASTNullable'
        },
        'non-nullable': {

        }
    },
    'BtrOPPREB': {
        'nullable': {
            None: 'BtrOPPREBNullable'
        },
        'non-nullable': {

        }
    },
    'GtOPPPTS': {
        'nullable': {
            None: 'GtOPPPTSNullable'
        },
        'non-nullable': {

        }
    },
    'WrsOPPAST': {
        'nullable': {
            None: 'WrsOPPASTNullable'
        },
        'non-nullable': {

        }
    },
    'WrsOPPOREB': {
        'nullable': {
            None: 'WrsOPPOREBNullable'
        },
        'non-nullable': {

        }
    },
    'BtrOPPPTSFB': {
        'nullable': {
            None: 'BtrOPPPTSFBNullable'
        },
        'non-nullable': {

        }
    },
    'WrsOPPFG3PCT': {
        'nullable': {
            None: 'WrsOPPFG3PCTNullable'
        },
        'non-nullable': {

        }
    },
    'LtOPPFG_PCT': {
        'nullable': {
            None: 'LtOPPFG_PCTNullable'
        },
        'non-nullable': {

        }
    },
    'WrsOPPPF': {
        'nullable': {
            None: 'WrsOPPPFNullable'
        },
        'non-nullable': {

        }
    },
    'LtOPPFTA': {
        'nullable': {
            None: 'LtOPPFTANullable'
        },
        'non-nullable': {

        }
    },
    'BtrOPPFGA': {
        'nullable': {
            None: 'BtrOPPFGANullable'
        },
        'non-nullable': {

        }
    },
    'WrsOPPPTSPAINT': {
        'nullable': {
            None: 'WrsOPPPTSPAINTNullable'
        },
        'non-nullable': {

        }
    },
    'GtPTSOFFTOV': {
        'nullable': {
            None: 'GtPTSOFFTOVNullable'
        },
        'non-nullable': {

        }
    },
    'GtOPPPTS2NDCHANCE': {
        'nullable': {
            None: 'GtOPPPTS2NDCHANCENullable'
        },
        'non-nullable': {

        }
    },
    'BtrOPPFG3PCT': {
        'nullable': {
            None: 'BtrOPPFG3PCTNullable'
        },
        'non-nullable': {

        }
    },
    'LtPTSFB': {
        'nullable': {
            None: 'LtPTSFBNullable'
        },
        'non-nullable': {

        }
    },
    'GtOPPREB': {
        'nullable': {
            None: 'GtOPPREBNullable'
        },
        'non-nullable': {

        }
    },
    'LtOPPPF': {
        'nullable': {
            None: 'LtOPPPFNullable'
        },
        'non-nullable': {

        }
    },
    'LtOPPDREB': {
        'nullable': {
            None: 'LtOPPDREBNullable'
        },
        'non-nullable': {

        }
    },
    'WrsOPPFGM': {
        'nullable': {
            None: 'WrsOPPFGMNullable'
        },
        'non-nullable': {

        }
    },
    'GtOPPBLK': {
        'nullable': {
            None: 'GtOPPBLKNullable'
        },
        'non-nullable': {

        }
    },
    'GtOPPFGA': {
        'nullable': {
            None: 'GtOPPFGANullable'
        },
        'non-nullable': {

        }
    },
    'WrsOPPFG_PCT': {
        'nullable': {
            None: 'WrsOPPFG_PCTNullable'
        },
        'non-nullable': {

        }
    },
    'WrsOPPFG3M': {
        'nullable': {
            None: 'WrsOPPFG3MNullable'
        },
        'non-nullable': {

        }
    },
    'BtrOPPTOV': {
        'nullable': {
            None: 'BtrOPPTOVNullable'
        },
        'non-nullable': {

        }
    },
    'BtrOPPFTA': {
        'nullable': {
            None: 'BtrOPPFTANullable'
        },
        'non-nullable': {

        }
    },
    'EqPTSPAINT': {
        'nullable': {
            None: 'EqPTSPAINTNullable'
        },
        'non-nullable': {

        }
    },
    'LtOPPBLK': {
        'nullable': {
            None: 'LtOPPBLKNullable'
        },
        'non-nullable': {

        }
    },
    'BtrOPPFT_PCT': {
        'nullable': {
            None: 'BtrOPPFT_PCTNullable'
        },
        'non-nullable': {

        }
    },
    'LtOPPPTSFB': {
        'nullable': {
            None: 'LtOPPPTSFBNullable'
        },
        'non-nullable': {

        }
    },
    'GtOPPSTL': {
        'nullable': {
            None: 'GtOPPSTLNullable'
        },
        'non-nullable': {

        }
    },
    'GtOPPDREB': {
        'nullable': {
            None: 'GtOPPDREBNullable'
        },
        'non-nullable': {

        }
    },
    'ActiveTeamsOnly': {
        'nullable': {
            None: 'ActiveTeamsOnlyNullable'
        },
        'non-nullable': {

        }
    },
    'BtrOPPPTS': {
        'nullable': {
            None: 'BtrOPPPTSNullable'
        },
        'non-nullable': {

        }
    },
    'WrsOPPDREB': {
        'nullable': {
            None: 'WrsOPPDREBNullable'
        },
        'non-nullable': {

        }
    },
    'LtOPPPTSPAINT': {
        'nullable': {
            None: 'LtOPPPTSPAINTNullable'
        },
        'non-nullable': {

        }
    },
    'LtOPPFTM': {
        'nullable': {
            None: 'LtOPPFTMNullable'
        },
        'non-nullable': {

        }
    },
    'WrsOPPFTM': {
        'nullable': {
            None: 'WrsOPPFTMNullable'
        },
        'non-nullable': {

        }
    },
    'EqPTSOFFTOV': {
        'nullable': {
            None: 'EqPTSOFFTOVNullable'
        },
        'non-nullable': {

        }
    },
    'EqOPPPTSFB': {
        'nullable': {
            None: 'EqOPPPTSFBNullable'
        },
        'non-nullable': {

        }
    },
    'BtrOPPAST': {
        'nullable': {
            None: 'BtrOPPASTNullable'
        },
        'non-nullable': {

        }
    },
    'MinGames': {
        'nullable': {
            None: 'MinGamesNullable'
        },
        'non-nullable': {

        }
    },
    'LtOPPFG3M': {
        'nullable': {
            None: 'LtOPPFG3MNullable'
        },
        'non-nullable': {

        }
    },
    'WrsOPPPTS': {
        'nullable': {
            None: 'WrsOPPPTSNullable'
        },
        'non-nullable': {

        }
    },
    'WrsOPPREB': {
        'nullable': {
            None: 'WrsOPPREBNullable'
        },
        'non-nullable': {

        }
    },
    'WrsOPPSTL': {
        'nullable': {
            None: 'WrsOPPSTLNullable'
        },
        'non-nullable': {

        }
    },
    'LtPTSPAINT': {
        'nullable': {
            None: 'LtPTSPAINTNullable'
        },
        'non-nullable': {

        }
    },
    'BtrOPPFG3A': {
        'nullable': {
            None: 'BtrOPPFG3ANullable'
        },
        'non-nullable': {

        }
    },
    'WrsOPPFT_PCT': {
        'nullable': {
            None: 'WrsOPPFT_PCTNullable'
        },
        'non-nullable': {

        }
    },
    'WrsOPPPTSFB': {
        'nullable': {
            None: 'WrsOPPPTSFBNullable'
        },
        'non-nullable': {

        }
    },
    'EqOPPPTSPAINT': {
        'nullable': {
            None: 'EqOPPPTSPAINTNullable'
        },
        'non-nullable': {

        }
    },
    'GtOPPFTM': {
        'nullable': {
            None: 'GtOPPFTMNullable'
        },
        'non-nullable': {

        }
    },
    'GtOPPPTSFB': {
        'nullable': {
            None: 'GtOPPPTSFBNullable'
        },
        'non-nullable': {

        }
    },
    'GtOPPFT_PCT': {
        'nullable': {
            None: 'GtOPPFT_PCTNullable'
        },
        'non-nullable': {

        }
    },
    'LtOPPFG3A': {
        'nullable': {
            None: 'LtOPPFG3ANullable'
        },
        'non-nullable': {

        }
    },
    'GtPTSPAINT': {
        'nullable': {
            None: 'GtPTSPAINTNullable'
        },
        'non-nullable': {

        }
    },
    'WrsOPPTOV': {
        'nullable': {
            None: 'WrsOPPTOVNullable'
        },
        'non-nullable': {

        }
    },
    'BtrOPPPF': {
        'nullable': {
            None: 'BtrOPPPFNullable'
        },
        'non-nullable': {

        }
    },
    'BtrOPPPTS2NDCHANCE': {
        'nullable': {
            None: 'BtrOPPPTS2NDCHANCENullable'
        },
        'non-nullable': {

        }
    },
    'GtOPPPF': {
        'nullable': {
            None: 'GtOPPPFNullable'
        },
        'non-nullable': {

        }
    },
    'WrsOPPFTA': {
        'nullable': {
            None: 'WrsOPPFTANullable'
        },
        'non-nullable': {

        }
    },
    'GtOPPFGM': {
        'nullable': {
            None: 'GtOPPFGMNullable'
        },
        'non-nullable': {

        }
    },
    'LtOPPFG3PCT': {
        'nullable': {
            None: 'LtOPPFG3PCTNullable'
        },
        'non-nullable': {

        }
    },
    'LtOPPREB': {
        'nullable': {
            None: 'LtOPPREBNullable'
        },
        'non-nullable': {

        }
    },
    'WStreak': {
        'nullable': {
            None: 'WStreakNullable'
        },
        'non-nullable': {

        }
    },
    'BtrOPPFTM': {
        'nullable': {
            None: 'BtrOPPFTMNullable'
        },
        'non-nullable': {

        }
    },
    'LtOPPFGA': {
        'nullable': {
            None: 'LtOPPFGANullable'
        },
        'non-nullable': {

        }
    },
    'LtOPPPTSOFFTOV': {
        'nullable': {
            None: 'LtOPPPTSOFFTOVNullable'
        },
        'non-nullable': {

        }
    },
    'EqPTS2NDCHANCE': {
        'nullable': {
            None: 'EqPTS2NDCHANCENullable'
        },
        'non-nullable': {

        }
    },
    'WrsOPPFG3A': {
        'nullable': {
            None: 'WrsOPPFG3ANullable'
        },
        'non-nullable': {

        }
    },
    'BtrOPPFGM': {
        'nullable': {
            None: 'BtrOPPFGMNullable'
        },
        'non-nullable': {

        }
    },
    'LtOPPOREB': {
        'nullable': {
            None: 'LtOPPOREBNullable'
        },
        'non-nullable': {

        }
    },
    'LtOPPPTS': {
        'nullable': {
            None: 'LtOPPPTSNullable'
        },
        'non-nullable': {

        }
    },
    'LtOPPTOV': {
        'nullable': {
            None: 'LtOPPTOVNullable'
        },
        'non-nullable': {

        }
    },
    'WrsOPPFGA': {
        'nullable': {
            None: 'WrsOPPFGANullable'
        },
        'non-nullable': {

        }
    },
    'GtPTSFB': {
        'nullable': {
            None: 'GtPTSFBNullable'
        },
        'non-nullable': {

        }
    },
    'BtrOPPFG_PCT': {
        'nullable': {
            None: 'BtrOPPFG_PCTNullable'
        },
        'non-nullable': {

        }
    },
    'EqOPPPTSOFFTOV': {
        'nullable': {
            None: 'EqOPPPTSOFFTOVNullable'
        },
        'non-nullable': {

        }
    },
    'GtOPPFG3PCT': {
        'nullable': {
            None: 'GtOPPFG3PCTNullable'
        },
        'non-nullable': {

        }
    },
    'EqPTSFB': {
        'nullable': {
            None: 'EqPTSFBNullable'
        },
        'non-nullable': {

        }
    },
    'BtrOPPPTSOFFTOV': {
        'nullable': {
            None: 'BtrOPPPTSOFFTOVNullable'
        },
        'non-nullable': {

        }
    },
    'LStreak': {
        'nullable': {
            None: 'LStreakNullable'
        },
        'non-nullable': {

        }
    },
    'GtOPPFG3M': {
        'nullable': {
            None: 'GtOPPFG3MNullable'
        },
        'non-nullable': {

        }
    },
    'DraftNumber': {
        'nullable': {
            None: 'DraftNumberNullable'
        },
        'non-nullable': {

        }
    },
    'YearsExperience': {
        'nullable': {
            None: 'YearsExperienceNullable'
        },
        'non-nullable': {

        }
    },
    'DraftTeamID': {
        'nullable': {
            None: 'DraftTeamIDNullable'
        },
        'non-nullable': {

        }
    },
    'DraftRound': {
        'nullable': {
            None: 'DraftRoundNullable'
        },
        'non-nullable': {

        }
    },
    'TwoWay': {
        'nullable': {
            None: 'TwoWayNullable'
        },
        'non-nullable': {

        }
    },
    'MinutesMin': {
        'nullable': {
        },
        'non-nullable': {
            None: 'MinutesMin'
        }
    },
}
