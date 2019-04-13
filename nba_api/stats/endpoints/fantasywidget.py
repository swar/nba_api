from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import ActivePlayers, LastNGames, LeagueID, Season, SeasonTypeAllStar, TodaysPlayers, LocationNullable, MonthNullable, PositionNullable, SeasonSegmentNullable, ConferenceNullable, DivisionNullable


class FantasyWidget(Endpoint):
    endpoint = 'fantasywidget'
    expected_data = {'FantasyWidgetResult': ['PLAYER_ID', 'PLAYER_NAME', 'PLAYER_POSITION', 'TEAM_ID', 'TEAM_ABBREVIATION', 'GP', 'MIN', 'FAN_DUEL_PTS', 'NBA_FANTASY_PTS', 'PTS', 'REB', 'AST', 'BLK', 'STL', 'TOV', 'FG3M', 'FGA', 'FG_PCT', 'FTA', 'FT_PCT']}

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(self,
                 active_players=ActivePlayers.default,
                 last_n_games=LastNGames.default,
                 league_id=LeagueID.default,
                 season=Season.default,
                 season_type_all_star=SeasonTypeAllStar.default,
                 todays_opponent=0,
                 todays_players=TodaysPlayers.default,
                 date_from_nullable='',
                 date_to_nullable='',
                 location_nullable=LocationNullable.default,
                 month_nullable=MonthNullable.default,
                 opponent_team_id_nullable='',
                 po_round_nullable='',
                 player_id_nullable='',
                 position_nullable=PositionNullable.default,
                 season_segment_nullable=SeasonSegmentNullable.default,
                 team_id_nullable='',
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
                'ActivePlayers': active_players,
                'LastNGames': last_n_games,
                'LeagueID': league_id,
                'Season': season,
                'SeasonType': season_type_all_star,
                'TodaysOpponent': todays_opponent,
                'TodaysPlayers': todays_players,
                'DateFrom': date_from_nullable,
                'DateTo': date_to_nullable,
                'Location': location_nullable,
                'Month': month_nullable,
                'OpponentTeamID': opponent_team_id_nullable,
                'PORound': po_round_nullable,
                'PlayerID': player_id_nullable,
                'Position': position_nullable,
                'SeasonSegment': season_segment_nullable,
                'TeamID': team_id_nullable,
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
        self.fantasy_widget_result = Endpoint.DataSet(data=data_sets['FantasyWidgetResult'])
