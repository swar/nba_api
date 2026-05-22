from nba_api.stats.static import teams


def test_nba_teams():
    assert len(teams.teams) == 30


def test_wnba_teams():
    assert len(teams.wnba_teams) == 15


def test_wnba_2026_expansion_teams_present():
    """Toronto Tempo and Portland Fire joined the WNBA as expansion franchises
    for the 2026 season. Regression guard for https://github.com/swar/nba_api/issues/666."""
    tempo = teams.find_wnba_team_by_abbreviation("TOR")
    assert tempo is not None
    assert tempo["id"] == 1611661332
    assert tempo["full_name"] == "Toronto Tempo"
    assert tempo["nickname"] == "Tempo"
    assert tempo["city"] == "Toronto"
    assert tempo["state"] == "Ontario"
    assert tempo["year_founded"] == 2026

    fire = teams.find_wnba_team_by_abbreviation("POR")
    assert fire is not None
    assert fire["id"] == 1611661327
    assert fire["full_name"] == "Portland Fire"
    assert fire["nickname"] == "Fire"
    assert fire["city"] == "Portland"
    assert fire["state"] == "Oregon"
    assert fire["year_founded"] == 2026

    # Inverse lookup: catches the case where the abbreviation index
    # resolves but the id-keyed lookup falls out of sync.
    assert teams.find_wnba_team_name_by_id(1611661332)["full_name"] == "Toronto Tempo"
    assert teams.find_wnba_team_name_by_id(1611661327)["full_name"] == "Portland Fire"
