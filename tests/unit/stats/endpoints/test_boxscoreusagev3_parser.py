"""Unit tests for BoxScoreUsageV3 parser."""

import pytest

from nba_api.stats.endpoints._parsers.boxscoreusagev3 import (
    NBAStatsBoxscoreUsageV3Parser,
)

from .data.boxscoreusagev3 import BOXSCOREUSAGEV3_SAMPLE


@pytest.fixture
def parser():
    """Create parser instance with minimal test fixture."""
    return NBAStatsBoxscoreUsageV3Parser(BOXSCOREUSAGEV3_SAMPLE)


@pytest.fixture
def json_fixture():
    """Return the BoxScoreUsageV3 sample fixture."""
    return BOXSCOREUSAGEV3_SAMPLE


class TestNBAStatsBoxscoreUsageV3Parser:
    """Test the BoxScoreUsageV3 parser."""

    def test_parser_initialization(self, parser):
        """Test that parser initializes correctly."""
        assert parser.nba_dict == BOXSCOREUSAGEV3_SAMPLE
        assert parser.boxscore == BOXSCOREUSAGEV3_SAMPLE["boxScoreUsage"]

    def test_get_team_headers(self, parser):
        """Test team headers are explicit and comprehensive."""
        headers = parser.get_team_headers()

        assert isinstance(headers, tuple)
        # Core fields
        assert "gameId" in headers
        assert "teamId" in headers
        assert "teamCity" in headers
        assert "teamName" in headers
        assert "teamTricode" in headers
        assert "teamSlug" in headers
        # Usage stats
        assert "minutes" in headers
        assert "usagePercentage" in headers
        assert "percentageFieldGoalsMade" in headers
        assert "percentageFieldGoalsAttempted" in headers
        assert "percentageThreePointersMade" in headers
        assert "percentageThreePointersAttempted" in headers
        assert "percentageFreeThrowsMade" in headers
        assert "percentageFreeThrowsAttempted" in headers
        assert "percentageReboundsOffensive" in headers
        assert "percentageReboundsDefensive" in headers
        assert "percentageReboundsTotal" in headers
        assert "percentageAssists" in headers
        assert "percentageTurnovers" in headers
        assert "percentageSteals" in headers
        assert "percentageBlocks" in headers
        assert "percentageBlocksAllowed" in headers
        assert "percentagePersonalFouls" in headers
        assert "percentagePersonalFoulsDrawn" in headers
        assert "percentagePoints" in headers

    def test_get_player_headers(self, parser):
        """Test player headers are explicit and comprehensive."""
        headers = parser.get_player_headers()

        assert isinstance(headers, tuple)
        # Core fields
        assert "gameId" in headers
        assert "teamId" in headers
        assert "personId" in headers
        assert "firstName" in headers
        assert "familyName" in headers
        assert "position" in headers
        # Usage stats
        assert "usagePercentage" in headers
        assert "percentageFieldGoalsMade" in headers
        assert "percentageFieldGoalsAttempted" in headers
        assert "percentageThreePointersMade" in headers
        assert "percentageThreePointersAttempted" in headers
        assert "percentageFreeThrowsMade" in headers
        assert "percentageFreeThrowsAttempted" in headers
        assert "percentageReboundsOffensive" in headers
        assert "percentageReboundsDefensive" in headers
        assert "percentageReboundsTotal" in headers
        assert "percentageAssists" in headers
        assert "percentageTurnovers" in headers
        assert "percentageSteals" in headers
        assert "percentageBlocks" in headers
        assert "percentageBlocksAllowed" in headers
        assert "percentagePersonalFouls" in headers
        assert "percentagePersonalFoulsDrawn" in headers
        assert "percentagePoints" in headers

    def test_get_team_data(self, parser):
        """Test team data extraction."""
        data = parser.get_team_data()

        assert isinstance(data, list)
        assert len(data) == 2  # Home and away teams

        # Check home team (first row)
        home_row = data[0]
        assert home_row[0] == "0021700807"  # gameId
        assert home_row[1] == 1610612739  # teamId
        assert home_row[2] == "Cleveland"  # teamCity
        assert home_row[3] == "Cavaliers"  # teamName
        assert home_row[4] == "CLE"  # teamTricode
        assert home_row[5] == "cavaliers"  # teamSlug
        assert home_row[6] == "265:00"  # minutes
        assert home_row[7] == 1.0  # usagePercentage

        # Check away team (second row)
        away_row = data[1]
        assert away_row[0] == "0021700807"  # gameId
        assert away_row[1] == 1610612750  # teamId
        assert away_row[2] == "Minnesota"  # teamCity
        assert away_row[3] == "Timberwolves"  # teamName
        assert away_row[4] == "MIN"  # teamTricode
        assert away_row[5] == "timberwolves"  # teamSlug

    def test_get_player_data(self, parser):
        """Test player data extraction."""
        data = parser.get_player_data()

        assert isinstance(data, list)
        assert len(data) == 2  # One player per team in fixture

        # Check first player (away team listed first)
        player_row = data[0]
        assert player_row[0] == "0021700807"  # gameId
        # Team info
        assert player_row[1] == 1610612750  # teamId (away team)
        assert player_row[2] == "Minnesota"  # teamCity
        # Player info
        assert player_row[6] == 203952  # personId
        assert player_row[7] == "Andrew"  # firstName
        assert player_row[8] == "Wiggins"  # familyName
        assert player_row[9] == "A. Wiggins"  # nameI
        assert player_row[10] == "andrew-wiggins"  # playerSlug
        assert player_row[11] == "F"  # position
        # Usage stats
        assert player_row[14] == "39:51"  # minutes
        assert player_row[15] == 0.19  # usagePercentage
        assert player_row[16] == 0.167  # percentageFieldGoalsMade

        # Check second player (home team)
        home_player_row = data[1]
        assert home_player_row[0] == "0021700807"  # gameId
        assert home_player_row[1] == 1610612739  # teamId (home team)
        assert home_player_row[6] == 2544  # personId
        assert home_player_row[7] == "LeBron"  # firstName
        assert home_player_row[8] == "James"  # familyName

    def test_get_data_sets(self, parser):
        """Test complete data extraction."""
        results = parser.get_data_sets()

        assert "TeamStats" in results
        assert "PlayerStats" in results

        # Team stats
        assert "headers" in results["TeamStats"]
        assert "data" in results["TeamStats"]
        assert len(results["TeamStats"]["data"]) == 2

        # Player stats
        assert "headers" in results["PlayerStats"]
        assert "data" in results["PlayerStats"]
        assert len(results["PlayerStats"]["data"]) == 2

    def test_team_stats_row_structure(self, parser):
        """Test that team stats rows have correct structure."""
        results = parser.get_data_sets()
        team_data = results["TeamStats"]["data"]
        team_headers = results["TeamStats"]["headers"]

        # Verify row length matches header count
        assert len(team_data[0]) == len(team_headers)
        assert len(team_data[1]) == len(team_headers)

    def test_player_stats_row_structure(self, parser):
        """Test that player stats rows have correct structure."""
        results = parser.get_data_sets()
        player_data = results["PlayerStats"]["data"]
        player_headers = results["PlayerStats"]["headers"]

        # Verify row length matches header count
        for row in player_data:
            assert len(row) == len(player_headers)

    def test_handles_missing_fields(self):
        """Test parser handles missing optional fields gracefully."""
        incomplete_data = {
            "boxScoreUsage": {
                "gameId": "123",
                "homeTeam": {
                    "teamId": 1,
                    "teamCity": "Test",
                    "teamName": "Team",
                    "teamTricode": "TST",
                    "teamSlug": "test",
                    "players": [],
                    "statistics": {},
                },
                "awayTeam": {
                    "teamId": 2,
                    "teamCity": "Away",
                    "teamName": "Team2",
                    "teamTricode": "AW",
                    "teamSlug": "away",
                    "players": [],
                    "statistics": {},
                },
            }
        }

        parser = NBAStatsBoxscoreUsageV3Parser(incomplete_data)
        data = parser.get_team_data()

        # Should return data with None for missing fields
        assert len(data) == 2
        assert data[0][0] == "123"  # gameId present
        # Missing statistics should be None, not cause errors

    def test_parser_with_full_response(self, json_fixture):
        """Test parser handles complete API response."""
        parser = NBAStatsBoxscoreUsageV3Parser(json_fixture)
        result = parser.get_data_sets()

        assert "TeamStats" in result
        assert "PlayerStats" in result

        # Should have data for both teams
        assert len(result["TeamStats"]["data"]) == 2

        # Should have data for all players
        player_count = len(result["PlayerStats"]["data"])
        assert player_count > 0  # At least some players

    def test_usage_stats_fields_extraction(self, parser):
        """Test that all usage statistics fields are extracted correctly."""
        results = parser.get_data_sets()
        player_data = results["PlayerStats"]["data"]

        # Get the second player (LeBron James from home team)
        lebron_row = player_data[1]

        # Usage stats start after gameId, team metadata, and player metadata
        # gameId(1) + team_metadata(5) + player_metadata(8) = 14, then usage stats start
        usage_stats_start = 14

        # Verify key usage stats
        assert lebron_row[usage_stats_start] == "48:19"  # minutes
        assert lebron_row[usage_stats_start + 1] == 0.272  # usagePercentage
        assert lebron_row[usage_stats_start + 2] == 0.333  # percentageFieldGoalsMade
        assert (
            lebron_row[usage_stats_start + 18] == 0.287
        )  # percentagePoints (index 32)

    def test_team_stats_aggregates(self, parser):
        """Test team statistics totals to 1.0 for percentage fields."""
        results = parser.get_data_sets()
        team_data = results["TeamStats"]["data"]

        # Team stats should have aggregated to 1.0 for usage percentage
        # and percentage fields when all players are included
        home_team = team_data[0]
        away_team = team_data[1]

        # gameId(1) + team_metadata(5) + minutes(1) = 7, then usagePercentage
        assert home_team[7] == 1.0  # Team usagePercentage should be 1.0
        assert away_team[7] == 1.0  # Team usagePercentage should be 1.0

    def test_parser_initialization_with_missing_boxscore(self):
        """Test parser handles missing boxScoreUsage key."""
        incomplete_data = {"meta": {}}

        parser = NBAStatsBoxscoreUsageV3Parser(incomplete_data)
        assert parser.boxscore == {}

        # Should not raise error, but will return rows with None values
        results = parser.get_data_sets()
        # Parser will iterate over empty teams but still create rows with None values
        assert "TeamStats" in results
        assert "PlayerStats" in results

    def test_header_order_consistency(self, parser):
        """Test that headers maintain consistent order."""
        team_headers = parser.get_team_headers()
        player_headers = parser.get_player_headers()

        # First header should always be gameId
        assert team_headers[0] == "gameId"
        assert player_headers[0] == "gameId"

        # Team headers should be subset of player headers
        # Player headers = team_headers (without per-player fields) + player_metadata + same stats
        assert all(
            h in player_headers for h in team_headers[:-19]
        )  # All but stats fields
