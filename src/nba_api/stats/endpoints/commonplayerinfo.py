from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueIDNullable


class CommonPlayerInfo(Endpoint):
    endpoint = "commonplayerinfo"
    expected_data = {
        "AvailableSeasons": ["SEASON_ID"],
        "CommonPlayerInfo": [
            "PERSON_ID",
            "FIRST_NAME",
            "LAST_NAME",
            "DISPLAY_FIRST_LAST",
            "DISPLAY_LAST_COMMA_FIRST",
            "DISPLAY_FI_LAST",
            "PLAYER_SLUG",
            "BIRTHDATE",
            "SCHOOL",
            "COUNTRY",
            "LAST_AFFILIATION",
            "HEIGHT",
            "WEIGHT",
            "SEASON_EXP",
            "JERSEY",
            "POSITION",
            "ROSTERSTATUS",
            "TEAM_ID",
            "TEAM_NAME",
            "TEAM_ABBREVIATION",
            "TEAM_CODE",
            "TEAM_CITY",
            "PLAYERCODE",
            "FROM_YEAR",
            "TO_YEAR",
            "DLEAGUE_FLAG",
            "NBA_FLAG",
            "GAMES_PLAYED_FLAG",
            "DRAFT_YEAR",
            "DRAFT_ROUND",
            "DRAFT_NUMBER",
        ],
        "PlayerHeadlineStats": [
            "PLAYER_ID",
            "PLAYER_NAME",
            "TimeFrame",
            "PTS",
            "AST",
            "REB",
            "PIE",
        ],
    }

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(
        self,
        player_id,
        league_id_nullable=LeagueIDNullable.default,
        proxy=None,
        headers=None,
        timeout=30,
        get_request=True,
    ):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {"PlayerID": player_id, "LeagueID": league_id_nullable}
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
        self.available_seasons = Endpoint.DataSet(data=data_sets["AvailableSeasons"])
        self.common_player_info = Endpoint.DataSet(data=data_sets["CommonPlayerInfo"])
        self.player_headline_stats = Endpoint.DataSet(
            data=data_sets["PlayerHeadlineStats"]
        )
