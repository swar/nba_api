import logging
import os
from datetime import datetime

from template import file_template, player_row_template

from nba_api.stats.endpoints.commonallplayers import CommonAllPlayers
from nba_api.stats.library.parameters import LeagueID, Season, WnbaSeason

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
log = logging.getLogger(__name__)

# Player adjustments format: {player_id: [last_name, first_name, full_name]}
# Note: is_active status is preserved from NBA API, not set here
player_adjustments = {
    # Asian naming convention (Family name, Given name)
    2775: ["Ha", "Seung-jin", "Ha Seung-jin"],  # Korean: 하승진
    201180: ["Sun", "Yue", "Sun Yue"],  # Chinese: 孙悦
    2397: ["Yao", "Ming", "Yao Ming"],  # Chinese: 姚明
    201146: ["Yi", "Jianlian", "Yi Jianlian"],  # Chinese: 易建联
    1627753: ["Zhou", "Qi", "Zhou Qi"],  # Chinese: 周琦
    # Players with nicknames in official name
    77036: ["Hoffman", "Paul 'The Bear'", "Paul 'The Bear' Hoffman"],
    77510: ["McClain", "Ted 'Hound Dog'", "Ted 'Hound Dog' McClain"],
}

wnba_player_adjustments = {}


def create_players_list(
    league_id=LeagueID.default,
    season=Season.default,
    player_adjustments=player_adjustments,
):
    log.info(f"Fetching players for league_id={league_id}, season={season}")

    log.debug("Fetching all players...")
    all_players = CommonAllPlayers(league_id=league_id, season=season).get_dict()

    log.debug("Fetching active players...")
    active_players = CommonAllPlayers(
        league_id=league_id, season=season, is_only_current_season=1
    ).get_dict()

    log.debug(f"All players response: {all_players}")

    players_dict = {}
    for player in all_players["resultSets"][0]["rowSet"]:
        # Catch players with only a single name.
        try:
            last_name, first_name = player[1].split(", ")
        except ValueError:
            last_name = player[1]
            first_name = ""
            log.warning(f"Player has single name: {player[1]} (ID: {player[0]})")

        players_dict[player[0]] = [last_name, first_name, player[2], False]

    log.info(f"Processed {len(players_dict)} total players")

    for player in active_players["resultSets"][0]["rowSet"]:
        players_dict[player[0]][-1] = True

    active_count = sum(1 for p in players_dict.values() if p[-1])
    log.info(f"Marked {active_count} players as active")

    if player_adjustments:
        log.info(f"Applying {len(player_adjustments)} player adjustments")
        for player_id, player_data in player_adjustments.items():
            # Preserve is_active status from NBA API when applying name adjustments
            is_active = players_dict.get(player_id, [None, None, None, False])[-1]
            players_dict[player_id] = player_data + [is_active]

    sorted_list = sorted(players_dict.items(), key=lambda kv: kv[1])
    log.info(f"Created sorted players list with {len(sorted_list)} players")
    return sorted_list


def format_player_string(players_list):
    log.info(f"Formatting {len(players_list)} players into string")
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

    result = players_string.rstrip(",\n")
    log.info(f"Generated player string with {len(result)} characters")
    return result


def write_static_data_file(directory, file_contents) -> str:
    log.info(f"Writing static data file to directory: {directory}")

    if not os.path.exists(directory):
        log.info(f"Creating directory: {directory}")
        os.makedirs(directory)

    file_name = "data.py"
    file_path = os.path.join(os.getcwd(), directory, file_name)

    log.info(f"Writing {len(file_contents)} characters to {file_path}")
    try:
        with open(file_path, "w") as f:
            f.write(file_contents)
        log.info(f"Successfully wrote static data file: {file_path}")
    except Exception as e:
        log.error(f"Failed to write static data file: {e}")
        raise

    return file_path


def generate_static_data_file(directory="static_files"):
    log.info("=" * 60)
    log.info("Starting static data file generation")
    log.info("=" * 60)

    try:
        log.info("Processing NBA players...")
        players_list = create_players_list()

        log.info("Processing WNBA players...")
        wnba_players_list = create_players_list(
            league_id=LeagueID.wnba,
            season=WnbaSeason.default,
            player_adjustments=wnba_player_adjustments,
        )

        log.info("Formatting NBA players string...")
        players_string = format_player_string(players_list)

        log.info("Formatting WNBA players string...")
        wnba_players_string = format_player_string(wnba_players_list)

        date_updated = datetime.now().strftime("%b, %d %Y")
        log.info(f"Generating file with date: {date_updated}")

        file_contents = file_template.format(
            players_list=players_string,
            wnba_players_list=wnba_players_string,
            date_updated=date_updated,
        )

        file_path = write_static_data_file(directory, file_contents)

        log.info("=" * 60)
        log.info("Static data file generation completed successfully")
        log.info(f"File written to: {file_path}")
        log.info("=" * 60)

    except Exception as e:
        log.error("=" * 60)
        log.error(f"Static data file generation FAILED: {e}")
        log.error("=" * 60)
        raise


if __name__ == "__main__":
    generate_static_data_file()
