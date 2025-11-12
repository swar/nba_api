"""Unit tests for ScheduleLeagueV2 parser."""

import json
import pytest
from pathlib import Path

from nba_api.stats.endpoints._parsers.scheduleleaguev2 import (
    NBAStatsScheduleLeagueV2Parser,
)


@pytest.fixture
def json_fixture():
    """Load the ScheduleLeagueV2 JSON fixture."""
    fixture_path = (
        Path(__file__).parents[4]
        / "docs"
        / "nba_api"
        / "stats"
        / "endpoints"
        / "responses"
        / "scheduleleaguev2.json"
    )

    if not fixture_path.exists():
        pytest.skip(f"Response file not found: {fixture_path}")

    with open(fixture_path) as f:
        return json.load(f)


@pytest.fixture
def parser(json_fixture):
    """Create a parser instance with the JSON fixture."""
    return NBAStatsScheduleLeagueV2Parser(json_fixture)


class TestNBAStatsScheduleLeagueV2Parser:
    """Test the ScheduleLeague V2 parser."""

    def test_parser_initialization(self, parser, json_fixture):
        """Test that parser initializes correctly."""
        assert parser.nba_dict == json_fixture

    def test_get_data_sets(self, parser):
        """Test get_data_sets returns correct structure."""
        result = parser.get_data_sets()

        assert "SeasonGames" in result
        assert "SeasonWeeks" in result

        # Check SeasonGames structure
        assert "headers" in result["SeasonGames"]
        assert "data" in result["SeasonGames"]
        assert isinstance(result["SeasonGames"]["headers"], list)
        assert isinstance(result["SeasonGames"]["data"], list)

        # Check SeasonWeeks structure
        assert "headers" in result["SeasonWeeks"]
        assert "data" in result["SeasonWeeks"]
        assert isinstance(result["SeasonWeeks"]["headers"], list)
        assert isinstance(result["SeasonWeeks"]["data"], list)

    def test_get_weeks_headers_returns_tuple(self, parser):
        """Test get_weeks_headers returns a tuple."""
        headers = parser.get_weeks_headers()

        assert isinstance(headers, tuple)
        assert len(headers) > 0

    def test_get_weeks_headers_structure(self, parser):
        """Test weeks headers include expected fields."""
        headers = parser.get_weeks_headers()

        # Should have league and season first
        assert "leagueId" in headers
        assert "seasonYear" in headers

    def test_get_weeks_data(self, parser, json_fixture):
        """Test weeks data extraction."""
        data = parser.get_weeks_data()

        assert isinstance(data, list)

        # Each row should be a list
        if len(data) > 0:
            assert all(isinstance(row, list) for row in data)

            # First two columns should be leagueId and seasonYear
            league_id = json_fixture["leagueSchedule"]["leagueId"]
            season_year = json_fixture["leagueSchedule"]["seasonYear"]
            for row in data:
                assert row[0] == league_id
                assert row[1] == season_year

    def test_get_games_headers_returns_tuple(self, parser):
        """Test get_games_headers returns a tuple."""
        headers = parser.get_games_headers()

        assert isinstance(headers, tuple)
        assert len(headers) > 0

    def test_get_games_headers_structure(self, parser):
        """Test games headers include expected fields."""
        headers = parser.get_games_headers()

        # Should have core fields
        assert "leagueId" in headers
        assert "seasonYear" in headers
        assert "gameDate" in headers
        assert "gameId" in headers
        assert "gameCode" in headers
        assert "gameStatus" in headers

        # Should have team fields
        assert any("homeTeam" in h for h in headers), "Should have homeTeam fields"
        assert any("awayTeam" in h for h in headers), "Should have awayTeam fields"

    def test_get_games_data(self, parser, json_fixture):
        """Test games data extraction."""
        data = parser.get_games_data()

        assert isinstance(data, list)
        assert len(data) > 0, "Should have game data"

        # Each row should be a list
        assert all(isinstance(row, list) for row in data)

        # First three columns should be leagueId, seasonYear, gameDate
        league_id = json_fixture["leagueSchedule"]["leagueId"]
        season_year = json_fixture["leagueSchedule"]["seasonYear"]
        for row in data:
            assert row[0] == league_id
            assert row[1] == season_year
            # gameDate should be a string
            assert isinstance(row[2], str)

    def test_get_team_headers(self, parser):
        """Test team headers generation."""
        headers = parser.get_team_headers()

        assert isinstance(headers, list)
        assert len(headers) > 0

        # Should have both home and away team fields
        home_team_fields = [h for h in headers if h.startswith("homeTeam_")]
        away_team_fields = [h for h in headers if h.startswith("awayTeam_")]

        assert len(home_team_fields) > 0, "Should have homeTeam fields"
        assert len(away_team_fields) > 0, "Should have awayTeam fields"
        assert len(home_team_fields) == len(away_team_fields), "Should have same fields for both teams"

    def test_get_team_data(self, parser, json_fixture):
        """Test team data extraction from a game."""
        # Get first game
        game = json_fixture["leagueSchedule"]["gameDates"][0]["games"][0]
        data = parser.get_team_data(game)

        assert isinstance(data, list)
        assert len(data) > 0

        # Should have data for both teams
        # Each team has teamId, teamName, teamCity, teamTricode, teamSlug, wins, losses, score, seed
        expected_fields_per_team = 9
        assert len(data) >= expected_fields_per_team * 2

    def test_get_broadcaster_types(self, parser):
        """Test broadcaster types extraction."""
        types = parser.get_broadcaster_types()

        assert types is not None
        # Common broadcaster types
        expected_types = [
            "nationalBroadcasters",
            "nationalRadioBroadcasters",
            "homeTvBroadcasters",
            "homeRadioBroadcasters",
            "awayTvBroadcasters",
            "awayRadioBroadcasters",
        ]
        for expected_type in expected_types:
            assert expected_type in types, f"Should have {expected_type}"

    def test_broadcaster_type_max(self, parser):
        """Test broadcaster type max count calculation."""
        max_count = parser.broadcaster_type_max("homeTvBroadcasters")

        assert isinstance(max_count, int)
        assert max_count >= 0

    def test_get_points_leaders_keys(self, parser):
        """Test points leaders keys extraction."""
        keys = parser.get_points_leaders_keys()

        assert isinstance(keys, list)

        # If there are keys, check common fields
        if len(keys) > 0:
            expected_fields = ["personId", "firstName", "lastName", "teamId", "points"]
            for field in expected_fields:
                assert field in keys, f"Should have {field} in points leaders"

    def test_points_leaders_max(self, parser):
        """Test points leaders max count calculation."""
        max_count = parser.points_leaders_max()

        assert isinstance(max_count, int)
        assert max_count >= 0

    def test_data_row_count_matches_headers(self, parser):
        """Test that each data row has same number of columns as headers."""
        result = parser.get_data_sets()

        # Check SeasonGames
        games_headers = result["SeasonGames"]["headers"]
        games_data = result["SeasonGames"]["data"]
        for i, row in enumerate(games_data):
            assert len(row) == len(games_headers), (
                f"Games row {i} has {len(row)} columns but headers has {len(games_headers)}"
            )

        # Check SeasonWeeks
        weeks_headers = result["SeasonWeeks"]["headers"]
        weeks_data = result["SeasonWeeks"]["data"]
        for i, row in enumerate(weeks_data):
            assert len(row) == len(weeks_headers), (
                f"Weeks row {i} has {len(row)} columns but headers has {len(weeks_headers)}"
            )

    def test_parser_handles_nested_structure(self, parser, json_fixture):
        """Test parser correctly processes nested game dates and games."""
        # Verify the fixture has nested structure
        assert "leagueSchedule" in json_fixture
        assert "gameDates" in json_fixture["leagueSchedule"]
        assert len(json_fixture["leagueSchedule"]["gameDates"]) > 0
        assert "games" in json_fixture["leagueSchedule"]["gameDates"][0]

        # Verify parser extracts data from nested structure
        data = parser.get_games_data()
        assert len(data) > 0, "Should extract data from nested games"

    def test_get_game_data(self, parser, json_fixture):
        """Test individual game data extraction."""
        game = json_fixture["leagueSchedule"]["gameDates"][0]["games"][0]
        data = parser.get_game_data(game)

        assert isinstance(data, list)
        assert len(data) > 0

    def test_get_broadcaster_keys(self, parser):
        """Test broadcaster keys extraction."""
        keys = parser.get_broadcaster_keys()

        assert isinstance(keys, list)

        # If there are keys, check common fields
        if len(keys) > 0:
            expected_fields = ["broadcasterScope", "broadcasterMedia", "broadcasterId", "broadcasterDisplay"]
            for field in expected_fields:
                assert field in keys, f"Should have {field} in broadcaster keys"
