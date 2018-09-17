from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import Direction, LeagueID, PlayerOrTeamAbbreviation, SeasonAllTime, SeasonTypeAllStar, Sorter


class LeagueGameLog(Endpoint):
    endpoint = 'leaguegamelog'
    expected_data = {'LeagueGameLog': ['SEASON_ID', 'TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'GAME_ID', 'GAME_DATE', 'MATCHUP', 'WL', 'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'PLUS_MINUS', 'VIDEO_AVAILABLE']}

    def __init__(self,
                 counter=0,
                 direction=Direction.default,
                 league_id=LeagueID.default,
                 player_or_team_abbreviation=PlayerOrTeamAbbreviation.default,
                 season_all_time=SeasonAllTime.default,
                 season_type_all_star=SeasonTypeAllStar.default,
                 sorter=Sorter.default,
                 date_from_nullable='',
                 date_to_nullable=''):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={
                'Counter': counter,
                'Direction': direction,
                'LeagueID': league_id,
                'PlayerOrTeam': player_or_team_abbreviation,
                'Season': season_all_time,
                'SeasonType': season_type_all_star,
                'Sorter': sorter,
                'DateFrom': date_from_nullable,
                'DateTo': date_to_nullable
            },
        )
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.league_game_log = Endpoint.DataSet(data=data_sets['LeagueGameLog'])
