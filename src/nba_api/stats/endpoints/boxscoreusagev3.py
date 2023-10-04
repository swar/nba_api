from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import (
    EndPeriod,
    EndRange,
    RangeType,
    StartPeriod,
    StartRange,
)


class BoxScoreUsageV3(Endpoint):
    endpoint = "boxscoreusagev3"
    expected_data = {
        "PlayerStats": [
            "gameId",
            "teamId",
            "teamCity",
            "teamName",
            "teamTricode",
            "teamSlug",
            "personId",
            "firstName",
            "familyName",
            "nameI",
            "playerSlug",
            "position",
            "comment",
            "jerseyNum",
            "minutes",
            "usagePercentage",
            "percentageFieldGoalsMade",
            "percentageFieldGoalsAttempted",
            "percentageThreePointersMade",
            "percentageThreePointersAttempted",
            "percentageFreeThrowsMade",
            "percentageFreeThrowsAttempted",
            "percentageReboundsOffensive",
            "percentageReboundsDefensive",
            "percentageReboundsTotal",
            "percentageAssists",
            "percentageTurnovers",
            "percentageSteals",
            "percentageBlocks",
            "percentageBlocksAllowed",
            "percentagePersonalFouls",
            "percentagePersonalFoulsDrawn",
            "percentagePoints",
        ],
        "TeamStats": [
            "gameId",
            "teamId",
            "teamCity",
            "teamName",
            "teamTricode",
            "teamSlug",
            "minutes",
            "usagePercentage",
            "percentageFieldGoalsMade",
            "percentageFieldGoalsAttempted",
            "percentageThreePointersMade",
            "percentageThreePointersAttempted",
            "percentageFreeThrowsMade",
            "percentageFreeThrowsAttempted",
            "percentageReboundsOffensive",
            "percentageReboundsDefensive",
            "percentageReboundsTotal",
            "percentageAssists",
            "percentageTurnovers",
            "percentageSteals",
            "percentageBlocks",
            "percentageBlocksAllowed",
            "percentagePersonalFouls",
            "percentagePersonalFoulsDrawn",
            "percentagePoints",
        ],
    }

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(
        self,
        game_id,
        end_period=EndPeriod.default,
        end_range=EndRange.default,
        range_type=RangeType.default,
        start_period=StartPeriod.default,
        start_range=StartRange.default,
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
            "GameID": game_id,
            "EndPeriod": end_period,
            "EndRange": end_range,
            "RangeType": range_type,
            "StartPeriod": start_period,
            "StartRange": start_range,
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
        data_sets = self.nba_response.get_data_sets(self.endpoint)
        self.data_sets = [
            Endpoint.DataSet(data=data_set)
            for data_set_name, data_set in data_sets.items()
        ]
        self.player_stats = Endpoint.DataSet(data=data_sets["PlayerStats"])
        self.team_stats = Endpoint.DataSet(data=data_sets["TeamStats"])
