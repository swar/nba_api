from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.library.parameters import PerMode36, LeagueIDNullable


class PlayerProfileV2(Endpoint):
    endpoint = "playerprofilev2"
    expected_data = {
        "CareerHighs": [
            "PLAYER_ID",
            "GAME_DATE",
            "VS_TEAM_ID",
            "VS_TEAM_CITY",
            "VS_TEAM_NAME",
            "VS_TEAM_ABBREVIATION",
            "STAT",
            "STATS_VALUE",
            "STAT_ORDER",
            "DATE_EST",
        ],
        "CareerTotalsAllStarSeason": [
            "PLAYER_ID",
            "LEAGUE_ID",
            "TEAM_ID",
            "GP",
            "GS",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "STL",
            "BLK",
            "TOV",
            "PF",
            "PTS",
        ],
        "CareerTotalsCollegeSeason": [
            "PLAYER_ID",
            "LEAGUE_ID",
            "ORGANIZATION_ID",
            "GP",
            "GS",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "STL",
            "BLK",
            "TOV",
            "PF",
            "PTS",
        ],
        "CareerTotalsPostSeason": [
            "PLAYER_ID",
            "LEAGUE_ID",
            "TEAM_ID",
            "GP",
            "GS",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "STL",
            "BLK",
            "TOV",
            "PF",
            "PTS",
        ],
        "CareerTotalsPreseason": [
            "PLAYER_ID",
            "LEAGUE_ID",
            "TEAM_ID",
            "GP",
            "GS",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "STL",
            "BLK",
            "TOV",
            "PF",
            "PTS",
        ],
        "CareerTotalsRegularSeason": [
            "PLAYER_ID",
            "LEAGUE_ID",
            "TEAM_ID",
            "GP",
            "GS",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "STL",
            "BLK",
            "TOV",
            "PF",
            "PTS",
        ],
        "NextGame": [
            "GAME_ID",
            "GAME_DATE",
            "GAME_TIME",
            "LOCATION",
            "PLAYER_TEAM_ID",
            "PLAYER_TEAM_CITY",
            "PLAYER_TEAM_NICKNAME",
            "PLAYER_TEAM_ABBREVIATION",
            "VS_TEAM_ID",
            "VS_TEAM_CITY",
            "VS_TEAM_NICKNAME",
            "VS_TEAM_ABBREVIATION",
        ],
        "SeasonHighs": [
            "PLAYER_ID",
            "GAME_DATE",
            "VS_TEAM_ID",
            "VS_TEAM_CITY",
            "VS_TEAM_NAME",
            "VS_TEAM_ABBREVIATION",
            "STAT",
            "STATS_VALUE",
            "STAT_ORDER",
            "DATE_EST",
        ],
        "SeasonRankingsPostSeason": [
            "PLAYER_ID",
            "SEASON_ID",
            "LEAGUE_ID",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "PLAYER_AGE",
            "GP",
            "GS",
            "RANK_MIN",
            "RANK_FGM",
            "RANK_FGA",
            "RANK_FG_PCT",
            "RANK_FG3M",
            "RANK_FG3A",
            "RANK_FG3_PCT",
            "RANK_FTM",
            "RANK_FTA",
            "RANK_FT_PCT",
            "RANK_OREB",
            "RANK_DREB",
            "RANK_REB",
            "RANK_AST",
            "RANK_STL",
            "RANK_BLK",
            "RANK_TOV",
            "RANK_PTS",
            "RANK_EFF",
        ],
        "SeasonRankingsRegularSeason": [
            "PLAYER_ID",
            "SEASON_ID",
            "LEAGUE_ID",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "PLAYER_AGE",
            "GP",
            "GS",
            "RANK_MIN",
            "RANK_FGM",
            "RANK_FGA",
            "RANK_FG_PCT",
            "RANK_FG3M",
            "RANK_FG3A",
            "RANK_FG3_PCT",
            "RANK_FTM",
            "RANK_FTA",
            "RANK_FT_PCT",
            "RANK_OREB",
            "RANK_DREB",
            "RANK_REB",
            "RANK_AST",
            "RANK_STL",
            "RANK_BLK",
            "RANK_TOV",
            "RANK_PTS",
            "RANK_EFF",
        ],
        "SeasonTotalsAllStarSeason": [
            "PLAYER_ID",
            "SEASON_ID",
            "LEAGUE_ID",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "PLAYER_AGE",
            "GP",
            "GS",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "STL",
            "BLK",
            "TOV",
            "PF",
            "PTS",
        ],
        "SeasonTotalsCollegeSeason": [
            "PLAYER_ID",
            "SEASON_ID",
            "LEAGUE_ID",
            "ORGANIZATION_ID",
            "SCHOOL_NAME",
            "PLAYER_AGE",
            "GP",
            "GS",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "STL",
            "BLK",
            "TOV",
            "PF",
            "PTS",
        ],
        "SeasonTotalsPostSeason": [
            "PLAYER_ID",
            "SEASON_ID",
            "LEAGUE_ID",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "PLAYER_AGE",
            "GP",
            "GS",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "STL",
            "BLK",
            "TOV",
            "PF",
            "PTS",
        ],
        "SeasonTotalsPreseason": [
            "PLAYER_ID",
            "SEASON_ID",
            "LEAGUE_ID",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "PLAYER_AGE",
            "GP",
            "GS",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "STL",
            "BLK",
            "TOV",
            "PF",
            "PTS",
        ],
        "SeasonTotalsRegularSeason": [
            "PLAYER_ID",
            "SEASON_ID",
            "LEAGUE_ID",
            "TEAM_ID",
            "TEAM_ABBREVIATION",
            "PLAYER_AGE",
            "GP",
            "GS",
            "MIN",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "FTM",
            "FTA",
            "FT_PCT",
            "OREB",
            "DREB",
            "REB",
            "AST",
            "STL",
            "BLK",
            "TOV",
            "PF",
            "PTS",
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
        per_mode36=PerMode36.default,
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
        self.parameters = {
            "PlayerID": player_id,
            "PerMode": per_mode36,
            "LeagueID": league_id_nullable,
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
        self.career_highs = Endpoint.DataSet(data=data_sets["CareerHighs"])
        self.career_totals_all_star_season = Endpoint.DataSet(
            data=data_sets["CareerTotalsAllStarSeason"]
        )
        self.career_totals_college_season = Endpoint.DataSet(
            data=data_sets["CareerTotalsCollegeSeason"]
        )
        self.career_totals_post_season = Endpoint.DataSet(
            data=data_sets["CareerTotalsPostSeason"]
        )
        self.career_totals_preseason = Endpoint.DataSet(
            data=data_sets["CareerTotalsPreseason"]
        )
        self.career_totals_regular_season = Endpoint.DataSet(
            data=data_sets["CareerTotalsRegularSeason"]
        )
        self.next_game = Endpoint.DataSet(data=data_sets["NextGame"])
        self.season_highs = Endpoint.DataSet(data=data_sets["SeasonHighs"])
        self.season_rankings_post_season = Endpoint.DataSet(
            data=data_sets["SeasonRankingsPostSeason"]
        )
        self.season_rankings_regular_season = Endpoint.DataSet(
            data=data_sets["SeasonRankingsRegularSeason"]
        )
        self.season_totals_all_star_season = Endpoint.DataSet(
            data=data_sets["SeasonTotalsAllStarSeason"]
        )
        self.season_totals_college_season = Endpoint.DataSet(
            data=data_sets["SeasonTotalsCollegeSeason"]
        )
        self.season_totals_post_season = Endpoint.DataSet(
            data=data_sets["SeasonTotalsPostSeason"]
        )
        self.season_totals_preseason = Endpoint.DataSet(
            data=data_sets["SeasonTotalsPreseason"]
        )
        self.season_totals_regular_season = Endpoint.DataSet(
            data=data_sets["SeasonTotalsRegularSeason"]
        )
