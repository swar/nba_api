import datetime
import time

import pytest

from nba_api.stats.endpoints import PlayByPlay, ScoreboardV2
from nba_api.stats.library.eventmsgtype import EventMsgType
from nba_api.stats.library.parameters import LeagueID
from nba_api.stats.library.playbyplayregex import eventmsgtype_to_re

# TODO: Re-enable this file once PlayByPlayV3 is set up for normalization.
pytest.skip(
    "PlayByPlay endpoint is likely deprecated in favor of PlayByPlayV3; skipping entire file for now. Fix later by "
    "updating to PlayByPlayV3 and ensuring normalization is working correctly.",
    allow_module_level=True,
)


pytestmark = [pytest.mark.live]


def pytest_generate_tests(metafunc):
    if "game" in metafunc.fixturenames and "play" in metafunc.fixturenames:
        metafunc.parametrize(
            "game, play",
            [
                (game_id, play_by_play)
                for game_id in get_game_ids()
                for play_by_play in get_play_by_play(game_id)
            ],
        )


def get_game_ids():
    gamefinder = ScoreboardV2(
        league_id=LeagueID.nba, day_offset=-1, game_date=datetime.datetime.now()
    )

    games_dict = gamefinder.get_normalized_dict()
    games = []
    for game in games_dict["GameHeader"]:
        games.append(game["GAME_ID"])

    return games


def get_play_by_play(game_id):
    # Delay briefly to prevent throttling
    time.sleep(0.600)
    return PlayByPlay(game_id).get_normalized_dict()["PlayByPlay"]


@pytest.fixture()
def game(request):
    return request.param


@pytest.fixture()
def play(request):
    return request.param


def test_play(game, play):
    for count in range(0, 1):
        dict_patterns = eventmsgtype_to_re[EventMsgType(play["EVENTMSGTYPE"])]
        description = (
            play["HOMEDESCRIPTION"] if count == 0 else play["VISITORDESCRIPTION"]
        )

        # Validate description
        if description is not None:
            match = False
            for pattern in dict_patterns:
                if pattern.match(description):
                    match = True

            if not match:
                msg = "EVENTMSGTYPE {eventmsgtype}: [{description}]\n\tAttempted Patterns\n".format(
                    eventmsgtype=play["EVENTMSGTYPE"], description=description
                )
                for pattern in dict_patterns:
                    msg += f"\t\t{pattern.pattern}\n"

                raise AssertionError(msg)
