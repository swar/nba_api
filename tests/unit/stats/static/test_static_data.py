from nba_api.stats.static import teams


def test_nba_teams():
    assert len(teams.teams) == 31


def test_wnba_teams():
    assert len(teams.wnba_teams) == 13


def test_find_team_by_abbreviation():
    gua = teams.find_team_by_abbreviation("GUA")
    assert gua is not None
    assert gua["id"] == 15018
    assert gua["full_name"] == "Guangzhou Loong Lions"
    assert gua["nickname"] == "Loong Lions"
    assert gua["city"] == "Guangzhou"
    assert gua["state"] == "Guangdong"
    assert gua["year_founded"] == 2000
