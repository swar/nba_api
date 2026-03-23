"""Parser for boxscorescoringv3 endpoint.

Parses scoring statistics including shot breakdowns by location and type:
- Field goal attempts and points by location (2pt, 3pt, midrange, paint, fastbreak)
- Free throw points
- Points off turnovers
- Assisted vs unassisted field goals

Structure:
    {
        "boxScoreScoring": {
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

# Scoring statistics (same for both team and player)
SCORING_STATS_FIELDS = (
    "minutes",
    "percentageFieldGoalsAttempted2pt",
    "percentageFieldGoalsAttempted3pt",
    "percentagePoints2pt",
    "percentagePointsMidrange2pt",
    "percentagePoints3pt",
    "percentagePointsFastBreak",
    "percentagePointsFreeThrow",
    "percentagePointsOffTurnovers",
    "percentagePointsPaint",
    "percentageAssisted2pt",
    "percentageUnassisted2pt",
    "percentageAssisted3pt",
    "percentageUnassisted3pt",
    "percentageAssistedFGM",
    "percentageUnassistedFGM",
)


class NBAStatsBoxscoreScoringV3Parser:
    """
    Parser for BoxScoreScoringV3 endpoint.

    Extracts scoring statistics for teams and players including:
    - Field goal attempts distribution by location (2pt, 3pt, midrange, paint)
    - Points distribution by type (fastbreak, free throw, off turnovers)
    - Assisted vs unassisted field goals and baskets
    """

    def __init__(self, nba_dict):
        """
        Initialize parser with NBA Stats API response.

        Args:
            nba_dict (dict): Raw API response dictionary
        """
        self.nba_dict = nba_dict
        self.boxscore = nba_dict.get("boxScoreScoring", {})

    def get_team_headers(self):
        """
        Get headers for TeamStats dataset.

        Returns:
            tuple: Column names for team statistics
        """
        return ("gameId",) + TEAM_METADATA_FIELDS + SCORING_STATS_FIELDS

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
            + SCORING_STATS_FIELDS
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
            stats_values = tuple(
                team_stats.get(field) for field in SCORING_STATS_FIELDS
            )

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
                    player_stats.get(field) for field in SCORING_STATS_FIELDS
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
                  Order matches expected_data in boxscorescoringv3.py
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
