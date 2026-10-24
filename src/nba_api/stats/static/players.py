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

# Lookup tables built on first use, keyed by id() of the player list. Each entry
# keeps a reference to its list so the id can't be reused by another object, and
# its length so a table is rebuilt when players are appended or removed.
_stripped_columns = {}
_rows_by_id = {}


def _cached(cache, key, players, build):
    entry = cache.get(key)
    if entry is None or entry[0] is not players or entry[1] != len(players):
        entry = cache[key] = (players, len(players), build())
    return entry[2]


def _stripped_column(players, row_id):
    return _cached(
        _stripped_columns,
        (id(players), row_id),
        players,
        lambda: [_strip_accents(str(player[row_id])) for player in players],
    )


def _build_id_index(players):
    index = {}
    for player in players:
        index.setdefault(str(player[player_index_id]), []).append(player)
    return index


def _find_players(regex_pattern, row_id, players=players):
    pattern = re.compile(_strip_accents(regex_pattern), flags=re.I)
    return [
        _get_player_dict(player)
        for player, value in zip(
            players, _stripped_column(players, row_id), strict=True
        )
        if pattern.search(value)
    ]


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


def _find_player_by_id(player_id, players=players):
    index = _cached(_rows_by_id, id(players), players, lambda: _build_id_index(players))
    players_list = [
        _get_player_dict(player) for player in index.get(str(player_id), [])
    ]
    if len(players_list) > 1:
        raise Exception("Found more than 1 id")
    elif not players_list:
        return None
    else:
        return players_list[0]


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
    return _find_player_by_id(player_id, players=wnba_players)


def get_wnba_players():
    return _get_players(players=wnba_players)


def get_wnba_active_players():
    return _get_active_players(players=wnba_players)


def get_wnba_inactive_players():
    return _get_inactive_players(players=wnba_players)
