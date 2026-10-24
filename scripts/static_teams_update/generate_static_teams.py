"""Refresh the static ``teams`` / ``wnba_teams`` data.

Existing rows are the base, so hand-curated fields (state, city, abbreviation)
are kept. The NBA API is used to:

* refresh each team's championship years,
* add teams the API reports as active that are not in the data yet, and
* warn about drift in abbreviation / nickname / city / year founded, or about
  teams that are no longer active, so those can be reviewed by hand.

The ``teams`` and ``wnba_teams`` blocks are rewritten in both
``scripts/static_players_update/template.py`` (so the players generator does not
revert them) and ``src/nba_api/stats/library/data.py``.

Usage (from the repo root)::

    uv run python scripts/static_teams_update/generate_static_teams.py --check
    uv run python scripts/static_teams_update/generate_static_teams.py
"""

import argparse
import logging
import re
import sys
import time
from pathlib import Path

from nba_api.stats.endpoints.commonteamyears import CommonTeamYears
from nba_api.stats.endpoints.teamdetails import TeamDetails
from nba_api.stats.library.data import teams, wnba_teams
from nba_api.stats.library.parameters import LeagueID

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
log = logging.getLogger(__name__)

REPO_ROOT = Path(__file__).resolve().parents[2]
TEMPLATE_PATH = REPO_ROOT / "scripts" / "static_players_update" / "template.py"
DATA_PATH = REPO_ROOT / "src" / "nba_api" / "stats" / "library" / "data.py"

REQUEST_TIMEOUT = 30
REQUEST_DELAY_SECONDS = 0.6
LINE_LENGTH = 88

(
    ID,
    ABBREVIATION,
    NICKNAME,
    YEAR_FOUNDED,
    CITY,
    FULL_NAME,
    STATE,
    CHAMPIONSHIP_YEARS,
) = range(8)

# The API has no state field, so states for new teams are listed here.
# {team_id: state}
team_states = {
    1611661327: "Oregon",  # Portland Fire
    1611661332: "Ontario",  # Toronto Tempo
}

LEAGUES = {
    "teams": (LeagueID.nba, teams),
    "wnba_teams": (LeagueID.wnba, wnba_teams),
}


def fetch_active_team_ids(league_id):
    """Return {team_id: abbreviation} for teams active in the latest season."""
    result_set = CommonTeamYears(league_id=league_id, timeout=REQUEST_TIMEOUT)
    result_set = result_set.get_dict()["resultSets"][0]
    headers = result_set["headers"]
    rows = [dict(zip(headers, row, strict=True)) for row in result_set["rowSet"]]
    latest = max(int(row["MAX_YEAR"]) for row in rows if row["MAX_YEAR"])
    return {
        row["TEAM_ID"]: row["ABBREVIATION"]
        for row in rows
        if row["MAX_YEAR"] and int(row["MAX_YEAR"]) == latest
    }


def fetch_team_details(team_id):
    """Return the background fields and championship years for one team."""
    result_sets = TeamDetails(team_id=team_id, timeout=REQUEST_TIMEOUT).get_dict()
    by_name = {s["name"]: s for s in result_sets["resultSets"]}

    background = by_name["TeamBackground"]
    background = dict(zip(background["headers"], background["rowSet"][0], strict=True))

    awards = by_name["TeamAwardsChampionships"]
    year_index = awards["headers"].index("YEARAWARDED")
    championships = sorted(int(row[year_index]) for row in awards["rowSet"])

    return {
        "abbreviation": background["ABBREVIATION"],
        "nickname": background["NICKNAME"],
        "year_founded": int(background["YEARFOUNDED"]),
        "city": background["CITY"],
        "championship_years": championships,
    }


def build_new_team_row(team_id, details):
    state = team_states.get(team_id)
    if state is None:
        log.warning(
            f"No state set for new team {team_id}; add it to team_states in this script"
        )
        state = ""
    return [
        team_id,
        details["abbreviation"],
        details["nickname"],
        details["year_founded"],
        details["city"],
        f"{details['city']} {details['nickname']}",
        state,
        details["championship_years"],
    ]


def merge_team_rows(local_rows, active_ids, get_details):
    """Merge API data into the local rows and return (rows, changes, warnings)."""
    rows = {row[ID]: list(row) for row in local_rows}
    changes = []
    warnings = []

    for team_id, row in rows.items():
        name = row[FULL_NAME]
        if team_id not in active_ids:
            warnings.append(f"{name} ({team_id}) is no longer active in the API")
            continue

        details = get_details(team_id)

        if details["championship_years"] != row[CHAMPIONSHIP_YEARS]:
            changes.append(
                f"{name}: championships {row[CHAMPIONSHIP_YEARS][-3:]}"
                f" -> {details['championship_years'][-3:]}"
            )
            row[CHAMPIONSHIP_YEARS] = details["championship_years"]

        for label, index, key in (
            ("abbreviation", ABBREVIATION, "abbreviation"),
            ("nickname", NICKNAME, "nickname"),
            ("city", CITY, "city"),
            ("year founded", YEAR_FOUNDED, "year_founded"),
        ):
            if details[key] != row[index]:
                warnings.append(
                    f"{name}: {label} is {row[index]!r} locally but"
                    f" {details[key]!r} in the API (not changed)"
                )

    for team_id in active_ids:
        if team_id not in rows:
            new_row = build_new_team_row(team_id, get_details(team_id))
            rows[team_id] = new_row
            changes.append(f"New team: {new_row[FULL_NAME]} ({team_id})")

    return [rows[team_id] for team_id in sorted(rows)], changes, warnings


