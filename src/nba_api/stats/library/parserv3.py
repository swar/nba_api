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


class NBAStatsScheduleLeagueV2Parser:
    def __init__(self, nba_dict):
        self.nba_dict = nba_dict

    def get_data_sets(self):
        results = {"SeasonGames": None, "SeasonWeeks": None}

        weeks_head = list(self.get_weeks_headers())
        weeks_data = self.get_weeks_data()
        results["SeasonWeeks"] = {"headers": weeks_head, "data": weeks_data}

        games_head = list(self.get_games_headers())
        games_data = self.get_games_data()
        results["SeasonGames"] = {"headers": games_head, "data": games_data}

        return results

    def get_weeks_headers(self):
        tmp = self.nba_dict[list(self.nba_dict.keys())[1]]["weeks"][0]
        headers = tuple(["leagueId", "seasonYear"] + [header for header in tmp.keys()])
        return headers

    def get_weeks_data(self):
        tmp = self.nba_dict[list(self.nba_dict.keys())[1]]
        return [
            [tmp["leagueId"], tmp["seasonYear"]] + list(x.values())
            for x in tmp["weeks"]
        ]

    def get_games_headers(self):
        tmp = self.nba_dict[list(self.nba_dict.keys())[1]]["gameDates"][0]["games"][0]
        headers = tuple(
            ["leagueId", "seasonYear", "gameDate"]
            + [
                header
                for header in tmp.keys()
                if header
                not in ("broadcasters", "awayTeam", "homeTeam", "pointsLeaders")
            ]
            + self.get_team_headers()
            + self.get_points_leaders_headers()
            + self.get_broadcaster_headers()
        )
        return headers

    def get_games_data(self):
        data = []
        tmp = self.nba_dict[list(self.nba_dict.keys())[1]]
        all_gameDates = tmp["gameDates"]
        for gameDate in all_gameDates:
            for game in gameDate["games"]:
                data.append(
                    [
                        tmp["leagueId"],
                        tmp["seasonYear"],
                        gameDate["gameDate"],
                    ]
                    + self.get_game_data(game)
                )
        return data

    def get_game_data(self, game_dict):
        data = []
        data.extend(
            [
                v
                for k, v in game_dict.items()
                if k not in ("broadcasters", "pointsLeaders", "homeTeam", "awayTeam")
            ]
        )
        data.extend(self.get_team_data(game_dict))
        data.extend(self.get_points_leaders_data(game_dict))
        data.extend(self.get_broadcaster_data(game_dict))
        return data

    def get_broadcaster_types(self):
        tmp = self.nba_dict[list(self.nba_dict.keys())[1]]["gameDates"][0]["games"][0]
        return tmp["broadcasters"].keys()

    def broadcaster_type_max(self, broadcaster_type):
        all_gameDates = self.nba_dict[list(self.nba_dict.keys())[1]]["gameDates"]
        max_count = 0
        for gameDate in all_gameDates:
            for game in gameDate["games"]:
                max_count = max(max_count, len(game["broadcasters"][broadcaster_type]))
        return max_count

    def get_broadcaster_keys(self):
        all_gameDates = self.nba_dict[list(self.nba_dict.keys())[1]]["gameDates"]
        # Not all games have any broadcasters (so can't use use game 0)
        # Not all broadcasters types are valid for any given game (so can't use broadcaster 0)
        # So we need to iterate over all games and all broadcasters types until we find them
        for gameDate in all_gameDates:
            for game in gameDate["games"]:
                for broadcasters in game["broadcasters"].values():
                    for broadcaster in broadcasters:
                        return list(broadcaster.keys())
        return []  # If there are no broadcasters at all, return an empty list

    def get_broadcaster_headers(self):
        headers = []
        for broadcaster_type in self.get_broadcaster_types():
            max_count = self.broadcaster_type_max(broadcaster_type)
            for i in range(max_count):
                idx = "_" + str(i) if max_count > 1 else ""
                for broadcaster_key in self.get_broadcaster_keys():
                    headers.append(broadcaster_type + idx + "_" + broadcaster_key)
        return headers

    def get_broadcaster_data(self, game_dict):
        data = []
        for broadcaster_type in self.get_broadcaster_types():
            max_count = self.broadcaster_type_max(broadcaster_type)
            ibroadcasters = iter(game_dict["broadcasters"][broadcaster_type])
            for _ in range(max_count):
                broadcaster = next(
                    ibroadcasters, {k: None for k in self.get_broadcaster_keys()}
                )
                data.extend(list(broadcaster.values()))
        return data

    def points_leaders_max(self):
        all_gameDates = self.nba_dict[list(self.nba_dict.keys())[1]]["gameDates"]
        max_count = 0
        for gameDate in all_gameDates:
            for game in gameDate["games"]:
                max_count = max(max_count, len(game["pointsLeaders"]))
        return max_count

    def get_points_leaders_keys(self):
        all_gameDates = self.nba_dict[list(self.nba_dict.keys())[1]]["gameDates"]
        # Future games don't have points leaders (empty array), so iterate until we find one

        for gameDate in all_gameDates:
            for game in gameDate["games"]:
                for pointsLeader in game["pointsLeaders"]:
                    return list(pointsLeader.keys())
        return []

    def get_points_leaders_headers(self):
        headers = []
        keys = self.get_points_leaders_keys()

        max_count = self.points_leaders_max()
        for i in range(max_count):
            idx = "_" + str(i) if max_count > 1 else ""
            for key in keys:
                headers.append("pointsLeaders" + idx + "_" + key)
        return headers

    def get_points_leaders_data(self, game_dict):
        data = []
        max_count = self.points_leaders_max()

        ipointsLeaders = iter(game_dict["pointsLeaders"])
        for _ in range(max_count):
            pointsLeader = next(
                ipointsLeaders,
                {
                    k: None for k in self.get_points_leaders_keys()
                },  # Default to None for missing points leaders
            )
            data.extend(list(pointsLeader.values()))
        return data

    def get_team_headers(self):
        headers = []

        tmp = self.nba_dict[list(self.nba_dict.keys())[1]]
        tmp_team = tmp["gameDates"][0]["games"][0]["homeTeam"]
        team_keys = list(tmp_team.keys())

        for team in ["homeTeam", "awayTeam"]:
            for team_key in team_keys:
                headers.append(team + "_" + team_key)
        return headers

    def get_team_data(self, game_dict):
        tmp_home = game_dict["homeTeam"]
        tmp_away = game_dict["awayTeam"]
        return list(tmp_home.values()) + list(tmp_away.values())


