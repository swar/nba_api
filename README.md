<h1 align="center">nba_api</h1>

<p align="center">
  <strong>A Python client for the APIs behind NBA.com</strong>
</p>

<p align="center">
  <a href="https://pypi.org/project/nba_api/"><img src="https://img.shields.io/pypi/v/nba_api.svg" alt="PyPI version"></a>
  <a href="https://pypi.org/project/nba_api/"><img src="https://img.shields.io/pypi/pyversions/nba_api.svg" alt="Python versions"></a>
  <a href="https://pepy.tech/project/nba-api"><img src="https://img.shields.io/pypi/dm/nba_api.svg" alt="Monthly downloads"></a>
  <a href="https://github.com/swar/nba_api/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/swar/nba_api/ci.yml?branch=master" alt="CI status"></a>
  <a href="https://github.com/swar/nba_api/blob/master/LICENSE"><img src="https://img.shields.io/github/license/swar/nba_api.svg" alt="MIT license"></a>
</p>

<p align="center">
  <a href="https://github.com/swar/nba_api/blob/master/docs/table_of_contents.md">Documentation</a> ·
  <a href="https://github.com/swar/nba_api/blob/master/docs/table_of_contents.md#reference">Endpoints</a> ·
  <a href="https://github.com/swar/nba_api/tree/master/docs/examples">Notebooks</a> ·
  <a href="https://join.slack.com/t/nbaapi/shared_invite/zt-3dc2qtnh0-udQJoSYrQVWaXOF3owVaAw">Slack</a>
</p>

**The NBA's stats, in Python.** `nba_api` wraps 130+ `stats.nba.com` endpoints and the live game feeds behind [NBA.com](https://www.nba.com/), no API key required, and hands stats back as pandas DataFrames.

- **Every corner of NBA.com stats**: player and team stats, box scores, game logs, shot charts, play-by-play, standings, and more, with each endpoint's parameters and data sets documented
- **Live game data**: scoreboard, box scores, play-by-play, and odds, updated during games
- **pandas built in**: stats come back as DataFrames, dicts, or JSON
- **Player and team IDs offline**: reference data ships with the package, so lookups need no request
- **More than the NBA**: many endpoints also cover the WNBA and G League through `league_id`

## Installation

```bash
pip install nba_api
```

Requires Python 3.10+. Installs `requests`, `numpy`, and `pandas`.

## Quick start

### Look up a player or team

Player and team reference data ships with the package, so lookups are instant and work offline.

```python
from nba_api.stats.static import players, teams

players.find_players_by_full_name("donovan mitchell")
# [{'id': 1628378, 'full_name': 'Donovan Mitchell', 'first_name': 'Donovan',
#   'last_name': 'Mitchell', 'is_active': True}]

teams.find_team_by_abbreviation("cle")
# {'id': 1610612739, 'full_name': 'Cleveland Cavaliers', 'abbreviation': 'CLE', ...}
```

Searches take case-insensitive regular expressions, and player name searches ignore accents (`"žydrūnas"` finds `"Zydrunas Ilgauskas"`).

### Get stats from `stats.nba.com`

```python
from nba_api.stats.endpoints import playercareerstats

career = playercareerstats.PlayerCareerStats(player_id=1628378)  # sends the request

df = career.season_totals_regular_season.get_data_frame()
df[["SEASON_ID", "TEAM_ABBREVIATION", "PTS"]].tail(3)
#   SEASON_ID TEAM_ABBREVIATION   PTS
# 6   2023-24               CLE  1463
# 7   2024-25               CLE  1701
# 8   2025-26               CLE  1952
```

Every stats endpoint works the same way: constructing it sends the request, and each data set it returns is an attribute with `get_data_frame()`, `get_dict()`, and `get_json()`. To grab everything at once, use `career.get_data_frames()` or `career.get_dict()`. The [endpoint reference](https://github.com/swar/nba_api/blob/master/docs/table_of_contents.md#reference) lists every endpoint's parameters and data sets.

### Follow live games from `cdn.nba.com`

```python
from nba_api.live.nba.endpoints import scoreboard

games = scoreboard.ScoreBoard()  # today's games
cavs = [
    g for g in games.games.get_dict()
    if "CLE" in (g["homeTeam"]["teamTricode"], g["awayTeam"]["teamTricode"])
]  # tonight's Cavs game, if they play
```

Live endpoints: `ScoreBoard`, `BoxScore(game_id)`, `PlayByPlay(game_id)`, and `Odds`. They return dicts and JSON.

## Request options

Every endpoint, stats or live, accepts the same request options:

```python
career = playercareerstats.PlayerCareerStats(
    player_id=1628378,
    timeout=60,                       # seconds; default 30
    proxy="http://127.0.0.1:8080",    # or a list of proxies to pick from at random
    headers={"User-Agent": "..."},    # replaces the default headers entirely
    get_request=False,                # build the request without sending it
)
career.get_request()                  # send it later
```

## Rate limits and hosting

> **Requests hanging or timing out?** `stats.nba.com` throttles rapid requests and does not respond to many cloud-hosting IP ranges (AWS, GCP, Azure, Colab, and others).

- Pause between requests when fetching in a loop, for example `time.sleep(1)`.
- Increase `timeout`.
- Route requests through a `proxy`, or set the `NBA_API_PROXY` environment variable.

More detail is in the [stats examples](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/examples.md).

## Documentation

- [Table of contents](https://github.com/swar/nba_api/blob/master/docs/table_of_contents.md): start here
- [Stats examples](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/examples.md): request options, return formats, static data
- [Jupyter notebooks](https://github.com/swar/nba_api/tree/master/docs/examples): basic calls, finding games, play-by-play, live data
- [Endpoint data structure](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints_data_structure.md): the methods every endpoint shares
- [Parameters](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md): valid values and defaults
- [Changelog](https://github.com/swar/nba_api/blob/master/CHANGELOG.MD)

## Community

- **Slack**: [join the workspace](https://join.slack.com/t/nbaapi/shared_invite/zt-3dc2qtnh0-udQJoSYrQVWaXOF3owVaAw) to get help, help others, share projects, and discuss the API.
- **Stack Overflow**: ask questions tagged [`nba-api`](https://stackoverflow.com/questions/tagged/nba-api).

## Contributing

Contributions of all sizes are welcome, from fixing a typo to adding an endpoint. See [CONTRIBUTING.md](https://github.com/swar/nba_api/blob/master/CONTRIBUTING.md) to set up a development environment and open a pull request.

NBA.com does not announce new, changed, or removed endpoints. If you find one, or hit a bug, [open an issue](https://github.com/swar/nba_api/issues).

## License and terms of use

`nba_api` is open source under the [MIT License](https://github.com/swar/nba_api/blob/master/LICENSE).

Data retrieved with this package comes from NBA.com and is subject to the NBA.com [Terms of Use](https://www.nba.com/termsofuse).

`nba_api` is an independent, community-maintained project and is not affiliated with, endorsed by, or sponsored by the NBA.
