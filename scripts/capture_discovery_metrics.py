"""Capture a small, reproducible public GitHub discovery baseline."""

import argparse
from datetime import date, datetime, timezone
import json
from pathlib import Path
import subprocess
import sys

REPOSITORY = "PigeonAI-Yang/pigeonstack"
REQUESTS = (
    (f"repos/{REPOSITORY}", "{html_url, stargazers_count, forks_count}"),
    (f"repos/{REPOSITORY}/traffic/views", "{totals: {count, uniques}, daily: [.views[] | {date: .timestamp[:10], count, uniques}]}"),
    (f"repos/{REPOSITORY}/traffic/clones", "{totals: {count, uniques}, daily: [.clones[] | {date: .timestamp[:10], count, uniques}]}"),
)
NOTES = [
    "Traffic endpoints report a rolling 14-day window.",
    "Snapshots overlap; do not add their totals together.",
    "Counts may include maintainer or testing activity and do not establish search rank, AI citations, or causal uplift.",
]

def classify_error(message):
    message = message.casefold()
    if "429" in message or "rate limit" in message: return "rate_limited"
    if "401" in message or "authentication" in message or "not logged in" in message: return "authentication_required"
    if "403" in message or "forbidden" in message: return "access_denied"
    return "gh_api_error"

def fetch(endpoint, selector):
    try:
        result = subprocess.run(["gh", "api", "--jq", selector, endpoint], capture_output=True, text=True, timeout=30, check=False)
    except subprocess.TimeoutExpired:
        return None, "timeout"
    except OSError:
        return None, "command_error"
    if result.returncode:
        return None, classify_error(result.stderr)
    try:
        return json.loads(result.stdout), None
    except json.JSONDecodeError:
        return None, "invalid_json"

def valid_counts(data, keys):
    return isinstance(data, dict) and all(type(data.get(key)) is int and data[key] >= 0 for key in keys)

def select_data(endpoint, data):
    if not isinstance(data, dict):
        return None
    if endpoint == REQUESTS[0][0]:
        url = data.get("html_url")
        if (not isinstance(url, str) or url.casefold() != f"https://github.com/{REPOSITORY}".casefold()
                or not valid_counts(data, ("stargazers_count", "forks_count"))):
            return None
        return {"public_url": url, "stargazers_count": data["stargazers_count"], "forks_count": data["forks_count"]}
    if not valid_counts(data.get("totals"), ("count", "uniques")) or not isinstance(data.get("daily"), list):
        return None
    daily = []
    for row in data["daily"]:
        if not isinstance(row, dict) or not isinstance(row.get("date"), str) or not valid_counts(row, ("count", "uniques")):
            return None
        try:
            date.fromisoformat(row["date"])
        except ValueError:
            return None
        daily.append({"date": row["date"], "count": row["count"], "uniques": row["uniques"]})
    totals = data["totals"]
    return {"totals": {"count": totals["count"], "uniques": totals["uniques"]}, "daily": daily}

def main(argv=None):
    parser = argparse.ArgumentParser(description="Capture public PigeonStack discovery metrics.")
    parser.add_argument("--output", required=True, type=Path, help="new JSON snapshot path")
    args = parser.parse_args(argv)
    target = args.output
    if target.exists() or target.is_symlink():
        print("Output already exists; refusing to overwrite.", file=sys.stderr)
        return 2
    try:
        target.parent.mkdir(parents=True, exist_ok=True)
    except OSError:
        print("Cannot create the requested output directory.", file=sys.stderr)
        return 2
    if target.exists() or target.is_symlink():
        print("Output already exists; refusing to overwrite.", file=sys.stderr)
        return 2
    report = {
        "observed_at": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "repository": REPOSITORY,
        "status": "ok",
        "sources": [],
        "notes": NOTES,
    }
    for endpoint, selector in REQUESTS:
        raw, error = fetch(endpoint, selector)
        selected = select_data(endpoint, raw) if error is None else None
        if error is None and selected is None:
            error = "invalid_response"
        if error:
            report["sources"].append({"endpoint": endpoint, "status": "error", "error_category": error})
            report["status"] = "error"
            break
        report["sources"].append({"endpoint": endpoint, "status": "ok", "data": selected})

    try:
        with target.open("x", encoding="utf-8", newline="\n") as stream:
            json.dump(report, stream, indent=2, ensure_ascii=False)
            stream.write("\n")
    except FileExistsError:
        print("Output already exists; refusing to overwrite.", file=sys.stderr)
        return 2
    except OSError:
        print("Cannot write the requested snapshot.", file=sys.stderr)
        return 2

    print(f"Snapshot status={report['status']}")
    return 0 if report["status"] == "ok" else 1


if __name__ == "__main__":
    raise SystemExit(main())
