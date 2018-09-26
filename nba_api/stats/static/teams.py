import re
from nba_api.stats.library.data import teams
from nba_api.stats.library.data import team_index_id, team_index_abbreviation, team_index_nickname, team_index_full_name
from nba_api.stats.library.data import team_index_city, team_index_state, team_index_year_founded


def _find_teams(regex_pattern, row_id):
    teams_found = []
    for team in teams:
        if re.search(regex_pattern, str(team[row_id]), flags=re.I):
            teams_found.append(_get_team_dict(team))
    return teams_found


def _get_team_dict(team_row):
    return {
        'id': team_row[team_index_id],
        'full_name': team_row[team_index_full_name],
        'abbreviation': team_row[team_index_abbreviation],
        'nickname': team_row[team_index_nickname],
        'city': team_row[team_index_city],
        'state': team_row[team_index_state],
        'year_founded': team_row[team_index_year_founded]
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
    teams_found = []
    for team in teams:
        if team[team_index_year_founded] == year:
            teams_found.append(_get_team_dict(team))
    return teams_found


def find_team_by_abbreviation(abbreviation):
    regex_pattern = '^{}$'.format(abbreviation)
    teams_list = _find_teams(regex_pattern, team_index_abbreviation)
    if len(teams_list) > 1:
        raise Exception('Found more than 1 id')
    elif not teams_list:
        return None
    else:
        return teams_list[0]


def find_team_name_by_id(team_id):
    regex_pattern = '^{}$'.format(team_id)
    teams_list = _find_teams(regex_pattern, team_index_id)
    if len(teams_list) > 1:
        raise Exception('Found more than 1 id')
    elif not teams_list:
        return None
    else:
        return teams_list[0]


def get_teams():
    teams_list = []
    for team in teams:
        teams_list.append(_get_team_dict(team))
    return teams_list
