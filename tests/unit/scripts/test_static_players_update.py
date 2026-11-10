import sys
from pathlib import Path

import pytest

from nba_api.stats.library.data import players, wnba_players

SCRIPT_DIR = Path(__file__).resolve().parents[3] / "scripts" / "static_players_update"
sys.path.insert(0, str(SCRIPT_DIR))

import generate_static_data_file as gen  # noqa: E402


def fake_common_all_players(rows, active_ids):
    class FakeCommonAllPlayers:
        def __init__(self, league_id, season, is_only_current_season=0):
            if is_only_current_season:
                rows_out = [row for row in rows if row[0] in active_ids]
            else:
                rows_out = rows
            self.response = {"resultSets": [{"rowSet": rows_out}]}

        def get_dict(self):
            return self.response

    return FakeCommonAllPlayers


def create_players(monkeypatch, rows, active_ids=(), adjustments=None):
    monkeypatch.setattr(
        gen, "CommonAllPlayers", fake_common_all_players(rows, active_ids)
    )
    return dict(gen.create_players_list(player_adjustments=adjustments or {}))


class TestCreatePlayersList:
    def test_last_comma_first(self, monkeypatch):
        result = create_players(monkeypatch, [[1, "Doncic, Luka", "Luka Doncic"]])
        assert result == {1: ["Doncic", "Luka", "Luka Doncic", False]}

    def test_suffix_after_comma_keeps_first_name(self, monkeypatch):
        rows = [[1643640, "Udeh, Jr., Ernest", "Ernest Udeh, Jr."]]
        result = create_players(monkeypatch, rows)
        assert result[1643640] == ["Udeh, Jr.", "Ernest", "Ernest Udeh, Jr.", False]

    def test_single_name(self, monkeypatch):
        result = create_players(monkeypatch, [[2403, "Nene", "Nene"]])
        assert result[2403] == ["Nene", "", "Nene", False]

    def test_marks_active_players(self, monkeypatch):
        rows = [
            [1, "Doncic, Luka", "Luka Doncic"],
            [2, "Jokic, Nikola", "Nikola Jokic"],
        ]
        result = create_players(monkeypatch, rows, active_ids={2})
        assert result[1][-1] is False
        assert result[2][-1] is True

    def test_adjustment_keeps_active_flag(self, monkeypatch):
        result = create_players(
            monkeypatch,
            [[1642385, "Cui, Cui", "Cui Cui"]],
            active_ids={1642385},
            adjustments={1642385: ["Cui", "Yongxi", "Cui Yongxi"]},
        )
        assert result[1642385] == ["Cui", "Yongxi", "Cui Yongxi", True]


# data.py is generated, so hand fixes there must also be in the adjustments
@pytest.mark.parametrize(
    ("adjustments", "data"),
    [(gen.player_adjustments, players), (gen.wnba_player_adjustments, wnba_players)],
    ids=["nba", "wnba"],
)
def test_data_matches_adjustments(adjustments, data):
    rows = {row[0]: row[1:4] for row in data}
    for player_id, names in adjustments.items():
        assert rows[player_id] == names


# 2403 is Nene, the only real single-name player
@pytest.mark.parametrize(
    ("data", "single_name_ids"),
    [(players, {2403}), (wnba_players, set())],
    ids=["nba", "wnba"],
)
def test_only_single_name_players_lack_first_name(data, single_name_ids):
    assert {row[0] for row in data if not row[2]} == single_name_ids
