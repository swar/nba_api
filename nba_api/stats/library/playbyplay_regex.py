import re

# regex patterns for all playbyplay and playbyplayv2 HOMEDESCRIPTION & VISITORDESCRIPTION fields 
player_name_char = r'((?#char)(\. \w+)|(\-?\'?\w+))?'
player_name_suffix = r'((?#suffix)([\s](Jr\.|III|II|IV)))?'
team_name = r'(?P<team_name>\w+( \w+)?)'

patterns = {
    'field_goal_type':  r'(?P<field_goal_type>[\w+( |\-)]*)',
    'free_throw_type': r'(?P<free_throw_type>(\w+ )?(\d of \d)|\w+)',
    'player_name': r"(?P<player_name>\w+{player_name_char}{player_name_suffix})".format(player_name_char=player_name_char,player_name_suffix=player_name_suffix),
    'points': r"\((?P<points>\d+) PTS\)",
    'rebound_team': r'^{team_name} Rebound$'.format(team_name=team_name),
    'turnover_team': r'^{team_name} Turnover: (?P<turnover_type>\w+\s?\w+) \(T#(?P<turnovers>\d.)\)$'.format(team_name=team_name),
    'timeout': r'^{team_name} Timeout: ((?P<timeout_type>\w+)) \(\w+ (?P<full>\d+) \w+ (?P<short>\d+)\)$'.format(team_name=team_name)}

patterns['block'] = r"^{player_name} BLOCK \((?P<blocks>\d+) BLK\)$".format(player_name=patterns['player_name'])                                
patterns['field_goal_made'] = r"^{player_name}\s{{1,2}}?((?P<distance>\d+)\' )?{field_goal_type} {points}( \({player_name_ast} (?P<assists>\d+) AST\))?$".format(
    player_name=patterns['player_name'],player_name_ast=patterns['player_name'].replace('player_name','player_name_ast'),
    field_goal_type=patterns['field_goal_type'],points=patterns['points'])
patterns['field_goal_missed'] = r"^MISS {player_name}\s{{1,2}}?((?P<distance>\d+)\' )?{field_goal_type}$".format(player_name=patterns['player_name'],field_goal_type=patterns['field_goal_type'])
patterns['foul'] = r"^{player_name} (?P<foul_type>.*)\s(?=(\(\w+(?P<personal>\d+)(\.\w+(?P<team>[\d|\w]+))?\) (\((?P<referee>\w.\w+)\)))$)".format(player_name=patterns['player_name'])
patterns['free_throw_made'] = r"{player_name} Free Throw {free_throw_type} {points}$".format(player_name=patterns['player_name'],
    free_throw_type=patterns['free_throw_type'],points=patterns['points'])
patterns['free_throw_miss'] = r"^MISS {player_name} Free Throw {free_throw_type}$".format(player_name=patterns['player_name'],
    free_throw_type=patterns['free_throw_type'])
patterns['jump_ball'] = r"^Jump Ball {player_name_home} vs. {player_name_away}: Tip to {player_name_tip}$".format(
    player_name_home=patterns['player_name'].replace('player_name','player_name_home'),player_name_away=patterns['player_name'].replace('player_name','player_name_away'),
    player_name_tip=patterns['player_name'].replace('player_name','player_name_tip'))
patterns['rebound_player'] = r"^{player_name} REBOUND \(Off:(?P<offensive>\d+) Def:(?P<defensive>\d+)\)$".format(player_name=patterns['player_name'])
patterns['steal'] = r"^{player_name}\s{{1,2}}?STEAL \((?P<steals>\d+) STL\)$".format(player_name=patterns['player_name'])
patterns['substitution'] = r"^SUB: {player_name_in} FOR {player_name_out}$".format(
    player_name_in=patterns['player_name'].replace('player_name','player_name_in'),player_name_out=patterns['player_name'].replace('player_name','player_name_out'))
patterns['turnover_player'] = r"^{player_name}\s{{1,2}}?(?P<turnover_type>[\w+?\-? ]*) (Turnover[ ]?)+ \(P(?P<personal>\d+)\.T(?P<team>\d+)\)$".format(player_name=patterns['player_name'])
patterns['violation'] = r"^{player_name} Violation:(?P<violation_type>\w+\s?\w+)\s\((?P<referee>\w.\w+)\)$".format(player_name=patterns['player_name'])

# compiled regex for all playbyplay and playbyplayv2 HOMEDESCRIPTION & VISITORDESCRIPTION fields 
re_block =  re.compile(patterns['block'])
re_field_goal_made = re.compile(patterns['field_goal_made'])
re_field_goal_missed = re.compile(patterns['field_goal_missed'])
re_free_throw_made = re.compile(patterns['free_throw_made'])
re_free_throw_miss = re.compile(patterns['free_throw_miss'])
re_foul = re.compile(patterns['foul'])
re_rebound_player = re.compile(patterns['rebound_player'])
re_rebound_team = re.compile(patterns['rebound_team'])
re_turnover_player = re.compile(patterns['turnover_player'])
re_turnover_team = re.compile(patterns['turnover_team'])
re_steal = re.compile(patterns['steal'])
re_substitution = re.compile(patterns['substitution'])
re_timeout = re.compile(patterns['timeout'])
re_violation = re.compile(patterns['violation'])
re_jump_ball = re.compile(patterns['jump_ball'])
