from datetime import datetime


class _NotRequired:
    none = ''

    default = none


class _ContextMeasure:
    pts = 'PTS'
    fgm = 'FGM'
    fga = 'FGA'
    fg_pct = 'FG_PCT'
    fg3m = 'FG3M'
    fg3a = 'FG3A'
    fg3_pct = 'FG3_PCT'
    pts_fb = 'PTS_FB'
    pts_off_tov = 'PTS_OFF_TOV'
    pts_2nd_chance = 'PTS_2ND_CHANCE'

    default = pts


class _No:
    no = 'N'

    default = no


class _YesNo(_No):
    yes = 'Y'


class AheadBehind:
    ahead_or_behind = 'Ahead or Behind'
    behind_or_tied = 'Behind or Tied'
    ahead_or_tied = 'Ahead or Tied'

    default = ahead_or_behind


class AheadBehindNullable(_NotRequired, AheadBehind):
    pass


class ClutchTime:
    last_5_minutes = 'Last 5 Minutes'
    last_4_minutes = 'Last 4 Minutes'
    last_3_minutes = 'Last 3 Minutes'
    last_2_minutes = 'Last 2 Minutes'
    last_1_minute = 'Last 1 Minute'
    last_30_seconds = 'Last 30 Seconds'
    last_10_seconds = 'Last 10 Seconds'

    default = last_5_minutes


class ClutchTimeNullable(_NotRequired, ClutchTime):
    pass


class Conference:
    east = 'East'
    west = 'West'
    none = ''

    default = none


class ConferenceNullable(_NotRequired, Conference):
    pass


class ContextMeasureSimple(_ContextMeasure):
    pf = 'PF'
    efg_pct = 'EFG_PCT'
    ts_pct = 'TS_PCT'


class ContextMeasureSimpleNullable(_NotRequired, ContextMeasureSimple):
    pass


class ContextMeasureDetailed(_ContextMeasure):
    ftm = 'FTM'
    fta = 'FTA'
    oreb = 'OREB'
    dreb = 'DREB'
    ast = 'AST'
    fgm_ast = 'FGM_AST'
    fg3_ast = 'FG3_AST'
    stl = 'STL'
    blk = 'BLK'
    blka = 'BLKA'
    tov = 'TOV'
    poss_end_ft = 'POSS_END_FT'
    pts_paint = 'PTS_PAINT'
    reb = 'REB'
    tm_fgm = 'TM_FGM'
    tm_fga = 'TM_FGA'
    tm_fg3m = 'TM_FG3M'
    tm_fg3a = 'TM_FG3A'
    tm_ftm = 'TM_FTM'
    tm_fta = 'TM_FTA'
    tm_oreb = 'TM_OREB'
    tm_dreb = 'TM_DREB'
    tm_reb = 'TM_REB'
    tm_team_reb = 'TM_TEAM_REB'
    tm_ast = 'TM_AST'
    tm_stl = 'TM_STL'
    tm_blk = 'TM_BLK'
    tm_blka = 'TM_BLKA'
    tm_tov = 'TM_TOV'
    tm_team_tov = 'TM_TEAM_TOV'
    tm_pf = 'TM_PF'
    tm_pfd = 'TM_PFD'
    tm_pts = 'TM_PTS'
    tm_pts_paint = 'TM_PTS_PAINT'
    tm_pts_fb = 'TM_PTS_FB'
    tm_pts_off_tov = 'TM_PTS_OFF_TOV'
    tm_pts_2nd_chance = 'TM_PTS_2ND_CHANCE'
    tm_fgm_ast = 'TM_FGM_AST'
    tm_fg3_ast = 'TM_FG3_AST'
    tm_poss_end_ft = 'TM_POSS_END_FT'
    opp_ftm = 'OPP_FTM'
    opp_fta = 'OPP_FTA'
    opp_oreb = 'OPP_OREB'
    opp_dreb = 'OPP_DREB'
    opp_reb = 'OPP_REB'
    opp_team_reb = 'OPP_TEAM_REB'
    opp_ast = 'OPP_AST'
    opp_stl = 'OPP_STL'
    opp_blk = 'OPP_BLK'
    opp_blka = 'OPP_BLKA'
    opp_tov = 'OPP_TOV'
    opp_team_tov = 'OPP_TEAM_TOV'
    opp_pf = 'OPP_PF'
    opp_pfd = 'OPP_PFD'
    opp_pts = 'OPP_PTS'
    opp_pts_paint = 'OPP_PTS_PAINT'
    opp_pts_fb = 'OPP_PTS_FB'
    opp_pts_off_tov = 'OPP_PTS_OFF_TOV'
    opp_pts_2nd_chance = 'OPP_PTS_2ND_CHANCE'
    opp_fgm_ast = 'OPP_FGM_AST'
    opp_fg3_ast = 'OPP_FG3_AST'
    opp_poss_end_ft = 'OPP_POSS_END_FT'


