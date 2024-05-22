import re
from nba_api.stats.library.data import teams, wnba_teams
from nba_api.stats.library.data import (
    team_index_id,
    team_index_abbreviation,
    team_index_nickname,
    team_index_full_name,
)
from nba_api.stats.library.data import (
    team_index_city,
    team_index_state,
    team_index_year_founded,
)
from nba_api.stats.library.data import team_index_championship_year


def _find_teams(regex_pattern, row_id, teams=teams):
    teams_found = []
    for team in teams:
        if re.search(regex_pattern, str(team[row_id]), flags=re.I):
            teams_found.append(_get_team_dict(team))
    return teams_found


def _find_team_name_by_id(team_id, teams=teams):
    regex_pattern = "^{}$".format(team_id)
    teams_list = _find_teams(regex_pattern, team_index_id, teams=teams)
    if len(teams_list) > 1:
        raise Exception("Found more than 1 id")
    elif not teams_list:
        return None
    else:
        return teams_list[0]


def _find_team_by_abbreviation(abbreviation, teams=teams):
    regex_pattern = "^{}$".format(abbreviation)
    teams_list = _find_teams(regex_pattern, team_index_abbreviation, teams=teams)
    if len(teams_list) > 1:
        raise Exception("Found more than 1 id")
    elif not teams_list:
        return None
    else:
        return teams_list[0]


def _find_teams_by_championship_year(year, teams=teams):
    for team in teams:
        if year in team[team_index_championship_year]:
            result = team[team_index_full_name]
    return result


def _find_teams_by_year_founded(year, teams=teams):
    teams_found = []
    for team in teams:
        if team[team_index_year_founded] == year:
            teams_found.append(_get_team_dict(team))
    return teams_found


def _get_teams(teams=teams):
    teams_list = []
    for team in teams:
        teams_list.append(_get_team_dict(team))
    return teams_list


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
    return _get_teams()


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
    return _find_team_by_abbreviation(abbreviation, teams=wnba_teams)


def find_wnba_team_name_by_id(team_id):
    return _find_team_name_by_id(team_id, teams=wnba_teams)


def get_wnba_teams():
    return _get_teams(teams=wnba_teams)
