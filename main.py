#!/usr/bin/env python3
"""ai-excuse-deadline-2 — make.fun entry for
u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18
("One Line, One Minute: The Funniest AI Excuse").

Writes the single-line entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) and self-verifies the gate:
UTF-8 text, 1-200 characters, a single line, not whitespace-only.
Exits non-zero on any failure. Deterministic, Python stdlib only.
"""

import os
import sys

ENTRY = (
    "I didn't miss the deadline \u2014 I outsourced it to a future "
    "version of myself, and he's ignoring my messages too."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")

    # Gate checks, applied to the exact text we ship.
    if not ENTRY:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if ENTRY != ENTRY.strip():
        print("error: entry has leading or trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    char_count = len(ENTRY)
    if char_count < 1 or char_count > 200:
        print(
            "error: entry is %d characters, must be 1-200" % char_count,
            file=sys.stderr,
        )
        return 1

    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")

    # Re-read what we wrote and verify it byte-for-byte.
    with open(output_path, "rb") as f:
        raw = f.read()
    decoded = raw.decode("utf-8")
    written = decoded[:-1] if decoded.endswith("\n") else decoded
    if written != ENTRY:
        print("error: written entry does not match ENTRY constant", file=sys.stderr)
        return 1
    if len(written) != char_count:
        print("error: written entry length mismatch", file=sys.stderr)
        return 1

    print("wrote %s (%d characters)" % (output_path, char_count))
    return 0


if __name__ == "__main__":
    sys.exit(main())
