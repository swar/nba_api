from collections import defaultdict

playbyplay = defaultdict(list)

# Block
playbyplay["Block"].append(
    {"description": "Collins BLOCK (1 BLK)", "player": "Collins", "blocks": "1"}
)

# Ejection
playbyplay["Ejection"].append(
    {
        "description": "Robinson Ejection:Second Technical",
        "player": "Robinson",
        "ejection_type": "Second Technical",
    }
)

# Field Goal Made (With Assist)
playbyplay["FieldGoalMade"].append(
    {
        "description": "S. Hill 24' 3PT Jump Shot (3 PTS) (Mahinmi 1 AST)",
        "player": "S. Hill",
        "distance": "24",
        "field_goal_type": "3PT Jump Shot",
        "points": "3",
        "player_ast": "Mahinmi",
        "assists": "1",
    }
)

# Field Goal Made (Without Assist)
playbyplay["FieldGoalMade"].append(
    {
        "description": "Aldridge 6' Turnaround Hook Shot (8 PTS)",
        "player": "Aldridge",
        "distance": "6",
        "field_goal_type": "Turnaround Hook Shot",
        "points": "8",
        "player_ast": None,
        "assists": None,
    }
)

# Field Goal Made (Without Distance & With Double Space)
playbyplay["FieldGoalMade"].append(
    {
        "description": "Broekhoff  3PT Jump Shot (3 PTS) (Lee 2 AST)",
        "player": "Broekhoff",
        "distance": None,
        "field_goal_type": "3PT Jump Shot",
        "points": "3",
        "player_ast": "Lee",
        "assists": "2",
    }
)

# Field Goal Made (Without Distance & With Single Space)
playbyplay["FieldGoalMade"].append(
    {
        "description": "Portis Tip Layup Shot (5 PTS)",
        "player": "Portis",
        "distance": None,
        "field_goal_type": "Tip Layup Shot",
        "points": "5",
        "player_ast": None,
        "assists": None,
    }
)

# Field Goal Missed
playbyplay["FieldGoalMissed"].append(
    {
        "description": "MISS O'Quinn 17' Jump Shot",
        "player": "O'Quinn",
        "distance": "17",
        "field_goal_type": "Jump Shot",
    }
)

# Field Goal Missed (Without Disstance & With Double Space)
playbyplay["FieldGoalMissed"].append(
    {
        "description": "MISS O'Quinn  3PT Jump Shot",
        "player": "O'Quinn",
        "distance": None,
        "field_goal_type": "3PT Jump Shot",
    }
)

# Field Goal Missed (Without Disstance & With Single Space)
playbyplay["FieldGoalMissed"].append(
    {
        "description": "MISS O'Quinn 3PT Jump Shot",
        "player": "O'Quinn",
        "distance": None,
        "field_goal_type": "3PT Jump Shot",
    }
)

# Foul Player
playbyplay["FoulPlayer"].append(
    {
        "description": "Collison P.FOUL (P1.TN) (M.Lindsay)",
        "player": "Collison",
        "foul_type": "P.FOUL",
        "personal": "1",
        "team": "N",
        "referee": "M.Lindsay",
    }
)

# Foul Player (Without Referee)
playbyplay["FoulPlayer"].append(
    {
        "description": "Jamison P.FOUL (P4.PN)",
        "player": "Jamison",
        "foul_type": "P.FOUL",
        "personal": "4",
        "team": "N",
        "referee": None,
    }
)

# Foul Team
playbyplay["FoulTeam"].append(
    {
        "description": "BUCKS T.Foul (Def. 3 Sec Lopez ) (M.Callahan)",
        "team": "BUCKS",
        "foul_type": "Def. 3 Sec",
        "player": "Lopez",
        "referee": "M.Callahan",
    }
)

# Foul Team
playbyplay["FoulTeam"].append(
    {
        "description": "BUCKS T.Foul (Def. 3 Sec Lopez Jr. ) (M.Callahan)",
        "team": "BUCKS",
        "foul_type": "Def. 3 Sec",
        "player": "Lopez Jr.",
        "referee": "M.Callahan",
    }
)

# Foul Team
playbyplay["FoulTeam"].append(
    {
        "description": "MAVERICKS Delay",
        "team": "MAVERICKS",
        "foul_type": "Delay",
        "player": None,
        "referee": None,
    }
)

# Free Throw Made
playbyplay["FreeThrowMade"].append(
    {
        "description": "Sumner Free Throw 2 of 2 (1 PTS)",
        "player": "Sumner",
        "free_throw_type": "2 of 2",
        "points": "1",
    }
)

