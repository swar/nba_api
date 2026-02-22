# Infrastructure params present on every endpoint; never test data.
INFRASTRUCTURE_PARAMS = {"proxy", "headers", "timeout", "get_request"}

# Canonical test values.
GAME_ID = "0021700807"  # Cavaliers vs. Celtics, 2017-18 regular season
PLAYER_ID = "2544"  # LeBron James
ALT_PLAYER_ID = "202681"  # Kyrie Irving
TEAM_ID = "1610612739"  # Cleveland Cavaliers
ALT_TEAM_ID = "1610612765"  # New Orleans Pelicans
COLLEGE = "Ohio State"
MINUTES_MIN = 10  # LeagueLineupViz minimum minutes filter
LINEUP_GROUP_ID = "-202689-203493-203501-1626174-1627827-"  # ShotChartLineupDetail
PLAYER_ID_LIST = "202681,203078,2544,201567,203954"
VS_PLAYER_ID_LIST = "201566,201939,201935,201142,203076"

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
