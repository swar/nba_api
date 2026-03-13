import functools
import re
import unicodedata

from nba_api.stats.library.data import (
    team_index_abbreviation,
    team_index_championship_year,
    team_index_city,
    team_index_full_name,
    team_index_id,
    team_index_nickname,
    team_index_state,
    team_index_year_founded,
    teams,
    wnba_teams,
)

# Pre-built indexes for O(1) lookups
_teams_by_id = {t[team_index_id]: t for t in teams}
_teams_by_abbreviation = {t[team_index_abbreviation]: t for t in teams}
_wnba_teams_by_id = {t[team_index_id]: t for t in wnba_teams}
_wnba_teams_by_abbreviation = {t[team_index_abbreviation]: t for t in wnba_teams}

# Pre-computed cached lists
_cached_teams = None
_cached_wnba_teams = None


@functools.lru_cache(maxsize=128)
def _compile_regex(pattern):
    return re.compile(_strip_accents(pattern), flags=re.I)


def _strip_accents(inputstr: str) -> str:
    normalizedstr = unicodedata.normalize("NFD", inputstr)
    return "".join(c for c in normalizedstr if unicodedata.category(c) != "Mn")


def _find_teams(regex_pattern, row_id, teams=teams):
    compiled = _compile_regex(regex_pattern)
    return [
        _get_team_dict(team)
        for team in teams
        if compiled.search(_strip_accents(str(team[row_id])))
    ]


def _find_team_name_by_id(team_id, _index=_teams_by_id):
    team = _index.get(team_id)
    return _get_team_dict(team) if team is not None else None


def _find_team_by_abbreviation(abbreviation, _index=_teams_by_abbreviation):
    team = _index.get(abbreviation.upper())
    return _get_team_dict(team) if team is not None else None


def _find_teams_by_championship_year(year, teams=teams):
    return [
        _get_team_dict(team)
        for team in teams
        if year in team[team_index_championship_year]
    ]


def _find_teams_by_year_founded(year, teams=teams):
    return [
        _get_team_dict(team) for team in teams if team[team_index_year_founded] == year
    ]


def _get_teams(teams=teams, _cache=False):
    global _cached_teams, _cached_wnba_teams
    if _cache:
        if teams is wnba_teams:
            if _cached_wnba_teams is None:
                _cached_wnba_teams = [_get_team_dict(t) for t in teams]
            return _cached_wnba_teams
        else:
            if _cached_teams is None:
                _cached_teams = [_get_team_dict(t) for t in teams]
            return _cached_teams
    return [_get_team_dict(t) for t in teams]


def _get_team_dict(team_row):
    return {
        "id": team_row[team_index_id],
        "full_name": team_row[team_index_full_name],
        "abbreviation": team_row[team_index_abbreviation],
        "nickname": team_row[team_index_nickname],
        "city": team_row[team_index_city],
        "state": team_row[team_index_state],
        "year_founded": team_row[team_index_year_founded],
    }


def find_teams_by_full_name(regex_pattern):
    return _find_teams(regex_pattern, team_index_full_name)


def find_teams_by_state(regex_pattern):
    return _find_teams(regex_pattern, team_index_state)


def find_teams_by_city(regex_pattern):
    return _find_teams(regex_pattern, team_index_city)


def find_teams_by_nickname(regex_pattern):
    return _find_teams(regex_pattern, team_index_nickname)


def find_teams_by_year_founded(year):
    return _find_teams_by_year_founded(year)


def find_teams_by_championship_year(year):
    return _find_teams_by_championship_year(year)


def find_team_by_abbreviation(abbreviation):
    return _find_team_by_abbreviation(abbreviation)


def find_team_name_by_id(team_id):
    return _find_team_name_by_id(team_id)


def get_teams():
    return _get_teams(_cache=True)


def find_wnba_teams_by_full_name(regex_pattern):
    return _find_teams(regex_pattern, team_index_full_name, teams=wnba_teams)


def find_wnba_teams_by_state(regex_pattern):
    return _find_teams(regex_pattern, team_index_state, teams=wnba_teams)


def find_wnba_teams_by_city(regex_pattern):
    return _find_teams(regex_pattern, team_index_city, teams=wnba_teams)


def find_wnba_teams_by_nickname(regex_pattern):
    return _find_teams(regex_pattern, team_index_nickname, teams=wnba_teams)


def find_wnba_teams_by_year_founded(year):
    return _find_teams_by_year_founded(year, teams=wnba_teams)


def find_wnba_teams_by_championship_year(year):
    return _find_teams_by_championship_year(year, teams=wnba_teams)


def find_wnba_team_by_abbreviation(abbreviation):
    return _find_team_by_abbreviation(abbreviation, _index=_wnba_teams_by_abbreviation)


def find_wnba_team_name_by_id(team_id):
    return _find_team_name_by_id(team_id, _index=_wnba_teams_by_id)


def get_wnba_teams():
    return _get_teams(teams=wnba_teams, _cache=True)
