"""Unit tests for GravityLeaders parser."""

import pytest

from nba_api.stats.endpoints._parsers.gravityleaders import (
    NBAStatsGravityLeadersParser,
)

from .data.gravityleaders import (
    GRAVITYLEADERS_EMPTY,
    GRAVITYLEADERS_INVALID_LEADERS_TYPE,
    GRAVITYLEADERS_MISSING_LEADERS,
    GRAVITYLEADERS_MIXED_VALID_INVALID,
    GRAVITYLEADERS_PARTIAL_FIELDS,
    GRAVITYLEADERS_SAMPLE,
)


@pytest.fixture
def json_fixture():
    """Load the GravityLeaders fixture."""
    return GRAVITYLEADERS_SAMPLE


@pytest.fixture
def parser(json_fixture):
    """Create a parser instance with the JSON fixture."""
    return NBAStatsGravityLeadersParser(json_fixture)


class TestNBAStatsGravityLeadersParser:
    """Test the GravityLeaders parser."""

    def test_parser_initialization(self, parser, json_fixture):
        """Test that parser initializes correctly."""
        assert parser.nba_dict == json_fixture
        assert parser.leaders == json_fixture["leaders"]

    def test_get_leaders_headers_returns_tuple(self, parser):
        """Test get_leaders_headers returns a tuple."""
        headers = parser.get_leaders_headers()

        assert isinstance(headers, tuple)
        assert len(headers) == 27  # All gravity leader fields

    def test_get_leaders_headers_structure(self, parser):
        """Test headers include expected fields."""
        headers = parser.get_leaders_headers()

        # Player identification fields
        assert "PLAYERID" in headers
        assert "FIRSTNAME" in headers
        assert "LASTNAME" in headers

        # Team fields
        assert "TEAMID" in headers
        assert "TEAMABBREVIATION" in headers
        assert "TEAMNAME" in headers
        assert "TEAMCITY" in headers

        # Core gravity fields
        assert "GRAVITYSCORE" in headers
        assert "AVGGRAVITYSCORE" in headers
        assert "FRAMES" in headers

        # On-ball perimeter fields
        assert "ONBALLPERIMETERFRAMES" in headers
        assert "ONBALLPERIMETERGRAVITYSCORE" in headers
        assert "AVGONBALLPERIMETERGRAVITYSCORE" in headers

        # Off-ball perimeter fields
        assert "OFFBALLPERIMETERFRAMES" in headers
        assert "OFFBALLPERIMETERGRAVITYSCORE" in headers
        assert "AVGOFFBALLPERIMETERGRAVITYSCORE" in headers

        # On-ball interior fields
        assert "ONBALLINTERIORFRAMES" in headers
        assert "ONBALLINTERIORGRAVITYSCORE" in headers
        assert "AVGONBALLINTERIORGRAVITYSCORE" in headers

        # Off-ball interior fields
        assert "OFFBALLINTERIORFRAMES" in headers
        assert "OFFBALLINTERIORGRAVITYSCORE" in headers
        assert "AVGOFFBALLINTERIORGRAVITYSCORE" in headers

        # Traditional stats
        assert "GAMESPLAYED" in headers
        assert "MINUTES" in headers
        assert "PTS" in headers
        assert "REB" in headers
        assert "AST" in headers

    def test_get_leaders_data(self, parser, json_fixture):
        """Test leaders data extraction."""
        data = parser.get_leaders_data()

        assert isinstance(data, list)
        assert len(data) == len(json_fixture["leaders"])

        # Each row should be a list
        assert all(isinstance(row, list) for row in data)

    def test_get_leaders_data_values(self, parser):
        """Test that data values match fixture."""
        data = parser.get_leaders_data()

        # First player should be Stephen Curry
        first_row = data[0]
        assert first_row[0] == 201939  # PLAYERID
        assert first_row[1] == "Stephen"  # FIRSTNAME
        assert first_row[2] == "Curry"  # LASTNAME
        assert first_row[3] == 1610612744  # TEAMID (GSW)
        assert first_row[8] == pytest.approx(20.8209629629)  # GRAVITYSCORE

    def test_get_data_sets(self, parser):
        """Test get_data_sets returns correct structure."""
        result = parser.get_data_sets()

        assert "leaders" in result

        # Check leaders structure
        assert "headers" in result["leaders"]
        assert "data" in result["leaders"]
        assert isinstance(result["leaders"]["headers"], tuple)
        assert isinstance(result["leaders"]["data"], list)

    def test_data_row_count_matches_headers(self, parser):
        """Test that each data row has same number of columns as headers."""
        result = parser.get_data_sets()
        headers = result["leaders"]["headers"]
        data = result["leaders"]["data"]

        for i, row in enumerate(data):
            assert len(row) == len(headers), (
                f"Row {i} has {len(row)} columns but headers has {len(headers)}"
            )

    def test_parser_preserves_player_order(self, parser, json_fixture):
        """Test that parser preserves player order from API response."""
        data = parser.get_leaders_data()
        headers = parser.get_leaders_headers()

        # Find PLAYERID index
        player_id_index = headers.index("PLAYERID")

        # Extract player IDs from parsed data
        parsed_player_ids = [row[player_id_index] for row in data]

        # Extract player IDs from fixture
        expected_player_ids = [leader["PLAYERID"] for leader in json_fixture["leaders"]]

        assert parsed_player_ids == expected_player_ids


