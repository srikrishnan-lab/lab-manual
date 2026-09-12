#!/usr/bin/env python3
"""Export the whole lab manual as one Markdown file.

For pasting or uploading into somewhere that takes a document rather than a
URL -- a Claude Project, a custom assistant's knowledge, an LLM context.

The bundle follows the sidebar order from _quarto.yml rather than the
filesystem, so it reads in the order a person would read the site. Relative
.qmd cross-references are rewritten to absolute URLs on the published site,
because "../guides/hopper.qmd" means nothing outside the repository.

    python3 scripts/export-bundle.py            # -> lab-manual-bundle.md
    python3 scripts/export-bundle.py --out X.md

Regenerate after changes: the bundle is a snapshot and goes stale, which is
why the live site is the better source if whatever you are feeding can take
a URL.
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://viveks.bee.cornell.edu/lab-manual"


def sidebar_order(quarto_yml: Path) -> list[str]:
    """Page order as listed in the _quarto.yml sidebar.

    Parsed with a regex rather than a YAML library so the script has no
    dependencies. Any .qmd not listed is appended afterwards, so nothing is
    silently dropped when someone adds a page without touching the sidebar.
    """
    text = quarto_yml.read_text(encoding="utf-8")
    seen, order = set(), []
    for m in re.finditer(r"^\s*-\s+([A-Za-z0-9_./-]+\.qmd)\s*$", text, re.M):
        p = m.group(1)
        if p not in seen:
            seen.add(p)
            order.append(p)
    return order


def title_and_body(path: Path) -> tuple[str, str]:
    raw = path.read_text(encoding="utf-8")
    fm = re.match(r"^---\n(.*?)\n---\n", raw, re.S)
    title, body = path.stem, raw
    if fm:
        t = re.search(r'^title:\s*"?(.*?)"?\s*$', fm.group(1), re.M)
        if t:
            title = t.group(1)
        body = raw[fm.end():]
    return title, body


def rewrite_links(body: str, page: Path) -> str:
    """Turn relative .qmd links into absolute published URLs."""
    def repl(m: re.Match) -> str:
        text, target = m.group(1), m.group(2)
        anchor = ""
        if "#" in target:
            target, anchor = target.split("#", 1)
            anchor = "#" + anchor
        resolved = (page.parent / target).resolve()
        try:
            rel = resolved.relative_to(ROOT).with_suffix(".html")
        except ValueError:
            return m.group(0)
        return f"[{text}]({SITE}/{rel.as_posix()}{anchor})"

    return re.sub(r"\[([^\]]*)\]\(([^)]*?\.qmd(?:#[^)]*)?)\)", repl, body)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="lab-manual-bundle.md")
    args = ap.parse_args()

    listed = sidebar_order(ROOT / "_quarto.yml")
    top = ["index.qmd", "about.qmd", "contributing/index.qmd"]
    on_disk = sorted(
        p.relative_to(ROOT).as_posix()
        for p in ROOT.rglob("*.qmd")
        if "_site" not in p.parts
    )
    ordered = [p for p in top if p in on_disk]
    ordered += [p for p in listed if p in on_disk and p not in ordered]
    missing = [p for p in on_disk if p not in ordered]
    ordered += missing
    if missing:
        print(f"note: {len(missing)} page(s) not in the sidebar, appended at "
              f"the end: {', '.join(missing)}", file=sys.stderr)

    today = dt.date.today().isoformat()
    out = [
        "# Srikrishnan Research Group — Lab Manual",
        "",
        f"Complete text of the lab manual, exported {today}.",
        f"Published version, which is authoritative: {SITE}",
        "",
        "This is a snapshot. Where it disagrees with the live site, the site wins.",
        "",
        "## Contents",
        "",
    ]
    sections = []
    for rel in ordered:
        title, body = title_and_body(ROOT / rel)
        body = rewrite_links(body, ROOT / rel)
        url = f"{SITE}/{Path(rel).with_suffix('.html').as_posix()}"
        out.append(f"- {title} — `{rel}`")
        sections.append(
            f"\n\n---\n\n# {title}\n\n"
            f"*Source: `{rel}` · {url}*\n\n{body.strip()}\n"
        )

    text = "\n".join(out) + "".join(sections) + "\n"
    dest = ROOT / args.out
    dest.write_text(text, encoding="utf-8")
    words = len(text.split())
    print(f"{dest.name}: {len(ordered)} pages, {words:,} words, "
          f"~{int(words * 1.4):,} tokens, {len(text) / 1024:.0f} KB")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
