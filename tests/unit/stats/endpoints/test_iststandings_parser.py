"""Unit tests for ISTStandings parser."""

import json
import pytest
from pathlib import Path

from nba_api.stats.endpoints._parsers.iststandings import (
    NBAStatsISTStandingsParser,
)


@pytest.fixture
def json_fixture():
    """Load the ISTStandings JSON fixture."""
    fixture_path = (
        Path(__file__).parents[4]
        / "docs"
        / "nba_api"
        / "stats"
        / "endpoints"
        / "responses"
        / "iststandings.json"
    )

    if not fixture_path.exists():
        pytest.skip(f"Response file not found: {fixture_path}")

    with open(fixture_path) as f:
        return json.load(f)


@pytest.fixture
def parser(json_fixture):
    """Create a parser instance with the JSON fixture."""
    return NBAStatsISTStandingsParser(json_fixture)


class TestNBAStatsISTStandingsParser:
    """Test the ISTStandings parser."""

    def test_parser_initialization(self, parser, json_fixture):
        """Test that parser initializes correctly."""
        assert parser.nba_dict == json_fixture

    def test_get_iststandings_headers_returns_list(self, parser):
        """Test get_iststandings_headers returns a list."""
        headers = parser.get_iststandings_headers()

        assert isinstance(headers, list)
        assert len(headers) > 0

    def test_get_iststandings_headers_structure(self, parser):
        """Test headers include expected fields."""
        headers = parser.get_iststandings_headers()

        # Should have league and season first
        assert headers[0] == "leagueId"
        assert headers[1] == "seasonYear"

        # Should have team metadata
        assert "teamId" in headers
        assert "teamCity" in headers
        assert "teamName" in headers
        assert "teamAbbreviation" in headers
        assert "conference" in headers
        assert "istGroup" in headers

        # Should have standings fields
        assert "wins" in headers
        assert "losses" in headers
        assert "pct" in headers
        assert "istGroupRank" in headers
        assert "istWildcardRank" in headers

    def test_get_iststandings_data(self, parser, json_fixture):
        """Test standings data extraction."""
        data = parser.get_iststandings_data()

        assert isinstance(data, list)
        assert len(data) > 0, "Should have team standings data"

        # Each row should be a list
        assert all(isinstance(row, list) for row in data)

        # First two columns should be leagueId and seasonYear
        league_id = json_fixture["leagueId"]
        season_year = json_fixture["seasonYear"]
        for row in data:
            assert row[0] == league_id
            assert row[1] == season_year

    def test_get_data_sets(self, parser):
        """Test get_data_sets returns correct structure."""
        result = parser.get_data_sets()

        assert "Standings" in result

        # Check Standings structure
        assert "headers" in result["Standings"]
        assert "data" in result["Standings"]
        assert isinstance(result["Standings"]["headers"], list)
        assert isinstance(result["Standings"]["data"], list)

    def test_data_row_count_matches_teams(self, parser, json_fixture):
        """Test that data rows match number of teams."""
        data = parser.get_iststandings_data()
        teams_count = len(json_fixture["teams"])

        assert len(data) == teams_count

    def test_headers_contain_game_columns(self, parser, json_fixture):
        """Test that parser flattens games into numbered columns."""
        headers = parser.get_iststandings_headers()

        # Should have game-numbered fields (e.g., gameId1, gameId2)
        # Get the number of games from first team
        num_games = len(json_fixture["teams"][0]["games"])

        # Check for game1 fields
        game1_fields = [h for h in headers if h.endswith("1")]
        assert len(game1_fields) > 0, "Should have game1 fields"

        # Should have gameId for each game number
        for i in range(1, num_games + 1):
            game_id_header = f"gameId{i}"
            assert game_id_header in headers, f"Should have {game_id_header}"

    def test_data_row_count_matches_headers(self, parser):
        """Test that each data row has same number of columns as headers."""
        result = parser.get_data_sets()
        headers = result["Standings"]["headers"]
        data = result["Standings"]["data"]

        for i, row in enumerate(data):
            assert len(row) == len(headers), (
                f"Row {i} has {len(row)} columns but headers has {len(headers)}"
            )

    def test_parser_handles_nested_games(self, parser, json_fixture):
        """Test parser correctly processes nested games structure."""
        # Verify the fixture has nested structure
        assert "teams" in json_fixture
        assert "games" in json_fixture["teams"][0]
        assert len(json_fixture["teams"][0]["games"]) > 0

        # Verify parser extracts data from nested structure
        data = parser.get_iststandings_data()
        assert len(data) > 0, "Should extract data from nested games"

    def test_headers_contain_key_ist_fields(self, parser):
        """Test that parser headers contain key IST tournament fields."""
        headers = parser.get_iststandings_headers()

        # Essential IST fields
        assert "leagueId" in headers
        assert "seasonYear" in headers
        assert "teamId" in headers
        assert "istGroup" in headers
        assert "istGroupRank" in headers
        assert "istWildcardRank" in headers
        assert "wins" in headers
        assert "losses" in headers
        assert "pct" in headers
        assert "diff" in headers
        assert "pts" in headers
        assert "oppPts" in headers

    def test_parser_preserves_team_order(self, parser, json_fixture):
        """Test that parser preserves team order from API response."""
        data = parser.get_iststandings_data()
        headers = parser.get_iststandings_headers()

        # Find teamId index
        team_id_index = headers.index("teamId")

        # Extract teamIds from parsed data
        parsed_team_ids = [row[team_id_index] for row in data]

        # Extract teamIds from fixture
        expected_team_ids = [team["teamId"] for team in json_fixture["teams"]]

        assert parsed_team_ids == expected_team_ids
