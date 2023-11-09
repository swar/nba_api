import pytest
from nba_api.stats.library.playbyplayregex import *
from data_playbyplayregex import playbyplay


# BLOCK
@pytest.mark.parametrize("play", playbyplay["Block"])
def test_block_player(play):
    #  Validate Pattern
    assert re_block.match(play["description"])

    #  Get Capture Groups
    search_result = re_block.search(play["description"])

    #  Player Name
    player = search_result.group("player")
    assert player == play["player"]

    #  Player
    block = search_result.group("blocks")
    assert block == play["blocks"]


# EJECTION
@pytest.mark.parametrize("play", playbyplay["Ejection"])
def test_ejection_player(play):
    #  Validate Pattern
    assert re_ejection.match(play["description"])

    #  Get Capture Groups
    search_result = re_ejection.search(play["description"])

    #  Player Name
    player = search_result.group("player")
    assert player == play["player"]

    # Ejection Type
    ejection_type = search_result.group("ejection_type")
    assert ejection_type == play["ejection_type"]


# FIELD GOAL MADE
@pytest.mark.parametrize("play", playbyplay["FieldGoalMade"])
def test_field_goal_made(play):
    # Validate Pattern
    assert re_field_goal_made.match(play["description"])

    # Get Capture Groups
    search_result = re_field_goal_made.search(play["description"])

    # Field Goal Type
    field_goal_type = search_result.group("field_goal_type")
    assert field_goal_type == play["field_goal_type"]

    # Player Name
    player = search_result.group("player")
    assert player == play["player"]

    # Disatance
    distance = search_result.group("distance")
    assert distance == play["distance"]

    # Points
    points = search_result.group("points")
    assert points == play["points"]

    # Player Name Assist
    player = search_result.group("player_ast")
    assert player == play["player_ast"]

    # Assists
    points = search_result.group("assists")
    assert points == play["assists"]


# FIELD GOAL MISSED
@pytest.mark.parametrize("play", playbyplay["FieldGoalMissed"])
def test_field_goal_missed(play):
    # Validate Pattern
    assert re_field_goal_missed.match(play["description"])

    # Get Capture Groups
    search_result = re_field_goal_missed.search(play["description"])

    # Field Goal Type
    field_goal_type = search_result.group("field_goal_type")
    assert field_goal_type == play["field_goal_type"]

    # Player Name
    player = search_result.group("player")
    assert player == play["player"]

    # Distance
    distance = search_result.group("distance")
    assert distance == play["distance"]


# FOUL PLAYER
@pytest.mark.parametrize("play", playbyplay["FoulPlayer"])
def test_foul_player(play):
    # Validate Pattern
    assert re_foul_player.match(play["description"])

    # Get Capture Groups
    search_result = re_foul_player.search(play["description"])

    # Player Name
    player = search_result.group("player")
    assert player == play["player"]

    # Foul Type
    foul_type = search_result.group("foul_type")
    assert foul_type == play["foul_type"]

    # Player
    player = search_result.group("personal")
    assert player == play["personal"]

    # Team Count
    team = search_result.group("team")
    assert team == play["team"]

    # Referee
    referee = search_result.group("referee")
    assert referee == play["referee"]


# FOUL TEAM
@pytest.mark.parametrize("play", playbyplay["FoulTeam"])
def test_foul_team(play):
    # Validate Pattern
    assert re_foul_team.match(play["description"])

    # Get Capture Groups
    search_result = re_foul_team.search(play["description"])

    # Player Name
    player = search_result.group("player")
    assert player == play["player"]

    # Team Name
    player = search_result.group("team")
    assert player == play["team"]

    # Foul Type
    foul_type = search_result.group("foul_type")
    assert foul_type == play["foul_type"]

    # Referee
    referee = search_result.group("referee")
    assert referee == play["referee"]


# FREE THROW MADE
@pytest.mark.parametrize("play", playbyplay["FreeThrowMade"])
def test_free_throw_made(play):
    # Validate Pattern
    assert re_free_throw_made.match(play["description"])

    # Get Capture Groups
    search_result = re_free_throw_made.search(play["description"])

    # Player Name
    player = search_result.group("player")
    assert player == play["player"]

    # Free Throw Type
    free_throw_type = search_result.group("free_throw_type")
    assert free_throw_type == play["free_throw_type"]

    # Points
    points = search_result.group("points")
    assert points == play["points"]


# FREE THROW MISSED
@pytest.mark.parametrize("play", playbyplay["FreeThrowMissed"])
def test_free_throw_missed(play):
    # Validate Pattern
    assert re_free_throw_miss.match(play["description"])

    # Get Capture Groups
    search_result = re_free_throw_miss.search(play["description"])

    # Player Name
    player = search_result.group("player")
    assert player == play["player"]

    # Free Throw Type
    free_throw_type = search_result.group("free_throw_type")
    assert free_throw_type == play["free_throw_type"]


