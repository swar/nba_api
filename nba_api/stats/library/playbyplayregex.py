import re
from collections import defaultdict
from nba_api.stats.library.eventmsgtype import EventMsgType

# regex patterns for all playbyplay and playbyplayv2 HOMEDESCRIPTION & VISITORDESCRIPTION fields 
pattern_player_char = r'((?#char)(\. \w+)|(\-?\'?\w+))?'
pattern_player_suffix = r'((?#suffix)([\s](Jr\.|III|II|IV)))?'
pattern_referee = r'(?P<referee>.*)'
pattern_team = r'(?P<team>\w+( \w+)?)'
pattern_field_goal_type = r'(?P<field_goal_type>[\w+( |\-)]*)'
pattern_free_throw_type = r'(?P<free_throw_type>(.* )?(\d of \d)|\w+)'
pattern_player = r"(?P<player>\w+{player_char}{player_suffix})".format(player_char=pattern_player_char,player_suffix=pattern_player_suffix)
pattern_points = r"\((?P<points>\d+) PTS\)"
pattern_rebound_team = r'^{team} Rebound$'.format(team=pattern_team)
pattern_turnover_team = r'^{team} Turnover: (?P<turnover_type>.*) \(T#(?P<turnovers>\d+)\)$'.format(team=pattern_team)
pattern_timeout = r'^{team} Timeout: ((?P<timeout_type>\w+)) \(\w+ (?P<full>\d+) \w+ (?P<short>\d+)\)$'.format(team=pattern_team)
pattern_block = r"^{player} BLOCK \((?P<blocks>\d+) BLK\)$".format(player=pattern_player)                    
pattern_ejection = r'^{player} Ejection:(?P<ejection_type>.*)$'.format(player=pattern_player)
pattern_field_goal_made = r"^{player}\s{{1,2}}?((?P<distance>\d+)\' )?{field_goal_type} {points}( \({player_ast} (?P<assists>\d+) AST\))?$".format(
    player=pattern_player,player_ast=pattern_player.replace('player','player_ast'), field_goal_type=pattern_field_goal_type,points=pattern_points)
pattern_field_goal_missed = r"^MISS {player}\s{{1,2}}?((?P<distance>\d+)\' )?{field_goal_type}$".format(player=pattern_player,field_goal_type=pattern_field_goal_type)
pattern_foul_player = r"^{player} (?P<foul_type>.*)\s(?=(\(\w+(?P<personal>\d+)(\.\w+(?P<team>[\d|\w]+))?\) (\({referee}\)))$)".format(player=pattern_player, referee=pattern_referee)
pattern_foul_team = r"^{team} T.Foul \((?P<foul_type>.*) {player} \) (\({referee}\))".format(player=pattern_player, team=pattern_team, referee=pattern_referee)
pattern_free_throw_made = r"^{player} Free Throw {free_throw_type} {points}$".format(player=pattern_player,free_throw_type=pattern_free_throw_type,points=pattern_points)
pattern_free_throw_miss = r"^MISS {player} Free Throw {free_throw_type}$".format(player=pattern_player,free_throw_type=pattern_free_throw_type)
pattern_jump_ball = r"^Jump Ball {player_home} vs. {player_away}: Tip to( {player_tip})?$".format(player_home=pattern_player.replace('player','player_home'),
    player_away=pattern_player.replace('player','player_away'),
    player_tip=pattern_player.replace('player','player_tip'))
pattern_rebound_player = r"^{player} REBOUND \(Off:(?P<offensive>\d+) Def:(?P<defensive>\d+)\)$".format(player=pattern_player)
pattern_steal = r"^{player}\s{{1,2}}?STEAL \((?P<steals>\d+) STL\)$".format(player=pattern_player)
pattern_substitution = r"^SUB: {player_in} FOR {player_out}$".format(
    player_in=pattern_player.replace('player','player_in'),player_out=pattern_player.replace('player','player_out'))
pattern_turnover_player = r"^{player}\s{{1,2}}?(?P<turnover_type>[\w+?\-? ]*) (Turnover[ ]?)+ \(P(?P<personal>\d+)\.T(?P<team>\d+)\)$".format(player=pattern_player)
pattern_violation = r"^{player} Violation:(?P<violation_type>\w+\s?\w+)\s\({referee}\)$".format(player=pattern_player, referee=pattern_referee)

# compiled regex for all playbyplay and playbyplayv2 HOMEDESCRIPTION & VISITORDESCRIPTION fields 
re_block = re.compile(pattern_block)
re_ejection = re.compile(pattern_ejection)
re_field_goal_made = re.compile(pattern_field_goal_made)
re_field_goal_missed = re.compile(pattern_field_goal_missed)
re_free_throw_made = re.compile(pattern_free_throw_made)
re_free_throw_miss = re.compile(pattern_free_throw_miss)
re_foul_player = re.compile(pattern_foul_player)
re_foul_team = re.compile(pattern_foul_team)
re_rebound_player = re.compile(pattern_rebound_player)
re_rebound_team = re.compile(pattern_rebound_team)
re_turnover_player = re.compile(pattern_turnover_player)
re_turnover_team = re.compile(pattern_turnover_team)
re_steal = re.compile(pattern_steal)
re_substitution = re.compile(pattern_substitution)
re_timeout = re.compile(pattern_timeout)
re_violation = re.compile(pattern_violation)
re_jump_ball = re.compile(pattern_jump_ball)

eventmsgtype_to_re = defaultdict(list, {
    EventMsgType.EJECTION : [re_ejection],
    EventMsgType.FIELD_GOAL_MADE : [re_field_goal_made],
    EventMsgType.FIELD_GOAL_MISSED : [re_field_goal_missed, re_block],
    EventMsgType.FREE_THROW : [re_free_throw_made, re_free_throw_miss],
    EventMsgType.REBOUND : [re_rebound_player, re_rebound_team],
    EventMsgType.TURNOVER : [re_turnover_player, re_steal, re_turnover_team],
    EventMsgType.FOUL : [re_foul_player, re_foul_team],
    EventMsgType.VIOLATION : [re_violation],
    EventMsgType.SUBSTITUTION : [re_substitution],
    EventMsgType.TIMEOUT : [re_timeout],
    EventMsgType.JUMP_BALL : [re_jump_ball]})