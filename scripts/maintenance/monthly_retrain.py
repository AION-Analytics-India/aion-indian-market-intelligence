#!/usr/bin/env python3
"""Controlled monthly classifier retraining orchestrator.

Default mode is dry-run and never changes model weights. Use --execute only
after a human approves the labeled JSONL and target training command.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_EXPORT = ROOT / "data" / "taxonomy_updates" / "accepted_rules_labeled.jsonl"
DEFAULT_ARCHIVE = ROOT / "data" / "model_archives" / "news_to_signal"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Prepare or execute monthly event-classifier retraining.")
    parser.add_argument("--execute", action="store_true", help="Actually invoke the training command.")
    parser.add_argument("--training-script", default=str(ROOT / "train_multitask.py"))
    parser.add_argument("--export-jsonl", default=str(DEFAULT_EXPORT))
    parser.add_argument("--archive-dir", default=str(DEFAULT_ARCHIVE))
    parser.add_argument("--model-dir", default=str(ROOT / "distribution" / "hf_model_aion_news_to_signal"))
    return parser.parse_args()


def run(cmd: list[str]) -> dict[str, str | int]:
    proc = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    return {
        "cmd": " ".join(cmd),
        "returncode": proc.returncode,
        "stdout": proc.stdout[-4000:],
        "stderr": proc.stderr[-4000:],
    }


def archive_model(model_dir: Path, archive_dir: Path) -> str | None:
    if not model_dir.exists():
        return None
    archive_dir.mkdir(parents=True, exist_ok=True)
    label = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    target = archive_dir / f"{model_dir.name}_{label}"
    if model_dir.is_dir():
        shutil.copytree(model_dir, target, dirs_exist_ok=False)
    else:
        shutil.copy2(model_dir, target)
    return str(target)


def main() -> None:
    args = parse_args()
    export_path = Path(args.export_jsonl)
    export_result = run(
        [
            sys.executable,
            str(ROOT / "scripts" / "maintenance" / "export_accepted_rules_jsonl.py"),
            "--output",
            str(export_path),
        ]
    )

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "mode": "execute" if args.execute else "dry_run",
        "export": export_result,
        "export_jsonl": str(export_path),
        "training_script": args.training_script,
        "model_dir": args.model_dir,
        "archive": None,
        "training": None,
    }

    if args.execute:
        payload["archive"] = archive_model(Path(args.model_dir), Path(args.archive_dir))
        payload["training"] = run([sys.executable, args.training_script])

    out = ROOT / "data" / "taxonomy_updates" / "monthly_retrain_last_run.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"output": str(out), "mode": payload["mode"]}, indent=2))


if __name__ == "__main__":
    main()
