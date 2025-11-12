"""Unit tests for BoxScoreTraditionalV3 parser."""

import pytest
from nba_api.stats.endpoints._parsers.boxscoretraditionalv3 import (
    NBAStatsBoxscoreTraditionalParserV3,
)
from .data.boxscoretraditionalv3 import BOXSCORETRADITIONALV3_SAMPLE


@pytest.fixture
def parser():
    """Create a parser instance with the JSON fixture."""
    return NBAStatsBoxscoreTraditionalParserV3(BOXSCORETRADITIONALV3_SAMPLE)


class TestNBAStatsBoxscoreTraditionalParserV3:
    """Test the BoxScoreTraditional V3 parser."""

    def test_parser_initialization(self, parser):
        """Test that parser initializes correctly."""
        assert parser.nba_dict == BOXSCORETRADITIONALV3_SAMPLE
        assert parser.boxscore == BOXSCORETRADITIONALV3_SAMPLE["boxScoreTraditional"]

    def test_get_team_headers(self, parser):
        """Test TeamStats headers match expected structure."""
        headers = parser.get_team_headers()

        assert isinstance(headers, tuple)
        assert len(headers) == 26
        assert headers[0] == "gameId"
        assert headers[1:6] == ("teamId", "teamCity", "teamName", "teamTricode", "teamSlug")
        # Traditional stats fields
        assert "minutes" in headers
        assert "fieldGoalsMade" in headers
        assert "points" in headers
        assert "plusMinusPoints" in headers

    def test_get_player_headers(self, parser):
        """Test PlayerStats headers match expected structure."""
        headers = parser.get_player_headers()

        assert isinstance(headers, tuple)
        assert len(headers) == 34  # gameId + 5 team + 8 player + 20 stats
        assert headers[0] == "gameId"
        # Team metadata
        assert "teamId" in headers
        # Player metadata
        assert "personId" in headers
        assert "firstName" in headers
        assert "familyName" in headers
        # Stats
        assert "points" in headers
        assert "assists" in headers
        assert "plusMinusPoints" in headers

    def test_get_start_bench_headers(self, parser):
        """Test TeamStarterBenchStats headers."""
        headers = parser.get_start_bench_headers()

        assert isinstance(headers, tuple)
        assert len(headers) == 26  # gameId + 5 team + 19 stats + startersBench
        assert headers[0] == "gameId"
        assert headers[-1] == "startersBench"
        # Should NOT have plusMinusPoints (that's for team/player only)
        assert "plusMinusPoints" not in headers
        assert "points" in headers

    def test_get_team_data(self, parser):
        """Test TeamStats data extraction."""
        data = parser.get_team_data()

        assert len(data) == 2  # home and away
        # Home team
        assert data[0][0] == "0022500165"  # gameId
        assert data[0][1] == 1610612738  # teamId
        assert data[0][2] == "Boston"  # teamCity
        assert data[0][3] == "Celtics"  # teamName
        assert data[0][4] == "BOS"  # teamTricode
        assert data[0][5] == "celtics"  # teamSlug
        # Stats
        assert data[0][6] == "PT120M"  # minutes
        assert data[0][-2] == 122  # points
        assert data[0][-1] == 14  # plusMinusPoints

        # Away team
        assert data[1][1] == 1610612744  # teamId
        assert data[1][2] == "Golden State"
        assert data[1][-2] == 108  # points
        assert data[1][-1] == -14  # plusMinusPoints

    def test_get_player_data(self, parser):
        """Test PlayerStats data extraction."""
        data = parser.get_player_data()

        # Should have 2 players (1 per team in minimal fixture)
        assert len(data) == 2

        # Home team player (Jayson Tatum)
        assert data[0][0] == "0022500165"  # gameId
        assert data[0][1] == 1610612738  # teamId (BOS)
        assert data[0][6] == 1630162  # personId
        assert data[0][7] == "Jayson"  # firstName
        assert data[0][8] == "Tatum"  # familyName
        assert data[0][-2] == 32  # points
        assert data[0][-1] == 12  # plusMinusPoints

        # Away team player (Stephen Curry)
        assert data[1][1] == 1610612744  # teamId (GSW)
        assert data[1][6] == 201939  # personId
        assert data[1][7] == "Stephen"  # firstName
        assert data[1][8] == "Curry"  # familyName
        assert data[1][-2] == 27  # points
        assert data[1][-1] == -15  # plusMinusPoints

    def test_get_start_bench_data(self, parser):
        """Test TeamStarterBenchStats data extraction."""
        data = parser.get_start_bench_data()

        # Should have 4 rows: home starters, home bench, away starters, away bench
        assert len(data) == 4

        # Home starters
        assert data[0][0] == "0022500165"  # gameId
        assert data[0][1] == 1610612738  # teamId
        assert data[0][2] == "Boston"  # teamCity
        assert data[0][-2] == 84  # points
        assert data[0][-1] == "Starters"  # startersBench

        # Home bench
        assert data[1][0] == "0022500165"  # gameId
        assert data[1][1] == 1610612738  # teamId
        assert data[1][-2] == 38  # points
        assert data[1][-1] == "Bench"  # startersBench

        # Away starters
        assert data[2][1] == 1610612744  # teamId (GSW)
        assert data[2][2] == "Golden State"
        assert data[2][-2] == 78  # points
        assert data[2][-1] == "Starters"

        # Away bench
        assert data[3][1] == 1610612744  # teamId (GSW)
        assert data[3][-2] == 30  # points
        assert data[3][-1] == "Bench"

    def test_get_data_sets(self, parser):
        """Test get_data_sets returns all datasets."""
        result = parser.get_data_sets()

        assert "TeamStats" in result
        assert "PlayerStats" in result
        assert "TeamStarterBenchStats" in result

        # Check structure
        assert "headers" in result["TeamStats"]
        assert "data" in result["TeamStats"]
        assert len(result["TeamStats"]["data"]) == 2

        assert "headers" in result["PlayerStats"]
        assert "data" in result["PlayerStats"]
        assert len(result["PlayerStats"]["data"]) == 2

        assert "headers" in result["TeamStarterBenchStats"]
        assert "data" in result["TeamStarterBenchStats"]
        assert len(result["TeamStarterBenchStats"]["data"]) == 4

    def test_headers_do_not_contain_starters_bench_keys(self, parser):
        """Test that headers filter out 'starters' and 'bench' dict keys."""
        team_headers = parser.get_team_headers()
        player_headers = parser.get_player_headers()

        assert "starters" not in team_headers
        assert "bench" not in team_headers
        assert "starters" not in player_headers
        assert "bench" not in player_headers

    def test_data_filters_out_dict_values(self, parser):
        """Test that data extraction filters out dict values from rows."""
        team_data = parser.get_team_data()
        player_data = parser.get_player_data()

        # Check no nested dicts in data rows
        for row in team_data:
            for value in row:
                assert not isinstance(value, dict), "Team data should not contain dicts"

        for row in player_data:
            for value in row:
                assert not isinstance(value, dict), "Player data should not contain dicts"

    def test_handles_missing_starters_bench_gracefully(self):
        """Test parser handles missing starters/bench data."""
        modified_fixture = BOXSCORETRADITIONALV3_SAMPLE.copy()
        modified_fixture["boxScoreTraditional"]["homeTeam"]["starters"] = None
        modified_fixture["boxScoreTraditional"]["homeTeam"]["bench"] = None

        parser = NBAStatsBoxscoreTraditionalParserV3(modified_fixture)
        data = parser.get_start_bench_data()

        # Should still return 4 rows
        assert len(data) == 4
        # Home starters row should have "Starters" label but no stats
        assert data[0][-1] == "Starters"
        # Home bench row should have "Bench" label
        assert data[1][-1] == "Bench"

    def test_parser_with_full_response(self):
        """Test parser handles complete API response."""
        import json
        from pathlib import Path

        response_path = Path(__file__).parents[4] / "docs" / "nba_api" / "stats" / "endpoints" / "responses" / "boxscoretraditionalv3.json"

        if not response_path.exists():
            pytest.skip(f"Full response file not found: {response_path}")

        with open(response_path) as f:
            full_data = json.load(f)

        parser = NBAStatsBoxscoreTraditionalParserV3(full_data)
        result = parser.get_data_sets()

        # Verify all datasets are present
        assert "TeamStats" in result
        assert "PlayerStats" in result
        assert "TeamStarterBenchStats" in result

        # Verify data structure
        assert len(result["TeamStats"]["data"]) == 2  # 2 teams
        assert len(result["PlayerStats"]["data"]) > 0  # Should have players
        assert len(result["TeamStarterBenchStats"]["data"]) == 4  # 2 teams * 2 (starters + bench)

        # Verify headers match expected_data from endpoint
        from nba_api.stats.endpoints.boxscoretraditionalv3 import BoxScoreTraditionalV3
        expected = BoxScoreTraditionalV3.expected_data

        assert list(result["TeamStats"]["headers"]) == expected["TeamStats"]
        assert list(result["PlayerStats"]["headers"]) == expected["PlayerStats"]
        assert list(result["TeamStarterBenchStats"]["headers"]) == expected["TeamStarterBenchStats"]
