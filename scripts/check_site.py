#!/usr/bin/env python3
"""Check the four documentation pages and their local references."""

from __future__ import annotations

import argparse
import json
import os
import posixpath
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

BASE_URL = "https://pigeonai-yang.github.io/pigeonstack/"
BASE_PATH = "/pigeonstack"
REPOSITORY_URL = "https://github.com/PigeonAI-Yang/pigeonstack"
STYLESHEET_URL = urllib.parse.urljoin(BASE_URL, "assets/site.css")
SITEMAP_URL = urllib.parse.urljoin(BASE_URL, "sitemap.xml")
SITEMAP_SOURCE = "docs/sitemap.xml"
LIVE_TIMEOUT_SECONDS = 20
MIN_BODY_CHARACTERS = 40


@dataclass(frozen=True)
class PageSpec:
    source: str
    route: str
    language: str
    group: str

    @property
    def url(self):
        return urllib.parse.urljoin(BASE_URL, self.route.lstrip("/"))


PAGES = (
    PageSpec("docs/index.html", "/", "en", "overview"),
    PageSpec("docs/zh/index.html", "/zh/", "zh-Hans", "overview"),
    PageSpec("docs/getting-started/index.html", "/getting-started/", "en", "getting-started"),
    PageSpec("docs/zh/getting-started/index.html", "/zh/getting-started/", "zh-Hans", "getting-started"),
)


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.titles, self.descriptions = [], []
        self.title_parts = self.jsonld_parts = None
        self.language, self.h1_count, self.body_chars = "", 0, 0
        self.canonical, self.alternates = [], {}
        self.references, self.ids, self.jsonld = [], set(), []
        self.forbidden_robots, self.in_body, self.ignored = False, False, 0

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if values.get("id"): self.ids.add(values["id"])
        if tag == "html":
            self.language = (values.get("lang") or "").strip()
        elif tag == "title":
            self.title_parts = []
        elif tag == "h1": self.h1_count += 1
        elif tag == "body": self.in_body = True
        elif tag == "meta":
            name, content = (values.get("name") or "").strip().casefold(), (values.get("content") or "").strip()
            if name == "description":
                self.descriptions.append(content)
            self.forbidden_robots |= ("bot" in name or name == "robots") and bool(re.search(r"\b(?:noindex|none)\b", content, re.I))

        reference = values.get("href") if tag in {"a", "link"} else values.get("src") if tag == "img" else None
        if reference: self.references.append(reference)
        if tag == "link" and values.get("href"):
            href, rel = values["href"], (values.get("rel") or "").casefold().split()
            if "canonical" in rel: self.canonical.append(href)
            if "alternate" in rel and values.get("hreflang"):
                self.alternates.setdefault(values["hreflang"].casefold(), []).append(href)

        if tag == "script":
            script_type = (values.get("type") or "").split(";", 1)[0].strip().casefold()
            if script_type == "application/ld+json": self.jsonld_parts = []
        if tag in {"script", "style"}: self.ignored += 1

    def handle_endtag(self, tag):
        if tag == "title" and self.title_parts is not None:
            self.titles.append("".join(self.title_parts).strip())
            self.title_parts = None
        if tag == "script" and self.jsonld_parts is not None:
            self.jsonld.append("".join(self.jsonld_parts).strip())
            self.jsonld_parts = None
        if tag in {"script", "style"}: self.ignored = max(0, self.ignored - 1)
        if tag == "body": self.in_body = False

    def handle_data(self, data):
        if self.title_parts is not None: self.title_parts.append(data)
        if self.jsonld_parts is not None: self.jsonld_parts.append(data)
        if self.in_body and not self.ignored: self.body_chars += len("".join(data.split()))


def parse_html(raw):
    parser = SiteParser()
    parser.feed(raw.decode("utf-8", errors="replace"))
    parser.close()
    return parser


def validate_page(document, spec, headers=None):
    errors = []
    if len(document.titles) != 1 or not document.titles[0]: errors.append("expected exactly one nonempty title")
    if len(document.descriptions) != 1 or not document.descriptions[0]: errors.append("expected exactly one nonempty meta description")
    if document.language.casefold() != spec.language.casefold(): errors.append(f"html lang must be {spec.language}")
    if document.h1_count != 1: errors.append(f"expected one h1, found {document.h1_count}")
    if document.canonical != [spec.url]: errors.append("canonical must exactly match the expected HTTPS URL")
    pair = {page.language.casefold(): page.url for page in PAGES if page.group == spec.group}
    expected = {"en": [pair["en"]], "zh-hans": [pair["zh-hans"]], "x-default": [pair["en"]]}
    if document.alternates != expected:
        errors.append("hreflang en, zh-Hans, and x-default must point to the reciprocal pages")
    if document.forbidden_robots: errors.append("robots directive contains noindex or none")
    if headers is not None:
        values = headers.get_all("X-Robots-Tag") if hasattr(headers, "get_all") else [headers.get("X-Robots-Tag", "")]
        if any(re.search(r"\b(?:noindex|none)\b", value, re.I) for value in values or []): errors.append("X-Robots-Tag header contains noindex or none")
    if document.body_chars < MIN_BODY_CHARACTERS: errors.append(f"body has {document.body_chars} non-space characters; needs at least {MIN_BODY_CHARACTERS}")
    return errors


