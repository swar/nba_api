# Endpoint scope
>/tools/stats/endpoint_scope/

Scopes out stats.nba.com endpoints: what a response contains, how it has drifted from
what the library expects, and how the server treats each parameter. Use it to check
existing endpoints for upstream changes and to map out a new endpoint before adding it.

It replaces [`endpoint_analysis`](../endpoint_analysis/analysis.md), which relied on
error messages stats.nba.com no longer sends: an empty request now returns a bare HTTP
500, and invalid values return `{"Param": ["Invalid parameters"]}` with no regex pattern.

## Usage

Run from the repo root:

```bash
# Offline audit of every endpoint against its VCR cassette (no network, ~3s)
uv run python -m tools.stats.endpoint_scope --all --offline

# Probe library endpoints live
uv run python -m tools.stats.endpoint_scope commonplayerinfo leaguedashplayerstats

# Scope an endpoint the library doesn't have yet: paste a working URL from devtools
uv run python -m tools.stats.endpoint_scope "https://stats.nba.com/stats/playerindex?LeagueID=00&Season=2025-26"

# Which values does the server accept? (one request per candidate value)
uv run python -m tools.stats.endpoint_scope leaguedashplayerstats --values PerMode,PlayerPosition
```

| Option | |
|---|---|
| `--all` / `--list` | Every library endpoint / list their names |
| `--offline` | Read baselines from cassettes; no requests |
| `--values [P1,P2]` | Enum discovery for all validated params, or just those listed |
| `--json FILE` | Write results (merged into FILE if it exists) |
| `--pause SECONDS` | Minimum gap between request starts (default 0.6) |
| `--no-cache` | Ignore the 24h response cache |
| `--resume` | Skip endpoints already finished in the `--json` file |
| `--no-priors` | Ignore parameter behaviour learned from earlier endpoints |
| `--use-env-proxy` | Use `NBA_API_PROXY`; the default is a direct connection |

Live runs hit stats.nba.com, which rate-limits aggressively. A cold `--all` run makes
about 1,300–1,500 requests (~30 minutes in one process). Run it in batches into one
`--json` file with `--resume`, so an interrupted run picks up where it stopped. Re-running
into the same `--json` file is cheaper: each endpoint's previous report steers the probing.

Throttling is handled rather than misread: HTTP 403/429/502/503/504 and timeouts are
retried with backoff and never counted as a verdict on a parameter. An endpoint that
still fails is retried after 60s and 180s, then recorded as `network-error`. The run
moves on, unless two endpoints in a row end that way, in which case it stops.

## How it works

Everything starts from a request known to work: the library's endpoint class with the
curated values in `tests/integration/helpers/endpoint_specs.py`, or the URL you pass.
Then one thing changes at a time:

1. **Baseline**: datasets and columns, compared with the class's `expected_data`.
   Nested (V3) endpoints are run through their parser, and raw fields no dataset column
   surfaces are listed as *unparsed fields*.
2. **Cassette diff**: every JSON key path in the live response, compared with the
   recorded cassette.
3. **Echo**: parameters the server echoes back that the library does not send.
4. **Nullable**: send `""`. Anything still returning 200 is nullable.
5. **Required**: drop parameters. A 500 means one of them is required. Non-null
   parameters are dropped one at a time, because most of them are required; the
   rest are dropped as one group, which still catches the rare param that is
   required yet accepts `""` (CommonTeamRoster `TeamID`).
6. **Validated**: send invalid values (`-1` for integers, `zz~` otherwise). The server's
   400 names every parameter it validates. Parameters that 500 instead are reported as
   *500 on bad type* (dates, mostly).
7. **Values** (opt-in): try every value of the related `parameters.py` classes. It
   reports which class fits, which values the library offers but the server rejects,
   and which values the server accepts that the library lacks.

Parameters are tested in groups, and a group is split only when it fails. Parameters
that usually fail are tested one at a time first, because a group containing them is
bound to fail. "Usually" comes from *priors*:

- the endpoint's own report in the `--json` file from an earlier run, if there is one;
- otherwise, how often the same parameter name failed on other endpoints (more than
  20% of the time for `""`, 30% for invalid values; any failure when dropped);
- otherwise, numeric values are tested one at a time.

Priors only change the order of tests, never which parameters get tested, so a wrong
prior costs requests but not accuracy. Every reported failure is confirmed by a request
that changes only that parameter. The priors and the response cache live in
`~/.cache/nba_api/endpoint_scope/`.

A network error aborts that endpoint's report rather than being read as a rejection.

## Checking accuracy and cost

`truth.py` grades the probing against **ground truth**: every parameter dropped,
blanked, set to `zz~`, and set to `-1` (if numeric), one at a time and uncached, with
every non-200 sent twice to check the server is deterministic.

```bash
# Record ground truth (live; ~3.5 requests per parameter)
uv run python -m tools.stats.endpoint_scope.truth record leaguedashteamstats boxscoreadvancedv3 --out truth.json

# Grade the scoper against it, cold and with warm priors (live, uncached)
uv run python -m tools.stats.endpoint_scope.truth score truth.json --check-simulator

# Same, with no network: answers come from truth.json
uv run python -m tools.stats.endpoint_scope.truth score truth.json --simulate
```

`--simulate` assumes a group of changes fails exactly when one of them fails alone.
`--check-simulator` replays the requests a live `score` sent and reports how often that
held. `truth.simulate_run` costs a whole run offline from an earlier `--json` file. Use
it to try out changes to the probing before spending live requests on them.

`report.py` turns `--json` output into a markdown report grouped by finding, including
a per-phase breakdown of where the requests went:

```bash
uv run python -m tools.stats.endpoint_scope.report scope.json --offline offline.json > report.md
```

## Output

Each endpoint gets a status:

- `success`: matches the library.
- `drift`: something was flagged; the `!` lines say what.
- `baseline-failed`: the known-good request itself failed.
- `network-error`
- `no-cassette` (offline only)

The `--json` output keeps the keys of the old `analysis.json`
(`parameters`, `required_parameters`, `nullable_parameters`, `parameter_patterns`,
`data_sets`) so the generators can still read it. `parameter_patterns` is always `null`
now that the server no longer publishes patterns; use `values` instead.
