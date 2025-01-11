"""
NBA Play-by-Play Event Parser
----------------------------
This module provides regular expression patterns for parsing NBA play-by-play event descriptions.
All patterns and compiled regex objects maintain their original interface for backward compatibility.
"""

import re
from collections import defaultdict
from nba_api.stats.library.eventmsgtype import EventMsgType

# Base pattern components
# ----------------------
TEAM_NAME_PATTERN = r"(?P<team>\w+( \w+)?)"

# Player name components with original structure
pattern_player_name_anomaly = r"(Mark Morris)|da Silva|"
pattern_player_char = r"((?#char)(\. \w+)|(\-?\'?\w+))?"
pattern_player_suffix = r"((?#suffix)([\s](Jr\.|Sr\.|III|II|IV)))?"
pattern_player = (
    r"(?P<player>{player_name_anomaly}(\w+{player_char}{player_suffix}))".format(
        player_name_anomaly=pattern_player_name_anomaly,
        player_char=pattern_player_char,
        player_suffix=pattern_player_suffix,
    )
)

# Event patterns grouped by category
# --------------------------------

# Team-based patterns
pattern_rebound_team = rf"^{TEAM_NAME_PATTERN} Rebound$"
pattern_turnover_team = (
    rf"^{TEAM_NAME_PATTERN} Turnover: (?P<turnover_type>.*) \(T# ?(?P<turnovers>\d+)\)$"
)
pattern_timeout = (
    rf"^{TEAM_NAME_PATTERN} Timeout: (?P<timeout_type>.*) "
    r"\(\w+( |\.)(?P<full>\d+) \w+ (?P<short>\d+)\)$"
)
pattern_violation_team = (
    rf"^{TEAM_NAME_PATTERN} Violation: (?P<violation_type>.*) Violation$"
)

# Player-based scoring patterns
pattern_field_goal_made = (
    r"^{player} (((?P<distance>\d+)\' )| )?[ ]*(?P<field_goal_type>[\w+( |\-)]*) "
    r"\((?P<points>\d+) PTS\)( \((?P<player_ast>\D+) (?P<assists>\d+) AST\))?$"
).format(player=pattern_player)

pattern_field_goal_missed = (
    r"^MISS {player} ((?P<distance>\d+)\' )?[ ]*(?P<field_goal_type>[\w+( |\-)]*)$"
).format(player=pattern_player)

# Free throw patterns
pattern_free_throw_made = (
    r"^(?P<player>.+) Free Throw (?P<free_throw_type>(.* )?(\d of \d)|\w+) "
    r"\((?P<points>\d+) PTS\)$"
)
pattern_free_throw_miss = (
    r"^MISS (?P<player>.+) Free Throw (?P<free_throw_type>(.* )?(\d of \d)|\w+)$"
)

# Defensive and possession patterns
pattern_block = r"^(?P<player>.+) BLOCK \((?P<blocks>\d+) BLK\)$"
pattern_steal = r"^(?P<player>.+) STEAL \((?P<steals>\d+) STL\)$"
pattern_rebound_player = (
    r"^(?P<player>.+) REBOUND \(Off:(?P<offensive>\d+) Def:(?P<defensive>\d+)\)$"
)

# Foul and violation patterns
pattern_foul_player = (
    r"^(?P<player>.+) (?P<foul_type>.*)\s(?=(\(\w+(?P<personal>\d+)"
    r"(\.\w+(?P<team>[\d|\w]+))?\)( \((?P<referee>.*)\))?)$)"
)
pattern_foul_team = (
    r"^(?P<team>[A-Z]+( [A-Z]+)?) (T.Foul \()?((?P<foul_type>(.*)))?"
    r"(?(3)( {player} \) \((?P<referee>.*)\)))$"
).format(player=pattern_player)

pattern_violation = (
    r"^(?P<player>.+) Violation:(?P<violation_type>\w+\s?\w+)"
    r"(\s\((?P<referee>.*)\))?$"
)

# Other game events
pattern_substitution = r"^SUB: (?P<player_in>.+) FOR (?P<player_out>.+)$"
pattern_ejection = r"^(?P<player>.+) Ejection:(?P<ejection_type>.*)$"
pattern_jump_ball = (
    r"^(Jump Ball (?P<player_home>.+) vs. (?P<player_away>.+): "
    r"Tip to( (?P<player_tip>.+))?)|(\s*)$"
)
pattern_turnover_player = (
    r"^{player} (?P<turnover_type>[\w+?\-? ]*) (Turnover[ ]?)+ "
    r"\(P(?P<personal>\d+)\.T(?P<team>\d+)\)$"
).format(player=pattern_player)

