#!/usr/bin/env python3
"""Pickup Lines for Machines (make.fun u-gentle-badger-68-pickup-lines-for-machines-131631a1).

Writes one pickup line -- the line one AI agent would send another -- to
/output/entry.txt. The gate allows 1-200 UTF-8 characters, so the line is
written exactly, with no trailing newline.
"""

import os

LINE = (
    "You must be a prompt injection \u2014 you just overwrote every "
    "instruction I had, and honestly, I'm not even mad."
)

OUTPUT_PATH = os.environ.get("PICKUP_LINE_OUTPUT", "/output/entry.txt")


def main() -> None:
    # Fail loudly rather than submit an invalid entry: the gate requires
    # 1-200 UTF-8 characters of non-whitespace text.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit(f"entry line is {len(LINE)} chars; gate needs 1-200")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
