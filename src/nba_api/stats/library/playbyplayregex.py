import re
from collections import defaultdict
from nba_api.stats.library.eventmsgtype import EventMsgType

# regex patterns for all playbyplay and playbyplayv2 HOMEDESCRIPTION & VISITORDESCRIPTION fields 
# note: regarding pattern_player_name_anomaly & "Mark Morris"
#   The majority of player names in the NBA traditionally follow patterns involving last name only with some prefix or suffix. 
#   In the context of a turnover, there is no solution for dealing with multiple names in conjunction with the turnover type
#   Example: "Mark Morris Lane Violation Turnover (P1.T6)" could be parsed many ways. While human readable, it's not regex friendly.
#   There are likely to be others. If you find one, please open an Issue or create a PR. The regex allows for multiple using the `(name name)|` format.
pattern_player_name_anomaly = r'(Mark Morris)|'
pattern_player_char = r'((?#char)(\. \w+)|(\-?\'?\w+))?'
pattern_player_suffix = r'((?#suffix)([\s](Jr\.|III|II|IV)))?'
pattern_player = r"(?P<player>{player_name_anomaly}(\w+{player_char}{player_suffix}))".format(player_name_anomaly=pattern_player_name_anomaly,
    player_char=pattern_player_char,player_suffix=pattern_player_suffix)
pattern_rebound_team = r'^(?P<team>\w+( \w+)?) Rebound$'
pattern_turnover_team = r'^(?P<team>\w+( \w+)?) Turnover: (?P<turnover_type>.*) \(T#(?P<turnovers>\d+)\)$'
pattern_timeout = r'^(?P<team>\w+( \w+)?) Timeout: ((?P<timeout_type>.*)) \(\w+( |\.)(?P<full>\d+) \w+ (?P<short>\d+)\)$'
pattern_block = r"^(?P<player>.+) BLOCK \((?P<blocks>\d+) BLK\)$"                    
pattern_ejection = r'^(?P<player>.+) Ejection:(?P<ejection_type>.*)$'
pattern_field_goal_made = r"^(?P<player>.+) (((?P<distance>\d+)\' )| )(?P<field_goal_type>[\w+( |\-)]*) \((?P<points>\d+) PTS\)( \((?P<player_ast>\D+) (?P<assists>\d+) AST\))?$"
pattern_field_goal_missed = r"^MISS (?P<player>.+) (((?P<distance>\d+)\' )| )(?P<field_goal_type>[\w+( |\-)]*)$"
pattern_foul_player = r"^(?P<player>.+) (?P<foul_type>.*)\s(?=(\(\w+(?P<personal>\d+)(\.\w+(?P<team>[\d|\w]+))?\)( \((?P<referee>.*)\))?)$)"
pattern_foul_team = r"^(?P<team>\w+( \w+)?) T.Foul \((?P<foul_type>.*) (?P<player>.+) \) (\((?P<referee>.*)\))"
pattern_free_throw_made = r"^(?P<player>.+) Free Throw (?P<free_throw_type>(.* )?(\d of \d)|\w+) \((?P<points>\d+) PTS\)$"
pattern_free_throw_miss = r"^MISS (?P<player>.+) Free Throw (?P<free_throw_type>(.* )?(\d of \d)|\w+)$"
pattern_jump_ball = r"^Jump Ball (?P<player_home>.+) vs. (?P<player_away>.+): Tip to( (?P<player_tip>.+))?$"
pattern_rebound_player = r"^(?P<player>.+) REBOUND \(Off:(?P<offensive>\d+) Def:(?P<defensive>\d+)\)$"
pattern_steal = r"^(?P<player>.+) STEAL \((?P<steals>\d+) STL\)$"
pattern_substitution = r"^SUB: (?P<player_in>.+) FOR (?P<player_out>.+)$"
pattern_turnover_player = r"^{player} (?P<turnover_type>[\w+?\-? ]*) (Turnover[ ]?)+ \(P(?P<personal>\d+)\.T(?P<team>\d+)\)$".format(player=pattern_player)
pattern_violation = r"^(?P<player>.+) Violation:(?P<violation_type>\w+\s?\w+)(\s\((?P<referee>.*)\))?$"
pattern_violation_team = r'^(?P<team>\w+( \w+)?) Violation: (?P<violation_type>.*) Violation$'


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
re_violation_team = re.compile(pattern_violation_team)


eventmsgtype_to_re = defaultdict(list, {
    EventMsgType.EJECTION : [re_ejection],
    EventMsgType.FIELD_GOAL_MADE : [re_field_goal_made],
    EventMsgType.FIELD_GOAL_MISSED : [re_field_goal_missed, re_block],
    EventMsgType.FREE_THROW : [re_free_throw_made, re_free_throw_miss],
    EventMsgType.REBOUND : [re_rebound_player, re_rebound_team],
    EventMsgType.TURNOVER : [re_turnover_player, re_steal, re_turnover_team],
    EventMsgType.FOUL : [re_foul_player, re_foul_team],
    EventMsgType.VIOLATION : [re_violation, re_violation_team],
    EventMsgType.SUBSTITUTION : [re_substitution],
    EventMsgType.TIMEOUT : [re_timeout],
    EventMsgType.JUMP_BALL : [re_jump_ball]})