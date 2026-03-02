import re
import unicodedata

from nba_api.stats.library.data import (
    player_index_first_name,
    player_index_full_name,
    player_index_id,
    player_index_is_active,
    player_index_last_name,
    players,
    wnba_players,
)

# Pre-built index for O(1) ID lookup
_players_by_id = {p[player_index_id]: p for p in players}
_wnba_players_by_id = {p[player_index_id]: p for p in wnba_players}


def _strip_accents(inputstr: str) -> str:
    """
    Normalize and remove accents from string.
    """
    # Normalize to decomposed form
    normalizedstr = unicodedata.normalize("NFD", inputstr)
    # Filter out accents (Mn = Mark, Nonspacing category)
    return "".join(
        charx for charx in normalizedstr if unicodedata.category(charx) != "Mn"
    )


def _find_players(regex_pattern, row_id, players=players):
    compiled = re.compile(_strip_accents(regex_pattern), flags=re.I)
    players_found = []
    for player in players:
        if compiled.search(_strip_accents(str(player[row_id]))):
            players_found.append(_get_player_dict(player))
    return players_found


def _find_player_by_id(player_id, _index=_players_by_id):
    player = _index.get(player_id)
    return _get_player_dict(player) if player is not None else None


def _get_players(players=players):
    players_list = []
    for player in players:
        players_list.append(_get_player_dict(player))
    return players_list


def _get_active_players(players=players):
    players_list = []
    for player in players:
        if player[player_index_is_active]:
            players_list.append(_get_player_dict(player))
    return players_list


def _get_inactive_players(players=players):
    players_list = []
    for player in players:
        if not player[player_index_is_active]:
            players_list.append(_get_player_dict(player))
    return players_list


def _get_player_dict(player_row):
    return {
        "id": player_row[player_index_id],
        "full_name": player_row[player_index_full_name],
        "first_name": player_row[player_index_first_name],
        "last_name": player_row[player_index_last_name],
        "is_active": player_row[player_index_is_active],
    }


def find_players_by_full_name(regex_pattern):
    return _find_players(regex_pattern, player_index_full_name)


def find_players_by_first_name(regex_pattern):
    return _find_players(regex_pattern, player_index_first_name)


def find_players_by_last_name(regex_pattern):
    return _find_players(regex_pattern, player_index_last_name)


def find_player_by_id(player_id):
    return _find_player_by_id(player_id)


def get_players():
    return _get_players()


def get_active_players():
    return _get_active_players()


def get_inactive_players():
    return _get_inactive_players()


def find_wnba_players_by_full_name(regex_pattern):
    return _find_players(regex_pattern, player_index_full_name, players=wnba_players)


def find_wnba_players_by_first_name(regex_pattern):
    return _find_players(regex_pattern, player_index_first_name, players=wnba_players)


def find_wnba_players_by_last_name(regex_pattern):
    return _find_players(regex_pattern, player_index_last_name, players=wnba_players)


def find_wnba_player_by_id(player_id):
    return _find_player_by_id(player_id, _index=_wnba_players_by_id)


def get_wnba_players():
    return _get_players(players=wnba_players)


def get_wnba_active_players():
    return _get_active_players(players=wnba_players)


def get_wnba_inactive_players():
    return _get_inactive_players(players=wnba_players)
