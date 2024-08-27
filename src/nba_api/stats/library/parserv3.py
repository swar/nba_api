class NBAStatsBoxscoreParserV3:
    def __init__(self, nba_dict):
        self.nba_dict = nba_dict

    def get_team_headers(self, headers=tuple(), level=0):
        if level == 0:
            tmp = self.nba_dict[list(self.nba_dict.keys())[1]]
            headers = headers + tuple(
                [header for header in tmp.keys() if header == "gameId"]
            )
            return self.get_team_headers(headers, level=1)
        elif level == 1:
            tmp = self.nba_dict[list(self.nba_dict.keys())[1]]["homeTeam"]
            headers = headers + tuple(
                [
                    header
                    for header in tmp.keys()
                    if header not in ("players", "statistics")
                ]
            )
            return self.get_team_headers(headers, level=2)
        else:
            try:
                tmp = self.nba_dict[list(self.nba_dict.keys())[1]]["homeTeam"][
                    "statistics"
                ]
            except KeyError:
                return list(headers)
            headers = headers + tuple([header for header in tmp.keys()])
            return list(headers)

    def get_players_headers(self, headers=tuple(), level=0):
        if level == 0:
            tmp = self.nba_dict[list(self.nba_dict.keys())[1]]
            headers = headers + tuple(
                [header for header in tmp.keys() if header == "gameId"]
            )
            return self.get_players_headers(headers, level=1)
        elif level == 1:
            tmp = self.nba_dict[list(self.nba_dict.keys())[1]]["homeTeam"]
            headers = headers + tuple(
                [
                    header
                    for header in tmp.keys()
                    if header not in ("players", "statistics")
                ]
            )
            return self.get_players_headers(headers, level=2)
        elif level == 2:
            tmp = self.nba_dict[list(self.nba_dict.keys())[1]]["homeTeam"]["players"][0]
            headers = headers + tuple(
                [header for header in tmp.keys() if header != "statistics"]
            )
            return self.get_players_headers(headers, level=3)
        else:
            tmp = self.nba_dict[list(self.nba_dict.keys())[1]]["homeTeam"]["players"][
                0
            ]["statistics"]
            headers = headers + tuple([header for header in tmp.keys()])
            return list(headers)

    def get_data_sets(self):
        results = {"PlayerStats": None, "TeamStats": None}
        team_head = self.get_team_headers()
        player_head = self.get_players_headers()
        team_data = self.get_team_data()
        pl_data = self.get_player_data()
        results["TeamStats"] = {"headers": team_head, "data": team_data}
        results["PlayerStats"] = {"headers": player_head, "data": pl_data}
        return results

    def get_team_data(self):
        raw_dict = self.nba_dict[list(self.nba_dict.keys())[1]]
        home_team_info = [
            value
            for key, value in raw_dict["homeTeam"].items()
            if key not in ("players", "statistics")
        ]
        home_team_stats = [x for x in raw_dict["homeTeam"]["statistics"].values()]

        away_team_info = [
            value
            for key, value in raw_dict["awayTeam"].items()
            if key not in ("players", "statistics")
        ]
        away_team_stats = [x for x in raw_dict["awayTeam"]["statistics"].values()]
        return [
            [raw_dict["gameId"]] + home_team_info + home_team_stats,
            [raw_dict["gameId"]] + away_team_info + away_team_stats,
        ]

    def get_player_data(self):
        raw_dict = self.nba_dict[list(self.nba_dict.keys())[1]]
        game_id = [raw_dict["gameId"]]
        data = []
        for team in ["awayTeam", "homeTeam"]:
            team_info = [
                [
                    value
                    for key, value in raw_dict[team].items()
                    if key not in ("players", "statistics")
                ]
            ]
            n_pl = len(raw_dict[team]["players"])
            play_info = [
                [
                    value
                    for key, value in raw_dict[team]["players"][i].items()
                    if key != "statistics"
                ]
                for i in range(len(raw_dict[team]["players"]))
            ]
            play_stats = [
                [
                    value
                    for key, value in raw_dict[team]["players"][i]["statistics"].items()
                ]
                for i in range(len(raw_dict[team]["players"]))
            ]
            stats = [
                [x, *y, *z, *w]
                for x, y, z, w in zip(
                    game_id * n_pl, team_info * n_pl, play_info, play_stats
                )
            ]
            data = data + stats
        return data


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
            if home_team_starter is not None else ["Starters"]
        )
        home_team_bench_stats = (
            [x for x in home_team_bench.values()] + ["Bench"]
            if home_team_bench is not None else ["Bench"]
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
            if away_team_starter is not None else ["Starters"]
        )
        away_team_bench_stats = (
            [x for x in away_team_bench.values()] + ["Bench"]
            if away_team_bench is not None else ["Bench"]
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


class NBAStatsBoxscoreMatchupsParserV3:
    def __init__(self, nba_dict):
        self.nba_dict = nba_dict

    def get_players_headers(self, headers=tuple(), level=0):
        if level == 0:
            tmp = self.nba_dict[list(self.nba_dict.keys())[1]]
            headers = headers + tuple(
                [header for header in tmp.keys() if header == "gameId"]
            )
            return self.get_players_headers(headers, level=1)
        elif level == 1:
            tmp = self.nba_dict[list(self.nba_dict.keys())[1]]["homeTeam"]
            headers = headers + tuple(
                [
                    header
                    for header in tmp.keys()
                    if header not in ("players", "statistics")
                ]
            )
            return self.get_players_headers(headers, level=2)
        elif level == 2:
            tmp = self.nba_dict[list(self.nba_dict.keys())[1]]["homeTeam"]["players"][0]
            headers = headers + tuple(
                [header + "Off" for header in tmp.keys() if header != "matchups"]
            )
            return self.get_players_headers(headers, level=3)
        elif level == 3:
            tmp = self.nba_dict[list(self.nba_dict.keys())[1]]["homeTeam"]["players"][
                0
            ]["matchups"][0]
            headers = headers + tuple(
                [header + "Def" for header in tmp.keys() if header != "statistics"]
            )
            return self.get_players_headers(headers, level=4)
        else:
            tmp = self.nba_dict[list(self.nba_dict.keys())[1]]["homeTeam"]["players"][
                0
            ]["matchups"][0]["statistics"]
            headers = headers + tuple([header for header in tmp.keys()])
            return list(headers)

    def get_player_data(self):
        tmp = self.nba_dict[list(self.nba_dict.keys())[1]]
        pl_data = []
        for team in ["homeTeam", "awayTeam"]:
            team_info = [tmp["gameId"]] + [
                value for key, value in tmp[team].items() if key != "players"
            ]
            for i, def_pl in enumerate(tmp[team]["players"]):
                for j, off_pl in enumerate(tmp[team]["players"][i]["matchups"]):
                    def_data = [
                        value
                        for key, value in tmp[team]["players"][i].items()
                        if key != "matchups"
                    ]
                    off_data = [
                        value
                        for key, value in tmp[team]["players"][i]["matchups"][j].items()
                        if key != "statistics"
                    ]
                    off_stats = list(
                        tmp[team]["players"][i]["matchups"][j]["statistics"].values()
                    )
                    pl_data.append(team_info + def_data + off_data + off_stats)
        return pl_data

    def get_data_sets(self):
        results = {"PlayerStats": None}
        player_head = self.get_players_headers()
        pl_data = self.get_player_data()
        results["PlayerStats"] = {"headers": player_head, "data": pl_data}
        return results


class NBAStatsPlayByPlayParserV3:
    def __init__(self, nba_dict):
        self.nba_dict = nba_dict

    def get_playbyplay_headers(self, headers=tuple(), level=0):
        if level == 0:
            tmp = self.nba_dict[list(self.nba_dict.keys())[1]]
            headers = headers + tuple(
                [header for header in tmp.keys() if header == "gameId"]
            )
            return self.get_playbyplay_headers(headers, level=1)
        else:
            tmp = self.nba_dict[list(self.nba_dict.keys())[1]]["actions"][0]
            headers = headers + tuple([header for header in tmp.keys()])
            return headers

    def get_playbyplay_data(self):
        return [
            [self.nba_dict["game"]["gameId"]] + list(x.values())
            for x in self.nba_dict["game"]["actions"]
        ]

    def get_videoavailable_headers(self):
        return "videoAvailable"

    def get_videoavailable_data(self):
        return self.nba_dict[list(self.nba_dict.keys())[1]]["videoAvailable"]

    def get_data_sets(self):
        results = {"PlayByPlay": None, "AvailableVideo": None}
        video_head = self.get_videoavailable_headers()
        pbp_head = self.get_playbyplay_headers()

        pbp_data = self.get_playbyplay_data()
        video_data = self.get_videoavailable_data()
        results["PlayByPlay"] = {"headers": pbp_head, "data": pbp_data}
        results["AvailableVideo"] = {"headers": [video_head], "data": [[video_data]]}
        return results


class NBAStatsISTStandingsParser:
    def __init__(self, nba_dict):
        self.nba_dict = nba_dict

    def get_iststandings_headers(self):
        team_header = [
            key for key, value in self.nba_dict["teams"][0].items() if key != "games"
        ]
        game_header = []
        for game in self.nba_dict["teams"][0]["games"]:
            number = game["gameNumber"]
            for key, value in game.items():
                if key == "gameNumber":
                    continue
                header = key + str(number)
                game_header.append(header)
        return ["leagueId"] + ["seasonYear"] + team_header + game_header

    def get_iststandings_data(self):
        teams_data = []
        for team in self.nba_dict["teams"]:
            team_value = []
            t_data = [value for key, value in team.items() if key != "games"]
            team_value.extend([self.nba_dict["leagueId"], self.nba_dict["seasonYear"]])
            team_value.extend(t_data)
            for game in team["games"]:
                for key, value in game.items():
                    if key == "gameNumber":
                        continue
                    team_value.append(value)
            teams_data.append(team_value)
        return teams_data

    def get_data_sets(self):
        results = {"Standings": None}
        iststandings_head = self.get_iststandings_headers()
        iststandings_data = self.get_iststandings_data()
        results["Standings"] = {"headers": iststandings_head, "data": iststandings_data}
        return results
