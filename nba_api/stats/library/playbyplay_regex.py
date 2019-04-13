import re

# regex patterns for all playbyplay and playbyplayv2 HOMEDESCRIPTION & VISITORDESCRIPTION fields 
player_name_char = r'((?#char)(\. \w+)|(\-?\'?\w+))?'
player_name_suffix = r'\s?((?#suffix)Jr.|Sr.|I|II|III|IV|V)?'

patterns = {
    'field_goal_type':  r'(?P<field_goal_type>[\w+( |\-)]*)',
    'free_throw_type': r'(?P<free_throw_type>(\w+ )?(\d of \d)|\w+)',
    'player_name': r"(?P<player_name>\w+{player_name_char}{player_name_suffix})".format(player_name_char=player_name_char,player_name_suffix=player_name_suffix),
    'points': r"\((?P<points>\d+) PTS\)",
    'rebound_team': r'^(?P<team_name>\w+( \w+)?) Rebound',
    'turnover_team': r'^(?<=Turnover: ).*(?= \()',
    'timeout': r'^\w+(\s\w+)? Timeout: ((?#timeout)\w+) \(\w+ \d+ \w+ \d+\)'}

patterns['block'] = r"^{player_name} BLOCK \((?P<blocks>\d+) BLK\)".format(player_name=patterns['player_name'])                                
patterns['field_goal_made'] = r"^{player_name}\s{{1,2}}?((?P<distance>\d+)\' )?{field_goal_type} {points}( \({player_name_ast} (?P<assists>\d+) AST\))?".format(
    player_name=patterns['player_name'],player_name_ast=patterns['player_name'].replace('player_name','player_name_ast'),
    field_goal_type=patterns['field_goal_type'],points=patterns['points'])
patterns['field_goal_missed'] = r"^MISS {player_name}\s{{1,2}}?((?P<distance>\d+)\' )?{field_goal_type}".format(player_name=patterns['player_name'],field_goal_type=patterns['field_goal_type'])
patterns['foul'] = r"^{player_name} (?P<foul_type>.*)\s(?=(\(\w+\d+(\.\w+[\d|\w]+)?\) ((?#referee)\(\w.\w+\))))".format(player_name=patterns['player_name'])
patterns['free_throw_made'] = r"{player_name} Free Throw {free_throw_type} {points}".format(player_name=patterns['player_name'],
    free_throw_type=patterns['free_throw_type'],points=patterns['points'])
patterns['free_throw_miss'] = r"^MISS {player_name} Free Throw {free_throw_type}".format(player_name=patterns['player_name'],
    free_throw_type=patterns['free_throw_type'])
patterns['jump_ball'] = r"^Jump Ball {player_name_1} vs. {player_name_2}: Tip to {player_name_tip}".format(
    player_name_1=patterns['player_name'].replace('player_name','player_name_1'),player_name_2=patterns['player_name'].replace('player_name','player_name_2'),
    player_name_tip=patterns['player_name'].replace('player_name','player_name_tip'))
patterns['rebound_player'] = r"^{player_name} REBOUND \(Off:(?P<offensive>\d+) Def:(?P<defensive>\d+)\)".format(player_name=patterns['player_name'])
patterns['steal'] = r"^{player_name}\s{{1,2}}?(?P<steals>STEAL) \(\d+ STL\)".format(player_name=patterns['player_name'])
patterns['substitution'] = r"^SUB: {player_name_sub} FOR {player_name_for}".format(
    player_name_sub=patterns['player_name'].replace('player_name','player_name_sub'),player_name_for=patterns['player_name'].replace('player_name_for','player_name_for'))
patterns['turnover_player'] = r"^{player_name}\s{{1,2}}?(?P<turnover_type>[\w+?\-? ]*) (Turnover[ ]?)+ \(P\d+\.T\d+\)".format(player_name=patterns['player_name'])
patterns['violation'] = r"^{player_name} Violation:(?P<violation>\w+\s?\w+)\s(?P<referee>\(\w.\w+\))".format(player_name=patterns['player_name'])

# compiled regex for all playbyplay and playbyplayv2 HOMEDESCRIPTION & VISITORDESCRIPTION fields 
block =  re.compile(patterns['block'])
field_goal_made = re.compile(patterns['field_goal_made'])
field_goal_missed = re.compile(patterns['field_goal_missed'])
free_throw_made = re.compile(patterns['free_throw_made'])
free_throw_miss = re.compile(patterns['free_throw_miss'])
foul = re.compile(patterns['foul'])
rebound_player = re.compile(patterns['rebound_player'])
rebound_team = re.compile(patterns['rebound_team'])
turnover_player = re.compile(patterns['turnover_player'])
turnover_team = re.compile(patterns['turnover_team'])
steal = re.compile(patterns['steal'])
substitution = re.compile(patterns['substitution'])
timeout = re.compile(patterns['timeout'])
violation = re.compile(patterns['violation'])
jump_ball = re.compile(patterns['jump_ball'])
