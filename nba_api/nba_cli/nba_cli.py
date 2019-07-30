import click
import json
from nba_api.stats.static import players
from nba_api.stats.static import teams

def show_result(res):
    click.echo(json.dumps(res, indent=4, sort_keys=True))

@click.command()
@click.option('-t','--type','type_', default='full', help="Determines the type of search. Default is full to search both first and last names. Other options include first to match only first names and last to match only last names.")
@click.option('-s','--search_string', required= True, help="Search string. Values with spaces or regex strings must be wrapped in double quotes.")
def get_players(type_, search_string):
    result = ""
    
    if (type_ == "full"):
        result = players.find_players_by_full_name(search_string)
    elif (type_ == "first"):
        result = players.find_players_by_first_name(search_string)
    elif (type_ == "last"):
        result = players.find_players_by_last_name(search_string)
    show_result(result)

@click.command()
@click.option('-t','--type','type_', default='full', help="Determines the type of search. Default is full. Other options include state, city, and abbrev.")
@click.option('-s','--search_string', help="Search string. Values with spaces or regex strings must be wrapped in double quotes.")
def get_teams(type_, search_string):
    result = ""
    
    if (type_ == "full"):
        if (not search_string):
            result = teams.get_teams()
        else:
            result = teams.find_teams_by_full_name(search_string)
    elif (type_ == "state"):
        result = teams.find_teams_by_state(search_string)
    elif (type_ == "city"):
        result = teams.find_teams_by_city(search_string)
    elif (type_ == "abbrev"):
        result = teams.find_team_by_abbreviation(search_string)
    show_result(result)
