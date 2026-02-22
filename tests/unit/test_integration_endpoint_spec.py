import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tests.integration.helpers.constants import GAME_ID, PLAYER_ID  # noqa: E402
from tests.integration.helpers.models import EndpointSpec  # noqa: E402


class DemoEndpoint:
    def __init__(
        self,
        game_id,
        player_id,
        season="default-season",
        proxy=None,
        headers=None,
        timeout=30,
        get_request=True,
    ):
        self.game_id = game_id
        self.player_id = player_id
        self.season = season
        self.proxy = proxy
        self.headers = headers
        self.timeout = timeout
        self.get_request = get_request


class CustomRequiredEndpoint:
    def __init__(self, game_id, custom_required):
        self.game_id = game_id
        self.custom_required = custom_required


def test_endpoint_spec_auto_resolves_required_params():
    endpoint = EndpointSpec(DemoEndpoint)()

    assert endpoint.game_id == GAME_ID
    assert endpoint.player_id == PLAYER_ID
    assert endpoint.season == "default-season"


def test_endpoint_spec_overrides_win_for_required_and_optional_params():
    endpoint = EndpointSpec(
        DemoEndpoint,
        game_id="0022300001",
        player_id="201939",
        season="2023-24",
    )()

    assert endpoint.game_id == "0022300001"
    assert endpoint.player_id == "201939"
    assert endpoint.season == "2023-24"


def test_endpoint_spec_raises_clear_error_for_unresolvable_required_params():
    spec = EndpointSpec(CustomRequiredEndpoint)

    with pytest.raises(ValueError) as exc_info:
        spec()

    message = str(exc_info.value)
    assert "CustomRequiredEndpoint" in message
    assert "custom_required" in message
    assert "PARAM_DEFAULTS" in message


def test_endpoint_spec_accepts_override_for_non_default_required_param():
    endpoint = EndpointSpec(CustomRequiredEndpoint, custom_required="ok")()

    assert endpoint.game_id == GAME_ID
    assert endpoint.custom_required == "ok"


def test_endpoint_spec_exposes_deprecation_reason():
    spec = EndpointSpec(DemoEndpoint, deprecated="Removed from API")

    assert spec.deprecated == "Removed from API"
