from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import (
    LeagueID,
    Season,
)


class ScheduleLeagueV2Int(Endpoint):
    endpoint = "scheduleleaguev2int"
    expected_data = {
        "SeasonGames": [
            "leagueId",
            "seasonYear",
            "gameDate",
            "gameId",
            "gameCode",
            "gameStatus",
            "gameStatusText",
            "gameSequence",
            "gameDateEst",
            "gameTimeEst",
            "gameDateTimeEst",
            "gameDateUTC",
            "gameTimeUTC",
            "gameDateTimeUTC",
            "awayTeamTime",
            "homeTeamTime",
            "day",
            "monthNum",
            "weekNumber",
            "weekName",
            "ifNecessary",
            "seriesGameNumber",
            "gameLabel",
            "gameSubLabel",
            "seriesText",
            "arenaName",
            "arenaState",
            "arenaCity",
            "postponedStatus",
            "branchLink",
            "gameSubtype",
            "isNeutral",
            # homeTeam
            "homeTeam_teamId",
            "homeTeam_teamName",
            "homeTeam_teamCity",
            "homeTeam_teamTricode",
            "homeTeam_teamSlug",
            "homeTeam_wins",
            "homeTeam_losses",
            "homeTeam_score",
            "homeTeam_seed",
            # awayTeam
            "awayTeam_teamId",
            "awayTeam_teamName",
            "awayTeam_teamCity",
            "awayTeam_teamTricode",
            "awayTeam_teamSlug",
            "awayTeam_wins",
            "awayTeam_losses",
            "awayTeam_score",
            "awayTeam_seed",
            # pointsLeaders - May be enumerated as pointsLeaders_0_personId, pointsLeaders_1_personId, etc.
            "pointsLeaders_personId",
            "pointsLeaders_firstName",
            "pointsLeaders_lastName",
            "pointsLeaders_teamId",
            "pointsLeaders_teamCity",
            "pointsLeaders_teamName",
            "pointsLeaders_teamTricode",
            "pointsLeaders_points",
            # broadcasters - May be enumerated if more than one of a type
            "nationalBroadcasters_broadcasterScope",
            "nationalBroadcasters_broadcasterMedia",
            "nationalBroadcasters_broadcasterId",
            "nationalBroadcasters_broadcasterDisplay",
            "nationalBroadcasters_broadcasterAbbreviation",
            "nationalBroadcasters_tapeDelayComments",
            "nationalBroadcasters_broadcasterVideoLink",
            "nationalBroadcasters_broadcasterDescription",
            "nationalBroadcasters_broadcasterTeamId",
            "nationalRadioBroadcasters_broadcasterScope",
            "nationalRadioBroadcasters_broadcasterMedia",
            "nationalRadioBroadcasters_broadcasterId",
            "nationalRadioBroadcasters_broadcasterDisplay",
            "nationalRadioBroadcasters_broadcasterAbbreviation",
            "nationalRadioBroadcasters_tapeDelayComments",
            "nationalRadioBroadcasters_broadcasterVideoLink",
            "nationalRadioBroadcasters_broadcasterDescription",
            "nationalRadioBroadcasters_broadcasterTeamId",
            "nationalOttBroadcasters_broadcasterScope",
            "nationalOttBroadcasters_broadcasterMedia",
            "nationalOttBroadcasters_broadcasterId",
            "nationalOttBroadcasters_broadcasterDisplay",
            "nationalOttBroadcasters_broadcasterAbbreviation",
            "nationalOttBroadcasters_tapeDelayComments",
            "nationalOttBroadcasters_broadcasterVideoLink",
            "nationalOttBroadcasters_broadcasterDescription",
            "nationalOttBroadcasters_broadcasterTeamId",
            "homeTvBroadcasters_broadcasterScope",
            "homeTvBroadcasters_broadcasterMedia",
            "homeTvBroadcasters_broadcasterId",
            "homeTvBroadcasters_broadcasterDisplay",
            "homeTvBroadcasters_broadcasterAbbreviation",
            "homeTvBroadcasters_tapeDelayComments",
            "homeTvBroadcasters_broadcasterVideoLink",
            "homeTvBroadcasters_broadcasterDescription",
            "homeTvBroadcasters_broadcasterTeamId",
            "homeRadioBroadcasters_broadcasterScope",
            "homeRadioBroadcasters_broadcasterMedia",
            "homeRadioBroadcasters_broadcasterId",
            "homeRadioBroadcasters_broadcasterDisplay",
            "homeRadioBroadcasters_broadcasterAbbreviation",
            "homeRadioBroadcasters_tapeDelayComments",
            "homeRadioBroadcasters_broadcasterVideoLink",
            "homeRadioBroadcasters_broadcasterDescription",
            "homeRadioBroadcasters_broadcasterTeamId",
            "homeOttBroadcasters_broadcasterScope",
            "homeOttBroadcasters_broadcasterMedia",
            "homeOttBroadcasters_broadcasterId",
            "homeOttBroadcasters_broadcasterDisplay",
            "homeOttBroadcasters_broadcasterAbbreviation",
            "homeOttBroadcasters_tapeDelayComments",
            "homeOttBroadcasters_broadcasterVideoLink",
            "homeOttBroadcasters_broadcasterDescription",
            "homeOttBroadcasters_broadcasterTeamId",
            "awayTvBroadcasters_broadcasterScope",
            "awayTvBroadcasters_broadcasterMedia",
            "awayTvBroadcasters_broadcasterId",
            "awayTvBroadcasters_broadcasterDisplay",
            "awayTvBroadcasters_broadcasterAbbreviation",
            "awayTvBroadcasters_tapeDelayComments",
            "awayTvBroadcasters_broadcasterVideoLink",
            "awayTvBroadcasters_broadcasterDescription",
            "awayTvBroadcasters_broadcasterTeamId",
            "awayRadioBroadcasters_broadcasterScope",
            "awayRadioBroadcasters_broadcasterMedia",
            "awayRadioBroadcasters_broadcasterId",
            "awayRadioBroadcasters_broadcasterDisplay",
            "awayRadioBroadcasters_broadcasterAbbreviation",
            "awayRadioBroadcasters_tapeDelayComments",
            "awayRadioBroadcasters_broadcasterVideoLink",
            "awayRadioBroadcasters_broadcasterDescription",
            "awayRadioBroadcasters_broadcasterTeamId",
            "awayOttBroadcasters_broadcasterScope",
            "awayOttBroadcasters_broadcasterMedia",
            "awayOttBroadcasters_broadcasterId",
            "awayOttBroadcasters_broadcasterDisplay",
            "awayOttBroadcasters_broadcasterAbbreviation",
            "awayOttBroadcasters_tapeDelayComments",
            "awayOttBroadcasters_broadcasterVideoLink",
            "awayOttBroadcasters_broadcasterDescription",
            "awayOttBroadcasters_broadcasterTeamId",
        ],
        "SeasonWeeks": [
            "leagueId",
            "seasonYear",
            "weekNumber",
            "weekName",
            "startDate",
            "endDate",
        ],
        "BroadcasterList": [
            "leagueId",
            "seasonYear",
            "broadcasterAbbreviation",
            "broadcasterDisplay",
            "broadcasterId",
            "regionId",
        ],
    }

    nba_response = None
    data_sets = None
    season_games = None
    season_weeks = None
    headers = None

    def __init__(
        self,
        league_id=LeagueID.default,
        season=Season.default,
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
            "LeagueID": league_id,
            "Season": season,
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
        self.season_games = Endpoint.DataSet(data=data_sets["SeasonGames"])
        self.season_weeks = Endpoint.DataSet(data=data_sets["SeasonWeeks"])
