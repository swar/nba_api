import warnings
from unittest.mock import patch

import pytest
import requests

from nba_api.library.proxy import (
    ProxyRequiredError,
    as_proxies,
    redact,
    resolve_proxy,
)
from nba_api.stats.endpoints import assistleaders

URL = "socks5://user:s3cret@proxy.example:1080"


@pytest.fixture(autouse=True)
def clean_env(monkeypatch):
    monkeypatch.delenv("NBA_API_PROXY", raising=False)
    monkeypatch.delenv("NBA_API_REQUIRE_PROXY", raising=False)
    monkeypatch.setattr("nba_api.library.debug.debug.PROXY", "", raising=False)


def test_default_is_direct():
    assert resolve_proxy() is None


def test_env_var_is_read_at_call_time(monkeypatch):
    monkeypatch.setenv("NBA_API_PROXY", URL)
    assert resolve_proxy() == URL


def test_explicit_argument_beats_env(monkeypatch):
    monkeypatch.setenv("NBA_API_PROXY", URL)
    assert resolve_proxy("http://other:8080") == "http://other:8080"


@pytest.mark.parametrize("disabled", ["", False])
def test_empty_explicit_disables_env_proxy(monkeypatch, disabled):
    monkeypatch.setenv("NBA_API_PROXY", URL)
    assert resolve_proxy(disabled) is None


def test_list_picks_one():
    assert resolve_proxy(["http://a:1", "http://b:2"]) in {"http://a:1", "http://b:2"}


def test_legacy_debug_proxy_is_fallback_and_warns(monkeypatch):
    monkeypatch.setattr("nba_api.library.debug.debug.PROXY", URL)
    with pytest.warns(FutureWarning):
        assert resolve_proxy() == URL


def test_env_beats_legacy_without_warning(monkeypatch):
    monkeypatch.setattr("nba_api.library.debug.debug.PROXY", "http://legacy:1")
    monkeypatch.setenv("NBA_API_PROXY", URL)
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        assert resolve_proxy() == URL


@pytest.mark.parametrize("explicit", [None, "", False, []])
def test_require_proxy_raises_without_one(monkeypatch, explicit):
    monkeypatch.setenv("NBA_API_REQUIRE_PROXY", "1")
    with pytest.raises(ProxyRequiredError):
        resolve_proxy(explicit)


def test_require_proxy_satisfied_by_env(monkeypatch):
    monkeypatch.setenv("NBA_API_REQUIRE_PROXY", "true")
    monkeypatch.setenv("NBA_API_PROXY", URL)
    assert resolve_proxy() == URL


def test_require_proxy_blocks_request_before_any_socket(monkeypatch):
    monkeypatch.setenv("NBA_API_REQUIRE_PROXY", "1")
    with (
        patch.object(requests.Session, "get") as get,
        pytest.raises(ProxyRequiredError),
    ):
        assistleaders.AssistLeaders()
    get.assert_not_called()


def test_as_proxies():
    assert as_proxies(None) is None
    assert as_proxies(URL) == {"http": URL, "https": URL}


def test_redact_masks_userinfo_and_bare_password():
    text = f"Cannot connect to proxy {URL}; auth s3cret failed"
    out = redact(text, URL)
    assert "s3cret" not in out and "user:" not in out
    assert "proxy.example:1080" in out


def test_request_errors_do_not_leak_credentials(monkeypatch):
    monkeypatch.setenv("NBA_API_PROXY", URL)
    err = requests.exceptions.ProxyError(f"Unable to connect to proxy {URL}")
    with (
        patch.object(requests.Session, "get", side_effect=err),
        pytest.raises(requests.exceptions.ProxyError) as exc,
    ):
        assistleaders.AssistLeaders()
    assert "s3cret" not in str(exc.value)
    assert exc.value.__cause__ is None and exc.value.__suppress_context__


@pytest.mark.parametrize(
    "password", ["pa/ss", "pa@ss", "p%40ss", "p:a:s:s", "pa ss"], ids=repr
)
def test_redact_handles_awkward_passwords(password):
    url = f"http://user:{password}@proxy.example:8080"
    out = redact(f"failed via {url} (retry)", url)
    assert password not in out
    assert "proxy.example" in out and "user:" not in out


def test_redact_does_not_mangle_on_short_secret():
    out = redact("GET http://x", "http://u:p@h:1")
    assert out == "GET http://x"


def test_list_with_blank_entries_never_goes_direct(monkeypatch):
    monkeypatch.setenv("NBA_API_REQUIRE_PROXY", "1")
    for _ in range(50):
        assert resolve_proxy(["", None, " ", "http://a:1"]) == "http://a:1"
    with pytest.raises(ProxyRequiredError):
        resolve_proxy(["", " "])


def test_redaction_keeps_exception_type_and_request(monkeypatch):
    monkeypatch.setenv("NBA_API_PROXY", URL)
    req = requests.Request("GET", "https://stats.nba.com").prepare()
    err = requests.exceptions.ConnectTimeout(f"timeout via {URL}", request=req)
    with (
        patch.object(requests.Session, "get", side_effect=err),
        pytest.raises(requests.exceptions.ConnectTimeout) as exc,
    ):
        assistleaders.AssistLeaders()
    assert exc.value.request is req and "s3cret" not in str(exc.value)


def test_redact_leaves_unrelated_urls_alone_when_proxy_known():
    out = redact("GET https://x.com/?e=me@b.com via " + URL, URL)
    assert "e=me@b.com" in out and "s3cret" not in out


def test_errors_are_untouched_without_a_proxy(monkeypatch):
    monkeypatch.delenv("NBA_API_PROXY", raising=False)
    inner = RuntimeError("boom")
    err = requests.exceptions.ConnectionError(inner)
    with (
        patch.object(requests.Session, "get", side_effect=err),
        pytest.raises(requests.exceptions.ConnectionError) as exc,
    ):
        assistleaders.AssistLeaders()
    assert exc.value.args[0] is inner


def test_errors_without_credentials_in_message_keep_args_and_context(monkeypatch):
    monkeypatch.setenv("NBA_API_PROXY", URL)
    inner = RuntimeError("boom")
    err = requests.exceptions.ConnectionError(inner)
    with (
        patch.object(requests.Session, "get", side_effect=err),
        pytest.raises(requests.exceptions.ConnectionError) as exc,
    ):
        assistleaders.AssistLeaders()
    assert exc.value.args[0] is inner
