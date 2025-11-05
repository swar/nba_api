"""Parser(s) for playbyplayv3 endpoint."""


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
