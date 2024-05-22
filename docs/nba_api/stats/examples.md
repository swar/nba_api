# Stats Examples

## Endpoint Usage Example

This is an example of how to call an `stats.nba.com` endpoint and access the data returned. This example can be applied to all stats endpoints.

Let's say we want to get the player information for `LeBron James (2544)`. I know that I can get this information by calling the [`CommonPlayerInfo`](endpoints/commonplayerinfo.md) stats endpoint.

Once you call the class, the request will be sent and the information will be stored inside the `player_info` variable. 

As of v1.1.0, we now support custom proxy, header, and timeout settings on every request.

```python
from nba_api.stats.endpoints import commonplayerinfo

# Basic Request
player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544)


custom_headers = {
    'Host': 'stats.nba.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}

# Only available after v1.1.0
# Proxy Support, Custom Headers Support, Timeout Support (in seconds)
player_info = commonplayerinfo.CommonPlayerInfo(player_id=2544, proxy='127.0.0.1:80', headers=custom_headers, timeout=100)
```

`player_info` can now be used to access different information that was returned by the request. [`CommonPlayerInfo`](endpoints/commonplayerinfo.md) contains the following data sets that are stored as a [`DataSet`](endpoints_data_structure.md).

* `available_seasons`
* `common_player_info`
* `player_headline_stats`

Each data set has additional methods in order to access the data in either `json`, a `dictionary`, or a `DataFrame`.

```python
# Returns data in a JSON string.
player_info.available_seasons.get_json()

# Returns data in a dictionary.
player_info.available_seasons.get_dict()

# Returns the data set in a pandas DataFrame.
player_info.available_seasons.get_data_frame()
```

Alternatively, you can retrieve the raw request of the response as well as all the data sets in `json`, a `dictionary`, a normalized `json` dictionary (`header:value` format), a normalized `dictionary`, and in a list of pandas `DataFrame`.

```python
# Returns the raw response of the request.
player_info.get_response()

# Returns all data in a JSON string.
player_info.get_json()

# Returns all data in a dictionary.
player_info.get_dict()

# Returns all data in a normalized JSON string.
player_info.get_normalized_json()

# Returns all data in a normalized dictionary.
player_info.get_normalized_dict()

# Returns a list of all data in a pandas DataFrame structure.
player_info.get_data_frames()
```


## Static Usage Examples

Using functions from the static library will not send any requests over http. This data is embedded in this package and will be updated as necessary.

### Players

You can find players using a regex pattern `case-insensitive` by full name, first name, last_name. Below is an example result for `LeBron James (2544)`
```python
lebron_james = {
  'id': 2544,
  'full_name': 'LeBron James',
  'first_name': 'LeBron',
  'last_name': 'James',
  'is_active': True
}
```

All three of these searches will return a list of players. Corresponding functions exist for WNBA players as well.

```python
from nba_api.stats.static import players

# Find players by full name.
players.find_players_by_full_name('james')

# Find players by first name.
players.find_players_by_first_name('lebron')

# Find players by last name.
players.find_players_by_last_name('^(james|love)$')

# Get all players.
players.get_players()

# Get all players in the WNBA.
players.get_wnba_players()
```

In addition, you can find players by ID by using `find_player_by_id()`. `get_active_players()` and `get_inactive_players()` will return a list of only active and only inactive players, respectively.


### Teams

You can also find teams using regex patterns on fields such as full name, state, city, and nickname. As well as finding teams by year founded, abbreviation, and id. Corresponding functions exist for WNBA players as well.

```python
from nba_api.stats.static import teams

# Find teams by full name.
teams.find_teams_by_full_name('cav')

# Find teams by state.
teams.find_teams_by_state('ohio')

# Find teams by city.
teams.find_teams_by_city('cleveland')

# Find teams by team nickname.
teams.find_teams_by_nickname('cav')

# Find teams by year founded.
teams.find_teams_by_year_founded(1968)

# Find teams by abbreviation.
teams.find_team_by_abbreviation('cle')

# Find teams by id.
teams.find_team_name_by_id(1610612739)

# Get all teams.
teams.get_teams()

# Get all WNBA teams.
teams.get_wnba_teams()
```
