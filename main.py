#!/usr/bin/env python3
"""One-star review of gravity, deadpan, single line.

Writes the review to $MAKEFUN_OUTPUT_DIR/entry.txt.
Python standard library only. Deterministic: same bytes on every run.
"""

import os
from pathlib import Path

REVIEW = "Gravity works fine until I drop my phone, then it aims straight for the one corner that cracks."


def main() -> None:
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / "entry.txt"
    path.write_text(REVIEW, encoding="utf-8")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
