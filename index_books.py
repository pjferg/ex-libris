"""Rebuild the Markdown index; use --watch to update it as books change."""

import argparse
import html
import json
from pathlib import Path
import re
import time
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent
FIELDS = ("title", "author", "status", "rating", "lent_to")


def metadata(text):
    """Read the simple, single-line fields used by the book template."""
    lines = text.splitlines()
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        raise ValueError("missing or unfinished metadata block")
    result = {}
    for line in lines[1:lines.index("---", 1)]:
        key, separator, value = line.partition(":")
        if not separator or key not in FIELDS:
            continue
        value = value.strip()
        if value.startswith('"'):
            value = json.loads(value)
        elif value.startswith("'"):
            if not value.endswith("'") or len(value) < 2:
                raise ValueError(f"unfinished quoted {key}")
            value = value[1:-1].replace("''", "'")
        elif value in ("|", ">", "|-", ">-", "|+", ">+"):
            raise ValueError(f"keep {key} on one line")
        elif value in ("null", "~"):
            value = ""
        result[key] = value
    if not result.get("title"):
        raise ValueError("missing title")
    return result


def cell(value):
    value = html.escape(str(value), quote=False).replace("|", "&#124;")
    return re.sub(r"([\\`*_[\]~])", r"\\\1", value).replace("\n", " ").replace("\r", " ")


def update():
    books = []
    for path in sorted((ROOT / "books").glob("*.md")):
        try:
            books.append((path, metadata(path.read_text(encoding="utf-8"))))
        except ValueError as error:
            raise ValueError(f"{path.name}: {error}") from error
    lines = ["# Library", "", "[About this library](README.md)", "",
             "| Title | Author | Status | Rating | Lent to |", "|---|---|---|---:|---|"]
    for path, book in sorted(books, key=lambda entry: entry[1]["title"].casefold()):
        title = f"[{cell(book['title'])}](books/{quote(path.name, safe='')})"
        lines.append("| " + " | ".join([title] + [cell(book.get(key, "")) for key in FIELDS[1:]]) + " |")
    content = "\n".join(lines) + "\n"
    index = ROOT / "index.md"
    if not index.exists() or index.read_text(encoding="utf-8") != content:
        index.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--watch", action="store_true", help="check for changes every second until Ctrl-C")
    args = parser.parse_args()
    previous_error = None
    if args.watch:
        print("Updating index.md as books change. Press Ctrl-C to stop.", flush=True)
    try:
        while True:
            try:
                update()
                previous_error = None
            except (OSError, ValueError) as error:
                if not args.watch:
                    parser.exit(1, f"Index not updated: {error}\n")
                if str(error) != previous_error:
                    print(f"Index not updated: {error}", flush=True)
                    previous_error = str(error)
            if not args.watch:
                break
            time.sleep(1)
    except KeyboardInterrupt:
        pass