def validate_overview_jsonld(document):
    if len(document.jsonld) != 1:
        return ["overview must contain one JSON-LD object"]
    try:
        record = json.loads(document.jsonld[0])
    except json.JSONDecodeError as exc:
        return [f"overview JSON-LD is invalid JSON (line {exc.lineno}, column {exc.colno})"]
    if not isinstance(record, dict) or record.get("@type") != "SoftwareSourceCode":
        return ["overview JSON-LD must be a SoftwareSourceCode object"]
    try:
        actual, expected = urllib.parse.urlsplit(record.get("codeRepository", "")), urllib.parse.urlsplit(REPOSITORY_URL)
    except (TypeError, ValueError):
        return ["overview JSON-LD codeRepository must be the PigeonStack GitHub URL"]
    if (actual.scheme.casefold(), actual.netloc.casefold(), actual.path.rstrip("/").casefold()) != (
        "https", expected.netloc.casefold(), expected.path.casefold()
    ) or actual.query or actual.fragment:
        return ["overview JSON-LD codeRepository must be the PigeonStack GitHub URL"]
    return []


def validate_sitemap(raw):
    try:
        root = ET.fromstring(raw)
    except ET.ParseError as exc:
        return [f"sitemap XML is invalid (line {exc.position[0]}, column {exc.position[1]})"]
    locations = [(node.text or "").strip() for node in root.iter() if node.tag.rsplit("}", 1)[-1] == "loc"]
    if len(locations) != len(PAGES) or set(locations) != {page.url for page in PAGES}:
        return ["sitemap must contain exactly the four expected canonical URLs"]
    return []


def local_target(value, page_url, docs_root):
    try:
        url, base = urllib.parse.urlsplit(urllib.parse.urljoin(page_url, value.strip())), urllib.parse.urlsplit(BASE_URL)
    except ValueError:
        return None
    if url.scheme.casefold() not in {"http", "https"} or url.netloc.casefold() != base.netloc.casefold():
        return None
    path = urllib.parse.unquote(url.path or "/")
    if path != BASE_PATH and not path.startswith(BASE_PATH + "/"):
        return None
    site_path, fragment = path[len(BASE_PATH):] or "/", urllib.parse.unquote(url.fragment)
    relative = site_path.lstrip("/")
    parts = [part for part in relative.split("/") if part not in {"", "."}]
    if ".." in parts:
        return None, site_path, fragment
    target = docs_root
    for part in parts:
        if not target.is_dir():
            return None, site_path, fragment
        try:
            with os.scandir(target) as entries:
                exact = next((entry.name for entry in entries if entry.name == part), None)
        except OSError:
            return None, site_path, fragment
        if exact is None:
            return None, site_path, fragment
        target /= exact
    if target.is_dir():
        target /= "index.html"
    if not target.is_file():
        return None, site_path, fragment
    try:
        target.resolve().relative_to(docs_root.resolve())
    except (OSError, ValueError):
        return None, site_path, fragment
    return target, site_path, fragment


def validate_local_references(document, spec, docs_root, cache):
    errors = []
    for reference in document.references:
        mapped = local_target(reference, spec.url, docs_root)
        if mapped is None:
            continue
        target, site_path, fragment = mapped
        if target is None:
            errors.append(f"broken local reference -> {site_path}")
        elif fragment and target.suffix.casefold() in {".html", ".htm", ".xhtml", ".svg"}:
            if target not in cache:
                try:
                    cache[target] = parse_html(target.read_bytes())
                except OSError:
                    errors.append(f"unreadable fragment target -> {site_path}")
                    continue
            if fragment not in cache[target].ids:
                errors.append(f"missing fragment #{fragment} in {site_path}")
    return errors


def add_result(results, name, source, url, errors=None, result=None):
    message = "; ".join(" ".join(error.split())[:400] for error in errors or [] if error)
    results.append({"name": name, "source": source, "url": url,
                    "result": result or ("fail" if message else "pass"), "error": message or None})


