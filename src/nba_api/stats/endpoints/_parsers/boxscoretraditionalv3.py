"""Parser for boxscoretraditionalv3 endpoint.

Parses traditional boxscore statistics including field goals, three-pointers,
free throws, rebounds, assists, steals, blocks, turnovers, fouls, and points.

Structure:
    {
        "boxScoreTraditional": {
            "gameId": str,
            "homeTeamId": int,
            "awayTeamId": int,
            "homeTeam": {team_metadata, players[], statistics{}, starters{}, bench{}},
            "awayTeam": {team_metadata, players[], statistics{}, starters{}, bench{}}
        }
    }
"""

# Common metadata fields
TEAM_METADATA_FIELDS = (
    "teamId",
    "teamCity",
    "teamName",
    "teamTricode",
    "teamSlug",
)

PLAYER_METADATA_FIELDS = (
    "personId",
    "firstName",
    "familyName",
    "nameI",
    "playerSlug",
    "position",
    "comment",
    "jerseyNum",
)

# Traditional statistics fields (team and player both have these 20 fields)
TRADITIONAL_STATS_FIELDS = (
    "minutes",
    "fieldGoalsMade",
    "fieldGoalsAttempted",
    "fieldGoalsPercentage",
    "threePointersMade",
    "threePointersAttempted",
    "threePointersPercentage",
    "freeThrowsMade",
    "freeThrowsAttempted",
    "freeThrowsPercentage",
    "reboundsOffensive",
    "reboundsDefensive",
    "reboundsTotal",
    "assists",
    "steals",
    "blocks",
    "turnovers",
    "foulsPersonal",
    "points",
    "plusMinusPoints",
)

# Starter/Bench statistics (same as traditional but NO plusMinusPoints)
STARTER_BENCH_STATS_FIELDS = (
    "minutes",
    "fieldGoalsMade",
    "fieldGoalsAttempted",
    "fieldGoalsPercentage",
    "threePointersMade",
    "threePointersAttempted",
    "threePointersPercentage",
    "freeThrowsMade",
    "freeThrowsAttempted",
    "freeThrowsPercentage",
    "reboundsOffensive",
    "reboundsDefensive",
    "reboundsTotal",
    "assists",
    "steals",
    "blocks",
    "turnovers",
    "foulsPersonal",
    "points",
)


class NBAStatsBoxscoreTraditionalParserV3:
    """
    Parser for BoxScoreTraditionalV3 endpoint.

    Extracts traditional statistics for teams and players including:
    - Field Goals (made, attempted, percentage)
    - Three-Pointers (made, attempted, percentage)
    - Free Throws (made, attempted, percentage)
    - Rebounds (offensive, defensive, total)
    - Assists, Steals, Blocks, Turnovers, Fouls
    - Points and Plus/Minus
    """

    def __init__(self, nba_dict):
        """
        Initialize parser with NBA Stats API response.

        Args:
            nba_dict (dict): Raw API response dictionary
        """
        self.nba_dict = nba_dict
        self.boxscore = nba_dict.get("boxScoreTraditional", {})

    def get_team_headers(self):
        """
        Get headers for TeamStats dataset.

        Returns:
            tuple: Column names for team statistics (26 fields)
        """
        return ("gameId",) + TEAM_METADATA_FIELDS + TRADITIONAL_STATS_FIELDS

    def get_player_headers(self):
        """
        Get headers for PlayerStats dataset.

        Returns:
            tuple: Column names for player statistics (34 fields)
        """
        return (
            ("gameId",)
            + TEAM_METADATA_FIELDS
            + PLAYER_METADATA_FIELDS
            + TRADITIONAL_STATS_FIELDS
        )

    def get_start_bench_headers(self):
        """
        Get headers for TeamStarterBenchStats dataset.

        Returns:
            tuple: Column names for starter/bench statistics (26 fields)
        """
        return (
            ("gameId",)
            + TEAM_METADATA_FIELDS
            + STARTER_BENCH_STATS_FIELDS
            + ("startersBench",)
        )

    def get_team_data(self):
        """
        Extract team statistics data for both home and away teams.

        Returns:
            list: List of two rows [home_team_data, away_team_data]
        """
        game_id = self.boxscore.get("gameId")
        data = []

        for team_key in ["homeTeam", "awayTeam"]:
            team = self.boxscore.get(team_key, {})

            # Team metadata
            team_metadata = [team.get(field) for field in TEAM_METADATA_FIELDS]

            # Team statistics
            stats = team.get("statistics", {})
            team_stats = [stats.get(field) for field in TRADITIONAL_STATS_FIELDS]

            # Combine: gameId + metadata + stats
            row = [game_id] + team_metadata + team_stats
            data.append(row)

        return data

    def get_player_data(self):
        """
        Extract player statistics data for all players from both teams.

        Returns:
            list: List of player data rows
        """
        game_id = self.boxscore.get("gameId")
        data = []

        for team_key in ["homeTeam", "awayTeam"]:
            team = self.boxscore.get(team_key, {})

            # Team metadata (same for all players on this team)
            team_metadata = [team.get(field) for field in TEAM_METADATA_FIELDS]

            # Process each player
            players = team.get("players", [])
            for player in players:
                # Player metadata
                player_metadata = [
                    player.get(field) for field in PLAYER_METADATA_FIELDS
                ]

                # Player statistics
                stats = player.get("statistics", {})
                player_stats = [stats.get(field) for field in TRADITIONAL_STATS_FIELDS]

                # Combine: gameId + team_metadata + player_metadata + stats
                row = [game_id] + team_metadata + player_metadata + player_stats
                data.append(row)

        return data

    def get_start_bench_data(self):
        """
        Extract starter/bench statistics for both teams.

        Returns:
            list: List of four rows [home_starters, home_bench, away_starters, away_bench]
        """
        game_id = self.boxscore.get("gameId")
        data = []

        for team_key in ["homeTeam", "awayTeam"]:
            team = self.boxscore.get(team_key, {})

            # Team metadata
            team_metadata = [team.get(field) for field in TEAM_METADATA_FIELDS]

            # Process starters
            starters = team.get("starters")
            if starters is not None:
                starter_stats = [
                    starters.get(field) for field in STARTER_BENCH_STATS_FIELDS
                ]
            else:
                starter_stats = [None] * len(STARTER_BENCH_STATS_FIELDS)

            # Combine: gameId + metadata + stats + "Starters" label
            starter_row = [game_id] + team_metadata + starter_stats + ["Starters"]
            data.append(starter_row)

            # Process bench
            bench = team.get("bench")
            if bench is not None:
                bench_stats = [bench.get(field) for field in STARTER_BENCH_STATS_FIELDS]
            else:
                bench_stats = [None] * len(STARTER_BENCH_STATS_FIELDS)

            # Combine: gameId + metadata + stats + "Bench" label
            bench_row = [game_id] + team_metadata + bench_stats + ["Bench"]
            data.append(bench_row)

        return data

    def get_data_sets(self):
        """
        Return all datasets for this endpoint.

        Returns:
            dict: Dictionary with PlayerStats, TeamStarterBenchStats, and TeamStats
                  Order matches expected_data in boxscoretraditionalv3.py
        """
        return {
            "PlayerStats": {
                "headers": self.get_player_headers(),
                "data": self.get_player_data(),
            },
            "TeamStarterBenchStats": {
                "headers": self.get_start_bench_headers(),
                "data": self.get_start_bench_data(),
            },
            "TeamStats": {
                "headers": self.get_team_headers(),
                "data": self.get_team_data(),
            },
        }
