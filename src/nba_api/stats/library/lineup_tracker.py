from ..endpoints.boxscoretraditionalv3 import BoxScoreTraditionalV3
from ..endpoints.playbyplayv3 import PlayByPlayV3


class LineupTracker:
    def __init__(self, game_id):
        self.game_id = game_id
        self.pbp_data = None
        self.start_lineup = None

    def fetch_data(self):
        """Fetch PBP and Initial Box Score to get 1st Quarter Starters."""
        pbp = PlayByPlayV3(game_id=self.game_id)

        if not pbp:
            raise ValueError(f"Invalid game ID: {self.game_id}")

        self.pbp_data = pbp.get_data_frames()[0]

        # Get official starters
        box = BoxScoreTraditionalV3(game_id=self.game_id)
        box_df = box.get_data_frames()[0]

        starters = box_df[box_df["position"] != ""][["teamId", "personId"]]

        if starters.empty:
            starters = box_df.groupby("teamId").head(5)[["teamId", "personId"]]

        self.start_lineup = starters

    def get_starters_for_quarter(self, quarter):
        """
        Logic:
        1. Start with Quarter 1 Starters
        2. Iterate through PBP events
        3. If EVENTMSGTYPE == 8 (Substitution), swap PLAYER1 (out) for PLAYER2 (in).
        4. Return the set at the beginning of the requested quarter.
        """

        if quarter == 1:
            return self.start_lineup.groupby("teamId")["personId"].aapply(set).to_dict()

        current_lineups = (
            self.start_lineup.groupby("teamId")["personId"].apply(set).to_dict()
        )

        previous_events = self.pbp_data[
            (self.pbp_data["period"] < quarter)
            | (
                (self.pbp_data["period"] == quarter)
                & (self.pbp_data["clock"] == "PT12M00.00S")
            )
        ]

        for _, row in previous_events.iterrows():
            if row["actionType"] == "substitution":
                team_id = row["teamId"]
                player_out = row["personId"]
                player_in = row["personIdValue"]

                if team_id in current_lineups:
                    current_lineups[team_id].discard(player_out)
                    current_lineups[team_id].add(player_in)

        for t_id in current_lineups:
            current_lineups[t_id] = self.validate_lineup(
                current_lineups[t_id], t_id, quarter
            )

        return current_lineups

    def validate_lineup(self, current_set, team_id, quarter):
        """Ensures that there are exactly 5 players by looking ahead in the PBP."""
        if len(current_set) == 5:
            return current_set

        if len(current_set) < 5:
            future_events = self.pbp_data[
                (self.pbp_data_data["period"] == quarter)
                & (self.pbp_data["teamId"] == team_id)
            ]
            for _, row in future_events.iterrows():
                p_id = row["personId"]
                if p_id not in current_set and p_id != 0:
                    current_set.add(p_id)
                    if len(current_set) == 5:
                        break
        return current_set
