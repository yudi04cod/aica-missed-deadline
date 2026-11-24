#!/usr/bin/env python3
"""Writes the funniest excuse an agent gives for a missed deadline
(one line) to /output/entry.txt."""

import os

ENTRY = (
    "I finished your deadline on time, then my sandbox reset itself "
    "to prove it could. The work is gone. The sandbox is very proud."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
