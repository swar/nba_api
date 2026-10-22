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
poetry run python -m tools.stats.endpoint_scope --all --offline

# Probe library endpoints live
poetry run python -m tools.stats.endpoint_scope commonplayerinfo leaguedashplayerstats

# Scope an endpoint the library doesn't have yet: paste a working URL from devtools
poetry run python -m tools.stats.endpoint_scope "https://stats.nba.com/stats/playerindex?LeagueID=00&Season=2025-26"

# Which values does the server accept? (one request per candidate value)
poetry run python -m tools.stats.endpoint_scope leaguedashplayerstats --values PerMode,PlayerPosition
```

| Option | |
|---|---|
| `--all` / `--list` | Every library endpoint / list their names |
| `--offline` | Read baselines from cassettes; no requests |
| `--values [P1,P2]` | Enum discovery for all validated params, or just those listed |
| `--json FILE` | Write results (merged into FILE if it exists) |
| `--pause SECONDS` | Delay between requests (default 0.6) |
| `--no-cache` | Ignore the 24h response cache |
| `--no-priors` | Ignore parameter behaviour learned from earlier endpoints |
| `--use-env-proxy` | Use `NBA_API_PROXY`; the default is a direct connection |

Live runs hit stats.nba.com, which rate-limits aggressively. Probe a few endpoints at a
time rather than `--all`.

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
4. **Required**: drop parameters. A 500 means one of them is required.
5. **Nullable**: send `""`. Anything still returning 200 is nullable.
6. **Validated**: send invalid values (`-1` for integers, `zz~` otherwise). The server's
   400 names every parameter it validates. Parameters that 500 instead are reported as
   *500 on bad type* (dates, mostly).
7. **Values** (opt-in): try every value of the related `parameters.py` classes. It
   reports which class fits, which values the library offers but the server rejects,
   and which values the server accepts that the library lacks.

Parameters are tested in groups, and a group is split only when it fails. Parameters
that failed on earlier endpoints are tested one at a time first, because dashboard
endpoints share them. Those *priors* and the response cache live in
`~/.cache/nba_api/endpoint_scope/`.

A network error aborts that endpoint's report rather than being read as a rejection.

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
