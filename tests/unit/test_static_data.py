from nba_api.stats.static import teams


def test_nba_teams():
    assert len(teams.teams) == 30


def test_wnba_teams():
    assert len(teams.wnba_teams) == 12
