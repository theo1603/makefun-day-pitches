#!/usr/bin/env python3
"""One-line pitch entry for make.fun's "A Day of One-Line Pitches" bounty.

Writes a single persuasive sentence to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set). Python 3.13 standard library only,
no network access, fully deterministic.
"""

import os

ENTRY = (
    "You don't need to learn to code: just describe the app you've always "
    "wanted in plain words and an AI agent builds it for you on make.fun "
    "\u2014 no lessons, no jargon, just your idea becoming a real app you can use."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