class DayOffset:
    def days(self, i):
        return str(int(i))

    default = '0'


class DefenseCategory:
    overall = 'Overall'
    threes = '3 Pointers'
    twos = '2 Pointers'
    less_than_6ft = 'Less Than 6Ft'
    less_than_10ft = 'Less Than 10Ft'
    greater_than_15ft = 'Greater Than 15Ft'

    default = overall


class DefenseCategoryNullable(_NotRequired, DefenseCategory):
    pass


class Direction:
    asc = 'ASC'
    desc = 'DESC'

    default = asc


class DistanceRange:
    range_5ft = '5ft Range'
    range_8ft = '8ft Range'
    by_zone = 'By Zone'

    default = by_zone


class DivisionSimple:
    atlantic = 'Atlantic'
    central = 'Central'
    northwest = 'Northwest'
    pacific = 'Pacific'
    southeast = 'Southeast'
    southwest = 'Southwest'

    default = atlantic


class DivisionSimpleNullable(_NotRequired, DivisionSimple):
    pass


class Division:
    east = 'East'
    west = 'West'

    default = east


class DivisionNullable(_NotRequired, Division):
    pass


class EndRange:
    default = '0'


class EndRangeNullable(_NotRequired, EndRange):
    pass


class GameDate:
    def get_date_format(self, datetime):
        return str(datetime.date())

    def get_date(self, year, month, day):
        return str(datetime(year=year, month=month, day=day).date())

    default = str(datetime.now().date())


class GameScopeSimple:
    last_10 = 'Last 10'
    yesterday = 'Yesterday'

    default = last_10


class GameScopeSimpleNullable(_NotRequired, GameScopeSimple):
    pass


class GameScopeDetailed(GameScopeSimple):
    season = 'Season'
    finals = 'Finals'

    default = season


class GameSegment:
    first_half = 'First Half'
    overtime = 'Overtime'
    second_half = 'Second Half'

    default = first_half


class GameSegmentNullable(_NotRequired, GameSegment):
    pass


class GroupQuantity:
    def players(self, i):
        return str(int(i))

    default = '5'


class LastNGames:
    def games(self, i):
        return str(int(i))

    default = '0'


class LastNGamesNullable(_NotRequired, LastNGames):
    pass


class LeagueID:
    nba = '00'
    aba = '01'
    wnba = '10'
    g_league = '20'

    default = nba


class LeagueIDNullable(_NotRequired, LeagueID):
    pass


class Location:
    home = 'Home'
    road = 'Road'

    default = home


class LocationNullable(_NotRequired, Location):
    pass


class MeasureTypeBase:
    base = 'Base'

    default = base


class MeasureTypeSimple(MeasureTypeBase):
    opponent = 'Opponent'


class MeasureTypePlayerGameLogs(MeasureTypeBase):
    advanced = 'Advanced'
    misc = 'Misc'
    scoring = 'Scoring'
    usage = 'Usage'


class MeasureTypeDetailed(MeasureTypeSimple, MeasureTypePlayerGameLogs):
    four_factors = 'Four Factors'


class MeasureTypeDetailedDefense(MeasureTypeDetailed):
    defense = 'Defense'


class Month:
    def month(self, i):
        return str(int(i))

    default = '0'


class MonthNullable(_NotRequired, Month):
    pass


class NumberOfGames:
    def games(self, i):
        return str(int(i))

    default = '2147483647'


class Outcome:
    win = 'W'
    loss = 'L'

    default = win


class OutcomeNullable(_NotRequired, Outcome):
    pass


class PaceAdjust(_YesNo):
    pass


class PaceAdjustNo(_No):
    pass


class PlusMinus(_YesNo):
    pass


class PlusMinusNo(_No):
    pass


class Period:
    all = '0'

    first = '1'
    second = '2'
    third = '3'
    fourth = '4'

    def quarter(self, i):
        return str(int(i))

    def overtime(self, i):
        return str(4 + int(i))

    default = all


