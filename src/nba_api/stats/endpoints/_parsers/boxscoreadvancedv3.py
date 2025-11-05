"""Parser(s) for boxscoreadvancedv3 endpoint."""


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
