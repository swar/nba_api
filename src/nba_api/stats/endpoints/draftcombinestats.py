from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import LeagueID, SeasonAll_Time


class DraftCombineStats(Endpoint):
    endpoint = "draftcombinestats"
    expected_data = {
        "DraftCombineStats": [
            "SEASON",
            "PLAYER_ID",
            "FIRST_NAME",
            "LAST_NAME",
            "PLAYER_NAME",
            "POSITION",
            "HEIGHT_WO_SHOES",
            "HEIGHT_WO_SHOES_FT_IN",
            "HEIGHT_W_SHOES",
            "HEIGHT_W_SHOES_FT_IN",
            "WEIGHT",
            "WINGSPAN",
            "WINGSPAN_FT_IN",
            "STANDING_REACH",
            "STANDING_REACH_FT_IN",
            "BODY_FAT_PCT",
            "HAND_LENGTH",
            "HAND_WIDTH",
            "STANDING_VERTICAL_LEAP",
            "MAX_VERTICAL_LEAP",
            "LANE_AGILITY_TIME",
            "MODIFIED_LANE_AGILITY_TIME",
            "THREE_QUARTER_SPRINT",
            "BENCH_PRESS",
            "SPOT_FIFTEEN_CORNER_LEFT",
            "SPOT_FIFTEEN_BREAK_LEFT",
            "SPOT_FIFTEEN_TOP_KEY",
            "SPOT_FIFTEEN_BREAK_RIGHT",
            "SPOT_FIFTEEN_CORNER_RIGHT",
            "SPOT_COLLEGE_CORNER_LEFT",
            "SPOT_COLLEGE_BREAK_LEFT",
            "SPOT_COLLEGE_TOP_KEY",
            "SPOT_COLLEGE_BREAK_RIGHT",
            "SPOT_COLLEGE_CORNER_RIGHT",
            "SPOT_NBA_CORNER_LEFT",
            "SPOT_NBA_BREAK_LEFT",
            "SPOT_NBA_TOP_KEY",
            "SPOT_NBA_BREAK_RIGHT",
            "SPOT_NBA_CORNER_RIGHT",
            "OFF_DRIB_FIFTEEN_BREAK_LEFT",
            "OFF_DRIB_FIFTEEN_TOP_KEY",
            "OFF_DRIB_FIFTEEN_BREAK_RIGHT",
            "OFF_DRIB_COLLEGE_BREAK_LEFT",
            "OFF_DRIB_COLLEGE_TOP_KEY",
            "OFF_DRIB_COLLEGE_BREAK_RIGHT",
            "ON_MOVE_FIFTEEN",
            "ON_MOVE_COLLEGE",
        ]
    }

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(
        self,
        league_id=LeagueID.default,
        season_all_time=SeasonAll_Time.default,
        proxy=None,
        headers=None,
        timeout=30,
        get_request=True,
    ):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {"LeagueID": league_id, "SeasonYear": season_all_time}
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
        self.draft_combine_stats = Endpoint.DataSet(data=data_sets["DraftCombineStats"])
