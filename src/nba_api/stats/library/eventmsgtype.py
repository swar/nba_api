from nba_api.library._enum_base import DeprecatedEnum


class EventMsgType(DeprecatedEnum):
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
    # Deprecated as of 2023.11.10
    UNKNOWN = 18, "'UNKNOWN' member is deprecated; use 'INSTANT_REPLAY' instead."
    INSTANT_REPLAY = 18