# Free Throw Made (Clear Path 1 of 2)
playbyplay["FreeThrowMade"].append(
    {
        "description": "Powell Free Throw Clear Path 1 of 2 (18 PTS)",
        "player": "Powell",
        "free_throw_type": "Clear Path 1 of 2",
        "points": "18",
    }
)

# Free Throw Missed
playbyplay["FreeThrowMissed"].append(
    {
        "description": "MISS Prince Free Throw 1 of 2",
        "player": "Prince",
        "free_throw_type": "1 of 2",
    }
)

# Jump Ball
playbyplay["JumpBall"].append(
    {
        "description": "Jump Ball Collins vs. O'Quinn: Tip to Leaf",
        "player_home": "Collins",
        "player_away": "O'Quinn",
        "player_tip": "Leaf",
    }
)

# Jump Ball (Without player_tip)
playbyplay["JumpBall"].append(
    {
        "description": "Jump Ball Green vs. McKinnie: Tip to",
        "player_home": "Green",
        "player_away": "McKinnie",
        "player_tip": None,
    }
)

# Jump Ball (With single space in description)
playbyplay["JumpBall"].append(
    {"description": " ", "player_home": None, "player_away": None, "player_tip": None}
)

# Jump Ball (With multiple spaces in description)
playbyplay["JumpBall"].append(
    {"description": "  ", "player_home": None, "player_away": None, "player_tip": None}
)

# Jump Ball (With empty description)
playbyplay["JumpBall"].append(
    {"description": "", "player_home": None, "player_away": None, "player_tip": None}
)

# Rebound Player
playbyplay["ReboundPlayer"].append(
    {
        "description": "Zubac REBOUND (Off:2 Def:4)",
        "player": "Zubac",
        "offensive": "2",
        "defensive": "4",
    }
)

# Rebound Team (One Word)
playbyplay["ReboundTeam"].append(
    {"description": "Timberwolves Rebound", "team": "Timberwolves"}
)

# Rebound Team (Two Words)
playbyplay["ReboundTeam"].append(
    {"description": "TRAIL BLAZERS Rebound", "team": "TRAIL BLAZERS"}
)

# Steal
playbyplay["Steal"].append(
    {"description": "Bradley STEAL (2 STL)", "player": "Bradley", "steals": "2"}
)

# Substitution
playbyplay["Substitution"].append(
    {
        "description": "SUB: Sefolosha FOR Ingles",
        "player_in": "Sefolosha",
        "player_out": "Ingles",
    }
)

# Timeout
playbyplay["Timeout"].append(
    {
        "description": "TRAIL BLAZERS Timeout: Regular (Full 5 Short 0)",
        "team": "TRAIL BLAZERS",
        "timeout_type": "Regular",
        "full": "5",
        "short": "0",
    }
)

# Timeout (multiple words in timeout_time)
playbyplay["Timeout"].append(
    {
        "description": "LAKERS Timeout: Coach Challenge (Full 2 Short 0)",
        "team": "LAKERS",
        "timeout_type": "Coach Challenge",
        "full": "2",
        "short": "0",
    }
)

# Timeout (single word in timeout_time)
playbyplay["Timeout"].append(
    {
        "description": "Magic Timeout: Regular (Reg.4 Short 0)",
        "team": "Magic",
        "timeout_type": "Regular",
        "full": "4",
        "short": "0",
    }
)

# Turnover Player (Single Name)
playbyplay["TurnoverPlayer"].append(
    {
        "description": "Harrison Double Dribble Turnover (P1.T10)",
        "player": "Harrison",
        "turnover_type": "Double Dribble",
        "personal": "1",
        "team": "10",
    }
)

# Turnover Player (Mark Morris)
playbyplay["TurnoverPlayer"].append(
    {
        "description": "Mark Morris Discontinue Dribble Turnover (P1.T11)",
        "player": "Mark Morris",
        "turnover_type": "Discontinue Dribble",
        "personal": "1",
        "team": "11",
    }
)

# Turnover Player (Hyphenated Name)
playbyplay["TurnoverPlayer"].append(
    {
        "description": "Bates-Diop 3 Second Violation Turnover (P1.T14)",
        "player": "Bates-Diop",
        "turnover_type": "3 Second Violation",
        "personal": "1",
        "team": "14",
    }
)

