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
import time

from tools.stats.endpoint_scope.scope import (
    Priors,
    format_report,
    list_endpoint_classes,
    resolve_targets,
    scope_endpoint,
)

# Seconds to wait before retrying an endpoint after its 1st, 2nd, ... network
# error. One endpoint can 503 for minutes while the rest of the site answers, so
# an endpoint that runs out of retries is recorded as a network error and the run
# moves on -- unless that keeps happening, which means stats.nba.com is blocking
# us and hammering it makes the block last longer.
BACKOFF = (60, 180)
MAX_FAILED_IN_A_ROW = 2
# Statuses worth keeping on --resume; anything else is probed again.
FINISHED = ("success", "drift", "baseline-failed")


def main(argv=None, sleep=time.sleep):
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
        "--resume",
        action="store_true",
        help="skip endpoints already finished in the --json file",
    )
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
    args = parser.parse_args(argv)

    classes = list_endpoint_classes()
    if args.list:
        print("\n".join(sorted(classes)))
        return
    targets = sorted(classes) if args.all else args.targets
    if not targets:
        parser.error("pass endpoint names/URLs, or --all")
    if args.resume and not args.json:
        parser.error("--resume needs --json")

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
    values = None if args.values is None else set(filter(None, args.values.split(",")))

    failed_in_a_row = 0
    for endpoint, params, cls, note in resolve_targets(targets, classes):
        if args.resume and results.get(endpoint, {}).get("status") in FINISHED:
            continue
        if not params and "pass a full URL" in (note or "") and not args.offline:
            print(f"\n== {endpoint}  [skipped] {note}")
            continue
        for delay in (*BACKOFF, None):
            report = scope_endpoint(
                endpoint,
                params,
                cls,
                note,
                offline=args.offline,
                values=values,
                priors=priors,
                previous=results.get(endpoint),
                **prober_kwargs,
            )
            if report["status"] != "network-error" or delay is None:
                break
            print(format_report(report), flush=True)
            print(f"   backing off {delay}s, then retrying {endpoint}", flush=True)
            sleep(delay)
        if report["status"] == "network-error":
            failed_in_a_row += 1
            if failed_in_a_row >= MAX_FAILED_IN_A_ROW:
                print(format_report(report), flush=True)
                print("\nRepeated network errors: stopping. Rerun later with --resume.")
                _write(args.json, results)
                raise SystemExit(1)
        else:
            failed_in_a_row = 0
        if not args.no_priors and report["status"] in ("success", "drift"):
            priors.save()
        print(format_report(report), flush=True)
        results[endpoint] = report
        statuses.append(report["status"])
        _write(args.json, results)

    if len(statuses) > 1:
        summary = {s: statuses.count(s) for s in sorted(set(statuses))}
        print(f"\nsummary: {summary}")


def _write(path, results):
    if path:
        with open(path, "w") as f:
            json.dump(results, f, indent=2, sort_keys=True, default=str)


if __name__ == "__main__":
    main()
