from enum import Enum

class EventMsgType(Enum):
    FIELD_GOAL_MADE = 1
    FIELD_GOAL_MISSED = 2
    FREE_THROW = 3
    REBOUND = 4
    TURNOVER = 5
    FOUL = 6
    VIOLATION = 7
    SUBSTITUTION = 8
    TIMEOUT = 9
    JUMP_BALL = 10
    EJECTION = 11
    PERIOD_BEGIN = 12
    PERIOD_END = 13
    UNKNOWN = 18


# period : start
# jumpball : recovered
# 3pt : Jump Shot
# 2pt : Hook
# rebound : defensive
# turnover : bad pass
# steal : None
# 2pt : Jump Shot
# 2pt : Layup
# rebound : offensive
# timeout : full
# substitution : out
# substitution : in
# turnover : out-of-bounds
# foul : personal
# freethrow : 1 of 1
# 2pt : DUNK
# freethrow : 1 of 2
# freethrow : 2 of 2
# block : None
# stoppage : out-of-bounds
# foul : offensive
# turnover : offensive foul
# stoppage : blood rule
# stoppage : equipment issue
# freethrow : 1 of 3
# freethrow : 2 of 3
# freethrow : 3 of 3
# period : end
# turnover : lost ball
# violation : kicked ball
# turnover : discontinued dribble
# turnover : traveling
# foul : technical
# instantreplay : request
# game : end