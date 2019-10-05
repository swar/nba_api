import pytest
from collections import defaultdict
from nba_api.stats.library.eventmsgtype import EventMsgType

playbyplay = defaultdict(list)

#Block
playbyplay["Block"].append({"description" : "Collins BLOCK (1 BLK)", "player" : "Collins", "blocks" : "1"})

#Ejection
playbyplay["Ejection"].append({"description" : "Robinson Ejection:Second Technical", "player" : "Robinson", "ejection_type" : "Second Technical"})

#Field Goal Made (With Assist)
playbyplay["FieldGoalMade"].append({"description" : "S. Hill 24' 3PT Jump Shot (3 PTS) (Mahinmi 1 AST)", "player" : "S. Hill", "distance" : "24", "field_goal_type" : "3PT Jump Shot", "points" : "3", "player_ast" : "Mahinmi", "assists" : "1"})

#Field Goal Made (Without Assist)
playbyplay["FieldGoalMade"].append({"description" : "Aldridge 6' Turnaround Hook Shot (8 PTS)", "player" : "Aldridge", "distance" : "6", "field_goal_type" : "Turnaround Hook Shot", "points" : "8", "player_ast" : None, "assists" : None})

#Field Goal Made (Without Distance & With Double Space)
playbyplay["FieldGoalMade"].append({"description" : "Broekhoff  3PT Jump Shot (3 PTS) (Lee 2 AST)", "player" : "Broekhoff", "distance" : None, "field_goal_type" : "3PT Jump Shot", "points" : "3", "player_ast" : "Lee", "assists" : "2"})

#Field Goal Missed
playbyplay["FieldGoalMissed"].append({"description" : "MISS O'Quinn 17' Jump Shot", "player" : "O'Quinn", "distance" : "17", "field_goal_type" : "Jump Shot"})

#Field Goal Missed (Without Disstance & With Double Space)
playbyplay["FieldGoalMissed"].append({"description" : "MISS O'Quinn  3PT Jump Shot", "player" : "O'Quinn", "distance" : None, "field_goal_type" : "3PT Jump Shot"})

#Foul Player
playbyplay["FoulPlayer"].append({"description" : "Collison P.FOUL (P1.TN) (M.Lindsay)", "player" : "Collison", "foul_type" : "P.FOUL", "personal" : "1", "team" : "N", "referee" : "M.Lindsay"})

#Foul Team
playbyplay["FoulTeam"].append({"description" : "BUCKS T.Foul (Def. 3 Sec Lopez ) (M.Callahan)", "team" : "BUCKS", "foul_type" : "Def. 3 Sec", "player" : "Lopez", "referee" : "M.Callahan"})

#Free Throw Made
playbyplay["FreeThrowMade"].append({"description" : "Sumner Free Throw 2 of 2 (1 PTS)", "player" : "Sumner", "free_throw_type" : "2 of 2", "points" : "1"})

#Free Throw Made (Clear Path 1 of 2)
playbyplay["FreeThrowMade"].append({"description" : "Powell Free Throw Clear Path 1 of 2 (18 PTS)", "player" : "Powell", "free_throw_type" : "Clear Path 1 of 2", "points" : "18"})

#Free Throw Missed
playbyplay["FreeThrowMissed"].append({"description" : "MISS Prince Free Throw 1 of 2", "player" : "Prince", "free_throw_type" : "1 of 2"})

#Jump Ball
playbyplay["JumpBall"].append({"description" : "Jump Ball Collins vs. O'Quinn: Tip to Leaf", "player_home" : "Collins", "player_away" : "O'Quinn", "player_tip" : "Leaf"})

#Jump Ball (Without player_tip)
playbyplay["JumpBall"].append({"description" : "Jump Ball Green vs. McKinnie: Tip to", "player_home" : "Green", "player_away" : "McKinnie", "player_tip" : None})  

#Rebound Player
playbyplay["ReboundPlayer"].append({"description" : "Zubac REBOUND (Off:2 Def:4)", "player" : "Zubac", "offensive" : "2", "defensive" : "4"})

#Rebound Team (One Word)
playbyplay["ReboundTeam"].append({"description" : "Timberwolves Rebound", "team" : "Timberwolves"})

#Rebound Team (Two Words)
playbyplay["ReboundTeam"].append({"description" : "TRAIL BLAZERS Rebound", "team" : "TRAIL BLAZERS"})

#Steal
playbyplay["Steal"].append({"description" : "Bradley STEAL (2 STL)", "player" : "Bradley", "steals" : "2"})

#Substitution
playbyplay["Substitution"].append({"description" : "SUB: Sefolosha FOR Ingles", "player_in" : "Sefolosha", "player_out" : "Ingles"})

#Timeout
playbyplay["Timeout"].append({"description" : "TRAIL BLAZERS Timeout: Regular (Full 5 Short 0)", "team" : "TRAIL BLAZERS", "timeout_type" : "Regular", "full" : "5", "short" : "0"})

#Timeout
playbyplay["Timeout"].append({"description" : "Magic Timeout: Regular (Reg.4 Short 0)", "team" : "Magic", "timeout_type" : "Regular", "full" : "4", "short" : "0"})

#Turnover Player
playbyplay["TurnoverPlayer"].append({"description" : "G. Harrison Double Dribble Turnover (P1.T10)", "player" : "G. Harrison", "turnover_type" : "Double Dribble", "personal" : "1", "team" : "10"})

#Turnover Team (less than 10)
playbyplay["TurnoverTeam"].append({"description" : "NUGGETS Turnover: Shot Clock (T#12)", "team" : "NUGGETS", "turnover_type" : "Shot Clock", "turnovers" : "12"})

#Turnover Team (greater than 9)
playbyplay["TurnoverTeam"].append({"description" : "NETS Turnover: Shot Clock (T#6)", "team" : "NETS", "turnover_type" : "Shot Clock", "turnovers" : "6"})

#Turnover Team (turnover_type starts with digit)
playbyplay["TurnoverTeam"].append({"description" : "WIZARDS Turnover: 5 Second Violation (T#12)", "team" : "WIZARDS", "turnover_type" : "5 Second Violation", "turnovers" : "12"})

#Violation
playbyplay["Violation"].append({"description" : "Dieng Violation:Kicked Ball (T.Brown)", "player" : "Dieng", "violation_type" : "Kicked Ball", "referee" : "T.Brown"})

