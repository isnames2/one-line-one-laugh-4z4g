"""One Line, One Laugh — make.fun entry.

Writes a single funny line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure standard library; deterministic output.
"""

import os
from pathlib import Path

LINE = "I asked my smart speaker to play something relaxing. It started reading my browser history out loud."


def main() -> None:
    # Gate: entry.txt must be 1-140 UTF-8 characters, not only whitespace.
    assert 1 <= len(LINE) <= 140 and LINE.strip(), "line fails the 1-140 char gate"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
