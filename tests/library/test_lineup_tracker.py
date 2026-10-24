import pytest

from nba_api.stats.library.lineup_tracker import LineupTracker


@pytest.mark.live
class TestLineupTracker:
    TEST_GAME_ID = "0022300001"

    def test_initialization(self):
        tracker = LineupTracker(self.TEST_GAME_ID)
        tracker.fetch_data()
        assert tracker.pbp_data is not None
        assert not tracker.start_lineup.empty

    def test_quarter_transition(self):
        tracker = LineupTracker(self.TEST_GAME_ID)
        tracker.fetch_data()

        # Test 2nd and 3rd quarters
        for q in [2, 3]:
            lineups = tracker.get_starters_for_quarter(q)
            assert len(lineups) == 2, "Should return data for exactly 2 teams"
            for team_id in lineups:
                assert len(lineups[team_id]) == 5, (
                    f"Quarter {q} failed to return 5 players for team {team_id}"
                )

    def test_invalid_game_id(self):
        with pytest.raises(ValueError):
            tracker = LineupTracker("9999999999")
            tracker.fetch_data()

    def test_overtime_support(self):
        ot_game_id = "0022300185"
        tracker = LineupTracker(ot_game_id)
        tracker.fetch_data()

        ot_lineup = tracker.get_starters_for_quarter(5)
        for team_id in ot_lineup:
            assert len(ot_lineup[team_id]) == 5
