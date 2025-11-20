"""Parser for boxscorefourfactorsv3 endpoint.

Parses "Four Factors" statistics - the key factors that determine basketball success:
1. Shooting (eFG%) - Effective Field Goal Percentage
2. Turnovers (TOV%) - Turnover Percentage
3. Rebounding (OR%) - Offensive Rebound Percentage
4. Free Throws (FTr) - Free Throw Attempt Rate

Also includes opponent Four Factors for defensive evaluation.

Structure:
    {
        "boxScoreFourFactors": {
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

# Four Factors statistics (same for both team and player)
FOUR_FACTORS_STATS_FIELDS = (
    "minutes",
    "effectiveFieldGoalPercentage",
    "freeThrowAttemptRate",
    "teamTurnoverPercentage",
    "offensiveReboundPercentage",
    "oppEffectiveFieldGoalPercentage",
    "oppFreeThrowAttemptRate",
    "oppTeamTurnoverPercentage",
    "oppOffensiveReboundPercentage",
)


class NBAStatsBoxscoreFourFactorsV3Parser:
    """
    Parser for BoxScoreFourFactorsV3 endpoint.

    Extracts Dean Oliver's "Four Factors" statistics for teams and players:
    - Shooting efficiency (eFG%)
    - Turnover rate
    - Offensive rebounding percentage
    - Free throw attempt rate

    Also includes opponent Four Factors (defensive metrics).
    """

    def __init__(self, nba_dict):
        """
        Initialize parser with NBA Stats API response.

        Args:
            nba_dict (dict): Raw API response dictionary
        """
        self.nba_dict = nba_dict
        self.boxscore = nba_dict.get("boxScoreFourFactors", {})

    def get_team_headers(self):
        """
        Get headers for TeamStats dataset.

        Returns:
            tuple: Column names for team statistics
        """
        return ("gameId",) + TEAM_METADATA_FIELDS + FOUR_FACTORS_STATS_FIELDS

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
            + FOUR_FACTORS_STATS_FIELDS
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
                team_stats.get(field) for field in FOUR_FACTORS_STATS_FIELDS
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
                    player_stats.get(field) for field in FOUR_FACTORS_STATS_FIELDS
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
                  Order matches expected_data in boxscorefourfactorsv3.py
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
