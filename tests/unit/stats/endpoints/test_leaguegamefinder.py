"""Unit tests for LeagueGameFinder endpoint."""

import warnings

from nba_api.stats.endpoints import LeagueGameFinder


class TestLeagueGameFinderWarnings:
    """Test warning behavior for LeagueGameFinder."""

    def test_game_id_nullable_emits_warning(self):
        """Test that using game_id_nullable parameter emits a warning."""
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")

            LeagueGameFinder(
                player_or_team_abbreviation="T",
                season_nullable="2023-24",
                game_id_nullable="0022301181",
                get_request=False,
            )

            # Should emit exactly one warning
            assert len(w) == 1
            assert issubclass(w[0].category, UserWarning)
            assert "game_id_nullable" in str(w[0].message)
            assert "Issue #446" in str(w[0].message)
            assert "0022301181" in str(w[0].message)

    def test_no_warning_without_game_id(self):
        """Test that NOT using game_id_nullable does not emit a warning."""
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")

            LeagueGameFinder(
                player_or_team_abbreviation="T",
                season_nullable="2023-24",
                get_request=False,
            )

            # Should not emit any warnings
            assert len(w) == 0

    def test_no_warning_with_empty_game_id(self):
        """Test that empty string for game_id_nullable does not emit a warning."""
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")

            LeagueGameFinder(
                player_or_team_abbreviation="T",
                season_nullable="2023-24",
                game_id_nullable="",
                get_request=False,
            )

            # Should not emit any warnings
            assert len(w) == 0


class TestLeagueGameFinderInitialization:
    """Test LeagueGameFinder initialization."""

    def test_endpoint_initialization_without_request(self):
        """Test endpoint initializes without making HTTP request."""
        endpoint = LeagueGameFinder(
            player_or_team_abbreviation="T",
            season_nullable="2023-24",
            get_request=False,
        )

        assert endpoint.parameters["PlayerOrTeam"] == "T"
        assert endpoint.parameters["Season"] == "2023-24"
        assert endpoint.endpoint == "leaguegamefinder"

    def test_game_id_parameter_mapping(self):
        """Test that game_id_nullable maps to GameID parameter."""
        endpoint = LeagueGameFinder(
            player_or_team_abbreviation="T",
            game_id_nullable="0022301181",
            get_request=False,
        )

        assert endpoint.parameters["GameID"] == "0022301181"
