from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import (
    Season,
    LeagueID,
    PlayerPositionAbbreviationNullable,
    ActiveNullable,
    AllStarNullable,
    HistoricalNullable,
)


class PlayerIndex(Endpoint):
    endpoint = "playerindex"
    expected_data = {
        "PlayerIndex": [
            "PERSON_ID",
            "PLAYER_LAST_NAME",
            "PLAYER_FIRST_NAME",
            "PLAYER_SLUG",
            "TEAM_ID",
            "TEAM_SLUG",
            "IS_DEFUNCT",
            "TEAM_CITY",
            "TEAM_NAME",
            "TEAM_ABBREVIATION",
            "JERSEY_NUMBER",
            "POSITION",
            "HEIGHT",
            "WEIGHT",
            "COLLEGE",
            "COUNTRY",
            "DRAFT_YEAR",
            "DRAFT_ROUND",
            "DRAFT_NUMBER",
            "ROSTER_STATUS",
            "PTS",
            "REB",
            "AST",
            "STATS_TIMEFRAME",
            "FROM_YEAR",
            "TO_YEAR",
        ]
    }

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(
        self,
        active_nullable=ActiveNullable.default,
        allstar_nullable=AllStarNullable.default,
        college_nullable="",
        country_nullable="",
        draft_pick_nullable="",
        draft_year_nullable="",
        height_nullable="",
        player_position_abbreviation_nullable=PlayerPositionAbbreviationNullable.default,
        historical_nullable=HistoricalNullable.default,
        league_id=LeagueID.default,
        season=Season.default,
        team_id_nullable="",
        weight_nullable="",
        proxy=None,
        headers=None,
        timeout=30,
        get_request=True,
    ):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
            "Active": active_nullable,
            "AllStar": allstar_nullable,
            "College": college_nullable,
            "Country": country_nullable,
            "DraftPick": draft_pick_nullable,
            "DraftYear": draft_year_nullable,
            "Height": height_nullable,
            "PlayerPosition": player_position_abbreviation_nullable,
            "Historical": historical_nullable,
            "LeagueID": league_id,
            "Season": season,
            "TeamID": team_id_nullable,
            "Weight": weight_nullable,
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
        self.data_sets = [
            Endpoint.DataSet(data=data_set)
            for data_set_name, data_set in data_sets.items()
        ]
        self.player_index = Endpoint.DataSet(data=data_sets["PlayerIndex"])
