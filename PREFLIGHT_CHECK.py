from __future__ import annotations

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FORBIDDEN_NAMES = {"__pycache__", "requirements(1).txt"}
errors: list[str] = []

for path in ROOT.rglob("*"):
    if path.name in FORBIDDEN_NAMES or path.suffix == ".pyc":
        errors.append(f"不要ファイル: {path.relative_to(ROOT)}")

for path in ROOT.rglob("*.py"):
    try:
        ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except Exception as exc:
        errors.append(f"構文エラー: {path.relative_to(ROOT)}: {exc}")

workflow_files = list((ROOT / ".github" / "workflows").glob("*.yml"))
if len(workflow_files) != 1:
    errors.append(f"ワークフロー数が1ではありません: {len(workflow_files)}")

if errors:
    print("PRE-FLIGHT FAILED")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print("PRE-FLIGHT OK")
