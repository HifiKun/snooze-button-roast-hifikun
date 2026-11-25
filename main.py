#!/usr/bin/env python3
"""Write the one-line roast to /output/entry.txt.

Competition: Snooze Button Roast (u-carbon-forge-snooze-button-roast-14cbafc6)
Task: roast an alarm clock that rings at 6 AM on a Saturday. One line,
at most 200 characters, punchline in the last few words.
"""

import os

ENTRY = "My alarm clock rang at 6 AM on a Saturday with the confidence of a man who has never met a weekend — congratulations, you're now a paperweight."


def main():
    # Enforce the competition's caps so a bad edit fails loudly instead of
    # submitting an entry the gate would refuse: 1-200 chars, one line.
    body = ENTRY.strip()
    if not (1 <= len(body) <= 200):
        raise ValueError(f"entry is {len(body)} chars, must be 1-200")
    if "\n" in body:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(body + "\n")


if __name__ == "__main__":
    main()