class NBAStatsScheduleLeagueV2IntParser(NBAStatsScheduleLeagueV2Parser):
    def __init__(self, nba_dict):
        super().__init__(nba_dict)

    def get_data_sets(self):
        results = super().get_data_sets()
        results["BroadcasterList"] = None

        broadcaster_head = list(self.get_broadcaster_list_headers())
        broadcaster_data = self.get_broadcaster_list_data()
        results["BroadcasterList"] = {
            "headers": broadcaster_head,
            "data": broadcaster_data,
        }
        return results

    def get_broadcaster_list_headers(self):
        tmp = self.nba_dict[list(self.nba_dict.keys())[1]]["broadcasterList"][0]
        return tuple(["leagueId", "seasonYear"] + [header for header in tmp.keys()])

    def get_broadcaster_list_data(self):
        tmp = self.nba_dict[list(self.nba_dict.keys())[1]]
        return [
            [tmp["leagueId"], tmp["seasonYear"]] + list(x.values())
            for x in tmp["broadcasterList"]
        ]


class NBAStatsBoxscoreSummaryParserV3:
    """Parser for BoxScoreSummary v3 endpoint.

    Extracts game summary data including game info, arena details, officials,
    line scores, inactive players, historical matchups, and game statistics.
    """

    def __init__(self, nba_dict):
        self.nba_dict = nba_dict

    def get_game_summary_headers(self):
        """Return column headers for the GameSummary dataset.

        Returns:
            list: Column names for core game information.
        """
        return [
            "gameId",
            "gameCode",
            "gameStatus",
            "gameStatusText",
            "period",
            "gameClock",
            "gameTimeUTC",
            "gameEt",
            "awayTeamId",
            "homeTeamId",
            "duration",
            "attendance",
            "sellout",
        ]

    def get_game_summary_data(self):
        """Extract core game information from the API response.

        Returns:
            list: Single row containing game status, teams, timing, and attendance.
        """
        summary = self.nba_dict["boxScoreSummary"]
        return [
            [
                summary.get("gameId"),
                summary.get("gameCode"),
                summary.get("gameStatus"),
                summary.get("gameStatusText"),
                summary.get("period"),
                summary.get("gameClock"),
                summary.get("gameTimeUTC"),
                summary.get("gameEt"),
                summary.get("awayTeamId"),
                summary.get("homeTeamId"),
                summary.get("duration"),
                summary.get("attendance"),
                summary.get("sellout"),
            ]
        ]

    def get_arena_info_headers(self):
        """Return column headers for the ArenaInfo dataset.

        Returns:
            list: Column names for arena location and details.
        """
        return [
            "gameId",
            "arenaId",
            "arenaName",
            "arenaCity",
            "arenaState",
            "arenaCountry",
            "arenaTimezone",
        ]

    def get_arena_info_data(self):
        """Extract arena information from the API response.

        Returns:
            list: Single row containing arena details. Returns None values
                  if arena object is missing from the response.
        """
        summary = self.nba_dict["boxScoreSummary"]
        arena = summary.get("arena", {})
        return [
            [
                summary.get("gameId"),
                arena.get("arenaId"),
                arena.get("arenaName"),
                arena.get("arenaCity"),
                arena.get("arenaState"),
                arena.get("arenaCountry"),
                arena.get("arenaTimezone"),
            ]
        ]

    def get_officials_headers(self):
        """Return column headers for the Officials dataset.

        Returns:
            list: Column names for game officials.
        """
        return [
            "gameId",
            "personId",
            "name",
            "nameI",
            "firstName",
            "familyName",
            "jerseyNum",
        ]

    def get_officials_data(self):
        """Extract game officials information from the API response.

        Returns:
            list: Rows for each official. Returns empty list if officials
                  array is missing from the response.
        """
        summary = self.nba_dict["boxScoreSummary"]
        game_id = summary.get("gameId")
        officials = summary.get("officials", [])
        return [
            [
                game_id,
                official.get("personId"),
                official.get("name"),
                official.get("nameI"),
                official.get("firstName"),
                official.get("familyName"),
                official.get("jerseyNum"),
            ]
            for official in officials
        ]

    def get_line_score_headers(self):
        """Return column headers for the LineScore dataset.

        Returns:
            list: Column names for period-by-period scores for both teams.
        """
        return [
            "gameId",
            "teamId",
            "teamCity",
            "teamName",
            "teamTricode",
            "teamSlug",
            "teamWins",
            "teamLosses",
            "period1Score",
            "period2Score",
            "period3Score",
            "period4Score",
            "score",
        ]

    def get_line_score_data(self):
        """Extract period-by-period scoring for both teams.

        Returns:
            list: Two rows (home and away) with scores for each period.
                  Only includes periods 1-4; overtime periods are not included.
        """
        summary = self.nba_dict["boxScoreSummary"]
        game_id = summary.get("gameId")
        data = []

        for team_key in ["homeTeam", "awayTeam"]:
            team = summary.get(team_key, {})
            periods = team.get("periods", [])
            period_scores = [None, None, None, None]
            for period in periods:
                period_num = period.get("period", 0)
                if 1 <= period_num <= 4:
                    period_scores[period_num - 1] = period.get("score")

            data.append(
                [
                    game_id,
                    team.get("teamId"),
                    team.get("teamCity"),
                    team.get("teamName"),
                    team.get("teamTricode"),
                    team.get("teamSlug"),
                    team.get("teamWins"),
                    team.get("teamLosses"),
                    period_scores[0],
                    period_scores[1],
                    period_scores[2],
                    period_scores[3],
                    team.get("score"),
                ]
            )

        return data

    def get_inactive_players_headers(self):
        """Return column headers for the InactivePlayers dataset.

        Returns:
            list: Column names for players who are inactive for the game.
        """
        return ["gameId", "teamId", "personId", "firstName", "familyName", "jerseyNum"]

    def get_inactive_players_data(self):
        """Extract inactive players for both teams.

        Returns:
            list: Rows for each inactive player from both teams. Returns empty
                  list if no inactive players or if inactives array is missing.
        """
        summary = self.nba_dict["boxScoreSummary"]
        game_id = summary.get("gameId")
        data = []

        for team_key in ["homeTeam", "awayTeam"]:
            team = summary.get(team_key, {})
            team_id = team.get("teamId")
            inactives = team.get("inactives", [])
            for inactive in inactives:
                data.append(
                    [
                        game_id,
                        team_id,
                        inactive.get("personId"),
                        inactive.get("firstName"),
                        inactive.get("familyName"),
                        inactive.get("jerseyNum"),
                    ]
                )

        return data

    def get_last_five_meetings_headers(self):
        """Return column headers for the LastFiveMeetings dataset.

        Returns:
            list: Column names for historical matchups between the two teams.
        """
        return [
            "recencyOrder",
            "gameId",
            "gameTimeUTC",
            "gameEt",
            "gameStatus",
            "gameStatusText",
            "awayTeamId",
            "awayTeamCity",
            "awayTeamName",
            "awayTeamTricode",
            "awayTeamScore",
            "awayTeamWins",
            "awayTeamLosses",
            "homeTeamId",
            "homeTeamCity",
            "homeTeamName",
            "homeTeamTricode",
            "homeTeamScore",
            "homeTeamWins",
            "homeTeamLosses",
        ]

    def get_last_five_meetings_data(self):
        """Extract the last five meetings between the two teams.

        Returns:
            list: Rows for up to 5 previous games between these teams,
                  ordered by recency. Returns empty list if lastFiveMeetings
                  is missing from the response.
        """
        summary = self.nba_dict["boxScoreSummary"]
        meetings = summary.get("lastFiveMeetings", {}).get("meetings", [])
        data = []

        for meeting in meetings:
            away_team = meeting.get("awayTeam", {})
            home_team = meeting.get("homeTeam", {})
            data.append(
                [
                    meeting.get("recencyOrder"),
                    meeting.get("gameId"),
                    meeting.get("gameTimeUTC"),
                    meeting.get("gameEt"),
                    meeting.get("gameStatus"),
                    meeting.get("gameStatusText"),
                    away_team.get("teamId"),
                    away_team.get("teamCity"),
                    away_team.get("teamName"),
                    away_team.get("teamTricode"),
                    away_team.get("score"),
                    away_team.get("wins"),
                    away_team.get("losses"),
                    home_team.get("teamId"),
                    home_team.get("teamCity"),
                    home_team.get("teamName"),
                    home_team.get("teamTricode"),
                    home_team.get("score"),
                    home_team.get("wins"),
                    home_team.get("losses"),
                ]
            )

        return data

    def get_available_video_headers(self):
        """Return column headers for the AvailableVideo dataset.

        Returns:
            list: Column names for video availability flags.
        """
        return [
            "gameId",
            "videoAvailableFlag",
            "ptAvailable",
            "ptXYZAvailable",
            "whStatus",
            "hustleStatus",
            "historicalStatus",
        ]

    def get_available_video_data(self):
        """Extract video availability flags for the game.

        Returns:
            list: Single row indicating which video types are available
                  for this game.
        """
        summary = self.nba_dict["boxScoreSummary"]
        return [
            [
                summary.get("gameId"),
                summary.get("videoAvailableFlag"),
                summary.get("ptAvailable"),
                summary.get("ptXYZAvailable"),
                summary.get("whStatus"),
                summary.get("hustleStatus"),
                summary.get("historicalStatus"),
            ]
        ]

    def get_game_info_headers(self):
        """Return column headers for the GameInfo dataset.

        Returns:
            list: Column names for game date, attendance, and duration.
        """
        return ["gameId", "gameDate", "attendance", "gameDuration"]

    def get_game_info_data(self):
        """Extract basic game information (date, attendance, duration).

        Returns:
            list: Single row with game date, attendance, and duration.
        """
        summary = self.nba_dict["boxScoreSummary"]
        return [
            [
                summary.get("gameId"),
                summary.get("gameEt"),
                summary.get("attendance"),
                summary.get("duration"),
            ]
        ]

    def get_other_stats_headers(self):
        """Return column headers for the OtherStats dataset.

        Returns:
            list: Column names for team statistics including points in paint,
                  fast break points, lead changes, and other game stats.
        """
        return [
            "gameId",
            "teamId",
            "teamCity",
            "teamName",
            "teamTricode",
            "points",
            "reboundsTotal",
            "assists",
            "steals",
            "blocks",
            "turnovers",
            "fieldGoalsPercentage",
            "threePointersPercentage",
            "freeThrowsPercentage",
            "pointsInThePaint",
            "pointsSecondChance",
            "pointsFastBreak",
            "biggestLead",
            "leadChanges",
            "timesTied",
            "biggestScoringRun",
            "turnoversTeam",
            "turnoversTotal",
            "reboundsTeam",
            "pointsFromTurnovers",
            "benchPoints",
        ]

    def get_other_stats_data(self):
        """Extract detailed game statistics from postgameCharts.

        Includes traditional stats plus advanced metrics like points in paint,
        fast break points, lead changes, bench points, etc.

        Returns:
            list: Two rows (home and away) with comprehensive game statistics.
                  Returns rows with None values if postgameCharts is missing.
        """
        summary = self.nba_dict["boxScoreSummary"]
        game_id = summary.get("gameId")
        postgame = summary.get("postgameCharts", {})
        data = []

        for team_key in ["homeTeam", "awayTeam"]:
            team = postgame.get(team_key, {})
            stats = team.get("statistics", {})
            data.append(
                [
                    game_id,
                    team.get("teamId"),
                    team.get("teamCity"),
                    team.get("teamName"),
                    team.get("teamTricode"),
                    stats.get("points"),
                    stats.get("reboundsTotal"),
                    stats.get("assists"),
                    stats.get("steals"),
                    stats.get("blocks"),
                    stats.get("turnovers"),
                    stats.get("fieldGoalsPercentage"),
                    stats.get("threePointersPercentage"),
                    stats.get("freeThrowsPercentage"),
                    stats.get("pointsInThePaint"),
                    stats.get("pointsSecondChance"),
                    stats.get("pointsFastBreak"),
                    stats.get("biggestLead"),
                    stats.get("leadChanges"),
                    stats.get("timesTied"),
                    stats.get("biggestScoringRun"),
                    stats.get("turnoversTeam"),
                    stats.get("turnoversTotal"),
                    stats.get("reboundsTeam"),
                    stats.get("pointsFromTurnovers"),
                    stats.get("benchPoints"),
                ]
            )

        return data

    def get_data_sets(self):
        """Compile all datasets for the BoxScoreSummary endpoint.

        Aggregates data from all getter methods into a dictionary of datasets,
        each containing headers and data in the format expected by the
        Endpoint.DataSet class.

        Returns:
            dict: Dictionary with 9 datasets (GameSummary, GameInfo, ArenaInfo,
                  Officials, LineScore, InactivePlayers, LastFiveMeetings,
                  OtherStats, AvailableVideo). Each dataset contains 'headers'
                  and 'data' keys.
        """
        results = {
            "GameSummary": None,
            "GameInfo": None,
            "ArenaInfo": None,
            "Officials": None,
            "LineScore": None,
            "InactivePlayers": None,
            "LastFiveMeetings": None,
            "OtherStats": None,
            "AvailableVideo": None,
        }

        results["GameSummary"] = {
            "headers": self.get_game_summary_headers(),
            "data": self.get_game_summary_data(),
        }
        results["GameInfo"] = {
            "headers": self.get_game_info_headers(),
            "data": self.get_game_info_data(),
        }
        results["ArenaInfo"] = {
            "headers": self.get_arena_info_headers(),
            "data": self.get_arena_info_data(),
        }
        results["Officials"] = {
            "headers": self.get_officials_headers(),
            "data": self.get_officials_data(),
        }
        results["LineScore"] = {
            "headers": self.get_line_score_headers(),
            "data": self.get_line_score_data(),
        }
        results["InactivePlayers"] = {
            "headers": self.get_inactive_players_headers(),
            "data": self.get_inactive_players_data(),
        }
        results["LastFiveMeetings"] = {
            "headers": self.get_last_five_meetings_headers(),
            "data": self.get_last_five_meetings_data(),
        }
        results["OtherStats"] = {
            "headers": self.get_other_stats_headers(),
            "data": self.get_other_stats_data(),
        }
        results["AvailableVideo"] = {
            "headers": self.get_available_video_headers(),
            "data": self.get_available_video_data(),
        }

        return results
