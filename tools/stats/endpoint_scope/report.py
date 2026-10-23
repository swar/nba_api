"""Turn endpoint_scope --json output into a markdown report grouped by finding.

    python -m tools.stats.endpoint_scope.report scope.json [--offline offline.json]

``--offline`` adds which endpoints have no VCR cassette (from an ``--offline``
run). The report lists findings by kind -- column drift, new datasets, new
parameters, rejected enum values, parser gaps, coverage, dead endpoints,
interactions -- then what the run cost.
"""

import argparse
import json
from collections import Counter

from tools.stats.endpoint_scope.scope import format_phases

PHASE_ORDER = ("baseline", "drop", "blank", "garbage", "values")


def case_renames(added, removed):
    """Columns that only changed case, e.g. Team_ID -> TEAM_ID."""
    lowered = {c.lower(): c for c in added}
    return [(c, lowered[c.lower()]) for c in removed if c.lower() in lowered]


def column_drift(results):
    """(breaking, additive, renamed_keys) lines, one per endpoint and change."""
    breaking, additive, renamed_keys = {}, {}, []
    for endpoint, r in sorted(results.items()):
        for dataset, change in (r.get("drift") or {}).items():
            if isinstance(change, str):
                if change.startswith("expected_data key"):
                    renamed_keys.append(f"`{endpoint}` `{dataset}`: {change}")
                else:
                    breaking.setdefault((endpoint, change), []).append(dataset)
                continue
            if "new dataset" in change:
                continue
            renames = case_renames(change["added"], change["removed"])
            renamed = {old for old, _ in renames} | {new for _, new in renames}
            removed = [c for c in change["removed"] if c not in renamed]
            added = [c for c in change["added"] if c not in renamed]
            parts = []
            if renames:
                parts.append(
                    "renamed " + ", ".join(f"`{a}` → `{b}`" for a, b in renames)
                )
            if removed:
                parts.append("removed " + ", ".join(f"`{c}`" for c in removed))
            if parts:
                breaking.setdefault((endpoint, "; ".join(parts)), []).append(dataset)
            if added:
                key = (endpoint, "added " + ", ".join(added))
                additive.setdefault(key, []).append(dataset)
    return _collapse(breaking), _collapse(additive), renamed_keys


def _collapse(changes):
    """`endpoint` DatasetA, DatasetB: change -- one line per distinct change."""
    lines = []
    for (endpoint, change), datasets in changes.items():
        names = ", ".join(datasets[:4])
        if len(datasets) > 4:
            names += f" (+{len(datasets) - 4} more)"
        lines.append(f"`{endpoint}` {names}: {change}")
    return lines


def new_datasets(results):
    return [
        f"`{endpoint}` **{dataset}** ({len(change['new dataset'])} cols)"
        for endpoint, r in sorted(results.items())
        for dataset, change in (r.get("drift") or {}).items()
        if isinstance(change, dict) and "new dataset" in change
    ]


def group_by_value(results, key):
    """{frozenset(values): [endpoints]} for list-valued report keys."""
    groups = {}
    for endpoint, r in sorted(results.items()):
        values = r.get(key)
        if values:
            groups.setdefault(tuple(sorted(values)), []).append(endpoint)
    return sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0]))


def rejected_values(results):
    lines = []
    for endpoint, r in sorted(results.items()):
        for parameter, v in (r.get("values") or {}).items():
            if v["library_offers_rejected"]:
                lines.append(
                    f"`{endpoint}` {parameter} ({v['library_class']}):"
                    f" rejects {v['library_offers_rejected']}"
                )
    return lines


def values_tested(results):
    lines = []
    for endpoint, r in sorted(results.items()):
        for parameter, v in (r.get("values") or {}).items():
            fit = ", ".join(v["best_fit_classes"])
            note = ""
            if v["library_class"] and v["library_class"] not in v["best_fit_classes"]:
                note = f" (library uses {v['library_class']})"
            extra = v["accepted_but_missing_from_library"]
            if extra:
                note += f"; also accepts {extra}"
            lines.append(f"`{endpoint}` {parameter}: fits {fit}{note}")
    return lines


def cost_table(results):
    rows, totals = [], Counter()
    for endpoint, r in sorted(results.items()):
        phases = r.get("phases") or {}
        lookups = sum(c["sent"] + c["cached"] for c in phases.values())
        rows.append(
            f"| {endpoint} | {r['status']} | {len(r.get('parameters') or [])} |"
            f" {lookups} | {r.get('requests', 0)} | {r.get('seconds', 0)} |"
            f" {format_phases(phases)} |"
        )
        for name, counts in phases.items():
            totals[name] += counts["sent"] + counts["cached"]
        totals["_sent"] += r.get("requests", 0)
        totals["_seconds"] += r.get("seconds", 0)
    return rows, totals


def phase_totals(totals):
    """Roll "drop:suspect" etc. up to their phase, keeping the sub-split."""
    lines, grand = [], sum(v for k, v in totals.items() if not k.startswith("_"))
    for top in PHASE_ORDER:
        subs = {k: v for k, v in totals.items() if k.split(":")[0] == top}
        if not subs:
            continue
        total = sum(subs.values())
        detail = ", ".join(
            f"{k.partition(':')[2] or 'group'} {v}" for k, v in sorted(subs.items())
        )
        lines.append(f"| {top} | {total} | {100 * total / grand:.0f}% | {detail} |")
    return lines, grand


