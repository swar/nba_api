# Stats examples

## Calling an endpoint

Every `stats.nba.com` endpoint follows the same pattern. Here we fetch player information for Donovan Mitchell (player ID `1628378`) with the [`CommonPlayerInfo`](endpoints/commonplayerinfo.md) endpoint:

```python
from nba_api.stats.endpoints import commonplayerinfo

player_info = commonplayerinfo.CommonPlayerInfo(player_id=1628378)
```

Constructing the endpoint sends the request. Don't know the ID? Look it up offline with [`players.find_players_by_full_name("donovan mitchell")`](#players).

### Request options

Every endpoint accepts these keyword arguments in addition to its own parameters:

| Argument | Default | Description |
|---|---|---|
| `timeout` | `30` | Seconds to wait for a response. |
| `proxy` | `None` | A proxy URL, or a list of URLs (one is picked at random per request). `None` uses the `NBA_API_PROXY` environment variable if set; `""` disables the proxy. See [`debug.py`](../debug.md#proxy). |
| `headers` | `None` | A `dict` that **replaces** the default browser-like headers. `None` uses the defaults, which work for most requests. |
| `get_request` | `True` | If `False`, the endpoint is built but not sent; call `.get_request()` to send it. |

```python
player_info = commonplayerinfo.CommonPlayerInfo(
    player_id=1628378,
    proxy="http://127.0.0.1:8080",
    timeout=60,
)
```

> [!TIP]
> `stats.nba.com` throttles rapid requests and does not respond to some cloud-hosting IP ranges, so requests from a server may hang until they time out. When fetching in a loop, pause between requests (for example, `time.sleep(1)`). If requests time out from a hosted environment, try a proxy.

### Reading the results

The response is split into data sets, each exposed as an attribute. `CommonPlayerInfo` returns three:

- `available_seasons`
- `common_player_info`
- `player_headline_stats`

The data sets for every endpoint are listed on its page in the [table of contents](../../table_of_contents.md). Each one is an [`Endpoint.DataSet`](endpoints_data_structure.md#class-endpointdataset):

```python
player_info.common_player_info.get_data_frame()  # pandas DataFrame
player_info.common_player_info.get_dict()        # {"headers": [...], "data": [[...], ...]}
player_info.common_player_info.get_json()        # the same, as a JSON string
```

You can also work with the whole response at once:

```python
player_info.get_data_frames()       # list of DataFrames, one per data set
player_info.get_normalized_dict()   # {"DataSetName": [{"COLUMN": value, ...}, ...], ...}
player_info.get_normalized_json()   # the same, as a JSON string
player_info.get_dict()              # the raw response, parsed
player_info.get_json()              # the raw response, re-serialized
player_info.get_response()          # the raw response text
player_info.get_request_url()       # the URL that was requested
```

## Static data

The `nba_api.stats.static` modules search player and team data that ships with the package. They send no requests, so they are fast and work offline. The data is refreshed with each release.

### Players

Name searches take a case-insensitive regular expression and ignore accents (`"žydrūnas"` finds `"Zydrunas Ilgauskas"`). They return a list of player dicts:

```python
from nba_api.stats.static import players

players.find_players_by_full_name("donovan mitchell")
# [{'id': 1628378, 'full_name': 'Donovan Mitchell', 'first_name': 'Donovan',
#   'last_name': 'Mitchell', 'is_active': True}]

players.find_players_by_first_name("donovan")
players.find_players_by_last_name("^(mitchell|mobley)$")  # anchors for exact matches
players.find_player_by_id(1628378)                   # a single dict, or None

players.get_players()           # all players
players.get_active_players()
players.get_inactive_players()
```

Every function has a WNBA equivalent, for example `players.find_wnba_players_by_full_name()` and `players.get_wnba_players()`. See [players.py](static/players.md).

### Teams

```python
from nba_api.stats.static import teams

teams.find_teams_by_full_name("cav")        # list of team dicts
teams.find_teams_by_state("ohio")
teams.find_teams_by_city("cleveland")
teams.find_teams_by_nickname("cav")
teams.find_teams_by_year_founded(1970)

teams.find_team_by_abbreviation("cle")      # a single dict, or None
teams.find_team_name_by_id(1610612739)      # a single dict, or None
teams.find_teams_by_championship_year(2016) # "Cleveland Cavaliers" (a string)

teams.get_teams()                           # all NBA teams
teams.get_wnba_teams()                      # all WNBA teams
```

See [teams.py](static/teams.md) for return values and the WNBA equivalents.
