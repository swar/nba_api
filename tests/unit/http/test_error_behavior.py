"""Characterization tests: the exceptions endpoints raise today, and when.

These tests pin CURRENT behavior on purpose, including behavior that looks wrong
(bare ``Exception``, ``KeyError`` from the constructor, non-2xx responses that load
without complaint). They exist so that a later change to the error model (typed
exceptions, an endpoint rewrite) can prove that every ``except`` clause users write
today still catches what it caught before.

Do not "fix" a test here to match new behavior. Change one only together with a
deliberate, documented behavior change (a ``CHANGELOG.MD`` entry users can read).

Each case asserts three things:

* the exact class (``type(exc) is X``),
* the builtin bases a user might catch (``ValueError``, ``KeyError``,
  ``RuntimeError``, ``requests.RequestException``, ``Exception``), and
* WHEN it raises: in the constructor (``get_request=True``, the default), in an
  explicit ``get_request()`` call, or only later on dataset access.

Everything is offline: ``requests.Session.get`` is replaced on a throwaway session,
and the proxy environment variables are cleared so an ambient ``NBA_API_PROXY``
can neither change nor leak into these results.
"""

import json
import re
from unittest.mock import MagicMock

import pytest
import requests

from nba_api.library.http import NBAHTTP
from nba_api.library.proxy import ProxyRequiredError
from nba_api.live.nba.endpoints import boxscore
from nba_api.live.nba.library.http import NBALiveHTTP
from nba_api.stats.endpoints import (
    boxscoretraditionalv3,
    commonplayerinfo,
    iststandings,
)
from nba_api.stats.library.http import NBAStatsHTTP
from nba_api.stats.static import players, teams

GAME_ID = "0022400001"

ENDPOINTS = {
    "stats-tabular": lambda **kw: commonplayerinfo.CommonPlayerInfo(
        player_id=2544, **kw
    ),
    "stats-v3": lambda **kw: boxscoretraditionalv3.BoxScoreTraditionalV3(
        game_id=GAME_ID, **kw
    ),
    "live": lambda **kw: boxscore.BoxScore(game_id=GAME_ID, **kw),
}

# Bases a caller might plausibly write in an ``except`` clause.
CATCHABLE = (
    ValueError,
    LookupError,
    KeyError,
    TypeError,
    AttributeError,
    RuntimeError,
    OSError,
    requests.RequestException,
    Exception,
)

HTML_BLOCK_PAGE = "<html><head><title>Access Denied</title></head><body></body></html>"
ERROR_MESSAGE_BODY = '{"Message":"An error has occurred."}'

TABULAR_OK = json.dumps(
    {
        "resource": "commonplayerinfo",
        "parameters": {"PlayerID": 2544},
        "resultSets": [
            {"name": name, "headers": ["A"], "rowSet": [[1]]}
            for name in ("CommonPlayerInfo", "PlayerHeadlineStats", "AvailableSeasons")
        ],
    }
)
LIVE_OK = json.dumps({"meta": {"code": 200}, "game": {"gameId": GAME_ID}})

PROXY_WITH_CREDS = "http://nbauser:s3cretpass@10.255.255.1:3128"


def _response(body, status=200, url="https://stats.nba.com/stats/x"):
    response = requests.Response()
    response.status_code = status
    response._content = body.encode("utf-8")
    response.encoding = "utf-8"
    response.url = url
    return response


def assert_catchable_as(exc, *expected):
    """``exc`` is an instance of exactly the ``expected`` members of CATCHABLE."""
    caught = {base for base in CATCHABLE if isinstance(exc, base)}
    assert caught == set(expected), {b.__name__ for b in caught}


@pytest.fixture(autouse=True)
def no_ambient_proxy(monkeypatch):
    monkeypatch.delenv("NBA_API_PROXY", raising=False)
    monkeypatch.delenv("NBA_API_REQUIRE_PROXY", raising=False)
    monkeypatch.setattr("nba_api.library.debug.debug.PROXY", "", raising=False)


