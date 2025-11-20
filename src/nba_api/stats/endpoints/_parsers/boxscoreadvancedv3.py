"""Parser for boxscoreadvancedv3 endpoint.

Parses advanced boxscore statistics including offensive/defensive ratings,
true shooting percentage, pace, and other advanced metrics.

Structure:
    {
        "boxScoreAdvanced": {
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

# Team statistics (includes estimatedTeamTurnoverPercentage)
TEAM_STATS_FIELDS = (
    "minutes",
    "estimatedOffensiveRating",
    "offensiveRating",
    "estimatedDefensiveRating",
    "defensiveRating",
    "estimatedNetRating",
    "netRating",
    "assistPercentage",
    "assistToTurnover",
    "assistRatio",
    "offensiveReboundPercentage",
    "defensiveReboundPercentage",
    "reboundPercentage",
    "estimatedTeamTurnoverPercentage",  # Team only
    "turnoverRatio",
    "effectiveFieldGoalPercentage",
    "trueShootingPercentage",
    "usagePercentage",
    "estimatedUsagePercentage",
    "estimatedPace",
    "pace",
    "pacePer40",
    "possessions",
    "PIE",
)

# Player statistics (no estimatedTeamTurnoverPercentage)
PLAYER_STATS_FIELDS = (
    "minutes",
    "estimatedOffensiveRating",
    "offensiveRating",
    "estimatedDefensiveRating",
    "defensiveRating",
    "estimatedNetRating",
    "netRating",
    "assistPercentage",
    "assistToTurnover",
    "assistRatio",
    "offensiveReboundPercentage",
    "defensiveReboundPercentage",
    "reboundPercentage",
    "turnoverRatio",
    "effectiveFieldGoalPercentage",
    "trueShootingPercentage",
    "usagePercentage",
    "estimatedUsagePercentage",
    "estimatedPace",
    "pace",
    "pacePer40",
    "possessions",
    "PIE",
)


class NBAStatsBoxscoreAdvancedV3Parser:
    """
    Parser for BoxScoreAdvancedV3 endpoint.

    Extracts advanced statistics for teams and players including:
    - Offensive/Defensive/Net Ratings
    - True Shooting Percentage
    - Effective Field Goal Percentage
    - Usage Percentage
    - Pace metrics
    - PIE (Player Impact Estimate)
    """

    def __init__(self, nba_dict):
        """
        Initialize parser with NBA Stats API response.

        Args:
            nba_dict (dict): Raw API response dictionary
        """
        self.nba_dict = nba_dict
        self.boxscore = nba_dict.get("boxScoreAdvanced", {})

    def get_team_headers(self):
        """
        Get headers for TeamStats dataset.

        Returns:
            tuple: Column names for team statistics
        """
        return ("gameId",) + TEAM_METADATA_FIELDS + TEAM_STATS_FIELDS

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
            + PLAYER_STATS_FIELDS
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
            stats_values = tuple(team_stats.get(field) for field in TEAM_STATS_FIELDS)

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
                    player_stats.get(field) for field in PLAYER_STATS_FIELDS
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
                  Order matches expected_data in boxscoreadvancedv3.py
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
