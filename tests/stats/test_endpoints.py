import time
import json

import pytest
import numpy as np

import nba_api.stats.endpoints as ep

class EndpointTester:
    '''Simple class to represent an endpoint with deferred evaluation.'''
    def __init__(self, endpoint_class, **kwargs):
        self.endpoint_class = endpoint_class
        self.kwargs = kwargs

    def __call__(self):
        return self.endpoint_class(**self.kwargs)

# Once we run the test to call the endpoints, we'll cache the responses here.
cached_eps = []

# A bunch of valid but uninstantiated endpoints for testing:
endpoints = [ EndpointTester(ep.AssistLeaders),
        EndpointTester(ep.AssistTracker),
        EndpointTester(ep.BoxScoreAdvancedV2, game_id='0021700807'),
        EndpointTester(ep.BoxScoreDefensive, game_id='0021700807'),
        EndpointTester(ep.BoxScoreFourFactorsV2, game_id='0021700807'),
        EndpointTester(ep.BoxScoreMatchups, game_id='0021700807'),
        EndpointTester(ep.BoxScoreMiscV2, game_id='0021700807'),
        EndpointTester(ep.BoxScorePlayerTrackV2, game_id='0021700807'),
        EndpointTester(ep.BoxScoreScoringV2, game_id='0021700807'),
        EndpointTester(ep.BoxScoreSummaryV2, game_id='0021700807'),
        EndpointTester(ep.BoxScoreTraditionalV2, game_id='0021700807'),
        EndpointTester(ep.BoxScoreUsageV2, game_id='0021700807'),
        EndpointTester(ep.CommonAllPlayers),
        EndpointTester(ep.CommonPlayerInfo, player_id='2544'),
        EndpointTester(ep.CommonPlayoffSeries),
        EndpointTester(ep.CommonTeamRoster, team_id='1610612739'),
        EndpointTester(ep.CommonTeamYears),
        EndpointTester(ep.DefenseHub, season='2017-18'),
        EndpointTester(ep.DraftCombineDrillResults),
        EndpointTester(ep.DraftCombineNonStationaryShooting),
        EndpointTester(ep.DraftCombinePlayerAnthro),
        EndpointTester(ep.DraftCombineSpotShooting),
        EndpointTester(ep.DraftCombineStats),
        EndpointTester(ep.DraftHistory),
        EndpointTester(ep.FantasyWidget),
        EndpointTester(ep.FranchiseHistory),
        EndpointTester(ep.FranchiseLeaders, team_id='1610612739'),
        EndpointTester(ep.FranchisePlayers, team_id='1610612739'),
        EndpointTester(ep.HomePageLeaders),
        EndpointTester(ep.HomePageV2),
        EndpointTester(ep.InfographicFanDuelPlayer, game_id='0021700807'),
        EndpointTester(ep.LeadersTiles),
        EndpointTester(ep.LeagueDashLineups),
        EndpointTester(ep.LeagueDashPlayerBioStats),
        EndpointTester(ep.LeagueDashPlayerClutch),
        EndpointTester(ep.LeagueDashPlayerPtShot),
        EndpointTester(ep.LeagueDashPlayerShotLocations),
        EndpointTester(ep.LeagueDashPlayerStats),
        EndpointTester(ep.LeagueDashPtDefend),
        EndpointTester(ep.LeagueDashPtStats),
        EndpointTester(ep.LeagueDashPtTeamDefend),
        EndpointTester(ep.LeagueDashTeamClutch),
        EndpointTester(ep.LeagueDashTeamPtShot),
        EndpointTester(ep.LeagueDashTeamShotLocations),
        EndpointTester(ep.LeagueDashTeamStats),
        EndpointTester(ep.LeagueGameFinder),
        EndpointTester(ep.LeagueGameLog),
        EndpointTester(ep.LeagueLeaders),
        EndpointTester(ep.LeaguePlayerOnDetails, team_id='1610612739'),
        EndpointTester(ep.LeagueSeasonMatchups, off_player_id_nullable=2544,
            def_player_id_nullable='1610612739'),
        EndpointTester(ep.LeagueStandings),
        EndpointTester(ep.PlayByPlay, game_id='0021700807'),
        EndpointTester(ep.PlayByPlayV2, game_id='0021700807'),
        EndpointTester(ep.PlayerAwards, player_id='2544'),
        EndpointTester(ep.PlayerCareerStats, player_id='2544'),
        EndpointTester(ep.PlayerCompare, player_id_list='202681,203078,2544,201567,203954',
                vs_player_id_list='201566,201939,201935,201142,203076'),
        EndpointTester(ep.PlayerDashPtPass, player_id='2544', team_id='1610612739'),
        EndpointTester(ep.PlayerDashPtReb, player_id='2544', team_id='1610612739'),
        EndpointTester(ep.PlayerDashPtShotDefend, player_id='2544',
                team_id='1610612739'),
        EndpointTester(ep.PlayerDashPtShots, player_id='2544', team_id='1610612739'),
        EndpointTester(ep.PlayerDashboardByClutch, player_id='2544'),
        EndpointTester(ep.PlayerDashboardByGameSplits, player_id='2544'),
        EndpointTester(ep.PlayerDashboardByGeneralSplits, player_id='2544'),
        EndpointTester(ep.PlayerDashboardByLastNGames, player_id='2544'),
        EndpointTester(ep.PlayerDashboardByOpponent, player_id='2544'),
        EndpointTester(ep.PlayerDashboardByShootingSplits, player_id='2544'),
        EndpointTester(ep.PlayerDashboardByTeamPerformance, player_id='2544'),
        EndpointTester(ep.PlayerDashboardByYearOverYear, player_id='2544'),
        EndpointTester(ep.PlayerFantasyProfile, player_id='2544'),
        EndpointTester(ep.PlayerFantasyProfileBarGraph, player_id='2544'),
        EndpointTester(ep.PlayerGameLog, player_id='2544'),
        EndpointTester(ep.PlayerGameStreakFinder),
        EndpointTester(ep.PlayerNextNGames, player_id='2544'),
        EndpointTester(ep.PlayerProfileV2, player_id='2544'),
        EndpointTester(ep.PlayerVsPlayer, player_id='2544', vs_player_id='202681'),
        EndpointTester(ep.PlayoffPicture),
        EndpointTester(ep.Scoreboard),
        EndpointTester(ep.ScoreboardV2),
        EndpointTester(ep.ShotChartDetail, player_id='2544', team_id='1610612739'),
        EndpointTester(ep.ShotChartLineupDetail),
        EndpointTester(ep.TeamAndPlayersVsPlayers,
                team_id=1610612739,
                player_id1=203954,
                player_id2=201567,
                player_id3=203507,
                player_id4=203078,
                player_id5=202681,
                vs_team_id=1610612765,
                vs_player_id1=203954,
                vs_player_id2=201567,
                vs_player_id3=203507,
                vs_player_id4=203078,
                vs_player_id5=202681),
        EndpointTester(ep.TeamDashLineups, team_id='1610612739'),
        EndpointTester(ep.TeamDashPtPass, team_id='1610612739'),
        EndpointTester(ep.TeamDashPtReb, team_id='1610612739'),
        EndpointTester(ep.TeamDashPtShots, team_id='1610612739'),
        EndpointTester(ep.TeamDashboardByClutch, team_id='1610612739'),
        EndpointTester(ep.TeamDashboardByGameSplits, team_id='1610612739'),
        EndpointTester(ep.TeamDashboardByGeneralSplits, team_id='1610612739'),
        EndpointTester(ep.TeamDashboardByLastNGames, team_id='1610612739'),
        EndpointTester(ep.TeamDashboardByOpponent, team_id='1610612739'),
        EndpointTester(ep.TeamDashboardByShootingSplits, team_id='1610612739'),
        EndpointTester(ep.TeamDashboardByTeamPerformance, team_id='1610612739'),
        EndpointTester(ep.TeamDashboardByYearOverYear, team_id='1610612739'),
        EndpointTester(ep.TeamDetails, team_id='1610612739'),
        EndpointTester(ep.TeamGameLog, team_id='1610612739'),
        EndpointTester(ep.TeamGameStreakFinder),
        EndpointTester(ep.TeamHistoricalLeaders, team_id='1610612739'),
        EndpointTester(ep.TeamInfoCommon, team_id='1610612739'),
        EndpointTester(ep.TeamPlayerDashboard, team_id='1610612739'),
        EndpointTester(ep.TeamPlayerOnOffDetails, team_id='1610612739'),
        EndpointTester(ep.TeamPlayerOnOffSummary, team_id='1610612739'),
        EndpointTester(ep.TeamVsPlayer, team_id='1610612739', vs_player_id='2544'),
        EndpointTester(ep.TeamYearByYearStats, team_id='1610612739'),
        EndpointTester(ep.VideoDetails, player_id='2544', game_id='0021700807',
                team_id='1610612739', start_period=1, end_period=1),
        EndpointTester(ep.VideoEvents, game_id='0021700807'),
        EndpointTester(ep.VideoStatus),
        EndpointTester(ep.WinProbabilityPBP, game_id='0021700807')]

@pytest.mark.parametrize('endpoint', endpoints)
def test_endpoints_run(endpoint):
    '''Test that each endpoint is callable.
    
    This takes a very, very long time in total (10-20 minutes) because we don't
    want to barrage the NBA site with requests.'''
    # Delay briefly.
    wait = np.random.gamma(shape=9, scale=0.4)
    time.sleep(wait)
    # Call the API.
    try:
        response = endpoint()
    except json.decoder.JSONDecodeError:
        endpoint_class = type(endpoint.endpoint_class)
        msg = 'Unable to decode response for {}'.format(endpoint_class)
        pytest.fail(msg=msg)
    # We want to hang onto all the responses so we don't need to re-retrieve
    # them later.
    cached_eps.append(response)

def test_valid_json():
    # Check that every called endpoint is valid json.
    valid = [ep.nba_response.valid_json() for ep in cached_eps]
    assert len(valid) == len(endpoints)
    assert all(valid)
