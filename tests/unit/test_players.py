import pytest

from nba_api.stats.static import players

testcases_fullname = [
    # 1. Specific accented names from dataset (regex)
    r"^Luka Dončić$",
    r"^Nikola [JV]ović$",
    r"^[NK]ikola [TJ]o[kp]ić$",
    r"^Sim[oó]ne Fontecchio$",
    r"^[VN]latko Čančar$",
    r"(Luka Dončić|Nikola Jokić)",
    r"^(Pau|Paul)l [GS]i(l|)geous(-Alexander)?",
    r"^[BbPp]ogdan [Bb]ogdanović",
    r"^(Olivier-Maxence|O-M) Prosper$",
    # 2. String names
    "Luka Dončić",
    "Nikola Jokić",
    "Vlatko Čančar",
    "Simone Fontecchio",
    "Dario Šarić",
    "LUKA DONCIC",  # No accents, uppercase
    "luka doncic",  # No accents, lowercase
    "Dončić, Luka",  # Reversed order
    "Armel Traore",
    "Tidjane Salaun",
    "Olivier-Maxence Prosper",
    "O-M Prosper",
    "Nikola Topic",
    "Luka Donci",
    "Dario Saric",
    "Bogdan Bogdanovic",
    " Nikola Jokić ",  # Extra whitespace
    "NIKOLA JOKIĆ",  # Uppercase with accent
    "Jonas valanćiunaŠ",  # wrong accents - should be Valančiūnas
]
testcases_firstname = [
    r"^Luka",
    r"^Nikola",
    r"^[NK]ikola",
    r"^Sim[oó]ne",
    r"^[VN]latko",
    r"(Luka|Nikola)",
    r"^(Pau|Paul)l",
    r"^[BbPp]ogdan",
    r"^(Olivier-Maxence|O-M)",
    "Luka",
    "Nikola",
    "Vlatko",
    "Simone",
    "Dario",
    "LUKA",
    "luka",
    "Armel",
    "Tidjane",
    "Olivier-Maxence",
    "O-M",
    "Bogdan",
    " Nikola ",
    "NIKOLA",
    "Jonas",
    "Jose",
    "José",
    "Nicolás",
    "Nicolas",
    "Élie",
    "Elie",
    "Maozinha",
]
testcases_lastname = [
    r"^Dončić",
    r"^[JV]ović",
    r"^[TJ]o[kp]ić$",
    r"^Fontecchio",
    r"^Čančar",
    r"^(Dončić|Jokić)$",
    r"^[GS]i(l|)geous(-Alexander)?",
    r"^[Bb]ogdanović",
    r"^Prosper$",
    "Dončić",
    "Jokić",
    "Jokic",
    "Čančar",
    "Fontecchio",
    "Šarić",
    "Saric",
    "DONCIC",
    "doncic",
    "Traore",
    "Salaun",
    "Čančar",
    "Valanciunas",
    "Prosper",
    "Donci",
    "Bogdanovic",
    " Jokić ",
    "JOKIĆ",
    "valanćiunaŠ",
]


@pytest.mark.parametrize("fullname", testcases_fullname)
def test_findbyfullname(fullname):
    result = players.find_players_by_full_name(fullname)
    print(
        f"Result of find_players_by_full_name('{fullname}'), n={len(result)}: {result}"
    )


@pytest.mark.parametrize("firstname", testcases_firstname)
def test_findbyfirstname(firstname):
    result = players.find_players_by_first_name(firstname)
    print(
        f"Result of find_players_by_full_name('{firstname}'), n={len(result)}: {result}"
    )


@pytest.mark.parametrize("lastname", testcases_lastname)
def test_findbylastname(lastname):
    result = players.find_players_by_last_name(lastname)
    print(
        f"Result of find_players_by_full_name('{lastname}'), n={len(result)}: {result}"
    )
