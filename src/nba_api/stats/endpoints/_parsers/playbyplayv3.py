"""Parser for playbyplayv3 endpoint.

This parser extracts play-by-play data from the NBA Stats API v3 format,
which returns nested JSON with game actions and video availability.
"""


class NBAStatsPlayByPlayParserV3:
    """Parser for PlayByPlayV3 endpoint.

    Extracts play-by-play actions and video availability from game data.
    Uses explicit field access and defensive coding to handle edge cases.
    """

    def __init__(self, nba_dict):
        """Initialize parser with API response dictionary.

        Args:
            nba_dict (dict): Raw API response containing game data.
        """
        self.nba_dict = nba_dict
        self.game = nba_dict.get("game", {})

    def get_playbyplay_headers(self):
        """Return column headers for the PlayByPlay dataset.

        Returns:
            tuple: Explicitly defined column names for play-by-play actions.
        """
        return (
            "gameId",
            "actionNumber",
            "clock",
            "period",
            "teamId",
            "teamTricode",
            "personId",
            "playerName",
            "playerNameI",
            "xLegacy",
            "yLegacy",
            "shotDistance",
            "shotResult",
            "isFieldGoal",
            "scoreHome",
            "scoreAway",
            "pointsTotal",
            "location",
            "description",
            "actionType",
            "subType",
            "videoAvailable",
            "shotValue",
            "actionId",
        )

    def get_playbyplay_data(self):
        """Extract play-by-play actions from the API response.

        Returns:
            list: List of action rows, each starting with gameId followed by
                  all action fields in the order defined by headers.
        """
        game_id = self.game.get("gameId")
        actions = self.game.get("actions", [])

        data = []
        for action in actions:
            row = [
                game_id,
                action.get("actionNumber"),
                action.get("clock"),
                action.get("period"),
                action.get("teamId"),
                action.get("teamTricode"),
                action.get("personId"),
                action.get("playerName"),
                action.get("playerNameI"),
                action.get("xLegacy"),
                action.get("yLegacy"),
                action.get("shotDistance"),
                action.get("shotResult"),
                action.get("isFieldGoal"),
                action.get("scoreHome"),
                action.get("scoreAway"),
                action.get("pointsTotal"),
                action.get("location"),
                action.get("description"),
                action.get("actionType"),
                action.get("subType"),
                action.get("videoAvailable"),
                action.get("shotValue"),
                action.get("actionId"),
            ]
            data.append(row)

        return data

    def get_videoavailable_headers(self):
        """Return column headers for the AvailableVideo dataset.

        Returns:
            list: Single header for video availability flag.
        """
        return ["videoAvailable"]

    def get_videoavailable_data(self):
        """Extract video availability flag from the API response.

        Returns:
            list: Single row with video availability value (0 or 1).
        """
        video_available = self.game.get("videoAvailable", 0)
        return [[video_available]]

    def get_data_sets(self):
        """Return all datasets for this endpoint.

        Returns:
            dict: Dictionary containing PlayByPlay and AvailableVideo datasets,
                  each with 'headers' and 'data' keys.
        """
        return {
            "PlayByPlay": {
                "headers": self.get_playbyplay_headers(),
                "data": self.get_playbyplay_data(),
            },
            "AvailableVideo": {
                "headers": self.get_videoavailable_headers(),
                "data": self.get_videoavailable_data(),
            },
        }
