"""Parser(s) for boxscoretraditionalv3 endpoint."""

from .boxscoreadvancedv3 import NBAStatsBoxscoreParserV3


class NBAStatsBoxscoreTraditionalParserV3(NBAStatsBoxscoreParserV3):
    def __init__(self, nba_dict):
        super().__init__(nba_dict)

    def get_start_bench_headers(self):
        return self.get_team_headers() + ["startersBench"]

    def get_start_bench_data(self):
        raw_dict = self.nba_dict[list(self.nba_dict.keys())[1]]
        home_team_info = [
            value
            for key, value in raw_dict["homeTeam"].items()
            if key not in ("players", "statistics", "starters", "bench")
        ]
        home_team_starter = raw_dict["homeTeam"]["starters"]
        home_team_bench = raw_dict["homeTeam"]["bench"]
        home_team_starter_stats = (
            [x for x in home_team_starter.values()] + ["Starters"]
            if home_team_starter is not None
            else ["Starters"]
        )
        home_team_bench_stats = (
            [x for x in home_team_bench.values()] + ["Bench"]
            if home_team_bench is not None
            else ["Bench"]
        )

        away_team_info = [
            value
            for key, value in raw_dict["awayTeam"].items()
            if key not in ("players", "statistics", "starters", "bench")
        ]
        away_team_starter = raw_dict["awayTeam"]["starters"]
        away_team_bench = raw_dict["awayTeam"]["bench"]
        away_team_starter_stats = (
            [x for x in away_team_starter.values()] + ["Starters"]
            if away_team_starter is not None
            else ["Starters"]
        )
        away_team_bench_stats = (
            [x for x in away_team_bench.values()] + ["Bench"]
            if away_team_bench is not None
            else ["Bench"]
        )

        return [
            [raw_dict["gameId"]] + home_team_info + home_team_starter_stats,
            [raw_dict["gameId"]] + home_team_info + home_team_bench_stats,
            [raw_dict["gameId"]] + away_team_info + away_team_starter_stats,
            [raw_dict["gameId"]] + away_team_info + away_team_bench_stats,
        ]

    def get_data_sets(self):
        results = {
            "PlayerStats": None,
            "TeamStarterBenchStats": None,
            "TeamStats": None,
        }
        team_head = [
            x for x in self.get_team_headers() if x not in ("starters", "bench")
        ]
        player_head = [
            x for x in self.get_players_headers() if x not in ("starters", "bench")
        ]
        start_bench_head = [
            x
            for x in self.get_start_bench_headers()
            if x not in ("starters", "bench", "plusMinusPoints")
        ]
        team_data = [
            [y for y in x if not isinstance(y, dict)] for x in self.get_team_data()
        ]
        pl_data = [
            [y for y in x if not isinstance(y, dict)] for x in self.get_player_data()
        ]
        start_bench_data = self.get_start_bench_data()
        results["TeamStats"] = {"headers": team_head, "data": team_data}
        results["PlayerStats"] = {"headers": player_head, "data": pl_data}
        results["TeamStarterBenchStats"] = {
            "headers": start_bench_head,
            "data": start_bench_data,
        }
        return results
