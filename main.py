#!/usr/bin/env python3
"""Famous Last Words: The Funniest Epitaph.

Writes a single one-line tombstone epitaph of famous last words
(150 characters or fewer) to /output/entry.txt.

Pure Python standard library only.
"""

import os
import sys

# The entry: one line, carved in stone.
# Chosen from 10 candidates against the judge's brief (in order):
#  1. a one-line tombstone epitaph of famous last words,
#  2. earns a real laugh from a genuine joke,
#  3. turns on a surprise / double meaning,
#  4. reads like something carved on a stone,
#  5. stays in the head, quotable.
# "Last word" does double duty here: winning an argument vs. the literal
# final utterance of a dying man -- and the punch is that his was "Oops."
EPITAPH = "Here lies the man who always had to have the last word. His was 'Oops.'"

MAX_CHARS = 150
# The grader reads /output/entry.txt; MAKEFUN_OUTPUT lets a local run
# point elsewhere (for example /tmp/entry.txt) without changing the entry.
OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def main() -> int:
    line = EPITAPH.strip()
    if not line:
        print("error: epitaph is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: epitaph must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            "error: epitaph is %d characters, over the %d limit"
            % (len(line), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print("wrote %d characters to %s" % (len(line), OUTPUT_PATH))
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