class TestGravityLeadersParserEdgeCases:
    """Test edge cases and lenient error handling."""

    def test_empty_leaders_list(self):
        """Test parser handles empty leaders list."""
        parser = NBAStatsGravityLeadersParser(GRAVITYLEADERS_EMPTY)

        assert parser.leaders == []
        data = parser.get_leaders_data()
        assert data == []

        result = parser.get_data_sets()
        assert result["leaders"]["data"] == []

    def test_missing_leaders_key(self):
        """Test parser handles missing 'leaders' key gracefully."""
        parser = NBAStatsGravityLeadersParser(GRAVITYLEADERS_MISSING_LEADERS)

        assert parser.leaders == []
        data = parser.get_leaders_data()
        assert data == []

    def test_none_input(self):
        """Test parser handles None input gracefully."""
        parser = NBAStatsGravityLeadersParser(None)

        assert parser.nba_dict == {}
        assert parser.leaders == []
        data = parser.get_leaders_data()
        assert data == []

    def test_invalid_leaders_type(self):
        """Test parser handles non-list leaders value."""
        parser = NBAStatsGravityLeadersParser(GRAVITYLEADERS_INVALID_LEADERS_TYPE)

        assert parser.leaders == []
        data = parser.get_leaders_data()
        assert data == []

    def test_mixed_valid_invalid_entries(self):
        """Test parser skips invalid entries and processes valid ones."""
        parser = NBAStatsGravityLeadersParser(GRAVITYLEADERS_MIXED_VALID_INVALID)

        data = parser.get_leaders_data()

        # Should only have 2 valid entries (the dicts)
        assert len(data) == 2

        # Verify the valid entries were processed
        player_ids = [row[0] for row in data]
        assert 12345 in player_ids
        assert 67890 in player_ids

    def test_partial_fields_returns_none(self):
        """Test parser returns None for missing fields."""
        parser = NBAStatsGravityLeadersParser(GRAVITYLEADERS_PARTIAL_FIELDS)

        data = parser.get_leaders_data()
        assert len(data) == 1

        row = data[0]
        # Present fields should have values
        assert row[0] == 11111  # PLAYERID
        assert row[1] == "Partial"  # FIRSTNAME
        assert row[2] == "Fields"  # LASTNAME

        # Missing fields should be None
        assert row[3] is None  # TEAMID
        assert row[8] is None  # GRAVITYSCORE

    def test_non_dict_input(self):
        """Test parser handles non-dict input."""
        parser = NBAStatsGravityLeadersParser("not_a_dict")

        assert parser.nba_dict == {}
        assert parser.leaders == []

    def test_list_input(self):
        """Test parser handles list input."""
        parser = NBAStatsGravityLeadersParser([1, 2, 3])

        assert parser.nba_dict == {}
        assert parser.leaders == []


class TestGravityLeadersParserRegistration:
    """Test parser registration in the parsers module."""

    def test_parser_importable_from_parsers(self):
        """Test parser can be imported from _parsers package."""
        from nba_api.stats.endpoints._parsers import NBAStatsGravityLeadersParser

        assert NBAStatsGravityLeadersParser is not None

    def test_parser_in_registry(self):
        """Test parser is registered in the parser registry."""
        from nba_api.stats.endpoints._parsers import get_parser_for_endpoint

        parser = get_parser_for_endpoint("gravityleaders", GRAVITYLEADERS_SAMPLE)
        assert isinstance(parser, NBAStatsGravityLeadersParser)

    def test_parser_in_all_exports(self):
        """Test parser is in __all__ exports."""
        from nba_api.stats.endpoints import _parsers

        assert "NBAStatsGravityLeadersParser" in _parsers.__all__
