import os
from datetime import datetime

from selenium import webdriver
from parsel import Selector

from tools.stats.static_players_update.template import file_template, player_row_template


url = 'https://stats.nba.com/players/list/{historic_players}'


def get_all_and_active_players():

    # Get page source for active players.
    driver = webdriver.Firefox()
    driver.get(url.format(historic_players=''))
    active_players = driver.page_source
    driver.quit()

    # Get page source for all players.
    driver = webdriver.Firefox()
    driver.get(url.format(historic_players='?/Historic=Y'))
    historic_button = driver.find_element_by_class_name('switch-paddle')
    historic_button.click()
    all_players = driver.page_source
    driver.quit()

    return active_players, all_players


def parse_player_data(response_text):
    sel = Selector(text=response_text)
    all_players = sel.xpath("//li[@class='players-list__name']")

    all_players_dict = {}
    for player in all_players:
        player_list = []
        player_id = (player.xpath(".//a/@href").get().strip('/player'))
        player_name_raw = player.xpath(".//a/text()").get().split(', ')
        player_first_name = player_name_raw[-1]
        player_last_name = player_name_raw[0]

        # Check if Nene, Zhou Qi, etc; player with only one name.
        if player_last_name == player_first_name:
            player_first_name = ''

        player_full_name = player_first_name + ' ' + player_last_name
        player_list.extend((int(player_id), player_last_name, player_first_name, player_full_name, False))
        all_players_dict[int(player_id)] = player_list

    return all_players_dict


def get_active_player_ids(response_text):
    sel = Selector(text=response_text)
    active_players = sel.xpath("//li[@class='players-list__name']")

    active_player_ids = []
    for player in active_players:
        active_player_ids.append(int((player.xpath(".//a/@href").get().strip('/player'))))

    return active_player_ids


def create_players_list():
    active_players_page_source, all_players_page_source = get_all_and_active_players()
    all_players = parse_player_data(all_players_page_source)
    active_player_ids = get_active_player_ids(active_players_page_source)

    players_list = []
    for player_id, player_data in all_players.items():
        if player_id in active_player_ids:
            player_data[-1] = True
        players_list.append(player_data)

    return players_list


def format_player_string(players_list):
    players_string = ""

    for player in players_list:
        player_string = player_row_template.format(id=player[0], last_name=player[1],
                                                   first_name=player[2], full_name=player[3],
                                                   is_active=player[4])
        players_string += player_string + ',\n'

    return players_string.rstrip(',\n')


def write_static_data_file(directory, file_contents):
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_name = 'data.py'
    f = open(os.path.join(os.getcwd(), directory, file_name), 'w')
    f.write(file_contents)
    f.close()


def generate_static_data_file(directory='static_files'):
    players_list = create_players_list()

    players_string = format_player_string(players_list)

    file_contents = file_template.format(players_list=players_string, date_updated=datetime.now().strftime('%b, %d %Y'))

    write_static_data_file(directory, file_contents)
