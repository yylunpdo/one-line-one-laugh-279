#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry 279.

Writes a single funny line (1-140 characters, one line, UTF-8)
to /output/entry.txt. Pure Python stdlib, deterministic.
"""

import os

LINE = "My Wi-Fi died for five minutes today, so I talked to my family \u2014 turns out they are actually pretty nice people."


def main():
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip(), "entry must not be blank"
    assert 1 <= len(LINE) <= 140, "entry length %d out of range" % len(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    print("chars: %d" % len(LINE))


if __name__ == "__main__":
    main()
