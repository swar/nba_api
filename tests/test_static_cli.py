from click.testing import CliRunner
from nba_api.nba_cli.nba_cli import get_players, get_teams
import json


def test_get_teams_default_type():
    runner = CliRunner()
    result = runner.invoke(get_teams, ["-s celtics"])
    d = json.loads(result.output)
    assert result.exit_code == 0
    assert all(1610612738 == x["id"] for x in d)


def test_get_teams_by_state():
    runner = CliRunner(echo_stdin=True)
    result = runner.invoke(get_teams, "-t state -s oregon".split())

    d = json.loads(result.output)
    assert result.exit_code == 0
    assert all("Oregon" == x["state"] for x in d)


def test_get_teams_by_city():
    runner = CliRunner()
    result = runner.invoke(get_teams, ["-t", "city", "-s", "los angeles"])
    d = json.loads(result.output)
    assert result.exit_code == 0
    assert all(x["city"] == "Los Angeles" for x in d)
    # assert all(x in result.output for x in ["1610612746", "1610612747"])


def test_get_teams_by_abbrev():
    runner = CliRunner()
    result = runner.invoke(get_teams, "-t abbrev -s tor".split())
    d = json.loads(result.output)
    assert result.exit_code == 0
    assert all(x["id"] == 1610612761 for x in [d])
    # assert "1610612761" in result.output


def test_get_teams_blank():
    runner = CliRunner()
    result = runner.invoke(get_teams)

    assert result.exit_code == 0


def test_get_players_default():
    runner = CliRunner()
    result = runner.invoke(get_players, "-s james".split())
    d = json.loads(result.output)
    assert result.exit_code == 0
    assert all(
        ("james" in x["first_name"].lower() or "james" in x["last_name"].lower())
        for x in d
    )


def test_get_players_full():
    runner = CliRunner()
    result = runner.invoke(get_players, "-t full -s paul".split())
    d = json.loads(result.output)
    assert result.exit_code == 0
    assert all(
        ("paul" in x["first_name"].lower() or "paul" in x["last_name"].lower())
        for x in d
    )


def test_get_players_last():
    runner = CliRunner()
    result = runner.invoke(get_players, "-t last -s anthony".split())
    d = json.loads(result.output)
    assert result.exit_code == 0
    assert all("anthony" in x["last_name"].lower() for x in d)


def test_get_players_first():
    runner = CliRunner()
    result = runner.invoke(get_players, "-t first -s andre".split())
    d = json.loads(result.output)
    assert result.exit_code == 0
    assert all("andre" in x["first_name"].lower() for x in d)


def test_get_players_blank():
    runner = CliRunner()
    result = runner.invoke(get_players)
    
    assert result.exit_code != 0

