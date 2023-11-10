import warnings
from nba_api.stats.library.eventmsgtype import EventMsgType


def test_eventmsgtype():
    with warnings.catch_warnings(record=True) as w:
        # Invoke Deprecation Warning
        _ = EventMsgType.UNKNOWN

        assert len(w) == 1

        assert issubclass(w[0].category, DeprecationWarning)
        assert (
            str(w[0].message)
            == "'UNKNOWN' member is deprecated; use 'INSTANT_REPLAY' instead."
        )
