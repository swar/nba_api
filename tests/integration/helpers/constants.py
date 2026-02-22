# Infrastructure params present on every endpoint; never test data.
INFRASTRUCTURE_PARAMS = {"proxy", "headers", "timeout", "get_request"}

# Canonical test values.
GAME_ID = "0022200552"  # Cavaliers vs. Bulls, 2023-01-03
PLAYER_ID = "1628378"  # Donovan Mitchell
ALT_PLAYER_ID = "1630596"  # Evan Mobley
TEAM_ID = "1610612739"  # Cleveland Cavaliers
ALT_TEAM_ID = "1610612759"  # San Antonio Spurs
COLLEGE = "Ohio State"
MINUTES_MIN = 10  # LeagueLineupViz minimum minutes filter

LINEUP = "201935-1628378-1628386-1629731-1630596"  # J. Harden - D. Mitchell - J. Allen - D. Wade - E. Mobley
LINEUP_GROUP_ID = f"-{LINEUP}-"
PLAYER_ID_LIST = f"-{LINEUP}-"
VS_PLAYER_ID_LIST = LINEUP

# Default values for required params, keyed by param name.
# Only params with no default in __init__ are resolved from here.
# Add new entries when an endpoint has an unrecognized required param.
PARAM_DEFAULTS = {
    "game_id": GAME_ID,
    "game_ids": GAME_ID,  # separate required param on CumeStats endpoints
    "player_id": PLAYER_ID,
    "person1_id": PLAYER_ID,
    "person2_id": PLAYER_ID,
    "player_id1": PLAYER_ID,
    "player_id2": PLAYER_ID,
    "player_id3": PLAYER_ID,
    "player_id4": PLAYER_ID,
    "player_id5": PLAYER_ID,
    "vs_player_id": ALT_PLAYER_ID,
    "vs_player_id1": ALT_PLAYER_ID,
    "vs_player_id2": ALT_PLAYER_ID,
    "vs_player_id3": ALT_PLAYER_ID,
    "vs_player_id4": ALT_PLAYER_ID,
    "vs_player_id5": ALT_PLAYER_ID,
    "player_id_list": PLAYER_ID_LIST,
    "vs_player_id_list": VS_PLAYER_ID_LIST,
    "team_id": TEAM_ID,
    "vs_team_id": ALT_TEAM_ID,
    "college": COLLEGE,
    "minutes_min": MINUTES_MIN,
    "group_id": LINEUP_GROUP_ID,
}
