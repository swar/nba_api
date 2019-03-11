import re

# regex patterns for all playbyplay and playbyplayv2 HOMEDESCRIPTION & VISITORDESCRIPTION fields 
player_name_char = r'((?#char)(\. \w+)|(\-?\'?\w+))?'
player_name_suffix = r'\s?((?#suffix)Jr.|Sr.|I|II|III|IV|V)?'

patterns = {
    'field_goal_type':  r'((?#field_goal_type)[\w+( |\-)]*)',
    'free_throw': r'Free Throw (?P<type>(\w+ )?(\d of \d)|\w+)',
    'player_name': r"((?#name)\w+{player_name_char}{player_name_suffix})".format(player_name_char=player_name_char,player_name_suffix=player_name_suffix),
    'rebound_team': r'^((?#team)\w+( \w+)?) Rebound',
    'turnover_team': r'^(?<=Turnover: ).*(?= \()',
    'timeout': r'^\w+(\s\w+)? Timeout: ((?#timeout)\w+) \(\w+ \d+ \w+ \d+\)'}

patterns['block'] = r"^{player_name} BLOCK \(\d+ BLK\)".format(player_name=patterns['player_name'])
patterns['field_goal_made'] = r"^{player_name}\s{{1,2}}?((?#distance)\d+\')? {field_goal_type}\(((?#pts)\d+ PTS)\)( \({player_name}((?#ast)\d+ AST)\))?".format(player_name=patterns['player_name'],field_goal_type=patterns['field_goal_type'])
patterns['field_goal_missed'] = r"^MISS {player_name}\s{{1,2}}?((?#distance)\d+\')? {field_goal_type}".format(player_name=patterns['player_name'],field_goal_type=patterns['field_goal_type'])
patterns['foul'] = r"^{player_name} (?P<foul_type>.*)\s(?=(\(\w+\d+(\.\w+[\d|\w]+)?\) ((?#referee)\(\w.\w+\))))".format(player_name=patterns['player_name'])
patterns['free_throw_made'] = r"{player_name} {free_throw}".format(player_name=patterns['player_name'],free_throw=patterns['free_throw'])
patterns['free_throw_miss'] = r"^MISS {player_name} {free_throw}".format(player_name=patterns['player_name'],free_throw=patterns['free_throw'])
patterns['jump_ball'] = r"^Jump Ball {player_name} vs. {player_name}: Tip to {player_name}".format(player_name=patterns['player_name'])
patterns['rebound_player'] = r"^{player_name} REBOUND \(Off:\d+ Def:\d+\)".format(player_name=patterns['player_name'])
patterns['steal'] = r"^{player_name}\s{{1,2}}?(?P<steal>STEAL) \(\d+ STL\)".format(player_name=patterns['player_name'])
patterns['substitution'] = r"^SUB: {player_name} FOR {player_name}".format(player_name=patterns['player_name'])
patterns['turnover_player'] = r"^{player_name}\s{{1,2}}?(?P<turnover_type>[\w+?\-? ]*) (Turnover[ ]?)+ \(P\d+\.T\d+\)".format(player_name=patterns['player_name'])
patterns['violation'] = r"^{player_name} Violation:((?#violation)\w+\s?\w+)\s((?#referee)\(\w.\w+\))".format(player_name=patterns['player_name'])

# compiled regex for all playbyplay and playbyplayv2 HOMEDESCRIPTION & VISITORDESCRIPTION fields 
block =  re.compile(patterns['block'])
field_goal_made = re.compile(patterns['field_goal_made'])
field_goal_missed = re.compile(patterns['field_goal_missed'])
free_throw_made = re.compile(patterns['free_throw'])
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
