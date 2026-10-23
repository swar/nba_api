"""Schedule data must not depend on the position of response metadata."""

import json
from copy import deepcopy

import pytest
from pandas.testing import assert_frame_equal

from nba_api.stats.endpoints.scheduleleaguev2 import ScheduleLeagueV2
from nba_api.stats.endpoints.scheduleleaguev2int import ScheduleLeagueV2Int
from nba_api.stats.library.http import NBAStatsResponse

from .data.scheduleleaguev2 import (
    SCHEDULELEAGUEV2_2015_16,
    SCHEDULELEAGUEV2_2020_21,
)


def load_endpoint(endpoint_class, payload):
    endpoint = endpoint_class(get_request=False)
    endpoint.nba_response = NBAStatsResponse(
        json.dumps(payload), 200, "http://mock.url"
    )
    endpoint.load_response()
    return endpoint


@pytest.mark.parametrize("endpoint_class", [ScheduleLeagueV2, ScheduleLeagueV2Int])
@pytest.mark.parametrize(
    "payload",
    [SCHEDULELEAGUEV2_2015_16, SCHEDULELEAGUEV2_2020_21],
    ids=["empty-weeks", "populated-weeks"],
)
@pytest.mark.parametrize(
    "keys",
    [
        ("leagueSchedule", "meta"),
        ("leagueSchedule",),
        ("meta", "extra", "leagueSchedule"),
    ],
    ids=["schedule-first", "without-meta", "extra-metadata"],
)
def test_schedule_response_metadata_does_not_change_datasets(
    endpoint_class, payload, keys
):
    payload = deepcopy(payload)
    if endpoint_class is ScheduleLeagueV2Int:
        payload["leagueSchedule"]["broadcasterList"] = [
            {"broadcasterId": 1234, "broadcasterDisplay": "Bally Sports"}
        ]
    expected = load_endpoint(endpoint_class, payload)

    payload["extra"] = {"requestId": "schedule-test"}
    reordered = {key: payload[key] for key in keys}
    actual = load_endpoint(endpoint_class, reordered)

    assert [dataset.get_dict() for dataset in actual.data_sets] == [
        dataset.get_dict() for dataset in expected.data_sets
    ]
    assert actual.get_normalized_dict() == expected.get_normalized_dict()
    for actual_frame, expected_frame in zip(
        actual.get_data_frames(), expected.get_data_frames(), strict=True
    ):
        assert_frame_equal(actual_frame, expected_frame)
