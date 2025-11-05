"""Parser(s) for boxscorematchupsv3 endpoint."""


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
