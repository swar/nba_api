"""Parser for gravityleaders endpoint."""


class NBAStatsGravityLeadersParser:
    """Parser for GravityLeaders endpoint data.

    Parses the nested JSON response from the gravityleaders endpoint into
    tabular datasets for use with Pandas DataFrames.

    The gravity score measures how much defensive attention a player draws,
    calculated from tracking data analyzing defender positions relative to
    the player.
    """

    # Define the expected field order for consistent output
    LEADER_FIELDS = (
        "PLAYERID",
        "FIRSTNAME",
        "LASTNAME",
        "TEAMID",
        "TEAMABBREVIATION",
        "TEAMNAME",
        "TEAMCITY",
        "FRAMES",
        "GRAVITYSCORE",
        "AVGGRAVITYSCORE",
        "ONBALLPERIMETERFRAMES",
        "ONBALLPERIMETERGRAVITYSCORE",
        "AVGONBALLPERIMETERGRAVITYSCORE",
        "OFFBALLPERIMETERFRAMES",
        "OFFBALLPERIMETERGRAVITYSCORE",
        "AVGOFFBALLPERIMETERGRAVITYSCORE",
        "ONBALLINTERIORFRAMES",
        "ONBALLINTERIORGRAVITYSCORE",
        "AVGONBALLINTERIORGRAVITYSCORE",
        "OFFBALLINTERIORFRAMES",
        "OFFBALLINTERIORGRAVITYSCORE",
        "AVGOFFBALLINTERIORGRAVITYSCORE",
        "GAMESPLAYED",
        "MINUTES",
        "PTS",
        "REB",
        "AST",
    )

    def __init__(self, nba_dict):
        """Initialize parser with NBA stats dictionary.

        Args:
            nba_dict: Dictionary containing 'leaders' key.
                      Handles None or malformed input gracefully.
        """
        self.nba_dict = nba_dict if isinstance(nba_dict, dict) else {}
        leaders = self.nba_dict.get("leaders", [])
        self.leaders = leaders if isinstance(leaders, list) else []

    def get_leaders_headers(self):
        """Get headers for gravity leaders data.

        Returns:
            Tuple of header names for the Leaders dataset
        """
        return self.LEADER_FIELDS

    def get_leaders_data(self):
        """Extract gravity leaders data (one row per player).

        Returns:
            List of rows, one for each player in the leaders list.
            Skips malformed entries gracefully.
        """
        data = []
        for leader in self.leaders:
            if not isinstance(leader, dict):
                continue
            row = [leader.get(field) for field in self.LEADER_FIELDS]
            data.append(row)
        return data

    def get_data_sets(self):
        """Return all datasets for this endpoint.

        Returns:
            Dictionary mapping dataset names to their headers and data
        """
        return {
            "leaders": {
                "headers": self.get_leaders_headers(),
                "data": self.get_leaders_data(),
            },
        }
