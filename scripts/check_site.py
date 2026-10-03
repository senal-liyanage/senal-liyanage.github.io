#!/usr/bin/env python3
"""Dependency-free structural QA for the static portfolio."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
EXTERNAL_SCHEMES = {"http", "https", "mailto", "tel", "data", "javascript"}
errors: list[str] = []


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.refs: list[tuple[str, str]] = []
        self.h1_count = 0
        self.title_depth = 0
        self.title_text: list[str] = []
        self.has_lang = False
        self.has_description = False
        self.has_canonical = False
        self.has_icon = False

    def handle_starttag(self, tag: str, attrs_list: list[tuple[str, str | None]]) -> None:
        attrs = dict(attrs_list)
        if tag == "html" and attrs.get("lang"):
            self.has_lang = True
        if attrs.get("id"):
            self.ids.append(attrs["id"] or "")
        if tag == "h1":
            self.h1_count += 1
        if tag == "title":
            self.title_depth += 1
        if tag == "meta" and attrs.get("name", "").lower() == "description" and attrs.get("content"):
            self.has_description = True
        if tag == "link":
            rel = (attrs.get("rel") or "").lower().split()
            if "canonical" in rel and attrs.get("href"):
                self.has_canonical = True
            if "icon" in rel and attrs.get("href"):
                self.has_icon = True
        if tag == "img" and not (attrs.get("alt") or "").strip():
            errors.append("Image is missing non-empty alt text")
        if tag in {"video", "canvas"} and not (attrs.get("aria-label") or attrs.get("aria-labelledby")):
            errors.append(f"{tag} is missing an accessible label")
        for attr in ("href", "src", "poster"):
            value = attrs.get(attr)
            if value:
                self.refs.append((attr, value))

    def handle_endtag(self, tag: str) -> None:
        if tag == "title" and self.title_depth:
            self.title_depth -= 1

    def handle_data(self, data: str) -> None:
        if self.title_depth:
            self.title_text.append(data)


def parse_page(path: Path) -> PageParser:
    parser = PageParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def target_for(source: Path, raw: str) -> tuple[Path | None, str]:
    parsed = urlsplit(raw)
    if parsed.scheme.lower() in EXTERNAL_SCHEMES or raw.startswith("//"):
        return None, ""
    fragment = unquote(parsed.fragment)
    path_text = unquote(parsed.path)
    if not path_text:
        return source, fragment
    if path_text.startswith("/"):
        candidate = ROOT / path_text.lstrip("/")
    else:
        candidate = source.parent / path_text
    if path_text.endswith("/"):
        candidate = candidate / "index.html"
    return candidate.resolve(), fragment


pages = sorted(ROOT.rglob("*.html"))
parsers: dict[Path, PageParser] = {}

for page in pages:
    parser = parse_page(page)
    parsers[page.resolve()] = parser
    rel = page.relative_to(ROOT)
    if not parser.has_lang:
        errors.append(f"{rel}: html lang attribute is missing")
    if parser.h1_count != 1:
        errors.append(f"{rel}: expected exactly one h1; found {parser.h1_count}")
    if not "".join(parser.title_text).strip():
        errors.append(f"{rel}: title is empty")
    if not parser.has_description:
        errors.append(f"{rel}: meta description is missing")
    if page.name != "404.html" and not parser.has_canonical:
        errors.append(f"{rel}: canonical URL is missing")
    if not parser.has_icon:
        errors.append(f"{rel}: favicon link is missing")
    if len(parser.ids) != len(set(parser.ids)):
        errors.append(f"{rel}: duplicate id values detected")

for page in pages:
    parser = parsers[page.resolve()]
    rel = page.relative_to(ROOT)
    for attr, ref in parser.refs:
        target, fragment = target_for(page.resolve(), ref)
        if target is None:
            continue
        if not target.exists():
            errors.append(f"{rel}: {attr} target does not exist: {ref}")
            continue
        if fragment:
            target_page = target
            if target_page.is_dir():
                target_page = target_page / "index.html"
            if target_page.suffix.lower() == ".html":
                parsed_target = parsers.get(target_page.resolve())
                if parsed_target is None:
                    parsed_target = parse_page(target_page)
                    parsers[target_page.resolve()] = parsed_target
                if fragment not in set(parsed_target.ids):
                    errors.append(f"{rel}: fragment #{fragment} not found in {target_page.relative_to(ROOT)}")

for required in ("robots.txt", "sitemap.xml"):
    if not (ROOT / required).exists():
        errors.append(f"Required production file is missing: {required}")

if errors:
    print("Site QA failed:")
    for error in sorted(set(errors)):
        print(f" - {error}")
    raise SystemExit(1)

print(f"Site QA passed: {len(pages)} HTML pages checked.")
