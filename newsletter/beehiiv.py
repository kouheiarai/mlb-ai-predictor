"""beehiiv Create Post API の薄いクライアント。

このエンドポイントは Max / Enterprise プラン限定なので、無料プランのあいだは
config.yaml の publish.mode を "local" にしておくこと（このモジュールは呼ばれない）。

  POST https://api.beehiiv.com/v2/publications/{publicationId}/posts
  https://developers.beehiiv.com/api-reference/posts/create
"""

from __future__ import annotations

import os
from typing import Any

import requests

API_ROOT = "https://api.beehiiv.com/v2"
TIMEOUT_SECONDS = 60


def publish(cfg: dict[str, Any], issue: dict[str, Any], status: str) -> str:
    """1 号を beehiiv に作成し、管理画面で確認できる URL を返す。

    status は "draft"（下書き）か "confirmed"（公開）。
    2026-08-06 以降、status を省略すると下書き扱いになる仕様変更が入ったため、
    ここでは常に明示的に送る。
    """
    if status not in ("draft", "confirmed"):
        raise RuntimeError(f"invalid publish.mode for beehiiv: {status!r}")

    settings = cfg["publish"]["beehiiv"]
    api_key = os.environ.get(settings.get("api_key_env", "BEEHIIV_API_KEY"))
    publication_id = os.environ.get(
        settings.get("publication_id_env", "BEEHIIV_PUBLICATION_ID")
    )
    if not api_key or not publication_id:
        raise RuntimeError(
            "BEEHIIV_API_KEY / BEEHIIV_PUBLICATION_ID are not set. "
            "Set them, or put publish.mode back to 'local' in config.yaml."
        )

    payload: dict[str, Any] = {
        "title": issue["title"],
        "subtitle": issue["subtitle"],
        "body_content": issue["body_html"],
        "status": status,
    }
    if settings.get("content_tags"):
        payload["content_tags"] = list(settings["content_tags"])
    if status == "confirmed" and settings.get("scheduled_at"):
        payload["scheduled_at"] = settings["scheduled_at"]

    response = requests.post(
        f"{API_ROOT}/publications/{publication_id}/posts",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=TIMEOUT_SECONDS,
    )

    if response.status_code == 403:
        raise RuntimeError(
            "beehiiv returned 403. The Create post endpoint requires a Max or Enterprise "
            "plan — on the free tier keep publish.mode set to 'local'."
        )
    if response.status_code >= 400:
        raise RuntimeError(f"beehiiv returned {response.status_code}: {response.text[:500]}")

    # 作成は非同期で進むため、201 が返っても本文の反映には数秒かかることがある。
    data = response.json().get("data", {})
    return data.get("web_url") or data.get("id") or "(created — check the beehiiv dashboard)"
