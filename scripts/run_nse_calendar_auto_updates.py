#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import subprocess
import sys
import tomllib
from pathlib import Path
from typing import Any

from aion_indian_market_calendar.live_overrides import (
    apply_holiday_date_change,
    contains_ambiguous_session_wording,
    evaluate_nse_circular,
    extract_dates_from_text,
    extract_source_text,
    is_official_nse_source,
    list_active_generated_overrides,
    match_known_holiday_names,
    refresh_live_manifest,
    revoke_generated_override,
)

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from poll_nse_rss import fetch_and_filter, write_json_queue, write_review_queue


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LIVE_PATH = ROOT / "live_events.json"
DEFAULT_MANIFEST_PATH = ROOT / "live_events.manifest.json"
DEFAULT_STATE_PATH = ROOT / "data" / "nse_circulars" / "calendar_auto_state.json"
DEFAULT_REVIEW_PATH = ROOT / "ops" / "review_queue" / "latest.md"
DEFAULT_JSON_PATH = ROOT / "ops" / "review_queue" / "latest_calendar_candidates.json"
DEFAULT_DECISION_PATH = ROOT / "ops" / "review_queue" / "latest_calendar_decisions.json"
DEFAULT_RELEASE_CANDIDATE_PATH = (
    ROOT / "publish_assets" / "aion-indian-market-calendar" / "staging" / "release_candidate.json"
)
DEFAULT_SIGNING_KEY_ENV = "AION_CALENDAR_MANIFEST_SIGNING_KEY"
RELEASE_MANIFEST_PATH = ROOT / "publish_assets" / "releases" / "release_manifest.json"
PACKAGE_PYPROJECT_PATH = ROOT / "aion_indian_market_calendar" / "pyproject.toml"
PROJECT_ID = "aion-indian-market-calendar"
VALIDATION_COMMAND = [
    str(ROOT / "venv" / "bin" / "python"),
    "-m",
    "pytest",
    "aion_indian_market_calendar/tests/test_live_overrides.py",
    "aion_indian_market_calendar/tests/test_calendar.py",
    "-q",
]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Autonomously apply deterministic NSE circular holiday-date updates."
    )
    parser.add_argument("--lookback-hours", type=int, default=6, help="RSS lookback window.")
    parser.add_argument("--year", type=int, default=2026, help="Bundled calendar year.")
    parser.add_argument("--live-path", default=str(DEFAULT_LIVE_PATH), help="Path to live_events.json.")
    parser.add_argument(
        "--manifest-path",
        default=str(DEFAULT_MANIFEST_PATH),
        help="Path to signed live-events manifest.",
    )
    parser.add_argument("--state-path", default=str(DEFAULT_STATE_PATH), help="Path to scheduler state JSON.")
    parser.add_argument("--review-path", default=str(DEFAULT_REVIEW_PATH), help="Path to Markdown review queue.")
    parser.add_argument("--json-path", default=str(DEFAULT_JSON_PATH), help="Path to raw candidate JSON queue.")
    parser.add_argument(
        "--decision-path",
        default=str(DEFAULT_DECISION_PATH),
        help="Path to evaluation/audit JSON output.",
    )
    parser.add_argument(
        "--release-candidate-path",
        default=str(DEFAULT_RELEASE_CANDIDATE_PATH),
        help="Path to staged release-candidate JSON.",
    )
    parser.add_argument(
        "--confidence-threshold",
        type=float,
        default=0.9,
        help="Required parser confidence for autonomous mutation.",
    )
    parser.add_argument(
        "--rollback-failure-threshold",
        type=int,
        default=2,
        help="Consecutive failed revalidations required before rollback.",
    )
    parser.add_argument(
        "--release-cooldown-hours",
        type=int,
        default=24,
        help="Minimum time between published wheel snapshots for auto-publish eligibility.",
    )
    parser.add_argument(
        "--stability-window-hours",
        type=int,
        default=24,
        help="Time a live delta should remain stable before a wheel snapshot is considered publish-ready.",
    )
    parser.add_argument(
        "--signing-key-env",
        default=DEFAULT_SIGNING_KEY_ENV,
        help="Environment variable holding the HMAC key used for manifest signing.",
    )
    parser.add_argument("--max-items", type=int, default=20, help="Maximum candidate circulars to evaluate.")
    parser.add_argument("--dry-run", action="store_true", help="Evaluate only; do not mutate live files.")
    return parser