class PeriodNullable(_NotRequired, Period):
    pass


class StartPeriod(Period):
    pass


class StartPeriodNullable(_NotRequired, StartPeriod):
    pass


class EndPeriod(Period):
    pass


class EndPeriodNullable(_NotRequired, EndPeriod):
    pass


class PerModeSimple:
    totals = 'Totals'
    per_game = 'PerGame'

    default = totals


class PerModeSimpleNullable(_NotRequired, PerModeSimple):
    pass


class PerMode36(PerModeSimple):
    per_36 = 'Per36'


class PerMode48(PerModeSimple):
    per_48 = 'Per48'


class PerModeDetailed(PerMode36, PerMode48):
    minutes_per = 'MinutesPer'
    per_40 = 'Per40'
    per_minute = 'PerMinute'
    per_possession = 'PerPossession'
    per_play = 'PerPlay'
    per_100_possessions = 'Per100Possessions'
    per_100_plays = 'Per100Plays'


class PlayerExperience:
    rookie = 'Rookie'
    sophomore = 'Sophomore'
    veteran = 'Veteran'

    default = rookie


class PlayerExperienceNullable(_NotRequired, PlayerExperience):
    pass


class PlayerOrTeam:
    player = 'Player'
    team = 'Team'

    default = team


class PlayerOrTeamAbbreviation:
    player = 'P'
    team = 'T'

    default = team


class PlayerPosition:
    forward = 'Forward'
    center = 'Center'
    guard = 'Guard'

    default = forward


class PlayerPositionNullable(_NotRequired, PlayerPosition):
    pass


class PositionNullable(_NotRequired, PlayerPosition):
    pass


class PlayerPositionAbbreviation:
    forward = 'F'
    center = 'C'
    guard = 'G'
    center_forward = 'C-F'
    forward_center = 'F-C'
    forward_guard = 'F-G'
    guard_forward = 'G-F'

    default = forward


class PlayerPositionAbbreviationNullable(_NotRequired, PlayerPositionAbbreviation):
    pass


class PlayerScope:
    all_players = 'All Players'
    rookies = 'Rookies'

    default = all_players


class TodaysPlayers(_YesNo):
    pass


class ActivePlayers(_YesNo):
    pass


class PlayType:
    transition = 'Transition'
    isolation = 'Isolation'
    pr_ball_handler = 'PRBallHandler'
    pr_roll_man = 'PRRollman'
    post_up = 'Postup'
    spot_up = 'Spotup'
    handoff = 'Handoff'
    cut = 'Cut'
    off_screen = 'OffScreen'
    putbacks = 'OffRebound'
    misc = 'Misc'

    default = transition


class PlayTypeNullable(_NotRequired, PlayType):
    pass


class PointDiff:
    def points(self, i):
        return str(int(i))

    default = '5'


class PointDiffNullable(_NotRequired, PointDiff):
    pass


class PtMeasureType:
    speed_distance = 'SpeedDistance'
    rebounding = 'Rebounding'
    possessions = 'Possessions'
    catch_shoot = 'CatchShoot'
    pull_up_shot = 'PullUpShot'
    defense = 'Defense'
    drives = 'Drives'
    passing = 'Passing'
    elbowTouch = 'ElbowTouch'
    postTouch = 'PostTouch'
    paintTouch = 'PaintTouch'
    efficiency = 'Efficiency'

    default = speed_distance


class RangeType:
    default = '0'


class RangeTypeNullable(_NotRequired, RangeType):
    pass


class Rank(_YesNo):
    pass


class RankNo(_No):
    pass


class RunType:
    default = 'each second'


class StartRange:
    default = '0'


class StartRangeNullable(_NotRequired, StartRange):
    pass


class Scope:
    rs = 'RS'
    s = 'S'
    rookies = 'Rookies'

    default = s


class SeasonYear:
    current_datetime = datetime.now()
    current_season_year = current_datetime.year
    if current_datetime.month <= 9:
        current_season_year -= 1

    default = current_season_year


class SeasonYearNullable(_NotRequired, SeasonYear):
    pass


class Season(SeasonYear):
    current_season_year = SeasonYear.current_season_year
    current_season = '{}-{}'.format(current_season_year, str(current_season_year + 1)[2:])

    default = current_season


class SeasonNullable(_NotRequired, Season):
    pass


