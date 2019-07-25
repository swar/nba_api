import click
from nba_api.stats.static import players
from nba_api.stats.static import teams


@click.group()
def cli():
    pass

@cli.command()
@click.argument('player_name')
def get_players(player_name):
    click.echo(players.find_players_by_full_name(player_name))


@cli.command()
@click.argument('team_name')
def get_teams(team_name):
    click.echo(teams.find_teams_by_full_name(team_name))
