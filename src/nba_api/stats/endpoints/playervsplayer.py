from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LastNGames, MeasureTypeDetailedDefense, Month, PaceAdjust, PerModeDetailed, Period, PlusMinus, Rank, Season, SeasonType, GameSegmentNullable, LeagueIDNullable, LocationNullable, OutcomeNullable, SeasonSegmentNullable, ConferenceNullable, DivisionNullable


class PlayerVsPlayer(Endpoint):
    endpoint = 'playervsplayer'
    expected_data = {'OnOffCourt': ['GROUP_SET', 'PLAYER_ID', 'PLAYER_NAME', 'VS_PLAYER_ID', 'VS_PLAYER_NAME', 'COURT_STATUS', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'NBA_FANTASY_PTS', 'CFID', 'CFPARAMS'], 'Overall': ['GROUP_SET', 'GROUP_VALUE', 'PLAYER_ID', 'PLAYER_NAME', 'GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', 'PTS', 'PLUS_MINUS', 'NBA_FANTASY_PTS', 'CFID', 'CFPARAMS'], 'PlayerInfo': ['PERSON_ID', 'FIRST_NAME', 'LAST_NAME', 'DISPLAY_FIRST_LAST', 'DISPLAY_LAST_COMMA_FIRST', 'DISPLAY_FI_LAST', 'BIRTHDATE', 'SCHOOL', 'COUNTRY', 'LAST_AFFILIATION'], 'ShotAreaOffCourt': ['GROUP_SET', 'PLAYER_ID', 'PLAYER_NAME', 'VS_PLAYER_ID', 'VS_PLAYER_NAME', 'COURT_STATUS', 'GROUP_VALUE', 'FGM', 'FGA', 'FG_PCT', 'CFID', 'CFPARAMS'], 'ShotAreaOnCourt': ['GROUP_SET', 'PLAYER_ID', 'PLAYER_NAME', 'VS_PLAYER_ID', 'VS_PLAYER_NAME', 'COURT_STATUS', 'GROUP_VALUE', 'FGM', 'FGA', 'FG_PCT', 'CFID', 'CFPARAMS'], 'ShotAreaOverall': ['GROUP_SET', 'GROUP_VALUE', 'PLAYER_ID', 'PLAYER_NAME', 'FGM', 'FGA', 'FG_PCT', 'CFID', 'CFPARAMS'], 'ShotDistanceOffCourt': ['GROUP_SET', 'PLAYER_ID', 'PLAYER_NAME', 'VS_PLAYER_ID', 'VS_PLAYER_NAME', 'COURT_STATUS', 'GROUP_VALUE', 'FGM', 'FGA', 'FG_PCT', 'CFID', 'CFPARAMS'], 'ShotDistanceOnCourt': ['GROUP_SET', 'PLAYER_ID', 'PLAYER_NAME', 'VS_PLAYER_ID', 'VS_PLAYER_NAME', 'COURT_STATUS', 'GROUP_VALUE', 'FGM', 'FGA', 'FG_PCT', 'CFID', 'CFPARAMS'], 'ShotDistanceOverall': ['GROUP_SET', 'GROUP_VALUE', 'PLAYER_ID', 'PLAYER_NAME', 'FGM', 'FGA', 'FG_PCT', 'CFID', 'CFPARAMS'], 'VsPlayerInfo': ['PERSON_ID', 'FIRST_NAME', 'LAST_NAME', 'DISPLAY_FIRST_LAST', 'DISPLAY_LAST_COMMA_FIRST', 'DISPLAY_FI_LAST', 'BIRTHDATE', 'SCHOOL', 'COUNTRY', 'LAST_AFFILIATION']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 vs_player_id,
                 player_id,
                 last_n_games=LastNGames.default,
                 measure_type_detailed_defense=MeasureTypeDetailedDefense.default,
                 month=Month.default,
                 opponent_team_id=0,
                 pace_adjust=PaceAdjust.default,
                 per_mode_detailed=PerModeDetailed.default,
                 period=Period.default,
                 plus_minus=PlusMinus.default,
                 rank=Rank.default,
                 season=Season.default,
                 season_type_playoffs=SeasonType.default,
                 date_from_nullable='',
                 date_to_nullable='',
                 game_segment_nullable=GameSegmentNullable.default,
                 league_id_nullable=LeagueIDNullable.default,
                 location_nullable=LocationNullable.default,
                 outcome_nullable=OutcomeNullable.default,
                 season_segment_nullable=SeasonSegmentNullable.default,
                 vs_conference_nullable=ConferenceNullable.default,
                 vs_division_nullable=DivisionNullable.default,
                 proxy=None,
                 headers=None,
                 timeout=30,
                 get_request=True):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
                'VsPlayerID': vs_player_id,
                'PlayerID': player_id,
                'LastNGames': last_n_games,
                'MeasureType': measure_type_detailed_defense,
                'Month': month,
                'OpponentTeamID': opponent_team_id,
                'PaceAdjust': pace_adjust,
                'PerMode': per_mode_detailed,
                'Period': period,
                'PlusMinus': plus_minus,
                'Rank': rank,
                'Season': season,
                'SeasonType': season_type_playoffs,
                'DateFrom': date_from_nullable,
                'DateTo': date_to_nullable,
                'GameSegment': game_segment_nullable,
                'LeagueID': league_id_nullable,
                'Location': location_nullable,
                'Outcome': outcome_nullable,
                'SeasonSegment': season_segment_nullable,
                'VsConference': vs_conference_nullable,
                'VsDivision': vs_division_nullable
        }
        if get_request:
            self.get_request()
    
    def get_request(self):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters=self.parameters,
            proxy=self.proxy,
            headers=self.headers,
            timeout=self.timeout,
        )
        self.load_response()
        
    def load_response(self):
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.on_off_court = Endpoint.DataSet(data=data_sets['OnOffCourt'])
        self.overall = Endpoint.DataSet(data=data_sets['Overall'])
        self.player_info = Endpoint.DataSet(data=data_sets['PlayerInfo'])
        self.shot_area_off_court = Endpoint.DataSet(data=data_sets['ShotAreaOffCourt'])
        self.shot_area_on_court = Endpoint.DataSet(data=data_sets['ShotAreaOnCourt'])
        self.shot_area_overall = Endpoint.DataSet(data=data_sets['ShotAreaOverall'])
        self.shot_distance_off_court = Endpoint.DataSet(data=data_sets['ShotDistanceOffCourt'])
        self.shot_distance_on_court = Endpoint.DataSet(data=data_sets['ShotDistanceOnCourt'])
        self.shot_distance_overall = Endpoint.DataSet(data=data_sets['ShotDistanceOverall'])
        self.vs_player_info = Endpoint.DataSet(data=data_sets['VsPlayerInfo'])
