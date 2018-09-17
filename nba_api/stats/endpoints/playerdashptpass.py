from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LastNGames, LeagueID, Month, PerModeSimple, Season, SeasonTypeAllStar, LocationNullable, OutcomeNullable, SeasonSegmentNullable, ConferenceNullable, DivisionNullable


class PlayerDashPtPass(Endpoint):
    endpoint = 'playerdashptpass'
    expected_data = {'PassesMade': ['PLAYER_ID', 'PLAYER_NAME_LAST_FIRST', 'TEAM_NAME', 'TEAM_ID', 'TEAM_ABBREVIATION', 'PASS_TYPE', 'G', 'PASS_TO', 'PASS_TEAMMATE_PLAYER_ID', 'FREQUENCY', 'PASS', 'AST', 'FGM', 'FGA', 'FG_PCT', 'FG2M', 'FG2A', 'FG2_PCT', 'FG3M', 'FG3A', 'FG3_PCT'], 'PassesReceived': ['PLAYER_ID', 'PLAYER_NAME_LAST_FIRST', 'TEAM_NAME', 'TEAM_ID', 'TEAM_ABBREVIATION', 'PASS_TYPE', 'G', 'PASS_FROM', 'PASS_TEAMMATE_PLAYER_ID', 'FREQUENCY', 'PASS', 'AST', 'FGM', 'FGA', 'FG_PCT', 'FG2M', 'FG2A', 'FG2_PCT', 'FG3M', 'FG3A', 'FG3_PCT']}

    def __init__(self,
                 team_id,
                 player_id,
                 last_n_games=LastNGames.default,
                 league_id=LeagueID.default,
                 month=Month.default,
                 opponent_team_id=0,
                 per_mode_simple=PerModeSimple.default,
                 season=Season.default,
                 season_type_all_star=SeasonTypeAllStar.default,
                 date_from_nullable='',
                 date_to_nullable='',
                 location_nullable=LocationNullable.default,
                 outcome_nullable=OutcomeNullable.default,
                 season_segment_nullable=SeasonSegmentNullable.default,
                 vs_conference_nullable=ConferenceNullable.default,
                 vs_division_nullable=DivisionNullable.default):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters={
                'TeamID': team_id,
                'PlayerID': player_id,
                'LastNGames': last_n_games,
                'LeagueID': league_id,
                'Month': month,
                'OpponentTeamID': opponent_team_id,
                'PerMode': per_mode_simple,
                'Season': season,
                'SeasonType': season_type_all_star,
                'DateFrom': date_from_nullable,
                'DateTo': date_to_nullable,
                'Location': location_nullable,
                'Outcome': outcome_nullable,
                'SeasonSegment': season_segment_nullable,
                'VsConference': vs_conference_nullable,
                'VsDivision': vs_division_nullable
            },
        )
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [Endpoint.DataSet(data=data_set) for data_set_name, data_set in data_sets.items()]
        self.passes_made = Endpoint.DataSet(data=data_sets['PassesMade'])
        self.passes_received = Endpoint.DataSet(data=data_sets['PassesReceived'])