# Turnover Player (Apostrophe)
playbyplay["TurnoverPlayer"].append(
    {
        "description": "O'Quinn Inbound Turnover (P2.T6)",
        "player": "O'Quinn",
        "turnover_type": "Inbound",
        "personal": "2",
        "team": "6",
    }
)

# Turnover Player (First Initial dot Last Name)
playbyplay["TurnoverPlayer"].append(
    {
        "description": "S. Hill Backcourt Turnover (P1.T3)",
        "player": "S. Hill",
        "turnover_type": "Backcourt",
        "personal": "1",
        "team": "3",
    }
)

# Turnover Player (Junior)
playbyplay["TurnoverPlayer"].append(
    {
        "description": "Porter Jr. Offensive Goaltending Turnover (P1.T16)",
        "player": "Porter Jr.",
        "turnover_type": "Offensive Goaltending",
        "personal": "1",
        "team": "16",
    }
)

# Turnover Player (Senior)
playbyplay["TurnoverPlayer"].append(
    {
        "description": "Morris Sr. Lost Ball Turnover (P1.T14)",
        "player": "Morris Sr.",
        "turnover_type": "Lost Ball",
        "personal": "1",
        "team": "14",
    }
)

# Turnover Player (Second)
playbyplay["TurnoverPlayer"].append(
    {
        "description": "Payton II Lane Violation Turnover (P1.T6)",
        "player": "Payton II",
        "turnover_type": "Lane Violation",
        "personal": "1",
        "team": "6",
    }
)

# Turnover Player (Third)
playbyplay["TurnoverPlayer"].append(
    {
        "description": "Robinson III Kicked Ball Violation Turnover (P1.T2)",
        "player": "Robinson III",
        "turnover_type": "Kicked Ball Violation",
        "personal": "1",
        "team": "2",
    }
)

# Turnover Player (Fourth)
playbyplay["TurnoverPlayer"].append(
    {
        "description": "Walker IV Out of Bounds - Bad Pass Turnover Turnover (P2.T5)",
        "player": "Walker IV",
        "turnover_type": "Out of Bounds - Bad Pass Turnover",
        "personal": "2",
        "team": "5",
    }
)

# Turnover Team (greater than 10)
playbyplay["TurnoverTeam"].append(
    {
        "description": "NUGGETS Turnover: Shot Clock (T# 12)",
        "team": "NUGGETS",
        "turnover_type": "Shot Clock",
        "turnovers": "12",
    }
)

# Turnover Team (greater than 10, no space after #)
playbyplay["TurnoverTeam"].append(
    {
        "description": "PACERS Turnover: Shot Clock (T#12)",
        "team": "PACERS",
        "turnover_type": "Shot Clock",
        "turnovers": "12",
    }
)

# Turnover Team (less than 9, no space after #)
playbyplay["TurnoverTeam"].append(
    {
        "description": "HORNETS Turnover: Shot Clock (T#6)",
        "team": "HORNETS",
        "turnover_type": "Shot Clock",
        "turnovers": "6",
    }
)

# Turnover Team (less than 9)
playbyplay["TurnoverTeam"].append(
    {
        "description": "NETS Turnover: Shot Clock (T# 6)",
        "team": "NETS",
        "turnover_type": "Shot Clock",
        "turnovers": "6",
    }
)

# Turnover Team (turnover_type starts with digit)
playbyplay["TurnoverTeam"].append(
    {
        "description": "WIZARDS Turnover: 5 Second Violation (T# 12)",
        "team": "WIZARDS",
        "turnover_type": "5 Second Violation",
        "turnovers": "12",
    }
)

# Violation
playbyplay["Violation"].append(
    {
        "description": "Dieng Violation:Kicked Ball (T.Brown)",
        "player": "Dieng",
        "violation_type": "Kicked Ball",
        "referee": "T.Brown",
    }
)

# Violation (Without Referee)
playbyplay["Violation"].append(
    {
        "description": "Miles Violation:Lane",
        "player": "Miles",
        "violation_type": "Lane",
        "referee": None,
    }
)

# Violation Team (Single String Team Name)
playbyplay["ViolationTeam"].append(
    {
        "description": "LAKERS Violation: Delay of game Violation",
        "team": "LAKERS",
        "violation_type": "Delay of game",
    }
)

# Violation Team (Double String Team Name)
playbyplay["ViolationTeam"].append(
    {
        "description": "TRAIL BLAZERS Violation: Delay of game Violation",
        "team": "TRAIL BLAZERS",
        "violation_type": "Delay of game",
    }
)
