import pytest
import re
from collections import defaultdict
from nba_api.stats.library.eventmsgtype import EventMsgType
from nba_api.stats.library.playbyplayregex import *

#Note: Ues conftest.py to feed data into the tests

#PLAYER NAME
def test_player(playbyplaydata):

    re_player = re.compile('^{player}'.format(player=pattern_player))

    for play in playbyplaydata["Player"]:

        #Get Capture Groups
        search_result = re_player.search(play['description'])
        
        #Player Name
        player = search_result.group('player')
        assert player == play['player']

#BLOCK
def test_block_player(playbyplaydata):
    
    for play in playbyplaydata["Block"]:

        #Validate Pattern
        assert re_block.match(play['description'])

        #Get Capture Groups
        search_result = re_block.search(play['description'])
        
        #Player Name
        player = search_result.group('player')
        assert player == play['player']

        #Player
        block = search_result.group('blocks')
        assert block == play['blocks']

#EJECTION
def test_ejection_player(playbyplaydata):
    
    for play in playbyplaydata["Ejection"]:

        #Validate Pattern
        assert re_ejection.match(play['description'])

        #Get Capture Groups
        search_result = re_ejection.search(play['description'])
        
        #Player Name
        player = search_result.group('player')
        assert player == play['player']

        #Ejection Type
        ejection_type = search_result.group('ejection_type')
        assert ejection_type == play['ejection_type']

#FIELD GOAL MADE
def test_field_goal_made(playbyplaydata):
    
    for play in playbyplaydata["FieldGoalMade"]:

        #Validate Pattern
        assert re_field_goal_made.match(play['description'])

        #Get Capture Groups
        search_result = re_field_goal_made.search(play['description'])
        
        #Field Goal Type
        field_goal_type = search_result.group('field_goal_type')
        assert field_goal_type == play['field_goal_type']

        #Player Name
        player = search_result.group('player')
        assert player == play['player']

        #Disatance
        distance = search_result.group('distance')
        assert distance == play['distance']

        #Points
        points = search_result.group('points')
        assert points == play['points']

        #Player Name Assist
        player = search_result.group('player_ast')
        assert player == play['player_ast']

        #Assists
        points = search_result.group('assists')
        assert points == play['assists']

#FIELD GOAL MISSED
field_goal_missed = "MISS O'Quinn 17' Jump Shot"
def test_field_goal_missed(playbyplaydata):

    for play in playbyplaydata["FieldGoalMissed"]:

        #Validate Pattern
        assert re_field_goal_missed.match(play['description'])

        #Get Capture Groups
        search_result = re_field_goal_missed.search(field_goal_missed)
        
        #Field Goal Type
        field_goal_type = search_result.group('field_goal_type')
        assert field_goal_type == play['field_goal_type']

        #Player Name
        player = search_result.group('player')
        assert player == play['player']

        #Distance
        distance = search_result.group('distance')
        assert distance == play['distance']

#FOUL
def test_foul_player(playbyplaydata):

    for play in playbyplaydata["Foul"]:

        #Validate Pattern
        assert re_foul.match(play['description'])

        #Get Capture Groups
        search_result = re_foul.search(play['description'])
        
        #Player Name
        player = search_result.group('player')
        assert player == play['player']

        #Foul Type
        foul_type = search_result.group('foul_type')
        assert foul_type == play['foul_type']

        #Player
        player = search_result.group('personal')
        assert player == play['personal']
        
        #Team Count
        team = search_result.group('team')
        assert team == play['team']

        #Referee
        referee = search_result.group('referee')
        assert referee == play['referee']

#FREE THROW MADE
def test_free_throw_made(playbyplaydata):

    for play in playbyplaydata["FreeThrowMade"]:

        #Validate Pattern
        assert re_free_throw_made.match(play['description'])

        #Get Capture Groups
        search_result = re_free_throw_made.search(play['description'])
    
        #Player Name
        player = search_result.group('player')
        assert player == play['player']

        #Free Throw Type
        free_throw_type = search_result.group('free_throw_type')
        assert free_throw_type == play['free_throw_type']


        #Points
        points = search_result.group('points')
        assert points == play['points']

#FREE THROW MISSED
def test_free_throw_missed(playbyplaydata):

    for play in playbyplaydata["FreeThrowMissed"]:

        #Validate Pattern
        assert re_free_throw_miss.match(play['description'])

        #Get Capture Groups
        search_result = re_free_throw_miss.search(play['description'])
        
        #Player Name
        player = search_result.group('player')
        assert player == play['player']

        #Free Throw Type
        free_throw_type = search_result.group('free_throw_type')
        assert free_throw_type == play['free_throw_type']

