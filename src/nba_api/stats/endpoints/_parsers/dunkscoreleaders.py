"""Parser for dunkscoreleaders endpoint."""


class NBAStatsDunkScoreLeadersParser:
    """Parser for dunkscoreleaders endpoint data.

    Parses the nested JSON response from the dunkscoreleaders endpoint into
    tabular datasets for use with Pandas DataFrames.
    """

    def __init__(self, nba_dict):
        """Initialize parser with NBA stats dictionary.

        Args:
            nba_dict: Dictionary containing 'dunks' key with nested data
        """
        self.nba_dict = nba_dict
        self.dunks = nba_dict.get("dunks", [])

    def get_dunkscoreleaders_headers(self):
        """Get headers for dunk score leaders data.

        Returns:
            List of header names for the DunkScoreLeaders dataset

        """
        return [
            "gameId",
            "gameDate",
            "matchup",
            "period",
            "gameClockTime",
            "eventNum",
            "playerId",
            "playerName",
            "firstName",
            "lastName",
            "teamId",
            "teamName",
            "teamCity",
            "teamAbbreviation",
            "dunkScore",
            "jumpSubscore",
            "powerSubscore",
            "styleSubscore",
            "defensiveContestSubscore",
            "maxBallHeight",
            "ballSpeedThroughRim",
            "playerVertical",
            "hangTime",
            "takeoffDistance",
            "reverseDunk",
            "dunk360",
            "throughTheLegs",
            "alleyOop",
            "tipIn",
            "selfOop",
            "playerRotation",
            "playerLateralSpeed",
            "ballDistanceTraveled",
            "ballReachBack",
            "totalBallAcceleration",
            "dunkingHand",
            "jumpingFoot",
            "passLength",
            "catchingHand",
            "catchDistance",
            "lateralCatchDistance",
            "passerId",
            "passerName",
            "passerFirstName",
            "passerLastName",
            "passReleasePoint",
            "shooterId",
            "shooterName",
            "shooterFirstName",
            "shooterLastName",
            "shotReleasePoint",
            "shotLength",
            "defensiveContestLevel",
            "possibleAttemptedCharge",
            "videoAvailable",
        ]

    def get_dunkscoreleaders_data(self):
        """Extract dunkscoreleaders data

        Returns:
            list: A list of rows, where each row represents a dunk event.
        """
        rows = []
        headers = self.get_dunkscoreleaders_headers()
        for dunk in self.dunks:
            row = [dunk.get(header) for header in headers]
            rows.append(row)
        return rows

    def get_data_sets(self):
        """Return all datasets for this endpoint.

        Returns:
            Dictionary mapping dataset name to its headers and data.
        """
        return {
            "DunkScoreLeaders": {
                "headers": self.get_dunkscoreleaders_headers(),
                "data": self.get_dunkscoreleaders_data(),
            },
        }
