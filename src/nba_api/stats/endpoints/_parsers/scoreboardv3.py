"""Parser for scoreboardv3 endpoint."""


class NBAStatsScoreboardV3Parser:
    """Parser for ScoreboardV3 endpoint data.

    Parses the nested JSON response from the scoreboardv3 endpoint into
    tabular datasets for use with Pandas DataFrames.
    """

    def __init__(self, nba_dict):
        """Initialize parser with NBA stats dictionary.

        Args:
            nba_dict: Dictionary containing 'scoreboard' key with nested data
        """
        self.nba_dict = nba_dict
        self.scoreboard = nba_dict.get("scoreboard", {})

    def get_scoreboard_info_headers(self):
        """Get headers for scoreboard-level information.

        Returns:
            Tuple of header names for the ScoreboardInfo dataset
        """
        return (
            "gameDate",
            "leagueId",
            "leagueName",
        )

    def get_scoreboard_info_data(self):
        """Extract scoreboard-level information.

        Returns:
            List containing one row with scoreboard info
        """
        return [[
            self.scoreboard.get("gameDate"),
            self.scoreboard.get("leagueId"),
            self.scoreboard.get("leagueName"),
        ]]

    def get_game_header_headers(self):
        """Get headers for game-level information.

        Returns:
            Tuple of header names for the GameHeader dataset
        """
        return (
            "gameId",
            "gameCode",
            "gameStatus",
            "gameStatusText",
            "period",
            "gameClock",
            "gameTimeUTC",
            "gameEt",
            "regulationPeriods",
            "seriesGameNumber",
            "gameLabel",
            "gameSubLabel",
            "seriesText",
            "ifNecessary",
            "seriesConference",
            "poRoundDesc",
            "gameSubtype",
            "isNeutral",
        )

    def get_game_header_data(self):
        """Extract game header data (one row per game).

        Returns:
            List of rows, one for each game
        """
        games = self.scoreboard.get("games", [])
        data = []

        for game in games:
            data.append([
                game.get("gameId"),
                game.get("gameCode"),
                game.get("gameStatus"),
                game.get("gameStatusText"),
                game.get("period"),
                game.get("gameClock"),
                game.get("gameTimeUTC"),
                game.get("gameEt"),
                game.get("regulationPeriods"),
                game.get("seriesGameNumber"),
                game.get("gameLabel"),
                game.get("gameSubLabel"),
                game.get("seriesText"),
                game.get("ifNecessary"),
                game.get("seriesConference"),
                game.get("poRoundDesc"),
                game.get("gameSubtype"),
                game.get("isNeutral"),
            ])

        return data

    def get_line_score_headers(self):
        """Get headers for line score information.

        Returns:
            Tuple of header names for the LineScore dataset
        """
        return (
            "gameId",
            "teamId",
            "teamCity",
            "teamName",
            "teamTricode",
            "teamSlug",
            "wins",
            "losses",
            "score",
            "seed",
            "inBonus",
            "timeoutsRemaining",
        )

    def get_line_score_data(self):
        """Extract line score data (one row per team per game).

        Returns:
            List of rows with team scoring information
        """
        games = self.scoreboard.get("games", [])
        data = []

        for game in games:
            game_id = game.get("gameId")

            # Home team
            home_team = game.get("homeTeam", {})
            data.append([
                game_id,
                home_team.get("teamId"),
                home_team.get("teamCity"),
                home_team.get("teamName"),
                home_team.get("teamTricode"),
                home_team.get("teamSlug"),
                home_team.get("wins"),
                home_team.get("losses"),
                home_team.get("score"),
                home_team.get("seed"),
                home_team.get("inBonus"),
                home_team.get("timeoutsRemaining"),
            ])

            # Away team
            away_team = game.get("awayTeam", {})
            data.append([
                game_id,
                away_team.get("teamId"),
                away_team.get("teamCity"),
                away_team.get("teamName"),
                away_team.get("teamTricode"),
                away_team.get("teamSlug"),
                away_team.get("wins"),
                away_team.get("losses"),
                away_team.get("score"),
                away_team.get("seed"),
                away_team.get("inBonus"),
                away_team.get("timeoutsRemaining"),
            ])

        return data

    def get_game_leaders_headers(self):
        """Get headers for game leaders information.

        Returns:
            Tuple of header names for the GameLeaders dataset
        """
        return (
            "gameId",
            "teamId",
            "leaderType",
            "personId",
            "name",
            "playerSlug",
            "jerseyNum",
            "position",
            "teamTricode",
            "points",
            "rebounds",
            "assists",
        )

    def get_game_leaders_data(self):
        """Extract game leaders data (home and away for each game).

        Returns:
            List of rows with game leader statistics
        """
        games = self.scoreboard.get("games", [])
        data = []

        for game in games:
            game_id = game.get("gameId")
            game_leaders = game.get("gameLeaders", {})

            # Home leader
            home_leader = game_leaders.get("homeLeaders", {})
            if home_leader:
                home_team = game.get("homeTeam", {})
                data.append([
                    game_id,
                    home_team.get("teamId"),
                    "home",
                    home_leader.get("personId"),
                    home_leader.get("name"),
                    home_leader.get("playerSlug"),
                    home_leader.get("jerseyNum"),
                    home_leader.get("position"),
                    home_leader.get("teamTricode"),
                    home_leader.get("points"),
                    home_leader.get("rebounds"),
                    home_leader.get("assists"),
                ])

            # Away leader
            away_leader = game_leaders.get("awayLeaders", {})
            if away_leader:
                away_team = game.get("awayTeam", {})
                data.append([
                    game_id,
                    away_team.get("teamId"),
                    "away",
                    away_leader.get("personId"),
                    away_leader.get("name"),
                    away_leader.get("playerSlug"),
                    away_leader.get("jerseyNum"),
                    away_leader.get("position"),
                    away_leader.get("teamTricode"),
                    away_leader.get("points"),
                    away_leader.get("rebounds"),
                    away_leader.get("assists"),
                ])

        return data

    def get_team_leaders_headers(self):
        """Get headers for team leaders information.

        Returns:
            Tuple of header names for the TeamLeaders dataset
        """
        return (
            "gameId",
            "teamId",
            "leaderType",
            "personId",
            "name",
            "playerSlug",
            "jerseyNum",
            "position",
            "teamTricode",
            "points",
            "rebounds",
            "assists",
            "seasonLeadersFlag",
        )

    def get_team_leaders_data(self):
        """Extract team leaders data (season averages for team leaders).

        Returns:
            List of rows with team leader season averages
        """
        games = self.scoreboard.get("games", [])
        data = []

        for game in games:
            game_id = game.get("gameId")
            team_leaders = game.get("teamLeaders", {})

            # Home team leader
            home_leader = team_leaders.get("homeLeaders", {})
            if home_leader:
                home_team = game.get("homeTeam", {})
                data.append([
                    game_id,
                    home_team.get("teamId"),
                    "home",
                    home_leader.get("personId"),
                    home_leader.get("name"),
                    home_leader.get("playerSlug"),
                    home_leader.get("jerseyNum"),
                    home_leader.get("position"),
                    home_leader.get("teamTricode"),
                    home_leader.get("points"),
                    home_leader.get("rebounds"),
                    home_leader.get("assists"),
                    team_leaders.get("seasonLeadersFlag"),
                ])

            # Away team leader
            away_leader = team_leaders.get("awayLeaders", {})
            if away_leader:
                away_team = game.get("awayTeam", {})
                data.append([
                    game_id,
                    away_team.get("teamId"),
                    "away",
                    away_leader.get("personId"),
                    away_leader.get("name"),
                    away_leader.get("playerSlug"),
                    away_leader.get("jerseyNum"),
                    away_leader.get("position"),
                    away_leader.get("teamTricode"),
                    away_leader.get("points"),
                    away_leader.get("rebounds"),
                    away_leader.get("assists"),
                    team_leaders.get("seasonLeadersFlag"),
                ])

        return data

    def get_broadcasters_headers(self):
        """Get headers for broadcasters information.

        Returns:
            Tuple of header names for the Broadcasters dataset
        """
        return (
            "gameId",
            "broadcasterType",
            "broadcasterId",
            "broadcastDisplay",
            "broadcasterTeamId",
            "broadcasterDescription",
        )

    def get_broadcasters_data(self):
        """Extract broadcasters data (all broadcaster types for each game).

        Returns:
            List of rows with broadcaster information
        """
        games = self.scoreboard.get("games", [])
        data = []

        broadcaster_types = [
            ("nationalBroadcasters", "nationalTv"),
            ("nationalRadioBroadcasters", "nationalRadio"),
            ("nationalOttBroadcasters", "nationalOtt"),
            ("homeTvBroadcasters", "homeTv"),
            ("homeRadioBroadcasters", "homeRadio"),
            ("homeOttBroadcasters", "homeOtt"),
            ("awayTvBroadcasters", "awayTv"),
            ("awayRadioBroadcasters", "awayRadio"),
            ("awayOttBroadcasters", "awayOtt"),
        ]

        for game in games:
            game_id = game.get("gameId")
            broadcasters = game.get("broadcasters", {})

            for api_field, broadcaster_type in broadcaster_types:
                broadcaster_list = broadcasters.get(api_field, [])
                for broadcaster in broadcaster_list:
                    data.append([
                        game_id,
                        broadcaster_type,
                        broadcaster.get("broadcasterId"),
                        broadcaster.get("broadcastDisplay"),
                        broadcaster.get("broadcasterTeamId"),
                        broadcaster.get("broadcasterDescription"),
                    ])

        return data

    def get_data_sets(self):
        """Return all datasets for this endpoint.

        Returns:
            Dictionary mapping dataset names to their headers and data
        """
        return {
            "ScoreboardInfo": {
                "headers": self.get_scoreboard_info_headers(),
                "data": self.get_scoreboard_info_data(),
            },
            "GameHeader": {
                "headers": self.get_game_header_headers(),
                "data": self.get_game_header_data(),
            },
            "LineScore": {
                "headers": self.get_line_score_headers(),
                "data": self.get_line_score_data(),
            },
            "GameLeaders": {
                "headers": self.get_game_leaders_headers(),
                "data": self.get_game_leaders_data(),
            },
            "TeamLeaders": {
                "headers": self.get_team_leaders_headers(),
                "data": self.get_team_leaders_data(),
            },
            "Broadcasters": {
                "headers": self.get_broadcasters_headers(),
                "data": self.get_broadcasters_data(),
            },
        }
