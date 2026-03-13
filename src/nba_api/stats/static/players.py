import functools
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

# Pre-computed cached lists
_cached_players = None
_cached_active_players = None
_cached_inactive_players = None
_cached_wnba_players = None
_cached_wnba_active_players = None
_cached_wnba_inactive_players = None


@functools.lru_cache(maxsize=128)
def _compile_regex(pattern):
    return re.compile(_strip_accents(pattern), flags=re.I)


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
    compiled = _compile_regex(regex_pattern)
    return [
        _get_player_dict(player)
        for player in players
        if compiled.search(_strip_accents(str(player[row_id])))
    ]


def _find_player_by_id(player_id, _index=_players_by_id):
    player = _index.get(player_id)
    return _get_player_dict(player) if player is not None else None


def _get_players(players=players, _cache=False):
    global _cached_players, _cached_wnba_players
    if _cache:
        if players is wnba_players:
            if _cached_wnba_players is None:
                _cached_wnba_players = [_get_player_dict(p) for p in players]
            return _cached_wnba_players
        else:
            if _cached_players is None:
                _cached_players = [_get_player_dict(p) for p in players]
            return _cached_players
    return [_get_player_dict(p) for p in players]


def _get_active_players(players=players, _cache=False):
    global _cached_active_players, _cached_wnba_active_players
    if _cache:
        if players is wnba_players:
            if _cached_wnba_active_players is None:
                _cached_wnba_active_players = [
                    _get_player_dict(p) for p in players if p[player_index_is_active]
                ]
            return _cached_wnba_active_players
        else:
            if _cached_active_players is None:
                _cached_active_players = [
                    _get_player_dict(p) for p in players if p[player_index_is_active]
                ]
            return _cached_active_players
    return [_get_player_dict(p) for p in players if p[player_index_is_active]]


def _get_inactive_players(players=players, _cache=False):
    global _cached_inactive_players, _cached_wnba_inactive_players
    if _cache:
        if players is wnba_players:
            if _cached_wnba_inactive_players is None:
                _cached_wnba_inactive_players = [
                    _get_player_dict(p)
                    for p in players
                    if not p[player_index_is_active]
                ]
            return _cached_wnba_inactive_players
        else:
            if _cached_inactive_players is None:
                _cached_inactive_players = [
                    _get_player_dict(p)
                    for p in players
                    if not p[player_index_is_active]
                ]
            return _cached_inactive_players
    return [_get_player_dict(p) for p in players if not p[player_index_is_active]]


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
    return _get_players(_cache=True)


def get_active_players():
    return _get_active_players(_cache=True)


def get_inactive_players():
    return _get_inactive_players(_cache=True)


def find_wnba_players_by_full_name(regex_pattern):
    return _find_players(regex_pattern, player_index_full_name, players=wnba_players)


def find_wnba_players_by_first_name(regex_pattern):
    return _find_players(regex_pattern, player_index_first_name, players=wnba_players)


def find_wnba_players_by_last_name(regex_pattern):
    return _find_players(regex_pattern, player_index_last_name, players=wnba_players)


def find_wnba_player_by_id(player_id):
    return _find_player_by_id(player_id, _index=_wnba_players_by_id)


def get_wnba_players():
    return _get_players(players=wnba_players, _cache=True)


def get_wnba_active_players():
    return _get_active_players(players=wnba_players, _cache=True)


def get_wnba_inactive_players():
    return _get_inactive_players(players=wnba_players, _cache=True)
