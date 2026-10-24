import pytest

from nba_api._core.client import Client

SECRET_PROXY = "http://user:hunter2@proxy.example:8080"


def test_defaults():
    client = Client()
    assert client.proxy is None
    assert client.headers == {}
    assert client.timeout == 30


@pytest.mark.parametrize(
    "proxy", [None, False, "", SECRET_PROXY, [SECRET_PROXY, "http://b:1"]]
)
def test_valid_proxy(proxy):
    assert Client(proxy=proxy).proxy == proxy


@pytest.mark.parametrize(
    "proxy", [True, 8080, {"http": SECRET_PROXY}, [SECRET_PROXY, 1]]
)
def test_invalid_proxy_raises(proxy):
    with pytest.raises(TypeError):
        Client(proxy=proxy)


def test_proxy_list_is_copied():
    proxies = [SECRET_PROXY]
    client = Client(proxy=proxies)
    proxies.append("http://other:1")
    assert client.proxy == [SECRET_PROXY]


@pytest.mark.parametrize("proxy", [SECRET_PROXY, [SECRET_PROXY]])
def test_repr_hides_proxy(proxy):
    text = repr(Client(proxy=proxy))
    assert "hunter2" not in text
    assert "proxy='***'" in text


def test_repr():
    assert repr(Client(timeout=10, cache=True, cache_size=5)) == (
        "Client(proxy=None, timeout=10, cache=True, cache_size=5)"
    )


def test_headers_merge_over_defaults():
    client = Client(headers={"User-Agent": "mine", "X-Extra": "1"})
    merged = client.merge_headers({"User-Agent": "default", "Accept": "json"})
    assert merged == {"User-Agent": "mine", "Accept": "json", "X-Extra": "1"}


def test_header_none_removes_default():
    client = Client(headers={"Accept": None})
    assert client.merge_headers({"Accept": "json", "Host": "x"}) == {"Host": "x"}


def test_headers_are_copied():
    headers = {"A": "1"}
    client = Client(headers=headers)
    headers["B"] = "2"
    assert client.headers == {"A": "1"}


@pytest.mark.parametrize("headers", [[("A", "1")], {"A": 1}, {1: "a"}])
def test_invalid_headers_raise(headers):
    with pytest.raises(TypeError):
        Client(headers=headers)


@pytest.mark.parametrize("timeout", [1, 0.5, (3, 30), (3.0, 27.5)])
def test_valid_timeout(timeout):
    assert Client(timeout=timeout).timeout == timeout


@pytest.mark.parametrize(
    "timeout", [None, 0, -1, True, "30", (3,), (3, None), (3, 0), [3, 30]]
)
def test_invalid_timeout_raises(timeout):
    with pytest.raises(ValueError):
        Client(timeout=timeout)


def test_each_client_has_its_own_session():
    assert Client().session is not Client().session


def test_context_manager_closes_session(monkeypatch):
    client = Client()
    closed = []
    monkeypatch.setattr(client.session, "close", lambda: closed.append(True))
    with client as entered:
        assert entered is client
    assert closed == [True]
