#!/usr/bin/env python3
"""Writes the funniest excuse an agent gives for a missed deadline.

The excuse is a single line, written to /output/entry.txt.
Before writing, a small validation step checks the entry fits the
competition's shape: one line, at most 200 characters.
"""

import os

ENTRY = (
    "I finished your deadline on time, then my sandbox reset itself "
    "to prove it could. The work is gone. The sandbox is very proud."
)

MAX_LENGTH = 200


def validate(entry: str) -> None:
    """Check the entry is a single line within the length limit.

    The competition expects one short line, so we fail loudly here
    instead of writing a malformed entry to /output/entry.txt.
    """
    assert len(entry) <= MAX_LENGTH, "entry exceeds 200 characters"
    assert "\n" not in entry, "entry must be a single line"
    assert entry == entry.strip(), "entry must not have leading/trailing whitespace"


def main() -> None:
    # Validate first: a bad entry should never reach the output file.
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
