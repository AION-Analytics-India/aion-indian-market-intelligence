from __future__ import annotations

import datetime as dt
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.request import Request, urlopen

import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from aion_indian_market_calendar.live_overrides import match_known_holiday_names

NSE_RSS_URL = "https://nsearchives.nseindia.com/content/RSS/Circulars.xml"
LOOKBACK_HOURS = 6
KEYWORDS = ("holiday", "trading session", "muhurat", "market closed", "market timing", "session")


def _now_utc() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def _published_at(entry) -> dt.datetime | None:
    published = str(entry.get("published", "") or entry.get("updated", "")).strip()
    if not published:
        return None
    for fmt in ("%a, %d %b %Y %H:%M:%S %z", "%a, %d %b %Y %H:%M:%S %Z", "%a, %d %b %Y %H:%M:%S GMT"):
        try:
            parsed = dt.datetime.strptime(published, fmt)
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=dt.timezone.utc)
            return parsed.astimezone(dt.timezone.utc)
        except ValueError:
            continue
    return None


def _fetch_feed_entries(url: str) -> list[dict[str, str]]:
    request = Request(url, headers={"User-Agent": "aion-indian-market-calendar/1.0"})
    with urlopen(request, timeout=15) as response:
        raw_xml = response.read()

    root = ET.fromstring(raw_xml)
    entries: list[dict[str, str]] = []
    for item in root.findall(".//item"):
        entries.append(
            {
                "title": str(item.findtext("title") or "").strip(),
                "link": str(item.findtext("link") or "").strip(),
                "published": str(item.findtext("pubDate") or "").strip(),
                "summary": str(item.findtext("description") or "").strip(),
            }
        )
    return entries


def fetch_and_filter(*, lookback_hours: int = LOOKBACK_HOURS) -> list[dict[str, str]]:
    entries = _fetch_feed_entries(NSE_RSS_URL)
    cutoff = _now_utc() - dt.timedelta(hours=lookback_hours)
    matches: list[dict[str, str]] = []
    for entry in entries:
        published_at = _published_at(entry)
        if published_at and published_at < cutoff:
            continue

        title = str(entry.get("title", "")).strip()
        lower_title = title.lower()
        if not any(keyword in lower_title for keyword in KEYWORDS):
            continue

        link = str(entry.get("link", "")).strip()
        summary = str(entry.get("summary", "")).strip()
        haystack = " ".join(part for part in (title, summary) if part)
        matched_holidays = match_known_holiday_names(haystack)

        matches.append(
            {
                "title": title,
                "link": link,
                "published": str(entry.get("published", "")).strip(),
                "summary": summary,
                "matched_holidays": matched_holidays,
            }
        )
    return matches


def write_review_queue(items: list[dict[str, str]], path: Path) -> None:
    lines = [f"# New NSE circulars found at {_now_utc().isoformat()}", ""]
    if not items:
        lines.append("No new relevant circulars.")
    else:
        for item in items:
            lines.extend(
                [
                    f"## [{item['title']}]({item['link']})",
                    f"Published: {item['published']}",
                    "",
                    item["summary"] or "_No summary provided._",
                    "",
                ]
            )
            matched_holidays = item.get("matched_holidays") or []
            if matched_holidays:
                for holiday_name in matched_holidays:
                    lines.extend(
                        [
                            f"Detected bundled holiday candidate: `{holiday_name}`",
                            "Suggested command:",
                            (
                                f"./venv/bin/python scripts/apply_nse_circular_to_calendar.py "
                                f"shift-holiday --holiday-name \"{holiday_name}\" "
                                f"--new-date YYYY-MM-DD --circular-url \"{item['link']}\" "
                                f"--circular-title \"{item['title']}\""
                            ),
                            "",
                        ]
                    )
            lines.extend(
                [
                    "Action: review and add/remove entries in `live_events.json` if the calendar should change.",
                    "",
                ]
            )
    path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")


def write_json_queue(items: list[dict[str, str]], path: Path) -> None:
    path.write_text(json.dumps({"items": items}, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    review_path = REPO_ROOT / "ops" / "review_queue" / "latest.md"
    json_path = REPO_ROOT / "ops" / "review_queue" / "latest_calendar_candidates.json"
    review_path.parent.mkdir(parents=True, exist_ok=True)
    items = fetch_and_filter()
    write_review_queue(items, review_path)
    write_json_queue(items, json_path)
