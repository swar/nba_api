import pytest

from nba_api._core.client import Client
from nba_api._core.common.cache import ResponseCache


def test_client_cache_off_by_default():
    assert Client().cache is None


def test_client_cache_on_uses_default_size():
    assert Client(cache=True).cache.size == 128


def test_client_cache_size():
    assert Client(cache=True, cache_size=5).cache.size == 5


def test_cache_size_without_cache_raises():
    with pytest.raises(ValueError, match="cache=True"):
        Client(cache_size=5)


@pytest.mark.parametrize("cache", [1, "yes", None])
def test_cache_must_be_bool(cache):
    with pytest.raises(TypeError):
        Client(cache=cache)


@pytest.mark.parametrize("size", [0, -1, 1.5, True, "128"])
def test_bad_cache_size_raises(size):
    with pytest.raises(ValueError):
        ResponseCache(size)


def test_key_ignores_param_order():
    key = ResponseCache.key
    assert key("stats", "x", {"a": 1, "b": 2}) == key("stats", "x", {"b": 2, "a": 1})


def test_key_includes_site():
    key = ResponseCache.key
    assert key("stats", "x", {}) != key("live", "x", {})


def test_get_and_set():
    cache = ResponseCache()
    cache.set("k", "v")
    assert cache.get("k") == "v"
    assert cache.get("missing") is None


def test_drops_least_recently_used_when_full():
    cache = ResponseCache(size=2)
    cache.set("a", 1)
    cache.set("b", 2)
    cache.get("a")  # "b" is now least recently used
    cache.set("c", 3)
    assert cache.get("b") is None
    assert cache.get("a") == 1
    assert cache.get("c") == 3
    assert len(cache) == 2


def test_clear():
    cache = ResponseCache()
    cache.set("a", 1)
    cache.clear()
    assert len(cache) == 0
