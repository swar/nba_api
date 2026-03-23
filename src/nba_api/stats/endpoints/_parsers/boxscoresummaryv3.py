"""Parser(s) for boxscoresummaryv3 endpoint."""


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
