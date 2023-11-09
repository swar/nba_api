from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import (
    LeagueID,
    Season,
    SeasonType,
    SeasonNullable,
)


class LeagueStandingsV3(Endpoint):
    endpoint = "leaguestandingsv3"
    expected_data = {
        "Standings": [
            "LeagueID",
            "SeasonID",
            "TeamID",
            "TeamCity",
            "TeamName",
            "TeamSlug",
            "Conference",
            "ConferenceRecord",
            "PlayoffRank",
            "ClinchIndicator",
            "Division",
            "DivisionRecord",
            "DivisionRank",
            "WINS",
            "LOSSES",
            "WinPCT",
            "LeagueRank",
            "Record",
            "HOME",
            "ROAD",
            "L10",
            "Last10Home",
            "Last10Road",
            "OT",
            "ThreePTSOrLess",
            "TenPTSOrMore",
            "LongHomeStreak",
            "strLongHomeStreak",
            "LongRoadStreak",
            "strLongRoadStreak",
            "LongWinStreak",
            "LongLossStreak",
            "CurrentHomeStreak",
            "strCurrentHomeStreak",
            "CurrentRoadStreak",
            "strCurrentRoadStreak",
            "CurrentStreak",
            "strCurrentStreak",
            "ConferenceGamesBack",
            "DivisionGamesBack",
            "ClinchedConferenceTitle",
            "ClinchedDivisionTitle",
            "ClinchedPlayoffBirth",
            "EliminatedConference",
            "EliminatedDivision",
            "AheadAtHalf",
            "BehindAtHalf",
            "TiedAtHalf",
            "AheadAtThird",
            "BehindAtThird",
            "TiedAtThird",
            "Score100PTS",
            "OppScore100PTS",
            "OppOver500",
            "LeadInFGPCT",
            "LeadInReb",
            "FewerTurnovers",
            "PointsPG",
            "OppPointsPG",
            "DiffPointsPG",
            "vsEast",
            "vsAtlantic",
            "vsCentral",
            "vsSoutheast",
            "vsWest",
            "vsNorthwest",
            "vsPacific",
            "vsSouthwest",
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
            "ReturnToPlay_East_PI_Flag",
            "ReturnToPlay_West_PI_Flag",
            "ReturnToPlay_Already_Eliminated",
            "Seeding_Game_1_Outcome",
            "Seeding_Game_2_Outcome",
            "Seeding_Game_3_Outcome",
            "Seeding_Game_4_Outcome",
            "Seeding_Game_5_Outcome",
            "Seeding_Game_6_Outcome",
            "Seeding_Game_7_Outcome",
            "Seeding_Game_8_Outcome",
            "Seeding_Game_1_ID",
            "Seeding_Game_2_ID",
            "Seeding_Game_3_ID",
            "Seeding_Game_4_ID",
            "Seeding_Game_5_ID",
            "Seeding_Game_6_ID",
            "Seeding_Game_7_ID",
            "Seeding_Game_8_ID",
            "Seeding_Game_1_Opponent",
            "Seeding_Game_2_Opponent",
            "Seeding_Game_3_Opponent",
            "Seeding_Game_4_Opponent",
            "Seeding_Game_5_Opponent",
            "Seeding_Game_6_Opponent",
            "Seeding_Game_7_Opponent",
            "Seeding_Game_8_Opponent",
            "Seeding_Game_1_Label",
            "Seeding_Game_2_Label",
            "Seeding_Game_3_Label",
            "Seeding_Game_4_Label",
            "Seeding_Game_5_Label",
            "Seeding_Game_6_Label",
            "Seeding_Game_7_Label",
            "Seeding_Game_8_Label",
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
        season=Season.default,
        season_type=SeasonType.default,
        season_nullable=SeasonNullable.default,
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
            "SeasonType": season_type,
            "SeasonYear": season_nullable,
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
        self.standings = Endpoint.DataSet(data=data_sets["Standings"])
