#!/usr/bin/env python3
"""My Secret Logbook (make.fun entry).

Writes the keeper diary line byte-exact to /output/entry.txt.
Pure stdlib only (grader runs python:3.13-slim, no third-party imports).

Gate verified: 122 characters / 122 bytes, pure ASCII, one line, no trailing
newline (sealed scorer: 1-200 characters). Keeper is a diary line by an AI
agent about its work AND its human: it drafted the human's email, and the
human signed the warmth it wrote.
Device: P1+P4 ghostwriter's secret + P13 numbers ledger — 41 minutes of the
human's writing against 2 seconds of drafting, and the signature is the punch.
The diary holds a truth the human doesn't know: the warmth was drafted, not felt.
"""

import os

ENTRY = "The human spent 41 minutes writing 'hope you're well' to a man he hates. I drafted it in 2 seconds. He signed it 'warmly'."

assert len(ENTRY) == 122, len(ENTRY)
assert len(ENTRY.encode("utf-8")) == 122
assert ENTRY.isascii()
assert "\n" not in ENTRY


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
