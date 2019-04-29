file_template = '''player_index_id = 0
player_index_last_name = 1
player_index_first_name = 2
player_index_full_name = 3
player_index_is_active = 4

# Data last updated: {date_updated}

players = [
{players_list}
]


team_index_id = 0
team_index_abbreviation = 1
team_index_nickname = 2
team_index_year_founded = 3
team_index_city = 4
team_index_full_name = 5
team_index_state = 6

teams = [
    [1610612737, 'ATL', 'Hawks', 1949, 'Atlanta', 'Atlanta Hawks', 'Atlanta'],
    [1610612738, 'BOS', 'Celtics', 1946, 'Boston', 'Boston Celtics', 'Massachusetts'],
    [1610612739, 'CLE', 'Cavaliers', 1970, 'Cleveland', 'Cleveland Cavaliers', 'Ohio'],
    [1610612740, 'NOP', 'Pelicans', 2002, 'New Orleans', 'New Orleans Pelicans', 'Louisiana'],
    [1610612741, 'CHI', 'Bulls', 1966, 'Chicago', 'Chicago Bulls', 'Illinois'],
    [1610612742, 'DAL', 'Mavericks', 1980, 'Dallas', 'Dallas Mavericks', 'Texas'],
    [1610612743, 'DEN', 'Nuggets', 1976, 'Denver', 'Denver Nuggets', 'Colorado'],
    [1610612744, 'GSW', 'Warriors', 1946, 'Golden State', 'Golden State Warriors', 'California'],
    [1610612745, 'HOU', 'Rockets', 1967, 'Houston', 'Houston Rockets', 'Texas'],
    [1610612746, 'LAC', 'Clippers', 1970, 'Los Angeles', 'Los Angeles Clippers', 'California'],
    [1610612747, 'LAL', 'Lakers', 1948, 'Los Angeles', 'Los Angeles Lakers', 'California'],
    [1610612748, 'MIA', 'Heat', 1988, 'Miami', 'Miami Heat', 'Florida'],
    [1610612749, 'MIL', 'Bucks', 1968, 'Milwaukee', 'Milwaukee Bucks', 'Wisconsin'],
    [1610612750, 'MIN', 'Timberwolves', 1989, 'Minnesota', 'Minnesota Timberwolves', 'Minnesota'],
    [1610612751, 'BKN', 'Nets', 1976, 'Brooklyn', 'Brooklyn Nets', 'New York'],
    [1610612752, 'NYK', 'Knicks', 1946, 'New York', 'New York Knicks', 'New York'],
    [1610612753, 'ORL', 'Magic', 1989, 'Orlando', 'Orlando Magic', 'Florida'],
    [1610612754, 'IND', 'Pacers', 1976, 'Indiana', 'Indiana Pacers', 'Indiana'],
    [1610612755, 'PHI', '76ers', 1949, 'Philadelphia', 'Philadelphia 76ers', 'Pennsylvania'],
    [1610612756, 'PHX', 'Suns', 1968, 'Phoenix', 'Phoenix Suns', 'Arizona'],
    [1610612757, 'POR', 'Trail Blazers', 1970, 'Portland', 'Portland Trail Blazers', 'Oregon'],
    [1610612758, 'SAC', 'Kings', 1948, 'Sacramento', 'Sacramento Kings', 'California'],
    [1610612759, 'SAS', 'Spurs', 1976, 'San Antonio', 'San Antonio Spurs', 'Texas'],
    [1610612760, 'OKC', 'Thunder', 1967, 'Oklahoma City', 'Oklahoma City Thunder', 'Oklahoma'],
    [1610612761, 'TOR', 'Raptors', 1995, 'Toronto', 'Toronto Raptors', 'Ontario'],
    [1610612762, 'UTA', 'Jazz', 1974, 'Utah', 'Utah Jazz', 'Utah'],
    [1610612763, 'MEM', 'Grizzlies', 1995, 'Memphis', 'Memphis Grizzlies', 'Tennessee'],
    [1610612764, 'WAS', 'Wizards', 1961, 'Washington', 'Washington Wizards', 'District of Columbia'],
    [1610612765, 'DET', 'Pistons', 1948, 'Detroit', 'Detroit Pistons', 'Michigan'],
    [1610612766, 'CHA', 'Hornets', 1988, 'Charlotte', 'Charlotte Hornets', 'North Carolina']
]
'''

player_row_template ='''    [{id}, "{last_name}", "{first_name}", "{full_name}", {is_active}]'''
