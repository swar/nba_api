import os
import shutil
from datetime import datetime

from nba_api.stats.endpoints.commonallplayers import CommonAllPlayers
from nba_api.stats.library.parameters import LeagueID, Season, WnbaSeason
from template import file_template, player_row_template

player_adjustments = {
    2775: ["Ha Seung-jin", "", "Ha Seung-jin", False],
    77036: ["Hoffman", "Paul 'The Bear'", "Paul 'The Bear' Hoffman", False],
    77510: ["McClain", "Ted 'Hound Dog'", "Ted 'Hound Dog' McClain", False],
    201180: ["Sun Yue", "", "Sun Yue", False],
}

wnba_player_adjustments = {}


def create_players_list(
    league_id=LeagueID.default,
    season=Season.default,
    player_adjustments=player_adjustments,
):
    all_players = CommonAllPlayers(league_id=league_id, season=season).get_dict()
    active_players = CommonAllPlayers(
        league_id=league_id, season=season, is_only_current_season=1
    ).get_dict()

    players_dict = {}
    for player in all_players["resultSets"][0]["rowSet"]:
        # Catch players with only a single name.
        try:
            last_name, first_name = player[1].split(", ")
        except ValueError:
            last_name = player[1]
            first_name = ""

        players_dict[player[0]] = [last_name, first_name, player[2], False]

    for player in active_players["resultSets"][0]["rowSet"]:
        players_dict[player[0]][-1] = True

    for player_id, player_data in player_adjustments.items():
        players_dict[player_id] = player_data

    return sorted(players_dict.items(), key=lambda kv: kv[1])


def format_player_string(players_list):
    players_string = ""

    for player in players_list:
        player_string = player_row_template.format(
            id=player[0],
            last_name=player[1][0],
            first_name=player[1][1],
            full_name=player[1][2],
            is_active=player[1][3],
        )
        players_string += player_string + ",\n"

    return players_string.rstrip(",\n")


def write_static_data_file(directory, file_contents) -> str:
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_name = "data.py"
    f = open(file_path := os.path.join(os.getcwd(), directory, file_name), "w")
    f.write(file_contents)
    f.close()
    return file_path


def generate_static_data_file(directory="static_files"):
    players_list = create_players_list()
    wnba_players_list = create_players_list(
        league_id=LeagueID.wnba,
        season=WnbaSeason.default,
        player_adjustments=wnba_player_adjustments,
    )

    players_string = format_player_string(players_list)
    wnba_players_string = format_player_string(wnba_players_list)

    file_contents = file_template.format(
        players_list=players_string,
        wnba_players_list=wnba_players_string,
        date_updated=datetime.now().strftime("%b, %d %Y"),
    )

    write_static_data_file(directory, file_contents)


if __name__ == "__main__":
    generate_static_data_file()