@pytest.fixture
def session_get(monkeypatch):
    """The ``get`` of the session every endpoint will use, as a mock."""
    session = requests.Session()
    session.get = MagicMock(name="Session.get")
    monkeypatch.setattr(NBAHTTP, "get_session", classmethod(lambda cls: session))
    return session.get


# --- Bodies that are not JSON ------------------------------------------------

NON_JSON_BODIES = {
    "html-200": (HTML_BLOCK_PAGE, 200),
    "html-403": (HTML_BLOCK_PAGE, 403),
    "empty-200": ("", 200),
    "message-body-200": (ERROR_MESSAGE_BODY, 200),
    "message-body-500": (ERROR_MESSAGE_BODY, 500),
}


@pytest.mark.parametrize("endpoint", ENDPOINTS)
@pytest.mark.parametrize("body,status", NON_JSON_BODIES.values(), ids=NON_JSON_BODIES)
def test_non_json_body_raises_jsondecodeerror_in_constructor(
    session_get, endpoint, body, status
):
    session_get.return_value = _response(body, status)

    with pytest.raises(json.JSONDecodeError) as info:
        ENDPOINTS[endpoint]()

    assert type(info.value) is json.JSONDecodeError
    assert_catchable_as(info.value, ValueError, Exception)
    session_get.assert_called_once()


@pytest.mark.parametrize("endpoint", ENDPOINTS)
@pytest.mark.parametrize("body,status", NON_JSON_BODIES.values(), ids=NON_JSON_BODIES)
def test_non_json_body_with_get_request_false_raises_on_get_request(
    session_get, endpoint, body, status
):
    session_get.return_value = _response(body, status)
    instance = ENDPOINTS[endpoint](get_request=False)
    session_get.assert_not_called()

    with pytest.raises(json.JSONDecodeError):
        instance.get_request()

    # nba_response is assigned before parsing fails, so the raw body is still
    # reachable, but get_dict() raises the same error again.
    assert instance.get_response() is not None
    with pytest.raises(json.JSONDecodeError):
        instance.get_dict()


@pytest.mark.parametrize(
    "http_class", [NBAStatsHTTP, NBALiveHTTP], ids=["stats", "live"]
)
def test_message_body_is_rewritten_to_non_json(session_get, http_class):
    """The ``{"Message": ...}`` JSON body is replaced, so the original is lost."""
    session_get.return_value = _response(ERROR_MESSAGE_BODY)

    response = http_class().send_api_request(endpoint="x", parameters={})

    assert response.valid_json() is False
    assert response.get_response() == (
        "<Error><Message>An error has occurred.</Message></Error>"
    )


@pytest.mark.parametrize(
    "http_class", [NBAStatsHTTP, NBALiveHTTP], ids=["stats", "live"]
)
def test_send_api_request_returns_invalid_json_without_raising(session_get, http_class):
    session_get.return_value = _response(HTML_BLOCK_PAGE, 403)

    response = http_class().send_api_request(endpoint="x", parameters={})

    assert response.valid_json() is False
    assert response.get_response() == HTML_BLOCK_PAGE


def test_raise_exception_on_error_raises_bare_exception(session_get):
    """Opt-in flag no endpoint passes; it raises a bare ``Exception``."""
    session_get.return_value = _response(HTML_BLOCK_PAGE)

    with pytest.raises(Exception, match="InvalidResponse") as info:
        NBAStatsHTTP().send_api_request(
            endpoint="x", parameters={}, raise_exception_on_error=True
        )

    assert type(info.value) is Exception
    assert_catchable_as(info.value, Exception)


def test_base_http_class_raises_bare_exception(session_get):
    with pytest.raises(Exception, match="_HTTP class") as info:
        NBAHTTP().send_api_request(endpoint="x", parameters={})

    assert type(info.value) is Exception
    session_get.assert_not_called()


# --- Valid JSON without the expected datasets/keys ----------------------------


