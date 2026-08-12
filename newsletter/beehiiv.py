"""beehiiv Create Post API の薄いクライアント。

このエンドポイントは Max / Enterprise プラン限定なので、無料プランのあいだは
config.yaml の publish.mode を "local" にしておくこと（このモジュールは呼ばれない）。

  POST https://api.beehiiv.com/v2/publications/{publicationId}/posts
  https://developers.beehiiv.com/api-reference/posts/create
"""

from __future__ import annotations

import os
import sys
from typing import Any

import requests

API_ROOT = "https://api.beehiiv.com/v2"
TIMEOUT_SECONDS = 60


def _credentials(cfg: dict[str, Any]) -> tuple[str, str]:
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
    return api_key, publication_id


def verify(cfg: dict[str, Any]) -> None:
    """投稿せずに API 接続だけを確かめる。

    読み取り専用のエンドポイントを叩くだけなので、beehiiv 側に何も作らない。
    Max トライアル中に「本番で使えるか」を確認する用途を想定している。
    """
    api_key, publication_id = _credentials(cfg)
    response = requests.get(
        f"{API_ROOT}/publications/{publication_id}",
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=TIMEOUT_SECONDS,
    )

    if response.status_code == 401:
        raise RuntimeError("401: API キーが無効です。beehiiv 側で再発行してください。")
    if response.status_code == 404:
        raise RuntimeError(
            "404: Publication ID が違います。beehiiv の Settings で確認してください。"
        )
    if response.status_code == 403:
        raise RuntimeError(
            "403: このプランでは API を使えません。Max トライアルが切れている可能性があります。"
        )
    if response.status_code >= 400:
        raise RuntimeError(f"{response.status_code}: {response.text[:300]}")

    data = response.json().get("data", {})
    print("OK  beehiiv API に接続できました。")
    print(f"    publication: {data.get('name', '(名前不明)')}")
    print(f"    id:          {data.get('id', publication_id)}")
    print("\n    投稿 API が使えるかはプラン次第です。実際に下書きを作って確かめるには")
    print("    config.yaml の publish.mode を draft にして ingest.py を実行してください。")


if __name__ == "__main__":
    # python beehiiv.py --check
    import yaml
    from pathlib import Path

    if "--check" not in sys.argv:
        print("使い方: python beehiiv.py --check", file=sys.stderr)
        sys.exit(2)
    try:
        verify(yaml.safe_load((Path(__file__).parent / "config.yaml").read_text(encoding="utf-8")))
    except RuntimeError as exc:
        print(f"NG  {exc}", file=sys.stderr)
        sys.exit(1)


def publish(cfg: dict[str, Any], issue: dict[str, Any], status: str) -> str:
    """1 号を beehiiv に作成し、管理画面で確認できる URL を返す。

    status は "draft"（下書き）か "confirmed"（公開）。
    2026-08-06 以降、status を省略すると下書き扱いになる仕様変更が入ったため、
    ここでは常に明示的に送る。
    """
    if status not in ("draft", "confirmed"):
        raise RuntimeError(f"invalid publish.mode for beehiiv: {status!r}")

    settings = cfg["publish"]["beehiiv"]
    api_key, publication_id = _credentials(cfg)

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
