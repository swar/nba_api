"""Parser for boxscoremiscv3 endpoint.

Parses miscellaneous boxscore statistics including points in various game situations:
- Points off turnovers
- Points from second chance opportunities
- Points from fast breaks
- Points in the paint
- Blocks and blocks against
- Personal fouls and fouls drawn

Structure:
    {
        "boxScoreMisc": {
            "gameId": str,
            "homeTeam": {team_metadata, players[], statistics{}},
            "awayTeam": {team_metadata, players[], statistics{}}
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

# Miscellaneous statistics (same for both team and player)
MISC_STATS_FIELDS = (
    "minutes",
    "pointsOffTurnovers",
    "pointsSecondChance",
    "pointsFastBreak",
    "pointsPaint",
    "oppPointsOffTurnovers",
    "oppPointsSecondChance",
    "oppPointsFastBreak",
    "oppPointsPaint",
    "blocks",
    "blocksAgainst",
    "foulsPersonal",
    "foulsDrawn",
)


class NBAStatsBoxscoreMiscV3Parser:
    """
    Parser for BoxScoreMiscV3 endpoint.

    Extracts miscellaneous statistics for teams and players including:
    - Points in various game situations (off turnovers, second chance, fast break, paint)
    - Opponent points in various game situations
    - Blocks and blocks against
    - Personal fouls and fouls drawn
    """

    def __init__(self, nba_dict):
        """
        Initialize parser with NBA Stats API response.

        Args:
            nba_dict (dict): Raw API response dictionary
        """
        self.nba_dict = nba_dict
        self.boxscore = nba_dict.get("boxScoreMisc", {})

    def get_team_headers(self):
        """
        Get headers for TeamStats dataset.

        Returns:
            tuple: Column names for team statistics
        """
        return ("gameId",) + TEAM_METADATA_FIELDS + MISC_STATS_FIELDS

    def get_player_headers(self):
        """
        Get headers for PlayerStats dataset.

        Returns:
            tuple: Column names for player statistics
        """
        return (
            ("gameId",)
            + TEAM_METADATA_FIELDS
            + PLAYER_METADATA_FIELDS
            + MISC_STATS_FIELDS
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

            # Extract team metadata
            team_metadata = tuple(team.get(field) for field in TEAM_METADATA_FIELDS)

            # Extract team statistics
            team_stats = team.get("statistics", {})
            stats_values = tuple(team_stats.get(field) for field in MISC_STATS_FIELDS)

            # Combine into single row
            row = (game_id,) + team_metadata + stats_values
            data.append(list(row))

        return data

    def get_player_data(self):
        """
        Extract player statistics data for all players on both teams.

        Returns:
            list: List of player data rows
        """
        game_id = self.boxscore.get("gameId")
        data = []

        for team_key in ["awayTeam", "homeTeam"]:
            team = self.boxscore.get(team_key, {})

            # Extract team metadata (same for all players on this team)
            team_metadata = tuple(team.get(field) for field in TEAM_METADATA_FIELDS)

            # Process each player
            for player in team.get("players", []):
                # Extract player metadata
                player_metadata = tuple(
                    player.get(field) for field in PLAYER_METADATA_FIELDS
                )

                # Extract player statistics
                player_stats = player.get("statistics", {})
                stats_values = tuple(
                    player_stats.get(field) for field in MISC_STATS_FIELDS
                )

                # Combine into single row
                row = (game_id,) + team_metadata + player_metadata + stats_values
                data.append(list(row))

        return data

    def get_data_sets(self):
        """
        Get all datasets for this endpoint.

        Returns:
            dict: Dictionary with PlayerStats and TeamStats datasets
                  Order matches expected_data in boxscoremiscv3.py
        """
        return {
            "PlayerStats": {
                "headers": list(self.get_player_headers()),
                "data": self.get_player_data(),
            },
            "TeamStats": {
                "headers": list(self.get_team_headers()),
                "data": self.get_team_data(),
            },
        }