@pytest.mark.parametrize(
    "body,missing",
    [
        ("{}", "resultSet"),
        ('{"resultSets": []}', "AvailableSeasons"),
        ('{"resultSet": {}}', "AvailableSeasons"),
    ],
    ids=["no-result-sets", "empty-result-sets", "nameless-result-set"],
)
def test_tabular_missing_datasets_raise_keyerror_in_constructor(
    session_get, body, missing
):
    session_get.return_value = _response(body)

    with pytest.raises(KeyError) as info:
        ENDPOINTS["stats-tabular"]()

    assert type(info.value) is KeyError
    assert info.value.args == (missing,)
    assert_catchable_as(info.value, LookupError, KeyError, Exception)


@pytest.mark.parametrize(
    "body,exc_type",
    [("[]", TypeError), ("null", TypeError), ('{"resultSets": null}', TypeError)],
    ids=["list", "null", "null-result-sets"],
)
def test_tabular_wrong_json_shape_raises_typeerror(session_get, body, exc_type):
    session_get.return_value = _response(body)

    with pytest.raises(exc_type) as info:
        ENDPOINTS["stats-tabular"]()

    assert type(info.value) is exc_type
    assert_catchable_as(info.value, TypeError, Exception)


@pytest.mark.parametrize(
    "body",
    ["{}", '{"boxScoreTraditional": {}}', '{"resultSets": []}'],
    ids=["empty", "empty-boxscore", "tabular-shape"],
)
def test_v3_missing_keys_do_not_raise(session_get, body):
    """The V3 parser uses ``.get()`` throughout, so a wrong body loads as Nones."""
    session_get.return_value = _response(body)

    endpoint = ENDPOINTS["stats-v3"]()

    assert endpoint.player_stats.get_dict()["data"] == []
    team_rows = endpoint.team_stats.get_dict()["data"]
    assert len(team_rows) == 2
    assert all(value is None for row in team_rows for value in row)
    assert len(endpoint.get_data_frames()) == 3


@pytest.mark.parametrize(
    "body,exc_type",
    [("[]", AttributeError), ("null", AttributeError)],
    ids=["list", "null"],
)
def test_v3_wrong_json_shape_raises_attributeerror(session_get, body, exc_type):
    session_get.return_value = _response(body)

    with pytest.raises(exc_type) as info:
        ENDPOINTS["stats-v3"]()

    assert type(info.value) is exc_type
    assert_catchable_as(info.value, AttributeError, Exception)


def test_nested_parser_indexing_missing_key_raises_keyerror(session_get):
    """Some nested-JSON parsers index directly; ISTStandings is one of them."""
    session_get.return_value = _response("{}")

    with pytest.raises(KeyError) as info:
        iststandings.ISTStandings()

    assert type(info.value) is KeyError
    assert info.value.args == ("teams",)
    assert_catchable_as(info.value, LookupError, KeyError, Exception)


def test_live_missing_game_does_not_raise_and_leaves_none(session_get):
    session_get.return_value = _response("{}")

    endpoint = ENDPOINTS["live"]()

    assert endpoint.get_dict() == {}
    assert endpoint.game is None
    assert endpoint.home_team is None
    # The failure only shows up when the caller touches a dataset.
    with pytest.raises(AttributeError) as info:
        endpoint.game.get_dict()
    assert type(info.value) is AttributeError


def test_live_game_without_teams_does_not_raise(session_get):
    session_get.return_value = _response('{"game": {}}')

    endpoint = ENDPOINTS["live"]()

    assert endpoint.game.get_dict() == {}
    assert endpoint.game_details.get_dict() == {}
    assert endpoint.home_team is None
    assert endpoint.away_team_player_stats is None


def test_live_wrong_json_shape(session_get):
    session_get.return_value = _response("null")
    with pytest.raises(TypeError) as info:
        ENDPOINTS["live"]()
    assert type(info.value) is TypeError

    session_get.return_value = _response("[]")
    endpoint = ENDPOINTS["live"]()
    assert endpoint.game is None


# --- Non-2xx status with a parseable body -------------------------------------


