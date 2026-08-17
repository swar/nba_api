import pytest

from nba_api.stats.static import teams


def test_nba_teams():
    assert len(teams.teams) == 30


def test_wnba_teams():
    assert len(teams.wnba_teams) == 13


# --- Conference and division static data -----------------------------------


CONFERENCES = ("East", "West")
DIVISIONS = ("Atlantic", "Central", "Southeast", "Northwest", "Pacific", "Southwest")


def test_every_nba_team_has_conference_and_division():
    nba_ids = {team["id"] for team in teams.get_teams()}
    assert set(teams.team_conferences) == nba_ids
    assert set(teams.team_divisions) == nba_ids


def test_conferences_are_evenly_split():
    by_conference = dict.fromkeys(CONFERENCES, 0)
    for conference in teams.team_conferences.values():
        assert conference in CONFERENCES
        by_conference[conference] += 1
    assert by_conference == {"East": 15, "West": 15}


def test_divisions_have_five_teams_each():
    by_division = dict.fromkeys(DIVISIONS, 0)
    for division in teams.team_divisions.values():
        assert division in DIVISIONS
        by_division[division] += 1
    assert all(count == 5 for count in by_division.values())


@pytest.mark.parametrize(
    "team_id, expected_conference, expected_division",
    [
        (1610612747, "West", "Pacific"),  # Los Angeles Lakers
        (1610612738, "East", "Atlantic"),  # Boston Celtics
        (1610612749, "East", "Central"),  # Milwaukee Bucks
        (1610612759, "West", "Southwest"),  # San Antonio Spurs
        (1610612737, "East", "Southeast"),  # Atlanta Hawks
        (1610612760, "West", "Northwest"),  # Oklahoma City Thunder
    ],
)
def test_known_team_conference_and_division_lookups(
    team_id, expected_conference, expected_division
):
    assert teams.get_team_conference(team_id) == expected_conference
    assert teams.get_team_division(team_id) == expected_division


def test_unknown_team_id_returns_none_for_both_helpers():
    assert teams.get_team_conference(1) is None
    assert teams.get_team_division(1) is None
    # WNBA team ids are intentionally not covered.
    assert teams.get_team_conference(1611661313) is None  # New York Liberty
    assert teams.get_team_division(1611661313) is None


def test_find_teams_by_conference():
    east = teams.find_teams_by_conference("East")
    west = teams.find_teams_by_conference("West")
    assert len(east) == 15
    assert len(west) == 15
    # Case-insensitive.
    assert {t["id"] for t in east} == {
        t["id"] for t in teams.find_teams_by_conference("east")
    }


def test_find_teams_by_division():
    pacific = teams.find_teams_by_division("Pacific")
    assert len(pacific) == 5
    assert {t["abbreviation"] for t in pacific} == {"GSW", "LAC", "LAL", "PHX", "SAC"}
    # Case-insensitive.
    assert {t["id"] for t in pacific} == {
        t["id"] for t in teams.find_teams_by_division("pacific")
    }


def test_find_teams_by_conference_exact_membership_is_disjoint():
    """Guard against a team being swapped between conferences. Count-only
    assertions would still pass if two teams traded conferences; exact
    membership + disjointness will not."""
    east = {t["id"] for t in teams.find_teams_by_conference("East")}
    west = {t["id"] for t in teams.find_teams_by_conference("West")}
    nba_ids = {t["id"] for t in teams.get_teams()}
    assert len(east) == 15
    assert len(west) == 15
    assert east.isdisjoint(west)
    assert east | west == nba_ids


def test_find_teams_by_unknown_value_returns_empty():
    # Division names passed to the conference helper, and vice versa, must
    # return empty rather than silently matching.
    assert teams.find_teams_by_conference("Central") == []
    assert teams.find_teams_by_conference("Pacific") == []
    assert teams.find_teams_by_division("East") == []
    assert teams.find_teams_by_division("Midwest") == []
    # Falsy input is tolerated, not crashing.
    assert teams.find_teams_by_conference(None) == []
    assert teams.find_teams_by_division("") == []
