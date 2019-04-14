import re

# regex patterns for all playbyplay and playbyplayv2 HOMEDESCRIPTION & VISITORDESCRIPTION fields 
pattern_player_name_char = r'((?#char)(\. \w+)|(\-?\'?\w+))?'
pattern_player_name_suffix = r'((?#suffix)([\s](Jr\.|III|II|IV)))?'
pattern_team_name = r'(?P<team_name>\w+( \w+)?)'
pattern_field_goal_type = r'(?P<field_goal_type>[\w+( |\-)]*)'
pattern_free_throw_type = r'(?P<free_throw_type>(\w+ )?(\d of \d)|\w+)'
pattern_player_name = r"(?P<player_name>\w+{player_name_char}{player_name_suffix})".format(player_name_char=pattern_player_name_char,player_name_suffix=pattern_player_name_suffix)
pattern_points = r"\((?P<points>\d+) PTS\)"
pattern_rebound_team = r'^{team_name} Rebound$'.format(team_name=pattern_team_name)
pattern_turnover_team = r'^{team_name} Turnover: (?P<turnover_type>\w+\s?\w+) \(T#(?P<turnovers>\d.)\)$'.format(team_name=pattern_team_name)
pattern_timeout = r'^{team_name} Timeout: ((?P<timeout_type>\w+)) \(\w+ (?P<full>\d+) \w+ (?P<short>\d+)\)$'.format(team_name=pattern_team_name)
pattern_block = r"^{player_name} BLOCK \((?P<blocks>\d+) BLK\)$".format(player_name=pattern_player_name)                    
pattern_field_goal_made = r"^{player_name}\s{{1,2}}?((?P<distance>\d+)\' )?{field_goal_type} {points}( \({player_name_ast} (?P<assists>\d+) AST\))?$".format(
    player_name=pattern_player_name,player_name_ast=pattern_player_name.replace('player_name','player_name_ast'), field_goal_type=pattern_field_goal_type,points=pattern_points)
pattern_field_goal_missed = r"^MISS {player_name}\s{{1,2}}?((?P<distance>\d+)\' )?{field_goal_type}$".format(player_name=pattern_player_name,field_goal_type=pattern_field_goal_type)
pattern_foul = r"^{player_name} (?P<foul_type>.*)\s(?=(\(\w+(?P<personal>\d+)(\.\w+(?P<team>[\d|\w]+))?\) (\((?P<referee>\w.\w+)\)))$)".format(player_name=pattern_player_name)
pattern_free_throw_made = r"{player_name} Free Throw {free_throw_type} {points}$".format(player_name=pattern_player_name,free_throw_type=pattern_free_throw_type,points=pattern_points)
pattern_free_throw_miss = r"^MISS {player_name} Free Throw {free_throw_type}$".format(player_name=pattern_player_name,free_throw_type=pattern_free_throw_type)
pattern_jump_ball = r"^Jump Ball {player_name_home} vs. {player_name_away}: Tip to {player_name_tip}$".format(player_name_home=pattern_player_name.replace('player_name','player_name_home'),
    player_name_away=pattern_player_name.replace('player_name','player_name_away'),
    player_name_tip=pattern_player_name.replace('player_name','player_name_tip'))
pattern_rebound_player = r"^{player_name} REBOUND \(Off:(?P<offensive>\d+) Def:(?P<defensive>\d+)\)$".format(player_name=pattern_player_name)
pattern_steal = r"^{player_name}\s{{1,2}}?STEAL \((?P<steals>\d+) STL\)$".format(player_name=pattern_player_name)
pattern_substitution = r"^SUB: {player_name_in} FOR {player_name_out}$".format(
    player_name_in=pattern_player_name.replace('player_name','player_name_in'),player_name_out=pattern_player_name.replace('player_name','player_name_out'))
pattern_turnover_player = r"^{player_name}\s{{1,2}}?(?P<turnover_type>[\w+?\-? ]*) (Turnover[ ]?)+ \(P(?P<personal>\d+)\.T(?P<team>\d+)\)$".format(player_name=pattern_player_name)
pattern_violation = r"^{player_name} Violation:(?P<violation_type>\w+\s?\w+)\s\((?P<referee>\w.\w+)\)$".format(player_name=pattern_player_name)

# compiled regex for all playbyplay and playbyplayv2 HOMEDESCRIPTION & VISITORDESCRIPTION fields 
re_block = re.compile(pattern_block)
re_field_goal_made = re.compile(pattern_field_goal_made)
re_field_goal_missed = re.compile(pattern_field_goal_missed)
re_free_throw_made = re.compile(pattern_free_throw_made)
re_free_throw_miss = re.compile(pattern_free_throw_miss)
re_foul = re.compile(pattern_foul)
re_rebound_player = re.compile(pattern_rebound_player)
re_rebound_team = re.compile(pattern_rebound_team)
re_turnover_player = re.compile(pattern_turnover_player)
re_turnover_team = re.compile(pattern_turnover_team)
re_steal = re.compile(pattern_steal)
re_substitution = re.compile(pattern_substitution)
re_timeout = re.compile(pattern_timeout)
re_violation = re.compile(pattern_violation)
re_jump_ball = re.compile(pattern_jump_ball)