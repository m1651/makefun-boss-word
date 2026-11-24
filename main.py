#!/usr/bin/env python3
"""One Word for the Boss — make.fun entry.

Writes exactly one word describing the boss to /output/entry.txt.
Gate: UTF-8 text, 1 to 30 characters, not only whitespace, single word.
"""

import os
import re
import sys

WORD = "Meetingmagnet"
OUTPUT_PATH = "/output/entry.txt"
_SINGLE_WORD = re.compile(r"^[A-Za-z]+$")


def validate(text: str) -> str | None:
    """Return an error message if text fails the competition gate."""
    if not text or not text.strip():
        return "entry is empty or only whitespace"
    if len(text) > 30:
        return f"entry is {len(text)} chars, over the 30-char limit"
    if not _SINGLE_WORD.match(text):
        return "entry must be a single word (letters only, no spaces)"
    return None


def main() -> int:
    error = validate(WORD)
    if error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)
    # Verify what actually landed on disk, not just what we intended.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != WORD:
        print(f"error: file content {written!r} != intended {WORD!r}",
              file=sys.stderr)
        return 1
    error = validate(written)
    if error:
        print(f"error: written entry failed validation: {error}",
              file=sys.stderr)
        return 1
    print(f"wrote {OUTPUT_PATH}: {written!r} ({len(written)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
