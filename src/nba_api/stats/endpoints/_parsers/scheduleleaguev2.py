"""Parser(s) for scheduleleaguev2 endpoint."""


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
        weeks = self.nba_dict[list(self.nba_dict.keys())[1]]["weeks"]
        if not weeks:
            # Return default headers when weeks array is empty (e.g., older seasons)
            headers = tuple(
                [
                    "leagueId",
                    "seasonYear",
                    "weekNumber",
                    "weekName",
                    "startDate",
                    "endDate",
                ]
            )
        else:
            tmp = weeks[0]
            headers = tuple(
                ["leagueId", "seasonYear"] + [header for header in tmp.keys()]
            )
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
