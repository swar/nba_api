import re

# regex patterns for all playbyplay and playbyplayv2 HOMEDESCRIPTION & VISITORDESCRIPTION fields 
player_name_suffix = r'\s?((?#suffix)Jr.|Sr.|I|II|III|IV|V)?'
player_name_char = r'((?#char)(\. \w+)|(\-?\'?\w+))?'

patterns = {
    'field_goal_type':  r'((?#field_goal_type)[\w+( |\-)]*)',
    'free_throw': r'Free Throw (?P<type>(\w+ )?(\d of \d)|\w+)',
    'player_name': rf"((?#name)\w+{player_name_char}{player_name_suffix})",
    'rebound_team': r'^((?#team)\w+( \w+)?) Rebound',
    'turnover_team': r'^(?<=Turnover: ).*(?= \()',
    'timeout': r'^\w+(\s\w+)? Timeout: ((?#timeout)\w+) \(\w+ \d+ \w+ \d+\)'}

patterns['block'] = rf"^{patterns['player_name']} BLOCK \(\d+ BLK\)"
patterns['field_goal_made'] = rf"^{patterns['player_name']}\s{{1,2}}?((?#distance)\d+\')? {patterns['field_goal_type']}\(((?#pts)\d+ PTS)\)( \({patterns['player_name']}((?#ast)\d+ AST)\))?"
patterns['field_goal_missed'] = rf"^MISS {patterns['player_name']}\s{{1,2}}?((?#distance)\d+\')? {patterns['field_goal_type']}"
patterns['foul'] = rf"^{patterns['player_name']} (?P<foul_type>.*)\s(?=(\(\w+\d+(\.\w+[\d|\w]+)?\) ((?#referee)\(\w.\w+\))))"
patterns['free_throw_made'] = rf"{patterns['player_name']} {patterns['free_throw']}"
patterns['free_throw_miss'] = rf"^MISS {patterns['player_name']} {patterns['free_throw']}"
patterns['jump_ball'] = rf"^Jump Ball {patterns['player_name']} vs. {patterns['player_name']}: Tip to {patterns['player_name']}"
patterns['rebound_player'] = rf"^{patterns['player_name']} REBOUND \(Off:\d+ Def:\d+\)"
patterns['steal'] = rf"^{patterns['player_name']}\s{{1,2}}?(?P<steal>STEAL) \(\d+ STL\)"
patterns['substitution'] = rf"^SUB: {patterns['player_name']} FOR {patterns['player_name']}"
patterns['turnover_player'] = rf"^{patterns['player_name']}\s{{1,2}}?(?P<turnover_type>[\w+?\-? ]*) (Turnover[ ]?)+ \(P\d+\.T\d+\)"
patterns['violation'] = rf"^{patterns['player_name']} Violation:((?#violation)\w+\s?\w+)\s((?#referee)\(\w.\w+\))"

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
