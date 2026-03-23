"""Parser for boxscoreplayertrackv3 endpoint.

Parses player tracking and movement statistics including:
- Movement: speed, distance traveled
- Ball touches and involvement: touches, passes, secondary assists, free throw assists
- Shooting: assists, contested/uncontested field goals (made, attempted, percentage)
- Rebounding: rebound chances (offensive, defensive, total)
- Defense: defended at rim field goals

Structure:
    {
        "boxScorePlayerTrack": {
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

# Player tracking statistics fields
PLAYERTRACK_STATS_FIELDS = (
    "minutes",
    "speed",
    "distance",
    "reboundChancesOffensive",
    "reboundChancesDefensive",
    "reboundChancesTotal",
    "touches",
    "secondaryAssists",
    "freeThrowAssists",
    "passes",
    "assists",
    "contestedFieldGoalsMade",
    "contestedFieldGoalsAttempted",
    "contestedFieldGoalPercentage",
    "uncontestedFieldGoalsMade",
    "uncontestedFieldGoalsAttempted",
    "uncontestedFieldGoalsPercentage",
    "fieldGoalPercentage",
    "defendedAtRimFieldGoalsMade",
    "defendedAtRimFieldGoalsAttempted",
    "defendedAtRimFieldGoalPercentage",
)


class NBAStatsBoxscorePlayerTrackV3Parser:
    """
    Parser for BoxScorePlayerTrackV3 endpoint.

    Extracts player tracking statistics for teams and players including:
    - Movement metrics (speed, distance)
    - Rebounding opportunities (offensive, defensive, total)
    - Ball handling (touches, passes, assists)
    - Shooting efficiency (contested/uncontested field goals)
    - Defensive impact (defended at rim)
    """

    def __init__(self, nba_dict):
        """
        Initialize parser with NBA Stats API response.

        Args:
            nba_dict (dict): Raw API response dictionary
        """
        self.nba_dict = nba_dict
        self.boxscore = nba_dict.get("boxScorePlayerTrack", {})

    def get_team_headers(self):
        """
        Get headers for TeamStats dataset.

        Returns:
            tuple: Column names for team statistics
        """
        return ("gameId",) + TEAM_METADATA_FIELDS + PLAYERTRACK_STATS_FIELDS

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
            + PLAYERTRACK_STATS_FIELDS
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
                team_stats.get(field) for field in PLAYERTRACK_STATS_FIELDS
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
                    player_stats.get(field) for field in PLAYERTRACK_STATS_FIELDS
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
                  Order matches expected_data in boxscoreplayertrackv3.py
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
