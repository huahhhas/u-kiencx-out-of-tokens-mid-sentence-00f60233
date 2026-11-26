#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence — one-line error message entry.

Prints the line and writes it byte-identical to /output/entry.txt.
"""

import os

LINE = "Error: out of tokens mid-sentence. Insert $0.02 to find out what I was about to sa"
# The line cuts itself off mid-word ("sa" for "say"): the error message
# demonstrates the failure it reports, and the paywall is the punchline.


def main() -> None:
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