def _quote(value, quote='"'):
    return f"{quote}{value}{quote}"


def _format_years(years, indent):
    one_line = "[" + ", ".join(str(y) for y in years) + "]"
    if len(" " * indent + one_line + ",") <= LINE_LENGTH:
        return one_line
    inner = "".join(f"\n{' ' * (indent + 4)}{y}," for y in years)
    return f"[{inner}\n{' ' * indent}]"


def format_row_ruff(row):
    """Format a row the way ``ruff format`` lays out data.py."""
    one_line = (
        f"    [{row[ID]}, {_quote(row[ABBREVIATION])}, {_quote(row[NICKNAME])},"
        f" {row[YEAR_FOUNDED]}, {_quote(row[CITY])}, {_quote(row[FULL_NAME])},"
        f" {_quote(row[STATE])}, {_format_years(row[CHAMPIONSHIP_YEARS], 4)}],"
    )
    if len(one_line) <= LINE_LENGTH and "\n" not in one_line:
        return one_line
    lines = [
        f"        {row[ID]},",
        f"        {_quote(row[ABBREVIATION])},",
        f"        {_quote(row[NICKNAME])},",
        f"        {row[YEAR_FOUNDED]},",
        f"        {_quote(row[CITY])},",
        f"        {_quote(row[FULL_NAME])},",
        f"        {_quote(row[STATE])},",
        f"        {_format_years(row[CHAMPIONSHIP_YEARS], 8)},",
    ]
    return "    [\n" + "\n".join(lines) + "\n    ],"


def format_row_template(row, quote='"'):
    """Format a row as a single line, as written in the players template."""
    years = "[" + ", ".join(str(y) for y in row[CHAMPIONSHIP_YEARS]) + "]"
    return (
        f"    [{row[ID]}, {_quote(row[ABBREVIATION], quote)},"
        f" {_quote(row[NICKNAME], quote)}, {row[YEAR_FOUNDED]},"
        f" {_quote(row[CITY], quote)}, {_quote(row[FULL_NAME], quote)},"
        f" {_quote(row[STATE], quote)}, {years}],"
    )


def template_row_formatter(text, variable_name):
    """Match the quote style the template already uses for this block."""
    single = re.search(rf"^{variable_name} = \[\n    \[\d+, '", text, re.MULTILINE)
    quote = "'" if single else '"'
    return lambda row: format_row_template(row, quote)


def replace_block(text, variable_name, rows, format_row):
    """Replace the ``variable_name = [ ... ]`` block at the start of a line.

    Whether the last row keeps a trailing comma follows the existing block.
    """
    pattern = re.compile(rf"^{variable_name} = \[\n.*?^\]\n", re.MULTILINE | re.DOTALL)
    matches = pattern.findall(text)
    if len(matches) != 1:
        raise ValueError(f"Expected exactly one '{variable_name} = [' block")
    trailing_comma = matches[0].endswith(",\n]\n")
    body = "\n".join(format_row(row) for row in rows)
    if not trailing_comma:
        body = body.removesuffix(",")
    return pattern.sub(lambda _: f"{variable_name} = [\n{body}\n]\n", text)


def update_file(path, merged, get_row_formatter, write):
    text = path.read_text(encoding="utf-8")
    updated = text
    for variable_name, rows in merged.items():
        row_formatter = get_row_formatter(text, variable_name)
        updated = replace_block(updated, variable_name, rows, row_formatter)
    if updated == text:
        log.info(f"{path.relative_to(REPO_ROOT)} is up to date")
        return False
    if write:
        path.write_text(updated, encoding="utf-8")
        log.info(f"Updated {path.relative_to(REPO_ROOT)}")
    else:
        log.info(f"{path.relative_to(REPO_ROOT)} would change")
    return True


def generate_static_teams(check=False):
    merged = {}
    all_changes = []
    all_warnings = []

    for variable_name, (league_id, local_rows) in LEAGUES.items():
        log.info(f"Fetching {variable_name} (league_id={league_id})")
        active_ids = fetch_active_team_ids(league_id)

        def get_details(team_id):
            time.sleep(REQUEST_DELAY_SECONDS)
            return fetch_team_details(team_id)

        rows, changes, warnings = merge_team_rows(local_rows, active_ids, get_details)
        merged[variable_name] = rows
        all_changes += [f"[{variable_name}] {c}" for c in changes]
        all_warnings += [f"[{variable_name}] {w}" for w in warnings]

    for change in all_changes:
        log.info(change)
    for warning in all_warnings:
        log.warning(warning)

    write = not check
    template_changed = update_file(TEMPLATE_PATH, merged, template_row_formatter, write)
    data_changed = update_file(DATA_PATH, merged, lambda *_: format_row_ruff, write)
    return template_changed or data_changed


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--check",
        action="store_true",
        help="report what would change without writing; exit 1 if out of date",
    )
    args = parser.parse_args(argv)

    changed = generate_static_teams(check=args.check)
    if args.check and changed:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
