[![Version: PyPI](https://img.shields.io/pypi/v/nba_api.svg?longCache=true&style=for-the-badge&logo=pypi)](https://pypi.python.org/pypi/nba_api)
[![Downloads per Month: PyPI](https://img.shields.io/pypi/dm/nba_api.svg?style=for-the-badge)](https://pepy.tech/project/nba-api)
[![Build: CircleCI](https://img.shields.io/circleci/project/github/swar/nba_api.svg?style=for-the-badge&logo=circleci)](https://circleci.com/gh/swar/nba_api)
[![License: MIT](https://img.shields.io/github/license/swar/nba_api.svg?style=for-the-badge)](https://github.com/swar/nba_api/blob/master/LICENSE)
[![Slack](https://img.shields.io/badge/Slack-NBA_API-4A154B?style=for-the-badge&logo=slack)](https://join.slack.com/t/nbaapi/shared_invite/zt-3dc2qtnh0-udQJoSYrQVWaXOF3owVaAw)

# nba_api

**An API client for NBA.com.** `nba_api` makes the APIs behind [NBA.com](https://www.nba.com/) easy to call from Python and documents them extensively — 130+ `stats.nba.com` endpoints, the live game data feeds on `cdn.nba.com`, and bundled player and team reference data.

## Installation

```bash
pip install nba_api
```

Requires Python 3.10+. Installs `requests`, `numpy`, and `pandas`.

## Quick start

### Find a player or team (no HTTP request)

Player and team reference data ships with the package, so lookups are instant and offline.

```python
from nba_api.stats.static import players, teams

players.find_players_by_full_name("jokic")
# [{'id': 203999, 'full_name': 'Nikola Jokić', 'first_name': 'Nikola',
#   'last_name': 'Jokić', 'is_active': True}]

teams.find_team_by_abbreviation("bos")
# {'id': 1610612738, 'full_name': 'Boston Celtics', 'abbreviation': 'BOS', ...}
```

Name searches are case-insensitive regular expressions and ignore accents (`"jokic"` matches `"Jokić"`).

### Official stats (`stats.nba.com`)

```python
from nba_api.stats.endpoints import playercareerstats

career = playercareerstats.PlayerCareerStats(player_id=203999)  # sends the request

career.season_totals_regular_season.get_data_frame()  # one data set as a pandas DataFrame
career.get_data_frames()                              # every data set, as a list of DataFrames
career.get_dict()                                     # the full response as a dict
```

Every stats endpoint works the same way: constructing it sends the request, and each data set the endpoint returns is available as an attribute with `get_data_frame()`, `get_dict()`, and `get_json()`. See the [endpoint reference](https://github.com/swar/nba_api/blob/master/docs/table_of_contents.md#reference) for each endpoint's parameters and data sets.

### Live game data (`cdn.nba.com`)

```python
from nba_api.live.nba.endpoints import scoreboard

games = scoreboard.ScoreBoard()  # today's games

games.score_board_date
games.games.get_dict()
```

Live endpoints: `ScoreBoard`, `BoxScore(game_id)`, `PlayByPlay(game_id)`, and `Odds`.

## Request options

Every endpoint, stats or live, accepts the same request options:

```python
career = playercareerstats.PlayerCareerStats(
    player_id=203999,
    timeout=60,                       # seconds; default 30
    proxy="http://127.0.0.1:8080",    # or a list of proxies to pick from at random
    headers={"User-Agent": "..."},    # replaces the default headers entirely
    get_request=False,                # build the request without sending it
)
career.get_request()                  # send it later
```

`stats.nba.com` throttles rapid requests and does not respond to some cloud-hosting IP ranges. If requests hang or time out, add a delay between calls, increase `timeout`, or route through a `proxy`. More detail is in the [stats examples](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/examples.md).

## Documentation

- [Table of contents](https://github.com/swar/nba_api/blob/master/docs/table_of_contents.md) — start here
- [Stats examples](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/examples.md) — request options, return formats, static data
- [Jupyter notebooks](https://github.com/swar/nba_api/tree/master/docs/examples) — basic calls, finding games, play-by-play, live data
- [Endpoint data structure](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints_data_structure.md) — the methods every endpoint shares
- [Parameters](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/library/parameters.md) — valid values and defaults
- [Changelog](https://github.com/swar/nba_api/blob/master/CHANGELOG.MD)

## Community

- **Slack** — [join the workspace](https://join.slack.com/t/nbaapi/shared_invite/zt-3dc2qtnh0-udQJoSYrQVWaXOF3owVaAw) to get help, help others, share projects, and discuss the API.
- **Stack Overflow** — ask questions tagged [`nba-api`](https://stackoverflow.com/questions/tagged/nba-api).

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](https://github.com/swar/nba_api/blob/master/CONTRIBUTING.md) to set up a development environment and open a pull request.

NBA.com does not announce new, changed, or removed endpoints. If you find one, or hit a bug, [open an issue](https://github.com/swar/nba_api/issues).

## License and terms of use

`nba_api` is open source under the [MIT License](https://github.com/swar/nba_api/blob/master/LICENSE).

Data retrieved with this package comes from NBA.com and is subject to the NBA.com [Terms of Use](https://www.nba.com/termsofuse).
