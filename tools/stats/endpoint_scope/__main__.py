"""CLI: python -m tools.stats.endpoint_scope <endpoint|URL> ... [options]

Examples:
    python -m tools.stats.endpoint_scope commonplayerinfo leaguedashplayerstats
    python -m tools.stats.endpoint_scope "https://stats.nba.com/stats/newthing?LeagueID=00"
    python -m tools.stats.endpoint_scope --all --json scope.json
    python -m tools.stats.endpoint_scope --all --offline     # cassettes only, no network
    python -m tools.stats.endpoint_scope leaguedashplayerstats --values PerMode,MeasureType
    python -m tools.stats.endpoint_scope --list
"""

import argparse
import json
import os

from tools.stats.endpoint_scope.scope import (
    Priors,
    format_report,
    list_endpoint_classes,
    resolve_targets,
    scope_endpoint,
)


def main():
    parser = argparse.ArgumentParser(
        prog="python -m tools.stats.endpoint_scope", description=__doc__
    )
    parser.add_argument("targets", nargs="*", help="endpoint names or full URLs")
    parser.add_argument("--all", action="store_true", help="every library endpoint")
    parser.add_argument("--list", action="store_true", help="list known endpoints")
    parser.add_argument("--json", help="write analysis.json-compatible results here")
    parser.add_argument(
        "--offline",
        action="store_true",
        help="no network: check cassettes against expected_data and parsers",
    )
    parser.add_argument(
        "--values",
        nargs="?",
        const="",
        help="discover accepted enum values (optionally comma-separated params);"
        " one request per candidate value",
    )
    parser.add_argument("--pause", type=float, default=0.6, help="seconds/request")
    parser.add_argument("--no-cache", action="store_true", help="ignore disk cache")
    parser.add_argument(
        "--no-priors",
        action="store_true",
        help="ignore what earlier endpoints taught us about shared parameters",
    )
    parser.add_argument(
        "--use-env-proxy",
        action="store_true",
        help="use NBA_API_PROXY (from env/.env); default is a direct connection",
    )
    args = parser.parse_args()

    classes = list_endpoint_classes()
    if args.list:
        print("\n".join(sorted(classes)))
        return
    targets = sorted(classes) if args.all else args.targets
    if not targets:
        parser.error("pass endpoint names/URLs, or --all")

    prober_kwargs = {
        "pause": args.pause,
        "proxy": None if args.use_env_proxy else "",
        "cache_ttl": 0 if args.no_cache else 86400,
    }

    results, statuses = {}, []
    priors = Priors(enabled=not args.no_priors)
    if args.json and os.path.exists(args.json):
        with open(args.json) as f:
            results = json.load(f)

    for endpoint, params, cls, note in resolve_targets(targets, classes):
        if not params and "pass a full URL" in (note or "") and not args.offline:
            print(f"\n== {endpoint}  [skipped] {note}")
            continue
        values = (
            None if args.values is None else set(filter(None, args.values.split(",")))
        )
        report = scope_endpoint(
            endpoint,
            params,
            cls,
            note,
            offline=args.offline,
            values=values,
            priors=priors,
            **prober_kwargs,
        )
        if not args.no_priors and report["status"] in ("success", "drift"):
            priors.save()
        print(format_report(report), flush=True)
        results[endpoint] = report
        statuses.append(report["status"])
        if args.json:
            with open(args.json, "w") as f:
                json.dump(results, f, indent=2, sort_keys=True, default=str)

    if len(statuses) > 1:
        summary = {s: statuses.count(s) for s in sorted(set(statuses))}
        print(f"\nsummary: {summary}")


if __name__ == "__main__":
    main()