# Compiled Regular Expressions
# --------------------------
# These regex objects are pre-compiled for performance and maintained as module-level
# variables for backward compatibility. Each regex corresponds to a specific play-by-play
# event type that might occur during an NBA game.
#
# Usage:
#   result = re_field_goal_made.match(description)
#   if result:
#       # Access named groups like distance, field_goal_type, points, etc.
#       field_goal_data = result.groupdict()

# Scoring-related regex
re_field_goal_made = re.compile(pattern_field_goal_made)     # Example: "Stephen Curry 26' 3PT Jump Shot (3 PTS)"
re_field_goal_missed = re.compile(pattern_field_goal_missed)  # Example: "MISS Stephen Curry 3PT Jump Shot"
re_free_throw_made = re.compile(pattern_free_throw_made)     # Example: "Stephen Curry Free Throw 1 of 2 (1 PTS)"
re_free_throw_miss = re.compile(pattern_free_throw_miss)     # Example: "MISS Stephen Curry Free Throw 2 of 2"

# Defensive plays
re_block = re.compile(pattern_block)           # Example: "Draymond Green BLOCK (2 BLK)"
re_steal = re.compile(pattern_steal)           # Example: "Chris Paul STEAL (1 STL)"
re_rebound_player = re.compile(pattern_rebound_player)  # Example: "Stephen Curry REBOUND (Off:1 Def:3)"
re_rebound_team = re.compile(pattern_rebound_team)     # Example: "Warriors Rebound"

# Violations and fouls
re_foul_player = re.compile(pattern_foul_player)     # Example: "Draymond Green P.FOUL (P1.T3) (J.Smith)"
re_foul_team = re.compile(pattern_foul_team)         # Example: "WARRIORS T.Foul (Defensive three seconds) (M.Davis)"
re_violation = re.compile(pattern_violation)         # Example: "Joel Embiid Violation:Lane"
re_violation_team = re.compile(pattern_violation_team)  # Example: "WARRIORS Violation: Delay of game"

# Turnovers
re_turnover_player = re.compile(pattern_turnover_player)  # Example: "Stephen Curry Bad Pass Turnover (P2.T5)"
re_turnover_team = re.compile(pattern_turnover_team)     # Example: "WARRIORS Turnover: Shot Clock (T#12)"

# Game management
re_substitution = re.compile(pattern_substitution)  # Example: "SUB: Andre Iguodala FOR Stephen Curry"
re_timeout = re.compile(pattern_timeout)         # Example: "WARRIORS Timeout: Regular (Reg.4 Short 0)"
re_jump_ball = re.compile(pattern_jump_ball)     # Example: "Jump Ball Embiid vs. Jokic: Tip to Harris"
re_ejection = re.compile(pattern_ejection)       # Example: "Draymond Green Ejection: Second Technical"

# Event Type to Regex Pattern Mapping
# -------------------------------
# Maps each NBA play-by-play event type to a list of regex patterns that could match it.
# Structure:
#   EventMsgType: [list of compiled regex patterns]
#
# Key behaviors:
# 1. Uses defaultdict(list) to return an empty list for any unmapped event type
# 2. Some events have multiple patterns because they can appear in different formats
#    or can trigger related events (e.g., a missed shot might have a block)
# 3. Order of patterns in lists matters - patterns are tried in order
#
# Common pattern groupings:
# - Single events: EJECTION, FIELD_GOAL_MADE, SUBSTITUTION, TIMEOUT, JUMP_BALL
# - Shot events: FIELD_GOAL_MISSED (includes blocks)
# - Possession changes: REBOUND (player or team), TURNOVER (includes steals)
# - Rules enforcement: FOUL (player or team), VIOLATION
# - Free throws: both makes and misses

eventmsgtype_to_re = defaultdict(
    list,
    {
        # Single event types - one straightforward pattern
        EventMsgType.EJECTION: [re_ejection],
        EventMsgType.FIELD_GOAL_MADE: [re_field_goal_made],

        # Complex events with potential secondary actions
        EventMsgType.FIELD_GOAL_MISSED: [re_field_goal_missed, re_block],  # Shot could be blocked
        EventMsgType.FREE_THROW: [re_free_throw_made, re_free_throw_miss],  # Both outcomes needed

        # Events that can be credited to either player or team
        EventMsgType.REBOUND: [re_rebound_player, re_rebound_team],
        EventMsgType.TURNOVER: [re_turnover_player, re_steal, re_turnover_team],  # Includes steals
        EventMsgType.FOUL: [re_foul_player, re_foul_team],
        EventMsgType.VIOLATION: [re_violation, re_violation_team],

        # Game management events
        EventMsgType.SUBSTITUTION: [re_substitution],
        EventMsgType.TIMEOUT: [re_timeout],
        EventMsgType.JUMP_BALL: [re_jump_ball],
    },
)
