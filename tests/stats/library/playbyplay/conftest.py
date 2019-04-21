import pytest
from collections import defaultdict
from nba_api.stats.library.eventmsgtype import EventMsgType

@pytest.fixture(scope="module")
def playbyplaydata():

    data = defaultdict(list)
       
    #Block
    data["Block"].append({"description" : "Collins BLOCK (1 BLK)", "player" : "Collins", "blocks" : "1"})

    #Ejection
    data["Ejection"].append({"description" : "Robinson Ejection:Second Technical", "player" : "Robinson", "ejection_type" : "Second Technical"})

    #Field Goal Made (With Assist)
    data["FieldGoalMade"].append({"description" : "S. Hill 24' 3PT Jump Shot (3 PTS) (Mahinmi 1 AST)", "player" : "S. Hill", "distance" : "24", "field_goal_type" : "3PT Jump Shot", "points" : "3", "player_ast" : "Mahinmi", "assists" : "1"})
    
    #Field Goal Made (Without Assist)
    data["FieldGoalMade"].append({"description" : "Aldridge 6' Turnaround Hook Shot (8 PTS)", "player" : "Aldridge", "distance" : "6", "field_goal_type" : "Turnaround Hook Shot", "points" : "8", "player_ast" : None, "assists" : None})

    #Field Goal Made (Without Distance)
    data["FieldGoalMade"].append({"description" : "Broekhoff 3PT Jump Shot (3 PTS) (Lee 2 AST)", "player" : "Broekhoff", "distance" : None, "field_goal_type" : "3PT Jump Shot", "points" : "3", "player_ast" : "Lee", "assists" : "2"})
    
    #Field Goal Missed
    data["FieldGoalMissed"].append({"description" : "MISS O'Quinn 17' Jump Shot", "player" : "O'Quinn", "distance" : "17", "field_goal_type" : "Jump Shot"})
    
    #Foul
    data["Foul"].append({"description" : "Collison P.FOUL (P1.TN) (M.Lindsay)", "player" : "Collison", "foul_type" : "P.FOUL", "personal" : "1", "team" : "N", "referee" : "M.Lindsay"})
    
    #Free Throw Made
    data["FreeThrowMade"].append({"description" : "Sumner Free Throw 2 of 2 (1 PTS)", "player" : "Sumner", "free_throw_type" : "2 of 2", "points" : "1"})
    
    #Free Throw Missed
    data["FreeThrowMissed"].append({"description" : "MISS Prince Free Throw 1 of 2", "player" : "Prince", "free_throw_type" : "1 of 2"})
    
    #Jump Ball
    data["JumpBall"].append({"description" : "Jump Ball Collins vs. O'Quinn: Tip to Leaf", "player_home" : "Collins", "player_away" : "O'Quinn", "player_tip" : "Leaf"})
    
    #Player (Single Name)
    data["Player"].append({"description" : "Millsap 25' 3PT Jump Shot (9 PTS) (Teague 1 AST)", "player" : "Millsap"})   

    #Player (Hyphenated Name)
    data["Player"].append({"description" : "Bates-Diop P.FOUL (P1.T4) (M.Boland)", "player" : "Bates-Diop"})   

    #Player (Apostrophe)
    data["Player"].append({"description" : "O'Quinn 20' Jump Shot (2 PTS) (Oladipo 1 AST)", "player" : "O'Quinn"})   

    #Player (First Initial dot Last Name)
    data["Player"].append({"description" : "S. Hill 24' 3PT Jump Shot (3 PTS) (Mahinmi 1 AST)", "player" : "S. Hill"})   

    #Player (Junior)
    data["Player"].append({"description" : "Porter Jr. 10' Driving Floating Jump Shot (2 PTS)", "player" : "Porter Jr."})   

    #Player (Second)
    data["Player"].append({"description" : "Payton II 2' Driving Reverse Layup (2 PTS) (Middleton 6 AST)", "player" : "Payton II"})   
  
    #Player (Third)
    data["Player"].append({"description" : "Robinson III Free Throw 1 of 1 (3 PTS)", "player" : "Robinson III"})   
    
    #Player (Fourth)
    data["Player"].append({"description" : "Walker IV REBOUND (Off:0 Def:1)", "player" : "Walker IV"})  
 
    #Rebound Player
    data["ReboundPlayer"].append({"description" : "Zubac REBOUND (Off:2 Def:4)", "player" : "Zubac", "offensive" : "2", "defensive" : "4"})
    
    #Rebound Team (One Word)
    data["ReboundTeam"].append({"description" : "Timberwolves Rebound", "team" : "Timberwolves"})
    
    #Rebound Team (Two Words)
    data["ReboundTeam"].append({"description" : "TRAIL BLAZERS Rebound", "team" : "TRAIL BLAZERS"})
    
    #Steal
    data["Steal"].append({"description" : "Bradley STEAL (2 STL)", "player" : "Bradley", "steals" : "2"})
    
    #Substitution
    data["Substitution"].append({"description" : "SUB: Sefolosha FOR Ingles", "player_in" : "Sefolosha", "player_out" : "Ingles"})
    
    #Timeout
    data["Timeout"].append({"description" : "TRAIL BLAZERS Timeout: Regular (Full 5 Short 0)", "team" : "TRAIL BLAZERS", "timeout_type" : "Regular", "full" : "5", "short" : "0"})
    
    #Turnover Player
    data["TurnoverPlayer"].append({"description" : "G. Harrison Double Dribble Turnover (P1.T10)", "player" : "G. Harrison", "turnover_type" : "Double Dribble", "personal" : "1", "team" : "10"})
    
    #Turnover Team
    data["TurnoverTeam"].append({"description" : "NUGGETS Turnover: Shot Clock (T#12)", "team" : "NUGGETS", "turnover_type" : "Shot Clock", "turnovers" : "12"})
    
    #Violation
    data["Visolation"].append({"description" : "Dieng Violation:Kicked Ball (T.Brown)", "player" : "Dieng", "violation_type" : "Kicked Ball", "referee" : "T.Brown"})

    return data