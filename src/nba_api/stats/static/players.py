import re
from nba_api.stats.library.data import players, wnba_players
from nba_api.stats.library.data import (
    player_index_id,
    player_index_full_name,
    player_index_first_name,
    player_index_last_name,
    player_index_is_active,
)
import unicodedata


def _find_players(regex_pattern, row_id, players=players):
    players_found = []
    for player in players:
        if re.search(_strip_accents(regex_pattern), _strip_accents(str(player[row_id])), flags=re.I):
            players_found.append(_get_player_dict(player))
    return players_found


def _strip_accents(inputstr: str) -> str:
    """
    Normalize and remove accents from string.
    """
    # Normalize to decomposed form
    normalizedstr = unicodedata.normalize('NFD', inputstr)
    # Filter out accents (Mn = Mark, Nonspacing category)
    return ''.join(charx for charx in normalizedstr if unicodedata.category(charx) != 'Mn')


def _find_player_by_id(player_id, players=players):
    regex_pattern = "^{}$".format(player_id)
    players_list = _find_players(regex_pattern, player_index_id, players=players)
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

# UNIT TEST of find_players_by_full_name w/ accent neutral/normalization search function
if __name__ == "__main__":
    test_cases = [
        # 1. Specific accented names from dataset
        r'^Luka Dončić$',  # Exact match with accent
        r'^Nikola [JV]ović$',  # Flexible first name, specific last name pattern
        r'^[NK]ikola [TJ]opić$',  # Flexible first letter, specific last name
        # 2. Accent-flexible matching
        r'^Sim[oó]ne Fontecchio$',  # Flexible accent on o
        r'^[VN]latko Čančar$',  # Flexible first letter, specific accent
        # 3. Flexible full/partial name matching
        r'(Luka Dončić|Nikola Jokić)',  # Multiple specific accented names
        r'^(Pau|Paul)l [GS]i(l|)geous(-Alexander)?$',  # Flexible name matching
        # 4. Case and accent insensitive
        r'^[BbPp]ogdan [Bb]ogdanović$',  # Multiple case and accent variations
        # 5. Complex name pattern matching
        r'^(Olivier-Maxence|O-M) Prosper$',  # Flexible matching for complex names
        # 6. Exact accented names
        'Luka Dončić',
        'Nikola Jokić',
        'Vlatko Čančar',
        'Simone Fontecchio',
        'Dario Šarić',
        # 7. Name variations
        'LUKA DONCIC',  # No accents, uppercase
        'luka doncic',  # No accents, lowercase
        'Dončić, Luka',  # Reversed order
        'Armel Traore',
        'Tidjane Salaun',
        # 8. Partial name matches
        'Dončic',
        'Jokic',
        'Čančar',
        'Maozinha',
        'Valanciunas',
        # 9. Complex name matching
        'Olivier-Maxence Prosper',
        'O-M Prosper',
        # 10. Similar but not exact matches
        'Nikola Topic',
        'Luka Donci',
        'Dario Saric',
        'Bogdan Bogdanovic',
        # 11. Tricky edge cases
        ' Nikola Jokić ',  # Extra whitespace
        'NIKOLA JOKIĆ',  # Uppercase with accent
        'Jonas valanćiunaŠ'  # wrong accents - should be Valančiūnas
    ]
    for index, testcasex in enumerate(test_cases):
        resultx = find_players_by_full_name(testcasex)
        print(f"Test Case {index + 1} - Result of find_players_by_full_name('{testcasex}'): {resultx}")
