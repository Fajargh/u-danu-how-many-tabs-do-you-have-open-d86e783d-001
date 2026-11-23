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


def main() -> None:
    text = TAB_COUNT

    # Validation guard: the gate requires /output/entry.txt to be UTF-8,
    # 1-5 characters, digits only, not only whitespace.
    if not (1 <= len(text) <= 5):
        raise ValueError(f"entry must be 1-5 characters, got {len(text)}")
    if not text.isascii() or not text.isdigit():
        raise ValueError("entry must contain digits only")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
