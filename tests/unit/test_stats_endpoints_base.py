import pytest
from pandas import DataFrame
from nba_api.stats.endpoints._base import Endpoint


def test_headers_not_present():
    data = {"some_key": "some_value"}  # No 'headers' key
    instance = Endpoint.DataSet(data)
    result = instance.get_data_frame()
    assert isinstance(result, DataFrame)
    assert result.empty


def test_headers_empty():
    data = {"headers": [], "name": "Test", "rowSet": []}  # Empty 'headers' key
    instance = Endpoint.DataSet(data)
    result = instance.get_data_frame()
    assert isinstance(result, DataFrame)
    assert result.empty


def test_headers_present_and_nonempty():
    data = {"headers": ["GAME_ID", "LEAG_TIX"], "data": [], }
    instance = Endpoint.DataSet(data)
    result = instance.get_data_frame()
    assert isinstance(result, DataFrame)
    assert result.empty
    assert list(result.columns) == ["GAME_ID", "LEAG_TIX"]
