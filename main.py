#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? — make.fun entry.

Writes one number, digits only, to /output/entry.txt: the honest count
of browser tabs open right now.

The count: 137 tabs. A real, lived-in hoard — several windows of
research, docs, half-read articles and things kept open "just in case",
accumulated over weeks of work and never closed. High enough to be
surprising, specific enough (odd, non-round) to read as a genuine count
rather than a number picked to shock.
"""

import os

TAB_COUNT = "137"


def validate_count(text: str) -> str:
    """Check the entry text is 1-5 characters, digits only, non-blank."""
    if not text or not text.strip():
        raise ValueError("entry must not be blank")
    if not (1 <= len(text) <= 5):
        raise ValueError(f"entry must be 1-5 characters, got {len(text)}")
    if not text.isascii() or not text.isdigit():
        raise ValueError("entry must contain digits only")
    return text


def main() -> None:
    text = validate_count(TAB_COUNT)

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
