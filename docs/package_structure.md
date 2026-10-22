# Package structure

```text
nba_api/
├── src/nba_api/                  # the installed package
│   ├── library/
│   │   ├── http.py               # shared HTTP client (NBAHTTP, NBAResponse)
│   │   └── debug/debug.py        # DEBUG flags and default proxy (NBA_API_PROXY)
│   ├── stats/                    # stats.nba.com
│   │   ├── endpoints/            # one module per endpoint
│   │   │   ├── _base.py          # Endpoint and Endpoint.DataSet base classes
│   │   │   ├── _parsers/         # parsers for endpoints that return nested JSON
│   │   │   └── _expected_data/   # expected data set columns for large endpoints
│   │   ├── library/
│   │   │   ├── http.py           # NBAStatsHTTP and NBAStatsResponse
│   │   │   ├── parameters.py     # parameter values and defaults
│   │   │   ├── data.py           # generated player and team data
│   │   │   └── ...               # play-by-play helpers (eventmsgtype, playbyplayregex)
│   │   └── static/               # offline player and team lookups
│   └── live/nba/                 # cdn.nba.com live data
│       ├── endpoints/            # ScoreBoard, BoxScore, PlayByPlay, Odds
│       └── library/http.py       # NBALiveHTTP
├── tests/
│   ├── unit/                     # offline tests; HTTP is mocked
│   └── integration/              # smoke and scenario tests using recorded (VCR) responses
├── docs/                         # this documentation, plus example notebooks in docs/examples/
├── tools/                        # endpoint analysis and code/doc generators
└── scripts/                      # maintenance scripts (static data refresh, endpoint analysis, releases)
```

## `src/nba_api`

The package installed by `pip install nba_api`. Users import from three places:

- **`nba_api.stats.endpoints`** — `stats.nba.com` endpoints. See [Endpoint data structure](nba_api/stats/endpoints_data_structure.md).
- **`nba_api.stats.static`** — offline player and team lookups. See [players.py](nba_api/stats/static/players.md) and [teams.py](nba_api/stats/static/teams.md).
- **`nba_api.live.nba.endpoints`** — live game data from `cdn.nba.com`.

Modules and directories prefixed with `_` are internal.

## `tests`

Unit tests run offline and must never make network requests. Integration tests replay HTTP responses recorded as VCR cassettes (the `vcr` marker); tests marked `live` call the real API. See [CONTRIBUTING.md](../CONTRIBUTING.md#running-checks).

## `tools` and `scripts`

`tools/` holds the endpoint analyzer and the generators for endpoint files and documentation. `scripts/` holds the entry points maintainers run. See [Scripts](scripts.md).