# JUMP BALL
@pytest.mark.parametrize("play", playbyplay["JumpBall"])
def test_jump_ball(play):
    # Validate Pattern
    assert re_jump_ball.match(play["description"])

    # Get Capture Groups
    search_result = re_jump_ball.search(play["description"])

    # Player Name
    player = search_result.group("player_home")
    assert player == play["player_home"]

    # Player Name
    player = search_result.group("player_away")
    assert player == play["player_away"]

    # Player Name
    player = search_result.group("player_tip")
    assert player == play["player_tip"]


# REBOUND PLAYER
@pytest.mark.parametrize("play", playbyplay["ReboundPlayer"])
def test_rebound_player(play):
    # Validate Pattern
    assert re_rebound_player.match(play["description"])

    # Get Capture Groups
    search_result = re_rebound_player.search(play["description"])

    # Player Name
    player = search_result.group("player")
    assert player == play["player"]

    # Offensive
    offensive = search_result.group("offensive")
    assert offensive == play["offensive"]

    # Defensive
    defensive = search_result.group("defensive")
    assert defensive == play["defensive"]


# REBOUND TEAM
@pytest.mark.parametrize("play", playbyplay["ReboundTeam"])
def test_rebound_team(play):
    # Validate Pattern
    assert re_rebound_team.match(play["description"])

    # Get Capture Groups
    search_result = re_rebound_team.search(play["description"])

    # Team Name
    team = search_result.group("team")
    assert team == play["team"]


# STEAL
@pytest.mark.parametrize("play", playbyplay["Steal"])
def test_steal_player(play):
    # Validate Pattern
    assert re_steal.match(play["description"])

    # Get Capture Groups
    search_result = re_steal.search(play["description"])

    # Player Name
    player = search_result.group("player")
    assert player == play["player"]

    # Steals
    offensive = search_result.group("steals")
    assert offensive == play["steals"]


# SUBSTITUTION
@pytest.mark.parametrize("play", playbyplay["Substitution"])
def test_substitution(play):
    # Validate Pattern
    assert re_substitution.match(play["description"])

    # Get Capture Groups
    search_result = re_substitution.search(play["description"])

    # Player In Name
    player_in = search_result.group("player_in")
    assert player_in == play["player_in"]

    # Player Out Name
    player_out = search_result.group("player_out")
    assert player_out == play["player_out"]


# TIMEOUT
@pytest.mark.parametrize("play", playbyplay["Timeout"])
def test_timeout(play):
    # Validate Pattern
    assert re_timeout.match(play["description"])

    # Get Capture Groups
    search_result = re_timeout.search(play["description"])

    # Team Name
    team = search_result.group("team")
    assert team == play["team"]

    # Timeout type
    timeout_type = search_result.group("timeout_type")
    assert timeout_type == play["timeout_type"]

    # Full
    full = search_result.group("full")
    assert full == play["full"]

    # Short
    short = search_result.group("short")
    assert short == play["short"]


# TURNOVER PLAYER
@pytest.mark.parametrize("play", playbyplay["TurnoverPlayer"])
def test_turnover_player(play):
    # Validate Pattern
    assert re_turnover_player.match(play["description"])

    # Get Capture Groups
    search_result = re_turnover_player.search(play["description"])

    # Player Name
    player = search_result.group("player")
    assert player == play["player"]

    # Turnover Type
    turnover_type = search_result.group("turnover_type")
    assert turnover_type == play["turnover_type"]

    # Personal
    personal = search_result.group("personal")
    assert personal == play["personal"]

    # Team
    team = search_result.group("team")
    assert team == play["team"]


# TURNOVER TEAM
@pytest.mark.parametrize("play", playbyplay["TurnoverTeam"])
def test_turnover_team(play):
    # Validate Pattern
    assert re_turnover_team.match(play["description"])

    # Get Capture Groups
    search_result = re_turnover_team.search(play["description"])

    # Team Name
    team = search_result.group("team")
    assert team == play["team"]

    # Turnover Type
    team = search_result.group("turnover_type")
    assert team == play["turnover_type"]

    # Turnovers
    team = search_result.group("turnovers")
    assert team == play["turnovers"]


# VIOLATION
@pytest.mark.parametrize("play", playbyplay["Violation"])
def test_violation(play):
    #  Validate Pattern
    assert re_violation.match(play["description"])

    #  Get Capture Groups
    search_result = re_violation.search(play["description"])

    #  Violation
    violation_type = search_result.group("violation_type")
    assert violation_type == play["violation_type"]

    # Player Name
    player = search_result.group("player")
    assert player == play["player"]

    # Referee
    referee = search_result.group("referee")
    assert referee == play["referee"]


# VIOLATION TEAM
@pytest.mark.parametrize("play", playbyplay["ViolationTeam"])
def test_violation_team(play):
    # Validate Pattern
    assert re_violation_team.match(play["description"])

    # Get Capture Groups
    search_result = re_violation_team.search(play["description"])

    # Violation
    violation_type = search_result.group("violation_type")
    assert violation_type == play["violation_type"]

    # Team Name
    team = search_result.group("team")
    assert team == play["team"]
