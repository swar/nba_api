[![Version: PyPI](https://img.shields.io/pypi/v/nba_api.svg?longCache=true&style=for-the-badge&logo=pypi)](https://pypi.python.org/pypi/nba_api)
[![Downloads per Month: PyPY](https://img.shields.io/pypi/dm/nba_api.svg?style=for-the-badge)](https://pepy.tech/project/nba-api)
[![Build: CircleCI](https://img.shields.io/circleci/project/github/swar/nba_api.svg?style=for-the-badge&logo=circleci)](https://circleci.com/gh/swar/nba_api)
[![License: MIT](https://img.shields.io/github/license/swar/nba_api.svg?style=for-the-badge)](https://github.com/swar/nba_api/blob/master/LICENSE)
[![Slack](https://img.shields.io/badge/Slack-NBA_API-4A154B?style=for-the-badge&logo=slack)](https://join.slack.com/t/nbaapi/shared_invite/zt-2c18itntt-ObWh0ovNQmnwLGFagmCbpg)

# nba_api

## An API Client Package to Access the APIs of NBA.com

`nba_api` is an API Client for `www.nba.com`. This package intends to make the APIs of [NBA.com](https://www.nba.com/) easily accessible and provide extensive documentation about them.

# Getting Started

`nba_api` requires Python 3.7+ along with the `requests` and `numpy` packages. While `pandas` is not required, it is required to work with Pandas DataFrames.

```bash
pip install nba_api
```

## NBA Official Stats

```python
from nba_api.stats.endpoints import playercareerstats

# Nikola Jokić
career = playercareerstats.PlayerCareerStats(player_id='203999') 

# pandas data frames (optional: pip install pandas)
career.get_data_frames()[0]

# json
career.get_json()

# dictionary
career.get_dict()
```

## NBA Live Data

```python
from nba_api.live.nba.endpoints import scoreboard

# Today's Score Board
games = scoreboard.ScoreBoard()

# json
games.get_json()

# dictionary
games.get_dict()
```

## Additional Examples

- [Requests/Response Options](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/examples.md#endpoint-usage-example)
  - Proxy Support, Custom Headers, and Timeout Settings
  - Return Types and Raw Responses
- [Static Data Sets](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/examples.md#static-usage-examples)
  - Reduce HTTP requests for common and frequently accessed player and team data.
- [Jupyter Notebooks](https://github.com/swar/nba_api/tree/master/docs/examples)
  - Practical examples in Jupyter Notebook format, including making basic calls, finding games, working with play-by-play data, and interacting with live game data.

# Documentation

- [Table of Contents](https://github.com/swar/nba_api/tree/master/docs/table_of_contents.md)
- [Package Structure](https://github.com/swar/nba_api/tree/master/docs/package_structure.md)
- [Endpoints](/docs/nba_api/stats/endpoints)
- Static Data Sets
  - [players.py](https://github.com/swar/nba_api/tree/master/docs/nba_api/stats/static/players.md)
  - [teams.py](https://github.com/swar/nba_api/tree/master/docs/nba_api/stats/static/teams.md)

# Join the Community
## Slack

Join [Slack](https://join.slack.com/t/nbaapi/shared_invite/zt-2c18itntt-ObWh0ovNQmnwLGFagmCbpg) to get help, help others, provide feedback, see amazing projects, participates in discussions, and collaborate with others from around the world.

## Stack Overflow

Not a Slack fan? No problem. Head over to [StackOverflow](https://stackoverflow.com/questions/tagged/nba-api). Be sure to tag your post with `nba-api`.

# Contributing

*See [Contributing to the NBA_API](https://github.com/swar/nba_api/blob/master/CONTRIBUTING.md) for complete details.*

## Endpoints

A significant purpose of this package is to continuously map and analyze as many endpoints on NBA.com as possible. The documentation and analysis of the endpoints and parameters in this package are some of the most extensive information available. At the same time, NBA.com does not provide information regarding new, changed, or removed endpoints.

If you find a new, changed, or deprecated endpoint, open a [GitHub Issue](https://github.com/swar/nba_api/issues)

## Bugs

Encounter a bug, [report a bug](https://github.com/swar/nba_api/issues).

# License & Terms of Use

## API Client Package

The `nba_api` package is Open Source with an [MIT License](https://github.com/swar/nba_api/blob/master/LICENSE).

## NBA.com

NBA.com has a [Terms of Use](https://www.nba.com/termsofuse) regarding the use of the NBA’s digital platforms.