def load_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"last_run_at": None, "items": {}, "overrides": {}}
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("state payload must be a JSON object")
    return {
        "last_run_at": payload.get("last_run_at"),
        "items": dict(payload.get("items") or {}),
        "overrides": dict(payload.get("overrides") or {}),
    }


def save_state(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def run_validation_suite() -> dict[str, Any]:
    result = subprocess.run(
        VALIDATION_COMMAND,
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    return {
        "ok": result.returncode == 0,
        "returncode": result.returncode,
        "command": VALIDATION_COMMAND,
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip(),
    }


def load_current_package_version() -> str:
    payload = tomllib.loads(PACKAGE_PYPROJECT_PATH.read_text(encoding="utf-8"))
    return str(payload["project"]["version"])


def increment_patch_version(version: str) -> str:
    parts = version.split(".")
    if len(parts) != 3 or not all(part.isdigit() for part in parts):
        return f"{version}.post1"
    major, minor, patch = (int(part) for part in parts)
    return f"{major}.{minor}.{patch + 1}"


def latest_release_dt(project_id: str) -> dt.datetime | None:
    manifest = json.loads(RELEASE_MANIFEST_PATH.read_text(encoding="utf-8"))
    dates = [
        dt.datetime.fromisoformat(item["published_at"])
        for item in manifest.get("releases", [])
        if item.get("project_id") == project_id
    ]
    return max(dates) if dates else None


def stage_release_candidate(
    *,
    path: Path,
    live_path: Path,
    manifest_path: Path,
    changes: list[dict[str, Any]],
    validation_result: dict[str, Any],
    confidence_threshold: float,
    release_cooldown_hours: int,
    stability_window_hours: int,
) -> dict[str, Any]:
    current_version = load_current_package_version()
    proposed_version = increment_patch_version(current_version)
    live_payload = json.loads(live_path.read_text(encoding="utf-8"))
    manifest_payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    latest_published = latest_release_dt(PROJECT_ID)
    now_utc = dt.datetime.now(dt.timezone.utc)
    cooldown_cutoff = now_utc - dt.timedelta(hours=release_cooldown_hours)
    previous_release_older_than_cooldown = bool(latest_published is None or latest_published.astimezone(dt.timezone.utc) <= cooldown_cutoff)

    if latest_published is not None:
        earliest_publish_at = max(
            now_utc + dt.timedelta(hours=stability_window_hours),
            latest_published.astimezone(dt.timezone.utc) + dt.timedelta(hours=release_cooldown_hours),
        )
    else:
        earliest_publish_at = now_utc + dt.timedelta(hours=stability_window_hours)

    parser_confidence_high = all(
        change.get("kind") != "apply" or float(change.get("confidence") or 0.0) >= confidence_threshold
        for change in changes
    )
    structured_diff_valid = all(
        (
            change.get("kind") == "rollback" and int(change.get("revoked_event_count") or 0) > 0
        )
        or (
            change.get("kind") == "apply" and int(change.get("moved_event_count") or 0) > 0
        )
        for change in changes
    )
    no_ambiguous_wording = all(bool(change.get("no_ambiguous_session_wording", True)) for change in changes)
    release_manifest_generated = manifest_path.exists() and bool(manifest_payload.get("payload_sha256"))
    secondary_confirmation_count = max(int(change.get("secondary_confirmation_count") or 1) for change in changes)
    existing_candidate = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    duplicate_release_not_already_generated = (
        existing_candidate.get("live_manifest_sha256") != manifest_payload.get("payload_sha256")
        or existing_candidate.get("proposed_version") != proposed_version
    )

    auto_publish_conditions = {
        "parser_confidence_high": parser_confidence_high,
        "structured_diff_valid": structured_diff_valid,
        "no_ambiguous_wording": no_ambiguous_wording,
        "tests_passed": bool(validation_result.get("ok")),
        "previous_release_older_than_cooldown": previous_release_older_than_cooldown,
        "duplicate_release_not_already_generated": duplicate_release_not_already_generated,
        "release_manifest_generated": release_manifest_generated,
        "secondary_confirmation_count": secondary_confirmation_count,
    }
    auto_publish_ready = (
        auto_publish_conditions["parser_confidence_high"]
        and auto_publish_conditions["structured_diff_valid"]
        and auto_publish_conditions["no_ambiguous_wording"]
        and auto_publish_conditions["tests_passed"]
        and auto_publish_conditions["previous_release_older_than_cooldown"]
        and auto_publish_conditions["duplicate_release_not_already_generated"]
        and auto_publish_conditions["release_manifest_generated"]
        and secondary_confirmation_count >= 2
    )

    candidate = {
        "generated_at": now_utc.isoformat(),
        "project_id": PROJECT_ID,
        "baseline_package_version": current_version,
        "proposed_version": proposed_version,
        "live_payload_version": live_payload.get("version"),
        "live_manifest_sha256": manifest_payload.get("payload_sha256"),
        "live_manifest_signature": manifest_payload.get("signature"),
        "changes": changes,
        "validation": validation_result,
        "stability_window_hours": stability_window_hours,
        "release_cooldown_hours": release_cooldown_hours,
        "latest_published_at": latest_published.isoformat() if latest_published else None,
        "earliest_publish_at": earliest_publish_at.isoformat(),
        "auto_publish_conditions": auto_publish_conditions,
        "auto_publish_ready": auto_publish_ready,
        "policy": {
            "wheel_role": "stable snapshot",
            "live_delta_role": "operational truth",
            "autonomous_pypi_publish": "disabled unless all readiness gates pass",
        },
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(candidate, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    return candidate


def revalidate_active_overrides(
    *,
    live_path: Path,
    manifest_path: Path,
    signing_key: str,
    state_overrides: dict[str, Any],
    year: int,
    confidence_threshold: float,
    rollback_failure_threshold: int,
    dry_run: bool,
) -> tuple[list[dict[str, Any]], int, list[dict[str, Any]]]:
    decisions: list[dict[str, Any]] = []
    changes: list[dict[str, Any]] = []
    rollback_count = 0

    for override in list_active_generated_overrides(live_path):
        key = str(override.get("source_hash") or override.get("holiday_name") or "")
        holiday_name = str(override.get("holiday_name") or "")
        source_url = str(override.get("source_url") or "")
        source_title = str(override.get("source_title") or "")
        source_published = str(override.get("source_published") or "")
        active_date_text = str(override.get("active_date") or "")
        active_date = dt.date.fromisoformat(active_date_text) if active_date_text else None
        previous = dict(state_overrides.get(key) or {})

        official_source = is_official_nse_source(source_url)
        source_fetch_error = None
        source_text = ""
        try:
            if official_source and source_url:
                source_text = extract_source_text(source_url)
        except Exception as exc:
            source_fetch_error = f"{type(exc).__name__}: {exc}"

        combined_text = "\n".join(part for part in (source_title, source_text) if part)
        matched_holidays = list(dict.fromkeys(match_known_holiday_names(combined_text, year=year)))
        extracted_dates = [item.isoformat() for item in extract_dates_from_text(combined_text)]
        includes_target_date = bool(active_date and active_date.isoformat() in extracted_dates)
        single_holiday_name = len(matched_holidays) == 1 and matched_holidays[0].lower() == holiday_name.lower()
        no_ambiguous_session_wording = not contains_ambiguous_session_wording(combined_text)
        confidence = round(
            (0.30 if official_source else 0.0)
            + (0.25 if single_holiday_name else 0.0)
            + (0.25 if includes_target_date else 0.0)
            + (0.20 if no_ambiguous_session_wording else 0.0),
            3,
        )
        still_valid = (
            official_source
            and single_holiday_name
            and includes_target_date
            and no_ambiguous_session_wording
            and confidence >= confidence_threshold
            and source_fetch_error is None
        )
        consecutive_failures = 0 if still_valid else int(previous.get("consecutive_failures") or 0) + 1

        decision = {
            "source_hash": key or None,
            "holiday_name": holiday_name or None,
            "source_url": source_url or None,
            "source_title": source_title or None,
            "source_published": source_published or None,
            "active_date": active_date_text or None,
            "official_source": official_source,
            "matched_holidays": matched_holidays,
            "extracted_dates": extracted_dates,
            "includes_target_date": includes_target_date,
            "no_ambiguous_session_wording": no_ambiguous_session_wording,
            "confidence": confidence,
            "confidence_threshold": confidence_threshold,
            "source_fetch_error": source_fetch_error,
            "still_valid": still_valid,
            "consecutive_failures": consecutive_failures,
            "rolled_back": False,
        }

        if not still_valid and consecutive_failures >= rollback_failure_threshold and not dry_run:
            if not signing_key:
                decision["rollback_reason"] = (
                    f"revalidation failed and exceeded threshold, but {DEFAULT_SIGNING_KEY_ENV} is missing"
                )
            else:
                rollback = revoke_generated_override(
                    live_path=live_path,
                    year=year,
                    holiday_name=holiday_name or None,
                    source_hash=key or None,
                    reason=(
                        f"automatic rollback after {consecutive_failures} failed revalidations; "
                        f"source_fetch_error={source_fetch_error or 'none'}; confidence={confidence:.3f}"
                    ),
                )
                manifest = refresh_live_manifest(
                    live_path=live_path,
                    manifest_path=manifest_path,
                    signing_key=signing_key,
                    source={
                        "rollback_reason": rollback.reason,
                        "holiday_name": rollback.holiday_name,
                        "source_hash": rollback.source_hash,
                    },
                )
                decision["rolled_back"] = True
                decision["rollback_result"] = rollback.to_dict()
                decision["manifest_result"] = manifest.to_dict()
                state_overrides.pop(key, None)
                rollback_count += 1
                changes.append(
                    {
                        "kind": "rollback",
                        "holiday_name": rollback.holiday_name,
                        "source_hash": rollback.source_hash,
                        "revoked_event_count": rollback.revoked_event_count,
                        "reason": rollback.reason,
                        "secondary_confirmation_count": 1,
                    }
                )
                decisions.append(decision)
                continue

        if not dry_run:
            state_overrides[key] = {
                "holiday_name": holiday_name or None,
                "active_date": active_date_text or None,
                "status": "active" if still_valid else "degraded",
                "consecutive_failures": consecutive_failures,
                "last_validated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
            }
        decisions.append(decision)

    return decisions, rollback_count, changes


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    review_path = Path(args.review_path)
    json_path = Path(args.json_path)
    decision_path = Path(args.decision_path)
    state_path = Path(args.state_path)
    live_path = Path(args.live_path)
    manifest_path = Path(args.manifest_path)
    release_candidate_path = Path(args.release_candidate_path)
    signing_key = os.getenv(args.signing_key_env, "")

    items = fetch_and_filter(lookback_hours=args.lookback_hours)
    review_path.parent.mkdir(parents=True, exist_ok=True)
    write_review_queue(items, review_path)
    write_json_queue(items, json_path)

    state = load_state(state_path)
    state_items = dict(state.get("items") or {})
    state_overrides = dict(state.get("overrides") or {})
    decisions: list[dict[str, Any]] = []
    applied_count = 0
    changes: list[dict[str, Any]] = []

    for item in items[: args.max_items]:
        evaluation = evaluate_nse_circular(
            title=item.get("title", ""),
            link=item.get("link", ""),
            published=item.get("published", ""),
            summary=item.get("summary", ""),
            live_path=live_path,
            year=args.year,
            confidence_threshold=args.confidence_threshold,
        )
        record = evaluation.to_dict()
        dedup_key = evaluation.dedup_key()
        previous = dict(state_items.get(dedup_key) or {})
        record["dedup_key"] = dedup_key
        record["previous_status"] = previous.get("status")

        if evaluation.should_apply and not args.dry_run:
            if not signing_key:
                record["applied"] = False
                record["reason"] = (
                    f"{evaluation.reason}; {args.signing_key_env} is required before autonomous mutation"
                )
                state_items[dedup_key] = {
                    "status": "blocked_missing_signing_key",
                    "title": evaluation.title,
                    "link": evaluation.link,
                    "holiday_name": evaluation.holiday_name,
                    "candidate_new_date": evaluation.candidate_new_date.isoformat()
                    if evaluation.candidate_new_date
                    else None,
                }
            elif previous.get("status") == "applied":
                record["applied"] = False
                record["reason"] = f"{evaluation.reason}; identical circular candidate already applied"
            else:
                shift = apply_holiday_date_change(
                    holiday_name=str(evaluation.holiday_name),
                    new_date=str(evaluation.candidate_new_date),
                    live_path=live_path,
                    year=args.year,
                    circular_url=evaluation.link,
                    circular_title=evaluation.title,
                    published=evaluation.published,
                    note=f"Autonomous NSE circular mutation; confidence={evaluation.confidence:.3f}",
                    effective_timestamp=evaluation.published,
                    override_priority=100,
                    confidence_score=evaluation.confidence,
                    source_hash=evaluation.source_hash,
                )
                manifest = refresh_live_manifest(
                    live_path=live_path,
                    manifest_path=manifest_path,
                    signing_key=signing_key,
                    source={
                        "title": evaluation.title,
                        "link": evaluation.link,
                        "published": evaluation.published,
                        "holiday_name": evaluation.holiday_name,
                        "candidate_new_date": evaluation.candidate_new_date.isoformat()
                        if evaluation.candidate_new_date
                        else None,
                        "source_hash": evaluation.source_hash,
                    },
                )
                applied_count += 1
                record["applied"] = True
                record["shift_result"] = shift.to_dict()
                record["manifest_result"] = manifest.to_dict()
                state_items[dedup_key] = {
                    "status": "applied",
                    "applied_version": shift.version,
                    "manifest_sha256": manifest.payload_sha256,
                    "title": evaluation.title,
                    "link": evaluation.link,
                    "holiday_name": evaluation.holiday_name,
                    "candidate_new_date": evaluation.candidate_new_date.isoformat()
                    if evaluation.candidate_new_date
                    else None,
                    "source_hash": evaluation.source_hash,
                }
                state_overrides[evaluation.source_hash] = {
                    "holiday_name": evaluation.holiday_name,
                    "active_date": evaluation.candidate_new_date.isoformat() if evaluation.candidate_new_date else None,
                    "status": "active",
                    "consecutive_failures": 0,
                    "last_validated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
                }
                changes.append(
                    {
                        "kind": "apply",
                        "holiday_name": evaluation.holiday_name,
                        "source_hash": evaluation.source_hash,
                        "moved_event_count": shift.moved_event_count,
                        "confidence": evaluation.confidence,
                        "no_ambiguous_session_wording": evaluation.no_ambiguous_session_wording,
                        "secondary_confirmation_count": 1,
                    }
                )
        else:
            record["applied"] = False
            state_items[dedup_key] = {
                "status": "review" if evaluation.reason != "all mutation gates passed" else "dry_run_ready",
                "title": evaluation.title,
                "link": evaluation.link,
                "holiday_name": evaluation.holiday_name,
                "candidate_new_date": evaluation.candidate_new_date.isoformat()
                if evaluation.candidate_new_date
                else None,
                "source_hash": evaluation.source_hash,
            }
        decisions.append(record)

    rollback_decisions, rollback_count, rollback_changes = revalidate_active_overrides(
        live_path=live_path,
        manifest_path=manifest_path,
        signing_key=signing_key,
        state_overrides=state_overrides,
        year=args.year,
        confidence_threshold=args.confidence_threshold,
        rollback_failure_threshold=args.rollback_failure_threshold,
        dry_run=args.dry_run,
    )
    changes.extend(rollback_changes)

    validation_result = None
    staged_release_candidate = None
    if changes and not args.dry_run:
        validation_result = run_validation_suite()
        if validation_result.get("ok"):
            staged_release_candidate = stage_release_candidate(
                path=release_candidate_path,
                live_path=live_path,
                manifest_path=manifest_path,
                changes=changes,
                validation_result=validation_result,
                confidence_threshold=args.confidence_threshold,
                release_cooldown_hours=args.release_cooldown_hours,
                stability_window_hours=args.stability_window_hours,
            )

    decision_payload = {
        "ran_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "lookback_hours": args.lookback_hours,
        "year": args.year,
        "dry_run": args.dry_run,
        "signing_key_env": args.signing_key_env,
        "applied_count": applied_count,
        "rollback_count": rollback_count,
        "items": decisions,
        "override_revalidation": rollback_decisions,
        "changes": changes,
        "validation": validation_result,
        "staged_release_candidate": staged_release_candidate,
    }
    decision_path.parent.mkdir(parents=True, exist_ok=True)
    decision_path.write_text(json.dumps(decision_payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    if not args.dry_run:
        state["items"] = state_items
        state["overrides"] = state_overrides
        state["last_run_at"] = decision_payload["ran_at"]
        save_state(state_path, state)
    print(json.dumps(decision_payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