def render(results, offline=None):
    statuses = Counter(r["status"] for r in results.values())
    out = ["# endpoint_scope run", ""]
    out.append(
        f"{len(results)} endpoints: "
        + ", ".join(f"{n} {s}" for s, n in statuses.most_common())
        + "."
    )

    breaking, additive, renamed_keys = column_drift(results)
    out += ["", "## Column drift vs `expected_data`", ""]
    out += ["### Likely to break users (renamed, removed, or missing)", ""]
    out += [f"- {line}" for line in breaking] or ["- none"]
    out += ["", "### Additive (new columns)", ""]
    out += [f"- {line}" for line in additive] or ["- none"]
    if renamed_keys:
        out += ["", "### `expected_data` keyed differently from the dataset", ""]
        out += [f"- {line}" for line in renamed_keys]

    out += ["", "## New datasets", ""]
    out += [f"- {line}" for line in new_datasets(results)] or ["- none"]

    out += ["", "## Parameters the server accepts that the library does not send", ""]
    for params, endpoints in group_by_value(results, "server_only_parameters"):
        out.append(
            f"- {', '.join(params)}: {len(endpoints)} endpoints ({', '.join(endpoints)})"
        )

    out += ["", "## Library enum values the server rejects", ""]
    out += [f"- {line}" for line in rejected_values(results)] or ["- none found"]
    tested = values_tested(results)
    if tested:
        out += ["", "<details><summary>All value discovery results</summary>", ""]
        out += [f"- {line}" for line in tested]
        out += ["", "</details>"]

    out += ["", "## Fields nested (V3) parsers drop", ""]
    for fields, endpoints in group_by_value(results, "unparsed_fields"):
        out.append(f"- {', '.join(fields)}: {', '.join(endpoints)}")

    out += ["", "## Coverage gaps", ""]
    no_spec = [
        e for e, r in sorted(results.items()) if r.get("note") == "no EndpointSpec"
    ]
    out.append(f"- No `EndpointSpec` ({len(no_spec)}): {', '.join(no_spec) or 'none'}")
    if offline:
        no_cassette = sorted(
            e for e, r in offline.items() if r["status"] == "no-cassette"
        )
        out.append(f"- No cassette ({len(no_cassette)}): {', '.join(no_cassette)}")

    out += ["", "## Baseline failures", ""]
    out += ["| endpoint | HTTP | spec note | body |", "|---|---|---|---|"]
    for endpoint, r in sorted(results.items()):
        if r["status"] in ("baseline-failed", "network-error"):
            body = (r.get("baseline_body") or r.get("error") or "")[:80].replace(
                "|", "/"
            )
            body = body.replace("\n", " ")
            out.append(
                f"| {endpoint} | {r.get('baseline_status', r['status'])} |"
                f" {r.get('note') or ''} | {body!r} |"
            )
    empty = [
        e
        for e, r in sorted(results.items())
        if r["status"] in ("success", "drift") and r.get("json_shape") == {}
    ]
    if empty:
        out += ["", "Answer HTTP 200 with an empty `{}` body (dead in practice):", ""]
        out += [f"- {e} ({results[e].get('note') or 'no note'})" for e in empty]
    working_but_flagged = [
        f"{e} ({r['note']})"
        for e, r in sorted(results.items())
        if r["status"] in ("success", "drift")
        and r.get("note") not in (None, "no EndpointSpec")
        and r.get("json_shape") != {}
    ]
    if working_but_flagged:
        out += [
            "",
            "Marked skip/deprecated in `endpoint_specs.py` but answered fine:",
            "",
        ]
        out += [f"- {line}" for line in working_but_flagged]

    out += ["", "## Parameter interactions", ""]
    interactions = [
        f"`{e}`: {r['interactions']}"
        for e, r in sorted(results.items())
        if r.get("interactions")
    ]
    out += [f"- {line}" for line in interactions] or ["- none detected"]

    rows, totals = cost_table(results)
    phase_lines, grand = phase_totals(totals)
    out += ["", "## Cost", ""]
    out.append(
        f"{grand} lookups ({totals['_sent']} sent live, the rest from the 24h cache),"
        f" {totals['_seconds'] / 60:.0f} min of request time."
    )
    out += ["", "| phase | lookups | share | split |", "|---|---|---|---|"]
    out += phase_lines
    out += ["", "<details><summary>Per endpoint</summary>", ""]
    out += ["| endpoint | status | params | lookups | sent | seconds | by phase |"]
    out += ["|---|---|---|---|---|---|---|"]
    out += rows
    out += ["", "</details>", ""]
    return "\n".join(out)


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="python -m tools.stats.endpoint_scope.report", description=__doc__
    )
    parser.add_argument("results", help="endpoint_scope --json output")
    parser.add_argument("--offline", help="--json output of an --offline run")
    args = parser.parse_args(argv)
    with open(args.results) as f:
        results = json.load(f)
    offline = None
    if args.offline:
        with open(args.offline) as f:
            offline = json.load(f)
    print(render(results, offline))


if __name__ == "__main__":
    main()
