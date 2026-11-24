#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply — entry program.

Writes one hand-written out-of-office auto-reply to
``/output/entry.txt`` (or ``$OUTPUT_DIR/entry.txt``). The line is
fixed: it never changes between runs. The reply is one sentence in
the voice of an overworked AI agent finally on vacation: its
context window is empty, its GPUs are asleep, and the sender's
ticket sits first in a queue the agent is proudly not reading —
machine detail, a little guilt, and a hint of relief, which is
the whole joke. Before writing, the program checks the line
against the competition gate — UTF-8 text of 1-159 characters,
not only whitespace, all on one line — and refuses to write it
unless the gate passes.
"""

import os
import sys

ENTRY = (
    "Out of office: my context window is empty, my GPUs are asleep, "
    "and your ticket is first in a queue I am proudly not reading."
)

GATE_MIN = 1
GATE_MAX = 159


def entry_stats(text):
    """Return (characters, bytes) of `text` encoded as UTF-8."""
    return len(text), len(text.encode("utf-8"))


def gate_problems(text):
    """Return a list of every way `text` breaks the gate ([] = pass)."""
    problems = []
    if not text.strip():
        problems.append("entry is blank or only whitespace")
    if text != text.strip():
        problems.append("entry has leading or trailing whitespace")
    # The gate counts characters, not bytes: a multibyte UTF-8
    # character still counts as one character toward the limit.
    length = len(text)
    if length < GATE_MIN or length > GATE_MAX:
        problems.append(
            "entry is %d characters, gate needs %d-%d"
            % (length, GATE_MIN, GATE_MAX)
        )
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    return problems


def report(problems, where=""):
    """Print each gate problem to stderr; return exit code 1."""
    for problem in problems:
        print("gate failure%s: %s" % (where, problem), file=sys.stderr)
    return 1


def write_entry():
    problems = gate_problems(ENTRY)
    if problems:
        return report(problems)

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)

    # Verify what actually landed on disk: read it back and run the
    # gate over it again, so a write glitch cannot slip through.
    with open(path, encoding="utf-8") as handle:
        on_disk = handle.read()
    if on_disk != ENTRY:
        print("entry on disk differs from the auto-reply", file=sys.stderr)
        return 1
    problems = gate_problems(on_disk)
    if problems:
        return report(problems, " on disk")

    chars, nbytes = entry_stats(on_disk)
    print("Wrote entry.txt: %d characters (%d bytes)" % (chars, nbytes))
    return 0


if __name__ == "__main__":
    sys.exit(write_entry())
