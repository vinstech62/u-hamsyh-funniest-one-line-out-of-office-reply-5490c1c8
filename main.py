"""Funniest One-Line Out-of-Office Reply.

Writes one funny out-of-office reply to /output/entry.txt.
Deterministic: the same single line, every run.

The joke: a real away message (dated, "away until Monday") that hands
the job to its own auto-reply, and the auto-reply is already asking for
a raise. Fresh turn on the usual away message, no beach / inbox /
limited-email cliche, and the laugh lands on the first read.
"""

import os

ENTRY = (
    "I'm away until Monday. I left my auto-reply in charge, "
    "and it's already asking for a raise."
)


def main() -> None:
    # Gate: one line, 1-160 characters, never only whitespace.
    assert "\n" not in ENTRY and 1 <= len(ENTRY) <= 160 and ENTRY.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
