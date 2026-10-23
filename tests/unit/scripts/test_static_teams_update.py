import sys
from pathlib import Path

import pytest

from nba_api.stats.library.data import teams, wnba_teams

SCRIPT_DIR = Path(__file__).resolve().parents[3] / "scripts" / "static_teams_update"
sys.path.insert(0, str(SCRIPT_DIR))

import generate_static_teams as gen  # noqa: E402

ATL = [1610612737, "ATL", "Hawks", 1949, "Atlanta", "Atlanta Hawks", "Georgia", [1958]]


def details(**overrides):
    base = {
        "abbreviation": "ATL",
        "nickname": "Hawks",
        "year_founded": 1949,
        "city": "Atlanta",
        "championship_years": [1958],
    }
    return {**base, **overrides}


class TestMergeTeamRows:
    def test_no_changes(self):
        rows, changes, warnings = gen.merge_team_rows(
            [ATL], {ATL[0]: "ATL"}, lambda _: details()
        )
        assert rows == [ATL]
        assert changes == []
        assert warnings == []

    def test_updates_championships(self):
        rows, changes, _ = gen.merge_team_rows(
            [ATL],
            {ATL[0]: "ATL"},
            lambda _: details(championship_years=[1958, 2026]),
        )
        assert rows[0][gen.CHAMPIONSHIP_YEARS] == [1958, 2026]
        assert len(changes) == 1

    def test_does_not_mutate_input_rows(self):
        gen.merge_team_rows(
            [ATL], {ATL[0]: "ATL"}, lambda _: details(championship_years=[1])
        )
        assert ATL[gen.CHAMPIONSHIP_YEARS] == [1958]

    def test_name_drift_warns_but_keeps_local_values(self):
        rows, changes, warnings = gen.merge_team_rows(
            [ATL], {ATL[0]: "ATL"}, lambda _: details(abbreviation="ATX", city="X")
        )
        assert rows == [ATL]
        assert changes == []
        assert len(warnings) == 2

    def test_inactive_team_is_kept_with_warning(self):
        rows, _, warnings = gen.merge_team_rows([ATL], {}, lambda _: details())
        assert rows == [ATL]
        assert "no longer active" in warnings[0]

    def test_new_team_is_added_in_id_order(self, monkeypatch):
        monkeypatch.setitem(gen.team_states, 5, "Ontario")
        new = details(abbreviation="TOR", nickname="Tempo", city="Toronto")
        rows, changes, _ = gen.merge_team_rows(
            [ATL],
            {ATL[0]: "ATL", 5: "TOR"},
            lambda team_id: details() if team_id == ATL[0] else new,
        )
        assert [r[gen.ID] for r in rows] == [5, ATL[0]]
        assert rows[0][gen.FULL_NAME] == "Toronto Tempo"
        assert rows[0][gen.STATE] == "Ontario"
        assert changes == ["New team: Toronto Tempo (5)"]

    def test_new_team_without_state_gets_blank_state(self):
        row = gen.build_new_team_row(999, details())
        assert row[gen.STATE] == ""


class TestFormatting:
    def test_short_row_stays_on_one_line_in_ruff_style(self):
        row = [1, "A", "B", 1950, "C", "D", "E", [1951]]
        assert gen.format_row_ruff(row) == (
            '    [1, "A", "B", 1950, "C", "D", "E", [1951]],'
        )

    def test_long_row_is_exploded_in_ruff_style(self):
        row = [*ATL[:7], list(range(1950, 1970))]
        formatted = gen.format_row_ruff(row)
        assert formatted.startswith("    [\n        1610612737,")
        assert all(len(line) <= gen.LINE_LENGTH for line in formatted.splitlines())

    def test_template_row_respects_quote_style(self):
        assert "'ATL'" in gen.format_row_template(ATL, quote="'")
        assert '"ATL"' in gen.format_row_template(ATL)


class TestReplaceBlock:
    @pytest.mark.parametrize("trailing_comma", [True, False])
    def test_preserves_trailing_comma_style(self, trailing_comma):
        end = "," if trailing_comma else ""
        text = f"before\nteams = [\n    [1],\n    [2]{end}\n]\nafter\n"
        out = gen.replace_block(text, "teams", [ATL], lambda row: f"    [{row[0]}],")
        expected_row = "    [1610612737]," if trailing_comma else "    [1610612737]"
        assert out == f"before\nteams = [\n{expected_row}\n]\nafter\n"

    def test_requires_exactly_one_block(self):
        with pytest.raises(ValueError):
            gen.replace_block("nothing here\n", "teams", [], str)

    @pytest.mark.parametrize(
        ("path", "get_formatter"),
        [
            (gen.DATA_PATH, lambda *_: gen.format_row_ruff),
            (gen.TEMPLATE_PATH, gen.template_row_formatter),
        ],
    )
    def test_regenerating_current_data_is_a_no_op(self, path, get_formatter):
        """Formatting must reproduce the checked-in files so diffs stay minimal."""
        text = path.read_text(encoding="utf-8")
        updated = text
        for name, rows in (("teams", teams), ("wnba_teams", wnba_teams)):
            updated = gen.replace_block(updated, name, rows, get_formatter(text, name))
        assert updated == text
