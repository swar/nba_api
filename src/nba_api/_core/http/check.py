"""Turn bad replies into errors. Each rule matches what NBA.com was seen to send.

Verified against live requests on 2026-10-24:

- Bad enum value: 400 with JSON naming the fields, e.g. {"PerMode": ["Invalid parameters"]}.
- Wrong type or missing required parameter: 500 with an empty body.
- Unknown stats endpoint: an endless redirect loop.
- Missing live file (game doesn't exist or hasn't started): 403 with S3 AccessDenied XML.
- Blocks (from issues #672, #678, #696): Akamai HTML pages, sometimes with status 200.
"""

import json
import re

from nba_api._core.common.errors import (
    BlockedError,
    HTTPStatusError,
    InvalidResponseError,
    NotFoundError,
    ParameterError,
)

_BLOCK_MARKERS = (
    "unable to process your request",
    "you don't have permission to access",
    "<title>access denied</title>",
)
_REFERENCE = re.compile(r"Reference\s*(?:#|Number:?)\s*([0-9a-f.]+)", re.IGNORECASE)
# 1.x checks for this body too; not seen in the 2026-10-24 tests.
_NBA_ERROR_BODY = {"Message": "An error has occurred."}


def _snippet(text, limit=200):
    text = " ".join(text.split())
    return text if len(text) <= limit else text[:limit] + "..."


def _is_s3_access_denied(text):
    return text.lstrip().startswith("<?xml") and "<Code>AccessDenied</Code>" in text


def _is_block_page(text):
    lowered = text.lower()
    return any(marker in lowered for marker in _BLOCK_MARKERS)


def check(response):
    """Raise the matching NBAAPIError if ``response`` is not usable data."""
    status, text, where = response.status, response.text, response.url

    if 300 <= status < 400:
        raise NotFoundError(
            f"{response.site} redirected the request for {response.endpoint!r} "
            f"({status}); the endpoint probably doesn't exist. URL: {where}",
            response,
        )

    if _is_s3_access_denied(text):
        raise NotFoundError(
            f"No live data at {where} ({status}). The game doesn't exist, hasn't "
            "started, or is older than 2019-20 (live data starts then; use the "
            "stats endpoints for older games).",
            response,
        )

    if _is_block_page(text):
        reference = _REFERENCE.search(text)
        ref = f" Akamai reference: {reference.group(1)}." if reference else ""
        raise BlockedError(
            f"NBA blocked the request ({status}); this is not a bug in nba_api. "
            "NBA.com often blocks cloud and data-center IPs and rapid requests: try "
            f"a proxy or slow down.{ref} URL: {where}",
            response,
        )

    if status == 400:
        fields = {}
        try:
            body = json.loads(text)
            if isinstance(body, dict):
                fields = body
        except ValueError:
            pass
        detail = (
            ", ".join(
                f"{name} ({'; '.join(map(str, msgs)) if isinstance(msgs, list) else msgs})"
                for name, msgs in fields.items()
            )
            or _snippet(text)
            or "no details given"
        )
        raise ParameterError(
            f"NBA rejected the parameters: {detail}. URL: {where}", response, fields
        )

    if status != 200:
        if status == 500 and not text.strip():
            hint = " NBA sends an empty 500 for a bad or missing parameter."
        else:
            hint = f" Body: {_snippet(text)}" if text.strip() else ""
        raise HTTPStatusError(f"NBA replied {status}.{hint} URL: {where}", response)

    try:
        body = json.loads(text)
    except ValueError:
        raise InvalidResponseError(
            f"NBA replied 200 but the body isn't JSON: {_snippet(text) or '(empty)'} "
            f"URL: {where}",
            response,
        ) from None
    if body == _NBA_ERROR_BODY:
        raise InvalidResponseError(
            f"NBA replied with its generic error message. URL: {where}", response
        )
