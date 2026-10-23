from nba_api.stats.static import teams


def test_nba_teams():
    assert len(teams.teams) == 30


def test_wnba_teams():
    assert len(teams.get_wnba_teams()) == 15


def test_portland_fire():
    team = teams.find_wnba_team_by_abbreviation("POR")

    assert team == {
        "id": 1611661327,
        "full_name": "Portland Fire",
        "abbreviation": "POR",
        "nickname": "Fire",
        "city": "Portland",
        "state": "Oregon",
        "year_founded": 2026,
    }


def test_toronto_tempo():
    team = teams.find_wnba_team_by_abbreviation("TOR")

    assert team == {
        "id": 1611661332,
        "full_name": "Toronto Tempo",
        "abbreviation": "TOR",
        "nickname": "Tempo",
        "city": "Toronto",
        "state": "Ontario",
        "year_founded": 2026,
    }
