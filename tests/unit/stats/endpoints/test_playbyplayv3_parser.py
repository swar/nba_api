"""Unit tests for PlayByPlayV3 parser."""

import pytest
from nba_api.stats.endpoints._parsers.playbyplayv3 import (
    NBAStatsPlayByPlayParserV3
)
from .data.playbyplayv3 import (
    PLAYBYPLAYV3_SAMPLE,
    PLAYBYPLAYV3_MINIMAL,
    PLAYBYPLAYV3_EMPTY
)


@pytest.fixture
def parser():
    """Create parser with sample data."""
    return NBAStatsPlayByPlayParserV3(PLAYBYPLAYV3_SAMPLE)


@pytest.fixture
def parser_minimal():
    """Create parser with minimal data (missing meta)."""
    return NBAStatsPlayByPlayParserV3(PLAYBYPLAYV3_MINIMAL)


@pytest.fixture
def parser_empty():
    """Create parser with empty actions."""
    return NBAStatsPlayByPlayParserV3(PLAYBYPLAYV3_EMPTY)


class TestNBAStatsPlayByPlayParserV3:
    """Test the PlayByPlayV3 parser."""

    def test_parser_initialization(self, parser):
        """Test parser initializes with data."""
        assert parser.nba_dict is not None
        assert "game" in parser.nba_dict

    def test_get_playbyplay_headers(self, parser):
        """Test PlayByPlay headers are correct and explicit."""
        headers = parser.get_playbyplay_headers()

        # Should be a tuple (immutable)
        assert isinstance(headers, tuple)
        
        # Should have gameId first
        assert headers[0] == "gameId"
        
        # Should contain all expected action fields
        expected_fields = [
            "gameId", "actionNumber", "clock", "period", "teamId",
            "teamTricode", "personId", "playerName", "playerNameI",
            "xLegacy", "yLegacy", "shotDistance", "shotResult",
            "isFieldGoal", "scoreHome", "scoreAway", "pointsTotal",
            "location", "description", "actionType", "subType",
            "videoAvailable", "shotValue", "actionId"
        ]
        
        for field in expected_fields:
            assert field in headers, f"Missing expected field: {field}"

    def test_get_playbyplay_data(self, parser):
        """Test PlayByPlay data extraction."""
        data = parser.get_playbyplay_data()

        # Should return a list of rows
        assert isinstance(data, list)
        
        # Should have 2 actions from sample data
        assert len(data) == 2
        
        # First row should start with gameId
        assert data[0][0] == "0022400001"
        
        # Second action should be action number 2
        assert data[1][1] == 2  # actionNumber field

    def test_get_videoavailable_headers(self, parser):
        """Test AvailableVideo headers."""
        headers = parser.get_videoavailable_headers()
        
        # Should return list with single header
        assert isinstance(headers, list)
        assert len(headers) == 1
        assert headers[0] == "videoAvailable"

    def test_get_videoavailable_data(self, parser):
        """Test AvailableVideo data extraction."""
        data = parser.get_videoavailable_data()

        # Should return nested list with single value
        assert isinstance(data, list)
        assert len(data) == 1
        assert len(data[0]) == 1
        assert data[0][0] == 1  # videoAvailable from sample

    def test_get_data_sets(self, parser):
        """Test get_data_sets returns all datasets."""
        result = parser.get_data_sets()

        # Should have both datasets
        assert "PlayByPlay" in result
        assert "AvailableVideo" in result
        
        # Each dataset should have headers and data
        for dataset_name in ["PlayByPlay", "AvailableVideo"]:
            assert "headers" in result[dataset_name]
            assert "data" in result[dataset_name]

    def test_handles_missing_meta(self, parser_minimal):
        """Test parser handles missing meta field gracefully."""
        # Should not crash even without meta field
        data_sets = parser_minimal.get_data_sets()
        
        assert "PlayByPlay" in data_sets
        assert len(data_sets["PlayByPlay"]["data"]) == 1

    def test_handles_empty_actions(self, parser_empty):
        """Test parser handles empty actions list."""
        data_sets = parser_empty.get_data_sets()
        
        # Should still return datasets
        assert "PlayByPlay" in data_sets
        assert "AvailableVideo" in data_sets
        
        # PlayByPlay should be empty
        assert len(data_sets["PlayByPlay"]["data"]) == 0
        
        # AvailableVideo should still have value
        assert len(data_sets["AvailableVideo"]["data"]) == 1

    def test_parser_uses_explicit_field_access(self):
        """Test that parser uses explicit field names, not dynamic extraction."""
        # This test verifies the parser doesn't use fragile patterns
        # We test with reordered keys to ensure it's not key-order dependent
        
        reordered_data = {
            "game": {  # Intentionally first (not second)
                "gameId": "test123",
                "videoAvailable": 1,
                "actions": [{
                    "actionNumber": 1,
                    "clock": "PT12M00.00S",
                    "period": 1,
                    "teamId": 123,
                    "teamTricode": "TST",
                    "personId": 456,
                    "playerName": "Test Player",
                    "playerNameI": "T. Player",
                    "xLegacy": 0,
                    "yLegacy": 0,
                    "shotDistance": 0,
                    "shotResult": None,
                    "isFieldGoal": 0,
                    "scoreHome": "0",
                    "scoreAway": "0",
                    "pointsTotal": 0,
                    "location": "TST",
                    "description": "Test",
                    "actionType": "test",
                    "subType": "test",
                    "videoAvailable": 1,
                    "shotValue": None,
                    "actionId": 1
                }]
            },
            "meta": {"version": 1}  # Intentionally second
        }
        
        parser = NBAStatsPlayByPlayParserV3(reordered_data)
        data_sets = parser.get_data_sets()
        
        # Should work regardless of key order
        assert data_sets["PlayByPlay"]["data"][0][0] == "test123"

    def test_data_types_preserved(self, parser):
        """Test that data types are preserved correctly."""
        data = parser.get_playbyplay_data()
        
        first_action = data[0]
        second_action = data[1]
        
        # Check types for first action (jump ball - no shot)
        assert isinstance(first_action[1], int)  # actionNumber
        assert isinstance(first_action[2], str)  # clock
        assert first_action[12] is None  # shotResult (None for non-shots)
        
        # Check types for second action (made shot)
        assert isinstance(second_action[1], int)  # actionNumber
        assert second_action[12] == "Made"  # shotResult
        assert second_action[22] == 3  # shotValue

    def test_defensive_against_missing_fields(self):
        """Test parser handles missing optional fields without crashing."""
        incomplete_data = {
            "game": {
                "gameId": "partial123",
                "actions": [
                    {
                        "actionNumber": 1,
                        "clock": "PT12M00.00S",
                        "period": 1
                        # Missing many optional fields
                    }
                ]
            }
        }
        
        parser = NBAStatsPlayByPlayParserV3(incomplete_data)
        
        # Should not crash - defensive .get() should handle missing fields
        # Note: Current implementation may crash - this test will fail
        # until we rewrite with defensive pattern
        try:
            data_sets = parser.get_data_sets()
            # If it doesn't crash, verify it returns something
            assert "PlayByPlay" in data_sets
        except (KeyError, IndexError) as e:
            # This is expected with current fragile implementation
            pytest.fail(f"Parser crashed on missing fields: {e}")