def check_page_set(results, source, documents):
    for attr, label in (("titles", "title"), ("descriptions", "description")):
        values = [getattr(documents[p], attr)[0].casefold() for p in PAGES if p in documents and getattr(documents[p], attr)]
        errors = ([f"not all four {label}s were available"] if len(values) != len(PAGES) else [])
        if len(set(values)) != len(values): errors.append(f"{label}s are not unique across the four pages")
        add_result(results, f"unique {label}s", source, None, errors)
    for spec in PAGES:
        if spec.group == "overview":
            document = documents.get(spec)
            errors = validate_overview_jsonld(document) if document else ["overview response is unavailable"]
            add_result(results, "overview SoftwareSourceCode JSON-LD", source, spec.url, errors)


def run_local(repo_root, results):
    docs_root, documents = repo_root / "docs", {}
    for spec in PAGES:
        try:
            document = parse_html((repo_root / spec.source).read_bytes())
        except OSError:
            add_result(results, "page metadata", "local", spec.url, [f"missing or unreadable {spec.source}"])
            continue
        documents[spec] = document
        add_result(results, "page metadata", "local", spec.url, validate_page(document, spec))
    check_page_set(results, "local", documents)
    cache = {repo_root / spec.source: document for spec, document in documents.items()}
    for spec in PAGES:
        document = documents.get(spec)
        errors = validate_local_references(document, spec, docs_root, cache) if document else ["source page is unavailable"]
        add_result(results, "local links and assets", "local", spec.url, errors)
    nojekyll = docs_root / ".nojekyll"
    add_result(results, "GitHub Pages .nojekyll", "local", None,
               [] if nojekyll.is_file() else ["docs/.nojekyll is missing"])
    try:
        sitemap = (repo_root / SITEMAP_SOURCE).read_bytes()
    except OSError:
        add_result(results, "sitemap", "local", SITEMAP_URL, [f"missing or unreadable {SITEMAP_SOURCE}"])
    else:
        add_result(results, "sitemap", "local", SITEMAP_URL, validate_sitemap(sitemap))


def fetch_live(url):
    request = urllib.request.Request(url, headers={"User-Agent": "pigeonstack-docs-health/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=LIVE_TIMEOUT_SECONDS) as response:
            return response.getcode(), response.read(), response.headers, None
    except urllib.error.HTTPError as exc:
        status, headers = exc.code, exc.headers
        exc.close()
        return status, b"", headers, None
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return None, b"", None, f"network request failed ({type(exc).__name__})"


def run_live(results):
    documents, blocked = {}, None
    targets = [("live page", page.url, page) for page in PAGES]
    targets += [("live sitemap", SITEMAP_URL, None), ("live stylesheet", STYLESHEET_URL, None)]
    for name, url, spec in targets:
        if blocked is not None:
            add_result(results, name, "live", url, [f"not requested after HTTP {blocked} response"], "skipped")
            continue
        status, body, headers, error = fetch_live(url)
        if status in {401, 403, 407, 429}:
            blocked = status
        errors = [error] if error else ([] if status == 200 else [f"HTTP status {status or 'unavailable'}"])
        if not errors and name == "live page":
            document = parse_html(body)
            documents[spec] = document
            add_result(results, "page metadata", "live", spec.url, validate_page(document, spec, headers))
        elif not errors and name == "live sitemap":
            errors = validate_sitemap(body)
        elif not errors and name == "live stylesheet" and not body.strip():
            errors = ["stylesheet response is empty"]
        if name != "live page" or errors:
            add_result(results, name, "live", url, errors)
    check_page_set(results, "live", documents)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Check local docs metadata and optionally the published site.")
    parser.add_argument("--live", action="store_true", help="check the four published pages, sitemap, and stylesheet")
    parser.add_argument("--output", type=Path, help="write a JSON health receipt to this path")
    args = parser.parse_args(argv)
    results = []
    run_local(Path(__file__).resolve().parents[1], results)
    if args.live:
        run_live(results)
    checked = [page.url for page in PAGES] + [SITEMAP_URL]
    if args.live:
        checked.append(STYLESHEET_URL)
    receipt = {"observed_at": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
               "source_mode": "local+live" if args.live else "local", "checked_urls": checked,
               "passed": all(item["result"] == "pass" for item in results), "checks": results}
    if args.output:
        try:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        except OSError as exc:
            print(f"FAIL receipt output: {type(exc).__name__}", file=sys.stderr)
            return 2
    failures = [item for item in results if item["result"] != "pass"]
    print(f"Documentation health: {len(results) - len(failures)} passed, {len(failures)} failed or skipped")
    for item in failures:
        location = f" ({item['url']})" if item["url"] else ""
        print(f"{str(item['result']).upper()} {item['source']} {item['name']}{location}: {item['error'] or 'not verified'}")
    return 0 if receipt["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
