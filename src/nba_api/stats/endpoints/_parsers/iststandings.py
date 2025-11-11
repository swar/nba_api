"""Parser(s) for iststandings endpoint."""


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
