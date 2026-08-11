"""gBizINFO REST API v2 client.

Endpoint and schema definitions were taken from the official OpenAPI document at
https://info.gbiz.go.jp/hojin/v3/api-docs (title: "GビズインフォREST API v2").

The API requires a token obtained by application at https://info.gbiz.go.jp/ .
Set it in the GBIZINFO_API_TOKEN environment variable.
"""

from __future__ import annotations

import os
import time
from datetime import date
from typing import Any, Iterator

import requests

BASE_URL = "https://info.gbiz.go.jp/hojin"
TOKEN_HEADER = "X-hojinInfo-api-token"

# updateInfo sub-resources that carry a dated, per-corporation event we can treat
# as a sales signal.  Each maps to the key holding the event list inside a
# HojinInfoForChildV2 object, and to the property naming that event's date.
EVENT_KINDS: dict[str, dict[str, str]] = {
    "subsidy": {"list_key": "subsidy", "date_field": "date_of_approval"},
    "procurement": {"list_key": "procurement", "date_field": "date_of_order"},
    "certification": {"list_key": "certification", "date_field": "date_of_approval"},
    "commendation": {"list_key": "commendation", "date_field": "date_of_commendation"},
}

# The public docs do not state a rate limit.  Community reports describe pausing
# after a few thousand requests, so we stay well clear with a polite fixed delay
# and back off hard whenever the server pushes back.
DEFAULT_MIN_INTERVAL = 1.0
MAX_RETRIES = 5


class GBizError(RuntimeError):
    """Raised when the API returns an unrecoverable error."""


class GBizClient:
    def __init__(
        self,
        token: str | None = None,
        min_interval: float = DEFAULT_MIN_INTERVAL,
        timeout: int = 60,
        session: requests.Session | None = None,
    ) -> None:
        self.token = token or os.environ.get("GBIZINFO_API_TOKEN", "")
        if not self.token:
            raise GBizError(
                "GBIZINFO_API_TOKEN is not set. Apply for a token at "
                "https://info.gbiz.go.jp/ and export it before running."
            )
        self.min_interval = min_interval
        self.timeout = timeout
        self.session = session or requests.Session()
        self._last_request_at = 0.0

    def _throttle(self) -> None:
        elapsed = time.monotonic() - self._last_request_at
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        self._last_request_at = time.monotonic()

    def get(self, path: str, params: dict[str, Any]) -> dict[str, Any] | None:
        """GET a gBizINFO path. Returns None when the API reports "no results".

        gBizINFO answers 404 for an empty result set rather than an empty list,
        so 404 is a normal outcome and not an error.
        """
        url = f"{BASE_URL}{path}"
        headers = {"Accept": "application/json", TOKEN_HEADER: self.token}

        for attempt in range(MAX_RETRIES):
            self._throttle()
            try:
                response = self.session.get(
                    url, params=params, headers=headers, timeout=self.timeout
                )
            except requests.RequestException as exc:
                if attempt == MAX_RETRIES - 1:
                    raise GBizError(f"request to {url} failed: {exc}") from exc
                time.sleep(2**attempt)
                continue

            if response.status_code == 200:
                return response.json()
            if response.status_code == 404:
                return None
            if response.status_code == 401:
                raise GBizError(
                    "gBizINFO rejected the token (401). Check GBIZINFO_API_TOKEN "
                    "and that the declared purpose covers this usage."
                )
            if response.status_code == 400:
                raise GBizError(f"bad request to {url}: {response.text[:300]}")
            # 429 / 5xx: back off and retry.
            if attempt == MAX_RETRIES - 1:
                raise GBizError(
                    f"{url} returned {response.status_code}: {response.text[:300]}"
                )
            time.sleep(2**attempt * 5)

        return None

    def iter_update_info(
        self,
        kind: str,
        start: date,
        end: date,
        with_metadata: bool = True,
        max_pages: int | None = None,
    ) -> Iterator[dict[str, Any]]:
        """Yield HojinInfoForChildV2 objects added/updated between start and end.

        Both bounds are inclusive and are sent in the yyyyMMdd form the API wants.
        """
        if kind not in EVENT_KINDS:
            raise GBizError(f"unknown event kind: {kind}")

        page = 1
        while True:
            payload = self.get(
                f"/v2/hojin/updateInfo/{kind}",
                {
                    "from": start.strftime("%Y%m%d"),
                    "to": end.strftime("%Y%m%d"),
                    "page": str(page),
                    "metadata_flg": "true" if with_metadata else "false",
                },
            )
            if payload is None:
                return

            for record in payload.get("hojin-infos") or []:
                yield record

            total_page = _to_int(payload.get("totalPage")) or 1
            if page >= total_page:
                return
            if max_pages is not None and page >= max_pages:
                return
            page += 1

    def count_update_info(self, kind: str, start: date, end: date) -> int | None:
        """Return totalCount for a period without walking every page."""
        payload = self.get(
            f"/v2/hojin/updateInfo/{kind}",
            {
                "from": start.strftime("%Y%m%d"),
                "to": end.strftime("%Y%m%d"),
                "page": "1",
                "metadata_flg": "false",
            },
        )
        if payload is None:
            return 0
        return _to_int(payload.get("totalCount"))


def _to_int(value: Any) -> int | None:
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return None
