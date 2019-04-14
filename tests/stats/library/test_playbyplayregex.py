import pytest
import re
from nba_api.stats.library.playbyplayregex import *

class TestPlayByPlay(object):

    #PLAYER NAME
    from nba_api.stats.library.playbyplayregex import pattern_player

    def test_player(self):
 
        re_player = re.compile('^{player}'.format(player=pattern_player))

        #Single Name
        description = "Millsap REBOUND (Off:0 Def:2)"
        player = re_player.search(description).group('player')
        assert player == 'Millsap'

        #Hyphenated Name
        description = "Bates-Diop REBOUND (Off:0 Def:1)"
        player = re_player.search(description).group('player')
        assert player == 'Bates-Diop'

        #Name with Apostrophe
        description = "O'Quinn REBOUND (Off:0 Def:1)"
        player = re_player.search(description).group('player')
        assert player == "O'Quinn"

        #First Initial + Last Name
        description = "S. Hill REBOUND (Off:0 Def:1)"
        player = re_player.search(description).group('player')
        assert player == "S. Hill"

        #Junior
        description = "Porter Jr. REBOUND (Off:0 Def:1)"
        player = re_player.search(description).group('player')
        assert player == "Porter Jr."

        #Second
        description = "Payton II REBOUND (Off:0 Def:1)"
        player = re_player.search(description).group('player')
        assert player == "Payton II"

        #Third
        description = "Robinson III REBOUND (Off:0 Def:1)"
        player = re_player.search(description).group('player')
        assert player == "Robinson III"
        
        #Fourth
        description = "Walker IV REBOUND (Off:0 Def:1)"
        player = re_player.search(description).group('player')
        assert player == "Walker IV"

    #BLOCK
    block_player = "Collins BLOCK (1 BLK)"
    def test_block_player(self):
        
        assert re_block.match(self.block_player)

        search_result = re_block.search(self.block_player)
        
        #Player Name
        player = search_result.group('player')
        assert player == 'Collins'

        #Player
        block = search_result.group('blocks')
        assert block == '1'
        
    #FIELD GOAL MADE
    field_goal_made = "Evans 24' 3PT Jump Shot (3 PTS) (O'Quinn 1 AST)"
    def test_field_goal_made(self):
        search_result = re_field_goal_made.search(self.field_goal_made)
        
        #Field Goal Type
        field_goal_type = search_result.group('field_goal_type')
        assert field_goal_type == '3PT Jump Shot'

        #Player Name
        player = search_result.group('player')
        assert player == 'Evans'

        #Disatance
        distance = search_result.group('distance')
        assert distance == '24'

        #Points
        points = search_result.group('points')
        assert points == '3'

        #Assists
        points = search_result.group('assists')
        assert points == '1'

        #Player Name Assist
        player = search_result.group('player_ast')
        assert player == "O'Quinn"

    #FIELD GOAL MISSED
    field_goal_missed = "MISS O'Quinn 17' Jump Shot"
    def test_field_goal_missed(self):
        search_result = re_field_goal_missed.search(self.field_goal_missed)
        
        #Field Goal Type
        field_goal_type = search_result.group('field_goal_type')
        assert field_goal_type == 'Jump Shot'

        #Player Name
        player = search_result.group('player')
        assert player == "O'Quinn"

        #Distance
        distance = search_result.group('distance')
        assert distance == '17'

   #FOUL
    foul_player = "Collison P.FOUL (P1.TN) (M.Lindsay)"
    def test_foul_player(self):
        search_result = re_foul.search(self.foul_player)
        
        #Player Name
        player = search_result.group('player')
        assert player == 'Collison'

        #Foul Type
        foul_type = search_result.group('foul_type')
        assert foul_type == 'P.FOUL'

        #Player
        player = search_result.group('personal')
        assert player == '1'
        
        #Team Count
        team = search_result.group('team')
        assert team == 'N'

        #Referee
        referee = search_result.group('referee')
        assert referee == 'M.Lindsay'

    #FREE THROW MADE
    free_throw_made = "Sumner Free Throw 2 of 2 (1 PTS)"
    def test_free_throw_made(self):
        search_result = re_free_throw_made.search(self.free_throw_made)
        
        #Player Name
        player = search_result.group('player')
        assert player == 'Sumner'

        #Free Throw Type
        free_throw_type = search_result.group('free_throw_type')
        assert free_throw_type == '2 of 2'

        #Points
        points = search_result.group('points')
        assert points == '1'

    #FREE THROW MISSED
    free_throw_miss = "MISS Prince Free Throw 1 of 2"
    def test_free_throw_missed(self):
        search_result = re_free_throw_miss.search(self.free_throw_miss)
        
        #Player Name
        player = search_result.group('player')
        assert player == 'Prince'

        #Free Throw Type
        free_throw_type = search_result.group('free_throw_type')
        assert free_throw_type == '1 of 2'

    #JUMP BALL
    jump_ball = "Jump Ball Collins vs. O'Quinn: Tip to Leaf"
    def test_jump_ball(self):
        search_result = re_jump_ball.search(self.jump_ball)
        
        #Player Name
        player = search_result.group('player_home')
        assert player == 'Collins'

        #Player Name
        player = search_result.group('player_away')
        assert player == "O'Quinn"

        #Player Name
        player = search_result.group('player_tip')
        assert player == 'Leaf'

    #REBOUND PLAYER
    rebound_player = "Zubac REBOUND (Off:2 Def:4)"
    def test_rebound_player(self):
        search_result = re_rebound_player.search(self.rebound_player)
        
        #Player Name
        player = search_result.group('player')
        assert player == 'Zubac'

        #Offensive
        offensive = search_result.group('offensive')
        assert offensive == "2"

        #Defensive
        defensive = search_result.group('defensive')
        assert defensive == '4'

    #REBOUND TEAM
    rebound_team = "Timberwolves Rebound"
    def test_rebound_team(self):
        search_result = re_rebound_team.search(self.rebound_team)
        
        #Team Name
        team = search_result.group('team')
        assert team == 'Timberwolves'
        
    #STEAL
    steal_player = "Bradley STEAL (2 STL)"
    def test_steal_player(self):
        search_result = re_steal.search(self.steal_player)
        
        #Player Name
        player = search_result.group('player')
        assert player == 'Bradley'

        #Steals
        offensive = search_result.group('steals')
        assert offensive == "2"
        
    #SUBSTITUTION
    substitution = "SUB: Sefolosha FOR Ingles"
    def test_substitution(self):
        search_result = re_substitution.search(self.substitution)
        
        #Player In Name
        player_in = search_result.group('player_in')
        assert player_in == 'Sefolosha'

        #Player Out Name
        player_out = search_result.group('player_out')
        assert player_out == 'Ingles'

    #TIMEOUT
    timeout = "TRAIL BLAZERS Timeout: Regular (Full 5 Short 0)"
    def test_timeout(self):
        search_result = re_timeout.search(self.timeout)
        
        #Team Name
        team = search_result.group('team')
        assert team == 'TRAIL BLAZERS'

        #Timeout type
        timeout_type = search_result.group('timeout_type')
        assert timeout_type == 'Regular'

        #Full
        full = search_result.group('full')
        assert full == '5'

        #Short
        short = search_result.group('short')
        assert short == '0'

    #TURNOVER PLAYER
    turnover_player = "G. Harrison Double Dribble Turnover (P1.T10)"
    def test_turnover_player(self):
        search_result = re_turnover_player.search(self.turnover_player)
        
        #Turnover Type
        turnover_type = search_result.group('turnover_type')
        assert turnover_type == 'Double Dribble'

        #Player Name
        player = search_result.group('player')
        assert player == 'G. Harrison'

        #Player
        player = search_result.group('personal')
        assert player == '1'

        #Team
        team = search_result.group('team')
        assert team == '10'

    #TURNOVER TEAM
    turnover_team = "NUGGETS Turnover: Shot Clock (T#12)"
    def test_turnover_team(self):
        search_result = re_turnover_team.search(self.turnover_team)
        
        #Team Name
        team = search_result.group('team')
        assert team == 'NUGGETS'

        #Turnover Type
        team = search_result.group('turnover_type')
        assert team == 'Shot Clock'

        #Turnovers
        team = search_result.group('turnovers')
        assert team == '12'

    #VIOLATION
    violation = "Dieng Violation:Kicked Ball (T.Brown)"
    def test_violation(self):
        search_result = re_violation.search(self.violation)
        
        #Violation
        violation_type = search_result.group('violation_type')
        assert violation_type == 'Kicked Ball'

        #Player Name
        player = search_result.group('player')
        assert player == 'Dieng'

        #Referee
        referee = search_result.group('referee')
        assert referee == 'T.Brown'