#JUMP BALL
def test_jump_ball(playbyplaydata):
    
    for play in playbyplaydata["JumpBall"]:

        #Validate Pattern
        assert re_jump_ball.match(play['description'])

        #Get Capture Groups   
        search_result = re_jump_ball.search(play['description'])
    
        #Player Name
        player = search_result.group('player_home')
        assert player == play['player_home']

        #Player Name
        player = search_result.group('player_away')
        assert player == play['player_away']

        #Player Name
        player = search_result.group('player_tip')
        assert player == play['player_tip']

#REBOUND PLAYER
def test_rebound_player(playbyplaydata):
    
    for play in playbyplaydata["ReboundPlayer"]:

        #Validate Pattern
        assert re_rebound_player.match(play['description'])

        #Get Capture Groups   
        search_result = re_rebound_player.search(play['description'])
        
        #Player Name
        player = search_result.group('player')
        assert player == play['player']

        #Offensive
        offensive = search_result.group('offensive')
        assert offensive == play['offensive']

        #Defensive
        defensive = search_result.group('defensive')
        assert defensive == play['defensive']

#REBOUND TEAM
def test_rebound_team(playbyplaydata):

    for play in playbyplaydata["RebounTeam"]:

        #Validate Pattern
        assert re_rebound_team.match(play['description'])

        #Get Capture Groups   
        search_result = re_rebound_team.search(play['description'])
        
        #Team Name
        team = search_result.group('team')
        assert team == play['team']
    
#STEAL
def test_steal_player(playbyplaydata):
 
    for play in playbyplaydata["Steal"]:

        #Validate Pattern
        assert re_steal.match(play['description'])

        #Get Capture Groups   
        search_result = re_steal.search(play['description'])
        
        #Player Name
        player = search_result.group('player')
        assert player == play['player']

        #Steals
        offensive = search_result.group('steals')
        assert offensive == play['steals']
    
#SUBSTITUTION
def test_substitution(playbyplaydata):

    for play in playbyplaydata["Substitution"]:

        #Validate Pattern
        assert re_substitution.match(play['description'])

        #Get Capture Groups   
        search_result = re_substitution.search(play['description'])
        
        #Player In Name
        player_in = search_result.group('player_in')
        assert player_in == play['player_in']

        #Player Out Name
        player_out = search_result.group('player_out')
        assert player_out == play['player_out']

#TIMEOUT
def test_timeout(playbyplaydata):

    for play in playbyplaydata["Timeout"]:

        #Validate Pattern
        assert re_timeout.match(play['description'])

        #Get Capture Groups   
        search_result = re_timeout.search(play['description'])
        
        #Team Name
        team = search_result.group('team')
        assert team == play['team']

        #Timeout type
        timeout_type = search_result.group('timeout_type')
        assert timeout_type == play['timeout_type']

        #Full
        full = search_result.group('full')
        assert full == play['full']

        #Short
        short = search_result.group('short')
        assert short == play['short']

#TURNOVER PLAYER
def test_turnover_player(playbyplaydata):

    for play in playbyplaydata["TuroverPlayer"]:

        #Validate Pattern
        assert re_turnover_player.match(play['description'])

        #Get Capture Groups   
        search_result = re_turnover_player.search(play['description'])
        
        #Player Name
        player = search_result.group('player')
        assert player == play['player']

        #Turnover Type
        turnover_type = search_result.group('turnover_type')
        assert turnover_type == play['turnover_type']

        #Personal
        personal = search_result.group('personal')
        assert player == play['personal']

        #Team
        team = search_result.group('team')
        assert team == play['team']

#TURNOVER TEAM
turnover_team = "NUGGETS Turnover: Shot Clock (T#12)"
def test_turnover_team(playbyplaydata):

     for play in playbyplaydata["TurnoverTeam"]:

        #Validate Pattern
        assert re_turnover_team.match(play['description'])

        #Get Capture Groups   
        search_result = re_turnover_team.search(play['description'])
        
        #Team Name
        team = search_result.group('team')
        assert team == play['team']

        #Turnover Type
        team = search_result.group('turnover_type')
        assert team == play['turnover_type']

        #Turnovers
        team = search_result.group('turnovers')
        assert team == play['turnovers']

#VIOLATION

def test_violation(playbyplaydata):

     for play in playbyplaydata["Violation"]:

        #Validate Pattern
        assert re_violation.match(play['description'])

        #Get Capture Groups   
        search_result = re_violation.search(play['violation'])
        
        #Violation
        violation_type = search_result.group('violation_type')
        assert violation_type == play['violation_type']

        #Player Name
        player = search_result.group('player')
        assert player == play['player']

        #Referee
        referee = search_result.group('referee')
        assert referee == play['referee']
