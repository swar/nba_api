"""Unit tests for ScoreboardV3 parser."""

import pytest

from nba_api.stats.endpoints._parsers.scoreboardv3 import (
    NBAStatsScoreboardV3Parser,
)

from .data.scoreboardv3 import SCOREBOARDV3_SAMPLE


@pytest.fixture
def parser():
    """Create parser instance with minimal test fixture."""
    return NBAStatsScoreboardV3Parser(SCOREBOARDV3_SAMPLE)


@pytest.fixture
def json_fixture():
    """Return the ScoreboardV3 sample fixture."""
    return SCOREBOARDV3_SAMPLE


class TestNBAStatsScoreboardV3Parser:
    """Test the ScoreboardV3 parser."""

    def test_parser_initialization(self, parser):
        """Test that parser initializes correctly."""
        assert parser.nba_dict == SCOREBOARDV3_SAMPLE
        assert parser.scoreboard == SCOREBOARDV3_SAMPLE["scoreboard"]

    def test_get_scoreboard_info_headers(self, parser):
        """Test scoreboard info headers are explicit."""
        headers = parser.get_scoreboard_info_headers()

        assert isinstance(headers, tuple)
        assert "gameDate" in headers
        assert "leagueId" in headers
        assert "leagueName" in headers

    def test_get_scoreboard_info_data(self, parser):
        """Test scoreboard info data extraction."""
        data = parser.get_scoreboard_info_data()

        assert len(data) == 1  # One row
        assert data[0][0] == "2025-11-05"  # gameDate
        assert data[0][1] == "00"  # leagueId
        assert data[0][2] == "National Basketball Association"  # leagueName

    def test_get_game_header_headers(self, parser):
        """Test game header headers are explicit."""
        headers = parser.get_game_header_headers()

        assert isinstance(headers, tuple)
        # Core fields
        assert "gameId" in headers
        assert "gameCode" in headers
        assert "gameStatus" in headers
        assert "gameStatusText" in headers
        assert "period" in headers
        assert "gameClock" in headers
        assert "gameTimeUTC" in headers
        assert "gameEt" in headers
        assert "regulationPeriods" in headers
        assert "seriesGameNumber" in headers
        assert "gameLabel" in headers
        assert "gameSubLabel" in headers
        assert "seriesText" in headers
        assert "ifNecessary" in headers
        assert "seriesConference" in headers
        assert "poRoundDesc" in headers
        assert "gameSubtype" in headers

    def test_get_game_header_data(self, parser):
        """Test game header data extraction."""
        data = parser.get_game_header_data()

        assert len(data) == 1  # One game in fixture
        row = data[0]
        assert row[0] == "0022500171"  # gameId
        assert row[1] == "20251105/PHICLE"  # gameCode
        assert row[2] == 3  # gameStatus
        assert row[3] == "Final"  # gameStatusText

    def test_get_line_score_headers(self, parser):
        """Test line score headers are explicit."""
        headers = parser.get_line_score_headers()

        assert isinstance(headers, tuple)
        assert "gameId" in headers
        assert "teamId" in headers
        assert "teamCity" in headers
        assert "teamName" in headers
        assert "teamTricode" in headers
        assert "teamSlug" in headers
        assert "wins" in headers
        assert "losses" in headers
        assert "score" in headers
        assert "seed" in headers
        assert "inBonus" in headers
        assert "timeoutsRemaining" in headers

    def test_get_line_score_data(self, parser):
        """Test line score data extraction."""
        data = parser.get_line_score_data()

        assert len(data) == 2  # Home and away teams
        # Home team (Cleveland)
        home_row = data[0]
        assert home_row[0] == "0022500171"  # gameId
        assert home_row[1] == 1610612739  # teamId
        assert home_row[2] == "Cleveland"  # teamCity
        assert home_row[3] == "Cavaliers"  # teamName
        assert home_row[4] == "CLE"  # teamTricode
        assert home_row[8] == 114  # score

    def test_get_game_leaders_headers(self, parser):
        """Test game leaders headers are explicit."""
        headers = parser.get_game_leaders_headers()

        assert isinstance(headers, tuple)
        assert "gameId" in headers
        assert "teamId" in headers
        assert "leaderType" in headers  # 'home' or 'away'
        assert "personId" in headers
        assert "name" in headers
        assert "playerSlug" in headers
        assert "jerseyNum" in headers
        assert "position" in headers
        assert "teamTricode" in headers
        assert "points" in headers
        assert "rebounds" in headers
        assert "assists" in headers

    def test_get_game_leaders_data(self, parser):
        """Test game leaders data extraction."""
        data = parser.get_game_leaders_data()

        assert len(data) == 2  # Home and away leaders
        # Home leader (Donovan Mitchell)
        home_leader = data[0]
        assert home_leader[0] == "0022500171"  # gameId
        assert home_leader[2] == "home"  # leaderType
        assert home_leader[3] == 1628378  # personId
        assert home_leader[4] == "Donovan Mitchell"  # name
        assert home_leader[9] == 46  # points

    def test_get_team_leaders_headers(self, parser):
        """Test team leaders headers are explicit."""
        headers = parser.get_team_leaders_headers()

        assert isinstance(headers, tuple)
        assert "gameId" in headers
        assert "teamId" in headers
        assert "leaderType" in headers
        assert "personId" in headers
        assert "name" in headers
        assert "points" in headers
        assert "rebounds" in headers
        assert "assists" in headers
        assert "seasonLeadersFlag" in headers

    def test_get_team_leaders_data(self, parser):
        """Test team leaders data extraction."""
        data = parser.get_team_leaders_data()

        assert len(data) == 2  # Home and away team leaders
        # Home leader (Donovan Mitchell season avg)
        home_leader = data[0]
        assert home_leader[0] == "0022500171"  # gameId
        assert home_leader[2] == "home"  # leaderType
        assert home_leader[3] == 1628378  # personId
        assert home_leader[4] == "Donovan Mitchell"  # name
        assert home_leader[9] == 31.9  # points (season average)

    def test_get_broadcasters_headers(self, parser):
        """Test broadcasters headers are explicit."""
        headers = parser.get_broadcasters_headers()

        assert isinstance(headers, tuple)
        assert "gameId" in headers
        assert "broadcasterType" in headers
        assert "broadcasterId" in headers
        assert "broadcastDisplay" in headers
        assert "broadcasterTeamId" in headers
        assert "broadcasterDescription" in headers

    def test_get_broadcasters_data(self, parser):
        """Test broadcasters data extraction."""
        data = parser.get_broadcasters_data()

        # Should have multiple rows (national + home + away for each type)
        assert len(data) > 0

        # Check for national broadcaster (ESPN)
        national_rows = [row for row in data if row[1] == "nationalTv"]
        assert len(national_rows) == 1
        assert national_rows[0][3] == "ESPN"  # broadcastDisplay

        # Check for home TV broadcaster
        home_tv_rows = [row for row in data if row[1] == "homeTv"]
        assert len(home_tv_rows) == 1
        assert home_tv_rows[0][3] == "FDSNOH/RESN"

    def test_get_data_sets(self, parser):
        """Test that all datasets are returned."""
        data_sets = parser.get_data_sets()

        assert "ScoreboardInfo" in data_sets
        assert "GameHeader" in data_sets
        assert "LineScore" in data_sets
        assert "GameLeaders" in data_sets
        assert "TeamLeaders" in data_sets
        assert "Broadcasters" in data_sets

        # Verify structure
        assert "headers" in data_sets["ScoreboardInfo"]
        assert "data" in data_sets["ScoreboardInfo"]

    def test_handles_missing_fields(self):
        """Test parser handles missing optional fields."""
        incomplete_data = {
            "scoreboard": {
                "gameDate": "2025-11-05",
                "leagueId": "00",
                "leagueName": "NBA",
                "games": []
            }
        }
        parser = NBAStatsScoreboardV3Parser(incomplete_data)

        # Should not crash
        data_sets = parser.get_data_sets()
        assert data_sets["GameHeader"]["data"] == []
        assert data_sets["LineScore"]["data"] == []
        assert data_sets["GameLeaders"]["data"] == []
        assert data_sets["TeamLeaders"]["data"] == []
        assert data_sets["Broadcasters"]["data"] == []