class SeasonAll(Season):
    all = 'ALL'


class SeasonAllNullable(_NotRequired, SeasonAll):
    pass


class SeasonAll_Time(Season):
    all_time = 'All Time'


class SeasonAllTime(Season):
    alltime = 'ALLTIME'


class SeasonID(SeasonYear):
    def get_season_id(self, season_year):
        return "2{}".format(season_year)

    current_season_year = SeasonYear.current_season_year
    current_season_year = "2{}".format(current_season_year)

    default = current_season_year


class SeasonType:
    regular = 'Regular Season'
    preseason = 'Pre Season'

    default = regular


class SeasonTypePlayoffs(SeasonType):
    playoffs = 'Playoffs'


class SeasonTypeNullable(_NotRequired, SeasonTypePlayoffs):
    pass


class SeasonTypeAllStar(SeasonTypePlayoffs):
    all_star = 'All Star'


class SeasonTypeAllStarNullable(_NotRequired, SeasonTypePlayoffs):
    pass


class SeasonSegment:
    post_all_star = 'Post All-Star'
    pre_all_star = 'Pre All-Star'

    default = post_all_star


class SeasonSegmentNullable(_NotRequired, SeasonSegment):
    pass


class ShotClockRange:
    def calculate_range(self, i):
        i = float(i)
        if i > 24 or i <= 0:
            return ''
        elif 22 < i <= 24:
            return '24-22'
        elif 18 < i <= 22:
            return '22-18 Very Early'
        elif 15 < i <= 18:
            return '18-15 Early'
        elif 7 < i <= 15:
            return '15-7 Average'
        elif 4 < i <= 7:
            return '7-4 Late'
        elif 0 < i <= 4:
            return '4-0 Very Late'

    range_22_24 = '24-22'
    range_18_22 = '22-18 Very Early'
    range_15_18 = '18-15 Early'
    range_7_15 = '15-7 Average'
    range_4_7 = '7-4 Late'
    range_0_4 = '4-0 Very Late'
    shot_clock_off = 'ShotClock Off'

    default = shot_clock_off


class ShotClockRangeNullable(_NotRequired, ShotClockRange):
    pass


class Sorter:
    fgm = 'FGM'
    fga = 'FGA'
    fg_pct = 'FG_PCT'
    fg3m = 'FG3M'
    fg3a = 'FG3A'
    fg3_pct = 'FG3_PCT'
    ftm = 'FTM'
    fta = 'FTA'
    ft_pct = 'FT_PCT'
    oreb = 'OREB'
    dreb = 'DREB'
    ast = 'AST'
    stl = 'STL'
    blk = 'BLK'
    tov = 'TOV'
    reb = 'REB'
    pts = 'PTS'
    date = 'DATE'

    default = date


class StarterBench:
    starters = 'Starters'
    bench = 'Bench'

    default = starters


class StarterBenchNullable(_NotRequired, StarterBench):
    pass


class Stat:
    points = 'PTS'
    rebounds = 'REB'
    assists = 'AST'
    field_goal_percent = 'FG_PCT'
    free_throw_percent = 'FT_PCT'
    threes_percent = 'FG3_PCT'
    steals = 'STL'
    blocks = 'BLK'

    default = points


class StatCategory:
    points = 'Points'
    rebounds = 'Rebounds'
    assists = 'Assists'
    defense = 'Defense'
    clutch = 'Clutch'
    playmaking = 'Playmaking'
    efficiency = 'Efficiency'
    fast_break = 'Fast Break'
    scoring_breakdown = 'Scoring Breakdown'

    default = points


class StatCategoryAbbreviation:
    pts = 'PTS'
    fgm = 'FGM'
    fga = 'FGA'
    fg_pct = 'FG_PCT'
    fg3m = 'FG3M'
    fg3a = 'FG3A'
    fg3_pct = 'FG3_PCT'
    ftm = 'FTM'
    fta = 'FTA'
    oreb = 'OREB'
    dreb = 'DREB'
    ast = 'AST'
    stl = 'STL'
    blk = 'BLK'
    tov = 'TOV'
    reb = 'REB'

    default = pts


class StatType:
    traditional = 'Traditional'
    advanced = 'Advanced'
    tracking = 'Tracking'

    default = traditional


class TypeGrouping:
    offensive = 'offensive'
    defensive = 'defensive'

    default = offensive


class TypeGroupingNullable(_NotRequired, TypeGrouping):
    pass
