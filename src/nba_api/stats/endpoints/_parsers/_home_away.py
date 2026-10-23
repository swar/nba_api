"""Home/away team IDs shared by the box score parsers."""

HOME_AWAY_FIELDS = ("homeTeamId", "awayTeamId")


def add_home_away_ids(data_sets, boxscore):
    """
    Append homeTeamId and awayTeamId to every row of every dataset.

    Box score responses give these once per game, so without them a row only
    says which team it belongs to, not whether that team was home or away.

    Args:
        data_sets (dict): {name: {"headers": [...], "data": [[...], ...]}}
        boxscore (dict): The response object holding homeTeamId/awayTeamId

    Returns:
        dict: The same data_sets, with both columns appended
    """
    ids = [boxscore.get(field) for field in HOME_AWAY_FIELDS]
    for data_set in data_sets.values():
        data_set["headers"] = list(data_set["headers"]) + list(HOME_AWAY_FIELDS)
        data_set["data"] = [list(row) + ids for row in data_set["data"]]
    return data_sets
