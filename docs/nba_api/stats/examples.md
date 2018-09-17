# Example Imports
```python
from nba_api.stats.endpoints import *
from nba_api.stats.static import players, teams
```

# Usage Examples

### Find Player by First Name
```python
# Find Players with first name matching regex pattern 'lebron'

player = players.find_players_by_first_name('lebron')
```
##### Returns
```python
players = [{'id': 2544, 'full_name': 'LeBron James', 'first_name': 'LeBron', 'last_name': 'James'}]
```

### Find Team by City
```python
# Find Teams with city matching regex pattern 'cleveland'
team = teams.find_teams_by_city('cleveland')
```
##### Returns
```python
teams = [{'id': 1610612739, 'full_name': 'Cleveland Cavaliers', 'abbreviation': 'CLE', 'nickname': 'Cavaliers', 'city': 'Cleveland', 'state': 'Ohio', 'year_founded': 1970}]
```


### Get Player Shot Chart Details in a pandas `DataFrame`
```python
df_shotchartdetails = shotchartdetail.ShotChartDetail(player_id='2544', team_id='1610612739').shot_chart_detail.get_data_frame()
```
This will return shot chart details in a data frame.