@pytest.mark.parametrize("status", [400, 404, 429, 500, 503])
def test_tabular_non_2xx_with_valid_json_loads_without_raising(session_get, status):
    session_get.return_value = _response(TABULAR_OK, status)

    endpoint = ENDPOINTS["stats-tabular"]()

    assert endpoint.common_player_info.get_dict()["data"] == [[1]]


@pytest.mark.parametrize("status", [403, 404, 500])
def test_live_non_2xx_with_valid_json_loads_without_raising(session_get, status):
    session_get.return_value = _response(LIVE_OK, status)

    endpoint = ENDPOINTS["live"]()

    assert endpoint.game.get_dict() == {"gameId": GAME_ID}


# --- requests exceptions --------------------------------------------------------

REQUESTS_ERRORS = [
    requests.Timeout,
    requests.exceptions.ConnectTimeout,
    requests.exceptions.ReadTimeout,
    requests.ConnectionError,
    requests.exceptions.ProxyError,
    requests.exceptions.SSLError,
]


@pytest.mark.parametrize("endpoint", ENDPOINTS)
@pytest.mark.parametrize("error", REQUESTS_ERRORS, ids=lambda e: e.__name__)
def test_requests_errors_propagate_unchanged_from_constructor(
    session_get, endpoint, error
):
    session_get.side_effect = error("boom")

    with pytest.raises(error) as info:
        ENDPOINTS[endpoint]()

    assert type(info.value) is error
    # requests.RequestException subclasses OSError (IOError), not ValueError.
    assert_catchable_as(info.value, requests.RequestException, OSError, Exception)
    assert str(info.value) == "boom"


@pytest.mark.parametrize("endpoint", ENDPOINTS)
def test_requests_error_not_raised_until_get_request(session_get, endpoint):
    session_get.side_effect = requests.Timeout("boom")
    instance = ENDPOINTS[endpoint](get_request=False)

    with pytest.raises(requests.Timeout):
        instance.get_request()


def _proxy_failure(*args, **kwargs):
    """Mimic what requests raises when a credentialed proxy is unreachable."""
    proxy = kwargs["proxies"]["https"]
    inner = OSError(f"Failed to establish a new connection to {proxy}")
    raise requests.exceptions.ProxyError(
        "HTTPSConnectionPool(host='stats.nba.com', port=443): Max retries exceeded "
        f"(Caused by ProxyError('Unable to connect to proxy {proxy}'))"
    ) from inner


@pytest.mark.parametrize("endpoint", ENDPOINTS)
@pytest.mark.parametrize("source", ["argument", "env"])
def test_proxy_connection_error_keeps_type_and_redacts_credentials(
    session_get, monkeypatch, endpoint, source
):
    session_get.side_effect = _proxy_failure
    kwargs = {}
    if source == "env":
        monkeypatch.setenv("NBA_API_PROXY", PROXY_WITH_CREDS)
    else:
        kwargs["proxy"] = PROXY_WITH_CREDS

    with pytest.raises(requests.exceptions.ProxyError) as info:
        ENDPOINTS[endpoint](**kwargs)

    exc = info.value
    assert type(exc) is requests.exceptions.ProxyError
    assert isinstance(exc, requests.ConnectionError)
    assert_catchable_as(exc, requests.RequestException, OSError, Exception)
    # Redaction is the part users rely on: no credentials anywhere in the error.
    for text in (str(exc), repr(exc), *map(str, exc.args)):
        assert "s3cretpass" not in text
        assert "nbauser" not in text
    assert "***" in str(exc)
    # The chained urllib3-style cause (which embeds the proxy URL) is dropped.
    assert exc.__cause__ is None
    assert exc.__context__ is None


def test_proxy_error_without_credentials_is_not_rewritten(session_get):
    session_get.side_effect = _proxy_failure
    proxy = "http://10.255.255.1:3128"

    with pytest.raises(requests.exceptions.ProxyError) as info:
        ENDPOINTS["stats-tabular"](proxy=proxy)

    assert proxy in str(info.value)
    # send_api_request re-raises ``from None``, so the cause is dropped either way.
    assert info.value.__cause__ is None
    assert info.value.__suppress_context__ is True


# --- Proxy required but unset ---------------------------------------------------


@pytest.mark.parametrize("endpoint", ENDPOINTS)
@pytest.mark.parametrize("proxy", [None, ""], ids=["default", "explicit-empty"])
def test_proxy_required_but_unset_raises_before_any_request(
    session_get, monkeypatch, endpoint, proxy
):
    monkeypatch.setenv("NBA_API_REQUIRE_PROXY", "1")
    kwargs = {} if proxy is None else {"proxy": proxy}

    # Nothing happens until a request is attempted.
    instance = ENDPOINTS[endpoint](get_request=False, **kwargs)

    with pytest.raises(ProxyRequiredError) as info:
        instance.get_request()
    with pytest.raises(ProxyRequiredError):
        ENDPOINTS[endpoint](**kwargs)

    assert type(info.value) is ProxyRequiredError
    assert_catchable_as(info.value, RuntimeError, Exception)
    session_get.assert_not_called()


# --- Using an endpoint before any request -------------------------------------


def test_stats_endpoint_accessors_before_request(session_get):
    instance = ENDPOINTS["stats-tabular"](get_request=False)

    with pytest.raises(TypeError):
        instance.get_data_frames()  # data_sets is None
    with pytest.raises(AttributeError):
        instance.get_dict()  # nba_response is None
    # Dataset attributes are only created by load_response().
    assert not hasattr(instance, "common_player_info")


def test_live_endpoint_accessors_before_request(session_get):
    instance = ENDPOINTS["live"](get_request=False)

    with pytest.raises(AttributeError):
        instance.get_dict()
    assert instance.game is None


# --- Static lookups -----------------------------------------------------------


@pytest.mark.parametrize(
    "lookup,arg",
    [
        (players.find_player_by_id, 0),
        (players.find_wnba_player_by_id, 0),
        (teams.find_team_name_by_id, 0),
        (teams.find_team_by_abbreviation, "ZZZ"),
        (teams.find_wnba_team_by_abbreviation, "ZZZ"),
    ],
    ids=lambda v: getattr(v, "__name__", str(v)),
)
def test_static_single_lookup_not_found_returns_none(lookup, arg):
    assert lookup(arg) is None


@pytest.mark.parametrize(
    "lookup,arg",
    [
        (players.find_players_by_full_name, "no such player xyzzy"),
        (teams.find_teams_by_full_name, "no such team xyzzy"),
    ],
    ids=lambda v: getattr(v, "__name__", str(v)),
)
def test_static_search_not_found_returns_empty_list(lookup, arg):
    assert lookup(arg) == []


@pytest.mark.parametrize(
    "lookup,arg",
    [
        # The argument is interpolated into a regex, so these match many rows.
        (teams.find_team_by_abbreviation, "..."),
        (teams.find_team_name_by_id, ".*"),
    ],
    ids=lambda v: getattr(v, "__name__", str(v)),
)
def test_static_team_lookup_matching_many_raises_bare_exception(lookup, arg):
    with pytest.raises(Exception, match="Found more than 1 id") as info:
        lookup(arg)

    assert type(info.value) is Exception
    assert_catchable_as(info.value, Exception)


def test_static_player_duplicate_id_raises_bare_exception():
    row = players.players[0]
    with pytest.raises(Exception, match="Found more than 1 id") as info:
        players._find_player_by_id(row[0], players=[row, list(row)])

    assert type(info.value) is Exception


@pytest.mark.parametrize(
    "lookup",
    [
        players.find_players_by_full_name,
        players.find_players_by_last_name,
        teams.find_teams_by_full_name,
        teams.find_team_by_abbreviation,
    ],
    ids=lambda f: f.__name__,
)
def test_static_lookup_invalid_regex_raises_re_error(lookup):
    with pytest.raises(re.error) as info:
        lookup("(")

    assert type(info.value) is re.error
    assert_catchable_as(info.value, Exception)
